import datetime
def dif_2days_in_sec(datetime1, datetime2):
    difdate = datetime.datetime.now()
    difdate = datetime1 - datetime2
    print(difdate.total_seconds())
datetime1 = datetime.datetime.strptime(input(), '%d/%m/%Y, %H:%M:%S')
datetime2 = datetime.datetime.strptime(input(), '%d/%m/%Y, %H:%M:%S')
dif_2days_in_sec(datetime1, datetime2)