import csv
from sys import argv

def add_student(student_list, name, phone, email, group):
    new_item = {"name": name, "phone": phone, "email": email, "group": group}
    insert_pos = 0
    for s in student_list:
        if name > s["name"]:
            insert_pos += 1
        else:
            break

    student_list.insert(insert_pos, new_item)
    return True

def delete_student(student_list, name):
    for i, s in enumerate(student_list):
        if s["name"] == name:
            del student_list[i]
            return True
    return False


def update_student(student_list, old_name, new_name, phone, email, group):
    
    for i, s in enumerate(student_list):
        if s["name"] == old_name:
            del student_list[i]
            add_student(student_list, new_name, phone, email, group)
            return True
    return False


def print_all(student_list):
    for s in student_list:
        print(
            f"name: {s['name']}, phone: {s['phone']}, "
            f"email: {s['email']}, group: {s['group']}" )

def add_element(student_list):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    group = input("Group: ")
    add_student(student_list, name, phone, email, group)
    print("Student added")


def delete_element(student_list):
    name = input("Name to delete: ")
    if delete_student(student_list, name):
        print("Deleted")
    else:
        print("Student not found")


def update_element(student_list):
    old_name = input("Name to update: ")

    for s in student_list:
        if s["name"] == old_name:
            print("Enter new data:")
            new_name = input("New name: ")
            phone = input("New phone: ")
            email = input("New email: ")
            group = input("New group: ")

            update_student(
                student_list, old_name, new_name, phone, email, group
            )
            print("Updated")
            return

    print("Student not found")

filename = "lab_2.csv"

def read_from_file(student_list):
    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student_list.append({
                    "name": row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "group": row["group"]
                })
    except FileNotFoundError:
        print(f"File '{filename}' not found. Start with empty list.")


def save_to_file(student_list):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "group"])
        writer.writeheader()
        for s in student_list:
            writer.writerow({
                "name": s["name"],
                "phone": s["phone"],
                "email": s["email"],
                "group": s["group"]
            })


def main():
    if len(argv) < 2:
        print(f"Usage: python lab_02.py lab_2.csv")
        return

    students = []
    read_from_file(students)

    while True:
        choice = input(
            "\n[C create, U update, D delete, P print, X exit]: "
        ).upper()

        match choice:
            case "C":
                add_element(students)
            case "U":
                update_element(students)
            case "D":
                delete_element(students)
            case "P":
                print_all(students)
            case "X":
                save_to_file(students)
                print("Saved. Exit.")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
