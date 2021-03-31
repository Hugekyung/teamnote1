# Softeer 모의 코테 문제(출력예제는 맞음)

n, k = map(int, input().split())
line = list(input())

pick = 0 # 부품을 집은 로봇 수
ph_list = [0 for _ in range(n)]

for i,v in enumerate(line):
    if v == 'P' and ph_list[i] == 0: # 로봇을 찾으면
        #print("{}번째 인덱스에 로봇이 있다".format(i))
        if i-k <= 0: # idx가 0보다 작거나 같을 경우 0으로 설정
            idx = 0
        else:
            idx = i-k
        print(idx)
        
        try: # 여기에 문제가 있는데,,,????
            while idx <= i+k: # 범위를 벗어나기 전까지 idx+1하며 반복
                if line[idx] == 'H' and ph_list[idx] == 0:
                    #print("여기11111")
                    ph_list[idx] = 1 # 집어진 부품 표시
                    ph_list[i] = 2
                    pick += 1
                    break # 한 개 집으면 멈춘다
                else:
                    #print("여기22222")
                    idx += 1
        except:
            pass
    #print("현재까지 로봇 수: {}개".format(pick))
#print(line)
#print(ph_list)
print(pick)