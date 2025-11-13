# Функції додавання, віднімання, множення та ділення перенести в файл functions.py. 
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    else:
        return a / b
    