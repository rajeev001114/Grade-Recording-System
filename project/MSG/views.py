from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Context, loader
# Create your views here.
import json
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#from MSG.models import *
from MSG.validations import *
from MSG.models import *
from ADM.models import *


####################################      function starts from here         ####################################      


def index(request):
	'''
	Return to index page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'msg/index.html', context_dict)


def local_view(request):
	'''
	Return to local evaluation page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = Moodle.objects.all()
	for item in query_results:
		if item.is_active == 1:
			context_dict = {'email':email , 'name':name , 'massage':"Your local marks stored in Moodle database.",'rolename':rolename}
			return render(request, 'msg/index.html', context_dict)
	context_dict = {'email':email , 'name':name , 'rolename':rolename}	
	return render(request, 'msg/local_evaluation.html', context_dict)


def moocs_view(request):
	'''
	Return to MOOC evaluation page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'email':email , 'name':name , 'rolename':rolename }	
	return render(request, 'msg/moocs_evaluation.html', context_dict)


def create_view(request):
	'''
	Return to create grade policy page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query_results = Courseallotment.objects.filter(personid__email = email)
	context_dict = {'email':email , 'name':name , 'rolename':rolename, 'query_results':query_results}	
	return render(request, 'msg/create.html', context_dict)


def view_view(request):
	'''
	Return to view grade policy page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query1 = CourseGrade.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	count = query1.count()
	context_dict  = {'query1':query1 , 'count':count , 'email':email , 'name':name , 'rolename':rolename}
	return render(request, 'msg/view.html', context_dict )


def generate_template_view(request):
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']	
	query1 = CourseGrade.objects.filter(personid__email = email)
	count = query1.count()
	context_dict  = {'query1':query1 , 'count':count ,'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'msg/generate_template.html', context_dict)


def upload_template_view(request):
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict  = {'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'msg/upload_template.html',context_dict)


def weight_view(request):
	'''
	Return to MOOC weight page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	q1 = Bm_weight.objects.filter(personid__email = email )
	count = q1.count()
	q2 = Courseallotment.objects.filter(personid__email = email )
	if count == 0:
		context_dict = {'error': " You have not enter weight of Blended MOOC. first enter the weight then go to distribution step.  " , 'q2':q2, 'email':email, 'name':name, 'rolename':rolename}
		return render(request, 'msg/bmoocs_weight.html', context_dict ) 
	context_dict  = { 'email':email, 'name':name , 'rolename':rolename , 'q2':q2}
	return render(request, 'msg/bmoocs_weight.html' , context_dict)


def success(request):
	'''
	Return to create grade policy success page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	gpid = request.GET["gpid"]
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'success': "You have successfully  added  grade policy.", 'gp_id':gpid ,'email':email , 'name':name , 'rolename':rolename  }
	return render(request, 'msg/success.html', context_dict )


def success_bmpolicy(request):
	'''
	Return to create grade MOOC policy page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	context_dict = {'success': "You have successfully submited weight of your blended MOOCs grading policy." ,'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'msg/success_bmpolicy.html', context_dict )


def upload_bmpolicy_view(request):
	'''
	Return to upload MOOC grade policy page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'msg/upload_bm_grade_policy.html', context_dict )


def upload_bmmarks_view(request):
	'''
	Return to upload MOOC marks page
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'msg/bm_marks.html', context_dict )


def insert_bmmarks_view(request):
	'''
	Return to insert marks view
	'''
	if 'email_id' not in request.session.keys():
		return render(request, 'tologin.html')
	email = request.session['email_id']
	name = request.session['name']
	rolename =  request.session['rolename']
	query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
	context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename }
	return render(request, 'msg/insert_bm_marks.html', context_dict )


#####################   Create Grade policy for a course ##########################


