T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0

    for i in range(n):
        for j in range(n):
            sumV = 0
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                for _ in range(m):
                    if 0 <= nx < n and 0 <= nx < n : sumV += arr[nx][ny]
                    else: break
                if maxV < sumV: maxV = sumV
            sumV = 0
            for dx, dy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                for _ in range(m):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= nx < n: sumV += arr[nx][ny]
                if maxV < sumV: maxV = sumV
    print(f'#%d'%tc)
    print(maxV)