import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    data = int(input())
    cnt = [0] * 10

    for _ in range(n):
        cnt[data%10] += 1
        data //= 10

    max = idx = 0
    for i in range(10):
        if max < cnt[i]:
            max = cnt[i] 
            idx = i
    
    print(f'#{test_case} {idx} {max}')
        

    