def create_grade_policy(request):
	'''
	Create grade policy
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		policy_row = request.POST
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		for key in policy_row.iterkeys():
			myDict = dict(policy_row.iterlists())	
		if 'csrfmiddlewaretoken' in myDict:	
			del myDict['csrfmiddlewaretoken']
		abbreviation_list = myDict['abbreviation']
		assignment_list = myDict['assignment']
		total_list = myDict['total']
		mandatory_list = myDict['mandatory']
		weight_list = myDict['weight']
		ccode = myDict['ccode'][0]
		q1 =   Academic_session.objects.filter(is_active = 1  )
		act_session = q1[0].year
		act_sem = q1[0].semester
		gpid = str(act_session) + '/' + str(act_sem) +'/' + str(ccode) 
		error_msg = ""


		######################         validation for exist grade policy
		gpcount = CourseGrade.objects.filter(personid__email = email , course_code= ccode , sessionid__year = act_session , sessionid__semester = act_sem ).count()
		if gpcount > 0:
			error_msg = "*ERROR-You have already created grade policy for this course in this semester"


		##################         validation for Empty feild
		for key in myDict.keys():
			for value in range(0, len(myDict[key])):
				if( validate_empty_feild(myDict[key][value]) ):
					pass
				else:
					context_dict = {'error': "*ERROR-Your have not filled "+ key + " value in row number: " + str((value+1)) }
					error_msg = context_dict['error'] #data here


		###### ################## valid abbrevation string
		if(error_msg == "" and valid_abbrevation(abbreviation_list)):
			context_dict = {'error': "*ERROR-Abbreviation column should contain ONLY uppercase alphabets of Maximum length 4."  }
			error_msg = context_dict['error']


		###### ################## validate unique of abbrevation and assignment
		if(error_msg == "" and validate_unique(abbreviation_list)):
			context_dict = {'error': "*ERROR-Your have duplicate values in Abbreviation column."  }
			error_msg = context_dict['error']
		if(error_msg == "" and validate_unique(assignment_list)):
			context_dict = {'error': "*ERROR-Your have duplicate values in Assignment column."  }
			error_msg = context_dict['error']


		############################### Validate Total and Mandetory numerecity
		if(error_msg == "" and validate_number(total_list)):
			context_dict = {'error': "*ERROR- No.of Assignments column value should be only positive INTEGER greater then zero." }
			error_msg = context_dict['error']
		if(error_msg == "" and validate_number(mandatory_list)):
			context_dict = {'error': "*ERROR- No. of Best Score column value  should be only positive INTEGER greater then zero." }
			error_msg = context_dict['error']
		if(error_msg == "" and validate_number(weight_list)):
			context_dict = {'error': "*ERROR- Weight column value  should be only positive INTEGER greater then zero." }
			error_msg = context_dict['error']


		############ ################### Validate Total and Mandetory range
		if(error_msg == "" and validate_range(total_list)):
			context_dict = {'error': "*ERROR- No.of Assignments field value should be greater then ZERO and less then 100." }
			error_msg = context_dict['error']
		if(error_msg == "" and validate_range(mandatory_list)):
			context_dict = {'error': "*ERROR- No. of Best Score field value should be greater then ZERO and less then equal to No.of Assignments." }
			error_msg = context_dict['error']


		############################### Validate Total and Mandetory
		if(error_msg == "" and validate_total_mandetory(total_list , mandatory_list)):
			context_dict = {'error': "*ERROR- No.of Assignments field value can not be less then No. of Best Score field value." }
			error_msg = context_dict['error']


		############################### Validate sum of weight range
		if(error_msg == "" and weight_range(weight_list)):
			context_dict = {'error': "*ERROR-Weight field value should be greater then ZERO and less then 101." }
			error_msg = context_dict['error']


		############################### Validate sum of weight
		if(error_msg == "" and weight_sum(weight_list)):
			context_dict = {'error': "*ERROR-: Weight column SUM should be exactly 100." }
			error_msg = context_dict['error']


		############################### Validate consolidated character		
		if(error_msg != ""):
			json_data = json.dumps({"returnval":error_msg})
			return HttpResponse(json_data)	


		###################    INsert grade policy in db
		aList = [Grade_policy(gp_id = gpid, abbreviation=abbreviation_list[i],assignment=assignment_list[i] , total=total_list[i],mandatory=mandatory_list[i], weight=weight_list[i]  ) for i in range(0,len(abbreviation_list))]
		Grade_policy.objects.bulk_create(aList)


		########################################   TO save in course garade
		p = CourseGrade( gp_id=gpid, course_code= ccode, sessionid = Academic_session.objects.get(is_active=1) , personid = Personinformation.objects.get(email= email))
		p.save()
		context_dict = {'success': "You have successfully  added one grade policy.", 'gp_id':gpid }
		json_data = json.dumps({"returnval":"success","gp_id":gpid})
		return HttpResponse(json_data)	
	else:
		dny = {'name': "ERROR " }
		json_data = json.dumps({"returnval":"Not Post"})
		return HttpResponse(json_data)


#####################      Function to Display data from data base in table ########


def show_grade_policy(request):
	'''
	View grade policy
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')	
		gp_id = request.POST['policy'] 
		rolename =  request.session['rolename']
		email = request.session['email_id']
		name = request.session['name']
		query_results = Grade_policy.objects.filter(gp_id = gp_id)
		query1 = CourseGrade.objects.filter(personid__email = email , sessionid__is_active = 1  )
		count = query1.count()
		if gp_id == 'select':
			context_dict  = {'query1':query1 , 'query_results':query_results, 'count':count, 'error':" You have not selected any grade policy."}
			return render(request, 'msg/view.html', {'context_dict':context_dict})
		context_dict  = {'query1':query1 , 'query_results':query_results, 'count':count ,'email':email, 'name':name}
		return render(request, 'msg/view.html', context_dict)
	else:
		return HttpResponse("Not allowed !!!!.      ")		


