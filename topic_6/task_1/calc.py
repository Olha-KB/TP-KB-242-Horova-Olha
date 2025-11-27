#3)	Використання модулів для програми калькулятор. Функції додавання, віднімання, множення та ділення перенести в файл functions.py. 
# Функції запиту на введення даних для операцій та самих операцій перемістити в файл operations.py. 
# Програму калькулятор реалізувати в файлі calc.py, до якого підключають файл functions.py та operations.py.


from functions import plus
from functions import minus
from functions import multiply
from functions import divide

from operations import get_numbers
from operations import get_operation

# Функція логування
def write_log(text):
    with open("log.txt", "a") as file:
        file.write(text + "\n")

def main():
    while True:
        a, b = get_numbers()
        op = get_operation()

        if op == '+':
            result = plus(a, b)
        elif op == '-':
            result = minus(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            print("Invalid operation!")
            write_log(f"ERROR: Invalid operation! {op}")
            continue

        write_log(f"{a}{op}{b}={result} ")
        write_log("-------------------------")

main()
