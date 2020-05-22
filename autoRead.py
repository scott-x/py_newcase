# -*- coding: utf-8 -*-
# @Author: scottxiong
# @Date:   2020-05-20 23:03:42
# @Last Modified by:   scottxiong
# @Last Modified time: 2020-05-22 16:44:54
import xlrd
import datetime
from util import parseCellValue

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
		country = parseCellValue(sheet.cell_value(4,1).strip()).strip()
		supplier = parseCellValue(sheet.cell_value(3,0).strip()).strip()
		buyer = parseCellValue(sheet.cell_value(6,2).strip()).strip()
		department =''
		if type(sheet.cell_value(6,1))==float:
			department = int(sheet.cell_value(6,1))
			department = str(department)
		else:	
			department = parseCellValue(sheet.cell_value(6,1).strip()).strip()

		if 'd' in department or 'D' in department:
			department = department[1:]
		if len(department)==1:
				department = '0'+department
		due = parseTimeToString(2,5,sheet)
		ship = parseTimeToString(3,5,sheet)
		store = parseTimeToString(4,5,sheet)

		vendor = parseCellValue(sheet.cell_value(2,1).strip()).strip()
		contact =  parseCellValue(sheet.cell_value(2,3).strip()).strip()

		if vendor !="":
			contact = vendor + "  <" + parseCellValue(sheet.cell_value(2,3).strip()).strip()+ ">"
		print("并非所有客人按标准填写 packaging form 信息，请仔细核对做稿信息")
		return country,supplier,buyer,department,due,ship,store,"",contact
	else:
		check_cell = sheet.cell_value(44,0).strip()
		if not "In-Store" in check_cell:
			print("非标准Excle，请手动完善其余信息")
			return "","","","","","","","",""
		else:	
			country = sheet.cell_value(30,1).strip()
			supplier = sheet.cell_value(27,1).strip()
			buyer = sheet.cell_value(20,1).strip()
			department =''

			if type(sheet.cell_value(15,1))==float:
				department = int(sheet.cell_value(15,1))
				department = str(department)
			else:
				# fix bug if type(department) the value is '' 
				department = str(sheet.cell_value(15,1))	
			
			if 'd' in department or 'D' in department:
				department = department[1:]
			if len(department)==1:
					department = '0'+department

			contact = sheet.cell_value(37,1).strip()

			due = parseTimeToString(44,1,sheet)
			ship = parseTimeToString(45,1,sheet)
			packout = parseTimeToString(46,1,sheet)
			store = parseTimeToString(49,1,sheet)	
			print("并非所有客人按标准填写 packaging form 信息，请仔细核对做稿信息")
			return country,supplier,buyer,department,due,ship,store,packout,contact
			
# parse_excel("/Users/apple/Desktop/d.xlsx")		

def parseTimeToString(row,col,sheet):
	if type(sheet.cell_value(row,col))==float:	
		res = xlrd.xldate.xldate_as_datetime(sheet.cell(row,col).value, 0).strftime( '%m/%d/%Y' )
	else:
		res = sheet.cell_value(row,col)	
	return res	