def generate_template(request):
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		gp_id = request.POST['policy']
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']


		##################      fetch data from database
		query1 = CourseGrade.objects.filter(personid__email = email)
		count = query1.count()
		query_results = Grade_policy.objects.filter(gp_id = gp_id)
		count = query1.count()


		########################             return if noquery selected    
		if gp_id == 'select':		
			contex_dict  = {'query1':query1 ,  'count':count, 'error':" You have not selected any grade policy."}
			return render(request, 'msg/generate_template.html', {'contex_dict':contex_dict})
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename= %s.csv' % (gp_id)


		####################             write header   ############################
		row_list = ['Roll Number']
		for item in query_results:
			if int(item.total) > 1:
				len1 = int(item.total)
				for i in range(0,len1):
					val = item.abbreviation + '-' + str((i+1))
					row_list.append( val )
			if int(item.total) == 1:
				row_list.append(item.abbreviation)			
		max_marks = row_list[1:]
		max_tag = []
		for i in range(0,len(max_marks)):
			max_tag.append('max')
		return response
	else:
		return HttpResponse("Not allowed !!!!.      ")		


#########################       valiadate file extention


def validate_file_extension(value):
	'''
	Validate file extention
	'''
	if not value.name.endswith('.csv'):
		return True
        return False


#########################       funtion ends here


