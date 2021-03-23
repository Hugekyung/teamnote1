n = int(input())
words = []
for _ in range(n):
    word = input()
    word_count = len(word)
    words.append((word, word_count))
words = list(set(words)) # 중복 단어 제거 후 사전 순 정렬
words.sort(key= lambda word: (word[1], word[0])) # 단어 길이 > 단어 사전 순 정렬

for word in words:
    print(word[0])