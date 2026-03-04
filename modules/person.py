class Person:
    def __init__(self, id, name, age, whoami, mo_no, address):        
        self.id=id
        self.name=name
        self.age=age
        self.whoami=whoami
        self.mo_no=mo_no
        self.address=address


    def update(self, name=None, age=None, whoami=None, mo_no=None, address=None):
        if name is not None:
            self.name=name
        if age is not None:
            self.age=age
        if whoami is not None:
            self.whoami=whoami
        if mo_no is not None:
            self.mo_no=mo_no
        if address is not None:
            self.address=address
        self.save()


    def save(self):
        pass