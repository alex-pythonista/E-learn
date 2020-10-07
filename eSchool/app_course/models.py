from django.db import models
from django.contrib.auth.models import User
from app_login.models import Teacher, Student
from django.utils.text import slugify
import uuid

# Create your models here.

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='course_teacher')
    course_title = models.CharField(max_length=255)
    course_poster = models.ImageField(verbose_name='Upload a course poster', upload_to='course_posters')
    course_article = models.TextField(verbose_name='Course Article')
    quiz_url = models.URLField(verbose_name='Quiz link')
    slug = models.SlugField(max_length=255, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_title

    def save(self):
        self.slug = slugify(self.course_title + '-' + str(uuid.uuid4()))
        super(Course, self).save()

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_question')
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_question')
    question = models.TextField()
    question_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-question_date']

    def __str__(self):
        return self.question

class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='q_reply')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reply')
    reply = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.reply
