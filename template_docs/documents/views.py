from django.shortcuts import render
from django.http import HttpResponse
from documents.utils.pdf_generator import PDFGenerator
from documents.templates_data.rfd_data import context_data
from documents.templates_data.cmr_data_json import cmr_data
import os
from django.utils.translation import gettext as _



# Create your views here.

def index(request): #HttpRequest
    context_data ={
         'shipment_number' :  'xxxx',
         'logo': 'nova_logo.png',
         'issuer': ' Mikita Kharko',
         'phone_issuer' : '+48546654543',
         'email_issuer': ' m.kharko@nova-tracking.com',
         'branch_issuer' : 'test',
         'city' : 'Warsaw',
         'date' : '04.01.2024'
    }
     
    return render(request,'pdf/cmr/index.html',context_data)


def generate_rfdShippingInstruction(request):
    #logo image
    current_script_path = os.path.abspath(__file__)
    current_script_folder = os.path.dirname(current_script_path)
    image_path = os.path.join(current_script_folder, "nova_logo.png")

    pdf_content = PDFGenerator.generate('documents/templates/pdf/rfdShippingInstruction/index.html',context_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=rfdShippingIns.pdf'

    response.write(pdf_content)

    return response


def generate_rfdWaybill(request):
    
   pdf_content = PDFGenerator.generate('documents/templates/pdf/rfdWaybill/index.html',context_data)

   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'inline; filename=rfdWaybill.pdf'

   response.write(pdf_content)

   return response


def generate_cmr(request):
    
    pdf_content = PDFGenerator.generate('documents/templates/pdf/cmr/index.html',cmr_data)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline; filename=cmr.pdf'

    response.write(pdf_content)

    return response
