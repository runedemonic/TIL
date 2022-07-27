change = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G','E']
n = input()

for i in change :
    n = n.replace(i, '')  # input 변수와 동일한 이름의 변수
print(n)