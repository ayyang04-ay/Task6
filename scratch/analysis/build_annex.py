"""Render the methods annex markdown to the PDF mounted in the data room."""
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

SRC, OUT = sys.argv[1], sys.argv[2]
ss = getSampleStyleSheet()
body = ParagraphStyle('body', parent=ss['BodyText'], fontName='Helvetica', fontSize=9, leading=12, spaceAfter=5)
h1 = ParagraphStyle('h1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=8)
h2 = ParagraphStyle('h2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=11, leading=14, spaceBefore=9, spaceAfter=5)
cell = ParagraphStyle('cell', parent=body, fontSize=8, leading=10, spaceAfter=0)
cellh = ParagraphStyle('cellh', parent=cell, fontName='Helvetica-Bold')

def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'`([^`]+)`', r'<font face="Courier">\1</font>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', t)
    return t

lines = open(SRC).read().split('\n')
flow, i = [], 0
while i < len(lines):
    L = lines[i]
    if L.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1]):
        rows = []
        hdr = [c.strip() for c in L.strip('|').split('|')]
        i += 2
        while i < len(lines) and lines[i].startswith('|'):
            rows.append([c.strip() for c in lines[i].strip('|').split('|')]); i += 1
        ncol = len(hdr)
        data = [[Paragraph(inline(c), cellh) for c in hdr]] + \
               [[Paragraph(inline(c), cell) for c in (r + [''] * ncol)[:ncol]] for r in rows]
        avail = A4[0] - 36 * mm
        t = Table(data, colWidths=[avail / ncol] * ncol, hAlign='LEFT')
        t.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#999999')),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#eeeeee')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 3), ('RIGHTPADDING', (0, 0), (-1, -1), 3),
            ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
        flow += [Spacer(1, 4), t, Spacer(1, 6)]
        continue
    s = L.strip()
    if s == '---':
        flow.append(HRFlowable(width='100%', thickness=0.4, color=colors.HexColor('#bbbbbb'),
                               spaceBefore=5, spaceAfter=5))
    elif s.startswith('## '):
        flow.append(Paragraph(inline(s[3:]), h2))
    elif s.startswith('# '):
        flow.append(Paragraph(inline(s[2:]), h1))
    elif s.startswith(('- ', '* ')):
        flow.append(Paragraph('&bull; ' + inline(s[2:]), body))
    elif s:
        buf = [s]
        while i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].startswith(('|', '#', '- ', '* ', '---')):
            i += 1; buf.append(lines[i].strip())
        flow.append(Paragraph(inline(' '.join(buf)), body))
    i += 1

SimpleDocTemplate(OUT, pagesize=A4, title='AX-1177 Methods Annex',
                  author='', subject='', creator='',
                  leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm).build(flow)
print('wrote', OUT)
