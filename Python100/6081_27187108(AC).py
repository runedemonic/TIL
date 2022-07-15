a = input()
n =0
if a == 'A':
    n = 10
elif a == 'B':
    n = 11
elif a == 'C':
    n =12
elif a =='D':
    n = 13
elif a =='E':
    n= 14
else:
    n=15

for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
