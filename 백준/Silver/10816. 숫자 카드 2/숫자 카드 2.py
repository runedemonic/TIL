from collections import Counter

n= int(input())
n1=sorted(map(int,input().split(' ')))
m=int(input())
m1=list(map(int,input().split(' ')))
count = Counter(n1)
cnt = 0

for i in m1:
    print(count[i],end=' ')

