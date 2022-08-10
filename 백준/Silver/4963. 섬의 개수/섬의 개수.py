import sys
sys.setrecursionlimit(10000)

dX = [1, 1, 0, -1, -1, -1, 0, 1]
dY = [0, 1, 1, 1, 0, -1, -1, -1]


def DFS(x, y, mapList, visitedList):
    visitedList[y][x] = True

    for i in range(8):
        nX = x + dX[i]
        nY = y + dY[i]

        if 0 <= nX < N and 0 <= nY < M:
            if visitedList[nY][nX] == False and mapList[nY][nX] == 1:
                DFS(nX, nY, mapList, visitedList)

while True:
    N,M = map(int,input().split())
    if N== 0 and M == 0:
        break
    wmap=[]
    for i in range(M):
        wmap.append(list(map(int, input().split())))
    visitedList = [list(False for _ in range(N)) for _ in range(M)]
    count = 0

    for i in range(M):
        for j in range(N):
            if visitedList[i][j] == False and wmap[i][j] == 1:
                DFS(j, i, wmap, visitedList)
                count += 1

    print(count)
