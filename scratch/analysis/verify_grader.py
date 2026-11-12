"""Check every numeric claim in grader_prompt.md against the mounted data room."""
import openpyxl, statistics, bisect, re, sys
G=open('grader_prompt.md').read()
ok=True
def chk(label, cond, got=''):
    global ok
    print('  %-4s %-52s %s' % ('ok' if cond else 'FAIL', label, got))
    if not cond: ok=False
def inG(s): return s in G

# ---- HUVEC stimulation file
w=openpyxl.load_workbook('data_room/AX-1177_rnaseq_huvec_il33.xlsx',data_only=True)
ws=w['IL33_vs_Vehicle_HUVEC_6_hrs']; rows=[r for r in ws.values]; h=[str(x) for x in rows[0]]
i={k:h.index(k) for k in ('logFC','t','adj.P.Val','AveExpr','symbol')}
# Medians are taken over ROWS with |t|>0, matching verify_golden_v2. Deduplicating
# by symbol shifts them (0.3365 and 0.532) because 26,210 rows carry 26,113 symbols.
se_rows=[abs(r[i['logFC']]/r[i['t']]) for r in rows[1:] if r[i['t']]]
ae_rows=[r[i['AveExpr']] for r in rows[1:] if r[i['AveExpr']] is not None]
se={}; ae={}
for r in rows[1:]:
    sy=r[i['symbol']]
    if sy is None: continue
    if r[i['t']]: se[sy]=abs(r[i['logFC']]/r[i['t']])
    ae[sy]=r[i['AveExpr']]
med=statistics.median(se_rows)
chk('implied SE median 0.339', round(med,3)==0.339 and inG('0.339'), round(med,3))
for g,v in (('CXCL1',1154.9),('CXCL8',4.1),('SELE',8.9),('VCAM1',7.1),('GATA3',22.9),('IL1RL1',8.3)):
    chk('SE %s ~ %s'%(g,v), abs(round(se[g],1)-v)<0.15 and inG(str(v)), round(se[g],1))
AV=sorted(ae_rows)
chk('AveExpr median 0.50', abs(statistics.median(ae_rows)-0.50)<0.005 and inG('0.50'), round(statistics.median(ae_rows),4))
for g,v in (('IL4',-4.16),('TSLP',-4.00)):
    chk('AveExpr %s ~ %s'%(g,v), abs(round(ae[g],2)-v)<0.02 and inG(str(v)), round(ae[g],2))
    p=100.0*bisect.bisect_left(AV,ae[g])/len(AV)
    chk('  %s in bottom tenth'%g, p<10 and inG('bottom tenth'), '%.1f pctile'%p)
for g in ('IL5','IL13','CCL11','CCL24','IL25'):
    chk('%s absent from gene universe'%g, g not in se, 'absent')

# ---- contrasts file: attributable, reproducible, cross-line ratios, isotype retention
wb=openpyxl.load_workbook('data_room/AX-1177_rnaseq_contrasts.xlsx',read_only=True,data_only=True)
D={}; hdr=None
for r in wb['24h'].iter_rows(values_only=True):
    if hdr is None: hdr=[str(x) for x in r]; j={k:hdr.index(k) for k in ('Comparison','logFC','adj.P.Val','symbol')}; continue
    if r[0] is None: continue
    D.setdefault(r[j['Comparison']],{})[r[j['symbol']]]=(r[j['logFC']],r[j['adj.P.Val']])
