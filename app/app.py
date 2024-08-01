import time
import random

from sqlalchemy import create_engine

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'



def add_new_row(n):
    # Connecto to the database
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    db = create_engine(db_string)

    # Insert a new number into the 'numbers' table.
    db.execute("INSERT INTO numbers (number,timestamp) "+\
        "VALUES ("+ \
        str(n) + "," + \
        str(int(3)) + ");")
    db.commit()


if __name__ == '__main__':
    while True:
        time.sleep(10)
        try:
            add_new_row(32)
        except Exception as e: 
            print('error', e)
            


        