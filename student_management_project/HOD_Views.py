from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages



@login_required(login_url='/')
def HOME(request):
    student_count= Student.objects.all().count()
    staff_count= Staff.objects.all().count()
    course_count= Course.objects.all().count()
    subject_count= Subject.objects.all().count()
    
    student_gender_male= Student.objects.filter(gender= 'male').count()
    student_gender_female= Student.objects.filter(gender= 'female').count()
    context={
        "student_count": student_count,
        "staff_count": staff_count,
        "course_count": course_count,
        "subject_count": subject_count,
        "student_gender_male": student_gender_male,
        "student_gender_female": student_gender_female,
    }
    return render(request, 'HOD/home.html', context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    
    course= Course.objects.all()
    session_year= Session_Year.objects.all()
    semester= Semester_Year.objects.all()
    
    if request.method == 'POST':
        profile_pic= request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        session_year_id= request.POST.get('session_year_id')
        semester_year_id= request.POST.get('semester_year_id')
        course_id= request.POST.get('course_id')
        enr= request.POST.get('enr')
        
        if CustomUser.objects.filter(email= email).exists():
            messages.warning(request, 'Email Alreday Taken !')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username Already Talen !")
            return redirect('add_student')
        else:
            user= CustomUser(
                first_name= first_name,
                last_name= last_name,
                username= username,
                email= email,
                profile_pic= profile_pic,
                user_type= 3,
                
            )
            user.set_password(password)
            user.save()
            
            course= Course.objects.get(id= course_id)
            session_year= Session_Year.objects.get(id= session_year_id)
            semester_year= Semester_Year.objects.get(id= semester_year_id)
            
            student= Student(
                admin= user,
                address= address,
                course_id= course,
                session_year_id= session_year,
                semester_year_id= semester_year,
                gender= gender,
                enr= enr
            )
            student.save()
            messages.success(request, user.first_name + ' ' + user.last_name + 'is Added Successfully!')
            return redirect('add_student')
    context= {
        'course': course,
        'session_year' : session_year,
        'semester' : semester
    }
    return render(request, 'HOD/add_student.html', context)

#students view function

def VIEW_STUDENT(request):
    student= Student.objects.all()
    context= {
        'student': student
    }
    return render(request, 'HOD/view_student.html', context)


#function for edit student
def EDIT_STUDENT(request, id):
    student= Student.objects.filter(id= id)
    course= Course.objects.all()
    semester= Semester_Year.objects.all()
    session_year= Session_Year.objects.all()    
    context={
        'student': student,
        'course': course,
        'semester': semester,
        'session_year': session_year
    }
    return render(request, 'HOD/edit_student.html', context)

#function for update student
def UPDATE_STUDENT(request):
    if request.method == 'POST':
        student_id= request.POST.get('student_id')
        profile_pic= request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        session_year_id= request.POST.get('session_year_id')
        semester_year_id= request.POST.get('semester_year_id')
        course_id= request.POST.get('course_id')
        enr= request.POST.get('enr')
        
        user= CustomUser.objects.get(id= student_id)
        
        user.first_name= first_name
        user.last_name= last_name
        user.email= email
        user.username= username
        
        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic= profile_pic
            
        user.save()
        
        student= Student.objects.get(admin= student_id)
        student.address= address
        student.gender= gender
        student.enr= enr
        
        course= Course.objects.get(id= course_id)
        student.course_id= course
        
        session_year= Session_Year.objects.get(id= session_year_id)
        student.session_year_id= session_year
        
        semester_year= Semester_Year.objects.get(id= semester_year_id)
        student.semester_year_id= semester_year
        
        student.save()
        messages.success(request, 'Student is Successfully Updated')
        return redirect('view_student')
        

    return render(request, 'HOD/edit_student.html')


#function for delete student
def DELETE_STUDENT(request, admin):
    student= CustomUser.objects.filter(id= admin)
    student.delete()
    messages.success(request, 'Student is Deleted Successfully!')
    return redirect('view_student')

#add course function

def ADD_COURSE(request):
    if request.method == 'POST':
        course_name= request.POST.get('course_name')
        
        course= Course(
            name= course_name,
        )
        course.save()
        messages.success(request, "Course Is Added Successfully!")
        return redirect('add_course')
    return render(request, 'HOD/add_course.html')


def VIEW_COURSE(request):
    course= Course.objects.all()
    context={
        'course': course
    }
    return render(request, 'HOD/view_course.html', context)

def EDIT_COURSE(request, id):
    course= Course.objects.get(id= id)
    context={
        'course': course
    }
    return render(request, 'HOD/edit_course.html', context)

def UPDATE_COURSE(request):
    if request.method == 'POST':
        course_id= request.POST.get('course_id')
        name= request.POST.get('name')
        
        course= Course.objects.get(id= course_id)
        course.name= name
        course.save()
        messages.success(request, 'Course Updated Successfully')
        return redirect('view_course')
    return render(request, 'HOD/edit_course.html')


def DELETE_COURSE(request, id):
    course= Course.objects.get(id= id)
    course.delete()
    messages.success(request, 'Course Deleted Successfully!')
    return redirect('view_course')

#staff related function

def ADD_STAFF(request):
    if request.method == 'POST':
        profile_pic= request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        
        if CustomUser.objects.filter(email= email).exists():
            messages.warning(request, 'Email Already Exists!')
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username= username).exists():
            messages.warning(request, 'Username Already Exists!')
            return redirect('add_staff')

        else:
            user= CustomUser(
                first_name= first_name,
                last_name= last_name,
                username= username,
                password= password,
                profile_pic= profile_pic,
                email= email,
                user_type= 2
            )
            user.set_password(password)
            user.save()
            
            staff= Staff(
                admin= user,
                address= address,
                gender= gender,
            )
            staff.save()
            messages.success(request, 'Staff is Successfully Added!')
            return redirect('add_staff')
    return render(request, 'HOD/add_staff.html')

