import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfMerger

# Paths
java_folder = r"C:\Users\I.T Solutions\Desktop\Java"
input_pdf = os.path.join(java_folder, "certificate.pdf")
output_pdf = os.path.join(java_folder, "certificate_with_header.pdf")

# Step 1: Create a PDF with "Certificate" header
header_pdf = os.path.join(java_folder, "header.pdf")
c = canvas.Canvas(header_pdf, pagesize=letter)
c.setFont("Helvetica-Bold", 24)
c.drawCentredString(300, 750, "Certificate")
c.save()

# Step 2: Merge header and certificate.pdf
merger = PdfMerger()
merger.append(header_pdf)
merger.append(input_pdf)
merger.write(output_pdf)
merger.close()

print(f"Done! Check: {output_pdf}") 