import xlwt
import xlrd

from xlutils.copy import copy

# https://www.cnblogs.com/guoyunlong666/p/11416503.html

template = "/Users/scottxiong/desktop/U200378_AOP 做稿/U200378_AOP_DetailList_W.xls"
old_workbook = xlrd.open_workbook(template,formatting_info=True,on_demand=True)
# 任务单
target_sheet = old_workbook.sheet_by_index(0)

style = xlwt.XFStyle()
style1 = xlwt.XFStyle()
style2 = xlwt.XFStyle()
style3 = xlwt.XFStyle()
style4 = xlwt.XFStyle()

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
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN

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

new_excel = copy(old_workbook)
new_sheet = new_excel.get_sheet(0)

# https://blog.csdn.net/tryll/article/details/102503043
# 去掉页眉和页脚
new_sheet.show_headers = False
new_sheet.header_str = b''
new_sheet.footer_str = b''
# 设置单元格宽度 https://blog.csdn.net/weixin_42122355/article/details/83536142
# new_sheet.col(1).width -= 600

new_sheet.write(1, 1, "Job #:U200378_APP",style1)
new_sheet.write(4, 0, "05/14/2020",style)
new_sheet.write(2, 1, "HW/China",style2)
new_sheet.write(3, 7, "Job #:U200378_APP",style3)
new_sheet.write(4, 7, "Program: Halloween",style3)
new_sheet.write(5, 7, "Supplier: Gemmy Test",style3)
new_sheet.write(6, 7, "Buyer: Teresa Parker (D17)",style3)
new_sheet.write(7, 7, "Artwork due date: 09/01/2010",style3)
new_sheet.write(8, 7, "Packout date: 09/02/2010",style3)
new_sheet.write(9, 7, "Shipdate: 09/03/2010",style3)
new_sheet.write(10, 7, "In-store date: 09/04/2010",style3)
new_sheet.write(12, 7, "联系人: www.scott.com",style3)

#fix bug: border-right is none
new_sheet.write(0, 6, "", style4)
new_sheet.write(1, 6, "", style4)
new_sheet.write(2, 6, "", style4)

new_excel.save("/Users/scottxiong/desktop/U200378_AOP 做稿/U200378_AOP_DetailList_W_test.xls")
