from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100,required=False)