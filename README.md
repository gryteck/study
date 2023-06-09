## Continuous Integration & Continuous Delivery

### Формулировка

Простейшее веб приложение, предоставляющее пользователю набор
операций над сущностью Person.

Приложение реализовывает API:

* `GET /persons/{personId}` – информация о человеке;
* `GET /persons` – информация по всем людям;
* `POST /persons` – создание новой записи о человеке;
* `PATCH /persons/{personId}` – обновление существующей записи о человеке;
* `DELETE /persons/{personId}` – удаление записи о человеке.

###  Пояснения
* Приложение завернуто в [Docker](Dockerfile).
* Приложение использует PostgreSQL для [взаимодействия](src/person_db.py) с бд.
* Запросы / ответы в формате JSON.
* Если запись по id не найдена, то возвращает HTTP статус 404 Not Found.
* При создании новой записи о человека (метод POST /person) возвращает HTTP статус 201 Created с пустым телом и
  Header `Location: /api/v1/persons/{personId}`, где `personId` – id созданной записи.
* В качестве веб фреймворка python используется flask
