from django import forms

class EmailForm(forms.Form):
    contact_email = forms.EmailField(required=True)