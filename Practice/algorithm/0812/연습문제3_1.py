import sys
sys.stdin = open('input3.txt')

def brute_force(t, p):
    ti = 0 # target index
    pi = 0 # pattern index
    cnt = 0 # count

    while ti < len(t):
        # 일치하지 않는 경우
        if t[ti] != p[pi]:
            ti -= pi
            pi = -1
        pi += 1
        ti += 1
        # 일치하는 경우 count
        if pi == len(p):
            cnt += 1
            pi = 0
    return cnt

for _ in range(10):
    tc = input()
    p = input()
    t = input()
    
    print('#%s %d' %(tc, brute_force(t, p)))
