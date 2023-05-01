import psycopg2
from config import params

db = psycopg2.connect(**params)
current = db.cursor()

sql = """
    INSERT INTO PhoneBook VALUES (%s, %s) returning *;
"""

name = input("Enter the name:")
phone_number = input("Enter the phone_number:")

current.execute(sql, (name, phone_number))
result = current.fetchone()

print("User added:")
print(result)

current.close()
db.commit()
db.close()