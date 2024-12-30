# acad/urls.py
from django.urls import path
from . import views

app_name = 'acad'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # 대시보드 페이지
    path('dashboard/', views.dashboard, name='academy_dashboard'),  # 기존 academy_dashboard 수정
]
