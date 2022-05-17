import sys
while True:
    num = sys.stdin.readline().rstrip()
    if int(num) == 0:
        break
    isPalindrom = True
    for i in range(len(num)//2+1):
        if num[i] != num[-(i+1)]:
            isPalindrom = False
    if isPalindrom:
        print("yes")
    else:
        print("no")
        

# ========================================
N = int(input())

cnt = 1
num = 666

while cnt < N:
    num += 1
    if "666" in str(num):
        cnt += 1

print(num)

# ========================================
K, N = map(int, input().split())
lines = []

for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)
while start <= end:
    count = 0
    middle = (start+end)//2
    for line in lines:
        count += line // middle
    if count >= N:
        start = middle + 1
    else:
        end = middle - 1
    
print((start+end)//2)


# ========================================
def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    
    return answer

# ========================================
def solution(arr):
    answer = []
    prev = -1
    
    for i in arr:
        if prev != i:
            answer.append(i)
        prev = i
    return answer