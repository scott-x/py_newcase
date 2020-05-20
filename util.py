from pathlib import Path
import re

def isExist(pth):
	return Path(pth).exists()

def firstLetterUpper(str):
    return str
	# str = str.strip()
 #    str = str.lower()
 #    if len(str)==0:
 #        str = ''
 #    else:
 #        if " " in str:
 #        	s = ""
 #        	str_arr = str.split()
 #        	n = 1
 #        	for x in str_arr:
 #        		n +=1
 #        		s += x.capitalize()
 #        		if n!=len(str_arr):
 #        			s += " "
 #        	str = s			
 #        else:
 #        	str str.capitalize()
 #    return str        

def validateJob(job,answer):
	match_str = ""
	if answer==1:
		match_str = "[UuBb][2][0][01][0-9][a-zA-Z0-9][0-9]_[a-zA-Z]{3}$"
	elif answer==2:
		match_str = "[CcBb][2][0][01][0-9][a-zA-Z0-9][0-9]_[a-zA-Z]{3}$"
	elif answer==3:
		match_str = "[Bb][2][0][01][0-9][a-zA-Z0-9][0-9]_[a-zA-Z]{3}$"	
	else:
		match_str = "[Pp][2][0][01][0-9][a-zA-Z0-9][0-9]_[a-zA-Z]{3}$"	

	if re.match(match_str,job):
		return True
	else:
		return False
