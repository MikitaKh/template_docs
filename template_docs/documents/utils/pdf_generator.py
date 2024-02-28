from django.conf import settings
from django.template.loader import get_template
from django.shortcuts import render
from django.template import engines
import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML
from weasyprint import CSS
from weasyprint.text.fonts import FontConfiguration
from io import BytesIO
import logging





class PDFGenerator:
    font_config = FontConfiguration()


    @staticmethod
    def generate(path_to_template: str, dict: dict) -> bytes:

     with open(path_to_template, 'r', encoding='utf-8') as template_file:
        html_content_template = template_file.read()

     django_engine = engines['django']
     template = django_engine.from_string(html_content_template)
     html_content = template.render(dict)
     
     font_config = FontConfiguration() 
     # Get path to css styles
     relative_directory = os.path.relpath(os.path.dirname(path_to_template), 'documents/templates')
    

     css_content = PDFGenerator.get_css_content(relative_directory,'documents/templates/',font_config)
    

    # Get html for generating html
     pdf_bytes = PDFGenerator.generate_pdf(html_content,css_content,font_config=font_config)

     return pdf_bytes
    

    @staticmethod
    def generate_pdf(html_content: str , css_content: CSS,font_config)->bytes:
        """Generate a PDF file and return its content as bytes."""
        pdf_io = BytesIO()
        #base path for rendering images
        base_url = str(settings.BASE_DIR)

        print("Base URL:", base_url)

        HTML(string=html_content,base_url=base_url).write_pdf(pdf_io , stylesheets=[css_content],font_config=font_config)
        logger = logging.getLogger('weasyprint')
        logger.addHandler(logging.FileHandler('C:/Users/agabi/Desktop/templates/template_docs/documents/utils/weasyprint.log'))
        return pdf_io.getvalue()
        
    @staticmethod
    def get_css_content(file_path: str , templates_path: str, font_config)->CSS:
        """Retrieve the CSS content based on the given file path and template path."""
        css_file_path = os.path.join(templates_path, f"{file_path}/style.css")
        
        return CSS(filename=css_file_path,font_config=font_config)
