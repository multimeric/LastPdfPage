# LastPdfPage

Sometimes PDFs are generated for a powerpoint presentation, which don't work so well as PDF documents.

For example, a single slide in the presentation might be designed to show each dotpoint when the presenter clicks.
However, once this presentation is converted to PDF, the document is unusable because each dotpoint now has its own 
slide.

`LastPdfPage` eliminates this problem by editing a PDF that has multiple pages with the same page number, and selecting
only the last (or first) page from each page range that has this issue.

# Installation

Simply run:

```bash
pip install git+github.com:TMiguelT/LastPdfPage.git
```

# CLI
```
Usage: last-pdf-page [OPTIONS] PDF

Options:
  --select [first|last]  Whether to choose the first, or last page for each
                         number

  --help                 Show this message and exit.
```

For example, to edit a PDF and take only the last page of each page-range with the same number:
```bash
last-pdf-page --select last somePdf.pdf > fixed.pdf
```

# Python API
```python
from last_pdf_page import simplify_pdf

with open('fixed.pdf', 'wb') as fp:
    simplify_pdf('somePdf.pdf', select='last', outfile=fp)
```
