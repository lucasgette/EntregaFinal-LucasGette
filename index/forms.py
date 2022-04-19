from django import forms


class ConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(label='')