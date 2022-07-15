stlist = list()

for i in range(24):
    stlist.append(0)
    
num = int(input())
numlist = input().split()

for i in range(num):
    stlist[int(numlist[i])] += 1
    
for i in range(1, len(stlist)):
    print(stlist[i], end=' ')

