Домашка 7
---
https://otus.ru/lessons/microservice-architecture/

Создать сервис "Заказ" и для одного из его методов, например, "создание заказа" сделать идемпотетным.
На выходе должно быть:
0) описание того, какой паттерн для реализации идемпотентности использовался
команда установки приложения (из helm-а или из манифестов). Обязательно указать в каком namespace нужно устанавливать и команду создания namespace, если это важно для сервиса.
тесты в postman
В тестах обязательно
использование домена arch.homework в качестве initial значения {{baseUrl}}

Используемый паттерн - заголовок ETag

Раскатка: 
~~~
minikube addons enable ingress


eval $(minikube docker-env) && docker build -t myapp:latest -f app/Dockerfile ./app
helm install my-release ./order-service-chart
~~~

