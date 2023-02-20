import datetime
def minus5day():
    print(datetime.datetime.now() - datetime.timedelta(days = 5))
minus5day()