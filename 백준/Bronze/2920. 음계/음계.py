n = input().split(' ')
result = ''.join(n)
if result == '12345678':
    print('ascending')
elif result == '87654321':
    print('descending')
else:
    print('mixed')