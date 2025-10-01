#1)	Написати функцію пошуку коренів квадратного рівняння використовуючи
#  функцію розрахунку дискримінанту з попередньої теми та умовні переходи.
import math

def discr(a, b, c):
    return b * b - 4 * a * c
a = int(input("What's a: "))
b = int(input("What's b: "))
c = int(input("What's c: "))
D = discr(a, b, c)
print("Discriminant (D) =", D)

def coreny(a, b, D):
    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        print("Коренів немає")
coreny(a, b, D)
