import os
from job import Job
from category import JobCategory
from type import T
from newcase import do
from color import Colored
from util import validateJob
from autoRead import parse_excel
from util import isExist

cl = Colored()

valid = True

print(cl.green("请选择你要做的新case类型【1-4】:"))
print(cl.cyan(" 1. USA"))
print(cl.cyan(" 2. CAN"))
print(cl.cyan(" 3. 非WMT"))
print(cl.cyan(" 4. 印刷"))
a = input(cl.magenta("your selection is: "))

if a != '1' and a!='2' and a!='3' and a!='4':
    print("非法操作，程序退出")
    exit()

job = Job()

def handle_type(t):
    if t == 1:
       job.t = T.ADDAPTATION
    elif t==2 :
       job.t = T.PROOFING
    else:
        print(cl.red("输入有误"))

def handle_first_selection(answer):
    answer = int(answer)
    show_type_selection = True
    if answer == 1:
        job.setCategory(JobCategory.USA)
    elif answer == 2:
        job.setCategory(JobCategory.CAN)
    elif answer == 3:
        show_type_selection = False
        job.setCategory(JobCategory.OTHER)
    elif answer == 4:
        show_type_selection = False
        job.setCategory(JobCategory.PRINT)
    else:
        show_type_selection = False

    if show_type_selection:
        print(cl.green("检查还是印刷【1-2】："))
        print(cl.cyan(" 1. 做稿"))
        print(cl.cyan(" 2. 检查"))
        b = input(cl.magenta("your selection is: "))
        if b!='1' and b !='2':
            print("非法操作，程序退出")
            exit()
        handle_type(int(b))
    
    if answer == 4:
        bmk_job = input(cl.cyan("工单号: "))
        po = input(cl.cyan("订单号: "))
        job.setJob(bmk_job)
        job.setPO(po)
    else:  
        bmk_job = input(cl.cyan("工单号:"))

        while not validateJob(bmk_job,answer):
            bmk_job = input(cl.cyan("请输入正确的工单号:"))
        
        #if bmk_job exists return
        if isExist(os.getenv("HOME")+"/Desktop/"+bmk_job.upper()+" 做稿"):
            print(cl.red("桌面上检测到: "+bmk_job.upper()+" 做稿"))
            return

        job.setJob(bmk_job)
        bref_brand = input(cl.cyan("系列简称:"))
        job.set_bref_brand(bref_brand)
        
        standared = input(cl.cyan("是否是标准的excel[y/n]:"))
        if standared=='y' or standared=='Y':
            pf_path = input(cl.cyan("please drag your packaging form here:"))
            while "\\" in pf_path:
                pf_path = input(cl.cyan("Excel文件名不合法，请重命名 eg, a.xlsx 再重新尝试:"))
            pf_path = pf_path.strip()
            country,supplier,buyer,department,due,ship,store,packout,contact=parse_excel(pf_path)
            job.setCountry(country)
            job.setSupplier(supplier)
            job.setBuyer(buyer)
            job.setDepartment(department)
            job.setDue(due)
            job.setPackout(packout)
            job.setShip(ship)
            job.setStore(store)
            job.setContact(contact)
        else:
            country = input(cl.cyan("国家:"))
            supplier = input(cl.cyan("Supplier: "))
            buyer = input(cl.cyan("Buyer Name:"))
            department = input(cl.cyan("Department: "))
            due = input(cl.cyan("Artwork due date: "))
            packout = input(cl.cyan("Packout date: "))
            ship = input(cl.cyan("Shipdate: "))
            store = input(cl.cyan("In-store date: "))
            contact = input(cl.cyan("联系人: "))

            job.setCountry(country)
            job.setSupplier(supplier)
            job.setBuyer(buyer)
            job.setDepartment(department)
            job.setDue(due)
            job.setPackout(packout)
            job.setShip(ship)
            job.setStore(store)
            job.setContact(contact)
    
    do(job)
      
handle_first_selection(int(a))