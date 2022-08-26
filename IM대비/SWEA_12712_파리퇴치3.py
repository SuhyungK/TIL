T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]


    for i in range(n):
        for j in range(n):
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = i + dx, j + dy
                for _ in range(m):

    print(f'#%d'%tc)
    print(arr)