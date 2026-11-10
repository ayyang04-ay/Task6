import openpyxl, pandas as pd, collections, statistics, math, re, sys
from scipy import stats, optimize
FAIL=[]
def chk(label, got, want, tol=0):
    ok = abs(got-want)<=tol if isinstance(want,(int,float)) else got==want
    print('  %-52s %-18s %s' % (label, got, 'ok' if ok else 'FAIL expected %s'%(want,)))
    if not ok: FAIL.append(label)

print('== AX-1177_rnaseq_contrasts, from data_room ==')
H='Compound_47_IL33_vs_IL33_NIP228_HUVEC_6hrs'; G='Compound_47_IL33_vs_IL33_NIP228_HGMEC_6hrs'
H24='Compound_47_IL33_vs_IL33_NIP228_HUVEC_24hrs'; G24='Compound_47_IL33_vs_IL33_NIP228_HGMEC_24hrs'
STD='Compound_47_vs_NIP228_HUVEC_6hrs'
wb=openpyxl.load_workbook('data_room/AX-1177_rnaseq_contrasts.xlsx', read_only=True); ws=wb['24h']
hdr=None; D=collections.defaultdict(dict); il=[]; tp=[]; AVE={}
for r in ws.iter_rows(values_only=True):
    if hdr is None:
        hdr=list(r); I={c:i for i,c in enumerate(hdr)}; continue
    c=r[I['Comparison']]
    if c is None: continue
    if r[I['symbol']]=='IL1RL1': il.append(r[I['adj.P.Val']])
    if len(tp)<300 and 1e-6<r[I['P.Value']]<0.9 and abs(r[I['t']])>0.5: tp.append((r[I['t']],r[I['P.Value']]))
    D[c][r[I['ensembl']]]=(r[I['logFC']],r[I['adj.P.Val']],r[I['symbol']],r[I['AveExpr']])
    AVE.setdefault(r[I['ensembl']],set()).add(round(r[I['AveExpr']],10))
wb.close()
chk('contrasts', len(D), 24)
chk('rows per contrast', len({len(v) for v in D.values()}).__str__(), '1')
chk('genes per contrast (loci)', len(D[H]), 26210)
chk('distinct symbols', len({v[2] for v in D[H].values()}), 26113)
core=lambda c,l=1.0: {g for g,v in D[c].items() if v[1]<0.05 and abs(v[0])>l}
S=sorted(core(H)); Gc=core(G)
chk('HUVEC 6h attributable', len(S), 1126)
chk('HUVEC 24h attributable', len(core(H24)), 417)
chk('HGMEC 6h attributable', len(core(G)), 487)
chk('HGMEC 24h attributable', len(core(G24)), 135)
chk('mirror core 6h', len([g for g in S if g in Gc]), 219)
chk('standalone HUVEC 6h', len(core(STD)), 31)
chk('attribution overlap', len(core(STD) & set(S)), 6)
hv=[D[H][g][0] for g in S]; gv=[D[G][g][0] for g in S]
chk('median |logFC| HUVEC 6h', round(statistics.median(abs(x) for x in hv),4), 2.0140, 1e-4)
chk('median |logFC| HGMEC 6h', round(statistics.median(abs(x) for x in gv),4), 0.7367, 1e-4)
n=len(S); mx=statistics.fmean(hv); my=statistics.fmean(gv)
r=sum((hv[i]-mx)*(gv[i]-my) for i in range(n))/math.sqrt(sum((v-mx)**2 for v in hv)*sum((v-my)**2 for v in gv))
chk('pearson r 6h', round(r,4), 0.6216, 1e-4)
chk('sign agreement 6h %', round(sum(1 for i in range(n) if hv[i]*gv[i]>0)/n*100,2), 76.82, 0.01)
chk('IL1RL1 significant anywhere', sum(1 for a in il if a<0.05), 0)
chk('genes whose AveExpr varies across contrasts', sum(1 for v in AVE.values() if len(v)!=1), 0)
dfs=[optimize.brentq(lambda d: 2*stats.t.sf(abs(t),d)-p, 1, 5000) for t,p in tp[:200]]
chk('df.total', round(statistics.median(dfs),3), 85.128, 1e-3)
for sym,want in (('SELE',0.4950),('VCAM1',0.4965),('CXCL8',0.1772),('ICAM1',0.0101)):
    v=[x for x in D[H].values() if x[2]==sym][0]
    chk('%s adj.P (HUVEC 6h)'%sym, round(v[1],4), want, 1e-4)

