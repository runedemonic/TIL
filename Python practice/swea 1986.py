number = int(input())
for i in range(0,number):
    a= int(input())
    result = 0
    for n in range(1,a+1):
        if n%2 != 0:
            result+=n
        else:
            result-=n
    print("#%d" % (i + 1), end=' ')
    print(result)