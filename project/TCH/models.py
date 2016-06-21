from django.db import models


from django.contrib.auth.models import User
from django.utils.timezone import *

from datetime import datetime,time
from datetime import date
from django.utils import timezone
from time import time
from datetime import datetime, timedelta

from ADM.models import *

# Create your models here.




class Personinformation(models.Model):
	GENDER_CHOICES = ( 
	('MALE', 'Male'),
	('FEMALE', 'Female'),
	('OTHER', 'OTHER'),
		)
	email=models.EmailField(max_length=100,null=False)
	titleid=models.IntegerField(null=True)
	firstname=models.CharField(max_length=45,null=True)
	lastname=models.CharField(max_length=45,null=True)
	designation=models.IntegerField(null=True)
	gender=models.CharField(max_length=10,choices=GENDER_CHOICES, null='TRUE')
	departmentid=models.ForeignKey(All_deprtment, unique=False)
	experience=models.CharField(max_length=45,null=True)
	qualification=models.CharField(max_length=45,null=True)
	telephone1=models.CharField(null=False, max_length=12, default=0)
	telephone2=models.CharField(default=0, max_length=12, null=True)
	createdondate=models.DateField(default=timezone.now,null=False)
	is_active=models.BooleanField(default=1)




class Courseallotment(models.Model):
	personid=models.ForeignKey(Personinformation, unique=False) 
	courseid=models.ForeignKey(All_course, unique=False)
	sessionid=models.ForeignKey(Academic_session , unique=False)
	is_active=models.BooleanField(default=1)


class Evaluation_table(models.Model):
	eval_name= models.CharField(max_length=30)
	eval_no= models.CharField(max_length=30)
	max_marks=models.FloatField()
	courseallotid=models.ForeignKey(Courseallotment , unique=False)
	is_active=models.BooleanField(default=1)


class Evaluation_marks(models.Model):
	roll_no= models.CharField(max_length=50)
	marks=models.FloatField()
	evalid=models.ForeignKey(Evaluation_table , unique=False)
	is_active=models.BooleanField(default=1)













