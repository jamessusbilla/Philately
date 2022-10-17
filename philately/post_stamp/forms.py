from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Philatelist, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["slug","firstName","lastName","email","content","subject","status"]

class SignUp(UserCreationForm):
    firstName = forms.CharField(max_length=200, required=True, help_text='Optional.')
    lastName = forms.CharField(max_length=200, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Philatelist
        fields = ('userName', 'firstName', 'lastName', 'email', 'password1', 'password2', )
