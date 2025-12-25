import sys
from lab_03_student import Student, StudentList
from utils import Utils

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python main.py lab_03.csv")
        return

    filename = sys.argv[1]
    students = StudentList()
    Utils.read_from_file(filename, students)

    while True:
        choice = input("\n[C create, U update, D delete, P print, X exit]: ").upper()

        match choice:
            case "C":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                group = input("Group: ")
                new_student = Student(name, phone, email, group)
                students.add_student(new_student)
            case "U":
                old_name = input("Enter current name to update: ")
                new_name = input("Enter new name: ")
                phone = input("New phone: ")
                email = input("New email: ")
                group = input("New group: ")
                updated_student = Student(new_name, phone, email, group)
                if not students.update_student(old_name, updated_student):
                    print("Student not found.")
            case "D":
                name = input("Enter name to delete: ")
                if not students.delete_student(name):
                    print("Student not found.")
            case "P":
                students.print_all()
            case "X":
                Utils.save_to_file(filename, students)
                print("Saved. Exit.")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
    