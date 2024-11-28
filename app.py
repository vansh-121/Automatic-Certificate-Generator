from flask import Flask, request, render_template, send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
import io
from PIL import Image  # Added for aspect ratio calculations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_certificate():
    name = request.form['name']
    course = request.form['course']
    organization = request.form['organization']
    date = request.form['date']

    # Create a buffer for the PDF
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Decorative Border
    pdf.setStrokeColor(colors.HexColor("#003366"))
    pdf.setLineWidth(10)
    pdf.rect(0.3 * inch, 0.3 * inch, 7.9 * inch, 10.4 * inch)  # Outer frame

    pdf.setStrokeColor(colors.HexColor("#6699CC"))
    pdf.setLineWidth(5)
    pdf.rect(0.4 * inch, 0.4 * inch, 7.7 * inch, 10.2 * inch)  # Inner frame

    # Background Watermark
    watermark_text = "Certificate of Achievement"
    pdf.saveState()
    pdf.translate(4.25 * inch, 6 * inch)
    pdf.rotate(45)
    pdf.setFont("Helvetica-Bold", 50)
    pdf.setFillColor(colors.HexColor("#d3d3d3"))
    pdf.setStrokeColor(colors.lightgrey)
    pdf.drawCentredString(0, 0, watermark_text)
    pdf.restoreState()

    # Header Logo
    # Load the logo and calculate aspect ratio
    logo_path = 'BFGI-logo.jpg'
    logo_image = Image.open(logo_path)
    logo_aspect_ratio = logo_image.width / logo_image.height

    # Define the desired width and calculate height to maintain aspect ratio
    logo_width = 2 * inch
    logo_height = logo_width / logo_aspect_ratio

    # Draw the logo
    pdf.drawImage(ImageReader(logo_image), 3.25 * inch, 9.5 * inch, width=logo_width, height=logo_height, mask='auto')

    # Title
    pdf.setFont("Helvetica-Bold", 30)
    pdf.setFillColor(colors.HexColor("#003366"))
    pdf.drawCentredString(4.25 * inch, 8.3 * inch, "Certificate of Achievement")

    # Subtitle
    pdf.setFont("Helvetica", 20)
    pdf.setFillColor(colors.black)
    pdf.drawCentredString(4.25 * inch, 7.5 * inch, f"This is to certify that")

    # Recipient Name
    pdf.setFont("Helvetica-Bold", 28)
    pdf.setFillColor(colors.HexColor("#8B0000"))
    pdf.drawCentredString(4.25 * inch, 6.8 * inch, name)

    # Course Info
    pdf.setFont("Helvetica", 18)
    pdf.setFillColor(colors.black)
    pdf.drawCentredString(4.25 * inch, 6.3 * inch, f"has successfully completed the")

    pdf.setFont("Helvetica-Bold", 22)
    pdf.setFillColor(colors.HexColor("#003366"))
    pdf.drawCentredString(4.25 * inch, 5.8 * inch, course)

    # Date and Signature Section
    pdf.setFont("Helvetica", 16)
    pdf.setFillColor(colors.black)
    pdf.drawString(1 * inch, 3.5 * inch, f"Date: {date}")
    pdf.drawString(5.5 * inch, 3.5 * inch, "Authorized Signature:")
    
    # Footer with Organization Name
    pdf.setFont("Helvetica-Oblique", 12)
    pdf.setFillColor(colors.HexColor("#666666"))
    pdf.drawCentredString(4.25 * inch, 1.5 * inch, f"Presented by {organization}")

    pdf.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name=f"{name}_certificate.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