def upload_template(request):
	'''
	Create grade policy
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		f = request.FILES['sentFile'] # here you get the files needed
		if(validate_file_extension(f)):
			context_dict = {'error': "*ERROR-: Uploaded file is not .CSV file." }
			return render(request, 'msg/upload_template.html', context_dict ) # change page redirection
		line_num = 0
		args =sessiondata(request)
		t_id = args['rcid']
		c_id = args['courseid']
		roll_list  = []
		marks_list = []
		reader = csv.reader(f)
		for row in reader:
			line_num = line_num +1
			li=str(row[0])
			if 'Grade Policy Id' in li:
				newstr = li.split( )


				gpid = newstr[4]		############## get gpid from uploaded file
				query_results = Grade_policy.objects.filter(gp_id = gpid)
				abbreviation_list = []
				assignment_list = []
				total_list = []
				mandatory_list = []
				weight_list = []
				consolidated_list = []
				for item in query_results:
					abbreviation_list.append(item.abbreviation) 
					assignment_list.append(item.assignment) 
					total_list.append(item.total) 
					mandatory_list.append(item.mandatory) 
					weight_list.append(item.weight) 
					consolidated_list.append(item.consolidated) 
				asmt_sum = find_sum(total_list, consolidated_list)	##  calculate no. of assignments
			elif '#' in li:
				pass
			elif 'Assignments' in li:
				newstr = li.split(':')
				Assignments_list= (newstr[1].lstrip().strip("[]")).split(',')
				if len(Assignments_list) != asmt_sum:
					context_dict = {'error': "*ERROR-: You have less or more number of assignments in template at line number: " + str(line_num) + " that given in  grade policy" }
					return render(request, 'msg/upload_template.html', context_dict ) 
			elif 'Max-Marks' in li:			
				newstr = li.split(':')
				max_marks_list = (newstr[1].lstrip().strip("[]")).split(',')
				max_marks_list = [(item.lstrip()).rstrip() for item in max_marks_list]
				if len(max_marks_list) != asmt_sum:
					context_dict = {'error': "*ERROR-: You have less or more  data in  Max-marks in template at line number: " + str(line_num) + " that given in  grade policy" }
					return render(request, 'msg/upload_template.html', context_dict ) 
				if(max_marks_authencity( max_marks_list)):
					context_dict = {'error': "*ERROR-: Either Max-marks is empty or invalid value at line number: " + str(line_num) }
					return render(request, 'msg/upload_template.html', context_dict ) 
				if(validate_max_marks( max_marks_list)):
					context_dict = {'error': "*ERROR-: Either max marks less then 1 at line number: " + str(line_num) }
					return render(request, 'msg/upload_template.html', context_dict ) 


				############   create row if not exist
				maxm_row, created  = Max_marks.objects.get_or_create(teacher_id= t_id  , course_id = c_id  )
				maxm_row.all_eval = Assignments_list
				maxm_row.max_marks= max_marks_list
				maxm_row.gp_id=gpid


				#maxm_row.save()               ######### this wiil save afer validations
			elif 'Roll Number' in li:
				if len(row) != (asmt_sum+1):
					context_dict = {'error': "*ERROR-: You have less or more  header field at line number: " + str(line_num)}
					return render(request, 'msg/upload_template.html', context_dict ) 
				if(valid_header( row)):
					context_dict = {'error': "*ERROR-: Header row or its element can not be empty at line number: " + str(line_num) }
					return render(request, 'msg/upload_template.html', context_dict ) 
				head_row = row[1:]
				maxm_row.all_eval = row[1:]
			else:
				row = [(item.lstrip()).rstrip() for item in row]
				roll_no = row[0]
				stu_marks_list = row[1:]
				if(valid_roll_no( roll_no)):
					context_dict = {'error': "*ERROR-: Students  Roll number can not be empty at line number: " + str(line_num) }
					return render(request, 'msg/upload_template.html', context_dict ) 
				if len(stu_marks_list) != (asmt_sum):
					context_dict = {'error': "*ERROR-: You have less or more  data  for the students having Roll number: " + str(roll_no) }
					return render(request, 'msg/upload_template.html', context_dict ) 
				if(marks_authencity( stu_marks_list)):
					context_dict = {'error': "*ERROR-: Students marks can not be other then Number and NA for  Roll number: " + str(roll_no) }
					return render(request, 'msg/upload_template.html', context_dict ) 
				if(less_then_zero_marks( stu_marks_list)):
					context_dict = {'error': "*ERROR-: Students marks can not be less then zero for  Roll number: " + str(roll_no) }
					return render(request, 'msg/upload_template.html', context_dict ) 
				if(marks_validity(max_marks_list, stu_marks_list)):
					context_dict = {'error': "*ERROR-: Students marks can not be more then max marks for  Roll number: " + str(roll_no) }
					return render(request, 'msg/upload_template.html', context_dict ) 
				roll_list.append(roll_no)
				marks_list.append(stu_marks_list)
		f.close()
		total_marks_list = []


		####################calculate total marks of students
		mm_list = max_marks_list[0:]
		mm_list = [float(item) for item in mm_list]
		for temp in marks_list:
			marks = temp[0:]
			for i in range(0, len(marks)):
				if marks[i] == "NA":
					marks[i] = 0
				else:
					marks[i] = float(marks[i])				
			pos = 0
			tot_marks = 0
			tm_list = []
			for ex in range(0, len(abbreviation_list)):
				to = total_list[ex]
				to = pos + to 
				l1 = marks[pos:to]
				m1 = mm_list[pos:to]
				wt = weight_list[ex]
				md = mandatory_list[ex]
				cld = consolidated_list[ex]
				pos = to
				cal_marks = 0.0
				sum_list1 = []
				for it in range(0, len(l1)):
					if cld == 'y':
						cal_marks = ( (l1[it] / m1[it]) * float(wt) )
		 				sum_list1.append(cal_marks)				
					else:
						cal_marks = float((l1[it] / m1[it]) * ( float(wt) / md) )
		 				sum_list1.append(cal_marks)
				sum_list1.sort(reverse=True)
				if cld == 'y':
					ex_marks = sum(sum_list1)
				else:
					sum_list_sorted = sum_list1[0:md]			
					ex_marks = sum(sum_list_sorted)
				tm_list.append(ex_marks)
			tot_marks = sum(tm_list)
			tot_marks = round(tot_marks , 2)
			total_marks_list.append(tot_marks)
		count_row = Student_marks.objects.filter(teacher_id=t_id , course_id=c_id).count()
		if count_row == 0:
			aList = [Student_marks(roll_no = roll_list[i], marks_obtain=marks_list[i],teacher_id=t_id , course_id=c_id , total =total_marks_list[i]) for i in range(0,len(roll_list))]
			Student_marks.objects.bulk_create(aList)


			maxm_row.save()   #######    save the max-marks row in database
		else:
			Student_marks.objects.filter(teacher_id=t_id , course_id=c_id).delete()
			aList = [Student_marks(roll_no = roll_list[i], marks_obtain=marks_list[i],teacher_id=t_id , course_id=c_id,total =total_marks_list[i] ) for i in range(0,len(roll_list))]
			Student_marks.objects.bulk_create(aList)


			maxm_row.save() #######    save the max-marks row in database
		context_dict = {'success': " You have successfully uploaded the marks of students, now you can  go to next step select the Blended MOOCs weight. "}
		return render(request, 'msg/upload_template.html' , context_dict)
	else:
		return HttpResponse("Not allowed !!!!.      ")		


#####################################################################                  ####################################


def insert_weight(request):
	'''
	Insert MOOC weight
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		weight = request.POST['weight']
		cname = request.POST['cname']
		q2 = Courseallotment.objects.filter(personid__email = email )
		if(num_authenticity(weight)):
			context_dict = {'error': "*ERROR-: Only numbers are allowed between 0 and 100 both inclusive " , 'q2':q2, 'email':email, 'name':name, 'rolename':rolename}
			return render(request, 'msg/bmoocs_weight.html', context_dict ) 
		weight = int(request.POST['weight'])
		if weight < 0 or weight > 100:
			context_dict = {'error': "*ERROR-: Number range should be between 0 and 100 both inclusive " , 'q2':q2, 'email':email, 'name':name, 'rolename':rolename}
			return render(request, 'msg/bmoocs_weight.html', context_dict ) 


		obj, created = Bm_weight.objects.update_or_create(personid = Personinformation.objects.get(email= email) , course_name = cname , sessionid = Academic_session.objects.get(is_active=1) , defaults={'bmoocs_weight': weight})
		obj.save()
		context_dict = {'success': "You have selected weight of Blended MOOC: " + str(weight) +"%" , 'q2':q2, 'email':email, 'name':name , 'rolename':rolename}
		return render(request, 'msg/bmoocs_weight.html', context_dict ) 
	else:
		return HttpResponse("Not allowed !!!!.      ")		


