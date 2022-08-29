# DFS 최단경로
# 가능한 모든 경로를 돌아봐야 함
# 경로의 수를 알 수 있음
# 최단 경로가 몇 개나 되는가?

# BFS 최단경로
#
# import sys
# sys.stdin = open('input.txt')

def dfs(i, j, N):
    global answer
    # 3을 만나면 return
    if maze[i][j] == 3:
        answer += 1
        return
    else:
        # 내가 지나온 경로로 다시 이 경로를 방문하는 건 막겠다
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            # 벽으로 둘러싸여 있어서 나가게 될 확률이 없음
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni, nj, N)
        # 한 번 지나갔던 경로를 다른 정점을 통해서 들어 왔을 때
        # 지나갈 수 있도록 하기 위해서 경로를 지나갔던 정보를 지워서
        # 다른 경로로 들어왔을 때는 들어오는 것 허용
        # * 다른 방향에서 들어오는 것은 허용하겠다 *
        visited[i][j] = 0
    # if 문이 종료되면 자동으로 return
    return 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = stj = -1

    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    answer = 0  # 경로의 횟수
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {dfs(sti, stj, N)}')