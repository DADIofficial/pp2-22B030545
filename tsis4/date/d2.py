import datetime
def today():
    print(datetime.datetime.now())
def yesterday():
    print(datetime.datetime.now() - datetime.timedelta(days=1))
def tommorow():
    print(datetime.datetime.now() + datetime.timedelta(days=1))