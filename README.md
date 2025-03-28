**# AkatosferaDjango**

Приложение Django

Это REST API проект магазина, разработанный с использованием фреймворка Django.
Функционал

_# Кактегории и подкатегории:_
- управление категориями и подкатегориями из админ-панели
- каждая категория имеет : наименование, slug, изображение
- подкатегория связана с родительской категорией

_Продукты :_
-добавление, изменение, удаление продуктов через админ панель
-Продукт содеожит : наименование, slug, изображение 3 размера, цену
-Каждый продукт принадлежит подкатегории

_Эндпоинты :_
-GET/api/categories/ - список категорий с подкатегориями
-GET/api/products/ - список продуктов

_Корзина :_
- добавление товара в корзину
- изменение количества
- удаление товара из корзины
- просмотр состава корзины
- общая сумма
- количество товара

_Авторизация :_
-авторизация по токену 
-авторизация обязательна для работы с корзиной

Покрытие тестами методов GET и POST

_Swagger :_
- Документация: [`/swagger/`](http://127.0.0.1:8000/swagger/)

**# Запуск проекта локально:**

 - Клонировать репозиторий git clone https://github.com/IrinaNaumenko2808/AkatosferaDjango
 - Установить Django pip install django
 - Создать виртуальное окружение и активировать: python -m venv venv
 - Применить миграции python manage.py migrate
 - Создать суперпользователя python manage.py createsuperuser
 - Загрузить фикстуры python manage.py loaddata fixtures.json
 - Запустить сервер python manage.py runserver
