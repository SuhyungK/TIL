import sys
sys.stdin = open('input.txt')

def length(arr):
    cnt = 1
    for a in arr:
        cnt += 1
    return cnt

t = int(input())
for tc in range(1, t+1):
    arr = input()
    stack = [0] * length(arr)
    top = -1

    for a in arr:
        if stack[top] != a:
            top += 1
            stack[top] = a
        else:
            top -= 1

    print('#%d %d'%(tc, top+1))
