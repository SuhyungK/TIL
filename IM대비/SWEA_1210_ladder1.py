import sys
sys.stdin = open('1210.txt')

for _ in range(10):
    tc = input()
    data = [list(map(int, input().split())) for _ in range(100)]

    for s in range(100):
        if data[99][s] == 1:
            pass

    print('#%s' %tc)