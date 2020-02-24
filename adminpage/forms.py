from django import forms 
from showdata.models import applyleave
from managementsystem.models import extendemp
from managementsystem.models import department
from managementsystem.models import catagory


class detailForm(forms.ModelForm):
    class Meta:
        model = extendemp
        fields = ['catagory','department']

class leaveformvarify(forms.ModelForm):
    class Meta:
        model = applyleave
        fields = ['user','leave','holidayfrom','holidayto','detail','varify']



