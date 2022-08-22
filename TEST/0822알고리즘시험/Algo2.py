# 3*3 배열과 패턴 배열을 하나씩 확인하는 함수
def checkPattern(arr, pattern):
    for row in range(3):
        for col in range(3):
            if arr[row][col] != pattern[row][col]:
                return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N * N 배열
    data = [list(input().split()) for _ in range(N)]
    pattern = [list(input().split()) for _ in range(3)]

    result = 0
    for i in range(N-2):        # 주어진 배열에서 3*3배열의 기준이 되는 지점
        for j in range(N-2):    # 가장 왼쪽, 위의 좌표값 범위 지정
            temp = []
            for row in data[i:i+3]: # 주어진 배열에서 3*3 배열 새로 생성
                temp.append(row[j:j+3])
            result += checkPattern(temp, pattern) # 모든 값이 일치하면 return 1 이므로 count +1

    print('#%d %d'%(tc, result))
