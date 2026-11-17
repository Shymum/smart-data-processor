# Smart Data Processor

A small Streamlit application for preparing CSV and Excel workbooks. Upload one or more files, preview each, stack rows by column name, trim text, remove empty rows and duplicates, then download CSV or XLSX. Processing happens in the running app; nothing is sent to a separate storage service by this application.

## Run locally

Requires Python 3.10 or newer. In this directory:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Try the fictional files in `demo_data/`. CSV input uses UTF-8; Excel input reads the first sheet. Combining stacks rows, matching columns by name and leaving unmatched fields empty. Duplicates are compared across all columns after the selected cleaning steps. XLSX export contains one sheet and does not retain original workbook formatting or formulas. Review results before using them.

## Tests

```bash
python -m pytest -q
```

This is a portfolio demonstration, not a production data governance tool. Demo records are fictional.
