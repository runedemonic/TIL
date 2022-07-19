number = int(input())
list=[]
for i in range(0,number):
    lst = map(int, input().split())
    a= round(sum(lst)/10)
    list.append(a)
    print("#%d" % (i + 1), end=' ')
    print(list[i])




