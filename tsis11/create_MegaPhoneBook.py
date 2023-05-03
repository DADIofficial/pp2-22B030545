import psycopg2
from config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    CREATE TABLE MegaPhoneBook(
        user_name VARCHAR,
        user_surname VARCHAR,
        phone_number VARCHAR
    );
"""

current.execute(sql)

current.close()
db.commit()
db.close()