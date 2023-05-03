import psycopg2
from config import params

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
result = [['Text']]
# указываем выходной параметр incor_number
cur.execute("CALL add_many_users(%s, %s, %s, %s)", (add_names, add_surnames, add_numbers, result))
res = cur.fetchone()[0]

conn.commit()
print(res)

cur.close()
conn.close()