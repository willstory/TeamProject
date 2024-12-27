from django.urls import reverse_lazy
from django.views import generic
from member.forms import MemberCreationForm  # 커스텀 사용자 모델을 위한 폼
from django.views.generic import TemplateView
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect, render


class HomeView(generic.TemplateView):
    template_name = 'home.html'

class UserCreateView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = MemberCreationForm
    success_url = reverse_lazy('register_done')

    def form_valid(self, form):
        user = form.save(commit=False)  # 사용자 객체를 저장하되, 아직 DB에 저장하지 않음
        user_type = self.request.POST.get('user_type')  # 선택된 사용자 유형 가져오기

        if user_type == 'academy':
            user.is_academy = True
            user.is_active = False  # 학원은 기본적으로 비활성화 상태로 설정
        else:
            user.is_academy = False
            user.is_active = True  # 학생은 활성화 상태로 설정

        user.save()  # 사용자 객체를 DB에 저장
        auth_login(self.request, user)  # 로그인 처리
        return super().form_valid(form)  # 성공적으로 폼을 처리한 후 리디렉션

class UserCreateDoneTV(generic.TemplateView):
    template_name = 'registration/register_done.html'

class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        
        # 사용자 유형에 따라 리디렉션
        if user.is_academy:
            return redirect('academy_dashboard')  # 학원 대시보드 URL
        else:
            return redirect('index')  # 학생 대시보드 URL

    def form_invalid(self, form):
        messages.error(self.request, '아이디 또는 비밀번호가 잘못되었습니다.')
        return super().form_invalid(form)

def academy_dashboard(request):
    return render(request, 'academy_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')