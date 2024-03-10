from django.urls import path

from .views import *

urlpatterns = [
    path('',index),
    path('generate_rfdShippingInstruction',generate_rfdShippingInstruction),
    path('generate_rfdWaybill',generate_rfdWaybill),
    path('generate_cmr',generate_cmr),
    path('generate_invoice',generate_invoice),
    path('generate_corrective_note',generate_corrective_note),
    path('generate_creditNote',generate_creditNote),
     path('generate_bol',generate_bill_of_landing),
]