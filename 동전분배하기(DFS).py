def DFS(L):
    global res
    if L == n:
        cv.sort()
        res = cv[2] - cv[0]
    else:
        for i in range(3):
            money[i] += cv[L]
            DFS(L+1)
            money[i] -= cv[L]
            DFS(L-1)


if __name__ == "__main__":
    # 동전의 개수를 입력 받는다.
    n = map(int, input().split())
    # 동전의 금액을 입력 받을 리스트 생성 cv = [] 해도됨.
    cv = list()
    # 각 사람이 받는 동전을 기록할 리스트 초기화
    money = [0]*3
    # 최소 차를 출력해야 하므로 최대값으로 초기화
    res = 2147000000
    for _ in range(n):
        cv.append(int(input()))
    DFS(0)
    print(res)
