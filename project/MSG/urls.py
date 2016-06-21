from django.conf.urls import patterns, url
from MSG import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),	
	url(r'^create_grade_policy/$', views.create_grade_policy, name='create_grade_policy'),
	url(r'^show_grade_policy/$', views.show_grade_policy, name='show_grade_policy'),
	url(r'^create_view/$', views.create_view, name='create_view'),					# call from index.html
	url(r'^view_view/$', views.view_view, name='view_view'),					# call from index.html
	url(r'^generate_template/$', views.generate_template, name='generate_template'),
	url(r'^generate_template_view/$', views.generate_template_view, name='generate_template_view'), # call from index.html
	url(r'^upload_template/$', views.upload_template, name='upload_template'),
	url(r'^upload_template_view/$', views.upload_template_view, name='upload_template_view'), # call from index.html

	url(r'^weight_view/$', views.weight_view, name='weight_view'), # call from index.html
	url(r'^success/$', views.success, name='success'),
	url(r'^read_bmpolicy/$', views.read_bmpolicy, name='read_bmpolicy'),
	url(r'^insert_weight/$', views.insert_weight, name='insert_weight'),
	url(r'^submit_bmpolicy/$', views.submit_bmpolicy, name='submit_bmpolicy'),
	url(r'^success_bmpolicy/$', views.success_bmpolicy, name='success_bmpolicy'),
	url(r'^generate_final_marksheet/$', views.generate_final_marksheet, name='generate_final_marksheet'),
	url(r'^create_composite_marksheet/$', views.create_composite_marksheet, name='create_composite_marksheet'),
	

	url(r'^upload_bmpolicy_view/$', views.upload_bmpolicy_view, name='upload_bmpolicy_view'),
	url(r'^insert_bmpolicy/$', views.insert_bmpolicy, name='insert_bmpolicy'),

	url(r'^upload_bmmarks_view/$', views.upload_bmmarks_view, name='upload_bmmarks_view'),

	url(r'^insert_bmmarks_view/$', views.insert_bmmarks_view, name='insert_bmmarks_view'),
	url(r'^insert_bmmarks/$', views.insert_bmmarks, name='insert_bmmarks'),

	url(r'^local_view/$', views.local_view, name='local_view'),
	url(r'^moocs_view/$', views.moocs_view, name='moocs_view'),

)




