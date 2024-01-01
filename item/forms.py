from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)

        widgets = {
            'category' : forms.Select(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'name' : forms.TextInput(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'price' : forms.TextInput(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'image' : forms.FileInput(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')

        widgets = {
            'category' : forms.Select(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'name' : forms.TextInput(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'price' : forms.TextInput(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
            'image' : forms.FileInput(attrs={
                'class' : 'rounded border form-control py-2 px-3'
            }),
        }