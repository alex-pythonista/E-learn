from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Teacher, Student

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(
        required=True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )
    class Meta:
        model = User
        fields = ('username', 'password')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="",widget=forms.TextInput(attrs={'placeholder': 'user@example.com'}))
    username = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password1 = forms.CharField(
        required=True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        required=True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter the password'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ('user', )

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', )
