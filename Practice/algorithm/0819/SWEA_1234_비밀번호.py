import sys
sys.stdin = open('input.txt')

tc = 0
while tc < 10:
    n, password = input().split()
    stack = [-1] * 100              # 초기값을 0으로 하면 비밀번호의 숫자와 비교할 때 헷갈릴 수 있어서 -1로 초기화
    top = -1

    for pwd in password:
        if stack[top] != pwd:
            top += 1
            stack[top] = pwd
        else:
            top -= 1

    tc += 1
    # stack의 전체값이 아니라 top이 가리키고 있는 곳 까지만 필요하기 때문에
    print('#%d %s' % (tc,''.join(stack[:top+1])))