a=int(input())
b=int(input())
c=int(input())
tmp=map(int,str(a*b*c))
list1 = list(tmp)
for i in range(0,10):
    print(list(list1).count(i))