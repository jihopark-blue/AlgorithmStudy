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
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.pop()

print(stack)

#결과
[1]
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

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.popleft()

print(queue)

# 결과
deque([3])
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
---
[참고1](https://velog.io/@falling_star3/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%ED%81%90Queue%EB%8D%B1Deque)
[참고2](https://velog.io/@nnnyeong/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D-Stack-%ED%81%90-Queue-%EB%8D%B1-Deque)


