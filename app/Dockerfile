FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
COPY models.py models.py
CMD ["python", "-u", "app.py"]