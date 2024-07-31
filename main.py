# This is a document for taking-note sheet

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for page in range(row["Pages"]):
        pdf.add_page()
        
        if page == 0:
            # Set header
            pdf.set_font(family="Times", style="B", size =24)
            pdf.set_text_color(27, 27, 27)
            pdf.cell(w =0, h =12, txt=row["Topic"], align="L", ln=1)
            
            x1, y1, x2, y2 = 10, 22, 200, 22
            pdf.set_draw_color(27, 27, 27)
            pdf.line(x1, y1, x2, y2)
            
            # set footer
            pdf.ln(260)
            pdf.set_font(family="Times", style="I", size=10)
            pdf.set_text_color(27, 27, 27)
            pdf.cell(w=0, h=10, txt=row["Topic"], align ="R")
        
        else:
            # set footer
            pdf.ln(272) # This number is added by the height of the header cell
            pdf.set_font(family="Times", style="I", size=10)
            pdf.set_text_color(27, 27, 27)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        
        # Add line to the Doc
        for i in range(32, 280, 10):
            
            y1 = y2 = i 
            x1, x2 = 10, 200
            pdf.set_draw_color(200, 200, 200)
            pdf.line(x1, y1, x2, y2)
            

pdf.output("output.pdf")
