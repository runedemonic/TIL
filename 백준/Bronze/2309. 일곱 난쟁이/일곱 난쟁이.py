dwarf = [int(input()) for i in range(9)]
#난쟁이들의 키를 삽입
total = sum(dwarf)
a=0
b=0

for i in range(9):
    for j in range(i+1,9):
        if total - (dwarf[i] + dwarf[j]) == 100:
            a,b = dwarf[i],dwarf[j]
            #가짜 난쟁이들을 찾으면 값을 저장하고
            break

dwarf.remove(a)
dwarf.remove(b)
dwarf.sort()
#배열에서 제거하고 정렬해줌
for i in dwarf:
    print(i)
