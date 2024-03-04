from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    privacy_policy = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input bigger-checkbox left-5px'}))
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control width-300', 'placeholder': 'Enter strong password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control width-300', 'placeholder': 'Confirm password'})
        self.fields['password2'].help_text = ''
        self.fields['privacy_policy'].label = 'I have read and agree to the Privacy Policy'
        privacy_policy_url = 'https://www.privacypolicygenerator.info/live.php?token=3z3z'
        self.fields['privacy_policy'].help_text = mark_safe("By ticking the box above, you acknowledge that you have read, understood, and agree to our <a href='{}' target='_blank'>Privacy Policy</a>. This includes how we collect, use, and protect your personal information. Please review it carefully to understand your rights and our obligations before consenting.".format(privacy_policy_url))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input bigger-checkbox left-5px'}))


class ProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}))
