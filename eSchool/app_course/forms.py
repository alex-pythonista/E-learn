from django import forms
from .models import Reply, Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question']

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['reply']