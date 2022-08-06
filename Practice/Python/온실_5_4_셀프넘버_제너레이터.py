
def fn_d(N):
    s = N
    for n in str(N):
        s += int(n)
    return s 

def is_selfnumber(n):
    arr = [j for j in range(1,n)]
    print(arr)
    for i in range(1,n):
        if fn_d(i) in arr: 
            arr.remove(fn_d(i))
    return arr

print(is_selfnumber(50))