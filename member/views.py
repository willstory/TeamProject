from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User  # User 모델이 member 앱에 정의되어 있다고 가정
from django.views.generic import TemplateView

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)  # 파일 업로드를 위해 request.FILES 추가
        user_type = request.POST.get('user_type')
        
        if form.is_valid():
            user = form.save()
            user.is_academy = (user_type == 'academy')
            user.save()
            login(request, user)  # 자동 로그인
            if user.is_academy:
                return redirect('academy_dashboard')  # 학원 대시보드로 리디렉션
            else:
                return redirect('student_academy_selection')  # 수강생 학원 선택 페이지로 리디렉션
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})