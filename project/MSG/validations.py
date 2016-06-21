import re
import csv
#from SIP.views import *
#from SIP.validations import *

###############  Function to check all column filled values ###########

def all_column_feild(max_len, *args):
			if max_len > len(args):
				return False
			else:
				return True


###############  Function end here                          ###########

###############  Function to check all column filled values ###########
def validate_empty_feild(value):
	if(value == ''):
		return 0;
	else:
		return 1 ;

###############  Function end here                          ###########


###############  Function to check unique column ###########

def validate_unique(args):
	len1 = len(args)
	#print"+++++++++++++++++++++++++++++++++++=" ,args[0] , len1
	p = set(args)
	if len1 > len(p):
		return True
	else:
		return False


###############  Function end here                          ###########
	
###############  Function to validate total and mandetory ###########

def validate_total_mandetory(tot , man):
	len1 = len(tot)	
	for i in range(0,len1):
		if tot[i] < man[i]:
			return True

	return False
###############  Function end here                          ###########



###############  Function to check total and mandetory range ###########

def validate_range(tot):
	len1 = len(tot)	
	#print tot , "in -+===================="
	for i in range(0,len1):
		if int(tot[i]) < 1:
			return True
		if int(tot[i]) > 99:	
			return True

	return False
###############  Function end here                          ###########

###############  Function to check sum of weight column ###########

def weight_sum(numList):
	theSum = 0
	for i in numList:
		theSum = theSum + int(i)
	
	if theSum == 100:
		return False
	else:
		return True





###############  Function end here                          ###########

###############  Function to check weight range ###########


def weight_range(tot):
	len1 = len(tot)	
	#print tot , "in -+===================="
	for i in range(0,len1):
		if int(tot[i]) < 1:
			return True
		if int(tot[i]) > 100:	
			return True

	return False




###############  Function end here                          ###########

###############  Function to consolidated column ###########

def consolidated(tot):
	len1 = len(tot)	
	#print tot , "in -+===================="
	for i in range(0,len1):
		if ((tot[i].lower() != 'y') and (tot[i].lower() != 'n' )):
			return True
		
	return False



###############  Function end here                          ###########


###############  Function to check valid abbrevation string ###########
def valid_abbrevation(args):
	for element in args:
		if element.isalpha():
			pass
		else:
			return True
		if element.isupper():
			pass
		else:	
			return True
	return False



###############  Function end here                          ###########

###############  Function to check Validate Total and Mandetory numerecity ###########

def validate_number(args):
	for element in args:
		if element.isnumeric():
			pass
		else:
			return True
		
	return False




###############  Function end here                          ###########

###############  Function to validate file extention ###########


def validate_file_extension(value):
	if not value.name.endswith('.csv'):
		return True
        return False





###############  Function end here                          ###########


###############  Function to get numerr of evaluation ###########


def find_sum(list1, list2):
	sum1 = sum(list1)
	len1 = len(list2)
	for i in range(0,len1):
		if list2[i] == 'y':
			sum1 = sum1 - list1[i] + 1
	return sum1
	

###############  Function end here                          ###########

###############  Function to check all column filled values ###########
def marks_validity(list1, list2):
	len1 = len(list2)
	for i in range(0,len1):	
		if not list2[i] == "NA":
			if (float(list1[i]) < float(list2[i])):
				return True
	return False


###############  Function end here                          ###########

###############  Function to check all column filled values ###########
def marks_authencity(list1):
	len1 = len(list1)
	for i in range(0,len1):	
		if not list1[i] == "NA":
			try:
    				float(list1[i])
    				#return True
  			except ValueError:
    				return True
			
	return False



###############  Function end here                          ###########


###############  Function to check all column filled values ###########

def validate_max_marks(list1):
	len1 = len(list1)
	for i in range(0,len1):
		if float(list1[i]) < 1:
			return True
	return False


###############  Function end here                          ###########

###############  Function to check all column filled values ###########
def max_marks_authencity(list1):
	len1 = len(list1)
	for i in range(0,len1):	
		try:
    			float(list1[i])
    			#return True
  		except ValueError:
    			return True
	return False

###############  Function end here                          ###########

###############  Function to check all column filled values ###########

def valid_roll_no(item):
	if item == "":
		return True
	return False

###############  Function end here                          ###########


###############  Function to check header of uploaded template ###########


def valid_header(list1):
	for item in list1:
		if item == "":
			return True
	return False



###############  Function end here                          ###########

###############  Function to check less then zero values ###########

def less_then_zero_marks(list1):
	len1 = len(list1)
	for i in range(0,len1):
		if list1[i] == "NA":
			pass
		else:
			if float(list1[i]) < 0 : 
				return True

	return False


###############  Function end here                          ###########
###############  Function to check all column filled values ###########

def num_authenticity(list1):
	if not unicode(list1).isnumeric(): 
		return True

	return False




###############  Function end here                          ###########

###############  Function to check empty value or string value of text box filled by teacher as pweight list ###########

def empty_and_num(list1):
	len1 = len(list1)
	for i in range(0,len1):
		if list1[i] == "":
			pass
		else:
			try:
    				float(list1[i])
    			#return True
  			except ValueError:
    				return True

	return False





###############  Function end here                          ###########


###############  Function to sum of bm_policy  ###########

def get_sum(list1):
	len1 = len(list1)
	sum1 = 0
	for i in range(0,len1):
		if list1[i] == "":
			pass
		else:
			sum1 = sum1 + int(list1[i])

	return sum1




###############  Function end here                          ###########

###############  Function to check less then zero value ###########


def less_then_zero(list1):
	len1 = len(list1)
	for i in range(0,len1):
		if list1[i] == "":
			pass
		else:
			if int(list1[i]) < 0 : 
				return True

	return False







###############  Function end here                          ###########

###############  Function to check all column filled values ###########




###############  Function end here                          ###########
