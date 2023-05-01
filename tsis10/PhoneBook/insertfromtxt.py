import psycopg2
from config import params

db = psycopg2.connect(**params)
current = db.cursor()

sql = """
    INSERT INTO PhoneBook VALUES (%s, %s, %s) returning *;
"""

with open("New_user.txt", "r") as f:
    lines = f.readlines()
    name = lines[0].strip()
    phone_number = lines[1].strip()
    city = lines[2].strip()
    new_user = (name, phone_number, city)

current.execute(sql, new_user)
result = current.fetchone()

print("User added:")
print(result)

current.close()
db.commit()
db.close()