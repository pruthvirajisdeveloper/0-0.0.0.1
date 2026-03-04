from datetime import datetime, timedelta


class Calculate:                       #date: YYYY-MM-DD, duration: DD*
    def __init__(self):
        pass

    def end_date(self, start_date, duration):                           
        return datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=duration)
    
    def start_date(self, end_date, duration):
        return datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=duration)