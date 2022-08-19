T = int(input())
for tc in range(1, T + 1):
    temp = [-1] * 9
    result, i = 1, 1
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행 검사
    for row in arr:
        for num in row:
            temp[num - 1] = i
        if (-1) * i in temp:
            result = 0
            break
        i *= (-1)

    # 열 검사
    re_arr = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            re_arr[j][8 - i] = arr[i][j]

    for row in re_arr:
        for num in row:
            temp[num - 1] = i
        if (-1) * i in temp:
            result = 0
            break
        i *= (-1)

    # 격자 검사
    for n in range(0, 9, 3):
        for m in range(0, 9, 3):
            sum = 0
            for i in range(n, n + 3):
                for j in range(m, m + 3):
                    sum += arr[i][j]
            if sum != 45:
                result = 0
                break

    print('#%d %d' % (tc, result))