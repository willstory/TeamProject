from django.db import models
from django.contrib.auth import get_user_model
from course.models import Course
from member.models import Member
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

from django.db import models

# models.py
from django.db import models

class QuestionData(models.Model):
    # 색인 = models.CharField(max_length=255, db_column='Index', primary_key=True)
    # 문제 = models.TextField(db_column='문제')
    # 유형 = models.CharField(max_length=100, db_column='유형')
    # 지문 = models.TextField(db_column='지문')
    # 보기 = models.TextField(db_column='보기')
    # 정답 = models.CharField(max_length=255, db_column='정답')
    # 변형 = models.CharField(max_length=100, db_column='변형')
    # 학년 = models.CharField(max_length=10, db_column='grade')
    # 연도 = models.CharField(max_length=4, db_column='year')
    # 강 = models.CharField(max_length=50, db_column='month')
    # 번호 = models.IntegerField(db_column='number')
    # 단원 = models.CharField(max_length=255, db_column='Total_number')
    # 그림 = models.CharField(max_length=255, db_column='그림')
    # 기본키 = models.CharField(max_length=50, db_column='PK_number')
    색인 = models.CharField(max_length=255, db_column='색인', primary_key=True)
    문제 = models.TextField(db_column='문제')
    유형 = models.CharField(max_length=100, db_column='유형')
    지문 = models.TextField(db_column='지문')
    보기 = models.TextField(db_column='보기')
    정답 = models.CharField(max_length=255, db_column='정답')
    변형 = models.CharField(max_length=100, db_column='변형')
    학년 = models.CharField(max_length=10, db_column='학년')
    연도 = models.CharField(max_length=4, db_column='연도')
    강 = models.CharField(max_length=50, db_column='강')
    번호 = models.IntegerField(db_column='번호')
    단원 = models.CharField(max_length=255, db_column='단원')
    그림 = models.CharField(max_length=255, db_column='그림')

    class Meta:
        db_table = 'question_data'
        managed = False  # Django가 이 테이블을 관리하지 않도록 설정

    def __str__(self):
        return f"{self.색인} - {self.문제[:20]}"




class Academy(models.Model):
    admin = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='academy', limit_choices_to={'member_type': 'academy_admin'}, null=True, blank=True, default=None)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # 전화번호 길이 조정
    email = models.EmailField()
    academy_name = models.CharField(max_length=255, null=True, blank=True)  # 기본값 설정
    academy_address = models.CharField(max_length=255, null=True, blank=True)  # 기본값 설정
    academy_phone = models.CharField(max_length=15, null=True, blank=True)  # Null 허용
    academy_email = models.EmailField(max_length=255, default='default@example.com')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('suspended', 'Suspended')  # 추가 상태
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    home_img = models.URLField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'academy'

    def __str__(self):
        return self.name  # academy_name 대신 name 반환

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # 유효성 검사 추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AcademyAdmin(models.Model):
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('owner', 'Owner'),
        ('manager', 'Manager'),
        ('staff', 'Staff')
    ], default='staff')
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date must be after start date.')
        
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name