n = int(input())
group_num = 0
for _ in range(n):
    word = input()
    word_len = len(word)
    word_uni = set(word)
    if len(word_uni) == word_len or len(word_uni) == 1:
        group_num += 1
    else:
        for i in range(word_len):
            try:
                if word[i] != word[i+1] and word[i] in word[i+2:]:
                    break
                elif word[i] == word[i+1] or word[i] != word[i+1]:
                    continue
                else:
                    group_num += 1
                    break
            except:
                pass
print(group_num)