from collections import deque
word = deque('love')
print(word) # ['l', 'o', 'v', 'e'] 출력

dq = deque((2, 2))
print(dq[0], dq[1])  # 2 2 가 출력됨


# 1. append 는 스택의 마지막(오른쪽 끝)에서 입출력합니다. pop또한 가장 오른쪽 끝에있는 것을 팝합니다.
like = deque()
like.append((2, 3))

# 2. 왼쪽꺼 팝하고싶으면 popleft를 사용하자! , appendleft또한 사용가능합니다.
tmp = like.popleft()
print(tmp) # (2, 3)
print(tmp[0]) # 2
print(tmp[1]) # 3


# 3. deque 확장하기: extend(), extendleft()
dq = deque('love')
dq.extend('you')
print(dq)  # deque(['l', 'o', 'v', 'e', 'y', 'o', 'u'])
dq.extendleft('I')  # deque(['I', 'l', 'o', 'v', 'e', 'y', 'o', 'u'])
print(dq)

# 4. 리스트처럼 사용 : insert(), remove()
word = deque('like')
word.insert(0, 'I')
print(word)  # deque(['I', 'l', 'i', 'k', 'e'])
# 100번째 항목은 존재하지 않으니 가장 끝에 추가
word.insert(100, 'I')
# I 항목을 제거합니다.
word.remove('I')
# 같은 항목이 있을떄는 왼쪽 먼저 제거합니다.
print(word)  # deque(['l', 'i', 'k', 'e', 'I'])
word.remove('I')
print(word)  # deque(['l', 'i', 'k', 'e'])

# 5. deque의 내용을 좌우 반전: reverse()
word.reverse()
print(word)  #deque(['e', 'k', 'i', 'l'])
