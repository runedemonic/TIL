number = int(input())

save=[]
for i in range(0,number):
    a= int(input())
    a1 = a
    while True:
        tmplist=list(map(int, str(a1)))
        save.extend(tmplist)
        result=list(set(save))
        a1 += a

        if len(result) == 10:
            print("#%d" % (i + 1), end=' ')
            print(a1-a)
            count = 0
            save=[]
            break
