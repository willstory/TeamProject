from django.db import models
from django.core.validators import MinValueValidator

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    academy = models.ForeignKey('academy.Academy', on_delete=models.CASCADE, related_name='course')
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    course_duration = models.IntegerField(validators=[MinValueValidator(1)])
    course_start_date = models.DateTimeField()
    course_created_at = models.DateTimeField(auto_now_add=True)
    course_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.course_name
    
class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('pending', '대기중'),
        ('approved', '승인완료'),
        ('cancelled', '수강취소'),
        ('completed', '수강완료'),
        ('dropped', '수강포기')
    ]

    enrollment_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    academy = models.ForeignKey('academy.Academy', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    course_created_at = models.DateTimeField(auto_now_add=True)
    course_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'enrollments'

class Payment(models.Model):
    STATUS_CHOICES = [
        ('success', '결제성공'),
        ('failed', '결제실패'),
        ('pending', '결제대기')
    ]
    
    payment_id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        db_table = 'payment'