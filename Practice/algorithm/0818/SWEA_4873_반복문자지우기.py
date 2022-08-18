import sys
sys.stdin = open('input.txt')

def length(arr):          # 0 제외한 길이 구하기
    cnt = 0
    for a in arr:
        if a != 0:
            cnt += 1
    return cnt

t = int(input())
for tc in range(1, t+1):
    string = list(input())
    temp = [0] * length(string)
    top = 0

    temp[0] = string[0]
    for s in string[1:]:
        if temp[top] == s: # 같으면 pop
            temp.pop(top)
            top -= 1
        else:
            top += 1
            temp[top] = s # 다르면 push

    print('#%d %d'%(tc, length(temp)))
