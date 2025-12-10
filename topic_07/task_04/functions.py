class Functions:

    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
           return "Помилка: ділення на нуль!"
        else:
            return a / b
    