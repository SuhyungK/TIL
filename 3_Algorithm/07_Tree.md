# Tree

- [트리](https://www.notion.so/22_Tree-d526b18052d6451aaac970f53f830a07)
- [이진 트리](https://www.notion.so/22_Tree-d526b18052d6451aaac970f53f830a07)
- 이진 트리의 표현
- [참조] 이진 트리의 저장
- 연습 문제
- 이진탐색 트리
- 힙

---

## 트리

### 트리의 개념

- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층 관계를 가지는 **계층**형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조
- 한 개 이상의 노드로 이루어진 유한 집합(정점이 한 개만 존재해도 트리)
    - 노드 중 최상위 노드를 루트라 함
    - 나머지 노드들은 n개의 분리 집합 T1… Tn으로 분리될 수 있음
- 이들 T1,… Tn은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리라 함
    - 트리의 일부분을 잘라내면 부 트리(*subtree)*가 됨
- **그래프와의 차이 : 순환구조가 없음, 같은 레벨의 노드끼리는 연결될 수 없음**

### 트리 용어 정리

- 노드(*node*) - 트리의 원소들
    - 트리 T의 노드 - A, B, C, D, E, F, G, H, I, J, K
- 간선(*edge*) - 노드를 연결하는 선. *부모 노드*와 *자식 노드* 연결(계층 관계)
- 루트 노드(*root node*) - 트리의 시작 노드
- 형제 노드 - 같은 부모 노드의 자식 노드들
- 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
    - 공통 조상 - 조상들 중에 겹치는 노드들
- 서브 트리(*subtree*) - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
    - 트리에서 일부만 잘라냈을 때 생성되는 또다른 트리
- 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들
    - 현재 노드를 루트 노드로 하는 하위 레벨의 노드들
- 차수(*degree*)
    - 노드의 자수 : 노드에 연결된 자식 노드의 수
    - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
    - 단말 노드(잎(*leaf*)노드)  : 차수가 0인 노드. 자식 노드가 없는 노드
- 높이
    - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
    - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨

## 이진 트리

- 모든 노드들이 2개의 서브 트리를 갖는 특별한 형태
- 각 노드가 자식 노드를 **최대 2개**까지만 가질 수 있는 트리
    - 왼쪽 자식 노드 1개(*left child node)*
    - 오른쪽 자식 노드 1개(*right child node)*
- 레벨 *i*에서 노드의 최대 개수는 2^*i* 개
- 높이가 *h*인 이진 트리가 가질 수 있는 노드의 개수는 *(h+1)*개가 되며,
- 최대 개수는 $2^{h+1}-1$개
    - 1~ $2^h$ 까지의 합

### 포화 이진 트리(Full Binary Tree)

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 *h*일 때, 최대의 노드 개수인 $2^{h+1}-1$의 노드를 가진 이진 트리
- 루트를 1번으로 하여 왼쪽 → 오른쪽으로 가면서 번호 붙이기

### 완전 이진 트리(Complete Binary Tree)

- 높이가 $h$이고 노드 수가 $n$개일 때, 포화 이진 트리의 노드 번호 1번부터 $n$번까지 중간에 빈 자리가 없는 이진 트리
- 노드가 10개인 완전 이진 트리
- 중간에 번호가 빠지면 안 되고 n번까지는 무조건 존재해야 함

```python
# 완전 이진 트리 구현
def pre(n):
    if n <= size:
        print(tree[n])
        pre(2*n)   # 왼쪽 자식
        pre(2*n+1) # 오른쪽 자식

tree = [0, 'A', 'B', 'C' ,'D', 'E', 'F']
size = len(tree) - 1 # 마지막 정점 번호
pre(1)
```

### 편향 이진 트리(Skewed Binary Tree)

- 높이 *h*에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드 만을 가지는 이진 트리
- = 선형 자료 구조

## 이진 트리 - 순회

- 트리의 각 노드를 중복되지 않게 전부 방문(*visit*)하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조와 같이 선후 연결 관계를 알 수 없음
- 전체의 *root,* 서브의 *root* 어느 쪽이든 시작한 *root*에 도착하면 끝남

### 순회의 3가지 방법

- 순회(*traversal*) : 트리의 노드들을 체계적으로 방문하는 것
    - V - 루트 / L - 왼쪽 서브 트리 / R - 오른쪽 서브 트리
- **전위순회(*preorder traversal*)** : 부모 노드 방문(*처리*) 후, 자식 노드를 좌, 우 순서로 방문
- 중위순회(*inorder traversal*) : 왼쪽 자식 노드 → 부모 노드 → 오른쪽 자식 노드
- 후위순회(*postorder traversal*) : 자식 노드를 좌우 순서로 방문한 후, 부모 노드 방문

### 전위 순회

- 각 서브 트리의 루트를 먼저 방문
1. 현재 노드 n을 방문하여 처리 → V
2. 현재 노드 n의 왼쪽을 방문 → L
3. 현재 노드 n의 오른쪽을 방문 → R

### 중위 순회

1. 현재 노드 n의 왼쪽 서브 트리로 이동 → L
2. 현재 노드 n을 방문하여 처리 → V
3. 현재 노드 n의 오른쪽 서브 트리로 이동 → R

### 후위 순회

1. 현재 노드 n의 왼쪽 서브 트리로 이동 → L
2. 현재 노드 n의 오른쪽 서브 트리로 이동 → R
3. 현재 노드 n을 방문하여 처리 → V

```python
"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
V = int(input())
node = list(map(int, input().split()))
E = V - 1
tree = [[0, 0] for _ in range(V+1)]

for i in range(E):
    p, c = node[2*i], node[2*i+1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c

def pre(n):
    if n:
				print(n, end= ' ')
        pre(tree[n][0])
        pre(tree[n][1])

pre(1)
# 전위 순회
# 1 2 4 7 12 3 5 8 9 6 10 11 13

# 중위 순회
# 12 7 4 2 1 8 5 9 3 10 6 13 11

# 후위 순회
# 12 7 4 2 8 9 5 10 13 11 6 3 1
```

## 배열을 이용한 이진 트리의 표현

- 포화 이진 트리 / 완전 이진 트리
- 이진 트리에 각 노드 번호를 다음과 같이 부여
- 루트의 번호 = 1
- 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 $2^n$ ~ $2^{n+1}-1$ 까지의 번호 차례대로 부여
- 노드 번호의 성질
    - 노드 번호가 *i* 인 노드의 부모 노드 번호? *i // 2*
    - 노드 번호가 *i* 인 노드의 왼쪽 자식 노드 번호 → *2*i*
    - 노드 번호가 *i* 인 노드의 오른쪽 자식 노드 번호 → *2*i +1*
    - 레벨 *n*의 노드 번호 시작 번호는? *2^n*
- 단점 :
    - 메모리 공간 낭비 발생
    - 비효율적일 수 있지만 문제 풀이 할 때는 아무 문제가 없다 ^^

## 이진 트리의 저장

- **노드의 개수 = 간선의 개수 + 1**
- 부모 번호를 인덱스로 자식 번호를 저장
    - 순회 하는 경우
- 4 ← 간선의 개수 N
- 1 2 1 3 3 4 3 5 ← 부모 자식 순

```python
# 부모 번호를 인덱스로 자식 번호를 저장하기
"""
정점 번호 V : 1 ~ (E+1)
간선 수 E
부모 - 자식 순
4
1 2 1 3 3 4 3 5
"""

E = int(input())
arr = list(map(int, input().split()))
V = E + 1
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    p, c =arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # p가 아직 자식이 없으면
        ch1[p] = c  # p의 자식 1로 저장
    else:
        ch2[p] = c

print(ch1)
print(ch2)
# for j in range(0, E*2, 2):
#     p, c = arr[j], arr[j+1]

"""
4
1 2 1 3 3 4 3 5
[0, 2, 0, 4, 0, 0]
[0, 3, 0, 5, 0, 0]
"""
```

### [추가]

```python
# 부모 인덱스로 자식 정보 입력
# 자식 인덱스로 부모 정보 입력
# 루트노드까지 올라가서 조상찾기

N = int(input())
arr = list(map(int, input().split()))
c1 = [0] * (N+2)
c2 = [0] * (N+2)
par = [0] * (N+2)

for i in range(N):
    p, c = arr[2*i], arr[2*i+1]
    if c1[p]:
        c2[p] = c
    else:
        c1[p] = c
    par[c] = p 

print('c1', c1)
print('c2', c2)
print('par', par)

idx = 5
anc = []
while 1:
    if par[idx] == 0:
        break
    anc += [par[idx]]
    idx //= 2 
print('anc', anc)
```

### 전위 순회

- *root = 1*

```python
def preorder(n): # 전위 순회
    if n :
        print(n)  # visit(n) -> 방문한 경우
        preorder(ch1[n])
        preorder(ch2[n])

root = 1
preorder(root)

"""
4
1 2 1 3 3 4 3 5
1
2
3
4
5
"""
```

### 중위 순회

```python
def inorder(n):  # 중위 순회
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

"""
2
1
4
3
5
"""
```

### 후위 순회

```python
def postorder(n):  # 후위 순회
    if n:
        inorder(ch1[n])
        inorder(ch2[n])
        print(n)

"""
2
4
5
3
1
"""
```

- 자식 번호를 인덱스로 부모 번호를 저장
    - 조상을 찾아야 할 때
    - 루트의 번호가 꼭 1번이 아닐 수도

```python
def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:  # 부모가 0이면 root
            return i

E = int(input())
arr = list(map(int, input().split()))
V = E + 1
par = [0] * (V+1)

for i in range(E):
    p, c =arr[i*2], arr[i*2+1]
    par[c] = p

root = find_root(V)

"""
4
2 1 2 3 1 4 1 5
"""

# 자식 노드가 i일 때 부모 노드는 i//2

def find_root(i):
    while 1:
        if par[i] == 0:  # 부모가 0이면 root
            return i
        i //= 2

E = int(input())
arr = list(map(int, input().split()))
V = E + 1
par = [0] * (V+1)

for i in range(E):
    p, c =arr[i*2], arr[i*2+1]
    par[c] = p

root = find_root(V)
print(root)
```

## 트리의 표현 - 연결리스트

- 배열을 이용한 이진 트리의 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현할 수 있음
- 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현

## <연습문제>

- 응용
    - 서브 트리에서 방문할 수 있는 정점의 개수는?
    - 특정 루트에 속한 자손 노드의 개수는?

```python
"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

def pre(n):
    if n:
        print(n, end=' ')
        pre(ch1[n])
        pre(ch2[n])

def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])

def post(n):
    if n:
        post(ch1[n])
        post(ch2[n])
        print(n, end=' ')

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i

V = int(input())
arr = list(map(int, input().split()))
E = V -1
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)

for e in range(0, 2*E, 2):
    p, c= arr[e], arr[e+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
print('전위순회 : ', end='')
pre(root)
print()
print('중위순회 : ', end='')
inorder(root)
print()
print('후위순회 : ', end='')
post(root)
print()

"""
전위순회 : 1 2 4 7 12 3 5 8 9 6 10 11 13 
중위순회 : 12 7 4 2 1 8 5 9 3 10 6 13 11 
후위순회 : 12 7 4 2 8 9 5 10 13 11 6 3 1
"""
```

- *global cnt* 없이 방문한 노드의 개수 세는 함수
- 서브 트리가 비어 있는 경우 = 자식/자손 노드가 없는 경우는 0을 반환
- 왼쪽과 오른쪽에서 각각 반환 값을 받은 후 자기 자신의 개수 +1 해서 다시 값 반환

```python
def f(n):       # global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:  # 서브 트리가 비어 있으면 = 자식/자손 노드가 없으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1
```

## 수식 트리

- 수식을 표현하는 이진 트리
- 수식 이진 트리(*Expression Binary Tree)*
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎(*leaf)* 노드

## 이진 탐색 트리

- 탐색 작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 갖는다
- key(왼쪽 서브 트리) < key(루트 노드) < key(오른쪽 서브 트리)
- 왼쪽 서브 트리와 오른쪽 서브 트리도 각각 이진 탐색 트리
- **중위 순회 → 오름차순으로 정렬**
- 탐색, 삽입, 삭제 시간은 트리의 높이만큼 걸림
- 평균의 경우
    - 이진 트리가 균형적으로 생성되어 있는 경우
    - O($log n$)
- 최악의 경우
    - 이진 트리가 한쪽으로 치우쳐진 경우
    - $O(n)$
    

### 중위 순회 → 오름차순

![캡처.PNG](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cdedfc76-3b67-47e3-958b-89c27eaeef67/%EC%BA%A1%EC%B2%98.png)

```python
tree = [0, 9, 4, 12, 3, 6, 0, 15, 0, 0, 5, 0, 0, 0, 13, 17]

def inorder(n):
    if n < len(tree) and tree[n]:
        inorder(2*n)
        print(tree[n], end=' ')
        inorder(2*n+1)

inorder(1)

"""
3 4 5 6 9 12 13 15 17
"""
```

## 힙

- 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 힙의 키를 우선순위로 활용하여 우선순위 큐를 구현할 수 있음
- 최대 힙
    - 키 값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
    - 부모 노드의 키 값 > 자식 노드의 키 값
    - 루트 노드 : 키 값이 가장 큰 노드
- 최소 힙
    - 키 값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**
    - 부모 노드의 키 값 < 자식 노드의 키 값
    - 루트 노드 : 키 값이 가장 작은 노드

## 힙 연산 - 삽입

```python
# 최대힙

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가
    # 부모 노드가 있고 부모 < 자식 노드인 경우 자리 교환
    c = last        # 삽입된 값을 자식 노드로 둠
    p = c // 2      # 완전 이진 트리에서 부모의 정점 번호
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p       # 부모를 새로운 자식으로
        p = c // 2

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
print(heap)
```

## 힙 연산 - 삭제

- 힙에서는 루트 노드의 원소만 삭제할 수 있음
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 *or* 최소값 구할 수 있음
- 항상 최대값 혹은 최소값이 힙의 루트에 위치하기 때문에 최대, 최소 값을 찾아낼 때 유리

```python
def deq():
    global last
    # 루트 백업
    tmp = heap[1]           # 완전 이진 트리라서 무조건 1
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1          # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c] : # 자식이 더 크면 최대 힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c           # 자식을 새로운 부모로
            c = 2 * p       # 왼쪽 자식 번호를 계산
        else:               # 부모가 더 크면 비교 교환 중단
            break
    return tmp

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())

"""
7
6
5
4
3
2
"""
```

### [추가]

```python
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = 2*p
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p*2
        else:
            break
    return tmp

heap = [0] * 10
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
print(heap)

while last:
    print(deq())
    print(heap)

"""
[0, 7, 4, 6, 2, 3, 5, 0, 0, 0]
7
6
5
4
3
2
"""
```