from category import JobCategory
import os

def get_temp(str):
    return os.getcwd() +"/templates/"+str+".xls"

class Job():
    def __init__(self):
        pass

    def setJob(self, job):
        self.job = job
        self.to = os.getenv("HOME")+"/Desktop/a/a.xls"
    def setCategory(self, category):
        self.category = category
        if self.category == JobCategory.USA:
            self.template = get_temp('usa')
        elif self.category == JobCategory.CAN:
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



