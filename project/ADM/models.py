from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone import *

from datetime import datetime,time
from datetime import date
from django.utils import timezone
from time import time

class All_deprtment(models.Model):
	department_name = models.CharField(max_length=50 , unique=True)	
	department_abb = models.CharField(max_length=10)
        is_active = models.BooleanField(default=1)



class All_course(models.Model):
	course_code = models.CharField(max_length=10)	
	course_name = models.CharField(max_length=50)
        dpname = models.ForeignKey(All_deprtment, blank=True, null=True, to_field='department_name')
	is_active = models.BooleanField(default=1)




class Userlogin(models.Model):
	user = models.OneToOneField(User, unique=True,related_name='login')	
	usertypeid=models.IntegerField(default=1)
	status=models.BooleanField(default=0)
	last_login=models.DateTimeField(default=timezone.now,null=False)
	nooflogins=models.IntegerField(null=True,default=0)


class Academic_session(models.Model):
	year = models.CharField(max_length=20)	
	semester = models.IntegerField()
        is_active = models.BooleanField(default=1)

	


class Teacher_mapping(models.Model):
	mdl_id = models.CharField(max_length=20)	
	mooc_id = models.CharField(max_length=20)
        is_active = models.BooleanField(default=1)


class Student_mapping(models.Model):
	mdl_id = models.CharField(max_length=20)	
	mooc_id = models.CharField(max_length=20)
        is_active = models.BooleanField(default=1)


class Moodle(models.Model):
	is_active = models.BooleanField()


class Course_mapping(models.Model):
	mdl_cid = models.CharField(max_length=20)	
	cid = models.ForeignKey(All_course, blank=True, null=True )
        is_active = models.BooleanField(default=1)





