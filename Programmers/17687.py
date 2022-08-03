# 
# 

def solution(n, t, m, p):
#     진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    answer = ''
    sequence = []
    num = 0
    hexa = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G'}
    while len(sequence) < m*t:
        temp = num
        trans = ''

        # 진법 변환
        while temp >= 1:
            remain = temp % n
            if remain > 9:
                remain = hexa[remain]
            trans = str(remain) + trans
            temp //= n
        if not trans:
            trans = str(temp)
        for c in trans:
            idx = len(sequence) + 1
            if (idx-p) % m == 0 and len(answer) < t:
                answer += c
            sequence.append(c)
            
        num += 1
    
    
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))