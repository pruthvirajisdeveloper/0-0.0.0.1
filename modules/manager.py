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


    def new_student(self):
        self.admin.new_student(id=10, name='pruthviraj', age=19, whoami=STUDENT, mo_no=9876543210, address="k-mahankal")
        self.admin.new_student(id=11, name='sayali', age=21, whoami=STUDENT, mo_no=9876543210, address="k-mahankal")
        self.admin.new_student(id=12, name='pranav', age=18, whoami=STUDENT, mo_no=9876543210, address="k-mahankal")
        self.admin.new_student(id=23, name='atharv', age=14, whoami=STUDENT, mo_no=9876543210, address="k-mahankal")
        self.admin.new_student(id=14, name='kiran', age=12, whoami=STUDENT, mo_no=9876543210, address="k-mahankal")