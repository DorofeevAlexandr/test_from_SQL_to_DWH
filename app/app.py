import time

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from hh_vacancies import get_page_vacancies
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

        json_vacancies = get_page_vacancies(text='Python Simmbirsoft', page=0)

        if json_vacancies:
            print(json_vacancies)
            for jv in json_vacancies['items']:    
                print(jv)            
                vacancie = Vacancies(
                    name = jv['name'],
                    hh_id = jv['id'],
                    published_at = jv['published_at'],
                    created_at = jv['created_at'],
                    url = jv['url'],
                )

                area = Area(
                    name= jv['area']['name'],
                    hh_id= jv['area']['id'],
                    url= jv['area']['url'],
                )
                print(*area)

                employer = Employer(
                    name= jv['employer']['name'],
                    hh_id= jv['employer']['id'],
                    url= jv['employer']['url'],
                )
        
        

                vacancie.area = area
                vacancie.employer = employer

                db.add_all([vacancie])

                #db.add(area)
                db.commit()



if __name__ == '__main__':
    time.sleep(5)
    try:
        add_postg()
    except Exception as e: 
        print('error', e)

        time.sleep(5)
    try:
        add_postg()
    except Exception as e: 
        print('error', e)
            


        