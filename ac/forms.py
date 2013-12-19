from django import forms
from django.contrib.auth.models import User

# import from ac models
from ac.models import Contact
from ac.models import Coordinator, AakashCentre, User


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Your name*.'}),
        help_text="Enter your name.", required=True)
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


class AakashCentreForm(forms.ModelForm):
    """Register Aakash Centre."""
    ac_id = forms.IntegerField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Aakash Centre ID or RC ID*.'}),
        help_text="", required=True)
    quantity = forms.IntegerField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Number of tablets received at your centre.'}),
        help_text="", required=False)
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Centre name*.'}),
        help_text="", required=True)
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'City*.'}),
        help_text="", required=True)
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'State*.'}),
        help_text="", required=True)
    
    class Meta:
        model = AakashCentre
        fields = ['ac_id', 'quantity', 'name', 'city', 'state']

    
class CoordinatorForm(forms.ModelForm):
    """Register Coordinator Form."""
    contact = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Coordinator contact number*.'}),
        help_text="", required=True)
    picture = forms.FileField(
        widget = forms.FileInput(
            attrs={'placeholder': 'Coordinator contact number*.'}),
        required=False)
    
    class Meta:
        model = Coordinator
        fields = ['contact', 'picture']
    

class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Coordinator name*.'}),
            help_text="", required=True,
        error_messages={'required':'Username is required.'})
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'First name*.'}),
            help_text="", required=True,
        error_messages={'required':'First name is required.'})
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Last name*.'}),
        help_text="", required=True,
        error_messages={'required':'Last name is required.'})
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Coordinator valid email*.'}),
            help_text="", required=True,
        error_messages={'required':'Valid Email address is required.'})
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Coordinator password*.'}),
        help_text="", required=True,
        error_messages={'required':'Password is missing.'})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
