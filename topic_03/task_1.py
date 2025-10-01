#1)	Написати програму калькулятор з постійними запитами на введення нових даних та операцій.
#  За основу взяти програму калькулятор з попередньої теми.
#  Реалізувати механізм завершення програми після отримання відповідної команди.
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

print("Калькулятор. Для завершення введіть команду 'stop'.")

while True:
    op = input("Введіть дію (+, -, *, /) або 'stop' для виходу: ")

    if op == "stop":
        print("Завершення програми.")
        break  # вихід із циклу

    try:
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: потрібно вводити числа!")
        continue

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
    