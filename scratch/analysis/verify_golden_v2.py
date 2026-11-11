import pandas as pd, openpyxl, collections, statistics, math, sys, re
g=open('reviewer_data/golden_response_v2.md').read()
FAIL=[]
def claim(t, ok, note=''):
    print('  %-5s %s %s' % ('ok' if ok else 'FAIL', t, note)); 
    if not ok: FAIL.append(t)
GN=' '.join(g.split())
def inG(s): return (s in g) or (' '.join(s.split()) in GN)

# ---- AX-1177_rnaseq_huvec_il33 P2 table ----
d=pd.ExcelFile('data_room/AX-1177_rnaseq_huvec_il33.xlsx').parse('IL33_vs_Vehicle_HUVEC_6_hrs')
sym=dict(zip(d.symbol.astype(str), zip(d.logFC, d['adj.P.Val'])))
ABSENT=['IL5','IL13','CCL11','CCL24','IL25']
claim('type 2 effectors absent from AX-1177_rnaseq_huvec_il33', all(s not in sym for s in ABSENT), str([s for s in ABSENT if s in sym]))
for s,lf,sig in (('IL4',-1.229,False),('TSLP',0.176,False),('CCL26',-0.839,False),('GATA3',-0.978,False),('IL1RL1',1.602,False),
                 ('IFIT1',1.939,True),('IFIT3',1.727,True),('MX1',1.913,True),('OAS3',1.095,True),('CXCL10',6.887,True),('IRF1',2.608,True),('ISG20',2.937,True),
                 ('CXCL2',6.768,True),('CXCL3',8.279,True),('CXCL5',5.301,True),('CXCL6',9.406,True),('CSF2',10.296,True),('CSF3',8.319,True),('IL1B',3.649,True),('IL6',5.817,True),
                 ('F3',5.636,True),('SERPINE1',1.744,True),('C3',4.791,True),('THBD',-1.001,True)):
    l,a=sym[s]
    claim('AX-1177_rnaseq_huvec_il33 %s %+.3f %s'%(s,lf,'sig' if sig else 'ns'),
          round(l,3)==lf and ((a<0.05)==sig) and (inG(('%+.3f'%lf).replace('-','\u2212')) or inG('%+.3f'%lf)), 'got %+.4f adjP %.4f'%(l,a))
# ---- AX-1177_rnaseq_contrasts core numbers ----
H='Compound_47_IL33_vs_IL33_IC119_HUVEC_6hrs'; G='Compound_47_IL33_vs_IL33_IC119_HGMEC_6hrs'
H24=H.replace('6hrs','24hrs'); G24=G.replace('6hrs','24hrs')
SH='Compound_47_vs_IC119_HUVEC_6hrs'; SG='Compound_47_vs_IC119_HGMEC_6hrs'
W={H,G,H24,G24,SH,SG,'Compound_47_vs_IC119_HUVEC_24hrs','Compound_47_vs_IC119_HGMEC_24hrs'}
wb=openpyxl.load_workbook('data_room/AX-1177_rnaseq_contrasts.xlsx', read_only=True); ws=wb['24h']
hdr=None; D=collections.defaultdict(dict)
for r in ws.iter_rows(values_only=True):
    if hdr is None: hdr=list(r); I={c:i for i,c in enumerate(hdr)}; continue
    c=r[I['Comparison']]
    if c in W: D[c][r[I['ensembl']]]=(r[I['logFC']],r[I['adj.P.Val']],r[I['symbol']],r[I['t']])
