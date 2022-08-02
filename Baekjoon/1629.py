# https://www.acmicpc.net/problem/1629
# 곱셈

# 틀린 풀이 - 규칙을 저장해서 인덱스로 접근하려 했음..
r = []
A, B, C = map(int, input().split())
r.append(A%C)
first = r[0] if A > C else -1
idx = 0 if first != -1 else -1

for i in range(2, B+1):
    new_r = A**i % C
    if new_r == first:
        break
    if first == -1 and A**i > C:
        first = new_r
        idx = i-1
    r.append(new_r)

print(r)
if B-idx > 0:
    print(r[(B-idx)%len(r)-1])
else:
    print(r[idx])