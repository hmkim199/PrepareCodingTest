# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이

def solution(dirs):
    x = 0
    y = 0
    visited = set()

    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for dir in dirs:
        dx, dy = move[dir]
        if -5 <= x+dx <= 5 and -5 <= y+dy <= 5:
            if ((x, y), (x+dx, y+dy)) and ((x+dx, y+dy), (x, y)) not in visited:
                visited.add(((x, y), (x+dx, y+dy)))
            x = x+dx
            y = y+dy
    return len(visited)