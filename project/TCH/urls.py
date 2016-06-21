from django.conf.urls import patterns, url
from TCH import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^view_course/$', views.view_course, name='view_course'),
	url(r'^all_view_course/$', views.all_view_course, name='all_view_course'),
	url(r'^mdl_marks/$', views.mdl_marks, name='mdl_marks'),
	url(r'^get_mdl_course_marks/$', views.get_mdl_course_marks, name='get_mdl_course_marks'),

	url(r'^upload_local_marks_view/$', views.upload_local_marks_view, name='upload_local_marks_view'),
	url(r'^get_exam_type/$', views.get_exam_type, name='get_exam_type'),

	url(r'^insert_evaluation_marks/$', views.insert_evaluation_marks, name='insert_evaluation_marks'),
	
	url(r'^update_local_marks_view/$', views.update_local_marks_view, name='update_local_marks_view'),
	url(r'^update_get_exam_type/$', views.update_get_exam_type, name='update_get_exam_type'),

	url(r'^get_student_marks/$', views.get_student_marks, name='get_student_marks'),
	url(r'^update_student_marks/$', views.update_student_marks, name='update_student_marks'),

	url(r'^teacher_registration/$', views.teacher_registration, name='teacher_registration'),
	url(r'^insert_teacher_info/$', views.insert_teacher_info, name='insert_teacher_info'),

	url(r'^admin_registration/$', views.admin_registration, name='admin_registration'),
	url(r'^insert_admin_info/$', views.insert_admin_info, name='insert_admin_info'),
)


#url(r'^add_department/$', views.add_department, name='add_department'),

