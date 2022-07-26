a,b = map(int, input().split())
GCD = 0
tmp =a
tmp1=b
while True:
    r = tmp % tmp1
    if r == 0:
        GCD = tmp1
        print(GCD)
        break
    else:
        tmp = tmp1
        tmp1 = r
LCM = (a*b)//GCD
print(LCM)
