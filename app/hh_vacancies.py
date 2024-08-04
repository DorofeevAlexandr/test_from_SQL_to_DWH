import requests      
import json          


# Функция для получения вакансий
def get_page_vacancies(text, page):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': text,
        'per_page': 1,
        'page': page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

get_page_vacancies(text='Data engineer', page=0)