import datetime
def minusmicrosec():
    print(datetime.datetime.now() - datetime.timedelta(microseconds = 1))
minusmicrosec()