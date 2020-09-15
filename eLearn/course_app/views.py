from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return HttpResponse('Welcome to eLearn!')