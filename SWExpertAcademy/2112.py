# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu&categoryId=AV5V1SYKAaUDFAWu&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98+SW&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 2112. [모의 SW 역량테스트] 보호 필름

# 몰라서 영상 보고 풀었음: https://www.youtube.com/watch?v=FxIHhrtLZdo

# 성능 검사 통과 여부 확인 함수
def performance_test():
    for i in range(W):
        count = 0
        temp = 1
        for j in range(1, D):
            prev = film[j-1][i] if inject_list[j-1] == -1 else inject_list[j-1]
            curr = film[j][i] if inject_list[j] == -1 else inject_list[j]

            if prev == curr:
                temp += 1
                count = max(count, temp)
            else:
                temp = 1
        if count < K:
            return False
    else:
        return True

def dfs(row, inject):
    global inject_list
    global min_count

    # 최소값 넘으면 안 봐도 됨
    if inject >= min_count:
        return
    
    # 마지막 줄까지 약품 처리 끝난 경우 최소 count 갱신
    if row == D:
        if performance_test():
            min_count = min(min_count, inject)
        return
    
    for i in range(-1, 2): # -1: 그대로, 0: A 약품 처리, 1: B 약품 처리
        inject_list[row] = i
        if i == -1:
            dfs(row+1, inject)
        else:
            dfs(row+1, inject+1)


T = int(input())
for testcase in range(1, T+1):
    D, W, K = map(int, input().split())
   
    film = []
    for _ in range(D):
        film.append(list(map(int, input().split())))

    min_count = K if K > 1 else 0
    inject_list = [0 for _ in range(D)]

    dfs(0, 0)
    print("#" + str(testcase), str(min_count))