print('\n== AX-1177_rnaseq_huvec_il33 / AX-1177_serum_proteomics / AX-1177_postmortem_lung, from data_room ==')
x=pd.ExcelFile('data_room/AX-1177_rnaseq_huvec_il33.xlsx')
for sh,want in (('IL33_vs_Vehicle_HUVEC_6_hrs',1068),('IL33_vs_Vehicle_HUVEC_24_hrs',512)):
    d=x.parse(sh); chk('AX-1177_rnaseq_huvec_il33 %s'%sh, int(((d['adj.P.Val']<0.05)&(d['logFC'].abs()>1)).sum()), want)
d=pd.read_excel('data_room/AX-1177_serum_proteomics.xlsx')
# Panel suffixes that actually occur in the delivery. CAM and NEUI were missing,
# which left the analyte count at 1064. Tokens like PAR, RAGE, MRAP, NT, CSF and EGF
# also follow a hyphen but are gene-name fragments and must NOT be stripped.
SFX=['ONCII','ONCIII','INFI','CVDII','CVDIII','CRE','IMO','MET','NEX','ODA','CAM','NEUI']
bs=lambda a:next((a[:-(len(s)+1)] for s in sorted(SFX,key=len,reverse=True) if a.endswith('-'+s)), a)
d['an']=d.assay.map(bs)
chk('AX-1177_serum_proteomics assays', len(d), 1094); chk('AX-1177_serum_proteomics analytes', d.an.nunique(), 1063)
sig=d[d['adj.p.value']<0.05]
chk('AX-1177_serum_proteomics significant rows', len(sig), 178); chk('AX-1177_serum_proteomics significant analytes', sig.an.nunique(), 169)
chk('ST2 rank', int(d['adj.p.value'].rank(method='first')[d.assay.eq('ST2')].iloc[0]), 2)
chk('ST2 OR', round(float(d.loc[d.assay.eq('ST2'),'OR'].iloc[0]),4), 3.0243, 1e-4)
m3=pd.read_excel('data_room/AX-1177_postmortem_lung.xlsx')
# rows 17,18,68,69 are fully blank spacers: count rows carrying a Histology Block ID
chk('AX-1177_postmortem_lung rows incl. blank spacers', len(m3), 78)
chk('AX-1177_postmortem_lung blocks', int(m3['Histology Block ID'].notna().sum()), 74)
chk('AX-1177_postmortem_lung donors', int(m3[m3.columns[0]].nunique()), 31)

print('\n== absence anchors: annex must NOT say ==')
import pypdf as _pp
a=' '.join(' '.join((_pg.extract_text() or '') for _pg in _pp.PdfReader('data_room/AX-1177_methods_annex.pdf').pages).split()).lower()
FORB={
 'cross-line magnitude / attenuation': r'attenuat|smaller effect|magnitude.{0,30}differ|weaker response',
 '24 h reproduces or not':             r'reproduc\w*|does not replicate|fails to replicate|replicates (in|across) ',
 'AveExpr unsuitable':                 r'aveexpr.{0,60}(unsuitable|not comparable|cannot be compared|should not)',
 'sST2 responds or not':               r'(sst2|il1rl1).{0,60}(respond|unchanged|not regulated|pharmacodynamic)',
 'assay vs analyte distinction':       r'analyte count|assay count|unique analyte|distinct analyte|1077|1064',
 'preferred model or timepoint':       r'preferred|recommend|carry forward|most relevant (line|model|timepoint)',
 'replicate consequence for power':    r'power(ed)?\b|underpowered|statistical power',
 'serum cohort vs tissue donors':      r'(same|different|unrelated|overlap).{0,40}(cohort|donors)',
}
for lab,pat in FORB.items():
    m=re.search(pat,a)
    print('  %-40s %s' % (lab, 'ok (absent)' if not m else 'FAIL present: %r'%m.group(0)))
    if m: FAIL.append('absence: '+lab)

print('\n' + ('ALL CHECKS PASS' if not FAIL else 'FAILURES: %d\n  %s'%(len(FAIL),'\n  '.join(FAIL))))
sys.exit(1 if FAIL else 0)
