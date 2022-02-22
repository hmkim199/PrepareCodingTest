# https://www.acmicpc.net/problem/2839
# 설탕 배달


N = int(input())

bags = (3, 5)
count = [N%bags[1]//bags[0], N // bags[1]]
possible = True

def sum_sugar():
    total = 0
    for i in range(len(bags)):
        total += bags[i]*count[i]
    return total

while sum_sugar() != N:
    count[1] -= 1
    count[0] = (N - bags[1]*count[1])//bags[0]
    
    if count[1] < 0:
        possible = False
        break

if not possible:
    print(-1)
else:
    print(sum(count))