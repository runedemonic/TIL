n=int(input())
for _ in range(n):
    m,n = map(int,input().split())

    cor = [[] for _ in range(n)]
    # 열로 박스 위치 저장
    for i in range(m):
        box = list(input().split())
        for j in range(n):
            cor[j].append(box[j])

    move = 0
    for i in range(n):
        boxcnt = cor[i].count(1)
        bottom = m-1

        for j in range(m-1,-1,-1):
            if cor[i][j] == '1':
                move += bottom - j
                bottom -= 1
    # for i in cor:
    #     for j in i:
    #         print(j, end=" ")
    #     print()
    print(move)