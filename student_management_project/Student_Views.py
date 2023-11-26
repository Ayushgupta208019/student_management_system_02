from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import *

@login_required(login_url='/')
def HOME(request):
    semester= Semester_Year.objects.all()
    subject_sem= Subject.objects.count()
    # current_user= request.user
    student_data= Student.objects.filter(admin= request.user.id)
    # student_data= Student.objects.all(id= request.user.id)  
    
    context= {
        'subject_sem': subject_sem,
        'semester': semester,
        'student_data': student_data,
        
    }
    
    return render(request, 'Student/home.html', context)


def NOTIFICATIONS(request):
    std_notification= Student_Notifications.objects.all().order_by('-id')[0:5]
    
    context={
        'notification': std_notification
    }
    return render(request, 'Student/notification.html', context)

def STUDENT_APPLY_LEAVE(request):
    student= Student.objects.filter(admin= request.user.id)
    for x in student:
        student_id= x.id
        
        student_leave_history= Student_leave.objects.filter(student_id= student_id)
        
        context= {
            'student_leave_history': student_leave_history
        }
            
        return render(request, 'Student/apply_leave.html', context)


def STUDENT_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date= request.POST.get('leave_date')
        leave_message= request.POST.get('leave_message')
        
        student= Student.objects.get(admin= request.user.id)
        
        leave= Student_leave(
            student_id= student,
            date= leave_date,
            message= leave_message,   
        )
        leave.save()
        messages.success(request, 'Apply for leave Successfully')
        return redirect('student_apply_leave')
    return render(request, 'Student/apply_leave.html')

def VIEW_RESULT(request):
    mark= None
    student= Student.objects.get(admin= request.user.id)
    result= Student_Exam_Result.objects.filter(student_id= student)
    
    for x in result:    
        assignment_mark= x.assignment_mark
        exam_marks= x.exam_marks
        mark= assignment_mark + exam_marks
    context= {
        'result': result,
        'mark': mark,

    }
    return render(request, 'Student/view_result.html', context)


def VIEW_DOCUMENT(request):
    document= Document_File.objects.all().order_by('-id')[0:5]
    context={
        'document': document,
    }
    
    return render(request, 'Student/view_document.html', context)

def BUS_DETAILS(request):
    bus_details= BusDetails.objects.all()
    context= {
        'bus_details': bus_details,
    }
    
    return render(request, 'Student/bus_details.html', context)

def HOSTEL_DETAILS(request):
    hostel_details= HostelDetails.objects.all()
    context= {
        'hostel_details': hostel_details,
    }
    
    return render(request, 'Student/view_hostel_details.html', context)

def STUDENT_VIEW_TIME_TABLE(request):
    time_table= Timetabel.objects.all()
    context= {
        'time_table': time_table,
    }
    return render(request, 'Student/student_view_time_table.html', context)