from django.contrib import admin
from .models import Course, Comment, Enrol

# Register your models here.

admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Enrol)