number = int(input())

for i in range(0,number):
    a =input()
    if a == a[::-1]:
        print("#%d" % (i + 1), end=' ')
        print(1)
    else:
        print("#%d" % (i + 1), end=' ')
        print(0)