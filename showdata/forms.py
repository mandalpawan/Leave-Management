from django import forms 
from .models import applyleave
from managementsystem.models import extendemp
from django.contrib.auth.models import User


class leaveform(forms.ModelForm):
    class Meta:
        model = applyleave
        fields = ['leave','holidayfrom','holidayto','detail']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['leave'].widget.attrs.update({'class':'selection'})
        self.fields['leave'].empty_label = "Select Leave Type"
        self.fields['holidayfrom'].widget.attrs.update({'type':'date'})
        self.fields['detail'].widget.attrs.update({'class':'form-control','placeholder':'Discription','id':'validationTextarea','rows':'5'})

class extendForm(forms.ModelForm):
    class Meta:
        model = extendemp
        fields = ['phone','catagory','department']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['phone'].widget.attrs.update({'class':'field-long','placeholder':'Enter Phone Number'})
        self.fields['catagory'].widget.attrs.update({'class':'field-long',})
        self.fields['catagory'].empty_label = "Select Catagory"
        self.fields['department'].widget.attrs.update({'class':'field-long',})
        self.fields['department'].empty_label = "Select Department"

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].widget.attrs.update({'class':'field-long','maxlength':'40'})
        self.fields['first_name'].widget.attrs.update({'class':'field-divided','maxlength':'15'})
        self.fields['last_name'].widget.attrs.update({'class':'field-divided','maxlength':'15'})



