temp = 0
numbers = [3, 10, 20, 50,-20,40]
for i in numbers:
    if temp == 0:
        temp = i
    elif i > temp:
        temp = i
    elif i <temp:
        continue

print(temp)