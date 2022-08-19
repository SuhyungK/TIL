import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        len1 = len2 = 0
        for j in range(n):
            if arr[i][j]:
                len1 += 1
            if arr[j][i]:
                len2 += 1
            # 값이 마지막이거나 0이면 검사
            if j == (n - 1) or arr[i][j] == 0:
                if len1 == k:
                    cnt += 1
                len1 = 0
            if j == (n - 1) or arr[j][i] == 0:
                if len2 == k:
                    cnt += 1
                len2 = 0

    print('#%d %d'%(tc,cnt))