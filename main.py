from pathlib import Path
import pandas
import glob
from fpdf import FPDF

#Read input data and set it up as a list of dataframes
filepaths = glob.glob("input_data/*.xlsx")
files = []
for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    files.append(filepath)

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
for file in files:
    filename = Path(file).stem

    invoice_num, date = filename.split("-")
    #Create PDF and write df data
    pdf.add_page()

    # Header
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=8, txt=f"Invoice #{invoice_num}", align='L', ln=1)
    pdf.cell(w=0, h=8, txt=f"Date: {date}", align='L', ln=1)

    #Empty cell to pad between header and table
    pdf.cell(w=0, h=12, ln=1)

    #Create table
    #for index, row in df.iterrows():
    #    pdf.cell(w=0, h=12, txt=row, border=1)



    #Output file to disk
    pdf.output(f"PDFs/{filename}.pdf")