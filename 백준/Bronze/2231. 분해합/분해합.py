a=input()

b= list(map(int,a))

scan = 9*len(b)

start = int(a)-scan

for i in range(max(1,start),int(a)+1):
    result = i + sum(map(int,str(i)))
    if result == int(a):
        print(i)
        break
    if i == int(a):
        print(0)