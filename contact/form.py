from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='نام شما',
        widget=forms.TextInput(attrs={'placeholder': 'نام شما'})
    )
    phone = forms.CharField(
        max_length=15,
        label='شماره تماس شما',
        widget=forms.TextInput(attrs={'placeholder': 'شماره تماس شما', 'dir': 'ltr'})
    )