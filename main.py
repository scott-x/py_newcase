import os
from job import Job
from category import JobCategory
from type import T
from newcase import do

DESKTOP = os.getenv('HOME')+"/Desktop"

print("请选择你要做的新case类型")
print(" 1. USA")
print(" 2. CAN")
print(" 3. 非WMT")
a = input("your selection is: ")
job = Job()

def handle_type(t):
    if t == 1:
        print("checking")
    elif t==2 :
        print("adaptaion")
    else:
        print("输入有误")

def handle_country(answer):
    valid = True
    if answer == 1:
        print("USA")
        job.setCategory(JobCategory.USA)
    elif answer == 2:
        print("CAN")
        job.setCategory(JobCategory.CAN)
    elif answer == 3:
        print("非WMT")
        valid = False
        job.setCategory(JobCategory.OTHER)
    elif answer == 3:
        print("印刷")
        valid = False
        job.setCategory(JobCategory.PRINT)
    else:
        valid = False
        print("输入有误")

    if valid:
        print(" 1. 检查")
        print(" 2. 做稿")
        b = input("your selection is: ")
        handle_type(int(b))

    bmk_job = input("请输入单号[eg: U200325_APP]:")
    job.setJob(bmk_job)
    do(job)

handle_country(int(a))