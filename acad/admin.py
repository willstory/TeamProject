from django.contrib import admin
from .models import Membership, Payment

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'join_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'membership', 'amount', 'pay_date')