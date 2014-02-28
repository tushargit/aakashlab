from django import forms
from django.contrib.auth.models import User

# import from ac models
from ac.models import Contact
from ac.models import Coordinator, AakashCentre, User
from ac.models import Project, TeamMember, Mentor
from captcha.fields import ReCaptchaField


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
    captcha = ReCaptchaField(attrs={'theme': 'clean'})
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'captcha']


class AakashCentreForm(forms.ModelForm):
    """Register Aakash Centre."""
    ac_id = forms.IntegerField(label="Aakash Centre ID",
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Aakash Centre ID or RC ID*.'}),
        help_text="", required=True)
    quantity = forms.IntegerField(
        label = 'Number of tablets received at your Center(0 if you don\'t know).',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'value': '0',
                   'placeholder': 'Number of tablets received at your centre(Optional).'}),
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
    picture = forms.ImageField(label='Profile picture',
        widget = forms.FileInput(
            attrs={'placeholder': 'Coordinator picture.'}),
        required=False)
    
    class Meta:
        model = Coordinator
        fields = ['contact', 'picture']
    

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Username to login*.'}),
            help_text="", required=True,
        error_messages={'required':'Username is required.'})
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Coordinator first name*.'}),
            help_text="", required=True,
        error_messages={'required':'First name is required.'})
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Coordinator last name*.'}),
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


class ProjectForm(forms.ModelForm):
    """Form to add new project.
    """
    name = forms.CharField(label='Project name',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Project name*.'}),
            help_text="", required=True,
        error_messages={'required':'Project name is required.'})

    summary = forms.CharField(label='Summary',
        widget= forms.Textarea(
            attrs={'class': 'form-control', 'rows': '3',
                   'placeholder': 'Summary of the project*.'}),
            help_text="", required=True,
        error_messages={'required':'Summary is required.'})

    ac = forms.ModelChoiceField(
        label='Centre',
        cache_choices=True,
        widget = None,
        queryset = AakashCentre.objects.all().order_by('name'),
        empty_label = None,
        help_text="", required=True,
        error_messages={'required':'Aakash centre is required.'})

    src_url = forms.URLField(
        label='Source code URL',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Valid URL of source code.'}),
        error_messages={'invalid': 'Enter valid URL.'},
        required=False)

    doc_url = forms.URLField(
        label='Documentation URL',
        widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Valid URL where docs are hosted.'}),
        error_messages={'invalid': 'Enter valid URL.'},
        required=False)

    doc_file = forms.FileField(
        label = 'Documentation file.',
        widget = forms.FileInput(),
        help_text = 'Upload documentation.',
        required=False)

    additional_url = forms.URLField(
        label='Additional URL',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Additional URL where project related files are hosted.'}),
        required=False)

    apk = forms.FileField(
        label='APK',
        help_text = 'Upload APK.',
        error_messages={'required': 'APK is required.'},
        required=True)

    logo = forms.ImageField(
        label = 'Logo',
        help_text = 'Upload project logo.',
        required=False)


    class Meta:
        model = Project
        fields = ['name', 'summary', 'ac', 'src_url', 'doc_url',
                   'doc_file', 'additional_url', 'apk', 'logo']


    def clean_doc_file(self):
        """Limit doc_file upload size."""
        if self.cleaned_data['doc_file']:
            doc_file = self.cleaned_data['doc_file']
            if doc_file._size/(1024*1024) <= 5: # < 5MB
                return doc_file
            else:
                raise forms.ValidationError("Filesize should be less than 5MB.")


    def clean_apk(self):
        """Limit APK upload size."""
        if self.cleaned_data['apk']:
            apk = self.cleaned_data['apk']
            if apk.content_type.split('/')[1] == "vnd.android.package-archive":
                if apk._size/(1024*1024) <= 12: # < 5MB
                    return apk
                else:
                    raise forms.ValidationError("APK file max. size is 12MB.")
            else:
                raise forms.ValidationError("Not a valid APK!")


class MemberForm(forms.ModelForm):
    """Project member form.
    """
    member_name = forms.CharField(
        label = 'Member name',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Team member name*.'}),
            help_text="", required=False,
        error_messages={'required':'Member name is required.'})
    
    member_email = forms.EmailField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter valid email.'}),
            help_text="", required=False,
        error_messages={'required': 'Valid Email address is required.'})


    class Meta:
        model = TeamMember
        fields = ['member_name', 'member_email']


class MentorForm(forms.ModelForm):
    """Mentor form.
    """
    mentor_name = forms.CharField(
        label = 'Mentor\'s name',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Mentor name*.'}),
            help_text="", required=False,
        error_messages={'required':'Mentor name is required.'})
    
    mentor_email = forms.EmailField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter valid email.'}),
            help_text="", required=False,
        error_messages={'required': 'Valid Email address is required.'})


    class Meta:
        model = Mentor
        fields = ['mentor_name', 'mentor_email']


class Agreement(forms.Form):
    """Terms & Conditions.
    """
    agree = forms.BooleanField(
        widget=forms.CheckboxInput(),
        label="This Project will be always be licensed \
        under GNU GPL v3 or greater ",
        required=True,
        error_messages={'required': 'You must agree to terms and conditions.'},)
