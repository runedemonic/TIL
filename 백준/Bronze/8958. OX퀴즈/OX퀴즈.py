number = int(input())
for i in range(0,number):
    result = 0
    a=input().split('X')
    for i in range(0,len(a)):
        score = 1
        plus = a[i].count('O')
        for i in range(0,plus):
               result+=score
               score+=1
    print(result)