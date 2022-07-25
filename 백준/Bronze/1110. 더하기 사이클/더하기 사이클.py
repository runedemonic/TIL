n = int(input())
cycle = 1
tmp = n
while True:
    a = tmp//10
    b = tmp %10
    c = (a +b)%10
    tmp = b*10+c
    if tmp == n:
        print(cycle)
        break
    else:
        cycle+=1