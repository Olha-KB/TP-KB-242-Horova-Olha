#3)	Використання модулів для програми калькулятор. Функції додавання, віднімання, множення та ділення перенести в файл functions.py. 
# Функції запиту на введення даних для операцій та самих операцій перемістити в файл operations.py. 
# Програму калькулятор реалізувати в файлі calc.py, до якого підключають файл functions.py та operations.py.
from funct import plus
from funct import minus
from funct import multiply
from funct import divide

from operations import get_numbers
from operations import get_operation

def main():
    while True:
        a, b = get_numbers()
        op = get_operation()
        if op == '+':
            print(f"Результат: {plus(a, b)}")
        elif op == '-':
            print(f"Результат: {minus(a, b)}")
        elif op == '*':
            print(f"Результат: {multiply(a, b)}")
        elif op == '/':
            print(f"Результат: {divide(a, b)}")
        else:
            print("Неправильний оператор!")

main()
