# Проект SageLove

## Как запустить проект

```
# Для того, чтобы собрать контейнеры при запуске, если раньше не были собраны
$ docker-compose up -d --build

# Для того, чтобы собрать контейнеры при запуске, если раньше не были собраны
$ docker-compose up -d
```

## Документации используемых пакетов

- [Django REST framework JWT](https://jpadilla.github.io/django-rest-framework-jwt)
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)

## Полезные статьи

- [Registration and Authentication in Django apps with dj-rest-auth](https://www.rootstrap.com/blog/registration-and-authentication-in-django-apps-with-dj-rest-auth/)
- [JWT Authentication in Vue.js and Django Rest Framework — Part 1](https://hackernoon.com/jwt-authentication-in-vue-js-and-django-rest-framework-part-1-c40c5c0d4f6e)
- [JWT Authentication in Vue.js and Django Rest Framework — Part 2](https://medium.com/hackernoon/jwt-authentication-in-vue-js-and-django-rest-framework-part-2-788f0ad53ad5)

#### Особенности стилей

- Для кнопок в стандартном их понимании используем класс my-button, если у них есть паддинг по бокам около 37px, то добавляем класс wide-padding



accounts/mutations.py

CreateChat — создание чата
CreateMessage — создание сообщение
DeleteChat — удаление чата

accounts/shema.py

chats_for_user — все чаты пользователя
messages_for_chat — все сообщения в чате (с пагинацией, first - сколько первых элементов нужно вывести, skip - сколько нужно пропустить)

backend/shema.py

message_created — подписка отслеживает новые сообщения в чате
chat_created — подписка отслеживает создание чата для пользователя
chat_deleted — подписка отслеживает удfление чата по id чата
