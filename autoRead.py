# -*- coding: utf-8 -*-
# @Author: scottxiong
# @Date:   2020-05-20 23:03:42
# @Last Modified by:   scottxiong
# @Last Modified time: 2020-05-22 01:02:45
import xlrd
import datetime

def getPFType(cell00_value):
	cell00_value = cell00_value.strip()
	if "GM Packaging Intake Form" in cell00_value :
		return 1
	else:	
		return 2
	pass

def parse_excel(filename):
	book = xlrd.open_workbook(filename)
	sheet = book.sheet_by_index(0)
	t = getPFType(sheet.cell_value(0,0))

	if t == 1:
		country = sheet.cell_value(4,1).strip()[8:].strip()
		supplier = sheet.cell_value(3,0).strip()[13:].strip()
		buyer = sheet.cell_value(6,2).strip()[22:].strip()
		department =''
		if type(sheet.cell_value(6,1))==float:
			department = int(sheet.cell_value(6,1))
			department = str(department)
		else:	
			department = sheet.cell_value(6,1).strip()[18:].strip()

		if 'd' in department or 'D' in department:
			department = department[1:]
		if len(department)==1:
				department = '0'+department
		due = parseTimeToString(2,5,sheet)
		ship = parseTimeToString(3,5,sheet)
		store = parseTimeToString(4,5,sheet)

		vendor = sheet.cell_value(2,1).strip()[33:].strip()
		contact =  sheet.cell_value(2,3).strip()[25:].strip()

		if vendor !="":
			contact = vendor + "  <" + sheet.cell_value(2,3).strip()[25:].strip()+ ">"

		return country,supplier,buyer,department,due,ship,store,"",contact
	else:
		"""
		# brand
		print(sheet.cell_value(14,1).strip())
		# department
		print(sheet.cell_value(15,1).strip())
		# buyer
		print(sheet.cell_value(20,1).strip())
		# company
		print(sheet.cell_value(27,1).strip())
		# country
		print(sheet.cell_value(30,1).strip())
		# vendor
		print(sheet.cell_value(37,1).strip())
		"""

		country = sheet.cell_value(30,1).strip()
		supplier = sheet.cell_value(27,1).strip()
		buyer = sheet.cell_value(20,1).strip()
		department =''

		if type(sheet.cell_value(15,1))==float:
			department = int(sheet.cell_value(15,1))
			department = str(department)

		if 'd' in department or 'D' in department:
			department = department[1:]
		if len(department)==1:
				department = '0'+department

		contact = sheet.cell_value(37,1).strip()

		due = parseTimeToString(44,1,sheet)
		ship = parseTimeToString(45,1,sheet)
		packout = parseTimeToString(46,1,sheet)
		store = parseTimeToString(49,1,sheet)	
		
		return country,supplier,buyer,department,due,ship,store,packout,contact
		
		pass
			
# parse_excel("/Users/apple/Desktop/d.xlsx")		

def parseTimeToString(row,col,sheet):
	res = ''
	if type(sheet.cell_value(row,col))==float:	
		# print(xlrd.xldate.xldate_as_datetime(sheet.cell(row,col).value, 0).strftime( '%m/%d/%Y' ) )
		res = xlrd.xldate.xldate_as_datetime(sheet.cell(row,col).value, 0).strftime( '%m/%d/%Y' )
	else:
		# print(sheet.cell_value(row,col))
		res = sheet.cell_value(row,col)	
	return res	