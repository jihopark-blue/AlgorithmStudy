
| |DFS|BFS|
|-|-|-|
|동작 원리| 스택 | 큐|
|구현 방법| 재귀 함수 이용| 큐 자료구조 이용|



# DFS
- Depth-First Search, 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택을 이용하는 알고리즘이므로, 재귀 함수를 이용했을 때 매우 간결하게 구현 가능
- 탐색을 수행함에 있어 데이터의 개수가 N개인 경우 O(N)의 시간이 소요
  
DFS 예제
```py
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

##########
# 결과
# 1 2 7 6 8 3 4 5
```

# BFS
- Breadth-First Search, 너비 우선 탐색
- 가까운 노드부터 탐색
- 선입선출 방식인 큐 자료구조를 이용해 구현
- 탐색을 수행함에 있어 O(N)의 시간이 소요됨
- 일반적인 경우, 실제 수행 시간은 DFS보다 좋은 편

BFS 예제
```py
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

##############
# 결과
# 1 2 3 8 7 4 5 6
```