def EDIT_STAFF(request, id):
    staff= Staff.objects.get(id= id)
    context={
        'staff': staff
    }
    return render(request, 'HOD/edit_staff.html', context)

def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id= request.POST.get('staff_id')
        profile_pic= request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        
        user= CustomUser.objects.get(id= staff_id)
        user.first_name= first_name
        user.last_name= last_name
        user.email= email
        user.username= username
        
        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic= profile_pic
            
        user.save()
        
        staff= Staff.objects.get(admin= staff_id)
        
        staff.gender= gender
        staff.address= address
        staff.save()
        messages.success(request, "Staff is Updated Successfully!")
        return redirect('view_staff')
    return render(request, 'HOD/edit.html')

def VIEW_STAFF(request):
    staff= Staff.objects.all()
    context= {
        'staff': staff
    }
    return render(request, 'HOD/view_staff.html', context)

def DELETE_STAFF(request, admin):
    staff= CustomUser.objects.get(id= admin)
    staff.delete()
    messages.success(request, 'Staff is Deleted Successfully!')
    return redirect('view_staff')

#functions for subjects

def ADD_SUBJECT(request):
    course= Course.objects.all()
    staff= Staff.objects.all()
    semester= Semester_Year.objects.all()
    context={
        'course': course,
        'staff': staff,
        'semester': semester,
    }
    if request.method == 'POST':
        subject_name= request.POST.get('subject_name')
        course_id= request.POST.get('course_id')
        staff_id= request.POST.get('staff_id')
        semester_id= request.POST.get('semester_id')

        course= Course.objects.get(id= course_id)
        staff= Staff.objects.get(id= staff_id)
        semester= Semester_Year.objects.get(id= semester_id)
        
        subject= Subject(
            name= subject_name,
            course= course,
            staff= staff,
            semester_year= semester,
        )
        subject.save()
        messages.success(request, 'Subject Added Successfully!')
        return redirect('add_subject')
    return render(request, "HOD/add_subject.html", context)


