#2) perform some test for strip, capitalize, title, upper, lower
def test_string_methods():
    original = "hello worLd!          "

    print("Original:", repr(original))
    print("strip():", repr(original.strip()))
    print("capitalize():", original.capitalize())
    print("title():", original.title())
    print("upper():", original.upper())
    print("lower():", original.lower())

test_string_methods()