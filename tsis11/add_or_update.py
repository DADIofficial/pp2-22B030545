from config import params
import psycopg2

conn = psycopg2.connect(**params)

print('''Write your user:
name  surname   phone''' )
arr_user = input().split()
cur = conn.cursor()


cur.execute("CALL add_or_update_user(%s, %s, %s)", (arr_user[0], arr_user[1], arr_user[2]))
conn.commit()

cur.close()
conn.close()