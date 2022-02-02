# https://www.acmicpc.net/problem/1978
# 소수 찾기

N = int(input())
nums = sorted(list(map(int, input().split())))
primes = [False, False] + [True]*(nums[-1]-1)

def prime(n):
    for i in range(2, n+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
            
def countPrime(primes, nums):
    count = 0
    for num in nums:
        if primes[num]:
            count += 1
    return count

prime(nums[-1])
print(countPrime(primes, nums))