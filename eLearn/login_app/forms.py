from django import forms
from .models import Instructor, Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TeacherSignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'}) 
    )
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'user@domain.com'}) 
    )
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}) 
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 're-enter the password'}) 
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class StudentSignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'}) 
    )
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'user@domain.com'}) 
    )
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}) 
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 're-enter the password'}) 
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'}) 
    )
    password = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}) 
    )
    class Meta:
        model = User
        fields = ['username', 'password']

class TeacherLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'}) 
    )
    password = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}) 
    )
    class Meta:
        model = User
        fields = ['username', 'password']