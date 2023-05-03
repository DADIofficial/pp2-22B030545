from config import params
import psycopg2

conn = psycopg2.connect(**params)

k = input("Who is delete? ")

cur = conn.cursor()


cur.execute("CALL delete_user(%s)", (k, ))
conn.commit()

cur.close()
conn.close()