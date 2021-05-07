import xlwt
import xlrd
import os
import datetime
from xlutils.copy import copy
from util import isExist
from category import JobCategory
from type import T


def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday.strftime('%m%d')

def getYesterdayDate(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday.strftime('%m/%d/%Y')    
   
# https://www.cnblogs.com/guoyunlong666/p/11416503.html

def do(job):
	old_workbook = xlrd.open_workbook(job.template,formatting_info=True)
	# 任务单
	target_sheet = old_workbook.sheet_by_index(0)

	style = xlwt.XFStyle()
	style1 = xlwt.XFStyle()
	style2 = xlwt.XFStyle()
	style3 = xlwt.XFStyle()
	style4 = xlwt.XFStyle()
	style5 = xlwt.XFStyle()

	font = xlwt.Font()
	font1 = xlwt.Font()
	font2 = xlwt.Font()
	font3 = xlwt.Font()
	font4 = xlwt.Font()

	font.name = "SimSun"
	font.height = 200
	font.bold = False

	font1.name = "SimSun"
	font1.height = 480
	font1.bold = True

	font2.name = "SimSun"
	font2.height = 360
	font2.bold = True

	font3.name = "SimSun"
	font3.height = 240
	font3.bold = True

	font4.name = "SimSun"
	font4.height = 160
	font4.bold = True

	borders = xlwt.Borders()
	borders1 = xlwt.Borders()

	borders.top = xlwt.Borders.THIN
	borders.bottom = xlwt.Borders.THIN
	borders.left = xlwt.Borders.THIN
	borders.right = xlwt.Borders.THIN

	borders1.right = xlwt.Borders.THIN

	alignment = xlwt.Alignment()
	alignment1 = xlwt.Alignment()

	alignment1.horz = xlwt.Alignment.HORZ_LEFT
	alignment1.vert = xlwt.Alignment.VERT_CENTER

	alignment.horz = xlwt.Alignment.HORZ_CENTER
	alignment.vert = xlwt.Alignment.VERT_CENTER

	style.font = font
	style.borders = borders
	style.alignment = alignment

	style1.font = font1
	style1.borders = borders
	style1.alignment = alignment

	style2.font = font2
	style2.borders = borders
	style2.alignment = alignment

	style3.font = font
	style3.borders = borders
	style3.alignment = alignment1

	style4.borders = borders
	style5.borders = borders1

	new_excel = copy(old_workbook)
	new_sheet = new_excel.get_sheet(0)

	# https://blog.csdn.net/tryll/article/details/102503043
	# 去掉页眉和页脚
	new_sheet.show_headers = False
	new_sheet.header_str = b''
	new_sheet.footer_str = b''
	# 设置单元格宽度 https://blog.csdn.net/weixin_42122355/article/details/83536142
	# new_sheet.col(1).width -= 600
	case_num = "Job #: "+job.job
	bref_brand = job.bref_brand
	
	if job.t == T.PROOFING:
		if job.category==JobCategory.USA:
			bref_brand = "WMUS "+job.bref_brand
		else:
			bref_brand = "WMCA "+job.bref_brand
			pass
	
	country = job.country
	program = "Program: "+job.program
	supplier = "Supplier: "+job.supplier
	buyer = "Buyer: "+job.buyer
	department = job.department
	due = "Artwork due date: "+ job.due
	packout = "Packout date: "+ job.packout
	ship = "Shipdate: "+ job.ship
	store = "In-store date: "+job.store
	contact = "联系人: "+ job.contact
	docket = "Docket Number: " + job.docket			

	today_str = datetime.datetime.now().strftime('%m/%d/%Y')
	new_sheet.write(1, 1, case_num,style1)
	if datetime.datetime.now().hour>8:
		new_sheet.write(4, 0, str(today_str),style)
	else:
		new_sheet.write(4, 0, str(getYesterdayDate()),style)	
		pass
	

	if job.category== JobCategory.PRINT:
		new_sheet.write(2, 1, job.PO ,style2)
	else:	
		Brand_Country = bref_brand+"/"+country if country !='' else bref_brand
		new_sheet.write(2, 1, Brand_Country ,style2)

	if job.category == JobCategory.CAN:
		new_sheet.write(2, 7, docket,style3)
		
	new_sheet.write(3, 7, case_num,style3)
	new_sheet.write(4, 7, program,style3)
	new_sheet.write(5, 7, supplier,style3)

	Buyer = buyer +'(D'+department+') ' if department != '' else buyer
	new_sheet.write(6, 7, Buyer ,style3)

	new_sheet.write(7, 7, due,style3)
	new_sheet.write(8, 7, packout,style3)
	new_sheet.write(9, 7, ship,style3)
	new_sheet.write(10, 7, store,style3)
	new_sheet.write(12, 7, contact,style3)

	if job.t == T.PROOFING:
		new_sheet.write(4, 1, "新case，见做稿, 请检查",style)

	#fix bug: border-right is none
	new_sheet.write(0, 6, "", style4)
	# new_sheet.write(0, 11, "", style5)
	# new_sheet.write(1, 11, "", style5)
	# new_sheet.write(2, 11, "", style5)
	# new_sheet.write(14, 15, "", style5)
	# new_sheet.write(15, 15, "", style5)
	new_sheet.write(1, 6, "", style4)
	new_sheet.write(2, 6, "", style4)

	today_str = datetime.datetime.now().strftime('%m%d')
	if datetime.datetime.now().hour<8:
		today_str=getYesterday()
		pass
		
	if not isExist(job.job_dir):
		os.mkdir(job.job_dir)
	
	if job.category	== JobCategory.PRINT:
		os.mkdir(job.job_dir+'/1客户资料')
		os.mkdir(job.job_dir+'/2BMK修改资料')
		os.makedirs(job.job_dir+'/3报价单或订单/'+str(today_str))
		os.mkdir(job.job_dir+'/4最终稿')
	else:	
		os.makedirs(job.job_dir+'/1 intake sheet & order/'+str(today_str))
		os.makedirs(job.job_dir+'/2 raw client files/'+str(today_str))	

	new_excel.save(job.to)
	pass

