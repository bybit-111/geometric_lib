# Geometric_lib



## Основная информация

Geometric_lib - библиотека для вычисления периметра и площади фигур.

---

## Описание функций

### Круг (`cicle.py`)
```python
import math


def area(r):
    '''Принимает число r, возвращает квадрат числа r, умноженный на pi'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает число r, умноженное на pi и на 2'''
    return 2 * math.pi * r

area(10)
perimeter(10)
```

### Квадрат (`square.py`)
```python
def area(a):
    '''Принимает число a, возвращает квадрат числа a'''
    return a * a


def perimeter(a):
    '''Принимает число a, возвращает число a, умноженное на 4'''
    return 4 * a

area(10)
perimeter(10)
```

### Прямоугольник (`rectangle.py`)
```python
def area(a, b):
    '''Принимает числа a и b, возвращает произведения чисел a на b'''
    return a * b


def perimeter(a, b):
    '''Принимает числа a и b, возвращает удвоенную сумму чисел a и b'''
    return 2 * (a + b)

area(10, 10)
perimeter(10, 10)
```

### Треугольник (`triangle.py`)
```python
def area(a, h):
    '''Принимает числа a и h, возвращает произведения чисел a на h, деленное на 2'''
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает числа a, b и c, возвращает сумму чисел a, b и c'''
    return a + b + c

area(10, 5)
perimeter(10, 4, 6)
```

---

## История изменения проекта


|  Хэш   |               История                     |
| ------ | ----------------------------------------- |
| d3d4f8e| New files rectangle.py and triangle.py    |
| 86edb1c| L-05: Update Docs. Add user agreement info|
| 438b89a| L-05: Add user agreement                  |
| 6adb962| L-03: Docs added                          |
| 3049431| L-04: Add rectangle.py                    |
| b5b0fae| L-04: Update docs for calculate.py        |
| d76db2a|L-04: Add calculate.py                     |
| 51c40eb|L-04: Doc updated for triangle             |
| d080c78|L-04: Triangle added                       |
| d078c8d|L-03: Docs added                           |
| 8ba9aeb|L-03: Circle and square added              |


---