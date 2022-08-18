import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    box = list(map(int, input().split()))
    fall = [(n-1) - i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if box[i] <= box[j]:
                fall[i] -= 1
    
    # 최대값
    for i in range(len(fall)-1):
        if fall[i] > fall[i+1]:
            fall[i], fall[i+1] = fall[i+1], fall[i]
    
    print(f'#{test_case} {fall[len(fall)-1]}')
