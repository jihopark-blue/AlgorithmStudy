# 합이 같은 부분집합 (DFS)
import sys
sys.stdin = open('input.txt', 'r')

def DFS(L, sum):
    if L == n:
        if sum == (total-sum): # 부분집함의 합이 나머지 부분집한의 합과 같음
            print("YES")
            sys.exit(0)  # 출력 후 종료
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print('NO') # 종료되지 않았다면 NO 출력

# 시간복잡도 줄이기
# sum이 total의 절반을 넘었다면 더 탐색할 필요 없음
def DFS(L, sum):
    if L == n:
        if sum > total//2:
            return
        
        if sum == (total-sum): # 부분집함의 합이 나머지 부분집한의 합과 같음
            print("YES")
            sys.exit(0)  # 출력 후 종료
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print('NO') # 종료되지 않았다면 NO 출력
