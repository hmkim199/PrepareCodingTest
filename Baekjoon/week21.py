# https://programmers.co.kr/learn/courses/30/lessons/67256
# [카카오 인턴] 키패드 누르기

# 저번 풀이
def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    distance = [0, 0]
    for number in numbers:
        if number in (1, 4, 7):
            answer += "L"
            left = number
        elif number in (3, 6, 9):
            answer += "R"
            right = number 
        else:
            if number == 0:
                number = 11
            distance[0] = abs(number-left) % 3 + abs(number-left) // 3
            distance[1] = abs(number-right) % 3 + abs(number-right) // 3
            if distance[0] == distance[1]:
                if hand == 'left':
                    left = number
                    answer += "L"
                else:
                    right = number
                    answer += "R"
            elif distance[0] < distance[1]:
                left = number
                answer += "L"
            else:
                right = number
                answer += "R"
                        
            
    return answer


# 이번 풀이
def solution(numbers, hand):
    answer = ''
    left = -1
    right = -2
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 
              4: (1, 0), 5: (1, 1), 6: (1, 2), 
              7: (2, 0), 8: (2, 1), 9: (2, 2), 
              -1: (3, 0), 0: (3, 1), -2: (3, 2), }
    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            left = num
        elif num in (3, 6, 9):
            answer += 'R'
            right = num
        else:
            left_x, left_y = keypad[left]
            right_x, right_y = keypad[right]
            new_x, new_y = keypad[num]
            
            dist_l = abs(new_x-left_x) + abs(new_y-left_y)
            dist_r = abs(new_x-right_x) + abs(new_y-right_y)
            if dist_l < dist_r:
                answer += 'L'
                left = num
            elif dist_l > dist_r:
                answer += 'R'
                right = num
            else:
                if hand == "left":
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num
            
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/81301
# 숫자 문자열과 영단어

def solution(s):
    answer = ''
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    temp = ''
    for c in s:
        if c.isdigit():
            answer += c
            continue
        temp += c
        if temp in numbers:
            answer += str(numbers[temp])
            temp = ''
    return int(answer)


# https://programmers.co.kr/learn/courses/30/lessons/72410
# 신규 아이디 추천

def solution(new_id):
    answer = ''
    for c in new_id:
        if c.isalpha():
            answer += c.lower()
        elif c.isdigit():
            answer += c
        elif c in ('-', '_'):
            answer += c
        elif c == '.':
            if answer and answer[-1] != c:
                answer += c
    
    while answer and answer[0] == ".":
        answer = answer[1:]
    while answer and answer[-1] == ".":
        answer = answer[:-1]
    
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]
        
            
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/77484
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    score = 0
    black = 0
    win_nums = set(win_nums)
    for lotto in lottos:
        if lotto in win_nums:
            score += 1
        elif lotto == 0:
            black += 1
    
    answer.append(7-(score+black))
    answer.append(7-(score))
    
    for i in range(len(answer)):
        if answer[i] > 6:
            answer[i] = 6
    return answer 


# https://programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    cnt = {}
    reports = {}
    for i in range(len(id_list)):
        reports[id_list[i]] = (i, set()) # id: index, set() 형태로 저장
        cnt[id_list[i]] = 0
    
    for rep in report:
        a, b = rep.split()
        length = len(reports[a][1])
        reports[a][1].add(b)
        if length != len(reports[a][1]):
            cnt[b] += 1
    
    for user in reports:
        for rep in reports[user][1]:
            if cnt[rep] >= k:
                answer[reports[user][0]] += 1
    
    return answer

# 두 번째 풀이
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    cnt = {}
    reports = {}
    for i in range(len(id_list)):
        id = id_list[i]
        reports[id] = {"idx": i, "rep": set()}
        cnt[id] = 0
    
    for rep in report:
        a, b = rep.split()
        length = len(reports[a]["rep"])
        reports[a]["rep"].add(b)
        if length != len(reports[a]["rep"]):
            cnt[b] += 1
    
    for user in reports:
        for rep in reports[user]["rep"]:
            if cnt[rep] >= k:
                answer[reports[user]["idx"]] += 1
    
    return answer