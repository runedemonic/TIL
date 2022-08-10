import sys
sys.setrecursionlimit(10000)

def dfs(start):
    visited[start] = True
    for i in net[start]:
        if not visited[i]:
            dfs(i)

All_c,connect_c =map(int,sys.stdin.readline().split())

net = [[] for _ in range(All_c + 1)]

visited = [False] * (All_c+1)

C_cnt = 0

for _ in range(connect_c):
    k,v = map(int,sys.stdin.readline().split())
    net[k].append(v)
    net[v].append(k)

for i in range(1,All_c+1):
    if not visited[i]:
        dfs(i)
        C_cnt += 1

print(C_cnt)
