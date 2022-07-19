import sys

sys.stdin = open("input.txt", "r")

number = int(input())
for i in range(0,number):
    a,b = map(int, input().split())
    print("#%d" % (i + 1), end=' ')
    print(int(a / b), a % b)