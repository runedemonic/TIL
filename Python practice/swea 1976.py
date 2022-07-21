number = int(input())

for i in range(0,number):
    h,m ,h1,m1 = map(int, input().split())
    result_m = (m + m1)%60
    result_h = (h + h1+ (m+m1)//60)%12
    if result_h == 0:
        result_h = 12
    print("#%d" % (i + 1), end=' ')
    print(f'{result_h} {result_m}')
