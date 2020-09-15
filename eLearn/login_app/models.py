from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    profile_picture = models.ImageField(upload_to='teacher_dp', blank=True)
    about = models.CharField(blank=True, max_length=255)
    fullname = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    profile_picture = models.ImageField(upload_to='student_dp', blank=True)
    about = models.CharField(blank=True, max_length=255)
    fullname = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username
