number = int(input())

for ele in range(number):
    i, s = input().split()
    i = int(i)
    s = list(s)
    s.pop(i-1)
    print("".join(s))