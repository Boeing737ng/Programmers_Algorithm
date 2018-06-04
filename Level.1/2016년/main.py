import datetime

def solution(a, b):
    week_days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return week_days[datetime.date(2016,a,b).weekday()]