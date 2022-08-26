import sys
sys.stdin = open('4615.txt')
T = int(input())

for tc in range(T):
    s = input()
    reversed_s = ''

    for i in range(len(s) -1, -1, -1):
        reversed_s += s[i]

    print('#%d %s' %(tc+1, reversed_s))

"""
#1 mhtirogla
#2 trohs si efil
#3 nohtyp deen uoy
#4 YFASS
"""