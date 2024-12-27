from django.contrib import admin
from .models import Academy

@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = ('academy_name', 'admin', 'academy_address', 'academy_phone')
    search_fields = ('academy_name', 'academy_address')