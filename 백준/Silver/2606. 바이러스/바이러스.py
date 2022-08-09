from collections import defaultdict

def dfs(graph, start, visited=[]):
    ## 데이터를 추가하는 명령어 / 재귀가 이루어짐
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

All_c = int(input())
connect_c=int(input())
net = defaultdict(list)
for _ in range(connect_c):
    k,v = map(int,input().split())
    net[k].append(v)
    net[v].append(k)
print(len(dfs(net,1))-1)
