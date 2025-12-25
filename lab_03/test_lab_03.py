import pytest
from lab_03_student import Student, StudentList
from utils import Utils

def test_add_student():
    lst = StudentList()
    result = lst.add_student(Student("Jon", "123", "jon@mail.com", "kb-221"))
    assert result is True
    assert len(lst.get_all()) == 1
    assert lst.get_all()[0].name == "Jon"

def test_delete_student():
    lst = StudentList()
    lst.add_student(Student("Bob", "1996633448", "bob@ukr.net", "kb-251"))
    result = lst.delete_student("Bob")
    assert result is True
    assert len(lst.get_all()) == 0

def test_update_student():
    lst = StudentList()
    lst.add_student(Student("Zak", "111", "zak@mail.com", "kb-241"))
    result = lst.update_student(
        "Zak",
        Student("Zak", "777", "zak@mail.com", "kb-241")
    )
    assert result is True
    assert len(lst.get_all()) == 1
    assert lst.get_all()[0].phone == "777"
