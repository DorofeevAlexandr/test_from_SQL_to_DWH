import time
import random

import sqlalchemy as db

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'



def add_postg():
    # Connecto to the database
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    engine = db.create_engine(db_string)
    print(engine)
    conn = engine.connect()
    metadata = db.MetaData()

    areas = db.Table('area_1', metadata, 
    db.Column('id', db.BIGINT, primary_key=True, autoincrement=True),
    db.Column('hh_id', db.Text),
    db.Column('name', db.Text),
    db.Column('url', db.Text)
    )    

    metadata.create_all(engine)

    insertion_query_areas = areas.insert().values([
    {'hh_id': '123456789', 'name': 'Dolgoprudny', 'url': 'http'},
    {'hh_id': '012', 'name': 'dsghg', 'url': 'httpss'},
    ])

    conn.execute(insertion_query_areas)
    conn.commit()



if __name__ == '__main__':
    while True:
        time.sleep(10)
        try:
            add_postg()
        except Exception as e: 
            print('error', e)
            


        