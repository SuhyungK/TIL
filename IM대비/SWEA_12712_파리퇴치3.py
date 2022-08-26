T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0

    for i in range(n):
        for j in range(n):
            sumV = arr[i][j]
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + dx, j + dy
                for _ in range(m-1):
                    if 0 <= ni < n and 0 <= nj < n : sumV += arr[ni][nj]
                    else: break
                if maxV < sumV: maxV = sumV
            sumV = arr[i][j]
            for dx, dy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                for _ in range(m-1):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n: sumV += arr[nx][ny]
                if maxV < sumV: maxV = sumV
    print(f'#%d'%tc)
    print(maxV)