# https://www.acmicpc.net/problem/5430
# AC

from collections import deque


T = int(input())

def AC():
    p = input()
    n = int(input())

    nums = input()[1:-1]
    if len(nums) > 0:
        nums = deque(nums.split(","))

    result = nums
    straight = True
    front = 0
    back = n-1
    for op in p:
        if op == "R":
            straight = not straight
        elif op == "D":
            if back < front:
                result = "error"
                return result
            else:
                if straight:
                    front += 1
                else:
                    back -= 1
    
    result = list(result)
    result = result[front:back+1]
    if straight:
        result = '[' + ','.join(result) + ']'
        return result
    else:
        result = '[' + ','.join(list(reversed(result))) + ']'
        return result

for _ in range(T):
    print(AC())