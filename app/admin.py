from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin 


# Register your models here.
# class UserModel(UserAdmin):
#     list_display= ['username', 'user_type']
admin.site.register(CustomUser)

admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Semester_Year)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Staff_leave)
admin.site.register(Student_Notifications)
admin.site.register(Student_leave)
admin.site.register(Student_Exam_Result)
admin.site.register(Document_File)
admin.site.register(About_Us)
admin.site.register(ChatMessage)
admin.site.register(QAResponse)
admin.site.register(BusDetails)
admin.site.register(Timetabel)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['enr', 'course_id', 'semester_year_id']

