from django import forms
from .models import Item
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        labels = {
            'item_desc': 'Item description',
        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'item_desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter item description', 'rows': 2}),
            'item_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item price', 'id': 'item-price'}),
            'item_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image URL'}),
        }
