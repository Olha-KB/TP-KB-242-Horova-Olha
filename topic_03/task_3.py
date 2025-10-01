#3)	Написати програму тестування функцій словників таких як: 
# update(), del(), clear(), keys(), values(), items()
def testing():
    # Початковий словник
    original = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "F": 5
    }
    
    print("Початковий словник:", original)
    
    # update() – додавання нових або зміна існуючих значень
    original.update({"B": 20, "E": 6})
    print("Після update({'B': 20, 'E': 6}):", original)
    
    # del – видалення елемента за ключем
    del original["C"]
    print("Після del original['C']:", original)
    
    # clear() – очищення словника
    temp_dict = original.copy()  # створимо копію для подальшої роботи
    temp_dict.clear()
    print("Після clear():", temp_dict)
    
    # keys() – отримання ключів
    print("Ключі словника:", original.keys())
    
    # values() – отримання значень
    print("Значення словника:", original.values())
    
    # items() – отримання пар (ключ, значення)
    print("Пари ключ-значення:", original.items())

# Виклик функції
testing()