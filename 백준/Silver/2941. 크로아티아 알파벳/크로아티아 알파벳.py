change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()

for i in change :
    n = n.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(n))