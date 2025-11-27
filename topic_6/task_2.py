#2)	Маючи не відсортований список, елементами якого є словники з двома параметрами (ім’я та оцінка) 
# виконати сортування списку, використовуючи стандартну функцію sorted(). Другим параметром для функції
#  sorted() має бути lambda функція, що повертає ім’я або оцінку із елемента словника.

studentList = [
    {'name': 'Zak', 'mark': 85},
    {'name': 'Anna', 'mark': 87},
    {'name': 'Bob', 'mark': 88},
    {'name': 'Ada', 'mark': 76},
    {'name': 'Iryna', 'mark': 90}
]

print("Сортування за іменем: ")
for elem in sorted(studentList, key=lambda student: student["name"]):
    print(f"Name = {elem['name']}  mark = {elem["mark"]}")

print("\nСортування за оцінкою: ")
for elem in sorted(studentList, key=lambda student: student["mark"]):
    print(f"Name = {elem['name']}  mark = {elem["mark"]}")
    