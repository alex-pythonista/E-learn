from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('initial/', views.initial_page, name='initial'),
    path('login_teacher/', views.teacher_login, name='login_teacher'),
    path('login_student/', views.student_login, name='login_student'),
    path('sign_up_teacher/', views.teacher_sign_up, name='sign_up_teacher'),
    path('sign_up_student/', views.student_sign_up, name='sign_up_student'),
    path('logout/', views.logout_user, name='logout'),
]