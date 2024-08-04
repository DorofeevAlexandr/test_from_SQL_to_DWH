import time
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Area, Employer, Vacancies 


db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'



def add_postg():
    # Connecto to the database
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    engine = create_engine(db_string)
    print(engine)

    with Session(autoflush=False, bind=engine) as db:
        # создаем компании

        area = Area(name= 'Saransk',
                     hh_id='123',
                     url= 'http'
                     )
        print(area)

        employer = Employer(name= 'Simbirsoft',
                            hh_id='456',
                            url= 'httpss'
                            )
        
        vacancie = Vacancies(
            name = 'python developer',
            hh_id = '56',
            published_at = '------',
            created_at = '------',
            url = '------'
        )

        vacancie.area = area
        vacancie.employer = employer

        # добавляем компании в базу данных, и вместе с ними добавляются пользователи
        db.add_all([vacancie])

        #db.add(area)
        db.commit()



if __name__ == '__main__':
    while True:
        time.sleep(5)
        try:
            add_postg()
        except Exception as e: 
            print('error', e)
            


        