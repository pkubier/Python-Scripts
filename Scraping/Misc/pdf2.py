import tkinter 
import camelot
import glob

directory = 'C:\\Users\\patrick\\Downloads\\pdfs\\*.pdf'
files = [filename for filename in glob.glob(directory)]

for pdf_filepath in files:
    csv_filepath=pdf_filepath.replace('.pdf','.csv')
    tables = camelot.read_pdf(pdf_filepath, pages='all')

    # the following lines seem to be duplicate
    tables.export(csv_filepath, f='csv', compress=True) # json, excel, html, sqlite
    tables.to_csv(csv_filepath)
