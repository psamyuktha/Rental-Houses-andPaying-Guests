from login.models import UserProfileInfo
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms



class UserInfoForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput() , label='Confirm password',)
    class Meta:
        model = User
        fields = ['username','email','first_name','password']

    def clean(self):
        cleaned_data = super(UserInfoForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['profile_pic','website']
