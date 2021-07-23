from django import forms
from main.models import registration
class registration_connect(forms.ModelForm):
    class Meta:
        model=registration
        fields="__all__"
        widgets={

             'user_name':forms.TextInput(attrs={'placeholder':'Ariful@#71','label':"User Name"}),
             'frist_name':forms.TextInput(attrs={'placeholder':'Ariful islam','label':'Frist Name'}),
             'email_address':forms.TextInput(attrs={'placeholder':'example@gmail.com','label':'Email Address'}),
             'last_name':forms.TextInput(attrs={'placeholder':'Roni','label':'Last Name'}),
             'phone_no':forms.TextInput(attrs={'placeholder':'0174160952*','label':'Phone Nambar'}),
             'road_no':forms.TextInput(attrs={'placeholder':'#Z5280A','label':'Road Namber'})




        }
