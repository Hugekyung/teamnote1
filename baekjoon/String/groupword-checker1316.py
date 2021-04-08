n = int(input())
count = 0

for _ in range(n):
    word = input()
    if len(set(word)) == 1 or len(set(word)) == len(word):
        count += 1
    else:
        for i in range(len(word)):
            try:
                if word[i] != word[i+1] and word[i] in word[i+2:]:
                    break
                else:
                    continue
            except:
                count += 1
                break
print(count)