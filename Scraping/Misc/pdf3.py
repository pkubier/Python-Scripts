import csv
from pathlib import Path


folder = Path(r'C:\Users\patrick\Downloads\pdfs')
csv_file = Path(r'C:\Users\patrick\Downloads\pdfs\output.csv')

with csv_file.open('w', encoding='utf-8') as f:
    writer = csv.writer(f, csv.QUOTE_ALL)

    writer.writerow(['FileName', 'Text'])

    for pdf_file in folder.glob('*.pdf'):
        pdf_text = convert_pdf_to_txt(pdf_file).replace('\n', '|')
        writer.writerow([pdf_file.name, pdf_text])
