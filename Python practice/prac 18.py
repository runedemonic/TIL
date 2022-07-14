from collections import Counter

word =input()
counter = Counter(word)

for i in counter.items():
    print(f'{i[0]} {i[1]}')
