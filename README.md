# PassPeak

Certification exam-prep website with original practice questions, free preview questions, and premium PDFs.

## What's here
- `index.html` — the whole site (home, exam catalog, practice mode, pricing, FAQ). Open it in a browser or host it on GitHub Pages / Netlify / Vercel.
- `data/exams.json` — question banks exported from the site's `EXAMS` data.
- `tools/mkpdf.py` — builds a premium PDF for one exam, stamped with the buyer's email.

## Settings
- Free questions per exam: `const FREE = 30;` in `index.html`
- Prices are in the `pricing()` function in `index.html` (PDF ₹1,500).

## Make a premium PDF
```bash
pip install reportlab
python3 tools/mkpdf.py dp-700 customer@example.com
```

## Adding questions
Each exam in `EXAMS` has `q: [[question, [A, B, C, D], correctIndex, explanation], ...]`.
Only use questions you wrote yourself.

## Next steps
- Connect Razorpay or Stripe checkout
- Generate and email the PDF after payment
- User accounts so progress syncs across devices
