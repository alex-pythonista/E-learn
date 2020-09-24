from django.urls import path
from . import views

app_name = 'course_app'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('publish_course/', views.publish_course, name='publish_course'),
    path('details/<slug:slug>/', views.course_details, name='details'),
]