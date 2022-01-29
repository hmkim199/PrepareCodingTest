# https://www.acmicpc.net/problem/1929
#  소수 구하기

M, N = map(int, input().split())

# def prime_number(M, N):
#     prime = 1
#     not_prime = -1
#     prime_numbers = [i for i in range(M, N+1)]
#     end = prime_numbers[-1]
#     while prime <= end:
#         prime += 1
#         for i in range(len(prime_numbers)):
#             if prime_numbers[i] not in (not_prime, prime):
#                 if prime_numbers[i] % prime == 0:
#                     prime_numbers[i] = not_prime
#     for i in prime_numbers:
#         if i != not_prime:
#             print(i)
    
# prime_number(M, N)

def prime(M, N):
    numbers = [False, False] + [True] * (N-1)
    primes = []

    for i in range(2, N+1):
        if numbers[i]:
            if i >= M:
                primes.append(i) 
            for j in range(2*i, N+1, i):
                numbers[j] = False

    print(*primes, sep="\n")

prime(M, N)