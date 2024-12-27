from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    MEMBER_TYPES = (
        ('user', '일반회원'),
        ('academy_admin', '학원운영자'),
        ('admin', '전체관리자'),
    )
    
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPES, default='user')
    phone = models.CharField(max_length=15, null=True)  # 전화번호 길이 조정
    address = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)  # 나이를 IntegerField로 변경
    phone_verified = models.BooleanField(default=False)
    gps_enabled = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='member_attachments/', null=True, blank=True)  # blank=True 추가
    is_academy = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='member_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='member_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    class Meta:
        db_table = 'member'
        verbose_name = '회원'
        verbose_name_plural = '회원들'

    def __str__(self):
        return self.username

class User(models.Model):
    # User 모델 정의
    is_academy = models.BooleanField(default=False)
    business_registration = models.FileField(upload_to='business_registrations/', blank=True, null=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_academy = None  # 초기화

    def save(self, *args, **kwargs):
        from academy.models import Academy  # save 메서드 내에서 임포트
        if self.enrolled_academy is not None:
            self.enrolled_academy = Academy.objects.get(id=self.enrolled_academy_id)  # 예시
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - Student"
    
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    # 추가적인 필드들을 여기에 정의할 수 있습니다.

    def __str__(self):
        return self.user.username