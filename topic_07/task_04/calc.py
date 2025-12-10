from functions import Functions
from operations import Operations
class Calculator:
    def __init__(self):
        self.funct = Functions()
        self.op = Operations()

    def run(self):
     while True:
        a, b = self.op.get_numbers()
        op = self.op.get_operation()
        if op == '+':
            print(f"Результат: { self.funct.plus(a, b)}")
        elif op == '-':
            print(f"Результат: { self.funct.minus(a, b)}")
        elif op == '*':
            print(f"Результат: { self.funct.multiply(a, b)}")
        elif op == '/':
            print(f"Результат: { self.funct.divide(a, b)}")
        else:
            print("Неправильний оператор!")


if __name__ == "__main__":
    calc= Calculator()
    calc.run()
