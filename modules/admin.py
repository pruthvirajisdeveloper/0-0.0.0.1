from modules.person import Person
from modules.student import Student
from modules.bill import Bill
from modules.lists import *

class Admin(Person):
    def __init__(self, id, name, age, whoami, mo_no, address):
        super().__init__(id, name, age, whoami, mo_no, address)
        self.students=[]
        self.seats=[]

    def set_student_list(self, list_is):
        self.students=list_is

    def new_student(self, id, name, age, whoami, mo_no, address):
        self.students.append(Student(id, name, age, whoami, mo_no, address))

    def list_all_students(self):
        content=[]
        for student in self.students:
            content.append(student.id_card())
        return sorted(content, key=lambda x: x[0])
            


    def get_id_card(self, id):
        for student in self.students:
            if id==student.id_card()[0]:
                return student.id_card()
        return None

    def book_seat(self, book_id):
        self.book_seat(book_id=book_id)

    def renew_seat(self, number, new_date, payment, duration, payment_id, date):
        for seat in self.seats:
            if number == seat.number:
                seat.renew(bill_id=payment_id, new_date=new_date, duration=duration)
                Bill(id=payment_id, total=payment[0], paid=payment[1], date=date).save()

    def save(self):
        self.list_all_students()


