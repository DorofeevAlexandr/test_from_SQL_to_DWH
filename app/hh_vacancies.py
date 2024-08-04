import requests      
import json     

from models import Area, Employer, Vacancies 


# Функция для получения вакансий
def get_page_vacancies(text, page):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': text,
        'per_page': 100,
        'page': page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def copy_vacancie(in_json):
    vacancie = Vacancies(
        name = in_json['name'],
        hh_id = in_json['id'],
        published_at = in_json['published_at'],
        created_at = in_json['created_at'],
        url = in_json['url'],
    )

    area = Area(
        name= in_json['area']['name'],
        hh_id= in_json['area']['id'],
        url= in_json['area']['url'],
    )
    print(*area)

    employer = Employer(
        name= in_json['employer']['name'],
        hh_id= in_json['employer']['id'],
        url= in_json['employer']['url'],
    )     

    vacancie.area = area
    vacancie.employer = employer
    return vacancie
