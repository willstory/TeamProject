# acad/models.py

from django.db import models

class Membership(models.Model):
    name = models.CharField(max_length=100)         # 회원 이름
    join_date = models.DateField(auto_now_add=True) # 가입일

    def __str__(self):
        return self.name

class Payment(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()  # 수납금액
    pay_date = models.DateField()           # 결제일

    def __str__(self):
        return f'{self.membership.name} - {self.amount}원 ({self.pay_date})'