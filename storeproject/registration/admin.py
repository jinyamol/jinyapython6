from django.contrib import admin
from .models import Department, Course

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')