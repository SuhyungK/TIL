# import sys
# sys.stdin = open('input.txt')

def bfs(N):
    # 행과 열로 이루어져있기 때문에 visited도 행x열
    visited = [[0] * N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni <N and 0 <= nj <N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = stj = -1

    print(f'#{tc} {bfs(N)}')

# 탐색
# 빠짐없이 중복없이 - DFS, BFS
# 최단거리 - DFS, BFS
# 경로의 수 - DFS
# 확산, 출발이 여러 곳 - BFS