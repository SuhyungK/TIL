"""
3
10 50
4 22 1 12 11 36 21 23 3 36
11 50
4 22 1 12 11 6 21 23 3 36 6
10 50
3 2 5 5 1 13 23 17 50 25
"""
# 보석의 모든 조합을 구해서 최대합 찾기
def comb(i, K, s):
    global res
    # 합이 예산을 벗어나는 경우 유효하지 않은 값이므로 return
    if s > M:
        return

    if i == K:
        if s > res:
            res = s
        return
    
    # 모든 조합에는 어떤 보석이 포함되는 경우 / 포함되지 않는 경우가 모두 존재
    comb(i+1, K, s+jew[i])
    comb(i+1, K, s)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    res = 0

    # 수집 대상인 보석만 찾아서 jew 리스트에 추가
    jew = []
    for i in range(N):
        for j in (4, 6, 7, 9, 11):
            if lst[i] % j == 0:
                jew.append(lst[i])
                break

    comb(0, len(jew), 0)
    print(f'#{tc}', res)