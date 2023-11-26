from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
 
class CustomUser(AbstractUser):
    USER= (
        ('1', 'HOD'),
        ('2', 'STAFF'),
        ('3', 'STUDENT'),
    )
    user_type= models.CharField(choices=USER, max_length=50, default=1)
    profile_pic= models.ImageField(upload_to='media/profile_pic')
    
    
class Course(models.Model):
    name= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Session_Year(models.Model):
    session_start= models.CharField(max_length=100)
    session_end= models.CharField(max_length=100)
    
    def __str__(self):
        return self.session_start + " to " + self.session_end
    
class Semester_Year(models.Model):
    semester= models.CharField(max_length=100)

    
    def __str__(self):
        return self.semester
    
class Student(models.Model):
    admin= models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address= models.TextField()
    gender= models.CharField(max_length=50)
    course_id= models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id= models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    semester_year_id= models.ForeignKey(Semester_Year, on_delete=models.DO_NOTHING)
    enr= models.CharField(max_length=50, default="E20301235600007")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
    
    #models for staff
    
class Staff(models.Model):
    admin= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address= models.TextField()
    gender= models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
    
class Subject(models.Model):
    name= models.CharField(max_length=100)
    course= models.ForeignKey(Course, on_delete=models.CASCADE)
    staff= models.ForeignKey(Staff, on_delete=models.CASCADE)
    semester_year= models.ForeignKey(Semester_Year, on_delete=models.CASCADE, default= True)
    created_at= models.DateTimeField(auto_now_add=True, null=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Staff_Notification(models.Model):
    staff_id= models.ForeignKey(Staff, on_delete=models.CASCADE)
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    status= models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.staff_id.admin.first_name
    
class Staff_leave(models.Model):
    staff_id= models.ForeignKey(Staff, on_delete=models.CASCADE)
    date= models.CharField(max_length=100)
    message= models.TextField()
    status= models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name
    
class Student_Notifications(models.Model):
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.message
    
    
class Student_leave(models.Model):
    student_id= models.ForeignKey(Student, on_delete=models.CASCADE)
    date= models.CharField(max_length=100)
    message= models.TextField()
    status= models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name


class Student_Exam_Result(models.Model):
    student_id= models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id= models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_mark= models.IntegerField()
    exam_marks= models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name
        
    
class Document_File(models.Model):
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    document= models.FileField(upload_to='media/', null=True)
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
   
    
class About_Us(models.Model):
    admin_name= models.CharField(max_length=100)
    admin_email= models.EmailField(max_length=254)
    admin_phone= models.CharField(max_length=10)
    designation= models.CharField(max_length=100, default= None)
    profile= models.CharField(max_length=100, default=None)
    admin_profile_pic= models.ImageField(upload_to="media/profile_pic", default=None)
    
    def __str__(self):
        return self.admin_name
     
     
class ChatMessage(models.Model):
    message = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
class QAResponse(models.Model):
    question = models.CharField(max_length=255)
    response = models.CharField(max_length=255)

    def __str__(self):
        return self.question
    
class BusDetails(models.Model):
    bus_code= models.CharField(max_length=50)
    bus_route= models.TextField()
    bus_fair= models.IntegerField()
    bus_type= models.CharField(max_length=50)
    
    def __str__(self):
        return self.bus_code
    
    
class HostelDetails(models.Model):
    hostel_block= models.CharField(max_length=50, default='block A')
    hostel_for= models.CharField(max_length=50, default='Male')
    hostel_fair= models.IntegerField()
    hostel_type= models.CharField(max_length=50, default='Non-AC')
    hostel_room_bed= models.IntegerField(default='6')
    hostel_availability= models.IntegerField(default=0)
    
    def __str__(self):
        return self.hsotel_block
    
class Timetabel(models.Model):
    teacher_id= models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject_id= models.ForeignKey(Subject, on_delete=models.CASCADE)
    course_id= models.ForeignKey(Course, on_delete=models.CASCADE)
    date= models.CharField(max_length=50)
    start_time= models.TimeField(auto_now=False, auto_now_add=False)
    end_time= models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.teacher_id.admin.first_name
    
class Attendance(models.Model):
    session = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class AttendanceReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Student_Notice(models.Model):
    student_notice= models.FileField(upload_to='media/', null=True),
    upload_at= models.DateTimeField(auto_now_add= True)
    
    
    
    
    