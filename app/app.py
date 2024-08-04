import time

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from hh_vacancies import get_page_vacancies, copy_vacancie


SEARCH_REQUEST = 'Data engineer'

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'


def load_vacancies_save_postgres():
    # Connecto to the database
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    engine = create_engine(db_string)
    print(engine)

    with Session(autoflush=False, bind=engine) as db:
        pages_count = get_page_vacancies(text=SEARCH_REQUEST, page=0)['pages']
        for page in range(pages_count):
            json_vacancies = get_page_vacancies(text=SEARCH_REQUEST, page=page)
            if json_vacancies:
                print(json_vacancies)
                for jv in json_vacancies['items']:    
                    print(jv)            
                    vacancie = copy_vacancie(jv)
                    db.add_all([vacancie])
                    #db.add(area)
                    db.commit()


if __name__ == '__main__':
    time.sleep(5)
    try:
        load_vacancies_save_postgres()
    except Exception as e: 
        print('error', e)
