# framework imports
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# project imports
from .forms import TeacherSignUpForm, StudentSignUpForm, StudentLoginForm, TeacherLoginForm, EditInstructorProfile, EditStudentProfile
from .models import Instructor, Student
# Create your views here.

def startpage(request):
    return render(request, 'login_app/startpage.html', {})

def instructor_sign_up(request):
    instructor_signup_form = TeacherSignUpForm()
    if request.method == 'POST':
        instructor_signup_form = TeacherSignUpForm(data=request.POST)
        if instructor_signup_form.is_valid():
            user = instructor_signup_form.save()
            instructor_profile = Instructor(user=user)
            instructor_profile.save()
            return HttpResponseRedirect(reverse('login_app:instructor_login'))
    return render(request, 'login_app/sign_up.html', {'teacher': True, 'signup_form': instructor_signup_form,})

def student_sign_up(request):
    student_signup_form = StudentSignUpForm()
    if request.method == 'POST':
        student_signup_form = StudentSignUpForm(data=request.POST)
        if student_signup_form.is_valid():
            user = student_signup_form.save()
            student_profile = Student(user=user)
            student_profile.save()
            return HttpResponseRedirect(reverse('login_app:student_login'))
    return render(request, 'login_app/sign_up.html', {'student': True, 'signup_form': student_signup_form})

def instructor_login(request):
    instructor_login_form = TeacherLoginForm()
    if request.method == 'POST':
        instructor_login_form = TeacherLoginForm(data=request.POST)
        if instructor_login_form.is_valid():
            username = instructor_login_form.cleaned_data.get('username')
            password = instructor_login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('course_app:home'))
    return render(request, 'login_app/login.html', {'teacher': True, 'login_form': instructor_login_form,})

def student_login(request):
    student_login_form = StudentLoginForm()
    if request.method == 'POST':
        student_login_form = TeacherLoginForm(data=request.POST)
        if student_login_form.is_valid():
            username = student_login_form.cleaned_data.get('username')
            password = student_login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('course_app:home'))
    return render(request, 'login_app/login.html', {'student': True, 'login_form': student_login_form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:startpage'))

@login_required
def profile(request):
    return render(request, 'login_app/profile.html', {})

@login_required
def edit_student(request):
    current_user = Student.objects.get(user=request.user)
    student_form = EditStudentProfile(instance=current_user)
    if request.method == 'POST':
        student_form = EditStudentProfile(request.POST, request.FILES, instance=current_user)
        if student_form.is_valid():
            student_form.save()
            # form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('login_app:profile'))
            
    return render(request, 'login_app/edit_profile.html', {'student_form': student_form, 'student': True})

@login_required
def edit_instructor(request):
    current_user = Instructor.objects.get(user=request.user)
    instructor_form = EditInstructorProfile(instance=current_user)
    if request.method == 'POST':
        instructor_form = EditInstructorProfile(request.POST, request.FILES, instance=current_user)
        if instructor_form.is_valid():
            instructor_form.save()
            # form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('login_app:profile'))

    return render(request, 'login_app/edit_profile.html', {'instructor_form': instructor_form, 'instructor': True})