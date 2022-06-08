# https://www.acmicpc.net/problem/1107
# 리모컨

# 검색해서 품. 브루트 포스.

N = int(input())
M = int(input())
broken = set()
if M != 0:
    broken = set(input().split())

now = 100
answer = abs(now-N) # 최악의 경우 +또는 -로만 움직임
for channel in range(1000001):
    channel_str = str(channel)
    for n in channel_str:
        if n in broken:
            break
    else: # for else문 -> for문이 break 등으로 비정상 종료된 게 아니면 else문으로 들어감
        answer = min(answer, abs(channel-N) + len(channel_str)) # min의 두번째 인자는, 현재 채널 자리수 + 현재 채널에서 목표 채널까지의 절대값(+ 또는 -만으로 이동)

print(answer)