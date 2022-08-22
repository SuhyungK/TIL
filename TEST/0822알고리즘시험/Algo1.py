T = int(input())
for tc in range(1, T+1):
    N = int(input())
    xy = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]
    row, col = xy[2] - xy[0] + 1, xy[3] - xy[1] + 1 # 평탄화 영역의 row : 행의 개수 / col : 열의 개수
    num = row * col # 총 칸의 개수

    sumV = 0
    arr = []
    for i in range(row):
        for j in range(col):
            arr.append(data[xy[0]+ i][xy[1]+ j]) # 2차원 배열을 1차원 배열로 변경
            sumV += data[xy[0]+ i][xy[1]+ j]     # 평단화 영역 높이 값의 총합

    avgV = sumV//num # 평균값 = (평탄화 영역의 높이 값의 총합) // (총 칸의 개수)
    idx, cnt = 0, 0
    while idx < num: # 총 칸의 개수 = 배열의 길이
        # 평균이 되는 값보다 크거나 작을 경우 차이 만큼 카운트 되므로 그만큼 cnt에 추가
        if arr[idx] < avgV:
            cnt += avgV - arr[idx]
        elif arr[idx] > avgV:
            cnt += arr[idx] - avgV
        idx += 1

    print('#%d %d'%(tc, cnt))