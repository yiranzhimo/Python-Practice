import re
words = input("请输入 words:")
letters_result = ' '.join(re.findall(r'[A-Za-z]', words)).split()
list(letters_result)
digit_result = ' '.join(re.findall(r'[0-9]+', words)).split()
list(digit_result)
print("LETTERS ",len(letters_result))
print("DIGITS ",len(digit_result))