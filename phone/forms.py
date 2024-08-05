from django import forms
from .models import Phone

class MobileForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'



