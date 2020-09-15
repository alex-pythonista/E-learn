# framework imports
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# project imports
from .forms import TeacherSignUpForm, StudentSignUpForm

# Create your views here.

def sign_up(request):
    teacher_form = TeacherSignUpForm()
    student_form = StudentSignUpForm()
    if request.method == 'POST':
        pass
    return render(request, 'login_app/sign_up.html', {'teacher_form': teacher_form, 'student_form': student_form})