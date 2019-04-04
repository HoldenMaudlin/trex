from django import forms

class EmailForm(forms.Form):
    contact_email = forms.EmailField(required=True, label="", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))