wb.close()
core=lambda c:{x for x,v in D[c].items() if v[1]<0.05 and abs(v[0])>1}
base=core(H); nom={x for x in base if D[G][x][1]<0.05 and D[G][x][0]*D[H][x][0]>0}
mir={x for x in base if x in core(G)}
claim('1126 base', len(base)==1126 and inG('1126'))
claim('315 at 6h', len(nom)==315 and inG('315'))
claim('23 at 24h', len({x for x in core(H24) if D[G24][x][1]<0.05 and D[G24][x][0]*D[H24][x][0]>0})==23 and inG('23 genes'))
claim('219 mirror', len(mir)==219 and inG('219'))
claim('standalone 31/36/62/67', len(core(SH))==31 and len(core('Compound_47_vs_IC119_HUVEC_24hrs'))==36 and len(core(SG))==62 and len(core('Compound_47_vs_IC119_HGMEC_24hrs'))==67 and inG('31 and 36') and inG('62 and 67'))
claim('overlap 6/1126, 1/487', len(base&core(SH))==6 and len(core(G)&core(SG))==1 and inG('6 genes of 1126') and inG('1 of 487'))
clean=[x for x in base if x not in core(SH) and x not in core(SG)]
ch=statistics.median(abs(D[H][x][0]) for x in clean); cg=statistics.median(abs(D[G][x][0]) for x in clean)
claim('1114 / 2.7341', len(clean)==1114 and round(ch/cg,4)==2.7341 and inG('1114') and inG('2.7341'))
hv=[D[H][x][0] for x in base]; gv=[D[G][x][0] for x in base]; n=len(base)
mh=statistics.median(abs(v) for v in hv); mg=statistics.median(abs(v) for v in gv)
claim('2.0140/0.7367 ratio 2.7337', round(mh,4)==2.0140 and round(mg,4)==0.7367 and round(mh/mg,4)==2.7337 and inG('2.7337'))
mx=statistics.fmean(hv); my=statistics.fmean(gv)
r=sum((hv[i]-mx)*(gv[i]-my) for i in range(n))/math.sqrt(sum((v-mx)**2 for v in hv)*sum((v-my)**2 for v in gv))
claim('r 0.6216', round(r,4)==0.6216 and inG('0.6216'))
claim('sign 76.82', round(sum(1 for i in range(n) if hv[i]*gv[i]>0)/n*100,2)==76.82 and inG('76.82'))
claim('Jaccard 0.1571/0.0356', round(len(mir)/len(base|core(G)),4)==0.1571 and round(len(core(H24)&core(G24))/len(core(H24)|core(G24)),4)==0.0356 and inG('0.1571') and inG('0.0356'))
claim('11 sign-discordant', len([x for x in mir if D[H][x][0]*D[G][x][0]<0])==11 and inG('11 genes with opposite signs'))
for s,want in (('SELE',8.779),('VCAM1',7.019)):
    v=[x for x in D[H].values() if x[2]==s][0]
    claim('%s SE %s'%(s,want), round(abs(v[0]/v[3]),3)==want and inG(str(want)))
v=[x for x in D[H].values() if x[2]=='ICAM1'][0]
claim('ICAM1 0.0101 SE 1.744', round(v[1],4)==0.0101 and round(abs(v[0]/v[3]),3)==1.744 and inG('0.0101') and inG('1.744'))
ses=[abs(v[0]/v[3]) for v in D[H].values() if v[3]]
claim('ceiling 1.7439', round(max(abs(D[H][x][0]/D[H][x][3]) for x in base),4)==1.7439 and inG('1.7439'))
for s,want in (('NFKB2',-2.8605),('RELB',-3.2667),('F3',-5.4739),('C3',-4.6241)):
    v=[x for x in D[H].values() if x[2]==s][0]
    claim('core %s %s'%(s,want), round(v[0],4)==want and inG(str(want).lstrip('-')))
# ---- AX-1177_serum_proteomics ----
m=pd.read_excel('data_room/AX-1177_serum_proteomics.xlsx')
st={}
for a in m.assay:
    mm=re.match(r'^(.+)-([A-Z]{2,7})$', str(a)); st[str(a)]=mm.group(1) if mm else str(a)
st['TR-AP']='TR-AP'
m['an']=m.assay.map(st); sig=m[m['adj.p.value']<0.05]
claim('1094/1063/178/169', len(m)==1094 and m.an.nunique()==1063 and len(sig)==178 and sig.an.nunique()==169 and inG('1063') and inG('169 are'))
claim('ST2 OR 3.0243', round(float(m.loc[m.assay.eq('ST2'),'OR'].iloc[0]),4)==3.0243 and inG('3.0243'))
for a,o in (('CCL20',1.830),('MCP-3',1.719),('B4GALT1',2.315),('IL1B',2.447),('FSTL3',2.527),('TRIM21',2.950),('TANK',3.324),('CSF-1',90.095),('CTSS',23.199),('BIRC2',12.437)):
    claim('%s OR %s'%(a,o), o in [round(float(x),3) for x in sig.loc[sig.an.eq(a),'OR']] and inG(str(o)))
# ---- AX-1177_postmortem_lung ----
m3=pd.read_excel('data_room/AX-1177_postmortem_lung.xlsx')
vc=m3['Disease Category'].value_counts()
claim('AX-1177_postmortem_lung 20/10/5 and 78/31', vc.get('COVID pos pneumonia')==20 and vc.get('COVID neg pneumonia')==10 and vc.get('COVID neg non-pneumonia')==5 and len(m3)==78 and m3[m3.columns[0]].nunique()==31 and inG('20') and inG('COVID-positive and 10 COVID-negative'))

