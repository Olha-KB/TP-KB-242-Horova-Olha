import pytest
from lab_02 import add_student, delete_student, update_student_logic

def test_add_student():
    test_list = []
    add_student(test_list, "Jon", "096...", "jon@mail.com", "kb-221")
    assert len(test_list) == 1
    assert test_list[0]["name"] == "Jon"

def test_delete_student():
    test_list = [{"name": "Bob", "phone": "0687458692", "email": "bob@gmail.com", "group": "kb-241"}]
    result = delete_student(test_list, "Bob")
    assert result is True
    assert len(test_list) == 0

def test_update_student_logic():
    # Початкові дані
    test_list = [{"name": "Zak", "phone": "06874221", "email": "zak@gmail.com", "group": "kb=241"}]
    
    # Оновлюємо Боба
    result = update_student_logic(test_list, "Zak", "Zak", "777", "zak@gmail.com", "kb-241")
    
    assert result is True
    assert len(test_list) == 1
    assert test_list[0]["name"] == "Zak"
    assert test_list[0]["phone"] == "777"
