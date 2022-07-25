number = int(input())
for i in range(0,number):
    a,b = map(int, input().split())
    print("Case #%d:" % (i + 1), end=' ')
    print(f'{a} + {b} = {a+b}')