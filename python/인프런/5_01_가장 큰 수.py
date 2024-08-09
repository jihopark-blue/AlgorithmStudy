# 정답 풀이

num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m>0 and stack[-1]<x: # stack이 비어있지 않고 마지막에 stack에 들어간 수가 지금 수보다 작음
        stack.pop() # 마지막에 들어간 숫자 pop
        m -= 1
    stack.append(x)
if m!=0: # 더 지워야함
        stack = stack[:-m] # 뒤쪽 m개의 숫자 삭제

res = ''.join(map(str, stack))
print(res)


# 내 폴이
'''
mx_idx = seperate.index(max(seperate)) 
idx = 0
cnt = 0

if mx_idx == m: 
    seperate = seperate[mx_idx:]

elif mx_idx > m: # max 앞 숫자가 제거해야 할 숫자보다 많으면
    tmp = seperate[:mx_idx]
    while cnt <= m:
        mx = max(tmp)
        if seperate[idx] != mx:
            seperate.pop(idx)
            cnt += 1
        else:
            idx += 1 # 제거한 숫자 없으면 idx += 1

else:
    while cnt < m:
        mn = min(seperate)
        mn_idx = seperate.index(mn)
        seperate.pop(mn_idx)
        cnt += 1
'''
