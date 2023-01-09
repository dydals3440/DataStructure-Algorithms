def DFS(L, sum):
    # 종료 조건
    global cnt
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            # cn[L]이 5면 6가닥 돌아야함.
            DFS(L+1, sum+(cv[L]*i))


if __name__ == "__main__":
    # 지폐의 금액
    T = int(input())
    # 동전의 종류 가지 수
    k = int(input())
    # 동전 금액
    cv = list()
    # 해당 금액의 동전의 개수
    cn = list()
    # 입력 받아 각 리스트에 금액과 동전 개수 append
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    # 개수를 세야 하므로 적어주기
    cnt = 0
    DFS(0, 0)
    print(cnt)
