from django import forms
from .models import contact
class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields ="__all__"
        widgets = {
            'f_name': forms.TextInput(attrs={'class':'form-control','placeholder':'enter your name'}),
            'f_phone': forms.TextInput(attrs={'class':'form-control','placeholder':'enter your phone number'}),
            'f_email': forms.EmailInput(attrs={'class':'form-control','placeholder':'enter your email id'}),
            'f_desc': forms.Textarea(attrs={'class':'form-control','placeholder':'enter description'})
            

        }
        labels={
            'f_name':'Name',
            'f_phone':'Phone no',
            'f_email':'Email ID',
            'f_desc':'Description'        }
