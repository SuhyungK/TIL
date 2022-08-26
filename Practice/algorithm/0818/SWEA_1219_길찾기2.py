import sys
sys.stdin = open('4615.txt')

def dfs(s, g):
    global top
    while 1:
        if s == g:              # 도착
            return 1
        visited[s] = 1          # 방문정보 기록
        for n in node[s]:       # 현재 있는 정점에서 갈 수 있는 곳 확인
            if visited[n] == 0: # 있으면 이동
                visited[n] = 1
                top += 1
                stack[top] = s
                s = n
                break
        else:                   # 없는 경우 : 스택이 비어 있으면 return 0, 스택에 값이 있으면 되돌아가서 다시 확인
            if top > -1:
                s = stack[top]
                top -= 1
            else:
                return 0

for _ in range(10):
    tc, n = map(int, input().split()) # n = 순서쌍의 개수
    arr = list(map(int, input().split()))
    node = [[] for _ in range(100)]
    visited = [0] * 100
    stack = [0] * 100
    top = -1

    for i in range(0, 2*n, 2): # 순서쌍 (i = 정점, i + 1 = 정점에서 갈 수 있는 곳 )
        node[arr[i]].append(arr[i+1])

    print('#%d %d'%(tc, dfs(0, 99)))