# **DP**

## **Dynamic Programming**

- 특정 문제를 푸는 알고리즘이 아니라 최적화 문제를 해결하는 알고리즘
- 알고리즘 문제 풀이의 접근방식을 가리키는 것
- 입력 크기가 **작은 부분 문제들**을 모두 해결한 후에 그 해들을 이용하여 큰 크기의 부문 문제를 해결하여, 최종적으로 주어진 입력의 문제를 해결

### **피보나치 수 DP 적용**

- 부문 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로,
- **최적 부분 구조**로 이루어져 있음
1. 문제를 부분 문제로 분할
2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구함
    - `Memoization`(큰 부분 문제의 답을 구할 수 없으면 작은 문제로 들어감)
3. 결과는 각 테이블에 저장하고 테이블에 저장된 부분 문제의 해를 이용해 상위 문제의 해를 구함

### **피보나치 수 DP 적용 알고리즘**

```python
def fibo2(n):
    f = [0, 1] # 이 두 개를 더하면 다음 값 도출

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]
```

- DP 구현방식 : `recursive` 방식
    - 값을 계속 가져와서 사용해야 할 때는 `table` 미리 채워두는 게 편함
    - 최종값만 출력하면 될 경우에는 굳이 필요없기도

```python
def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i - 2]
    return

table = [0] * 101
fibo_dp(100) # table을 미리 채워놓은 상태

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {table[N]}')
```

- `memoization` 을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현하는 것이 성능 면에서 보다 효율적
    - 기본적인 함수 호출 자체가 CPU, 변수, 함수 주소 등등을 다 저장하고 이동하기 때문에 짧은 함수 호출도 오래 걸릴 수 있음 ⇒ 호출하고 복귀하는 시간이 더 오래 걸림

# DFS(깊이 우선 탐색)
- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 게 중요
- 깊이 우선 탐색(`Depth First Search, DFS`)
- 너비 우선 탐색(`Breadth First Search, BFS`)


## DFS
- 탐색하는 대상 : 정점
- 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 **갈림길 간선이 있는 정점으로 되돌아와서** 다른 방향의 정점으로 탐색 반복
    - 경로를 저장하는 방법으로 스택, 재귀호출이 있음
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 반복해야 하므로 후입선출 구조 스택 사용


### DFS 알고리즘
1. 시작 정점 v를 결정하여 방문
2. 정점 v에 인접(내가 갈 수 있는)한 정점 중에서
    - 1 -> 2(단방향) : 1에게 2는 인접, 2에게 1은 인접 X
3. 방문하지 않은 정점 `w`가 있으면, 정점 `v`를 스택에 `push`하고 정점 `w` 방문
4. 방문하지 않은 정점이 없으면 탐색의 방향을 바꾸기 위해 스택을 `pop`하여 받은 가장 마지막 방문 정점을 `v`로 하여 다시 `3.` 반복
    - `pop`한 스택이 가장 마지막 방문 정점

- pseudocode
```python
# visited[], stack[] 초기화
DFS(v)
    # 초기화
    시작점 v 방문;
    visited[v] <= true;

    # 방문
    while {
        if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면 )
            push(v)
            v <- w (w에 방문)
            visited[w] <- true;
        else   
            if ( 스택이 비어 있지 않으면 )
                v < - pop(stack)
            else
                break
    }
```

### DFS 실제 구현
```python
adjList = [[1, 2],
           [0, 3, 4],
           [0, 4],
           [1, 5],
           [1, 2, 5],
           [3, 4, 6],
           [5]]

def dfs(v, N):
    visited = [0] * N # N : 정점의 개수
    stack = [0] * N # stack 생성
    top = -1
    print(v)       # 방문하는 곳
    visited[v] = 1 # 시작점 방문 표시
    while True:
        for w in adjList[v]:    # if(v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0: # push(v)
                top += 1
                stack[top] = v
                v = w           # v <- w (w에 방문)
                visited[w] = 1
                print(v)        # 방문
                break
        else:                   # w가 없으면
            if top != -1:       # 스택이 비어 있지 않은 경우
                v = stack[top]  # pop
                top -= 1
            else:               # 스택이 비어 있으면
                break           # while 종료
dfs(0, 7)
```

### DFS input
```python
def dfs(v):
    print(v) # v 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)

            
V, E = map(int, input().split())
N = V + 1 # 0번부터 시작이니까
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
```
```python
# 인접 행렬 리스트
data = [[0 for _ in range(N+1)] for _ in range(N+1)] # 0부터하면 헷갈리니까 1부터
for i in range(E): # 인덱스 자리에 1이 있으면 그 자리와 연결되어 있다
    x, y = map(int, input().split())
    data[x][y] = 1

    if data[x][y] ==1 and visited[y] == False: # 굳이 1차원 배열을 다 돌 필요 없이..
        pass
```