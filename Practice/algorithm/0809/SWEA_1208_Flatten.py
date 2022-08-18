import sys
sys.stdin = open('input.txt')

for test_case in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    maxIdx = minIdx = 0

    # dump 횟수만큼 반복
    while dump != 0:
        # 최대높이 최소높이 찾기
        for i in range(100):
            if box[maxIdx] < box[i]:
                maxIdx = i
            elif box[minIdx] > box[i]:
                minIdx = i

        box[maxIdx] -= 1 # 최대높이 -= 1
        box[minIdx] += 1 # 최소높이 += 1

        # 반복문 끝나고 다시 최대최소 찾아서 차이값 구하기        
        for j in range(100):
            maxIdx = j if box[maxIdx] < box[j] else maxIdx
            minIdx = j if box[minIdx] > box[j] else minIdx

        if box[maxIdx] - box[minIdx] <= 1:
            break

        # 차이가 1보다 작지 않으면 다시 반복
        dump -= 1

    print(f'#{test_case+1} {box[maxIdx]-box[minIdx]}')