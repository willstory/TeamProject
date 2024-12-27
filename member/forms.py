from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member
from .models import Profile
from .models import User

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('username', 'password1', 'password2')  # 필요한 필드 추가

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number']  # 수정할 필드들

class SignupForm(UserCreationForm):
    business_registration = forms.FileField(
        required=False, 
        label="사업자등록증 업로드",
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf,.jpg,.jpeg,.png"})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'business_registration']