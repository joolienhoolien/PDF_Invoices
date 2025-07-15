import pandas
import glob
from fpdf import FPDF

#Read input data and set it up as a list of dataframes
filepaths = glob.glob("invoices/*.xlsx")
files = []
for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    files.append(filepath)

#Create PDF and write df data
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

pdf.add_page()

# Header
pdf.set_font('Arial', 'B', 24)
pdf.set_text_color(100, 100, 100)

filename = "10001-2023.1.1.18.xls"
pdf.cell(w=0, h=12, txt=f"Invoice #{filename.split("-")[0]}", align='L', ln=1)

date = filename.split("-")[1].removesuffix(".xls")
pdf.cell(w=0, h=12, txt=f"Date:{date}", align='L', ln=1)

#Empty cell to pad between header and table
pdf.cell(w=0, h=12, ln=1)

#Create table
for index, row in df.iterrows():
    pdf.cell(w=0, h=12, txt=row, border=1)