from modules.lists import *
from datetime import datetime, timedelta
class Seat:
    def  __init__(self, number=0, student_id=0, status=NON_ACTIVE, book_id=0, bill_id=0, end_date=''):
        self.bills=[]
        self.bills.append(bill_id)
        self.book_id=book_id
        self.status=status
        self.number=number
        self.student_id=student_id
        self.end_date=end_date

    def renew(self, bill_id, new_date, duration): #new_date: "%YYYY-%MM-%DD", duration : %DD*
        self.bills.append[bill_id]
        date_obj = datetime.strptime(new_date, "%Y-%m-%d")
        self.end_date=date_obj + timedelta(days=duration)

    def book(self, book_id):
        self.book_id=book_id

    def update(self):
        self.save()

    def save(self):
        data=[self.bills,
            self.book_id,
            self.status,
            self.number,
            self.student_id,
            self.end_date
            ]
        print('saved: ', data)