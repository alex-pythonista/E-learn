from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import uuid
from django.utils.text import slugify
from app_login.models import Teacher, Student
from .models import Course, Question, Reply
from .forms import QuestionForm, ReplyForm
# from .forms import 

# Create your views here.


class Home(ListView):
    context_object_name = 'course_list'
    model = Course
    template_name = 'app_course/home.html'

class PublishCourse(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'app_course/publish_course.html'
    fields = ('course_title', 'course_poster', 'course_article', 'quiz_url')

    def form_valid(self, form):
        course_obj = form.save(commit=False)
        course_obj.teacher = self.request.user.teacher_profile
        title = course_obj.course_title
        course_obj.slug = slugify(title.replace(" ", "-") + str(uuid.uuid4()))
        course_obj.save()
        return HttpResponseRedirect(reverse('app_course:home'))

@login_required
def course_details(request, slug):
    course = Course.objects.get(slug=slug)
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user.student_profile
            question.course = course
            question.save()
            return HttpResponseRedirect(reverse('app_course:course_details', kwargs={'slug': slug}))

    return render(request, 'app_course/course_details.html', {'course': course, 'form': form})

class MyCourses(LoginRequiredMixin, TemplateView):
    template_name = 'app_course/my_courses.html'

@login_required
def question(request, pk):
    form = ReplyForm()
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.question = question
            reply.save()
            return HttpResponseRedirect(reverse('app_course:question', kwargs={'pk': pk}))
    return render(request, 'app_course/question.html', {'form':form, 'question': question})
