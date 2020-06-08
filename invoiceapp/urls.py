
from django.urls import path
from .views import index, invoicedata, loginview, logout, invoiceformview, delete_item, detailed_invoice, invoice_email

urlpatterns = [

    path('', index, name='index'),
    path('invoice-data/', invoicedata, name='invoice-data'),
    path('login/', loginview, name='login'),
    path('logout/', logout, name='logout'),
    path('form/', invoiceformview, name='invoice-form'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
    path('detailed-invoice/<int:id>/', detailed_invoice, name='detailed_invoice'),
    path('invoice-email/', invoice_email, name='invoice-email')
]