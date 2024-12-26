from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    MEMBER_TYPES = (
        ('user', '일반회원'),
        ('academy_admin', '학원운영자'),
        ('admin', '전체관리자'),
    )
    
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPES, default='user')
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=10, null=True)
    phone_verified = models.BooleanField(default=False)
    gps_enabled = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='member_attachments/', null=True)
    
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