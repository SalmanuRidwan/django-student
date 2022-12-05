from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_code']
    
admin.site.register(Course, CourseAdmin)