#####################################################################                  ####################################


def read_bmpolicy(request):
	'''
	Read MOOC grade policy
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		cname =  request.POST['cname']
		q1 = Bm_weight.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname )
		query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		count = q1.count()
		if count == 0:
			context_dict = {'query1':query1,'error': "*ERROR-: You have not entered weightage of Blended MOOCs " ,'email':email , 'name':name , 'rolename':rolename}
			return render(request, 'msg/bm_marks.html', context_dict   ) 
		weight = q1[0].bmoocs_weight


		query_results = Bm_grade_policy.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname )         ##############             check here  ################
		count_list = []
		context_dict  = { 'success': "you have selected weightage of Blended MOOCs: " + str(weight) +"%" , 'weight': str(weight) + '%' , 'rolename':rolename }
		for item in query_results:
			for i in range(0,int(item.min_count)):
				val  = item.examtype + '-' + str((i+1))
				count_list.append(val)
		context_dict['count_list'] = count_list	
		context_dict['email'] = email	
		context_dict['name'] = name
		request.session['cname'] = cname
		context_dict['query1'] =query1
		return render(request, 'msg/bm_marks.html', context_dict )
	else:
		return HttpResponse("Not allowed !!!!.      ")		


#####################################################################                  ####################################	


def submit_bmpolicy(request):
	'''
	Submit weight distribution
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		cname = request.session['cname'] 
		policy_row = request.POST
		for key in policy_row.iterkeys():
			myDict = dict(policy_row.iterlists())	
		pweight_list =  myDict['pweight']
		q1 = Bm_weight.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname )
		weight = q1[0].bmoocs_weight
		error_msg = ""
		if( empty_and_num(pweight_list)):
			context_dict = {'error': "*ERROR-: Enter valid number greater then zero !!!!! " }
			error_msg = context_dict['error']
		if(error_msg == ""):
			sum1 = get_sum(pweight_list)
		if((error_msg == "" and weight != sum1)):
			context_dict = {'error': "*ERROR-: Your distributed weight sum should be equal to " + str(weight) + ". It is now " + str(sum1) + "."}
			error_msg = context_dict['error']
		if(error_msg != ""):
			json_data = json.dumps({"returnval":error_msg})
			return HttpResponse(json_data)	
		new_pweight_list = []
		for item in pweight_list:
			if item == "":
				new_pweight_list.append(0)
			else:
				new_pweight_list.append(int(item))  


		obj, created = BM_policy_weight.objects.update_or_create( personid = Personinformation.objects.get(email= email) , course_name = cname , sessionid = Academic_session.objects.get(is_active=1) , defaults={'pweight': new_pweight_list})
		context_dict = {'success': "You have successfully submited weight of your blended MOOCs grading policy." }
		json_data = json.dumps({"returnval":"success"})
		return HttpResponse(json_data)	
	else:
		return HttpResponse("Not allowed !!!!.      ")		


#####################################################################                  ####################################


