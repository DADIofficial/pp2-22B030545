import psycopg2
import csv
from config import params

db = psycopg2.connect(**params)
cursor = db.cursor()

insert_query = "INSERT INTO PhoneBook (person_name, phone_number) VALUES (%s, %s)"

with open('New_user.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute(insert_query, row)
        db.commit()

cursor.close()
db.close()