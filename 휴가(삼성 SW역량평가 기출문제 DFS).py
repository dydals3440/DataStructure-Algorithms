def DFS(L, sum):
    global res
    if L == n+1:
        if res < sum:
            res = sum
    else:
        # L일날 상담하면 T[L]일 후 상담이 가능하다.
        if L + T[L] <= n+1:
            DFS(T[L]+L, sum + P[L])
            DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    # L자체를 일이라고 보기떄문에 우리는 0번 인덱스를 활용하지 않을 것이다
    # 하지만 파이썬은 0번 인덱스부터 시작하기에 값을 입력받고 그냥 0번을 채워줄것이다.
    T.insert(0, 0)
    P.insert(0, 0)
    # 1일부터 시작, L로 T랑 P요소를 접근할 것이다.
    DFS(1, 0)
    print(res)
