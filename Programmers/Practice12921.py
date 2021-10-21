# https://programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기

# 예전 코드
import math

def solution(n):
    answer = 0
    #result = []
    for i in range(2, n+1):
        prime = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            answer += 1
            #result.append(i)
        #print(result)
    return answer



#지금 코드 -> 에라토스테네스의 체 이용
def solution(n):
    answer = 0
    isPrime = [True for _ in range(n+1)]
    isPrime[0], isPrime[1] = False, False
    
    for i in range(len(isPrime)):
        if isPrime[i] == True:
            answer += 1
            for j in range(2, len(isPrime)):
                if i*j > len(isPrime)-1:
                    break
                isPrime[i*j] = False

    
    return answer