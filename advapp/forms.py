from django import forms
from .models import Advreg

class Advregform(forms.ModelForm):
    class Meta:
        model = Advreg
        fields=['NAME','AGE','WEIGHT','PHNO']