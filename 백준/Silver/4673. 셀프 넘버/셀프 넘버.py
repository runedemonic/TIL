numbers=set()
all=set(range(1,10001))

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    numbers.add(i)

result = sorted(all-numbers)
for i in result:
    print(i)
