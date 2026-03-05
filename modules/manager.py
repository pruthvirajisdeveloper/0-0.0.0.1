from modules.admin import Admin
from modules.lists import *
class Manager:
    def __init__(self):
        self.admin=Admin(id='A00001', name='shamal', age=40, whoami=ADMIN, mo_no=9876543210, address=None)

    def load_data(self):
        pass

    def save_data(self):
        pass

    def refresh_data(self):
        pass

    def update(self):
        pass

    def list_all_students(self):
        return self.admin.list_all_students()

    def get_id_card(self, id_no):
        return self.admin.get_id_card(id=id_no)


    def new_student(self, name, age, whoami, mo_no, address):
        self.admin.new_student(id=self.create_new_id_for_student(), name=name, age=age, whoami=whoami, mo_no=mo_no, address=address)

    def create_new_id_for_student(self):
        return 
    