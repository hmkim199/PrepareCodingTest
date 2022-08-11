# https://app.codility.com/c/run/training6VM85H-GXR/
# BinaryGap

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    bin_num = str(bin(N))[2:]
    start = False
    max_gap = 0
    temp_gap = 0
    
    for c in bin_num:
        if c == '1':
            start = True
            max_gap = max(max_gap, temp_gap)
            temp_gap = 0
        else:
            if start:
                temp_gap += 1

    return max_gap


