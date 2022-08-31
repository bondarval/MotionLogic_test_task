# MotionLogic_test_task: сравнение данных по сетям ресторанов Burger King, KFC, McDonalds
## Описание
Проект представляет собой ORM для работы с данными по ресторанам Burger King, KFC, McDonalds(только открытые). 
Проведено извлечение данных с официальных сайтов, их группировка и обработка с помощью pandas.
На основе полученных данных сделан вывод о состоянии конкурентной среды. 
## Используемые технологии
 - Python 3.9
 - Django 4.1
 - Pandas 1.4.3
 - REST Framework 3.13.1
 - CORS headers 3.13
 - Gunicorn 20.0.4
 - PostgreSQL 12.2
 - Docker 20.10.2
 - подробнее см. прилагаемый файл зависимостей requrements.txt
## Установка
### Шаблон описания файла .env
 - DB_ENGINE=django.db.backends.postgresql
 - DB_NAME=postgres
 - POSTGRES_USER=postgres
 - POSTGRES_PASSWORD=postgres
 - DB_HOST=db
 - DB_PORT=5432
 - SECRET_KEY=<секретный ключ проекта django>
### Инструкции для развертывания и запуска приложения
для Linux-систем все команды необходимо выполнять от имени администратора
- Склонировать репозиторий
```bash
git clone https://github.com/bondarval/MotionLogic_test_task.git
```
- Выполнить вход на удаленный сервер
- Установить docker на сервер:
```bash
apt install docker.io 
```
- Установить docker-compose на сервер:
```bash
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -session)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
- Локально отредактировать файл infra/nginx.conf, обязательно в строке server_name вписать IP-адрес сервера
- Скопировать файлы docker-compose.yml и nginx.conf из директории infra на сервер:
```bash
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```
- Создать .env файл по предлагаемому выше шаблону. Обязательно изменить значения POSTGRES_USER и POSTGRES_PASSWORD
- Для работы с Workflow добавить в Secrets GitHub переменные окружения для работы:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    
    DOCKER_PASSWORD=<пароль от DockerHub>
    DOCKER_USERNAME=<имя пользователя>
    
    SECRET_KEY=<секретный ключ проекта django>

    USER=<username для подключения к серверу>
    HOST=<IP сервера>
    PASSPHRASE=<пароль для сервера, если он установлен>
    SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

    TELEGRAM_TO=<ID чата, в который придет сообщение>
    TELEGRAM_TOKEN=<токен вашего бота>
    ```
    Workflow состоит из четырёх шагов:
     - Проверка кода на соответствие PEP8
     - Сборка и публикация образа бекенда на DockerHub.
     - Автоматический деплой на удаленный сервер.
     - Отправка уведомления в телеграм-чат. 
- Собрать и запустить контейнеры на сервере:
```bash
docker-compose up -d --build
```
- После успешной сборки выполнить следующие действия (только при первом деплое):
    * провести миграции внутри контейнеров:
    ```bash
    docker-compose exec backend python manage.py migrate --no-input
    ```
    * Собрать статику проекта:
    ```bash
    docker-compose exec backend python manage.py collectstatic --no-input
    ```
    * Загрузить в базу тестовые данные(необязательно):
    ```bash
    docker-compose exec backend python manage.py loaddata fixtures.json
    ```
    * Создать суперпользователя Django (если необходимо), после запроса от терминала ввести логин и пароль для суперпользователя:
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```
### Команды для заполнения базы данными
 - Загрузить в базу тестовые данные
```bash
docker-compose exec backend python manage.py loaddata fixtures.json
```
 - При необходимости создать резервную копию данных, выполнить команду:
```bash
docker-compose exec backend python manage.py dumpdata > fixtures.json
```
 - Остановить и удалить неиспользуемые элементы инфраструктуры Docker:
```bash
docker-compose down -v --remove-orphans
```
## Авторы
- Бондарь Валерий