# SQL

Запросы на выборку

```
SELECT * 
FROM `USERS` 
WHERE `NAME` AND `ID` < 5 
LIKE '%Мышь%';
```

Перемножение таблиц

```angular2html
SELECT `USERS`.`NAME`, `FOOD`.`PRODUCT` 
FROM `USERS` INNER JOIN `FOOD` ON `USERS`.`ID`=`FOOD`.`USER_ID`
WHERE `USERS`.`NAME` LIKE 'Мышь';
```

Многостолбцовые подзапросы

```angular2html
SELECT Reservations.* FROM Reservations
INNER JOIN Rooms
ON Reservations.room_id = Rooms.id
WHERE Reservations.price = Rooms.price;
```

Порядок выполнения функций: 
```angular2html
SELECT > FROM > WHERE > GROUP BY > HAVING > ORDER BY
```

Оконные функции:

1. Агрегирующие (Aggregate)
```
select name, subject, grade,
sum(grade) over (partition by name) as sum_grade,
avg(grade) over (partition by name) as avg_grade,
count(grade) over (partition by name) as count_grade,
min(grade) over (partition by name) as min_grade,
max(grade) over (partition by name) as max_grade
from student_grades;
```
2. Ранжирующие (Ranking)
```angular2html
select name, subject, grade,
row_number() over (partition by name order by grade desc),
rank() over (partition by name order by grade desc),
dense_rank() over (partition by name order by grade desc)
from student_grades;
```
3. Функции смещения (Value)
```angular2html
select name, quartal, subject, grade, 
lag(grade) over (order by quartal) as previous_grade,
lead(grade) over (order by quartal) as next_grade
from grades_quartal;
```
Хранимые процедуры (SP)
```angular2html
CREATE OR REPLACE PROC uspGetEmployees
AS
SELECT *
FROM Person.Person
WHERE MiddleName IS NOT NULL;
GO
```
Запуск процедуры:
```EXEC uspGetEmployees;```