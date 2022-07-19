number = int(input())
for i in range(0,number):
    a,b = map(int, input().split())
    print("#%d" % (i + 1), end=' ')
    if a > b:
        print('>')
    elif a==b:
        print('=')
    elif a < b:
        print('<')