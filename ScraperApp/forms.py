from django import forms

class ScraperInput(forms.Form):
    username = forms.CharField()
    email = forms.EmailField() 
    