def DFS(L):
    global res
    # 종료조건
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            # 세 사람의 총액이 서로 다른지 확인해주는 방법 set 자료구조를 활용해서 같은 것은 리스트에서 제외시켜줄 수 있음
            tmp = set()
            for x in money:
                tmp.add(x)
                # 총액이 다르지 않다면 3개의 자료가 나올 것이다.
            if len(tmp) == 3:
                res = cha
    else:
        # 가지 뻗기
        for i in range(3):
            money[i] += cv[L]
            DFS(L+1)
            # 그 전상황으로 백트래킹 하기 그래야 모든 가지를 순회할 수 있음, 백트래킹 할떄 돈을 더했던 것도 취소해야함.
            money[i] -= cv[L]
            # DFS(L-1) 을 안해주는 이유?


if __name__ == "__main__":
    # 동전의 개수를 입력 받는다.
    n = int(input())
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
