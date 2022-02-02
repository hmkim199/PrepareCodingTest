# https://www.acmicpc.net/problem/1920
# 수 찾기

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

# start 가 -1인 경우 생각해....
def binarySearch(search_num, target_list):
    start = 0
    end = len(target_list)-1
    while start <= end:
        mid = (start+end)//2
        if target_list[mid] > search_num:
            end = mid-1
        elif target_list[mid] < search_num:
            start = mid+1
        else:
            return mid
    return -1

for i in range(M):
    if binarySearch(B[i], A) != -1:
        print(1)
    else:
        print(0)
