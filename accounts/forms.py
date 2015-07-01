from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

from accounts.models import CustomUser


class CustomRegistration(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'enter your email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'  , 'placeholder':'enter your last name'}))
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control datepicker'  , 'placeholder':'enter your birthdate'}))
    captcha = CaptchaField()

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

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ImageForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image_path']