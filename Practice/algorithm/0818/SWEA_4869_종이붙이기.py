import sys
sys.stdin = open('4615.txt')

def dp(n):
    if n == 2 : return 3
    elif n > 2:
        return dp(n-1) + 2 * dp(n-2)
    return n

T = int(input())
for tc in range(1, T+1):
    n = int(input()) // 10
    print(f'#{tc} {dp(n)}')


