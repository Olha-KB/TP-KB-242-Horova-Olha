#3)	Написати програму калькулятор використовуючи match конструкцію. 
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


match op:
    case "+":
        print("Результат:", plus(a, b))
    case "-":
        print("Результат:", minus(a, b))
    case "*":
        print("Результат:", multiply(a, b))
    case "/":
        print("Результат:", divide(a, b))
    case _:
        print("Помилка: невідома операція!")
