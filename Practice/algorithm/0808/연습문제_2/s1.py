import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    cnt = [0] * 10
    trip, run = 0, 0
    card = int(input())

    for i in range(6):
        cnt[card%10] += 1
        card //= 10

    # triplet
    i = 0
    while i < 10:
        if cnt[i] >= 3:
            cnt[i] -= 3
            trip += 1
            continue
        if i <= 7:
            # 남아 있는 값이 run 이려면 (1,1,1) or (2,2,2)
            if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
                cnt[i] -= 1
                cnt[i+1] -= 1
                cnt[i+2] -= 1
                run += 1
                continue
        i += 1

    if trip + run == 2: print(f'#{test_case} 1')
    else: print(f'#{test_case} 0')