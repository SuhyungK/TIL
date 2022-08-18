import sys
sys.stdin = open('input.txt')

def memo(n):
    pass
    if n not in memory:
        arr = []
        for i in range(1, n - 1):
            temp = memo(n - 1)[i] + memo(n - 1)[i - 1]
            arr.append(temp)
        arr.insert(0, 1)
        arr.append(1)

        memory[n] = arr
    return memory[n]


memory = {1: [1], 2: [1, 1]}
memo(10)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    print('#%d' % tc)
    for i in range(1, n + 1):
        print(*memory[i])


# 출처 : https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/pascal%20triangle%20with%20memoization.py#L74