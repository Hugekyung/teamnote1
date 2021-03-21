n = int(input())
m_list = []

for m in range(1, n):
    total = m
    for i in str(m):
        total += int(i)
    if total == n:
        m_list.append(m)

if not m_list:
    print(0)
else:
    print(min(m_list))