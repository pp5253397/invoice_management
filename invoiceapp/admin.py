from django.contrib import admin
from .models import AgentDetails, InvoiceDetails, ItemDetails

admin.site.register(AgentDetails)
admin.site.register(InvoiceDetails)
admin.site.register(ItemDetails)
