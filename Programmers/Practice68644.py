# https://programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기

# 예전 코드
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    return sorted(answer)


# 현재 코드
def solution(numbers):
    answer = []

    for i in range(0, len(numbers)):
        for j in numbers[i+1:]:
            answer.append(numbers[i]+j)
    answer = sorted(list(set(answer)))
    return answer