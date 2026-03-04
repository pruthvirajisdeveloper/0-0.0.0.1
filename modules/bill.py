class Bill:
    def __init__(self, id, total, paid, date):
        self.pmts=[]
        self.id=id
        self.total=total
        self.paid=paid
        self.date=date

    def new_payment(self, amt, date): #amt:'[total, paid]'
        total=amt[0]
        paid=amt[1]
        self.total += total
        self.paid += paid
        self.pmts.append([amt, date])
        return [self.paid, self.total, self.total-self.paid, date]

    def save(self):
        pass


if __name__ == "__main__":
    a=Bill(id='b0001', paid=100, total=300)
    b=a.new_payment(amt=[100, 200], date='')
    print(b)