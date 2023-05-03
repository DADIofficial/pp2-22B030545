from config import params
import psycopg2

conn = psycopg2.connect(**params)

k = int(input("How many new users: "))
add_names, add_surnames, add_numbers = [], [], []

print('''Okay, write your:
 name     surname    phone''')

for i in range(0, k):
    l = input().split()
    add_names.append(l[0])
    add_surnames.append(l[1])
    add_numbers.append(l[2])

cur = conn.cursor()


cur.execute("SELECT add_many_users(%s, %s, %s)", (add_names, add_surnames, add_numbers))
conn.commit()
result = cur.fetchone()[0]
if result != None:
    print("Incorrect data: ", result)

cur.close()
conn.close()