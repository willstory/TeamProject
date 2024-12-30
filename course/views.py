from django.shortcuts import render, get_object_or_404
from .models import Course, Enrollment, Payment
from django.contrib.auth.decorators import login_required

@login_required
def my_courses(request):
    # 현재 로그인된 사용자가 수강 중인 강의
    enrollments = Enrollment.objects.filter(member=request.user)
    return render(request, 'course/my_course.html', {'enrollments': enrollments})

@login_required
def course_detail(request, course_id):
    # 특정 강의의 상세 정보
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/course_detail.html', {'course': course})

@login_required
def course_enroll(request, course_id):
    # 수강 신청 로직
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # 이미 수강 중인지 확인
        if Enrollment.objects.filter(member=request.user, course=course).exists():
            message = "이미 수강 중인 강의입니다."
        else:
            # 수강 신청 생성
            Enrollment.objects.create(
                member=request.user,
                academy=course.academy,
                course=course,
                course_status='pending'
            )
            message = "수강 신청이 완료되었습니다."
        return render(request, 'course/course_enroll.html', {'course': course, 'message': message})

@login_required
def payment(request, enrollment_id):
    # 결제 처리 로직
    enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
    if request.method == 'POST':
        Payment.objects.create(
            enrollment=enrollment,
            member=request.user,
            amount=enrollment.course.course_price,
            status='success'  # 결제 성공으로 가정
        )
        enrollment.course_status = 'approved'
        enrollment.save()
        message = "결제가 완료되었습니다."
    else:
        message = "결제 정보를 확인해주세요."
    return render(request, 'course/payment.html', {'enrollment': enrollment, 'message': message})

@login_required
def refund(request):
    # 환불 로직
    return render(request, 'course/refund.html')
