def bfs(v, N, t): # v: 시작, N : 마지막 정점, t : 찾는 정점
    visited = [0] * N
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t: # 이 탐색에서 하려는 일 : visit(v)
            return visited[99] # 경로의 총 길이 출력 : 몇 개의 정점을 거쳐왔는지
                               # visited[w] = visited[v] + 1 로 표시해왔기 때문에
        for w in adjlst[v]:
            if visited[w] == 0:
                q.append(w)
                # A : 1 / B C D : 2 / E F , G H I : 3
                # 정점까지의 최단 거리 등 구할 때 이런 방식으로 함
                visited[w] = visited[v] + 1

    return '발견 실패'
for _ in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjlst = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjlst[a].append(b)

    bfs(0, 99, 99) # 시작, 마지막 정점, 정점의 개수

# BFS 특징 : 출발점이 2개 이상이어도 가능하다