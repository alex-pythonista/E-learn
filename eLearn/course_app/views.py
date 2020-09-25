# framework imports
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# project imports
from .forms import PublishCourse, CommentForm
import uuid
from .models import Course, Enrol
from login_app.models import Instructor, Student

# Create your views here.

@login_required
def home(request):
    courses = Course.objects.all()
    return render(request, 'course_app/home.html', {'courses': courses,})

@login_required
def publish_course(request):
    form = PublishCourse()
    current_user = Instructor.objects.get(user=request.user)
    if request.method == 'POST':
        form = PublishCourse(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            title = course.course_title
            course.instructor = current_user
            course.slug = title.replace(' ', '-') + str(uuid.uuid4())
            course.save()
            return HttpResponseRedirect(reverse('course_app:home'))
    return render(request, 'course_app/publish_course.html', {'form': form})

@login_required
def course_details(request, slug):
    course = Course.objects.get(slug=slug)
    student = Student.objects.get(user=request.user)
    already_enrolled = Enrol.objects.filter(student=student, course=course)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.course = course
            comment.save()
            return HttpResponseRedirect(reverse('course_app:details', kwargs={'slug': slug}))

    return render(request, 'course_app/course_details.html', {'course': course, 'form': comment_form, 'enrolled': already_enrolled})

@login_required
def enrol_course(request, slug):
    student = Student.objects.get(user=request.user)
    course = Course.objects.get(slug=slug)
    already_enrolled = Enrol.objects.filter(student=student, course=course)
    if not already_enrolled:
        enrolled = Enrol(student=student, course=course)
        enrolled.save()
    return HttpResponseRedirect(reverse('course_app:details', kwargs={'slug': slug}))