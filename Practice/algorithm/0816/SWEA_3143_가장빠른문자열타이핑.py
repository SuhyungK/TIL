T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    la, lb = len(a), len(b)

    i, cnt = 0, la
    while i < la-lb+1:
        if a[i:i+lb] == b:
            i += lb
            cnt -= (lb - 1)
        else:
            i += 1
    
    print('#%d %d'%(tc, cnt))