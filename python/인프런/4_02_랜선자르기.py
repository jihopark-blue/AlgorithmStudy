# 이진 탐색
# 결정 알고리즘

'''
import sys
sys.stdin=open('in4.txt','r')

k, n = map(int, input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))

lt = 0
rt = max(nums)

while lt <= rt:
    mid = (lt + rt) // 2

    cnt = 0
    for num in nums:
        cnt += num//mid

    if cnt == n:
        break
    elif cnt > n:
        lt = mid+1
    elif cnt < n:
        rt = mid-1

print(mid)
'''

# 정답 코드

import sys
sys.stdin = open('in5.txt', 'r')

k, n = map(int, input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))

lt = 1  # 0으로 나누는 것을 방지하기 위해 lt를 1로 시작
rt = max(nums)
answer = 0  # 길이를 저장할 변수

while lt <= rt:
    mid = (lt + rt) // 2

    cnt = 0
    for num in nums:
        cnt += num // mid

    if cnt >= n:  # 충분한 개수를 만들 수 있는 경우
        answer = mid  # mid 값을 저장
        lt = mid + 1  # 더 큰 범위 계속 탐색해야함
    else:
        rt = mid - 1  

print(answer)
