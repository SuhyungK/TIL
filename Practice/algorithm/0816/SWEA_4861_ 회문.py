T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print('#%d '%tc, end='')
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                temp = arr[i][j:j+M]
                print(temp)

    for j in range(N):
        temp = ''
        for i in range(N):
            temp += arr[i][j]

        for k in range(N-M+1):
            if temp[k:k+M] == temp[k:k+M][::-1]:
                print(temp[k:k+M])