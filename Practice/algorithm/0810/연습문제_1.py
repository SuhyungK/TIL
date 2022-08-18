import sys
sys.stdin = open('input1.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)] # 초기화
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    s = 0 

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += abs(arr[ni][nj] - arr[i][j])
    print(f'#{test_case+1} {s}')
            
