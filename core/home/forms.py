from django import forms 
from home.models import Contact 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        #fields = ['name','age','phone_number']
        #exclude = ['phone_number']
    #name = forms.CharField(max_length=100)
    #age = forms.IntegerField()
    #gender = forms.CharField(max_length=100)
    #comment = forms.CharField(max_length=1000)
