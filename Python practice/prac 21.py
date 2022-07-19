number= int(input())
count = []
lenth = 0
while number:
    a=number % 10
    count.append(a)
    number //= 10
    lenth += 1

for i in range(0,len(count)):
    lenth -= 1
    count[i] *= 10**lenth
print(sum(count))
