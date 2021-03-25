from string import digits
words = "H1e2l3l4o5w6o7r8l9d"
res = words.translate(str.maketrans('', '', digits))
print(res)
