nlist=[]
score=[]
compare=[]
for i in range(10):
    m = int(input())
    nlist.append(m)
    score.append(sum(nlist))
    compare.append(abs(100-sum(nlist)))


min_list = list(filter(lambda x: compare[x]==min(compare), range(len(compare))))

print(score[max(min_list)])
