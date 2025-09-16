#1) revert the string "abcdefg123" with static len = 10 to "321gfedcba"
text = input("Введи текст: ")
fixed_len = 10
result = text[:fixed_len ][::-1]
print(result) 
