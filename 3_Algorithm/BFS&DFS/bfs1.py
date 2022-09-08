"""
1 - 2 3 4
2 - 5 6
4 - 7 8 9

1 2
1 3
1 4
2 5
2 6
4 7
4 8
4 9
"""
def bfs(v, N): # v : 시작 정점 / N : 마지막 정점
    visited = [0] * (N + 1)     # visited 생성
    queue = []                  # 큐 생성
    queue.append(v)             # 시작점 enQueue
    visited[v] = 1              # 시작점 처리 표시

    # 큐가 비어있지 않으면
    while queue:
        t = queue.pop(0)        # deQueue
        # visit(t)              # 처리할 일(ex. print)
        print(t)
        for w in adjlst[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
    pass

v, e = map(int, input().split())
adjlst = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    # 양쪽 연결
    adjlst[a].append(b)
    adjlst[b].append(a)

bfs(0, v)
print(adjlst)