from pathlib import Path
import pandas
import glob
from fpdf import FPDF



filepaths = glob.glob("input_data/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)

    filename = Path(filepath).stem

    invoice_num, date = filename.split("-")
    pdf.add_page()

    # Header
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=8, txt=f"Invoice #{invoice_num}", align='L', ln=1)
    pdf.cell(w=0, h=8, txt=f"Date: {date}", align='L', ln=1)

    #Empty cell to pad between header and table
    #pdf.cell(w=0, h=12, ln=1)


    #Create table
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")

    #Table headers
    pdf.set_font('Times', style="B", size=10)
    pdf.set_text_color(80, 80, 80)
    columns = [column.replace("_", " ").title() for column in df.columns]
    pdf.cell(w=30, h=8, txt=f"{columns[0]}", border=1)
    pdf.cell(w=60, h=8, txt=f"{columns[1]}", border=1)
    pdf.cell(w=40, h=8, txt=f"{columns[2]}", border=1)
    pdf.cell(w=30, h=8, txt=f"{columns[3]}", border=1)
    pdf.cell(w=30, h=8, txt=f"{columns[4]}", border=1, ln=1)

    #Table contents
    for index, row in df.iterrows():
        pdf.set_font('Times', style="I", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=f"{row["product_id"]}", border=1)
        pdf.cell(w=60, h=8, txt=f"{row["product_name"]}", border=1)
        pdf.cell(w=40, h=8, txt=f"{row["amount_purchased"]}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row["price_per_unit"]}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row["total_price"]}", border=1, ln=1)



    #Output file to disk
    pdf.output(f"PDFs/{filename}.pdf")