def VIEW_SUBJECT(request):
    subject= Subject.objects.all()
    context= {
        'subject': subject
    }
    return render(request, 'HOD/view_subject.html', context)


def EDIT_SUBJECT(request,id):
    subject= Subject.objects.get(id= id)
    course= Course.objects.all()
    staff= Staff.objects.all()
    semester= Semester_Year.objects.all()
    
    context= {
        'subject': subject,
        'course': course,
        'staff': staff,
        'semester': semester,
    }
    return render(request, 'HOD/edit_subject.html', context)

def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        subject_id= request.POST.get('subject_id')
        subject_name= request.POST.get('subject_name')
        course_id= request.POST.get('course_id')
        staff_id= request.POST.get('staff_id')
        semester_id= request.POST.get('semester_id')
        
        course= Course.objects.get(id= course_id)
        staff= Staff.objects.get(id= staff_id)
        semester= Semester_Year.objects.get(id= semester_id)
        subject= Subject(
            id= subject_id,
            name= subject_name,
            course= course,
            staff= staff,
            semester_year= semester,
        )
        subject.save()
        messages.success(request, 'Subject Updated Successfully!')
        return redirect('view_subject')
        
        
def DELETE_SUBJECT(request, id):
    subject= Subject.objects.filter(id= id)
    subject.delete()
    messages.success(request, 'Course Deleted Successfully!')
    return redirect('view_subject')
    
    
#function for sessions

def ADD_SESSION(request):
    if request.method == 'POST':
        session_year_start= request.POST.get("session_year_start")
        session_year_end = request.POST.get("session_year_end")

        session= Session_Year(
            session_start= session_year_start,
            session_end= session_year_end
        )
        session.save()
        messages.success(request, "Session Added Successfully!")
        return redirect('add_session')
    return render(request, 'HOD/add_session.html')

def EDIT_SESSION(request, id):
    session= Session_Year.objects.filter(id= id)
    context= {
        'session': session,
    }
    return render(request, 'HOD/edit_session.html', context)

def UPDATE_SESSION(request):
    session_id= request.POST.get('session_id')
    session_year_start= request.POST.get("session_year_start")
    session_year_end = request.POST.get("session_year_end")
    
    session= Session_Year.objects.get(id= session_id)
    session.session_start= session_year_start
    session.session_end= session_year_end
    session.save()
    messages.success(request, "Session Updated Successfully!")
    return redirect("view_session")
    

def VIEW_SESSION(request):
    session= Session_Year.objects.all()
    context= {
        'session': session,
    }
    return render(request, 'HOD/view_session.html', context)

def DELETE_SESSION(request, id):
    session= Session_Year.objects.get(id= id)
    session.delete()
    messages.success(request, 'Session Deleted Successfully!')
    return redirect('view_session')


def ADD_SEMESTER(request):
    if request.method == 'POST':
        semester_name= request.POST.get('semester_name')
        
        semester= Semester_Year(
            semester= semester_name,
        )
        semester.save()
        messages.success(request, "Semester Added Successfully!")
        return redirect('add_semester')
    return render(request, 'HOD/add_semester.html')


def VIEW_SEMESTER(request):
    semester= Semester_Year.objects.all()
    context={
        'semester': semester,
    }
    return render(request, 'HOD/view_semester.html', context)


def EDIT_SEMESTER(request, id):
    semester= Semester_Year.objects.filter(id= id)
    context= {
        'semester': semester
    }
    return render(request, 'HOD/edit_semester.html', context)


def UPDATE_SEMESTER(request):
    semester_id= request.POST.get('semester_id')
    semester_name= request.POST.get('semester_name')
    semester= Semester_Year.objects.get(id= semester_id)
    semester.semester= semester_name
    semester.save()
    messages.success(request, 'Semester Updated Successfully!')
    return render(request, 'HOD/edit_semester.html')


def DELETE_SEMESTER(request, id):
    semester= Semester_Year.objects.get(id= id)
    semester.delete()
    messages.success(request, 'Semester Deleted Successfully!')
    return redirect("view_semester")

