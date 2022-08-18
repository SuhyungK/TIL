import sys
sys.stdin = open('input.txt')

# (랑 {가 들어오면 push
# )랑 }가 들어오면 stack에서의 값과 비교해서 짝이면 pop 아니면 return 0
# 검사를 다 했는데 stack에 값이 남아있으면 return 0
#      "        stack에 값이 없으면 return 1

def bracket(arr):
    stack = []
    bd = {')':'(','}':'{'}
    for a in arr:
        if a == '(' or a == '{':  # push
            stack.append(a)
        elif a in bd.keys(): # stack이 비어있지 않고 a가 '}' or ')'
            if not stack:    # 닫는 괄호값이 들어왔는데 stack이 비어 있는 경우 return 0
                return 0     # 이걸 안 해줘서 에러남
            elif stack.pop() != bd.get(a): # stack.pop()이 가장 마지막에 들어온 값을 반환하므로
                return 0                   # 두 값이 다르면 짝을 이루지 못하니까 return 0

    if stack: # 검사가 끝나고 stack이 비어있는 경우 1, 비어있지 않는 경우 0
        return 0
    return 1

t = int(input())
for tc in range(1, t+1):
    print('#%d %d'%(tc, bracket(list(input()))))

