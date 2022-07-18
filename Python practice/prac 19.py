number= int(input())
count = 1
while True:
    number //= 10
    count += 1
    if number // 10 <1:
        break
print(count)