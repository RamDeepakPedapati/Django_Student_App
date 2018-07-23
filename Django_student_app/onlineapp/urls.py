from django.conf.urls import url


from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from onlineapp.view import *
from .view.college import *
from .view.students import *
from .view.auth import *
from .view.studentSerializerView import *
from .view.CollegeSerializerView import *
from rest_framework_jwt.views import *


app_name="onlineapp"



urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),


    # path('colleges/',CollegeView.as_view(),name="colleges_html"),

    path('colleges/', CollegeListView.as_view(), name="collegeshtml"),
    path('colleges/<int:pk>', CollegeDetailView.as_view(), name="collegesmarks"),

    # path('collegesdetail/<acronym>', CollegeDetailView.as_view(), name="collegesmarks"),

    # path('studentForm/',AddStudent.as_view(),name="colleges_html"),

    path('colleges/add',CreateCollegeView.as_view(),name="add_college"),
    path('colleges/<int:pk>/edit',UpdateCollegeView.as_view(),name="edit_college"),
    path('colleges/<int:pk>/delete',DeleteCollegeView.as_view(),name="delete_college"),

    path('colleges/<int:college_id>/students/add',CreateStudentView.as_view(),name="add_student"),
    path('colleges/<int:college_id>/students/<int:pk>/edit',UpdateStudentView.as_view(),name="edit_student"),
    path('colleges/<int:college_id>/students/<int:pk>/delete',DeleteStudentView.as_view(),name="delete_student"),
    path('signup/',SignUpView.as_view(),name='signup'),

    path('login/',LoginView.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),




    path('api/v1/college/',college_list,name='rest_college_list'),
    path('api/v1/college/<int:pk>/',college_detail,name='rest_college'),
    path('api/v1/college/<int:pk>/students/',AllStudentListApi.as_view(),name='rest_student'),
    path('api/v1/college/<int:pk>/students/<int:student_id>',StudentDetailApi.as_view(),name='college_student'),
    path('api/v1/api-auth-token/',obtain_jwt_token),


    url(r'^', TemplateView.as_view(template_name="index.html")),








    # path('',views.welcome),
    # path('hello/',views.hello, name='hello'),
    #
    # path('example/',views.some_view),
    # path('colleges/',views.college_details),
    # path('college/',views.colleges),
    # path('clg_index/', views.clg_index),
    # path('tic_tac_toe/',views.tic_tac_toe),
    # path('student_details/',views.student_details),
    # path('student_detail/',views.student_detail),
    # path('student_detail/<int:value>',views.student_detail),
    # path('student_total/',views.student_total),
    # path('clg_stats/<str:clg>',views.college_stats),
    # path('students/',views.students),
    # path('profile/<int:id>',views.Profile),
    # path('testsession/',views.test_session),
    # path('testing/',views.test)
    # path('welcome/', views.index,name='index')
]