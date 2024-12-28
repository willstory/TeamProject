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

class MemberProfileEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['phone', 'address', 'age', 'business_registration', 'gps_enabled']  # gps_enabled 추가

    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '전화번호'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '주소'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '나이'}))
    business_registration = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    gps_enabled = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))  # GPS 사용 여부 체크박스