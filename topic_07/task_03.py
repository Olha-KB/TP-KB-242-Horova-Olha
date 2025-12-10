#3)	Розробити клас Student атрибутами якого э два параметра name та age. Створити список елементами якого є об'єкти класу Student. 
# Написати цикл який виводить на екран елементи списку у відсортованому порядку. 
# Для сортування використати стандартну функцію sorted. Функція sorted має використовувати lambda функцію для визначення ключа сортування.\
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} with age {self.age}"


students = [
    Student("Zak", 19),
    Student("Anna", 17),
    Student("Bob", 22),
    Student("Iryna", 20)
]

print("Сортування за іменем: ")
sorted_students = sorted(students, key=lambda student: student.name)
for student in sorted_students:
    print(student)

print("\nСортування за віком: ")
sorted_students = sorted(students, key=lambda student: student.age)
for student in sorted_students:
    print(student)

