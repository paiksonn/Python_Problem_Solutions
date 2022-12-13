## Задание 1

### Описание

Реализовать конвертер c форматированием. На входе файл *.py c содержимым в виде описания задачи и исходного кода задачи, на выходе файл *.md с оформленным форматированием под markdown формат. Если *.md файл не пуст, то осуществить дозапись в файл новой задачи без перезаписи содержимого.
Программа должна быть покрыта тестами.

### Пример 1
<details><summary>Вход</summary><blockquote>
    
solution.py

```
# title Print Hello
# description Напечатать на экран Hello!
# ---end----
def print_hello():
    print('Hello!')
    
```    
 
out.md
````
````
</blockquote></details>


<details><summary>Выход</summary><blockquote>

out.md

````
+ [Print Hello](#print-hello)
## Print Hello
Напечатать на экран Hello!
```python 
def print_hello():
    print('Hello!')
```
````
</blockquote></details>

### Пример 2

<details><summary>Вход</summary><blockquote>

solution.py

```
# title Print Greeting
# description Напечатать на экран Greeting!
# ---end----
def print_greeting():
    print('Greeting!')
    
```    
 
out.md

````
+ [Print Hello](#print-hello)
## Print Hello
Напечатать на экран Hello!
```python 
def print_hello():
    print('Hello!')
```
````
</blockquote></details>
    
<details><summary>Выход</summary><blockquote>

out.md

````
+ [Print Hello](#print-hello)
+ [Print Greeting](#print-greeting)
## Print Hello
Напечатать на экран Hello!
```python 
def print_hello():
    print('Hello!')
```
## Print Greeting
Напечатать на экран Greeting!
```python 
def print_greeting():
    print('Greeting!')
```
````
</blockquote></details>
