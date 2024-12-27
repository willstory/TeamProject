from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member
from .models import Profile

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('username', 'password1', 'password2')  # 필요한 필드 추가

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number']  # 수정할 필드들