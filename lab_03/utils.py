import csv
from lab_03_student import Student, StudentList

filename = "lab_03.csv"

class Utils:
    @staticmethod
    def read_from_file(filename, students: StudentList):
        try:
            with open(filename) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row["name"],
                        row["phone"],
                        row["email"],
                        row["group"]
                    )
                    students.add_student(student)   # тут вже правильно
        except FileNotFoundError:
            print("File not found. Start with empty list.")

    @staticmethod
    def save_to_file(filename, students: StudentList):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["name", "phone", "email", "group"]
            )
            writer.writeheader()
            for student in students.get_all():
                writer.writerow(student.to_dict())
