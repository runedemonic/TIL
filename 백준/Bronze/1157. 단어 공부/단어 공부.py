import collections

a = input()
result=list(a.upper()) #모든 문자를 대문자로 변환
cnt=collections.Counter(result) #모든 문자의 개수 세기
all_v = cnt.values()

overlap = 0     #중복 검사

for v in all_v:
    if v == max(all_v): #최대값이 여러개인지 검사
        overlap += 1
        
max_key = max(cnt,key=cnt.get) #최대값 저장

if overlap > 1:
    print('?')      #최대값이 여러개일시 ? 출력
else:
    print(max_key)  # 최대값의 key출력
