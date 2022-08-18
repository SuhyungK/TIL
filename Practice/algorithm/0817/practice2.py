import sys
sys.stdin = open('practice2.txt')

t = int(input())
for tc in range(1, t+1):
    bracket = list(input())
    temp = []

    top = -1
    for b in bracket:
        if b == '(':
            top += 1
            temp.append(b)
        elif temp and temp[-1] == '(':
            temp.pop()
            bracket.pop(top)
            top -= 1
        elif temp and temp[-1] == ')':
            break

    if bracket == []:
        print('#%d %d'%(tc, 1))
    print(temp, bracket)



