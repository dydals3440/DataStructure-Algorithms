# import sys
# sys.stdin = open("input.txt", "r")

# BFS는 deque를 사용합니다
from collections import deque
# 좌표의 맥시멈은 1만이므로
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
# n이 출발점 m이 도착점
n, m = map(int, input().split())
# 처음에 n에서 출발하므로 시작점 1 체크
ch[n] = 1 
# 거리는 0으로 표기
dis[n] = 0 
dQ = deque()
dQ.append(n)

# queue가 비어있으면 멈춥니다.
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5): #next가 now-1, now+1, now+5 이렇게 3번 돕니다.
        # 음수로 가면안됨 좌표는 1투어라고 문제에서 표기
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] =1 # 방문했따 체크
                dis[next] = dis[now]+1 #next는 자기 부모값 now 보다 하나 더 증가
print(dis[m])