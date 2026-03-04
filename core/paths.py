import os
name='mahankalilb'
class Paths:
    global name
    def __init__(self):
        self.sys_path= os.environ.get("LOCALAPPDATA")+f'\\{name}'

    def get_sys_path(self):
        return self.sys_path
    
    def get_admin_path(self):
        return self.sys_path + '\\admins\\'
    
    def get_bill_path(self):
        return self.sys_path + '\\bills\\'
    
    def get_seat_path(self):
        return self.sys_path + '\\seats\\'
    
    def get_student_path(self):
        return self.sys_path + '\\students\\'