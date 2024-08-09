# 📚 자료구조
1. 스택 (Stack), 큐 (Queue), 덱 (Dequeue)
2. 그래프
   
## ☁️ 스택 (Stack)
![stack](https://github.com/hufs71/code-study/assets/115367115/2c4c293e-c363-4bed-b713-6482e7a76857)

한 쪽에서만 자료를 넣고 뺄 수 있는 후입선출 `LIFO (Last In First Out)` 형식의 선형 자료구조 
- 같은 구조와 크기의 자료를 정해진 방향으로만 쌓을 수 있고, top으로 정한 곳을 통해서만 접근할 수 있다.
### 스택의 연산
- push(삽입): 데이터 삽입
- pop(삭제): 데이터 삭제
### 예제
```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1] # 최상단 원소부터 출력

##########

# 결과
# [5, 2, 3, 1]
# [1, 3, 2, 5]
```
---
## ☁️ 큐 (Queue)
![queue](https://github.com/hufs71/code-study/assets/115367115/c35fab17-c203-441f-984a-c9375db3c199)

한 쪽에서 삽입 작업이 이루어지고, 다른 한 쪽에서는 삭제 작업이 이루어지는 선입선출 `FIFO(First In First Out)` 형식의 선형 자료구조

- 삭제 연산만 수행되는 곳은 `프론트(front)`, 삽입 연산만 이루어지는 곳을 `리어(rear)`, 리어에서 이루어지는 삽인 연산을 `인큐(enQueue)`, 프론트에서 이루어지는 삭제 연산을 `디큐(dnQueue)`라고 부른다.
- 
### 큐의 연산
큐의 연산은 collections 모듈에서 제공하는 deque 자료구조를 활용하는 것이 좋다. deque는 스택과 큐의 장점을 모두 채택한 것인데, 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다. 
- append(): 오른쪽에서 데이터 삽입
- appendleft(): 왼쪽에서 데이터 삽입
- pop(): 오른쪽에서 데이터 삭제
- popleft(): 왼쪽에서 데이터 삭제

### 큐 예제

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력

########
# 결과
# deque([3, 7, 1, 4])
# deque([4, 1, 7, 3])
```
---
## ☁️ 덱 (Dequeue)
![dequeue](https://github.com/hufs71/code-study/assets/115367115/b8bacc42-704e-4557-83e1-4e94a3820e27)

양쪽에서 삽입과 삭제가 가능한 구조이며, 스택과 큐의 연산을 모두 지원한다. 
- `Scroll`: 입력 제한 덱 (입력은 한 쪽에서만 발생하고, 출력은 양쪽에서 일어날 수 있음)
- `Shelf`: 출력 제한 덱 (입력은 양쪽에서 일어나고, 출력은 한 쪽에서 일어나도록 제한)

### 덱의 연산
collections 모듈에서 제공하는 deque 클래스로 구현 가능
- append(): 오른쪽에서 데이터 삽입
- appendleft(): 왼쪽에서 데이터 삽입
- pop(): 오른쪽에서 데이터 삭제
- popleft(): 왼쪽에서 데이터 삭제

### 덱 예제
```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.pop()
queue.pop()

print(queue)

# 결과
deque([1])
```

[참고1](https://velog.io/@falling_star3/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%ED%81%90Queue%EB%8D%B1Deque)
[참고2](https://velog.io/@nnnyeong/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D-Stack-%ED%81%90-Queue-%EB%8D%B1-Deque)

---

## ☁️ 그래프
![asdf](https://github.com/hufs71/code-study/assets/115367115/2b7341b5-f8b2-49d3-aedb-4ac62d5bc2e8)

> - 노드, Node (정점, Vortex)
> - 간선, Edge
> - 두 node가 edge로 연결되어 있다면 '두 node는 인접하다(adjacent)'라고 표현

### 그래프를 표현하는 두 가지 방식
1. 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
2. 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식

인접 행렬 방식 예제
```py
INF = 99999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
   [0, 7, 5],
   [7, 0, INF],
   [5, INF, 0]
]

print(graph)

#########
# 결과
# [[0, 7, 5], [7, 0, 99999999999], [5, 99999999999, 0]]
```

인접 리스트 방식 예제
```py
# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)

###########
# 결과
# [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
```
