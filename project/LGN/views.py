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
from ADM.models import Userlogin
from TCH.models import *
from django.contrib.auth.models import User
from django.utils.timezone import *
from datetime import datetime,time
from datetime import date
from django.utils import timezone
from time import time
from django.views.decorators.cache import cache_control
from globalss import *
# Create your views here.
import string


def login(request):
	return render(request, 'tologin.html')


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
				request.session['rolename'] = "Admin"
				user_info.nooflogins +=1
				user_info.last_login=datetime.now()
				user_info.status=1
				user_info.save()
                                args['email']=request.session['email_id']
				args['name'] = f_name
				args['rolename'] = "Admin"
				return render_to_response("adm/index.html",args)
			else:
				request.session['email_id'] =request.POST['email']
				request.session['name'] = f_name
				request.session['rolename'] = 'Teacher'
				user_info.nooflogins +=1
				user_info.last_login=datetime.now()
				user_info.status=1
				user_info.save()
				args['email']=request.session['email_id']
				args['name'] = f_name
				args['rolename'] = 'Teacher'
				return render_to_response("tch/index.html",args)
		else:
			## If password not valid, then returns -1
			return HttpResponse("IN valid password!!!!.")
	else:
		return HttpResponse("Not allowed !!!!. ")


#################### Delete session and redirect to login page on logout click#######################################
@cache_control(no_cache=True, must_revalidate=True, no_store=True)


def logout(request):
	try:	
		del request.session['name']
		del request.session['email_id']
		del request.session['rolename']
		del request.session['cname']
		del request.session['mdl_course']
		request.session.flush()
		cache.clear()
		auth.logout(request)
		response = redirect('/')
		response['Cache-Control'] = 'no-cache, no-store, max-age=0, must-revalidate'
		response.delete_cookie()
		return response
	except:
        	return HttpResponseRedirect('/')


########change password on confirmation of old password  and after change password delete logged-in session , logout and redirect to login page for login with new passwords     ##########################


def pwd_field_empty(request,args,value):
    #ck_password =  r"^[A-Za-z0-9!@#$%^&*()_]{6,20}$"	
    module = 'Login'
    if value == 'Change_Pass':
        if not args['old_password']:
            args['message']="Old passowrd cannoit empty"#retrieve_error_message(module,'Pwd_empty','PASS_EMPTY')
## Checks if Field is Blank
    if not args['password1'] or not args['password2'] :	
        args['message']="*ERROR: Password cannot be empty"#retrieve_error_message(module,'Pwd_empty','PASS_EMPTY')
    elif  args['password1'] != args['password2']:
        args['message']= "*ERROR: Confirm  passwords do not match"#retrieve_error_message(module,value,'PWD_NO_MTCH')
        args['message']="*ERROR: Password contain whitespace" #retrieve_error_message(module,value,'INV_CHAR')
    elif len(args['password1'])<6 or len(args['password1'])>30:
         args['message']= "*ERROR: Pasword length should be in a range 6 to 30"
## Checks if Field is Blank
    return args


#######################################3            change password ######################################################


def change_pass(request):
    module = LOGIN_
    page = CHANGEPASS_
    args={}
    args.update(csrf(request))
    if request.method == 'POST':
       args={}
       try: 
		   args.update(csrf(request))
		   args['old_password']=oldpwd=request.POST.get('old_password','')
		   user=User.objects.get(username=request.session['email_id'])
		   args['password1']=password1= request.POST.get('new_password1','')
		   args['password2']=password2= request.POST.get('new_password2','')
		   args['message']=[]
		   args = pwd_field_empty(request,args,'Password')
		   per_id=Personinformation.objects.get(email=request.session['email_id']).id
		   if args['message']:
			  return render_to_response(changepassword_,args)
		   else: 
		         if user.check_password(oldpwd):
				        user.set_password(password1)
				        user.save()
				        try:
				            ec_id = 'success'
				        except Exception as e:
				               args['error_message'] = "changepass_email"
				               args['error_message'] = "\n Error " + str(e.message) + str(type(e))
				               return render(request,error_,args)
				        del request.session['name']
				        del request.session['email_id']
				        del request.session['rolename']
				        request.session.flush()
				        auth.logout(request)
				        return render_to_response(changepasswordsuccess_,args)            
		         args['message']= "Old password does not match"#retrieve_error_message(module,page,'OLD_NO_MTCH')
		         return render_to_response(changepassword_,args)
       except:
               args['error_message']= "not_logged_in"
               return render_to_response(login_,args)
    return  render_to_response(changepassword_,args)
