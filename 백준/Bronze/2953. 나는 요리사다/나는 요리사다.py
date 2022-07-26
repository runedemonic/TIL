result =[]
for i in range(5):
    b= list(map(int,input().split()))
    result.append(sum(list(b)))

print(result.index(max(result))+1)
print(max(result))
