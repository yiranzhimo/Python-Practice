s = input()
num, char = 0, 0 
for i in s:
    if i.isdigit():
        num = num + 1  
    elif i.isalpha():    
        char = char + 1
print("Digit - ",num)
print("Letter - ",char)
