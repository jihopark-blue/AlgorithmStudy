def DFS1():
    cnt = 3        # 지역변수
    print(cnt)     # 지역변수 출력

def DFS2():
    if cnt==5:     # 먼저 지역변수인지 확인
        print(cnt) # 지역변수 없으니 전역변수 출력

def DFS3():
    if cnt == 5:     # cnt = cnt+1 line 때문제 지역변수로 인식, UnboundLocalError 발생
        cnt = cnt+1  # 지역변수 생성 - 참조할 지역변수 없으니 에러남
        print(cnt)        # 'cnt = ' 여기서 지역변수로 번역

def DFS4():
    cnt = 3          # 지역변수 생성시 UnboundLocalError x
    if cnt == 3:     
        cnt = cnt+1  
        print(cnt)

def DFS5():
    global cnt       # 기존 전역변수 사용
    if cnt == 5:     # 지역변수 생성 x
        cnt = cnt+1  
        print(cnt)
        
if __name__=='__main__':
    cnt = 5        # 전역변수
    DFS1()
    DFS2()
    DFS3()
    DFS4()
    DFS5()
    print(cnt)

# -> 3 5 UnboundLocalError 4 6
