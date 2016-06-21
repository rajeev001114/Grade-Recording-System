from django.shortcuts import render,render_to_response
from django.template import Context, loader
# Create your views here.
import json
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#from ADM.validations import *
from ADM.models import *
from TCH.models import *
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def index(request):
	'''
	Return to admin index page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/index.html', context_dict)


def login(request):
	'''
	Return to login page.
	'''
	return render(request, 'tologin.html')


def moodle_setup(request):
	'''
	Return to Moodle setting page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/moodle_setup.html', context_dict)


def local_setup(request):
	'''
	Return to local system setting page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/local_setup.html', context_dict)


def get_college_name(request):
	'''
	Get college name from file
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	import os
	path = os.path.dirname(os.path.realpath(__file__))
	f = open(path + '/collegename.txt')
	return HttpResponse(f.read())


def add_department(request):
	'''
	Return to add department page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')	
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.all()
	count = query_results.count()
	context_dict  = { 'count':count , 'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/add_department.html' , context_dict)


def view_department(request):
	'''
	Return to view department page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	count = query_results.count()
	context_dict  = { 'count':count , 'query_results':query_results , 'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/view_department.html' , context_dict)


def remove_department_view(request):
	'''
	Return to remove department page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	count = query_results.count()
	context_dict  = { 'count':count , 'query_results':query_results , 'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/remove_department.html' , context_dict)


def reactive_department_view(request):
	'''
	Return to reactive department page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 0)
	count = query_results.count()
	context_dict  = { 'count':count , 'query_results':query_results , 'email':email , 'name':name, 'rolename':rolename}
	return render(request, 'adm/reactive_department.html' , context_dict)


def add_course_view(request):
	'''
	Return to add course page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	count = query_results.count()
	context_dict  = { 'count':count , 'query_results':query_results , 'email':email , 'name':name, 'rolename':rolename}
	return render(request, 'adm/add_course.html' , context_dict)


def success_add_course(request):
	'''
	Return to success page after adding course.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	ccount = request.GET["ccount"]
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'success': "You have successfully  added all the course" ,'ccount': ccount  , 'email':email , 'name':name, 'rolename':rolename}
	return render(request, 'adm/success.html', context_dict )


def view_course(request):
	'''
	Return to view course page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	count = query_results.count()
	context_dict  = { 'count':count , 'query_results':query_results , 'email':email , 'name':name, 'rolename':rolename}
	return render(request, 'adm/view_course.html' , context_dict)


def view_academic_session(request):
	'''
	Return to add academic session page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	year_list = ['2014-15','2015-16', '2016-17', '2017-18', '2018-19']
	sem_list = [1,2,3]
	query_results = Academic_session.objects.all()
	count = query_results.count()
	context_dict  = { 'count':count , 'year_list':year_list , 'sem_list':sem_list, 'email':email , 'name':name, 'rolename':rolename}
	return render(request, 'adm/academic_session.html' , context_dict)


def department_management(request):
	'''
	Return to department main page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict  = { 'email':email , 'name':name, 'rolename':rolename}
	return render(request, 'adm/department_management.html' , context_dict)


def course_management(request):
	'''
	Return to course main page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict  = { 'email':email , 'name':name, 'rolename':rolename}
	return render(request, 'adm/course_management.html' , context_dict)


def view_session_course(request):
	'''
	Return to view session course page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	context_dict  = {  'email':email , 'name':name , 'rolename':rolename, 'query_results':query_results}
	return render(request, 'adm/session_course_assignment.html' , context_dict)


def view_allcate_course(request):
	'''
	Return to view allocate course page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	context_dict  = {  'email':email , 'name':name , 'rolename':rolename, 'query_results':query_results}
	return render(request, 'adm/view_allocate_course.html' , context_dict)


