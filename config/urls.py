"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # Django 프로젝트에서 정적 파일을 제공하기 위한 URL 패턴을 생성
from . import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path("",views.HomeView.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', views.UserCreateDoneTV.as_view(), name='register_done'),    
=======
    path('', views.Homeview.as_view(), name='index'),  # 메인 페이지
    path('acad/', include('acad.urls')),               # acad 앱 연결
>>>>>>> main
]

# 개발 환경에서 정적 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)