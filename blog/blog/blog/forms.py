from django import forms

class contact_form(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    descrption = forms.CharField(widget=forms.Textarea)
