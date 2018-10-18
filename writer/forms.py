from django import forms

class Newform(forms.Form):
    title = forms.CharField(max_length= 50)
    body = forms.Textarea()
    thumb = forms.ImageField()
    