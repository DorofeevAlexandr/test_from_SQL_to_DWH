FROM postgres:16-alpine
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database
COPY vacancies_database.sql /docker-entrypoint-initdb.d/vacancies_database.sql
