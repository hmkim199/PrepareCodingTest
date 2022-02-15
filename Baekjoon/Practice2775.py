# https://www.acmicpc.net/problem/2775
# 부녀회장이 될테야
 

T = int(input())
p = {} # 메모이제이션 할 딕셔너리

def get_people(k, n):
    if k == 0:
        p[(k,n)] = n
        return n
    elif (k,n) in p:
        return p[(k,n)]
    else:
        people = 0
        for i in range(1, n+1):
            people += get_people(k-1, i)
        p[(k,n)] = people
        return people
    

for _ in range(T):
    k = int(input())
    n = int(input())
    print(get_people(k, n))