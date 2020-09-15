from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    
]