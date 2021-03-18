sugar = int(input())

# 아직 못풀었어!!!
# bag = 0
# while True:
#     if sugar % 5 == 0:
#         bag += (sugar // 5)
#         print(bag)
#         break
#     sugar -= 3
#     bag += 1
#     if sugar < 0:
#         print(-1)

def Sugar(sugar):
    for x in range((sugar//3)+1):
        for y in range((sugar//5)+1):
            if (3*x + 5*y) == sugar:
                return (x+y)
    return -1
            
                