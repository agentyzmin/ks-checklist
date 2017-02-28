# Киевский стандарт - чеклист
Демодоступ
  https://pure-river-13970.herokuapp.com/
  login: demo
  pass: demodemo
## Установка на локал
### Для запуска на локале потребуеться
- python 3.6 (https://www.python.org/downloads/)
- postgresql (https://www.postgresql.org/download/)

1. Устанавливаем python и postgresql, создаем БД
2. Скачиваем репозиторий
3. Заходим в папку с репозиторием, открываем файл settings.py в папаке checklist

  Заменяем
  ```sh
  ALLOWED_HOSTS = ['pure-river-13970.herokuapp.com']
  ```
  на
  ```sh
  ALLOWED_HOSTS = []
  ```
  Заменяем
  ```sh
  DATABASES = {
     'default': dj_database_url.config(
         default='postgres://xrcpwnpfhurdqz:1c311de293b7dcc7c0098c5845f2c6d0a7c074839818c60561d56d7a4fad50e2@ec2-54-235-173-161.compute-1.amazonaws.com:5432/dris91t2ltg5e'),
  }
  ```
  на
  ```sh
  DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'YourDBName',
         'USER': 'YourUserName',
         'PASSWORD': 'YourPassword',
     }
  }
  ```
  И заполняем данные для доступа в БД в полях NAME, USER, PASSWORD.

4. Активируем venv

  Заходим в папку репозитория в терминале и выполняем
  ```sh
  $ source venv/bin/activate
  ```

5. Запускаем миграцию моделей в БД
  ```sh
  python manage.py migrate
  ```

6. Создаем пользователя для входа в админку
  ```sh
  python manage.py createsuperuser
  ```
  Вводим логин и пароль

7. Запускаем Django сервер
  ```sh
  python manage.py runserver
  ```
  (по умолчанию запускает проект на 127.0.0.1, если необходимо указать порт, выполняем python manage.py runserver 8000 или любой другой порт)

8. Создадим ЖК и вопросы

  * Заходим в админку 127.0.0.1/admin
  * Создаем ЖК в Apartment и вопросы в Question

### Вуаля!
