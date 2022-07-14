S = input()
word = list("aeiou")
count = 0
for alpha in S:
    if alpha in word:
        count += 1
print(count)