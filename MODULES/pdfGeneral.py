# Importez les bibliothèques nécessaires
import io
from markdown import markdown
from weasyprint import HTML

def md2pdf():
    # Définissez le contenu Markdown
    with open('../AUDIT_TEMPLATE/AUDIT_TEMPLATE.md', 'r') as txt:
        markdown_content = txt.read()

    # Convertissez le contenu Markdown en HTML
    html_content = markdown(markdown_content)

    # Créez un fichier PDF en mémoire
    pdf_buffer = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_buffer)

    # Récupérez les données du PDF en mémoire
    pdf_data = pdf_buffer.getvalue()

    # Ouvrez un fichier en écriture
    with open('file.pdf', 'wb') as f:
        # Écrivez les données du PDF dans le fichier
        f.write(pdf_data)
