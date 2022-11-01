from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    amount = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Amount in tk"}))
    address = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Address"}))
    zipcode = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Zip code", 'title': 'Your name'}))
    city = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "City", 'title': 'Your name'}))
    country = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Country", 'title': 'Your name'}))

    class Meta:
        model = Payment
        fields = ['amount', 'address', 'zipcode', 'city', 'country']
