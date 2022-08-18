T = int(input())

for test_case in range(1, T + 1):
    n, q = map(int, input().split())

    box = [0] * n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            box[j-1] = i

    print(f'#{test_case}',*box)