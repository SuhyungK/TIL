import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    _ = input()
    table = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0

    # 배열 회전, N극 왼쪽 S극 오른쪽
    arr = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            arr[99-j][i] = table[i][j]

    # 하나씩 순회하면서 1 다음에 2가 나오면 교착 상태 count +1
    # 2 가 나왔을 때 이전에 나온 숫자가 1이었는지를 확인할 수 있는 변수 temp
    for line in arr:
        temp = False
        for mag in line:
            if mag == 1:
                temp = True
            elif mag == 2 and temp == True:
                cnt += 1
                temp = False

    print('#%d %d'%(tc, cnt))