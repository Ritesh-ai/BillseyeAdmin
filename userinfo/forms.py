from django import forms
from django.contrib.auth.models import User
from .models import UserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        # fields = '__all__'
        fields = ('first_name','last_name','username','email','password')

# class UserInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserInfo
#         fields = ('Address','Phone_number')
