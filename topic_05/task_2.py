#2)	Програма конвертування іноземної валюти в українську гривню. Для отримання актуальних курсів валют необхідно використовувати
#  API НБУ та модуль, що надає можливість виконувати запити до сторонніх сервісів requests. Достатня умова роботи – можливість
#  конвертації для трьох іноземних валют EUR, USD, PLN. Користувачу надається можливість введення кількості та типу валюти, результат
# роботи програми – конвертоване значення в українських гривнях.

import requests
response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

try:
    user_choise = input("Будь ласка, виберіть валюту 'EUR' , 'USD', 'PLN'")

    for elem in response.json():
        if (elem["cc"] == "EUR" or elem["cc"] == "USD" or elem["cc"] == "PLN" ):
            if elem["cc"] ==  user_choise:
                rate = elem["rate"]
                print (f"Курс: {rate}")
                break

    suma = int(input("Введіть суму:"))
    resultat = suma * rate
    print (f"Вибрана валюта: {user_choise}")
    print (f"Сума: {suma}")
    print (f"Конвертоване значення в гривнях: {resultat}")
except Exception as ex:
    print(type(ex))
    print(ex)
