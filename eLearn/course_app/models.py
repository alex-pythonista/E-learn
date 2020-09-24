from django.db import models
from django.contrib.auth.models import User
from login_app.models import Instructor, Student
from django.utils.text import slugify
import uuid

# Create your models here.

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='course_instructor')
    course_title = models.CharField(max_length=255, verbose_name='Course Title')
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(verbose_name='Upload course image', upload_to='course_image', default='')
    video_lecture = models.FileField(verbose_name='Upload video', upload_to='course_video')
    article = models.TextField(verbose_name='Course article', blank=True)
    quiz = models.URLField(blank=True)

    def __str__(self):
        return self.course_title

    def save(self):
        self.slug = slugify(self.course_title + '-' + str(uuid.uuid4()))
        super(Course, self).save()

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date', ]

    def __str__(self):
        return self.comment

class Enrol(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrolled_student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_course')
    enrolment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.student, self.course)
    
