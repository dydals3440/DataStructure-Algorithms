# 파이썬은 기본적으로 모든 입력을 str 형으로 처리합니다.
# 다른 타입으로 입력을 받고 싶다면 int(), float() 등 타입 캐스팅 함수를 사용해야 합니다.
string = input() # 문자열 입력
num = int(input()) # 정수형 입력
floating = float(input()) # 실수형 입력

# 2. 공백을 가지는 입출력
str1, str2 = input().split() # 공백을 두고 문자열을 입력 받을 떄
num1, num2 = map(int, input().split()) # 공백을 두고 정수를 입력받을 떄
float1, float2 = map(float, input().split()) # 공백을 두고 실수를 입력받을 떄

# 3. 변수를 포함한 문자열 출력('{} {}'.foramt 키워드를 사용하는게 가장 편리한 것 같다)
message1 = "이 글은"
number1 = 5
print('{} {}번 수정되었습니다.'.format(message1, number1))

# List
# 1. 리스트 생성 [대괄호] 사용 외에도 list() 함수를 통해 생성가능
arr1 = [1, 2, 3, 4, 5] # [1, 2, 3, 4, 5] 생성
arr2 = list() # 빈 리스트 생성
arr2 = list([1, 2, 3, 4, 5]) #[1, 2, 3, 4, 5] 생성

# 2. 리스트 초기화
# 간단한 1차원 배열 초기화
n = 5
arr = [0] * n # [0, 0, 0, 0, 0]

# 리스트 컴프리헨션을 활용한 초기화
# 1. row * col 크기의 2차원 리스트를 0으로 초기화하는 예제
row, col = map(int, input().split())
# 반복내용 for _ in range(반복횟수)]
arr = [[0] * col for _ in range(row)]

# 2. 0, 1, 2, 3, ... N-2, N-1 로 리스트를 초기화하는 예제
n = int(input())
arr = [i for i in range(n)]

# 3. 0 ~ N-1 중 짝수 원소만으로 리스트를 초기화하는 예제
n = int(input())
arr = [i for i in range(n) if i % 2 == 0]

# 4. 0 ~ N-1의 제곱 값으로 리스트를 초기화하는 예제
n = [i * i for i in range(n)]