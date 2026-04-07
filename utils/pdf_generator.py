from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime

def generate_medical_summary_pdf(extracted_results, ai_summary):
    """
    Generate a professional medical summary PDF.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontSize=18,
        spaceAfter=20,
        textColor=colors.dodgerblue
    )
    
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=10,
        textColor=colors.darkblue
    )

    elements = []

    # Title
    elements.append(Paragraph("Medical Lab Report Analysis", title_style))
    elements.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # AI Summary Section
    elements.append(Paragraph("AI-Generated Explanation", header_style))
    elements.append(Paragraph(ai_summary, styles['Normal']))
    elements.append(Spacer(1, 20))

    # Lab Results Table
    elements.append(Paragraph("Detailed Lab Results", header_style))
    
    # Table Data
    data = [["Test Name", "Result", "Unit", "Reference", "Status"]]
    for res in extracted_results:
        data.append([
            res['test_name'],
            str(res['value']),
            res['unit'],
            f"{res['min']} - {res['max']}",
            res['status']
        ])

    t = Table(data, colWidths=[150, 80, 80, 100, 80])
    
    # Table Styling
    t_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ])
    
    # Style rows based on status
    for i, res in enumerate(extracted_results):
        if res['status'] == 'High':
            t_style.add('TEXTCOLOR', (4, i+1), (4, i+1), colors.red)
        elif res['status'] == 'Low':
            t_style.add('TEXTCOLOR', (4, i+1), (4, i+1), colors.blue)
        else:
            t_style.add('TEXTCOLOR', (4, i+1), (4, i+1), colors.green)
            
    t.setStyle(t_style)
    elements.append(t)

    # Disclaimer
    elements.append(Spacer(1, 30))
    disclaimer_text = "<b>Disclaimer:</b> This is an AI-generated explanation for educational purposes. It is NOT a medical diagnosis. Please consult with a healthcare professional for interpretation."
    elements.append(Paragraph(disclaimer_text, styles['Italic']))

    doc.build(elements)
    buffer.seek(0)
    return buffer
