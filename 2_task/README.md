## Задание 2

### Описание

Реализовать конвертер из csv файла в json объект. На вход программа принимает csv файл, результатом работы программы является файл *.json, содержимым которого является сконвертированные csv в json.
Программа должна быть покрыта тестами, учесть крайние случаи, что файл может быть пустым, некоторых значений может и не быть в csv

Необходимо реализовать 2 решения:
1. Без использования сторонних модулей
2. С использованием модулей import csv, import json 



### Пример

<details><summary>Вход</summary><blockquote>

input.csv

```
id,name,birth,salary,department
1,Ivan,1980,150000,1
2,Alex,1960,200000,5
3,Ivan,,130000,8
```
</blockquote></details>

<details><summary>Выход</summary><blockquote>

output.json

```
[
 {
   id: 1,
   name: Ivan,
   birth: 1980,
   salary: 150000,
   department: 1
 },
 {
   id: 2,
   name: Alex,
   birth: 1960,
   salary: 200000,
   department: 5
 },
 {
   id: 3,
   name: Ivan,
   birth: null,
   salary: 130000,
   department: 8
 }
]
```
</blockquote></details>
