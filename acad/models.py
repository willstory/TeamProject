from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
# from member.models import Member

class Membership(models.Model):
    name = models.CharField(max_length=100)         # 회원 이름
    join_date = models.DateField(auto_now_add=True) # 가입일

    def __str__(self):
        return self.name

class Payment(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 수납금액을 DecimalField로 변경
    pay_date = models.DateField(validators=[MaxValueValidator(timezone.now().date())])  # 미래 날짜 방지

    def __str__(self):
        return f'{self.membership.name} - {self.amount:,.2f}원 ({self.pay_date})'  # 금액 포맷팅