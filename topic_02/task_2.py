#2)	Написати програму калькулятор використовуючи if else конструкцію. 
# Кожна операція має бути виконана в окремій функції.

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль!"

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
op = input("Введіть дію (+, -, *, /): ")

if op == "+":
    print("Результат:", plus(a, b))
elif op == "-":
    print("Результат:", minus(a, b))
elif op == "*":
    print("Результат:", multiply(a, b))
elif op == "/":
    print("Результат:", divide(a, b))
else:
    print("Помилка: невідома операція!")
    