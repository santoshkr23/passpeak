import json, sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from xml.sax.saxutils import escape
slug, buyer = sys.argv[1], sys.argv[2]
e = next(x for x in json.load(open(__import__("os").path.join(__import__("os").path.dirname(__file__),"..","data","exams.json"))) if x["s"]==slug)
ink, acc, mut = HexColor("#121a2e"), HexColor("#2446e8"), HexColor("#5a6580")
S = lambda n,**k: ParagraphStyle(n, fontName=k.pop("f","Helvetica"), textColor=k.pop("c",ink), **k)
code, h1, body, q, o, ex, sm = S("c",f="Courier-Bold",c=acc,fontSize=12), S("h",f="Helvetica-Bold",fontSize=26,leading=31), S("b",fontSize=11,leading=16,c=mut), S("q",f="Helvetica-Bold",fontSize=11.5,leading=16,spaceAfter=6), S("o",fontSize=11,leading=16,leftIndent=14), S("e",fontSize=10,leading=14,c=mut,leftIndent=14), S("s",fontSize=8,c=mut)
L="ABCD"
def stamp(c, d):
    c.saveState(); c.setFont("Helvetica",8); c.setFillColor(mut)
    c.drawString(40,25,f"PassPeak · {e['c']} · Licensed to {buyer} · Personal use only")
    c.drawRightString(A4[0]-40,25,f"Page {d.page}")
    c.setFillColor(HexColor("#e4e8f2")); c.setFont("Helvetica-Bold",34)
    c.translate(A4[0]/2,A4[1]/2); c.rotate(40); c.drawCentredString(0,0,buyer); c.restoreState()
f=[Paragraph(e["c"],code),Spacer(1,8),Paragraph(escape(e["n"]),h1),Spacer(1,12),
   Paragraph(f"Premium practice PDF · {len(e['q'])} questions with answer key and explanations",body),Spacer(1,6),
   Paragraph(f"Licensed to {escape(buyer)}. Original questions written against the official exam objectives. Not affiliated with {e['v']}.",body),Spacer(1,24)]
for i,(t,opts,a,x) in enumerate(e["q"]):
    f.append(KeepTogether([Paragraph(f"Question {i+1}. {escape(t)}",q)]+[Paragraph(f"{L[k]}.  {escape(v)}",o) for k,v in enumerate(opts)]+[Spacer(1,16)]))
f+= [PageBreak(),Paragraph("Answer key",h1),Spacer(1,14)]
for i,(t,opts,a,x) in enumerate(e["q"]):
    f.append(KeepTogether([Paragraph(f"{i+1}. {L[a]} — {escape(opts[a])}",q),Paragraph(escape(x),ex),Spacer(1,10)]))
SimpleDocTemplate(f"{e['c']}-premium.pdf",pagesize=A4,leftMargin=50,rightMargin=50,topMargin=50,bottomMargin=50,title=f"{e['c']} Premium PDF",author="PassPeak").build(f,onFirstPage=stamp,onLaterPages=stamp)
print("ok")
