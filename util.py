from pathlib import Path
import re

# get the cell value, such as buyer information: Teresa Parker (D18)
def parseCellValue(str):
	if ":" in str:
		return str.split(':')[1]
	else:
		return ""	

def isExist(pth):
	return Path(pth).exists()

def firstLetterUpper(str):
	str = str.lower().strip()
	
	if " " in str:
		str = str.split(' ')
		new_str = ""
		
		for x in str:
			item =""
			n = 0
			for y in x:
				n += 1
				if n==1:
	 				if ord(x[0]) >=97 and ord(x[0]) <= 122:
	 					y = chr(ord(x[0])-32)
				item += y
			new_str += item+" "
			if "hk" in new_str or 'Hk' in new_str:
				new_str = new_str.replace("hk","HK")
			if "usa" in new_str or "Usa" in new_str:
				new_str = new_str.replace("usa","USA")
			if "ig" in new_str or "Ig" in new_str:
				new_str = new_str.replace("ig","IG")	
			if "f.c." in new_str or "F.c." in new_str:
				new_str = new_str.replace("f.c.","F.C.")
			if "lp" in new_str or "Lp" in new_str:
				new_str = new_str.replace("lp","LP")
			if "ucp" in new_str or "Ucp" in new_str:
				new_str = new_str.replace("ucp","UCP")
			if "dsl" in new_str or "Dsl" in new_str:
				new_str = new_str.replace("dsl","DSL")
			if "Gi-go" in new_str:
				new_str = new_str.replace("Gi-go","Gi-Go")	
			if "(pvt)" in new_str:
				new_str = new_str.replace("(pvt)","(PVT)")	
		return new_str	
	else:
		return str.capitalize()


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
