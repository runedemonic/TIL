number = int(input())
w_list=[]
rank = 1
for i in range(0,number):
    a= map(int,input().split())
    w_list.append(list(a))
for i in range(len(w_list)):
    for j in range(len(w_list)):
        if w_list[i][0] < w_list[j][0] and w_list[i][1] < w_list[j][1]:
            rank += 1
    print(rank,end=' ')
    rank = 1