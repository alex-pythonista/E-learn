from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from login_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('login_app.urls')),
    path('course/', include('course_app.urls')),
    path('', views.startpage, name='startpage'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
