from collections import defaultdict


def dfs(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()

    ##시작 노드 설정해주기
    need_visited.append(start_node)

    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()

        ##만약 방문한 리스트에 없다면
        if node not in visited:
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited

All_c = int(input())
connect_c=int(input())
net = defaultdict(list)
for _ in range(connect_c):
    k,v = map(int,input().split())
    net[k].append(v)
    net[v].append(k)
print(len(dfs(net,1))-1)