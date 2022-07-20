number = int(input())
for i in range(0,number):
    P, Q, R, S, W = map(int, input().split())
    result_A = P * W
    if W<= R:
        result_B = Q
    elif W > R:
        result_B = Q+((W-R)*S)
    print("#%d" % (i + 1), end=' ')
    if result_A > result_B:
        print(result_B)
    elif result_A < result_B:
        print(result_A)