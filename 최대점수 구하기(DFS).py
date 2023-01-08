def DFS(L, sum, time):
    global res
    # 지정 시간 초과시 그냥 DFS 종료
    if time > m:
        return
    # 가지 뻗기
    if L == n:
        # 결과값을 계속 누적해서 받으면은 그 값과 res 비교해서 최대값으로 계속 초기화 해준다.
        if sum > res:
            res = sum
    # 가지 뻗을 수 있는 경우, 없는 경우
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)



if __name__ == "__main__":
    n, m = map(int, input().split())
    # 점수를 기록
    pv = list()
    # solve 시간 기록
    pt = list()
    # n 개의 문제의 점수와 시간을 입력받음 각리스트에 넣어줌.
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    # 최대 점수 출력해야하므로 res 는 최솟값으로
    res = -21470000000
    DFS(0, 0, 0)
    print(res)
