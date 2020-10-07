from django.contrib import admin
from django.urls import path, include
from app_course.views import home
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app_login.urls')),
    path('course/', include('app_course.urls')),
    path('', home, name='home'),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
