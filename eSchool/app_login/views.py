from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student
from .forms import LoginForm, SignUpForm

# Create your views here.

def initial_page(request):
    return render(request, 'app_login/initial.html', {})

# teacher login
def teacher_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app_course:home'))
    return render(request, 'app_login/login.html', {'teacher': True, 'form': form})

# student login
def student_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app_course:home'))
    return render(request, 'app_login/login.html', {'form': form})

def teacher_sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            teacher_profile = Teacher(user=user)
            teacher_profile.save()
            return HttpResponseRedirect(reverse('app_login:login_teacher'))
    return render(request, 'app_login/sign_up.html', {'teacher': True, 'form':form}) 

def student_sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            student_profile = Student(user=user)
            student_profile.save()
            return HttpResponseRedirect(reverse('app_login:login_student'))
    return render(request, 'app_login/sign_up.html', {'form':form}) 

@login_required
def logout_user(request):
    current_user = request.user
    if current_user == Teacher(user=current_user):
        logout(request)
        return HttpResponseRedirect(reverse('app_login:login_teacher'))
    else:
        logout(request)
        return HttpResponseRedirect(reverse('app_login:login_student'))