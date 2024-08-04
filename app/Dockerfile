FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
COPY models.py models.py
COPY hh_vacancies.py hh_vacancies.py
CMD ["python", "-u", "app.py"]