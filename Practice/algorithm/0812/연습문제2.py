import sys
sys.stdin = open('test.txt')

def itos(N):
    s = ''
    zero = ord('0')
    minus = False
    if N < 0:
        minus = True
        N *= (-1)
    while N:
        N, remain = N // 10, N % 10
        s += chr(remain + zero)
    if minus:
        s += '-'
    
    print(s[::-1], type(s)) 

T = int(input())

for tc in range(1, T+1):
    print('#%d '%tc, end='')
    itos(int(input()))
