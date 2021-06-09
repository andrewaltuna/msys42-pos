from django import forms
from .models import item

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = [
            'item_name',
            'item_price',
            'stock_quantity',
        ]