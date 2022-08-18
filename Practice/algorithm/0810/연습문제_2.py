import sys
sys.stdin = open('input2.txt')

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    
    for i in range(1, 1<<len(arr)):
        s = 0
        for j in range(len(arr)):
            if i & (1<<j):
                s += arr[j]
        if s == 0:
            print(f'#{test_case} 1')
            break
    else:
        print(f'#{test_case} 0')

"""
#1 0
#2 1
#3 1
"""