import json
from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,redirect, render)
from django.http import HttpResponse, JsonResponse





@login_required(login_url='/')
def HOME(request):
    staff_data= Staff.objects.filter(admin= request.user.id)
    context= {
        'staff_data': staff_data
    }
    return render(request, 'Staff/home.html', context)


def NOTIFICATIONS(request):
    staff= Staff.objects.filter(admin= request.user.id)
    for x in staff:
        staff_id= x.id
        
        notification= Staff_Notification.objects.filter(staff_id= staff_id)
        
        context={
            'notification': notification,
        }
        return render(request, 'Staff/notification.html', context)
    
def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification= Staff_Notification.objects.get(id= status)
    notification.status = 1
    notification.save()
    return redirect('staff_notifications')

def STAFF_APPLY_LEAVE(request):
    staff= Staff.objects.filter(admin= request.user.id)
    for x in staff:
        staff_id= x.id
        
        staff_leave_history= Staff_leave.objects.filter(staff_id= staff_id)
        
        context= {
            'staff_leave_history': staff_leave_history
        }
            
        return render(request, 'Staff/apply_leave.html', context)


def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date= request.POST.get('leave_date')
        leave_message= request.POST.get('leave_message')
        
        staff= Staff.objects.get(admin= request.user.id)
        
        leave= Staff_leave(
            staff_id= staff,
            date= leave_date,
            message= leave_message,   
        )
        leave.save()
        messages.success(request, 'Apply for leave Successfully')
        return redirect('staff_apply_leave')
    return render(request, 'Staff/apply_leave.html')