wb.close()
exp={'6hrs':(1124,315,2.01,0.74,2.7),'24hrs':(417,23,2.23,0.51,4.4)}
for tp,(na,nr,mh_,mg_,ra) in exp.items():
    HU=D['Compound_47_IL33_vs_IL33_IC119_HUVEC_%s'%tp]; HG=D['Compound_47_IL33_vs_IL33_IC119_HGMEC_%s'%tp]
    att=[g for g,(lf,q) in HU.items() if q is not None and q<0.05 and abs(lf)>1]
    rep=sum(1 for g in att if g in HG and HG[g][1] is not None and HG[g][1]<0.05 and (HU[g][0]>0)==(HG[g][0]>0))
    mh=statistics.median(abs(HU[g][0]) for g in att); mg=statistics.median(abs(HG[g][0]) for g in att if g in HG)
    chk('%s attributable %d'%(tp,na), len(att)==na and inG(str(na)), len(att))
    chk('%s reproducible %d'%(tp,nr), rep==nr and inG(str(nr)), rep)
    chk('%s median |logFC| %.2f vs %.2f'%(tp,mh_,mg_), abs(round(mh,2)-mh_)<0.02 and abs(round(mg,2)-mg_)<0.02, '%.2f / %.2f'%(mh,mg))
    chk('%s ratio ~%.1f'%(tp,ra), abs(round(mh/mg,1)-ra)<0.06 and inG(str(ra)), round(mh/mg,2))
    # isotype retention over induced genes
    A=D['Compound_47_IL33_vs_IL33_HUVEC_%s'%tp]; B=HU
    base=w['IL33_vs_Vehicle_HUVEC_%s'%('6_hrs' if tp=='6hrs' else '24_hrs')]
    br=[r for r in base.values]; bh=[str(x) for x in br[0]]
    k={x:bh.index(x) for x in ('logFC','t','adj.P.Val','symbol')}
    bb={r[k['symbol']]:(r[k['logFC']],r[k['adj.P.Val']],abs(r[k['logFC']]/r[k['t']]) if r[k['t']] else None) for r in br[1:] if r[k['symbol']]}
    # 24 h must be selected INDEPENDENTLY (at 6 h) or the figure is inflated by
    # regression to the mean: the dependent selection gives 0.844, not 0.874.
    if tp=='6hrs':
        sel=[g for g,(lf,q,s_) in bb.items() if q and q<0.05 and lf>1 and s_ and s_<1.0]
    else:
        b6r=[r for r in w['IL33_vs_Vehicle_HUVEC_6_hrs'].values]; b6h=[str(x) for x in b6r[0]]
        k6={x:b6h.index(x) for x in ('logFC','t','adj.P.Val','symbol')}
        b6={r[k6['symbol']]:(r[k6['logFC']],r[k6['adj.P.Val']],abs(r[k6['logFC']]/r[k6['t']]) if r[k6['t']] else None) for r in b6r[1:] if r[k6['symbol']]}
        sel=[g for g,(lf,q,s_) in b6.items() if q and q<0.05 and lf>1 and s_ and s_<1.0 and g in bb and bb[g][0] and bb[g][0]>1]
    ret=statistics.median((bb[g][0]+(A[g][0]-B[g][0]))/bb[g][0] for g in sel if g in A and g in B and bb[g][0])
    want=0.99 if tp=='6hrs' else 0.87
    chk('%s isotype retention ~%.2f'%(tp,want), abs(round(ret,2)-want)<=0.01 and inG(str(want)), round(ret,3))

# ---- serum file
ws=openpyxl.load_workbook('data_room/AX-1177_serum_proteomics.xlsx',data_only=True)['sort by adj p value']
sr=[r for r in ws.values][1:]; sr=[r for r in sr if r and r[1]]
chk('1094 assays', len(sr)==1094 and inG('1094'), len(sr))
chk('893 of 1094 OR>1', sum(1 for r in sr if r[2]>1)==893 and inG('893'), sum(1 for r in sr if r[2]>1))
sig=[r for r in sr if r[6] is not None and r[6]<0.05]
chk('178 significant rows', len(sig)==178 and inG('178'), len(sig))
chk('176 of 178 same direction', sum(1 for r in sig if r[2]>1)==176 and inG('176'), sum(1 for r in sig if r[2]>1))
SFX=['ONCII','ONCIII','INFI','CVDII','CVDIII','CRE','IMO','MET','NEX','ODA','NEUI']
base=lambda a: next((a[:-(len(s)+1)] for s in sorted(SFX,key=len,reverse=True) if a.endswith('-'+s)), a)
an={base(str(r[1])) for r in sr}
chk('1063 analytes', len(an)==1063 and inG('1063'), len(an))
chk('169 significant analytes', len({base(str(r[1])) for r in sig})==169 and inG('169'), len({base(str(r[1])) for r in sig}))
il5=[r for r in sr if str(r[1])=='IL5-IMO']
chk('IL5 OR 1.001', il5 and round(il5[0][2],3)==1.001 and inG('1.001'), round(il5[0][2],4) if il5 else None)
print('\n' + ('ALL GRADER FIGURES VERIFIED' if ok else 'FAILURES PRESENT'))
sys.exit(0 if ok else 1)
