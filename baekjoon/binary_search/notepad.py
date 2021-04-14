x = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
t = [10, 9, -5, 2, 3, 4, 5, -10]
from collections import Counter
counter = Counter(x)
print(counter)
for i in t:
    print(counter[i])