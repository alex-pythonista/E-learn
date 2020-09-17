from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('teacher-sign-up/', views.instructor_sign_up, name='instructor_sign_up'),
    path('student-sign-up/', views.student_sign_up, name='student_sign_up'),
    path('teacher-login/', views.instructor_login, name='instructor_login'),
    path('student-login/', views.student_login, name='student_login'),
    path('index/', views.startpage, name='startpage'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_instructor/', views.edit_instructor, name='edit_instructor'),
    path('edit_student/', views.edit_student, name='edit_student'),
]