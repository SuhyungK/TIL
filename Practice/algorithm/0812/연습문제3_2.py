def brute_force(t, p):
    ti = 0 # target index
    pi = 0 # pattern index
    cnt = 0 # count
 
    while ti < len(t):
        # 문자열이 일치할 경우
        if t[ti] == p[pi]:
            pi += 1
            ti += 1
        # 문자열이 일치하지 않는 경우
        else:
            ti = ti - pi + 1
            pi = 0
        if pi == len(p):
            cnt += 1
            pi = 0
    return cnt
 
for _ in range(10):
    tc = input()
    p = input()
    t = input()
     
    print('#%s %d' %(tc, brute_force(t, p)))