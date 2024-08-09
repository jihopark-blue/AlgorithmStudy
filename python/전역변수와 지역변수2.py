def DFS1():
    a[0] = 7    # 새로운 local 리스트 생성 x, 전역 리스트 사용
    print(a)

def DFS2():
    a = [7, 8]  # 새로운 local 리스트 생성
    print(a)

def DFS3():
    a = a + [4]  # UnboundLocalError
    print(a)

def DFS4():
    global a     # 전역 리스트 사용, UnboundLocalError x
    a = a + [4]  
    print(a)
    
if __name__=='__main__':
    a = [1, 2, 3]
    DFS1()
    DFS2()
    DFS3()
    DFS4()
    print(a)

# -> [7, 2, 3] [7, 8] UnboundLocalError [7, 2, 3, 4] [7, 2, 3, 4]
