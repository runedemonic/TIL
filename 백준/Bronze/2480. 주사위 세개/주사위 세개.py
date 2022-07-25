a = map(int, input().split())
a=list(a)
result=[]
for i in a:
    if a.count(i) == 3:
        result.append(10000+i*1000)

    elif a.count(i) == 2:
        result.append(1000+i*100)

    else:
        result.append(max(a)*100)

print(max(result))