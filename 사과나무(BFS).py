from collections import deque
# 좌상우하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 격자판 정의
n = int(input())
# 격자판 생성
a = [list(map(int, input().split())) for _ in range(n)]
# 격자판 0으로 초기화
ch = [[0] * n for _ in range(n)]
# 사과 개수의 합을 출력할 곳을 초기화 합니다.
sum = 0
# BFS는 Q를 사용하므로 초기화 합니다.
Q = deque()
# 격자판 한 가운데가 시작 지점이므로 우리는 1로 체크하고
ch[n // 2][n // 2] = 1
# 그곳의 합을 더한다음에
sum += a[n // 2][n // 2]
# Q에 넣습니다.
Q.append((n // 2, n // 2))
L = 0

# Q에 아무것도 없으면 종료됩니다.
while Q:
  # 종료지점 L이 2보다 크면 종료 (5*5이면 위아래로 가운데에서 2칸씩만 가면 종료되므로)
  if L == n // 2:
    break
  # 가지 뻗기
  size = len(Q)
  for i in range(size):
    tmp = Q.popleft()  # 처음에 2,2가 pop되면서 tmp에 튜플 형식으로 임시저장! 즉 첫 값을 팝하고 그에 해당하는 가지를 내리는 과정 BFS
    for j in range(4):
      x = tmp[0] + dx[j]
      y = tmp[1] + dy[j]
      if ch[x][y] == 0:
        sum += a[x][y]
        ch[x][y] = 1
        Q.append((x, y))
  print(L, size)
  for x in ch:
    print(x)
  L += 1

print(sum)

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 0 1
# [0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0]
# [0, 1, 1, 1, 0]
# [0, 0, 1, 0, 0]
# [0, 0, 0, 0, 0]
# 1 4
# [0, 0, 1, 0, 0]
# [0, 1, 1, 1, 0]
# [1, 1, 1, 1, 1]
# [0, 1, 1, 1, 0]
# [0, 0, 1, 0, 0]
# 379
