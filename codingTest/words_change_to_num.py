""" 2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어 """

import re

def solution(s):
    word_list = [('zero', 0), ('one', 1), ('two', 2), ('three', 3), ('four', 4), 
                 ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]
    
    try:
        if int(s):
            return int(s)
    except:
        for word in word_list:
            s = re.sub(word[0], str(word[1]), s)
        return int(s)