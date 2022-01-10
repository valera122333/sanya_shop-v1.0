from os import name
from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        fields = ["name", "price", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "price": forms.TextInput(attrs={"class": "form-input"}),
        }
