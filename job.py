from category import JobCategory
from util import firstLetterUpper
from type import T

import os

m = {
    "HW": "Halloween",
    "HV":"Harvest",
    "PEN":"Pen + Gear",
    "HOL":"Holiday Time",
    "VAL":"Valentine",
    "WTC":"Way To Celebrate",
    "WTCW":"Way To Celebrate Wedding",
    "PA" :"Patriotic",
    "SUM":"Summer",
    "STP":"St. Patrick's Day",
    "SPR":"Spring",
    "NY":"New Year",
    "MG":"Mardi Gras",
    "EA":"Easter",
    "FA":"Father's Day",
    "MO":"Mother's Day",
    "MSB":"May Sweet Baby",
    "OZ":"Ozark Trail",
    "GV":"Great Value",
    "BW":"BlackWeb",
    "ONN":"ONN",
    "AW":"Athletic Works",
    "CA":"Canadiana",
    "MOV":"Movelo",
    "GV":"Great Value",
    "SP":"Spark",
    "EQU":"Equate",
    "GD":"Graduation",
    "HAN":"Hanukkah"
}

def get_temp(str):
    return os.getenv("HOME") +"/templates/"+str+".xls"

class Job():
    def __init__(self):
        # 系列简称
        self.bref_brand = ''
        # 国家
        self.country = ''
        # 系列全程
        self.program = ''
        # 客人
        self.supplier = ''
        # buyer
        self.buyer = ''
        # 部门
        self.department = ''
        # due date
        self.due = ''
        # packout date
        self.packout = ''
        # ship date
        self.ship = ''
        # in-store date
        self.store =''
        # main contact
        self.contact = ''
        # PO
        self.PO = ''   
        # t
        self.t = ''
        # docket
        self.docket = ''
        pass

    def setDocket(self,docket):
        self.docket = docket
    
    def setPO(self,po):
        self.PO = po

    def setJob(self, job):
        self.job = job.upper()
        if self.category == JobCategory.PRINT:
            self.job_dir = os.getenv("HOME")+"/Desktop/"+self.job
        else:
            self.job_dir = os.getenv("HOME")+"/Desktop/"+self.job+" 做稿"
        self.to = self.job_dir+"/"+self.job+"_DetailList_W.xls"

    def setCountry(self,country):
        if len(country)==3:
            self.country = country.strip().upper()
        else:    
            self.country = country.strip().capitalize()

    def set_bref_brand(self,bref_brand):
        self.bref_brand = bref_brand.upper()
        if self.bref_brand in m:
            self.program = m.get(self.bref_brand)
        else:
            self.program = ""
            if self.category==JobCategory.PRINT:
                self.bref_brand = bref_brand.upper()
            else:    
                self.bref_brand = bref_brand
            

    def setSupplier(self,supplier):
        self.supplier = firstLetterUpper(supplier.strip())

    def setBuyer(self,buyer):
        self.buyer = firstLetterUpper(buyer.strip())
    
    def setDepartment(self,department):
        self.department = department.strip()

    def setDue(self,due):
        self.due = str(due).strip()

    def setPackout(self,packout):
        self.packout = str(packout).strip()

    def setShip(self,ship):
        self.ship = str(ship).strip()
    
    def setStore(self,store):
        self.store = str(store).strip()
    
    def setContact(self,contact):
        self.contact = contact.strip()

    def setCategory(self, category):
        self.category = category
        if self.category == JobCategory.USA:
            if self.t == T.PROOFING:
                self.template = get_temp('usa_proofing')
            else:
                self.template = get_temp('usa')

        elif self.category == JobCategory.CAN:
            if self.t == T.PROOFING:
                self.template = get_temp('can_proofing')
            else:
                self.template = get_temp('can')

        elif self.category == JobCategory.OTHER:
            self.template = get_temp('nonwmt')
        elif self.category == JobCategory.PRINT:
            self.template = get_temp('print')

    def setType(self,t):
        self.t = t
        
    def run(self):
        # make the new case
        pass

