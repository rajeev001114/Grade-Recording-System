from django.conf.urls import patterns, url
from ADM import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^add_department/$', views.add_department, name='add_department'),
	url(r'^create_department/$', views.create_department, name='create_department'),
	url(r'^view_department/$', views.view_department, name='view_department'),
	url(r'^remove_department_view/$', views.remove_department_view, name='remove_department_view'),
	url(r'^remove_department/$', views.remove_department, name='remove_department'),
	url(r'^reactive_department_view/$', views.reactive_department_view, name='reactive_department_view'),
	url(r'^reactive_department/$', views.reactive_department, name='reactive_department'),
	url(r'^add_course_view/$', views.add_course_view, name='add_course_view'),
	url(r'^add_course/$', views.add_course, name='add_course'),
	url(r'^validatelogin/$', views.validatelogin, name='validatelogin'),
	url(r'^success_add_course/$', views.success_add_course, name='success_add_course'),
	url(r'^view_course/$', views.view_course, name='view_course'),
	url(r'^get_course_list/$', views.get_course_list, name='get_course_list'),

	url(r'^deactive_course/$', views.deactive_course, name='deactive_course'),
	url(r'^reactive_course/$', views.reactive_course, name='reactive_course'),
	url(r'^view_academic_session/$', views.view_academic_session, name='view_academic_session'),
	url(r'^register_session/$', views.register_session, name='register_session'),
	url(r'^get_session/$', views.get_session, name='get_session'),
	url(r'^department_management/$', views.department_management, name='department_management'),
	url(r'^course_management/$', views.course_management, name='course_management'),
	url(r'^view_session_course/$', views.view_session_course, name='view_session_course'),
	url(r'^get_course_and_teacher/$', views.get_course_and_teacher, name='get_course_and_teacher'),
	url(r'^allocate_session_course/$', views.allocate_session_course, name='allocate_session_course'),
	url(r'^get_college_name/$', views.get_college_name, name='get_college_name'),

	url(r'^view_allcate_course/$', views.view_allcate_course, name='view_allcate_course'), ## from index
	url(r'^get_allcate_course/$', views.get_allcate_course, name='get_allcate_course'),
	
	url(r'^moodle_view/$', views.moodle_view, name='moodle_view'),
	url(r'^teacher_mapping/$', views.teacher_mapping, name='teacher_mapping'),
	url(r'^student_mapping/$', views.student_mapping, name='student_mapping'),
	url(r'^upload_teacher_mapping/$', views.upload_teacher_mapping, name='upload_teacher_mapping'),
	url(r'^upload_student_mapping/$', views.upload_student_mapping, name='upload_student_mapping'),


	url(r'^moodle_setup/$', views.moodle_setup, name='moodle_setup'),
	url(r'^moodle_binary/$', views.moodle_binary, name='moodle_binary'),
	url(r'^local_setup/$', views.local_setup, name='local_setup'),

)

#	url(r'^deactive_course/(.*)/$', views.deactive_course, name='deactive_course'),

