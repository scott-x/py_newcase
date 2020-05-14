from pathlib import Path

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