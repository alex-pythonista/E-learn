from django.contrib import admin
from .models import Student, Instructor

# Register your models here.

admin.site.register(Student)
admin.site.register(Instructor)