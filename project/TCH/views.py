from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.template import Context, loader
# Create your views here.
import json
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
#from ADM.validations import *
from TCH.models import *
from ADM.models import *
from ADM.models import *
from MSG.models import *
# Create your views here.


def index(request):
	'''
	Return to teacher dashboard
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'tch/index.html', context_dict)


def view_course(request):
	'''
	View current allocated courses
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = Courseallotment.objects.filter(personid__email=email , sessionid__is_active = 1 )
	query_1 = Academic_session.objects.filter(is_active = 1 )
	session = str(query_1[0].year) + '_SEM-' + str(query_1[0].semester)
	count = query_results.count() 
	context_dict = {'email':email , 'name':name , 'rolename':rolename , 'query_results':query_results , 'count':count, 'session':session }
	return render(request, 'tch/view_course.html', context_dict)


def all_view_course(request):
	'''
	View all allocated courses
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = Courseallotment.objects.filter(personid__email=email  )
	count = query_results.count() 
	context_dict = {'email':email , 'name':name , 'rolename':rolename , 'rolename':rolename , 'query_results':query_results , 'count':count}
	return render(request, 'tch/all_view_course.html', context_dict)


def upload_local_marks_view(request):
	'''
	Return to upload local marks page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename  }
	return render(request, 'tch/upload_local_marks.html', context_dict )


