from django import forms
from .models import Course, Comment

class PublishCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_title', 'image', 'video_lecture', 'article', 'quiz')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

