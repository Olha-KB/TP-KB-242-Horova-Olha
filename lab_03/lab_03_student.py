class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Group: {self.group}"

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "group": self.group
        }

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        insert_position = 0
        for s in self.students:
            if student.name > s.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        return True

    def delete_student(self, name: str):
        for i, student in enumerate(self.students):
            if student.name == name:
                del self.students[i]
                return True
        return False

    def update_student(self, name: str, new_student: Student):
        for i, student in enumerate(self.students):
            if student.name == name:
                self.students[i] = new_student
                return True
        return False

    def print_all(self):
        if not self.students:
            print("No students in the list.")
            return
        for student in self.students:
            print(student)
    def get_all(self):
        return self.students
