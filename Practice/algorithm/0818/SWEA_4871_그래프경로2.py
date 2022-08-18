import sys
sys.stdin = open('input.txt')

def dfs(s, g):
    while 1:
        if s == g:
            return 1
        visited[s] = 1 # s에 방문
        for n in node[s]:
            if visited[n] == 0:
                stack.append(s)
                s = n
                visited[s] = 1
                break
        else:
            if stack: s = stack.pop()
            else:
                return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[[] for _ in range(V+1)] for _ in range(V+1)]
    visited = [0] * (V+1)
    stack = []

    # 인접 행렬 리스트로 풀기
    for _ in range(E):
        v, e = map(int, input().split())
        node[v].append(e)
    s, g = map(int, input().split()) # 찾으려는 출발,도착 노드
    print('#%d %d'%(tc, dfs(s, g)))