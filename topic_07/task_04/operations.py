class Operations:
    def get_numbers(self):
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
        return a, b

    def get_operation(self):
        op = input("Введіть операцію (+, -, *, /): ")
        return op
