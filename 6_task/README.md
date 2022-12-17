## Задание 6

### Описание

Реализовать класс для комплексных чисел ComplexNumber. Основные операции: сложение, вычитание, умножение, модуль числа. Покрыть тестами.
 
### Пример

```python
first = ComplexNumber(1, 2)
second = ComplexNumber(2, 3)
third = first + second
print(third) # 3 + 5i
d = {}
d[first] = 0
d[second] = 1
d[third] = d[first] + d[second]
print(d[third]) # 1
```
