from django.shortcuts import render
from django.http import HttpResponse
from documents.utils.pdf_generator import PDFGenerator
from documents.templates_data.rfd_data_json import rfd_data 
from documents.templates_data.cmr_data_json import cmr_data
from documents.templates_data.invoice_data_json import invoice_data
from documents.templates_data.corrective_note_data_json import corrective_note_data
from documents.templates_data.credit_note_json import credit_note_data
from documents.templates_data.bol_data_json import bol_data
from documents.templates_data.sea_bill_of_lading_data_json import sea_bol_data

import os
from django.utils.translation import gettext as _



# Create your views here.

def index(request): #HttpRequest
     
    return render(request,'pdf/bol/index.html',context_data)


def generate_rfdShippingInstruction(request):

    pdf_content = PDFGenerator.generate('documents/templates/pdf/rfdShippingInstruction/index.html',rfd_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=rfdShippingIns.pdf'

    response.write(pdf_content)

    return response

def generate_rfdForwardingInstruction(request):

    pdf_content = PDFGenerator.generate('documents/templates/pdf/rfdForwardingInstruction/index.html',rfd_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=rfdForwardingIns.pdf'

    response.write(pdf_content)

    return response


def generate_rfdWaybill(request):
    
   pdf_content = PDFGenerator.generate('documents/templates/pdf/rfdWaybill/index.html',rfd_data)

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


def generate_invoice(request):

    pdf_content = PDFGenerator.generate('documents/templates/pdf/invoice/index.html',invoice_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=invoice.pdf'

    response.write(pdf_content)

    return response


def generate_corrective_note(request):
    
    pdf_content = PDFGenerator.generate('documents/templates/pdf/correctiveNote/index.html',corrective_note_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=correctiveNote.pdf'

    response.write(pdf_content)

    return response


def generate_creditNote(request):
    
    pdf_content = PDFGenerator.generate('documents/templates/pdf/creditNote/index.html',credit_note_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=creditNote.pdf'

    response.write(pdf_content)

    return response

def generate_debitNote(request):
    
    pdf_content = PDFGenerator.generate('documents/templates/pdf/debitNote/index.html',credit_note_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=debitNote.pdf'

    response.write(pdf_content)

    return response


def generate_bill_of_landing(request):
    
    pdf_content = PDFGenerator.generate('documents/templates/pdf/bol/index.html',bol_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=bill_of_landing.pdf'

    response.write(pdf_content)

    return response



def generate_domestic_cmr(request):
    
    pdf_content = PDFGenerator.generate('documents/templates/pdf/domesticCmr/index.html',cmr_data)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline; filename=cmr.pdf'

    response.write(pdf_content)

    return response


def generate_sea_bill_of_lading(request):
                                
    pdf_content = PDFGenerator.generate('documents/templates/pdf/sea_bill_of_lading/index.html',sea_bol_data)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline; filename=sea_bill_of_lading.pdf'

    response.write(pdf_content)

    return response                 
