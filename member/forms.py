from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Profile

class SignupForm(UserCreationForm):
    # 사업자등록증 업로드 필드
    business_registration = forms.FileField(
        required=False,  # 선택적으로 파일을 업로드하도록 설정
        label="사업자등록증 업로드",
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf,.jpg,.jpeg,.png"})
    )

    class Meta:
        model = Member
        fields = ['username', 'email', 'password1', 'password2']

# ProfileForm에서 수정할 필드들 정의
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number']  # bio와 phone_number 필드를 수정 가능하게 설정
