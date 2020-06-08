from django import forms
from .models import InvoiceDetails, ItemDetails
from django.forms import (formset_factory, modelformset_factory)


class InvoiceDetailsForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetails
        fields = '__all__'

class ItemDetailsForm(forms.ModelForm):
    class Meta:
        model = ItemDetails
        fields = ('item_description', 'item_quantity', 'item_rate')
        labels = {
            'item_description': 'Item Description',
            'item_quantity': 'Quantity',
            'item_rate': 'Total Amount'
        }
        widgets = {
            'item_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description'
                }),
            'item_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Quantity'
                }),
            'item_rate': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Total Amount'
                })

        }

BookModelFormset = modelformset_factory(
    ItemDetails,
    fields=('item_description', 'item_quantity', 'item_rate'),
    extra=1,
    widgets = {
            'item_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description'
                }),
            'item_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Quantity'
                }),
            'item_rate': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Total Amount'
                })

        }
)