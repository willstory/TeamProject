from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    # 강의조회
    path('detail/<int:course_id>/', views.course_detail, name='course_detail'),

    # 수강신청
    path('enroll/<int:course_id>/', views.course_enroll, name='course_enroll'),
    path('enrollment/info/', views.enrollment_info, name='enrollment_info'),
    path('enrollment/cancel/<int:enrollment_id>/', views.enrollment_cancel, name='enrollment_cancel'),
    
    # 결제 관련
    path('payment/<int:enrollment_id>/', views.payment, name='payment'),
    path('payment/history/', views.payment_history, name='payment_history'),
    path('payment/cancel/<int:payment_id>/', views.payment_cancel, name='payment_cancel'),
]
