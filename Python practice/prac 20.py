number= int(input())
count = 0
while number:
    a=number % 10
    count += a
    number //= 10

print(count)