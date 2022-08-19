import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    _ = input()
    table = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0

    for i in range(100):
        temp = False
        for j in range(100):
            if table[j][i] == 1:
                temp = True
            elif table[j][i] == 2 and temp == True:
                cnt += 1
                temp = False

    print('#%d %d'%(tc, cnt))