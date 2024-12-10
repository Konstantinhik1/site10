from django import forms
from .models import Product
from django. forms import ModelForm
from django.contrib.auth.models import Group




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount"


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]