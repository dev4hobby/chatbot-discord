from random import randint


async def get_result() -> str:
    result = "앞"
    number = randint(0, 1)
    if number == 0:
        result = "뒤"
    return result