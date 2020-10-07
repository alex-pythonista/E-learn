from django.urls import path
from . import views

app_name = 'app_course'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('publish/', views.PublishCourse.as_view(), name='publish'),
    path('course_details/<slug:slug>/', views.course_details, name='course_details'),
    path('my_courses/', views.MyCourses.as_view(), name='my_courses'),
    path('question/<pk>/', views.question, name='question'),
]