def STAFF_SEND_NOTIFICATION(request):
    staff= Staff.objects.all()
    seen_notification= Staff_Notification.objects.all().order_by('-id')[0:5]
    context= {
        'staff': staff,
        'seen_notificatiion': seen_notification
    }
    return render(request, 'HOD/staff_notification.html', context)

def SAVE_STAFF_NOTIFICATION(request):
    if request.method == 'POST':
        staff_id= request.POST.get('staff_id')
        message_staff= request.POST.get('message')
        print(staff_id, message_staff)
        
        staff= Staff.objects.get(admin= staff_id)
        notification= Staff_Notification(
            staff_id= staff,
            message= message_staff
        )
        
        notification.save()
        messages.success(request, 'Notification Sent Successfully!')
        return redirect('staff_send_notification')
    return render(request,'HOD/home.html')

def Staff_Leave_view(request):
    staff_leave= Staff_leave.objects.all()

    
    context= {
        'staff_leave': staff_leave,
        
    }
    return render(request, "HOD/staff_leave.html", context)

def STAFF_APPROVE_LEAVE(request, id):
    leave= Staff_leave.objects.get(id= id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')


def STAFF_DISAPPROVE_LEAVE(request, id):
    leave= Staff_leave.objects.get(id= id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')

#students related urls

def STUDENT_SEND_NOTIFICATION(request):
    student= Student.objects.all()
    seen_notificatiion= Student_Notifications.objects.all().order_by('-id')[0:5]
    

    context= {
        'student': student,
        'seen_notificatiion': seen_notificatiion
    }
    return render(request, 'HOD/student_notification.html', context)
    

    
def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == 'POST':
        message= request.POST.get('message')
        notification= Student_Notifications(
            message= message,
        )
        
        notification.save()
        messages.success(request, 'Notification Sent Successfully!')
        return redirect('student_send_notification')
    return render(request,'HOD/home.html')


def Student_Leave_view(request):
    student_leave= Student_leave.objects.all()
    
    context= {
        'student_leave': student_leave,
        
    }
    return render(request, "HOD/student_leave.html", context)

def STUDENT_APPROVE_LEAVE(request, id):
    leave= Student_leave.objects.get(id= id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')


def STUDENT_DISAPPROVE_LEAVE(request, id):
    leave= Student_leave.objects.get(id= id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')

def TIME_TABLE(request):
    staff= Staff.objects.all()
    course= Course.objects.all()
    subject= Subject.objects.all()
    
    if request.method == 'POST':
        teacher_id= request.POST['teacher_id']
        course_id= request.POST['course_id']
        subject_id= request.POST['subject_id']
        date= request.POST['date']
        start_time= request.POST['start_time']
        end_time= request.POST['end_time']
        
        teacher= Staff.objects.get(id= teacher_id)
        course2= Course.objects.get(id= course_id)
        subject2= Subject.objects.get(id= subject_id)
        time_table= Timetabel(
            date=date,
            start_time=start_time,
            end_time=end_time,
            teacher_id=teacher,
            course_id=course2,
            subject_id=subject2
            
        )
        time_table.save()
        messages.success(request, 'Time Table is Added Successfully!')
        return render(request, 'Hod/add_time_table.html')
        
    
    
    context= {
        'staff':staff,
        'course':course,
        'subject':subject
    }
    return render(request, 'Hod/add_time_table.html',context)

def VIEW_TIME_TABLE(request):
    time_table= Timetabel.objects.all()
    
    context= {
        'time_table': time_table
    }
    return render(request, 'Hod/view_time_table.html', context)


def NOTICE(request):
    return render(request, 'HOD/add_notice_student.html')

def ADD_STUDENT_NOTICE(request):
    if request.method == 'POST':
        student_notice= request.POST.get('student_notice')
        notice= Student_Notice(
            student_notice= student_notice
        )
        notice.save()
        messages.success(request, "Notice Added Successfully!")
        return redirect('add_student_notice')
    return render(request, 'HOD/add_notice_student.html')