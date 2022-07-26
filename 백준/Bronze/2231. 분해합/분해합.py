a=input()
b= map(int,a)
#scan = 9*len(list(b))
#int(a)-scan
for i in range(1,int(a)+1):
    result = i + sum(map(int,str(i)))
    if result == int(a):
        print(i)
        break
    if i == int(a):
        print(0)