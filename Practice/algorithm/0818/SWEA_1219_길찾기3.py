def dfs(s, g):
    visited[s] = 1  # 방문한 곳 확인
    while 1:
        for n in node[s]: # 정점에서 갈 수 있는 곳 확인
            if visited[n] == 0: # 있으면 현재 지점 기록 후 이동
                if n == g:      # 갈 수 있는 지점이 도착점이면 종료
                    return 1
                stack.append(s)
                s = n
                visited[s] = 1
                break
        else:                   # 없는 경우 : 스택이 비어 있으면 return 0, 스택에 값이 있으면 되돌아가서 다시 확인
            if stack: s = stack.pop()
            else:
                return 0

for _ in range(10):
    tc, n = map(int, input().split()) # n = 순서쌍의 개수
    arr = list(map(int, input().split()))
    node = [[] for _ in range(100)]
    visited = [0] * 100
    stack = []
    for i in range(0, 2*n, 2): # 순서쌍 (i = 정점, i + 1 = 정점에서 갈 수 있는 곳 )
        node[arr[i]].append(arr[i+1])

    print('#%d %d'%(tc, dfs(0, 99)))