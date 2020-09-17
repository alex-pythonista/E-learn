from django import forms
from .models import Instructor, Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Instructor, Student

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

class EditStudentProfile(forms.ModelForm):
    fullname = forms.CharField(
        required=False,
        label="Student full name",
    )
    class Meta:
        model = Student
        exclude = ['user']

class EditInstructorProfile(forms.ModelForm):
    fullname = forms.CharField(
        required=False,
        label="Instructor full name",
    )
    class Meta:
        model = Instructor
        exclude = ['user']