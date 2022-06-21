from itertools import combinations
import copy

def subtract_score(apeach, lion):
    a = 0
    l = 0
    for i in range(len(apeach)):
        if apeach[i] != 0 and lion[i] <= apeach[i]:
            a += (10-i)
        elif 0 <= apeach[i] < lion[i]:
            l += (10-i)
    return l - a

def solution(n, info):
    answer = [0 for _ in range(11)]
    answer[0] = n
    is_possible = False
    pool = []
    for i in range(len(info)):
        for _ in range(info[i]+1):
            pool.append(10-i)
    
    combi = set(combinations(pool, n))
    
    for c in combi:
        temp = [0 for _ in range(11)]
        for t in c:
            temp[10-t] += 1
        now = subtract_score(info, answer)
        sub = subtract_score(info, temp)
        
        if sub > now and sub > 0:
            answer = copy.deepcopy(temp)
            is_possible = True
        
        elif sub == now and sub > 0:
            for i in range(len(answer)-1, -1, -1):
                if answer[i] > temp[i]:
                    break
                elif answer[i] < temp[i]:
                    answer = copy.deepcopy(temp)
                    break  
            is_possible = True     
    
    if is_possible:
        return answer
    else:
        return [-1]