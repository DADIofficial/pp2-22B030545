from config import params
import psycopg2

conn = psycopg2.connect(**params)

k = input("Who is find? ")

cur = conn.cursor()


cur.execute("SELECT * FROM return_all_same_user(%s)", (k, ))
result = cur.fetchall()
print(result)

conn.commit()

cur.close()
conn.close()