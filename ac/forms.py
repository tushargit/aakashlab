from django import forms
from django.contrib.auth.models import User

# import from ac models
from ac.models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Your name*.'}),
        help_text="Enter youe name.", required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class':'form-control',
                                  'placeholder': 'Enter valid email*.'}),
        help_text="Enter Email.", required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control',
                                     'placeholder': 'Please write your message*.',
                                     'rows': 4}), 
        help_text="Please write your message.", required=True)
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

