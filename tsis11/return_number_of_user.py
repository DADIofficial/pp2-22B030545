from config import params
import psycopg2

conn = psycopg2.connect(**params)

k = int(input("Start row:"))
l = int(input("Number of row:"))

cur = conn.cursor()


cur.execute("SELECT * FROM get_users_between_rows(%s, %s)", (k, l))
result = cur.fetchall()
print(result)

conn.commit()

cur.close()
conn.close()