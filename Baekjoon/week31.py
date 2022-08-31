# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 모음 사전

from itertools import product

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        dictionary += product(alphabet, repeat=i) # product는 중복 순열. alphabet의 요소들 중에서 반복해서 i개 뽑아 줄세워서 리턴.
    
    dictionary.sort()
    return dictionary.index(tuple(word))+1