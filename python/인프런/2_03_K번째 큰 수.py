# 3. K번째 큰 수

import sys
sys.stdin=open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() # 중복 제거
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n): # 숫자 3개
            res.add(a[i]+a[j]+a[m]) # set 자료구조에 추가

res = list(res) # sort하기 위해 list로 변환
res.sort(reverse=True)
print(res[k-1])
