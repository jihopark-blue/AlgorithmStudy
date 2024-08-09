n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# dy 초기화 
dy = [[0] * n for _ in range(n)]
dy[0][0] = arr[0][0]
# dy 의 0행 0열 초기화 : arr의 각 0행 오른쪽 방향 누적, 0열 아래 방향 누적 
for i in range(n):
    dy[0][i] = dy[0][i-1] + arr[0][i]
    dy[i][0] = dy[i-1][0] + arr[i][0] 

for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]  # 왼쪽과 위쪽방향의 dy 값중 작은 값에 현재 arr 의 값을 더한값을 저장 

print(dy[n-1][n-1])
