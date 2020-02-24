from django import forms 
from .models import extendemp


class extendemp_form(forms.ModelForm):
    class Meta:
        model = extendemp
        fields = ['catagory','department','phone']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['catagory'].widget.attrs.update({'class':'field-select'})
        self.fields['catagory'].empty_label = "Select Category"
        self.fields['department'].widget.attrs.update({'class':'field-select'})
        self.fields['department'].empty_label = "Select Department"
        self.fields['phone'].widget.attrs.update({'class':'field-long','placeholder':'Enter Mobile Number'})


        
