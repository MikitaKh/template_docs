from django.urls import path

from .views import *

urlpatterns = [
    path('',index),
    path('generate_rfdShippingInstruction',generate_rfdShippingInstruction),
    path('generate_rfdWaybill',generate_rfdWaybill),
    path('generate_cmr',generate_cmr)
]