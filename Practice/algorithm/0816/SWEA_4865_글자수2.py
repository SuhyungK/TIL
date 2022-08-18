T = int(input())

for tc in range(1, T+1):
    s1 = input()
    s2 = input()

    str_dict = {}
    for s in s2:
        if s not in str_dict:
            str_dict[s] = 1
        else:
            str_dict[s] = str_dict[s] + 1

    maxV = 0    
    for s in s1:
        cnt = str_dict.get(s)
        if maxV < cnt:
            maxV = cnt
    print(f'#{tc} {maxV}')