queue = []
my_chu = 20
next_person = 1

queue.append([1, 1]) # 1번이 줄을 선 상태

while 1:
    # 1번이 줄을 서서 사탕 1개를 가져감
    idx, num = queue.pop(0) # idx번째 사람이 num개 가져감
    my_chu -= num
    # 1번이 다시 줄을 선다
    queue.append([idx, num+1])
    next_person += 1
    # 2번이 줄을 서게 됨
    queue.append([next_person, 1])

    input()
    print(f'줄에 서 있는 사람 : {len(queue)}')
    print(f'현재 1인당 나눠주는 사탕 : {my_chu}')
    print(f'현재 남아있는 사탕 : {my_chu}')

    if not num:
        break