def moodle_view(request):
	'''
	Return to Moodle page.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict  = {  'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/mapping.html' , context_dict)


def teacher_mapping(request):
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict  = {  'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/teacher_mapping.html' , context_dict)


def student_mapping(request):
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict  = {  'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'adm/student_mapping.html' , context_dict)


################################################        create department function ################################################################ 


def create_department(request):
	'''
	Create department in local system.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		a= request.POST
		rolename =  request.session['rolename']
		email = request.session['email_id']
		name = request.session['name']
		myDict = {}
		for key in a.iterkeys():
			myDict = dict(a.iterlists())	
		if 'csrfmiddlewaretoken' in myDict:	
			del myDict['csrfmiddlewaretoken']
		dp_name = myDict['dpname'][0]
		dp_abb = myDict['dpabb'][0]
		if not dp_name[0].isalpha():
			context_dict = {'error': "*ERROR-: " + str(dp_name) + " department name should start from character only " ,  'dp_name':dp_name, 'dp_abb':dp_abb , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/add_department.html', context_dict ) 
		if not dp_abb[0].isalpha():
			context_dict = {'error': "*ERROR-: " + str(dp_name) + " department abbreviation should start from character only " ,  'dp_name':dp_name, 'dp_abb':dp_abb , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/add_department.html', context_dict ) 
		dp_name = dp_name.rstrip()	
		dp_abb = dp_abb.rstrip()
		query_results = All_deprtment.objects.all()
		count = query_results.count()
		if count > 0:
			for item in query_results:
				if(item.department_name == dp_name):
					context_dict = {'error': "*ERROR-: " + str(dp_name) + " department name already exist, choose other name " ,  'dp_name':dp_name, 'dp_abb':dp_abb , 'count':count , 'email':email , 'name':name , 'rolename':rolename}
					return render(request, 'adm/add_department.html', context_dict ) 
				if(item.department_abb == dp_abb):
					context_dict = {'error': "*ERROR-: " + str(dp_abb) + " department abbreviation already exist, choose other abbreviation",'dp_name':dp_name, 'dp_abb':dp_abb , 'count':count , 'email':email , 'name':name , 'rolename':rolename }
					return render(request, 'adm/add_department.html', context_dict ) 
		p = All_deprtment.objects.create(department_name=dp_name, department_abb=dp_abb)
		p.save()
		context_dict = {'success': " You have successfully added " + str(dp_name) + " department" , 'email':email , 'name':name , 'rolename':rolename}
		return render(request, 'adm/add_department.html' , context_dict)
	else:
		return HttpResponse("Not allowed !!!!. .")


################################################        remove department function ################################################################ 


def remove_department(request):
	'''
	Remove department in local system.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		a= request.POST
		dp_name = request.POST['dpname']
		query_results = All_deprtment.objects.filter(is_active = 1)
		count = query_results.count()
		if dp_name == 'select':
			contex_dict  = {'query_results':query_results, 'count':count, 'error':" You have not selected any department"}
			return render(request, 'adm/remove_department.html', contex_dict)
		All_deprtment.objects.filter(department_name=dp_name).update(is_active=False)
		contex_dict  = { 'count':count , 'query_results':query_results , 'success': " You have successfully deactivate  " + str(dp_name) + " department" , 'email':email , 'name':name , 'rolename':rolename}
		return render(request, 'adm/remove_department.html' , contex_dict) 
	else:
		return HttpResponse("Not allowed !!!!. ")


################################################        reactive department function ################################################################ 


def reactive_department(request):
	'''
	Reactivte department in local system.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		a= request.POST
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		dp_name = request.POST['dpname']
		query_results = All_deprtment.objects.filter(is_active = 0)
		count = query_results.count()
		if dp_name == 'select':
			contex_dict  = {'query_results':query_results, 'count':count, 'error':" You have not selected any department" , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/reactive_department.html', contex_dict)
		All_deprtment.objects.filter(department_name=dp_name).update(is_active=True)
		contex_dict  = { 'count':count , 'query_results':query_results , 'success': " You have successfully reactivate   " + str(dp_name) + " department" , 'email':email , 'name':name , 'rolename':rolename}
		return render(request, 'adm/reactive_department.html' , contex_dict) 
	else:
		return HttpResponse("Not allowed !!!!.")


################################################        add course in  department function ################################################################ 


def add_course(request):
	'''
	Create course in department.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		a= request.POST
		for key in a.iterkeys():
			myDict = dict(a.iterlists())	
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		if 'csrfmiddlewaretoken' in myDict:	
			del myDict['csrfmiddlewaretoken']
		dp_name = myDict['dpname'][0]
		ccode_list = myDict['ccode']
		cname_list = myDict['cname']
		ccode_list = [item.rstrip() for item in ccode_list]
		cname_list = [item.rstrip() for item in cname_list]
		error_msg = ""
		for item in ccode_list:
			if item[0] == ' ' :
				error_msg = " Course code can not start with space"
		if(error_msg == ""):
			for item in cname_list:
				if item[0] == ' ' :
					error_msg = " Course Name can not start with space"
		query_results = All_course.objects.filter(dpname = dp_name )
		count = query_results.count()
		if(error_msg == "" and count > 0):
			for item in query_results:
				if(error_msg != ""):
					break
				else:
					for i in range(0 , len(cname_list)):
						if(item.course_code == ccode_list[i]):
							error_msg =  str(ccode_list[i]) + " course code already register"
							break
						if(item.course_name == cname_list[i]):
							error_msg =  str(cname_list[i]) + " course name already register"
							break
		if(error_msg != ""):
			json_data = json.dumps({"returnval":error_msg})
			return HttpResponse(json_data)	


		###################    INsert grade policy in db , foregin key vlue by parent modal
		aList = [All_course(dpname = All_deprtment.objects.get(department_name=dp_name), course_code=ccode_list[i],course_name=cname_list[i] ) for i in range(0,len(ccode_list))]
		All_course.objects.bulk_create(aList)
		ccount = len(cname_list)
		context_dict = {'success': "You have successfully  added one grade policy.", 'ccount':ccount }
		json_data = json.dumps({"returnval":"success","ccount":ccount})
		return HttpResponse(json_data)
	else:
		json_data = json.dumps({"returnval":"Not Post"})
		return HttpResponse(json_data)


################################################    get course list ################################################################ 


def get_course_list(request):
	'''
	Get course list.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		dp_name = request.POST['dpname']
		query_results = All_deprtment.objects.filter(is_active = 1)
		count = query_results.count()
		if dp_name == 'all':
			query_results1 = All_course.objects.filter(dpname__is_active=1 ) ## access using foreign key
			contex_dict  = {'query_results':query_results, 'query_results1':query_results1,'count':count, 'error':" You have not selected any department" , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/view_course.html', contex_dict)
		else:
			query_results1 = All_course.objects.filter(dpname=dp_name )
			contex_dict  = {'query_results':query_results, 'query_results1':query_results1,'count':count, 'error':" You have not selected any department" , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/view_course.html', contex_dict)
	else:
		return HttpResponse("Not allowed !!!!. ")


################################################        deactive course  ################################################################ 


def deactive_course(request):
	'''
	Remove course in department.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	location = request.GET.get('location')
	All_course.objects.filter(pk=location).update(is_active=False)
	cname = All_course.objects.filter(pk=location)[0].course_name
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	count = query_results.count()
	contex_dict  = { 'count':count , 'query_results':query_results , 'email':email , 'name':name , 'rolename':rolename , 'success': "You have successfuly deactive the course: " + str(cname)}
	return render(request, 'adm/view_course.html' , contex_dict)


################################################        reactive course  ################################################################ 


def reactive_course(request):
	'''
	Reactive course in department.
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	location = request.GET.get('location')
	All_course.objects.filter(pk=location).update(is_active=True)
	cname = All_course.objects.filter(pk=location)[0].course_name
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = All_deprtment.objects.filter(is_active = 1)
	count = query_results.count()
	contex_dict  = { 'count':count , 'query_results':query_results , 'email':email , 'name':name , 'rolename':rolename , 'success': "You have successfuly reactivate the course: " + str(cname)}
	return render(request, 'adm/view_course.html' , contex_dict)


################################################        register session  ################################################################ 


def register_session(request):
	'''
	Register session in system.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		a= request.POST
		year_list = ['2014-15','2015-16', '2016-17', '2017-18', '2018-19']
		sem_list = [1,2,3]
		session_year = request.POST['acdsession']
		sem = request.POST['sem']
		query_results = Academic_session.objects.all()
		count = query_results.count()
		q1 = Academic_session.objects.filter(year = session_year)
		c1  = q1.count()
		if count > 0:
			obj1 = Academic_session.objects.latest('year')
			temp_y = obj1.year
			index1 = year_list.index(session_year) 
			index2 =  year_list.index(temp_y) 
			if index1 > index2+1 or  index1 < index2:
				contex_dict  = { 'year_list':year_list , 'sem_list':sem_list, 'count':count, 'error':" Either this session is too old or skipping the session" , 'email':email , 'name':name , 'rolename':rolename}
				return render(request, 'adm/academic_session.html', contex_dict)
			if c1 == 0:
				temp_s = obj1.semester	
				if int(temp_s) == 1 or int(sem) == 2:
					contex_dict  = { 'year_list':year_list , 'sem_list':sem_list, 'count':count, 'error':" You are skkiping the semester" , 'email':email , 'name':name , 'rolename':rolename}
					return render(request, 'adm/academic_session.html', contex_dict)
		if c1 == 2:
			contex_dict  = { 'year_list':year_list , 'sem_list':sem_list, 'count':count, 'error':" This academic session is already completed" , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/academic_session.html', contex_dict)
		if c1 > 0:
			if int(q1[0].semester) == int(sem):
				contex_dict  = { 'year_list':year_list , 'sem_list':sem_list, 'count':count, 'error':" This  semester is already completed for this session" , 'email':email , 'name':name , 'rolename':rolename}
				return render(request, 'adm/academic_session.html', contex_dict)
		query_results = Academic_session.objects.filter(is_active = 1).update(is_active = 0)
		p = Academic_session.objects.create(year=session_year, semester = sem)
		p.save()
		contex_dict  = { 'year_list':year_list , 'sem_list':sem_list, 'count':count, 'success':" Your have successfully register the session: " + str(session_year) , 'email':email , 'name':name , 'rolename':rolename}
		return render(request, 'adm/academic_session.html', contex_dict)


################################################        get session ################################################################ 


def get_session(request):
	'''
	Get session in system.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		year_list = ['2014-15','2015-16', '2016-17', '2017-18', '2018-19']
		sem_list = [1,2,3]
		query_results = Academic_session.objects.all()
		count = query_results.count()
		contex_dict  = { 'year_list':year_list , 'sem_list':sem_list, 'count':count, 'query_results': query_results , 'email':email , 'name':name , 'rolename':rolename}
		return render(request, 'adm/academic_session.html', contex_dict)


################################################        get course teacher list ################################################################ 


def get_course_and_teacher(request):
	'''
	Get course and techer for allocation.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		a= request.POST
		dpname = request.POST['dpname']	
		techerdp = request.POST['teacher']
		query_results = All_deprtment.objects.filter(is_active = 1)
		query_results1 = All_course.objects.filter(dpname__id = dpname , is_active = 1 )
		query_results2 = Personinformation.objects.filter(departmentid__id = techerdp )
		context_dict  = {  'email':email , 'name':name , 'rolename':rolename , 'query_results':query_results, 'query_results1':query_results1,'query_results2':query_results2 }
		return render(request, 'adm/session_course_assignment.html' , context_dict)


################################################        assigned current semester courses ################################################################ 


def allocate_session_course(request):
	'''
	Allocate course to teacher
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		a= request.POST
		courseid = request.POST['courseid']	
		teacherid = request.POST['teacher']
		error_msg = ""
		query_results = Courseallotment.objects.filter(personid__id = teacherid , courseid__id = courseid , sessionid__is_active = 1)
		count = query_results.count()
		if count > 0:
			error_msg = "*ERROR- Pair of  selceted course and teacher for this semester is already allocated."
		if(error_msg != ""):
			json_data = json.dumps({"returnval":error_msg})
			return HttpResponse(json_data)


		####################        save in data base
		p = Courseallotment.objects.create(personid = Personinformation.objects.get(id = teacherid), courseid = All_course.objects.get(id=courseid) , sessionid= Academic_session.objects.get(is_active = 1) )
		p.save()
		success = "You have successfully  allocate course to the teacher."
		json_data = json.dumps({"returnval":success })
		return HttpResponse(json_data)	


################################################      get allocate course ################################################################ 


def get_allcate_course(request):
	'''
	Get allocation for current session
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		dp_name = request.POST['dpname']
		query_results = All_deprtment.objects.filter(is_active = 1)
		count = query_results.count()
		if dp_name == 'all':
			query_results1 = Courseallotment.objects.filter(sessionid__is_active=1 ) ## access using foreign key
			contex_dict  = {'query_results':query_results, 'query_results1':query_results1,'count':count,  'email':email , 'name':name , 'rolename':rolename, 'dpt':"Course allocation of all departments "}
			return render(request, 'adm/view_allocate_course.html', contex_dict)
		else:
			query_results1 = Courseallotment.objects.filter(courseid__dpname__department_name=dp_name )
			contex_dict  = {'query_results':query_results, 'query_results1':query_results1,'count':count, 'email':email , 'name':name , 'rolename':rolename, 'dpt':"Course allocation of " + (dp_name) }
			return render(request, 'adm/view_allocate_course.html', contex_dict)
	else:
		return HttpResponse("Not allowed !!!!. ")


################################################        validate login ################################################################ 


def validatelogin(request):
	args={}
	if request.method == 'POST':
		a= request.POST
		user_auth=auth.authenticate(username=request.POST['email'], password=request.POST['password'])
		## Checks if the password entered by the user matches with the password in the userlogin table
		#if check_password(request.POST['password'],user_info.password):
		if user_auth is not None and user_auth.is_active:
			auth.login(request,user_auth)
			userdetail = User.objects.get(username=request.POST['email'])
			f_name =  userdetail.first_name		 	
			user_info=Userlogin.objects.get(user=userdetail)
			if user_info.usertypeid == 0:
				request.session['email_id'] =request.POST['email']
				request.session['name'] = f_name
				user_info.nooflogins +=1
				user_info.last_login=datetime.now()
				user_info.status=1
				user_info.save()
                                args['email']=request.session['email_id']
				args['name'] = f_name
				return render_to_response("adm/index.html",args)
			else:
				request.session['email_id'] =userdetail.email
				user_info.nooflogins +=1
				user_info.last_login=datetime.now()
				user_info.status=1
				user_info.save()
				return HttpResponse('/ADM/')
		else:
			## If password not valid, then returns -1
			return HttpResponse("IN valid password!!!!. .")
	else:
		return HttpResponse("Not allowed !!!!. .")


#########################       valiadate file extention      ###################################################################################


def validate_file_extension(value):
	if not value.name.endswith('.csv'):
		return True
        return False


################################################       upload teacher and moodle mapping ################################################################ 


def upload_teacher_mapping(request):	
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		f = request.FILES['sentFile'] # here you get the files needed
		query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		if(validate_file_extension(f)):
			context_dict = {'error': "*ERROR-: Uploaded file is not .CSV file." , 'query1':query1 }
			return render(request, 'adm/teacher_mapping.html', context_dict ) # change page redirection
		id_list1 = []
		id_list2 = []
		line_no = 0
		query_results = Teacher_mapping.objects.filter(is_active = 1)
		reader = csv.reader(f)
		for row in reader:
			line_no = line_no +1
			if row[0] == "" or row[1] == "" :
				context_dict = {'error': "*ERROR-: Uploaded file has empty string at line no. " + str(line_no) , 'query1':query1 }
				return render(request, 'adm/teacher_mapping.html', context_dict ) # change page redirection
			for item in query_results:
				if str(item.mdl_id) == str(row[0]) and str(item.mooc_id) == str(row[1]):
					context_dict = {'error': "*ERROR-: This pair of Moodle id and MOOC id is already exist. ERROR* at line no. " + str(line_no) , 'query1':query1 }
					return render(request, 'adm/teacher_mapping.html', context_dict ) # change page redirection
			id_list1.append(row[0])
			id_list2.append(row[1])
		aList = [Teacher_mapping(mdl_id=id_list1[i],mooc_id=id_list2[i] ) for i in range(0,len(id_list1))]
		Teacher_mapping.objects.bulk_create(aList)
		context_dict = {'success': "*Success-: Uploaded file successfully saves in a database" , 'query1':query1 }
		return render(request, 'adm/teacher_mapping.html', context_dict ) # change page redirection


################################################    upload mooc student and teacher moodle mapping ################################################################ 


def upload_student_mapping(request):
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		#context_dict = {}
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		f = request.FILES['sentFile'] # here you get the files needed
		query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		if(validate_file_extension(f)):
			context_dict = {'error': "*ERROR-: Uploaded file is not .CSV file." , 'query1':query1 }
			return render(request, 'adm/student_mapping.html', context_dict ) # change page redirection
		id_list1 = []
		id_list2 = []
		line_no = 0
		query_results = Student_mapping.objects.filter(is_active = 1)
		reader = csv.reader(f)
		for row in reader:
			line_no = line_no +1
			if row[0] == "" or row[1] == "" :
				context_dict = {'error': "*ERROR-: Uploaded file has empty string at line no. " + str(line_no) , 'query1':query1 }
				return render(request, 'adm/student_mapping.html', context_dict ) # change page redirection
			for item in query_results:
				if str(item.mdl_id) == str(row[0]) and str(item.mooc_id) == str(row[1]):
					context_dict = {'error': "*ERROR-: This pair of Moodle id and MOOC id is already exist. ERROR* at line no. " + str(line_no) , 'query1':query1 }
					return render(request, 'adm/student_mapping.html', context_dict ) # change page redirection
			id_list1.append(row[0])
			id_list2.append(row[1])
		aList = [Student_mapping(mdl_id=id_list1[i],mooc_id=id_list2[i] ) for i in range(0,len(id_list1))]
		Student_mapping.objects.bulk_create(aList)
		context_dict = {'success': "*Success-: Uploaded file successfully saves in a database" , 'query1':query1 }
		return render(request, 'adm/student_mapping.html', context_dict ) # change page redirection


################################################    moodle used or not ################################################################ 


def moodle_binary(request):
	'''
	Include or exclude Moodle from system.
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		a= request.POST
		value = int(a['moodle']) 
		count = Moodle.objects.count()
		if count == 1:
			Moodle.objects.all().update(is_active=value)
			contex_dict  = { 'success': " You have successfully perform the opration" , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/moodle_setup.html' , contex_dict) 
		else:
			p = Moodle.objects.create(is_active=value)
			p.save()
			contex_dict  = { 'success': " You have successfully perform the opration" , 'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'adm/moodle_setup.html' , contex_dict) 
	else:
		return HttpResponse("Not allowed !!!!. ")
