from datetime import timedelta, datetime
FREE = 0
ACTIVE = 1
BOOKED_ACTIVE = 2
BOOKED_INACTIVE = -1

class Student:
    def __init__(self, id,  name, address, age, work, uid):
        self.id=id
        self.name=name
        self.address=address
        self.age=age
        self.work=work
        self.uid=uid

    

class Member:
    def __init__(self, num, id):
        self.num=num
        self.id=id
        self.seats=[]

    def refresh(self):
        pass

    def update(self):
        pass


class Seat:
    def __init__(self, number, student:int, info:str):
        self.number=number
        self.student=student
        self.fees=Fees()
        self.info=info
        self.state=FREE #                 1:active, 2:booked+active, -1:booked+notactive, 0:not active
        self.booking=None
        self.markdates=[]
        self.end_date=None
        

    def assign(self, student:int, date:str, duration:int, fees:int, of:int):
        if self.state == -1:
            self.state=2
        elif self.state == 0:
            self.state=1
        self.student=student
        self.end_date=self.calculate_end_date(date=date, duration=duration)
        self.duration=duration
        self.add_fees(fees, of)
        return self.state


    def book(self, bookid:int):
        if self.state == 0:
            self.state=-1
        elif self.state == 1:
            self.state=2
        self.booking=True
        self.bookid=bookid
        return self.state

    def renew(self, new_date:str, duration:int, fees, of):
        
        self.markdates.append(new_date)
        self.end_date=self.calculate_end_date(date=new_date, duration=duration)
        self.add_fees(fees, of)
        return self.state


    def remove_member(self):
        self.member=None
        self.student=None
        self.fees=Fees()
        self.info=None
        if self.state == 1:
            self.state=0
        elif self.state == 2:
            self.state=-1 #                1:active, 2:booked+active, -1:booked+notactive, 0:not active
        self.booking=None
        self.markdates=[]
        self.end_date=None
        

    def calculate_end_date(self, date: str, duration: int):
        start_date = datetime.strptime(date, "%Y-%m-%d")
        end_date = start_date + timedelta(days=duration)
        return end_date

    def add_fees(self, fees, of):
        self.fees.add(fees=fees, of=of)

    def full_info(self, indent=0):
        spaces = " " * indent
        value = ""

        for key, val in self.__dict__.items():
            if hasattr(val, "__dict__"):
                value += f"{spaces}{key}:\n"
                for k, v in val.__dict__.items():
                    value += f"{spaces}    {k}: {v}\n"
            else:
                value += f"{spaces}{key}: {val}\n"

        return value


class Fees:
    def __init__(self):
        self.total=0
        self.paid=0

    def add(self, fees, of):
        self.total=self.total+int(of)
        self.paid=self.paid+int(fees)

    def get_due(self):
        return self.total-self.paid
    

class manager:
    def __init__(self):
        self.seats=[]
        self.students=[]

    def load_seats(self):
        pass
        
    def new_member(self, number, student, info):
        self.seats.append(Seat(number, student, info))

    def new_student(self, name, address, age, work, uid):
        self.students.append(Student(id=len(self.students)+1, name=name, address=address, age=age, work=work, uid=uid))

    def book_seat(self):
        pass

    def remove_student(self):
        pass

    def book_seat(self):
        pass

    def add_fees(self):
        pass

    def renew_seat(self):
        pass

    def list_all_seats(self):
        for st in self.seats:
            print (st.full_info())
    def list_all_students(self):
        pass

if __name__ == '__main__':
    

    i=manager()
    i.new_student(name="pruthviraj", address="deshing", age=19, work=None, uid='0000000001')
    i.new_student(name="samiksha", address="savalwadi", age=18, work=None, uid='0000000002')
    i.new_student(name="priyesh", address="budhgav", age=20, work=None, uid='0000000003')
    i.new_student(name="dinesh", address="deshing", age=23, work=None, uid='0000000004')
    i.new_student(name="gayatri", address="deshing", age=18, work=None, uid='0000000005')
    i.new_student(name="timir", address="savali", age=24, work=None, uid='0000000006')
    i.new_student(name="sakshi", address="ambap", age=25, work=None, uid='0000000007')
    i.new_student(name="kanhaiya", address="deshing", age=23, work=None, uid='0000000008')
    i.new_student(name="dipali", address="valava", age=34, work=None, uid='0000000009')
    i.new_student(name="komal", address="deshing", age=18, work=None, uid='0000000010')
    i.new_student(name="suhani", address="mumbai", age=30, work=None, uid='0000000011')
    i.new_student(name="samarth", address="puna", age=21, work=None, uid='0000000012')
    i.new_student(name="ramesh", address="kuchi", age=25, work=None, uid='0000000013')
    i.new_student(name="laxmi", address="deshing", age=18, work=None, uid='0000000014')
    i.new_student(name="vedant", address="dafalapur", age=15, work=None, uid='0000000015')
    i.new_student(name="karan", address="kerala", age=17, work=None, uid='0000000016')
    i.new_student(name="viraj", address="shindewadi", age=19, work=None, uid='0000000017')
    
    i.new_member(number=1, student=i.students[0], info='this is a imfo')
    i.new_member(number=2, student=i.students[1], info='this is a imfo')
    i.new_member(number=3, student=i.students[2], info='this is a imfo')
    i.new_member(number=4, student=i.students[3], info='this is a imfo')
    i.new_member(number=5, student=i.students[4], info='this is a imfo')
    i.new_member(number=6, student=i.students[5], info='this is a imfo')
    i.new_member(number=7, student=i.students[6], info='this is a imfo')
    i.new_member(number=8, student=i.students[7], info='this is a imfo')
    i.new_member(number=9, student=i.students[8], info='this is a imfo')
    i.new_member(number=10, student=i.students[9], info='this is a imfo')
    i.new_member(number=11, student=i.students[10], info='this is a imfo')
    i.new_member(number=12, student=i.students[11], info='this is a imfo')
    i.new_member(number=13, student=i.students[12], info='this is a imfo')
    i.new_member(number=14, student=i.students[13], info='this is a imfo')
    i.new_member(number=15, student=i.students[14], info='this is a imfo')
    i.new_member(number=16, student=i.students[15], info='this is a imfo')


    i.list_all_seats()
