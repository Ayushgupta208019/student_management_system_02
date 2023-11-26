"""student_management_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from student_management_project import HOD_Views, Staff_Views, Student_Views, views
from app import app_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('about-us', views.ABOUT_US, name='about-us'),
    
    #login logout path section
    path('', views.LOGIN, name='login'),
    path('dologin', views.dologin, name='dologin'),
    path('dologout', views.dologout, name='logout'),
    
    #This path is for HOD panel!!!
    path('Hod/home', HOD_Views.HOME, name="hod_home"),
    path('Hod/Student/Add', HOD_Views.ADD_STUDENT, name="add_student"),
    path('HOD/Student/View', HOD_Views.VIEW_STUDENT, name='view_student'),
    path('HOD/Student/Edit/<str:id>', HOD_Views.EDIT_STUDENT, name='edit_student'),
    path('HOD/Student/Update', HOD_Views.UPDATE_STUDENT, name='update_student'),
    path('HOD/Student/Delete/<str:admin>', HOD_Views.DELETE_STUDENT, name='delete_student'),
    
    path('HOD/Course/Add', HOD_Views.ADD_COURSE, name='add_course'),
    path('HOD/Course/View', HOD_Views.VIEW_COURSE, name='view_course'),
    path('HOD/Course/Edit/<str:id>', HOD_Views.EDIT_COURSE, name="edit_course"),
    path('HOD/Course/Update', HOD_Views.UPDATE_COURSE, name="update_course"),
    path('HOD/Course/Delete/<str:id>', HOD_Views.DELETE_COURSE, name='delete_course'),
    
    path('HOD/Staff/Add', HOD_Views.ADD_STAFF, name='add_staff'),
    path('HOD/Staff/View', HOD_Views.VIEW_STAFF, name= 'view_staff'),
    path('HOD/Staff/Edit/<str:id>', HOD_Views.EDIT_STAFF, name= 'edit_staff'),
    path('HOD/Update/Staff', HOD_Views.UPDATE_STAFF, name="update_staff"),
    path('HOD/Delete/Staff/<str:admin>', HOD_Views.DELETE_STAFF, name="delete_staff"),
    
    path('HOD/Subject/Add', HOD_Views.ADD_SUBJECT, name="add_subject"),
    path('HOD/Subject/View', HOD_Views.VIEW_SUBJECT, name="view_subject"),
    path('HOD/Subject/Edit/<str:id>', HOD_Views.EDIT_SUBJECT, name="edit_subject"),
    path('HOD/Subject/Edit', HOD_Views.UPDATE_SUBJECT, name="update_subject"),
    path('HOD/Subject/Delete/<str:id>', HOD_Views.DELETE_SUBJECT, name="delete_subject"),
    
    path('HOD/Session/Add', HOD_Views.ADD_SESSION, name="add_session"),
    path('HOD/Session/View', HOD_Views.VIEW_SESSION, name="view_session"),
    path('HOD/Session/Edit/<str:id>', HOD_Views.EDIT_SESSION, name="edit_session"),
    path('HOD/Session/update', HOD_Views.UPDATE_SESSION, name="update_session"),
    path('HOD/Session/Delete/<str:id>', HOD_Views.DELETE_SESSION, name="delete_session"),
    
    path('HOD/Semester/Add', HOD_Views.ADD_SEMESTER, name="add_semester"),
    path('HOD/Semester/View', HOD_Views.VIEW_SEMESTER, name="view_semester"),
    path('HOD/Semester/Edit/<str:id>', HOD_Views.EDIT_SEMESTER, name="edit_semester"),
    path('HOD/Semester/Update', HOD_Views.UPDATE_SEMESTER, name="update_semester"),
    path('HOD/Semester/Delete/<str:id>', HOD_Views.DELETE_SEMESTER, name="delete_semester"),
    path('HOD/Staff/Send_Notification', HOD_Views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('HOD/Staff/Save_Notification', HOD_Views.SAVE_STAFF_NOTIFICATION, name="save_staff_notification"),
    path('HOD/Staff/Leave_view', HOD_Views.Staff_Leave_view, name="staff_leave_view"),
    path('HOD/Staff/approve_leave/<str:id>', HOD_Views.STAFF_APPROVE_LEAVE, name="staff_approve_leave"),
    path('HOD/Staff/disapprove_leave/<str:id>', HOD_Views.STAFF_DISAPPROVE_LEAVE, name="staff_disapprove_leave"),
    
    path('HOD/Student/send_notification', HOD_Views.STUDENT_SEND_NOTIFICATION, name="student_send_notification"),
    path('HOD/Student/save_notification', HOD_Views.SAVE_STUDENT_NOTIFICATION, name="save_student_notification"),
    
    path('HOD/Student/Leave_view', HOD_Views.Student_Leave_view, name="student_leave_view"),
    path('HOD/Student/approve_leave/<str:id>', HOD_Views.STUDENT_APPROVE_LEAVE, name="student_approve_leave"),
    path('HOD/Student/disapprove_leave/<str:id>', HOD_Views.STUDENT_DISAPPROVE_LEAVE, name="student_disapprove_leave"),
    path('HOD/Time_Table/Add', HOD_Views.TIME_TABLE, name="time_table"),
    path('HOD/Time_Table/View', HOD_Views.VIEW_TIME_TABLE, name="view_time_table"),
    path('HOD/Notice/Add', HOD_Views.ADD_STUDENT_NOTICE, name= 'add_student_notice'),
    path('HOD/Notice', HOD_Views.NOTICE, name= 'notice'),
    

    


    
    
    #this is staff urls.
    path('Staff/home', Staff_Views.HOME, name='staff_home'),
    path('Staff/Notifications', Staff_Views.NOTIFICATIONS, name="staff_notifications"),
    path('Staff/mark_as_done/<str:status>', Staff_Views.STAFF_NOTIFICATION_MARK_AS_DONE, name="staff_notification_mark_as_done"),
    path('Staff/Apply_leave', Staff_Views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('Staff/Apply_leave_save', Staff_Views.STAFF_APPLY_LEAVE_SAVE, name="staff_apply_leave_save"),
    
    path('Staff/Add/Result', Staff_Views.STAFF_ADD_RESULT, name="staff_add_result"),
    path('Staff/Save/Result', Staff_Views.STAFF_SAVE_RESULT, name="staff_save_result"),
    
    path('Staff/Add/Document', Staff_Views.ADD_DOCUMENT, name="add_document"),
    path('Staff/Add/Bus_Detail', Staff_Views.ADD_BUS_DETAILS, name='add_bus_details'),
    path('Staff/View/Bus_Detail', Staff_Views.VIEW_BUS_DETAILS, name='view_bus_details'),
    path('Staff/Bus/Edit/<str:id>', Staff_Views.EDIT_BUS_DETAILS, name="edit_bus_details"),
    path('Staff/Bus/Edit', Staff_Views.UPDATE_BUS_DETAILS, name="update_bus_details"),
    path('Staff/Bus/Delete/<str:id>', Staff_Views.DELETE_BUS_DETAILS, name="delete_bus_details"),
    path('Staff/Add/hosetl_details', Staff_Views.ADD_HOSTEL_DETAILS, name='add_hostel_details'),
    path('Staff/View/hostel_Detail', Staff_Views.VIEW_HOSTEL_DETAILS, name='view_hostel_details'),
    path('Staff/Hostel/Edit/<str:id>', Staff_Views.EDIT_HOSTEL_DETAILS, name="edit_hostel_details"),
    path('Staff/Hostel/Edit', Staff_Views.UPDATE_HOSTEL_DETAILS, name="update_hostel_details"),
    path('Staff/Hostel/Delete/<str:id>', Staff_Views.DELETE_HOSTEL_DETAILS, name="delete_hostel_details"),
    path('Staff/View/Time_Table', Staff_Views.STAFF_VIEW_TIME_TABLE, name="staff_time_table"),
    


    
    
    #this is studenrs urls.
    path('Student/home', Student_Views.HOME, name= "student_home"),
    path('Student/Notifications', Student_Views.NOTIFICATIONS, name="notifications"),
    path('Student/Apply_leave', Student_Views.STUDENT_APPLY_LEAVE, name='student_apply_leave'),
    path('Student/Apply_leave_save', Student_Views.STUDENT_APPLY_LEAVE_SAVE, name="student_apply_leave_save"),
    path('Student/View/Result', Student_Views.VIEW_RESULT, name='view_result'),
    path('Student/View/Document', Student_Views.VIEW_DOCUMENT, name="view_document"),
    path('Student/View/Bus_Details', Student_Views.BUS_DETAILS, name="bus_details"),
    path('Student/View/Hostel_Details', Student_Views.HOSTEL_DETAILS, name="hostel_details"),
    path('Student/View/Time_Table', Student_Views.STUDENT_VIEW_TIME_TABLE, name="student_time_table"),



    

    #This path related to user's profile
    path('Profile', views.User_Profile, name='Profile'),
    path('Profile_update', views.PROFILE_UPDATE, name="profile_update"),
    
    path('chatbot', app_views.chatbot, name='chatbot'),

    
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