def insert_bmpolicy(request):
	'''
	Insert MOOC grade policy
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
			return render(request, 'msg/upload_bm_grade_policy.html', context_dict ) # change page redirection
		cname =  request.POST['cname']
		reader = csv.reader(f)
		for row in reader:
			obj, created = Bm_grade_policy.objects.update_or_create(course_name=cname, personid = Personinformation.objects.get(email= email),sessionid = Academic_session.objects.get(is_active=1), min_count = int(row[0]), weight = float(row[1]), examtype = row[2], drop_count = row[3],short_label =  row[4])
		query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename , 'success': "You have successfully submitted blended MOOCs grading policy for " + str(cname)  }
		return render(request, 'msg/upload_bm_grade_policy.html', context_dict )


#####################################################################                  ####################################


def insert_bmmarks(request):
	'''
	Insert MOOC marks
	'''
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
			return render(request, 'msg/insert_bm_marks.html', context_dict ) # change page redirection
		cname =  request.POST['cname']
		max_list = []
		all_evl_list = []
		marks_list = []
		line_no = 0
		reader = csv.reader(f)
		for row in reader:
			line_no = line_no +1
			if row[0] == 'max':
				max_list = row[1:]
			elif row[0] =='Roll Number':
				all_evl_list = row[1:]
			else:
				roll_no = row[0]
				stu_marks_list = row[1:]
				max_marks_list = max_list[0:]
				if(marks_authencity( stu_marks_list)):
					context_dict = {'error': "*ERROR-: Students marks can not be other then Number and NA for  Roll number: " + str(roll_no) ,'query1':query1,'email':email , 'name':name , 'rolename':rolename}
					return render(request, 'msg/insert_bm_marks.html', context_dict ) # change page redirection
				if(less_then_zero_marks( stu_marks_list)):
					context_dict = {'error': "*ERROR-: Students marks can not be less then zero for  Roll number: " + str(roll_no) ,'query1':query1,'email':email , 'name':name , 'rolename':rolename}
					return render(request, 'msg/insert_bm_marks.html', context_dict ) # change page redirection
				if(marks_validity(max_marks_list, stu_marks_list)):
					context_dict = {'error': "*ERROR-: Students marks can not be more then max marks for  Roll number: " + str(roll_no) , 'query1':query1,'email':email , 'name':name , 'rolename':rolename}
					return render(request, 'msg/insert_bm_marks.html', context_dict ) # change page redirection
		reader = csv.reader(f)
		for row in reader:
			if row[0] == 'max':
				max_list = row[1:]
			elif row[0] =='Roll Number':
				all_evl_list = row[1:]
				count = Bm_max_marks.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname ).count()
				if count == 0:
					aList = [Bm_max_marks(personid = Personinformation.objects.get(email= email) , course_name = cname , sessionid = Academic_session.objects.get(is_active=1) ,all_eval=all_evl_list[i], max_marks=max_list[i]  ) for i in range(0,len(max_list))]
					Bm_max_marks.objects.bulk_create(aList)
				else:
					Bm_max_marks.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname ).delete()
					aList = [Bm_max_marks(personid = Personinformation.objects.get(email= email) , course_name = cname , sessionid = Academic_session.objects.get(is_active=1) ,all_eval=all_evl_list[i], max_marks=max_list[i]  ) for i in range(0,len(max_list))]
					Bm_max_marks.objects.bulk_create(aList)
			else:
				marks_list = row[1:]
				obj, created = Bm_student_marks.objects.update_or_create(roll_no = row[0], personid = Personinformation.objects.get(email= email) , course_name = cname , sessionid = Academic_session.objects.get(is_active=1) , defaults={'marks': marks_list})
		context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename,'success': "You have successfully submitted blended MOOCs marks for " + str(cname) }
		return render(request, 'msg/insert_bm_marks.html', context_dict )


#####################################################################            generate final mark sheet      ####################################


def generate_final_marksheet(request):
	'''
	Return to final mark sheet page
	'''
	if 1 == 1:
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		######   validation for total weight and disrtibuted weight
		query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		q1 = Bm_weight.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		context_dict = {'query1':query1 ,'email':email , 'name':name , 'rolename':rolename , 'q1':q1 }
		return render(request, 'msg/generate_final_marksheet.html', context_dict )
	else:
		return HttpResponse("Not allowed !!!!.      ")		


#####################################################################         create composite marksheet         ####################################


def create_composite_marksheet(request):
	'''
	Create Composite MArk sheet
	'''
	if request.method == 'POST':
		if 'email_id' not in request.session.keys():
			return render(request, 'tologin.html')
		email = request.session['email_id']
		name = request.session['name']
		rolename =  request.session['rolename']
		cname =  request.POST['cname']
		query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		
		query2 = Bm_weight.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname )
		
		count = query2.count()
		total_list = []
		rollno_list = []
		if count > 0:
			weight = query2[0].bmoocs_weight
			if 1 > 0:
				query3 = Bm_student_marks.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname )
				for item in query3:
					a = item.marks.split("'")
					rollno_list.append(item.roll_no)
					mlist = []
					for item in a:
						
						if item.isdigit():
							mlist.append(int(item))
						if item == "NA":
							mlist.append(int(0))
					total_list.append(mlist)
			

				query4 = Bm_max_marks.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname )
				alleval  = []
				maxmarks = []	
				for item in query4:
					alleval.append(item.all_eval)
					maxmarks.append(int(item.max_marks))


				query5= BM_policy_weight.objects.filter(personid__email = email  , sessionid__is_active = 1 , course_name = cname )
				for item in query5:
					distrebtionlist = item.pweight.lstrip('[').rstrip(']').split(',')
					for item in a:	
						pass
				##########   marks computation star from here	
				marks_obtain_list = []
				
				# calculate MOOCs marks
				for item in total_list:
					temp = []
					for i in range(0,len(item)):
						s = float( float (item[i]) / float(maxmarks[i]) * float(distrebtionlist[i]) )
						round(s, 1)  
						temp.append(s)
					marks_obtain_list.append(round(sum(temp),2))



				########      read marks  from moodle   ##################################################################
			
				from django.db import connections

				query_results = Moodle.objects.all()
				for item in query_results:
					if item.is_active == 1 and weight > 0:
						
						query1 = Course_mapping.objects.filter(cid__course_name = request.POST['cname']  , is_active = 1 )
						for item in query1:
							cid = item.mdl_cid
						cursor = connections['moodle'].cursor()
					    	cursor.execute("SELECT * FROM mdl_course_completions where course = %s" % cid)
						row = cursor.fetchall()

						res_dict = []
						aList = [] # roll no.
						bList = []  ## total marks
						for item in row:
							
							aList.append(int(item[1]))
							bList.append(float(item[6]))
							res_dict.append(aList)

						w1 = float(  (100 - float(weight) ) / 100 )			
						bList = [round(item*w1 , 2) for item in bList]
						#############      start header line from here  ###################################################
						headrowlist = ['Roll Number']
						headrowlist.append('Institute Total Marks')
				
						headrowlist = headrowlist + alleval
						headrowlist.append('MOOCs Total')
						headrowlist.append('Composite Total')

						total_composite_marks_list = []
						for i in range(0,len(bList)):	
							total_composite_marks_list.append(round( (bList[i] + marks_obtain_list[i]),2) ) 
						combined_list = []
			
		

						for i in range(0,len(rollno_list)):
							temp1 = []
							temp1.append(rollno_list[i])
							temp1.append(bList[i])
							temp1 = temp1 + total_list[i]
					
							temp1.append(marks_obtain_list[i])
							temp1.append(total_composite_marks_list[i])
							combined_list.append(temp1)

						#######################          create csv file ##########################

						response = HttpResponse(content_type='text/csv')
						response['Content-Disposition'] = 'attachment; filename= %s.csv' % (cname)

						writer = csv.writer(response)
						query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )

						####################             write header   ############################
						writer.writerow(['Teacher Name: '+ query1[0].personid.firstname + ' ' + query1[0].personid.lastname ])
						writer.writerow(['Course Name: '+ cname ])
						writer.writerow(['MOOCs weightage: ' +  str(weight)])						
						distrebtionlist.insert(0,w1*100)
						writer.writerow(['Weight distribution'] + distrebtionlist)
						maxmarks.insert(0,w1*100)
						maxmarks.append(weight)
						maxmarks.append(100)
						
						writer.writerow(['Maximum marks for evaluations'] + maxmarks)
						writer.writerow( headrowlist )						
						for i in range(0,len(combined_list)): 
							writer.writerow( combined_list[i])
						return response

				
				########      Moddle is not connected  ##################################################################
				########      read local marks   ##################################################################
				
				query1 = All_course.objects.filter(course_name = cname  , is_active = 1 )
				for item in query1:
					ccode = item.course_code
				query1 = CourseGrade.objects.filter(course_code = ccode )
				for item in query1:
					gpid = item.gp_id
				
				lcl_asmt_list = []
				lcl_ttl_list = []
				lcl_mndt_list = []
				lcl_wgt_list = []				
				query1 = Grade_policy.objects.filter(gp_id = gpid )
				for item in query1:
					lcl_asmt_list.append(item.assignment)
					lcl_ttl_list.append(item.total)
					lcl_mndt_list.append(item.mandatory)
					lcl_wgt_list.append(item.weight)
	
				for j in range(0,len(lcl_asmt_list)):
					for i in range(0,int(lcl_ttl_list[j])):
						val  = lcl_asmt_list[j] + '-' + str((i+1))
				
				max_marks_list = []
				lcl_roll_list = []
				lcl_aggrrt_list = []
				lcl_eval_list = []
				lcl_id_list = []
				query1 = Evaluation_table.objects.filter(courseallotid__courseid__course_code = ccode )
				for item in query1:
					max_marks_list.append(item.max_marks)
					lcl_id_list.append(item.id)
				
				for item in lcl_id_list:
					query1 = Evaluation_marks.objects.filter(evalid = item )
					temp = []
					for item1 in query1:
						
						temp.append(item1.marks)
						if item1.roll_no in lcl_roll_list:
							pass
						else:
							lcl_roll_list.append(item1.roll_no)
									
					lcl_eval_list.append(temp)
				
				waightage_list = []
				new_max_marks_list = []
				for i in range(0,len(lcl_wgt_list) ):
					waightage_list.append(float(lcl_wgt_list[i] / lcl_mndt_list[i] ))
				
				count = 0 
				for i in range(0,len(lcl_ttl_list) ):
					for j in range(0, lcl_ttl_list[i]):
						new_max_marks_list.append(( max_marks_list[count]/max_marks_list[count] ) * waightage_list[i])
						count = count + 1

				for i in range(0,len(lcl_eval_list) ):
					for j in range(0,len(lcl_eval_list[i]) ):
						lcl_eval_list[i][j] = round(lcl_eval_list[i][j] * float(new_max_marks_list[i] / max_marks_list[i]), 2)
				
				for item in lcl_roll_list:
					lcl_aggrrt_list.append(float(0))					
			
				
				for i in range(0,len(lcl_roll_list) ):
					ct = 0
					std_sum = 0
					for p in range(0, len(lcl_ttl_list) ):
						lcl_total = lcl_ttl_list[p]
						lcl_mandt = lcl_mndt_list[p]
						temp = []
						for j in range(0,lcl_total):
							temp.append(lcl_eval_list[ct][i])
							ct = ct + 1
						temp.sort(reverse=True)
						temp1 = temp[:lcl_mandt]
						std_sum =std_sum + sum(temp1)
					lcl_aggrrt_list[i] = round(std_sum,2)
				
				w1 = float(  (100 - float(weight) ) / 100 )			
				lcl_aggrrt_list = [round(item*w1 , 2) for item in lcl_aggrrt_list]
				for i in range(0,len(lcl_roll_list) ):	
					temp = []			
					for j in range(0,len(lcl_eval_list) ):
						temp.append(lcl_eval_list[j][i])
				
				if weight > 0:
					#############      start header line from here  ###################################################
					headrowlist = ['Roll Number']
					headrowlist.append('Institute Total Marks')
				
					headrowlist = headrowlist + alleval
					headrowlist.append('MOOCs Total')
					headrowlist.append('Composite Total')

					total_composite_marks_list = []
					for i in range(0,len(lcl_aggrrt_list)):	
						total_composite_marks_list.append(round( (lcl_aggrrt_list[i] + marks_obtain_list[i]),2) ) 
					combined_list = []
			
		

					for i in range(0,len(rollno_list)):
						temp1 = []
						temp1.append(rollno_list[i])
						temp1.append(lcl_aggrrt_list[i])
						temp1 = temp1 + total_list[i]
					
						temp1.append(marks_obtain_list[i])
						temp1.append(total_composite_marks_list[i])
						combined_list.append(temp1)
				



					#######################          create csv file ##########################

					response = HttpResponse(content_type='text/csv')
					response['Content-Disposition'] = 'attachment; filename= %s.csv' % (cname)

					writer = csv.writer(response)
					query1 = Courseallotment.objects.filter(personid__email = email, sessionid__is_active = 1 )
					####################             write header   ############################

					writer.writerow(['Teacher Name : '+ query1[0].personid.firstname + ' ' + query1[0].personid.lastname ])			
					writer.writerow(['Course Name : '+ cname ])					
					writer.writerow(['Blended MOOCs weightage: ' +  str(weight)])					
					writer.writerow(['Local evaluations'] + lcl_asmt_list)
					writer.writerow(['Weight distribution for Local evaluations'] + lcl_wgt_list)
					writer.writerow(['MOOCs evaluations'] + alleval)
					writer.writerow(['Weight distribution for MOOCs evaluations'] + distrebtionlist)

					max_marks_list.append(w1*100)
					maxmarks.append(weight)
					maxmarks.append(100)
					writer.writerow(['Maximum marks for all evaluations'] + max_marks_list + maxmarks)					
					writer.writerow( headrowlist )
					
					for i in range(0,len(combined_list)): 
						writer.writerow( combined_list[i])
					return response
				
			else:
				pass
		
		### output only local mark sheet        ####################################################################
		headrowlist = ['Roll Number']
		headrowlist.append('Institute Total Marks')
		

		combined_list = []

		for i in range(0,len(rollno_list)):
			temp1 = []
			temp1.append(rollno_list[i])
			temp1.append(lcl_aggrrt_list[i])
			combined_list.append(temp1)
			
		#######################          create csv file ##########################

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename= %s.csv' % (cname)

		writer = csv.writer(response)
		query1 = Courseallotment.objects.filter(personid__email = email  , sessionid__is_active = 1 )
		####################             write header   ############################

		writer.writerow(['Teacher Name : '+ query1[0].personid.firstname + ' ' + query1[0].personid.lastname ])		
		writer.writerow(['Course Name : '+ cname ])
		writer.writerow(['Blended MOOCs weightage: ' +  str(weight)])
		writer.writerow(['Local evaluations'] + lcl_asmt_list)
		writer.writerow(['Weight distribution for Local evaluations'] + lcl_wgt_list)
		max_marks_list.append(100)
		writer.writerow(['Maximum marks for all evaluations'] + max_marks_list )
		writer.writerow( headrowlist )

		for i in range(0,len(combined_list)): 
			writer.writerow( combined_list[i])
		return response

	else:
		return HttpResponse("Not allowed !!!!.      ")		
