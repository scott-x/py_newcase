import xlrd
import xlwt
xlsx = xlrd.open_workbook("/Users/scottxiong/Desktop/test.xlsx")
table = xlsx.sheet_by_index(0)
print(table.cell(0,0).value)

new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet("sheet01")
worksheet.write(0,0,"hello workd")
new_workbook.save("/Users/scottxiong/Desktop/test1.xls")

