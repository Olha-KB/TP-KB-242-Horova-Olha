def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return  a / b
    except ZeroDivisionError:
        print("ERROR: друге число 0")

while True:
    op = input("Введіть дію (+, -, *, /) або 'stop' для виходу: ")
    if op == "stop":
        print("Завершення програми.") 
        break  # вихід із циклу
    try:
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))   
        
           
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
        
       
    except ValueError:
     print("ERROR: потрібно вводити числа!")
   