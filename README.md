"# Django-DRF-Postgres-DockerCompose"

ToDo List API + парсер https://astanahub.com/ru/service/techpark/ Сервис Todo list построен на фреймворке Django + Django Rest Framework + БД Postgres. Включает в себя стандартный API с CRUD операциями, авторизацией (email + password + DRF TokenAuth) и регистрацией пользователей с ограничением доступа для незарегистрированных пользователей. На главной странице сервиса реализована пагинация и запущен Swagger. Тестировал вручную и для удобства собрал простой UI на localhost:8000. Запускается через команду docker compose up —build

