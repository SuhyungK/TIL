T = int(input())

for tc in range(1, T+1):
    cnt = 0
    s1 = input()
    s2 = input()
    i = j = 0
    print('#%d' %tc, end=' ')
    while i < len(s2):
        if s1[j] == s2[i]:
            cnt += 1
        else:
            cnt = 0
            i -= j
            j = -1
        i += 1
        j += 1

        if cnt == len(s1):
            print(1)
            break
    if cnt < len(s1):
        print(0)