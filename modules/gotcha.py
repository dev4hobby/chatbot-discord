from random import randint


async def get_result() -> str:
    result = "한번 더 해봐"
    number = randint(0, 2)
    if number == 0:
        result = "운이 없군. 꽝이야"
    elif number == 1:
        result = "당첨!"
    return result
