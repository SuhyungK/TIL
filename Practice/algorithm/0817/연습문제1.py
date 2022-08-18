# 스택 구현하기
def push(item, top):
    top += 1
    stack[top] = item
    print(stack[top])

def pop(top):
    print(stack[top])
    top -= 1

size = int(input())
stack = [0] * size
top = -1

push(1, top)