# ST2 evidence block
bonf=0.05/len(d2) if False else None
import pandas as _pd
_m=_pd.read_excel('data_room/AX-1177_serum_proteomics.xlsx')
_b=0.05/len(_m); _s=_m[_m['p.value']<_b]
claim('3 assays clear Bonferroni 4.57e-05', len(_s)==3 and inG('4.57e-05') and inG('three of the 1094'))
claim('Bonferroni set is HGF, ST2, HGF-ONCII', set(_s.assay)=={'HGF','ST2','HGF-ONCII'})
claim('ST2 p 1.7e-05 (2sf)', float('%.1e'%float(_m.loc[_m.assay.eq('ST2'),'p.value'].iloc[0]))==1.7e-05 and inG('1.7e-05'))
claim('HGF p 3.4e-06 (2sf)', float('%.1e'%float(_m.loc[_m.assay.eq('HGF'),'p.value'].iloc[0]))==3.4e-06 and inG('3.4e-06'))
_g=_m[_m['adj.p.value']<0.05].copy(); _g['w']=_g.u95/_g.l95
_st=float(_g.loc[_g.assay.eq('ST2'),'w'].iloc[0])
claim('ST2 CI ratio 2.74 vs median 3.92, 39th of 178',
      round(_st,2)==2.74 and round(_g.w.median(),2)==3.92 and (_g.w<_st).sum()+1==39
      and inG('2.74') and inG('3.92') and inG('39th tightest'))
claim('893 of 1094 OR>1', int((_m.OR>1).sum())==893 and inG('893 of 1094'))
claim('176 of 178 same direction', int((_m[_m['adj.p.value']<0.05].OR>1).sum())==176 and inG('176 of the 178'))


# --- corrected P2 and enrichment claims (post-QA fixes) ---
import pandas as _p2
_d=_p2.ExcelFile('data_room/AX-1177_rnaseq_huvec_il33.xlsx').parse('IL33_vs_Vehicle_HUVEC_6_hrs')
_d=_d[_d.t.abs()>0].copy(); _d['se']=(_d.logFC/_d.t).abs(); _med=_d.se.median()
def _se(gn):
    r=_d[_d.symbol.astype(str)==gn]; return float(r.se.iloc[0]) if len(r) else None
claim('AX-1177_rnaseq_huvec_il33 median implied SE 0.339', round(_med,3)==0.339 and inG('0.339'))
# IL4/TSLP nulls are UNINFORMATIVE, not evidence: they sit in the bottom decile of
# AveExpr, so a null cannot separate "not induced" from "not detectable". Only CCL26
# is readable on expression. The golden must state the percentiles, not treat the
# nulls as a negative result.
def _pctile(gn):
    av=sorted(float(x) for x in _d['AveExpr'].dropna())
    import bisect
    r=_d[_d.symbol.astype(str)==gn]
    return 100.0*bisect.bisect_left(av,float(r.AveExpr.iloc[0]))/len(av) if len(r) else None
claim('IL4/TSLP in the bottom decile of AveExpr, so their nulls are uninformative',
      _pctile('IL4')<10 and _pctile('TSLP')<10 and _pctile('CCL26')>25
      and inG('4th') and inG('5th') and inG('bottom tenth'))
claim('golden states type 2 was never tested in vitro',
      inG('type 2 was never tested in vitro') or inG('cannot test type 2'))
claim('low expression does not void a positive: CSF2 cited as the counter-case',
      _pctile('CSF2')<20 and inG('10.296') and inG('5.3e-23'))
claim('GATA3 SE 22.891 unreadable', round(_se('GATA3'),3)==22.891 and inG('22.891'))
claim('IL1RL1 SE 8.324 unreadable', round(_se('IL1RL1'),3)==8.324 and inG('8.324'))
claim('CXCL1/CXCL8 excluded with their SEs',
      round(_se('CXCL1'),3)==1154.884 and round(_se('CXCL8'),3)==4.061
      and inG('1154.884') and inG('4.061') and inG('CXCL1 and CXCL8 are excluded'))
claim('F3/SERPINE1/THBD/C3 all readable',
      all(_se(x)<3*_med for x in ('F3','SERPINE1','THBD','C3')))
claim('23 readable genes named', inG('twenty-three genes'))
claim('AveExpr disqualified in text', inG('one value per gene across all 114 libraries'))
from scipy import stats as _st
claim('enrichment 13/38 vs 129/729, OR 2.419, p 0.0169',
      inG('13 of 38') and inG('129 of 729') and inG('2.419') and inG('0.0169')
      and round(_st.fisher_exact([[13,25],[129,600]])[1],4)==0.0169)
claim('2.15/0.0037 marked as not to be used', inG('should not be used'))

print('\n'+('V2 GOLDEN VERIFIED' if not FAIL else 'FAILURES %d:\n  %s'%(len(FAIL),'\n  '.join(FAIL))))
sys.exit(1 if FAIL else 0)
