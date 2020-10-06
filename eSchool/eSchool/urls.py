from django.contrib import admin
from django.urls import path, include
from app_course.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app_login.urls')),
    path('course/', include('app_course.urls')),
    path('', home, name='home'),
    
]
