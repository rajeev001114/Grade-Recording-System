from django.db import models

# Create your models here.
from datetime import datetime,time
from datetime import date
from django.utils import timezone
from time import time
from django.core.exceptions import ValidationError
from django.utils.timezone import *

from ADM.models import *
from TCH.models import *

def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)






class Grade_policy(models.Model):
	gp_id = models.CharField(max_length=50) 
	abbreviation = models.CharField(max_length=4)
	assignment = models.CharField(max_length=20)
	total = models.IntegerField()
	mandatory = models.IntegerField()
	weight = models.IntegerField()
	
	
	
	
class Content(models.Model):
	name = models.CharField(max_length=20)
	file = models.FileField(upload_to='.')



class CourseGrade(models.Model):
	gp_id = models.CharField(max_length=50)
        course_code = models.CharField(max_length=20)
	personid=models.ForeignKey(Personinformation, unique=False)		
	sessionid=models.ForeignKey(Academic_session , unique=False)
	


class Bm_max_marks(models.Model):
	course_name = models.CharField(max_length=50)
	personid=models.ForeignKey(Personinformation, unique=False)		
	sessionid=models.ForeignKey(Academic_session , unique=False)
	all_eval = models.CharField(max_length=20)
	max_marks = models.IntegerField()



class Bm_student_marks(models.Model):
	roll_no = models.CharField(max_length=30,default="0")
	course_name = models.CharField(max_length=50)
	personid=models.ForeignKey(Personinformation, unique=False)		
	sessionid=models.ForeignKey(Academic_session , unique=False)
	marks = models.TextField(null=True)


class Student_marks(models.Model):
	roll_no = models.CharField(max_length=30,default="0")	
	total = models.FloatField()


class Bm_weight(models.Model):
	course_name = models.CharField(max_length=50)
	personid=models.ForeignKey(Personinformation, unique=False)		
	sessionid=models.ForeignKey(Academic_session , unique=False)
	bmoocs_weight = models.IntegerField()


class Bm_grade_policy(models.Model):
	course_name = models.CharField(max_length=50)
	personid=models.ForeignKey(Personinformation, unique=False)		
	sessionid=models.ForeignKey(Academic_session , unique=False)
	min_count = models.IntegerField()
	weight = models.FloatField(default=0)
	examtype = models.CharField(max_length=50)
	drop_count = models.IntegerField()
	short_label = models.CharField(max_length=20)
	


class BM_policy_weight(models.Model):
	course_name = models.CharField(max_length=50)
	personid=models.ForeignKey(Personinformation, unique=False)		
	sessionid=models.ForeignKey(Academic_session , unique=False)
	pweight = models.TextField()