def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin = request.user.id)

    subjects = Subject.objects.filter(staff_id = staff)
    print(subjects)
    semester_year = Semester_Year.objects.all()
    course = Course.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_semester = None
    get_course= None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            semester_year_id = request.POST.get('semester_year_id')
            course_id = request.POST.get('course_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_semester = Semester_Year.objects.get(id = semester_year_id)
            get_course= Course.objects.get(id= course_id)
            subjects= Subject.objects.filter(id= subject_id)
            for i in subjects:
                student_id = i.course.id, i.semester_year.id
                students = Student.objects.filter(semester_year_id = student_id, course_id= student_id)
                print(students)

    context = {
        'subjects':subjects,
        'semester_year':semester_year,  
        'course': course,
        'action':action,
        'get_subject':get_subject,
        'get_semester':get_semester,
        'get_course': get_course,
        'students':students,
    }

    return render(request,'Staff/add_result.html',context)

def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        course_id = request.POST.get('subject_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_course = Course.objects.get(id= course_id)

        check_exist = Student_Exam_Result.objects.filter(subject_id=get_course, student_id=get_student).exists()
        if check_exist:
            result = Student_Exam_Result.objects.get(subject_id=get_course, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_marks = Exam_mark
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('staff_add_result')
        else:
            result = Student_Exam_Result(
                student_id=get_student, 
                subject_id=get_course, 
                exam_marks=Exam_mark, 
                assignment_mark= assignment_mark
                )
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')
        

def ADD_DOCUMENT(request):
    subject= Subject.objects.all()
    context={
            'subject': subject
        }
    if request.method == 'POST':    
        subject_name= request.POST.get('subject_name')
        document= request.FILES.get('document')
        message= request.POST.get('message')
        subject= Subject.objects.get(id= subject_name)
        
        document_save= Document_File(
            subject_name= subject,
            document= document,
            message=message
        )
        document_save.save()
        messages.success(request, 'Documents Upload Successsfully!')
        return redirect('add_document')
       
    return render(request, 'Staff/document.html', context)


def ADD_BUS_DETAILS(request):
    if request.method == 'POST':
        bus_code= request.POST.get('bus_code')
        bus_route= request.POST.get('bus_route')
        bus_type= request.POST.get('bus_type')
        bus_fair= request.POST.get('bus_fair')

        bus_details= BusDetails(
            bus_code= bus_code,
            bus_route= bus_route,
            bus_type= bus_type,
            bus_fair= bus_fair
        )
        bus_details.save()
        messages.success(request, 'Bus Details Added Successfully')
        return redirect('add_bus_details')
    return render(request, 'Staff/add_bus_details.html')

def VIEW_BUS_DETAILS(request):
    bus_details= BusDetails.objects.all()
    context= {
        'bus_details': bus_details,
    }
    
    return render(request, 'Staff/view_bus_details.html', context)


def EDIT_BUS_DETAILS(request, id):
    bus= BusDetails.objects.get(id= id)
    context={
        'bus': bus,
    }
    return render(request, 'Staff/edit_bus_details.html', context)

def UPDATE_BUS_DETAILS(request):
    if request.method == 'POST':
        bus_id= request.POST.get('bus_id')
        bus_code= request.POST.get('bus_code')
        bus_type= request.POST.get('bus_type')
        bus_fair= request.POST.get('bus_fair')
        bus_route= request.POST.get('bus_route')


        
        bus= BusDetails.objects.get(id= bus_id)
        bus.bus_code= bus_code
        bus.bus_type= bus_type
        bus.bus_fair= bus_fair
        bus.bus_route= bus_route
        bus.save()
        messages.success(request, 'Bus Details Updated Successfully')
        return redirect('view_bus_details')
    return render(request, 'Staff/view_bus_details.html')
    
def DELETE_BUS_DETAILS(request, id):
    bus= BusDetails.objects.get(id= id)
    bus.delete()
    messages.success(request, 'Bus Details Deleted Successfully')
    return redirect('view_bus_details')


def ADD_HOSTEL_DETAILS(request):
    if request.method == 'POST':
        hostel_block= request.POST.get('hostel_block')
        hostel_for= request.POST.get('hostel_for')
        hostel_fair= request.POST.get('hostel_fair')
        hostel_type= request.POST.get('hostel_type')
        hostel_room_bed= request.POST.get('hostel_room_bed')

        hostel_details= HostelDetails(
            hostel_block= hostel_block,
            hostel_for= hostel_for,
            hostel_fair= hostel_fair,
            hostel_type= hostel_type,
            hostel_room_bed= hostel_room_bed
        )
        hostel_details.save()
        messages.success(request, 'Hostel Details Added Successfully')
        return redirect('add_hostel_details')
    return render(request, 'Staff/add_hostel_details.html')

def VIEW_HOSTEL_DETAILS(request):
    hostel_details= HostelDetails.objects.all()
    context= {
        'hostel_details': hostel_details,
    }
    
    return render(request, 'Staff/view_hostel_details.html', context)


def EDIT_HOSTEL_DETAILS(request, id):
    hostel= HostelDetails.objects.get(id= id)
    context={
        'hostel': hostel,
    }
    return render(request, 'Staff/edit_hostel_details.html', context)


def UPDATE_HOSTEL_DETAILS(request):
    if request.method == 'POST':
        hostel_id= request.POST.get('hostel_id')
        hostel_block= request.POST.get('hostel_block')
        hostel_for= request.POST.get('hostel_for')
        hostel_fair= request.POST.get('hostel_fair')
        hostel_type= request.POST.get('hostel_type')
        hostel_room_bed= request.POST.get('hostel_room_bed')


        
        hostel= HostelDetails.objects.get(id= hostel_id)
        hostel.hostel_block= hostel_block
        hostel.hostel_for= hostel_for
        hostel.hostel_fair= hostel_fair
        hostel.hostel_type= hostel_type
        hostel.hostel_room_bed= hostel_room_bed
        hostel.save()
        messages.success(request, 'Hostel Details Updated Successfully')
        return redirect('view_hostel_details')
    return render(request, 'Staff/view_hostel_details.html')


def DELETE_HOSTEL_DETAILS(request, id):
    hostel= HostelDetails.objects.get(id= id)
    hostel.delete()
    messages.success(request, 'Hostel Details Deleted Successfully')
    return redirect('view_hostel_details')

def STAFF_VIEW_TIME_TABLE(request):
    time_table= Timetabel.objects.all()
    context= {
        'time_table': time_table,
    }
    return render(request, 'Staff/view_staff_time_table.html', context)

