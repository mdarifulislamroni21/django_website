from django import forms
from main.models import user_details
#create New Form
class user_details_connect(forms.ModelForm):
    class Meta:
        model=user_details
        fields="__all__"
        widgets={
            'buydate':forms.TextInput(attrs={'type':'date'}),
            'product':forms.TextInput(attrs={'placeholder':'T-Shart'})
        }
