# Тестовое задание для кандидата на Backend-практикум «От SQL до DWH»

В проекте реализовано:
- Получение данных о вакансиях "Data Engineer" на сайте HH.ru.
- Развертывание приложения в Docker контейнере.
- Развертывание базы данных PostgreSQL в Docker контейнере.
- Подключение к БД при помощи современных UI инструментов (например, DBeaver или аналогичных сред).

Для развертывания приложения нужно:
- Установить на компьютер: Git, Python3, Docker и Docker-Compouse.
- Склонировать git репозиторий на компьютер.
$ git clone https://github.com/DorofeevAlexandr/test_from_SQL_to_DWH.git

- Собрать образы командой. 
$ sudo docker compose build

- Запустить контейнеры командой.
$ sudo docker compose up -d
 
- Лог выполнения приложения можно проверить командой.
$ sudo docker logs --tail 100 test_from_sql_to_dwh-app-1

Для просмотра данных в базе, нужно подключиться к базе PostgreSQL в  Docker контейнере,
со следующими параметрами:
 POSTGRES_PASSWORD=secret
 POSTGRES_USER=username
 POSTGRES_DB=database
 POSTGRES_PORT='5431'
