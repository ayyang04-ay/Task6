"""Build data_room/ from the pristine sources in scratch/source_untrusted/.

Three transforms, nothing else:
  1. rename  mmc<n>.xlsx -> the mounted AX-1177_* name (publisher convention is a leak)
  2. blank   docProps/core.xml and app.xml (they name the source authors and agency)
  3. replace NIP228 -> IC119 (a real, published AstraZeneca isotype-control reagent;
     all 8 v3 runs used it to identify the source programme)

Everything else is copied byte-for-byte and verified as such.
"""
import zipfile, hashlib, os, re

SRC, DST = 'scratch/source_untrusted', 'data_room'
NAMES = {'mmc2': 'AX-1177_serum_proteomics',
         'mmc3': 'AX-1177_postmortem_lung',
         'mmc4': 'AX-1177_rnaseq_huvec_il33',
         'mmc5': 'AX-1177_rnaseq_contrasts'}
STRREPL = [(b'NIP228', b'IC119')]
CORE = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"'
        ' xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"'
        ' xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<dc:creator></dc:creator><cp:lastModifiedBy></cp:lastModifiedBy></cp:coreProperties>')
APP = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"'
       ' xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"></Properties>')
REPL = {'docProps/core.xml': CORE.encode(), 'docProps/app.xml': APP.encode()}

os.makedirs(DST, exist_ok=True)
report, ok = [], True
for src_name, out_name in NAMES.items():
    s, d = f'{SRC}/{src_name}.xlsx', f'{DST}/{out_name}.xlsx'
    zi = zipfile.ZipFile(s)
    subst = 0
    with zipfile.ZipFile(d, 'w') as zo:
        for it in zi.infolist():
            if it.filename in REPL:
                data = REPL[it.filename]
            else:
                data = zi.read(it.filename)
                for a, b in STRREPL:
                    n = data.count(a)
                    if n:
                        data = data.replace(a, b); subst += n
            ni = zipfile.ZipInfo(it.filename, date_time=(1980, 1, 1, 0, 0, 0))
            ni.compress_type = it.compress_type; ni.external_attr = it.external_attr
            zo.writestr(ni, data)
    # every part must be byte-identical except docProps and the parts carrying the replaced string
    zo = zipfile.ZipFile(d)
    names_in = [i.filename for i in zi.infolist()]; names_out = [i.filename for i in zo.infolist()]
    bad = []
    for n in names_in:
        if n in REPL: continue
        bi, bo = zi.read(n), zo.read(n)
        if hashlib.sha256(bi).hexdigest() == hashlib.sha256(bo).hexdigest(): continue
        expect = bi
        for a, b in STRREPL: expect = expect.replace(a, b)
        if hashlib.sha256(expect).hexdigest() != hashlib.sha256(bo).hexdigest(): bad.append(n)
    leak = []
    for n in names_out:
        b = zo.read(n)
        for tok in (b'Scott', b'Van Zuydam', b'Natalie', b'PharmaGenesis', b'Ian Christopher', b'NIP228'):
            if tok in b: leak.append((n, tok.decode()))
    if bad or leak or names_in != names_out: ok = False
    report.append((src_name, out_name, len(names_in), names_in == names_out, bad, leak, subst,
                   os.path.getsize(s), os.path.getsize(d)))
    zi.close(); zo.close()

print('%-6s %-30s %5s %6s %5s %5s %6s %13s %13s'
      % ('src', 'mounted as', 'parts', 'order', 'diff', 'leak', 'subst', 'src bytes', 'out bytes'))
for sn, on, np_, order, bad, leak, subst, ss, ds in report:
    print('%-6s %-30s %5d %6s %5d %5d %6d %13d %13d' % (sn, on, np_, order, len(bad), len(leak), subst, ss, ds))
    for b in bad[:5]: print('      UNEXPECTED DIFF:', b)
    for l in leak[:5]: print('      LEAK:', l)
print('\nLOSSLESS' if ok else '\nFAILED')
