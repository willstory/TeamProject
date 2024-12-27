from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User  # User 모델이 member 앱에 정의되어 있다고 가정
from django.views.generic import TemplateView
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        user_type = request.POST.get('user_type')
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_academy = (user_type == 'academy')
            user.save()

            # 파일 업로드 처리
            if user.is_academy and request.FILES.get('business_registration'):
                business_registration = request.FILES['business_registration']
                user.business_registration.save(business_registration.name, business_registration)

            login(request, user)  # 자동 로그인
            if user.is_academy:
                return redirect('academy_dashboard')
            else:
                return redirect('student_academy_selection')
    else:
        form = SignupForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_edit_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('mypage')  # 수정 후 리디렉트할 URL
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'member/profile_edit.html', {'form': form})

@login_required
def mypage(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'member/mypage.html', {'profile': profile})