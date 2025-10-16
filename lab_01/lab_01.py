#Реалізувати відсортований телефонний довідник студентів групи.

## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@gmail.com", "group":"kb-242"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "group":"kb-241"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "group":"kb-243"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "group":"kb-244"}
]

def printAllList():
    print("{:<10} {:<12} {:<25} {:<15}".format("Name", "Phone", "Email", "Group"))
    print("-" * 65)
    for elem in list:
        print("{:<10} {:<12} {:<25} {:<15}".format(elem["name"], 
        elem["phone"], elem["email"], elem["group"]))
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    for item in list:
        if name == item["name"]:
            print("Current data:", item)
            new_name = input(f"New name ({item['name']}): ") or item["name"]
            new_phone = input(f"New phone ({item['phone']}): ") or item["phone"]
            new_email = input(f"New email ({item['email']}): ") or item["email"]
            new_group = input(f"New group ({item['group']}): ") or item["group"]
            item["name"] = new_name
            item["phone"] = new_phone
            item["email"] = new_email
            item["group"] = new_group
            list.sort(key=lambda x: x["name"])
            print("Data has been updated")
            return
    print("Element was not found")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete," 
          "P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")
main()
