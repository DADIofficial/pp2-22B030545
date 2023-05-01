import psycopg2
from config import params


change = int(input('''
What you want change:
1-name 2-number 3-city
'''))
changer=input("Okay, Who is this? ")

db=psycopg2.connect(**params)
current=db.cursor()

if change == 1:
    sql = """
        UPDATE PhoneBook SET person_name=%s WHERE person_name=%s;
    """
if change == 2:
    sql = """
        UPDATE PhoneBook SET phone_number=%s WHERE person_name=%s;
    """
if change == 3:
    sql = """
        UPDATE PhoneBook SET city=%s WHERE person_name=%s;
    """
db=psycopg2.connect(**params)
current=db.cursor()

current.execute(sql, (input("New value: "), changer))

current.close()
db.commit()
db.close()