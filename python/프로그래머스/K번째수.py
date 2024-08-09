# 정렬 알고리즘
# https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    
    answer = []
    
    for command in commands:
        
        first = command[0]
        second = command[1]
        third = command[2]
        
        tmp = array[first-1:second] # 2, 3, 4, 6
        tmp.sort()
        answer.append(tmp[third-1])
        
    return answer
