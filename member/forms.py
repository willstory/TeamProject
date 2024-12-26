from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('username', 'password1', 'password2')  # 필요한 필드 추가