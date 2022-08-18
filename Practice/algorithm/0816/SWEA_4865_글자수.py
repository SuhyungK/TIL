T = int(input())

for tc in range(1, T+1):
    t = list(input())
    t = list(set(t))
    s = input()

    ti = si = cnt = maxV = 0
    while ti < len(t):
        if t[ti] == s[si]:
            cnt += 1

        si += 1
        if si == len(s):
            if maxV < cnt:
                maxV = cnt
            cnt = si = 0
            ti += 1

    print('#%d %d'%(tc, maxV))