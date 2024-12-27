from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'academy')
    search_fields = ('course_name',)
    list_filter = ('academy',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('member', 'course', 'course_created_at')  # 'student'를 'member'로 수정하고, 'enrollment_date'를 'course_created_at'으로 수정
    search_fields = ('member__username', 'course__course_name')  # 'student__username'을 'member__username'으로 수정
    list_filter = ('course',)
