from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student
from .forms import LoginForm, SignUpForm, EditStudentForm, EditTeacherForm

# Create your views here.

def initial_page(request):
    return render(request, 'app_login/initial.html', {})

# teacher and student login
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
                return HttpResponseRedirect(reverse('app_login:profile_teacher'))
    return render(request, 'app_login/login.html', {'teacher': True, 'form': form})

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
                return HttpResponseRedirect(reverse('app_login:profile_student'))
    return render(request, 'app_login/login.html', {'form': form})

# sign up part
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

# logout part
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:initial'))

# profile view
@login_required
def teacher_profile(request):
    return render(request, 'app_login/profile.html', {'teacher': True})

@login_required
def student_profile(request):
    return render(request, 'app_login/profile.html', {})

# edit profile

@login_required
def edit_teacher(request):
    current_user = Teacher.objects.get(user=request.user)
    form = EditTeacherForm(instance=current_user)
    if request.method == 'POST':
        form = EditTeacherForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = EditTeacherForm(instance=current_user)
            return HttpResponseRedirect(reverse('app_login:profile_teacher'))
    return render(request, 'app_login/edit_profile.html', {'form': form})

@login_required
def edit_student(request):
    current_user = Student.objects.get(user=request.user)
    form = EditStudentForm(instance=current_user)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = EditStudentForm(instance=current_user)
            return HttpResponseRedirect(reverse('app_login:profile_student'))
    return render(request, 'app_login/edit_profile.html', {'form': form})

