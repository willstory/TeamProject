from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Profile, Member
from .forms import SignupForm, ProfileForm, MemberProfileEditForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  # 파일 업로드 처리
        user_type = request.POST.get('user_type')  # 수강생 또는 학원 구분
        
        if form.is_valid():
            # Member 모델로 저장
            user = form.save(commit=False)
            user.member_type = 'academy_admin' if user_type == 'academy' else 'user'
            user.is_academy = (user_type == 'academy')  # 학원인 경우 is_academy=True로 설정
            user.save()

            # 사업자등록증 처리
            if user.is_academy and request.FILES.get('business_registration'):
                business_registration = request.FILES['business_registration']
                user.business_registration.save(business_registration.name, business_registration)

            login(request, user)  # 자동 로그인 처리
            if user.is_academy:
                return redirect('academy_dashboard')  # 학원 대시보드로 리디렉션
            else:
                return redirect('student_academy_selection')  # 수강생 학원 선택 페이지로 리디렉션
    else:
        form = SignupForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    member = request.user

    if request.method == 'POST':
        form = MemberProfileEditForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member:profile_view')  # 수정 후 프로필 페이지로 리디렉트
    else:
        form = MemberProfileEditForm(instance=member)

    return render(request, 'member/profile_view.html', {'form': form, 'member': member})

@login_required
def profile_edit_view(request):
    # 현재 로그인한 사용자에 해당하는 Member 객체를 가져옵니다.
    member = get_object_or_404(Member, id=request.user.id)

    if request.method == 'POST':
        # POST 요청 시 폼을 바인딩하고 제출된 데이터를 처리합니다.
        form = MemberProfileEditForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()  # 유효한 데이터일 경우 저장
            return redirect('member:profile_view')  # 프로필 뷰로 리디렉션
    else:
        # GET 요청 시 기존 데이터를 가지고 폼을 초기화합니다.
        form = MemberProfileEditForm(instance=member)

    return render(request, 'member/profile_edit.html', {'form': form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # 세션에 새로운 비밀번호 업데이트
            return redirect('member:profile_view')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'member/change_password.html', {'form': form})

@login_required
def mypage(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'member/mypage.html', {'profile': profile})