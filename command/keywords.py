from .deprecated import keywords_match

keyword_find = {
    '초코우유' : '근본은 덴마크죠? 그쵸?',
    '독일' : '이보게.. 젊은이...',
    '연어' : '노르웨이산 연어가 두팩에 단돈 19,800원!',
}

def find_multi(message):
    try:
        target = message.content.split()
    except Exception as e:
        return None
    try:
        return keyword_find[target[0]]
    except Exception as e:
        return None