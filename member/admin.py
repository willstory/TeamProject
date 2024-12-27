from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member

# admin.site.register(Member, UserAdmin)
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'member_type', 'phone', 'age', 'phone_verified')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('member_type', 'phone_verified')