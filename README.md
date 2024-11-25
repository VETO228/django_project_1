# TaskTracker

TaskTracker представляет из себя упрощенною систему управлением задач, которая позволит
пользователям создавать и управлять проектами и задачами, назначать исполнителей и
отслеживать статус выполнения.

## Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Настройка](#настройка)
- [Запуск проекта](#запуск-проекта)
- [Использование](#использование)
- [Тестирование](#тестирование)


## Требования

Перечислите зависимости вашего проекта. Например:

- Python (версия 3.13)
- Django (версия 5.1.3)
- Channels (версия 4.2.0)
- Django Rest Framework (версия 3.15.2)
- Django Rest Framework simpleJWT (версия 5.3.1)
- Pillow (версия 11.0.0)
- Djoser (версия 2.3.1)
- drf_yasg (версия 1.21.8)
- drf-spectacular (версия 0.27.2)
- django-filter (версия 24.3)
- docker (версия 7.1.0)
- corsheaders (версия 4.6.0)
- 

## Установка
git clone https://github.com/VETO228/django_project_1/tree/frei
cd ./django_project_1/

python -m venv venv
source venv/bin/activate  # Для MacOS/Linux
venv\Scripts\activate  # Для Windows

pip install -r requirements.txt

## Настройка

Создайте файл .env и добавьте необходимые переменные окружения:

SECRET_KEY='django-insecure-t=!^p5gub4s%**t_x)011$glc4w35=g5u32s8qkzo4ylwo-be3'
DEBUG=True
DATABASE_URL= {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            'USER': os.environ.get('DJANGO_DB_USER', 'your_db_user'),
            'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'your_db_password'),
            'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),
            'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
        } 
    }

Выполните миграции базы данных:

python manage.py migrate

## Запуск проекта

python manage.py runserver

## Использование

Регистрация:

Нажимаете на кнопку 'Регистрация' и регистрируетесь

Вход:

Нажимаете на кнопку 'Вход' и входите в свой аккаунт

Создание проекта:

Нажимаете на кнопку 'Создать проект' и создайте свой проект

Просмотр проектов:

Нажимаете на кнопку 'Проекты' и сможете просмотреть проекты и их сортировать

Создание задачи:

Нажимаете на кнопку 'Создание задачи' и создайте свою задачу

Просмотр задач:

Нажимаете на кнопку 'Задачи' и сможете просмотреть задачи и их сортировать

Редактирование проекта:

Введите в URL-адрессе
http://127.0.0.1:8000/api/v1/project/айди_проекта/update
и вы сможете редактировать свой проект

Удаление проекта:

Введите в URL-адрессе
http://127.0.0.1:8000/api/v1/project/айди_проекта/delete
и вы сможете удалить свой проект

Редактирование задачи:

Введите в URL-адрессе
http://127.0.0.1:8000/api/v1/task/айди_проекта/update
и вы сможете редактировать свою задачу

Удаление задачи:

Введите в URL-адрессе
http://127.0.0.1:8000/api/v1/task/айди_проекта/delete
и вы сможете удалить свою задачу

## Тестирование

python manage.py test