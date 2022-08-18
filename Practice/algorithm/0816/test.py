import sys
sys.stdin = open('test.txt')

def pali(arr):
    ans = 0
    for row in range(100):
        for col in range(100, 0, -1):
            for j in range(100-col+1):
                temp = arr[row][j:j+col]
                if temp == temp[::-1]:
                    ans = len(temp)
                    return ans


for _ in range(10):
    tc = input()
    arr = [input() for _ in range(100)]

    p1 = pali(arr)
    
    print('#%s' %tc)