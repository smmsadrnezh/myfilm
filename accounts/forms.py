from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

from accounts.models import CustomUser


class CustomRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    #captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'password1', 'password2')

    def save(self, commit=True):
        CustomUser = super(UserCreationForm, self).save(commit=False)
        CustomUser.email = self.cleaned_data['email']
        CustomUser.first_name = self.cleaned_data['first_name']
        CustomUser.last_name = self.cleaned_data['last_name']
        CustomUser.birth_date = self.cleaned_data['birth_date']
        CustomUser.image_path = self.cleaned_data['username'] + ".jpg"
        CustomUser.password = self.clean_password2()

        if commit:
            CustomUser.save()

        return CustomUser