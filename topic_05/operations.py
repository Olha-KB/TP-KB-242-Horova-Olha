# Функції запиту на введення даних для операцій та самих операцій перемістити в файл operations.py. 

def get_numbers():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    return a, b


def get_operation():
    op = input("Введіть операцію (+, -, *, /): ")
    return op
