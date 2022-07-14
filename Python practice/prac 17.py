word = input()
result = []

for i in word:
    result.append(chr(ord(i) - 32) if 97 <= ord(i) <= 122 else i)

print("".join(result))