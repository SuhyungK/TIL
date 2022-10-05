"""
안전지역이 될 수 있는 빈 공간(0)의 개수를 전부 센 다음에
그 중에서 공격 가능한 지역들이 발견될 때마다 하나씩 빼주는 방식

3
5
0 1 0 0 0
0 0 2 2 0
0 1 0 0 0
0 2 1 2 0
0 0 0 0 0
5
0 0 0 0 0
0 2 1 2 0
0 1 0 1 0
0 2 1 2 0
0 0 0 0 0
5
0 0 1 0 0
1 2 0 1 0
0 1 2 0 1
1 0 0 2 0
0 1 2 0 1
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tower = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    cnt = 0

    start = []
    for i in range(N):
        for j in range(N):
            # 방어탑에서부터 공격이 가능하기 때문에 방어탑부터 탐색하기 위해서 방어탑의 좌표 저장
            if tower[i][j] == 2:
                start.append((i, j))
            elif not tower[i][j]:
                cnt += 1

    while start:
        si, sj = start.pop()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            # 매번 탐색의 시작좌표는 동일해야 하기때문에 while문이 실행동안 변경되었던 ni, nj 값을 다시 초기값으로 갱신
            ni, nj = si, sj 
            # 좌표값이 유효하고 공격 가능한 지역인 경우 탐색
            while -1 < ni+di < N and -1 < nj+dj < N and tower[ni+di][nj+dj] == 0:
                ni, nj = ni + di, nj + dj
                # 다만, 방문하지 않은 지역인 경우에만 카운팅 -> 방문처리
                if visit[ni][nj] == 0:
                    cnt -= 1
                    visit[ni][nj] = 1

    print(f'#{tc}', cnt)
