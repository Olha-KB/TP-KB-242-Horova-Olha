#4)	Маючи відсортований список, написати функцію пошуку позиції для вставки нового елементу в список.
def find_position(sorted_list, new_element):
    for i, item in enumerate(sorted_list):
        if new_element <= item:
            return i
    return len(sorted_list)

my_list = ["A", "B", "C", "D", "E", "F"]
new_elem = "D"  

position = find_position(my_list, new_elem)
print(f"Список: {my_list}")
print(f"Нова позиція для '{new_elem}': {position}")
