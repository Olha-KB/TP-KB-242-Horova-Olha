#1)	Гра з комп’ютером: камінь, ножиці, папір. Програма виконує запит від користувача на введення одного із значень 
# ["stone", "scissor", "paper"]. Наступним кроком, використовуючи модуль random, програма у випадковому порядку вибирає одне із значень 
# ["stone", "scissor", "paper"]. В залежності від умови, що камінь перемагає ножиці, ножиці перемагають папір, а папір перемагає камінь визначити переможця.
import random

user_choise = input("Please enter on of the 'stone', 'scissor', 'paper'")
random_choise = random.choice(["stone", "scissor", "paper"])
print (f"Ваш вибір: {user_choise}" )
print (f"Вибір комп'ютера: {random_choise}" )

if user_choise == random_choise:
    print("Переможців не має!")

elif (user_choise == "stone" and random_choise == "scissor") or \
     (user_choise == "scissor" and random_choise == "paper") or \
     (user_choise == "paper" and random_choise == "stone"):
    print("Вітаю! Ви перемогли")
elif user_choise != "stone" and user_choise != "scissor" and user_choise != "paper":
    print("Помилка! Неправильно введено команду")
else:
    print("Комп'ютер переміг!")
