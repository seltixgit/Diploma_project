Дипломные проект "Сервис авторизации по номеру телефона".
В данном проекте используются следующие технологии:
Python - высокоуровневый язык программирования общего назначения.

Django Rest Framework (DRF) — набор инструментов для создания веб-сервисов и API на основе фреймворка Django.

PostgreSQL — свободная объектно-реляционная система управления базами данных (СУБД).

Описание:
В проекте разработана реферальная система, которая позволяет пользователям регистрироваться и авторизоваться по номеру телефона,
а также использовать и распространять инвайт-коды.

После отправки в запросе номера телефона генерируется 4-х значный код авторизации.
При повторном запросе вводится полученный код. В случае совпадения данных авторизация успешна.

Ранее не авторизованный пользователь записывается в базу. Ему также автоматически присваивается 6-значный код для приглашения других пользователей (invite код).
При повторной авторизации присваивается новый 4-х значный код авторизации.

Пользователю доступно получение и редактирование своего профиля. Реализована возможность применить один чужой invite-код.
Так же в API профиля доступен список пользователей, которые ввели invite-код текущего пользователя.

Установка и запуск приложения:
Клонируйте проект на свое устройство.
Настройте виртуальное окружение и установите зависимости из "requirements.txt".
Создайте в корне проекта файл ".env" и заполните его по образцу из файла ".env.sample".
Примените миграции командой "python manage.py migrate".
Для запуска проекта выполните команду "python manage.py runserver".
Запуск проекта через Docker:
Создайте в корне проекта файл ".env" и заполните его по образцу из файла ".env.sample". Параметр для подключения к БД должен быть "HOST=database".
Для сборки и запуска контейнеров выполните команду "docker-compose up -d --build"

Описание API запросов:

HTTP метод POST отправляет номер телефона для запроса кода на авторизацию.
url http://127.0.0.1:8000/api/users/login/
parameters:
phone - номер телефона в формате (+7 ....)
{"phone": "номер телефона"}
Получение 4-х значного кода на авторизацию пользователя.

HTTP метод PUT отправляет на сервер полученный пользователем код авторизации.
url http://127.0.0.1:8000/api/users/login/
parameters:
auth_code - 4-х значный код авторизации
{"auth_code": "код авторизации"}
Получение доступа (Авторизация).

HTTP метод POST отправляет номер телефона и код для получения токена.
url http://127.0.0.1:8000/api/users/token/
parameters:
phone - номер телефона в формате (+7 ....)
password - 4-х значный код авторизации
{"phone": "номер телефона", "password": "код авторизации"}
Получение токена для аутентификации пользователя.

HTTP метод GET (необходимо передать в Headers Bearer Token) для получения информации из профиля.
url http://127.0.0.1:8000/api/users/ {user_id}/
Получение информации из профиля пользователя.

HTTP метод PUT (необходимо передать в Headers Bearer Token) для обновления информации.
url http://127.0.0.1:8000/api/users/ {user_id}/
parameters:
phone - номер телефона (обязательное поле)
avatar - аватар
email - электронная почта
city - город
telegram_id - телеграм ID
referral_code - invite-код от другого пользователя
{"phone": "номер телефона", "referral_code": "invite-код"}
Обновление информации в профиле пользователя.

HTTP метод DELETE (необходимо передать в Headers Bearer Token) для удаления профиля.
url http://127.0.0.1:8000/api/users/ {user_id}/
Удаление профиля пользователя.

HTTP метод GET (необходимо передать в Headers Bearer Token) для просмотра списка пользователей.
url http://127.0.0.1:8000/api/users/list/
Просмотр зарегистрированных пользователей модератором или администратором.

Дополнительные URL:

http://127.0.0.1:8000/admin/ панель администратора

Администратора можно создать командой python manage.py createsuperuser

http://127.0.0.1:8000/swagger/ автодокументация swagger

http://127.0.0.1:8000/redoc/ автодокументация redoc