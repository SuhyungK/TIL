import sys
sys.stdin = open('4615.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[-1] * n for _ in range(n)]

    mid = n // 2
    board[mid][mid] = board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = board[mid][mid - 1] = 1

    cnt = [2, 2]
    dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    for _ in range(m):
        i, j, ot = map(int, input().split())
        board[i - 1][j - 1] = ot
        cnt[ot - 1] += 1
        for dx, dy in dxy:
            nx = (i - 1) + dx
            ny = (j - 1) + dy
            if 0 <= nx < n and 0 <= ny < n and abs(ot - board[nx][ny]) == 1:
                cntV = 1
                for _ in range(n):
                    nx += dx
                    ny += dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if abs(ot - board[nx][ny]) == 1:
                            cntV += 1
                        elif board[nx][ny] == ot:
                            cnt[ot - 1] += cntV
                            cnt[ot - 2] -= cntV
                            dx *= (-1)
                            dy *= (-1)
                            while 0 <= nx + dx < n and 0 <= ny + dy < n and board[nx + dx][ny + dy] != ot:
                                nx += dx
                                ny += dy
                                board[nx][ny] = ot
                            break
                        else: break
                    else: break
    print(f'#{tc}', *cnt)