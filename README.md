# Проект Натальи Ключевской (Опросники-знакомства)

## Как запустить проект

1. `python .\backend\manage.py runserver` - dev-сервер бэкенда
2. `npm run serve` - dev-сервер фронтенда

## Как начать работу над проектом

1. Установить Python глобально (проверить - `python --version`)
2. `pip install --user pipenv` - Установить pipenv глобально
3. Установить npm глобально (проверить - `npm -v`)
4. Установить vue-cli глобально (проверить - `vue --version`)

## Структура проекта

| Локация    | Содержание                           |
| ---------- | ------------------------------------ |
| `/backend` | Django проект & Backend-конфигурация |
| `/src`     | Vue приложение                       |

## Технический стек проекта

1. Фронтенд
   1. Vue.js
2. Бэкенд
   1. Python Django
   2. DjangoRESTFramework

## Как создать аналогичный проект

1. Создаём `.gitignore` и `README.md` по шаблону
2. `python -m venv venv`
3. `.\venv\Scripts\activate`
4. `django-admin startproject **название-проекта**`
5. `vue create src`
6. Настроить `vue.config.js`
