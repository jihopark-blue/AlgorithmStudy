# 선택 정렬

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))


# 15 27 12
for i in range(n):
    mi = i
    for j in range(i+1, n):
        if nums[mi] < nums[j]:
            mi = j
    nums[i], nums[mi] = nums[mi], nums[i]

print(nums)


'''
# 수의 개수가 500개 이하로 매우 적으며, 모든 수는 1이상 100,000 이하이므로 어떠한 정렬 알고리즘을 사용해도 문제 해결 가능
# 가장 코드가 간결한 파이썬 기본 정렬 라이브러리 사용

n = int(input())
array = []
for i in range(n):
		array.append(int(input())
		
array = sorted(array, reverse=True)

for i in array:
		print(i, end=' ')
'''
