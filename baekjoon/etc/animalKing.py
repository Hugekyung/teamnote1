'''엘리스 AI 트랙 문제 - 동물의 왕
여러분, 제가 아주 공평한 제안을 하겠습니다. 먼저 여러분께 1번부터 100번까지 무작위로 번호를 나눠드릴 테니 모두 순서대로 원 위에 서주세요. 저는 1번 동물에게 막대기를 드리겠습니다. 막대기를 받은 동물이 다음 동물(2번)을 막대기로 찌르면 그 동물은 원 밖으로 나가고, 막대기는 그다음 동물(3번)에게 전달됩니다. 그렇게 마지막 한 분이 남을 때까지 반복하는 거죠.
자, 그럼 2번분은 나가주세요. 그리고 4번분…'''

animals = list(range(1, 101))
stickmanidx = 0
while len(animals) > 1:
    loser_idx = (stickmanidx + 1) % len(animals)
    print('loser_idx >> ', stickmanidx+1, '%', len(animals), '=', loser_idx)
    animals.pop(loser_idx)
    print(len(animals))
    stickmanidx = loser_idx

print(animals)