def update_local_marks_view(request):
	'''
	Return to update local marks page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename  }
	return render(request, 'tch/update_local_marks_view.html', context_dict )


def teacher_registration(request):
	'''
	Return to teacher registration page
	'''
	query_results = All_deprtment.objects.filter(is_active = 1)
	count = query_results.count()
	context_dict = {'query_results':query_results }
	return render(request, 'tch/teacher_registration.html', context_dict)


def admin_registration(request):
	'''
	Return to admin registration page
	'''
	query_results = Userlogin.objects.filter(usertypeid = 0)
	count = query_results.count()
	if count > 0:
		context_dict = {'error_message':"*ERROR-: Admin is already created." }
		return render(request, 'tologin.html', context_dict)
	context_dict = {'query_results':query_results }
	return render(request, 'tch/admin_registration.html', context_dict)


#############            get evaluations for subject ############################################################################################


def get_exam_type(request):
	'''
	Get all evaluations
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	c_code =  request.POST['ccode']
	q2 = CourseGrade.objects.filter(course_code = c_code , sessionid__is_active = 1)
	for item in  q2:
		gpid = item.gp_id
	######   validation for total weight and disrtibuted weight
	query2 = Grade_policy.objects.filter(gp_id = gpid )
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	request.session['upload_subject_marks'] = c_code
	count_list = []
	for item in query2:
		for i in range(0,int(item.total)):
			val  = item.assignment + '-' + str((i+1))
			count_list.append(val)
	context_dict = {'query1':query1 , 'query3':count_list ,'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'tch/upload_local_marks.html', context_dict )


#############            get evaluations for subject ############################################################################################


def update_get_exam_type(request):
	'''
	Update local marks
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	c_code =  request.POST['ccode']
	q2 = CourseGrade.objects.filter(course_code = c_code , sessionid__is_active = 1)
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	if q2.count() == 0:
		context_dict = {'error': "*ERROR-: No data found !!! ",'query1':query1 ,'email':email , 'name':name , 'rolename':rolename }
		return render(request, 'tch/update_local_marks_view.html', context_dict )
	for item in  q2:
		gpid = item.gp_id
	######   validation for total weight and disrtibuted weight
	query2 = Grade_policy.objects.filter(gp_id = gpid )
	request.session['update_subject_marks'] = c_code
	count_list = []
	for item in query2:
		for i in range(0,int(item.total)):
			val  = item.assignment + '-' + str((i+1))
			count_list.append(val)
	context_dict = {'query1':query1 , 'query3':count_list ,'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'tch/update_local_marks_view.html', context_dict )


#############            get student marks for evaluation ############################################################################################


def get_student_marks(request):
	'''
	Get student marks
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	examname = request.POST['examname']
	request.session['examname'] = examname
	eval1= examname.split('-')
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )		
	query_results1 = Evaluation_marks.objects.filter(evalid__eval_name = eval1[0] , evalid__eval_no = eval1[1] )
	context_dict = {'query1':query1  , 'query_results1':query_results1, 'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'tch/update_local_marks_view.html', context_dict )


#########################       valiadate file extention  ######################################################################################


def validate_file_extension(value):
	if not value.name.endswith('.csv'):
		return True
        return False


#############            insert marks for evaluation ############################################################################################


def insert_evaluation_marks(request):
	'''
	Save local evaluation in database
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		f = request.FILES['sentFile'] # here you get the files needed
		if(validate_file_extension(f)):
			query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
			context_dict = {'error': "*ERROR-: Uploaded file is not .CSV file." , 'query1':query1 }
			return render(request, 'tch/upload_local_marks.html', context_dict ) # change page redirection
		c_code =  request.session['upload_subject_marks']
		weight =  request.POST['weight']
		examname = request.POST['examname']
		eval1= examname.split('-')
		line_num = 1
		roll_list = []
		marks_list = []
		reader = csv.reader(f)
		for row in reader:
			if float(row[1]) > float(weight) or float(row[1]) < 0:
				query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
				context_dict = {'error': "*ERROR-: Uploaded file contain maximum marks less the obtain marks or obtain marks less then zero at line no. " + str(line_num) + ". Select subject again" , 'query1':query1 }
				return render(request, 'tch/upload_local_marks.html', context_dict ) # change page redirection
			roll_list.append(row[0])
			marks_list.append(float(row[1]))
			line_num = line_num +1
		count = Evaluation_table.objects.filter(eval_name = eval1[0], eval_no= int(eval1[1]), courseallotid__personid__email = email, courseallotid__sessionid__is_active=1 ,courseallotid__courseid__course_code = c_code).count()
		if count == 0 :
			try:
				p = Evaluation_table( eval_name = eval1[0], eval_no= eval1[1] , max_marks = weight, courseallotid = Courseallotment.objects.get(personid__email = email, sessionid__is_active=1 , courseid__course_code = c_code ))
				p.save()
			except:
				aList = [Evaluation_marks(roll_no = roll_list[i], marks=marks_list[i], evalid= Evaluation_table.objects.get(eval_name = eval1[0], eval_no= eval1[1], courseallotid__personid__email = email  , courseallotid__sessionid__is_active  =1 ,courseallotid__courseid__course_code = c_code) ) for i in range(0,len(roll_list))]
				Evaluation_marks.objects.bulk_create(aList)
			del request.session['upload_subject_marks']   #####  delete session
			query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
			context_dict = {'success': "You have successfully uploaded marks ", 'query1':query1 }
			return render(request, 'tch/upload_local_marks.html', context_dict ) # change page redirection
		else:
			query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
			context_dict = {'error': "*ERROR-: Marks for this evaluation is already Uploaded !!! " , 'query1':query1 }
			return render(request, 'tch/upload_local_marks.html', context_dict ) # change page redirection
	else:
		return HttpResponse("Not allowed !!!!.      ")		


#############            update student marks for evaluation ############################################################################################


def update_student_marks(request):
	'''
	Update student marks
	'''	
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	location = request.GET.get('location')
	u_marks =  float(request.POST['updatemarks'])
	rollno = request.POST['roll_no']
	eval1= request.session['examname'].split('-')
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	query_results1 = Evaluation_table.objects.filter(eval_name = eval1[0] , eval_no = eval1[1] )
	for item in query_results1:
		mx_marks = item.max_marks
	if u_marks > mx_marks or u_marks < 0 :
		del request.session['update_subject_marks']
		context_dict = {'error': "*ERROR-: Update marks is greater then max marks or less then zero for evaluation ", 'query1':query1, 'email':email , 'name':name , 'rolename':rolename }
		return render(request, 'tch/update_local_marks_view.html', context_dict ) 
	Evaluation_marks.objects.filter(roll_no = rollno , evalid__eval_name = eval1[0], evalid__eval_no = eval1[1] ).update(marks = u_marks)
	del request.session['update_subject_marks']
	context_dict = {'success': "*SUCCESS-: You have successfully update the marks.", 'query1':query1, 'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'tch/update_local_marks_view.html', context_dict ) 


#############            accessing moodle data ############################################################################################
from django.db import connections


def mdl_marks(request):
	'''
	Get Moodle marks of students
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	for e in Personinformation.objects.filter(email = email):
    		moocid = int (e.id)
	for e in Teacher_mapping.objects.filter(mooc_id = moocid):
    		mdlid = int (e.mdl_id)
	mdl_course_enrol = [] 
	mdl_course_dict = {} 
	cursor = connections['moodle'].cursor()
    	cursor.execute("SELECT * FROM mdl_user_enrolments where userid = %s" % mdlid)
	row1 = cursor.fetchall()	
	for e in row1:
		mdl_course_enrol.append(int(e[2]))
	for cid in mdl_course_enrol:
		cursor = connections['moodle'].cursor()
    		cursor.execute("SELECT * FROM mdl_enrol where id = %s" % cid)
		row1 = cursor.fetchone()
		cursor = connections['moodle'].cursor()
    		cursor.execute("SELECT * FROM mdl_course where id = %s" % row1[3])
		row2 = cursor.fetchone()
		mdl_course_dict[int(row2[0])]  = str(row2[3])
	request.session['mdl_course'] = mdl_course_dict
	context_dict = {'query1':mdl_course_dict,'email':email , 'name':name , 'rolename':rolename  }
	return render(request, 'tch/moodle_marks.html', context_dict)


#############            accessing moodle marks ############################################################################################


def get_mdl_course_marks(request):
	'''
	Get Moodle course
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	mdl_course_dict =  request.session['mdl_course']
	cid = int(request.POST['course_id'])
	cursor = connections['moodle'].cursor()
    	cursor.execute("SELECT * FROM mdl_course_completions where course = %s" % cid)
	row = cursor.fetchall()
	res_dict = []
	for item in row:
		aList = []
		aList.append(int(item[1]))
		aList.append(float(item[6]))
		res_dict.append(aList)
	context_dict = {'query1':mdl_course_dict,'email':email , 'name':name , 'rolename':rolename , 'query_results':res_dict , 'uid': "User Id" , 'Marks':"Marks" }
	return render(request, 'tch/moodle_marks.html', context_dict)


#############        insert    teacher registrsation ############################################################################################


def insert_teacher_info(request):
	'''
	Save teacher information
	'''
	dp_name = request.POST['dpname']
	emailid = request.POST['email']
	f_name = request.POST['fname']
	l_name = request.POST['lname']
	ph = request.POST['phnum']
	gender1 = request.POST['gender']
	qualification1 = request.POST['qualification']
	exep = int(request.POST['exep'])
	pwd = request.POST['password']
	query_results = All_deprtment.objects.filter(is_active = 1)
	query1 = Personinformation.objects.filter(email = emailid)
	count = query1.count()
	if count > 0:
		context_dict = { 'query_results':query_results, 'error': "This Email Id is already in use." }
		return render(request, 'tch/teacher_registration.html', context_dict)
	query1 = Personinformation.objects.filter(firstname =f_name )
	count = query1.count()
	if count > 0:
		context_dict = { 'query_results':query_results, 'error': "This first name is already in use. Enter a different first name" }
		return render(request, 'tch/teacher_registration.html', context_dict)
	p = Personinformation.objects.create(email=emailid, firstname=f_name, lastname =l_name, gender = gender1, departmentid = All_deprtment.objects.get(department_name = dp_name), experience = exep, qualification = qualification1, telephone1 = ph, designation = 5 , titleid = 0 )
	p.save()
	user = User.objects.create_user( emailid, emailid, pwd)
	user.last_name = l_name
	user.first_name = f_name	
	user.is_active = True
	user.save()
	u_login = Userlogin.objects.create(usertypeid = 1, status = 1, user = User.objects.get( email = emailid) )
	u_login.save()
	context_dict = { 'query_results':query_results, 'success': "You have successfully register. Go to Login page" }
	return render(request, 'tch/teacher_registration.html', context_dict)


#############        insert    admin registrsation ############################################################################################


def insert_admin_info(request):
	'''
	Save admin information
	'''
	emailid = request.POST['email']
	f_name = request.POST['fname']
	l_name = request.POST['lname']
	ph = request.POST['phnum']
	gender1 = request.POST['gender']
	qualification1 = request.POST['qualification']
	exep = int(request.POST['exep'])
	pwd = request.POST['password']
	query_results = All_deprtment.objects.filter(is_active = 1)
	query1 = Personinformation.objects.filter(email = emailid)
	count = query1.count()
	if count > 0:
		context_dict = { 'query_results':query_results, 'error': "This Email Id is already in use." }
		return render(request, 'tch/teacher_registration.html', context_dict)
	query1 = Personinformation.objects.filter(firstname =f_name )
	count = query1.count()
	if count > 0:
		context_dict = { 'query_results':query_results, 'error': "This first name is already in use. Enter a different first name" }
		return render(request, 'tch/teacher_registration.html', context_dict)
	p = Personinformation.objects.create(email=emailid, firstname=f_name, lastname =l_name, gender = gender1, experience = exep, departmentid = All_deprtment.objects.get(department_name = 'Computer Science'), qualification = qualification1, telephone1 = ph, designation = 0 , titleid = 0 )
	p.save()
	user = User.objects.create_user( emailid, emailid, pwd)
	user.last_name = l_name
	user.first_name = f_name	
	user.is_active = True
	user.save()
	u_login = Userlogin.objects.create(usertypeid = 0, status = 1, user = User.objects.get( email = emailid) )
	u_login.save()
	context_dict = { 'query_results':query_results, 'success': "You have successfully register. Go to Login page" }
	return render(request, 'tch/teacher_registration.html', context_dict)
