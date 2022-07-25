n = int(input())
count =99

if n<100:
    count =n
else:
    for i in range(100, n+1):
        a= map(int,str(i))
        a=list(a)
        if a[2] -a[1] == a[1] - a[0]:
            count+=1
print(count)