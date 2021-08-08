from random import randint


async def get_result() -> str:
    result = "ㅇㅇ"
    number = randint(0, 1)
    if number == 0:
        result = "ㄴㄴ"
    return result
