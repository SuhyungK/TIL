import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    n, k = map(int, input().split())
    arr = [input().split('0') for _ in range(n)]
    for row in arr:
        for r in row:
            print(r.strip())

    # print('#%d %d'%(tc))
