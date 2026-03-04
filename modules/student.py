from modules.person import Person
class Student(Person):
    def __init__(self, id, name, age, whoami, mo_no, address):
        super().__init__(id, name, age, whoami, mo_no, address)


    def id_card(self):
        return [self.id, self.name, self.age, self.whoami, self.mo_no, self.address]