# https://programmers.co.kr/learn/courses/30/lessons/86491
# 최소직사각형

# 내 코드
def solution(sizes):
    answer = 0
    w, h = max(sizes[0][0], sizes[0][1]), min(sizes[0][0], sizes[0][1])

    for i in range(1, len(sizes)):
        sizes[i][0], sizes[i][1] = max(sizes[i][0], sizes[i][1]), min(sizes[i][0], sizes[i][1])
        if w < sizes[i][0]:
            w = sizes[i][0]
        if h < sizes[i][1]:
            h = sizes[i][1]
    
    answer = w * h
    
    return answer