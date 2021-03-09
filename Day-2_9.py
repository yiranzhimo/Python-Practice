lines=[]
while True:
    try:
        lines.append(input())
    except:
        break

for i in lines:
    print(i.upper())
