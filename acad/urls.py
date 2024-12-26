from django.urls import path
from . import views

app_name = 'acad'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # 대시보드 페이지
]