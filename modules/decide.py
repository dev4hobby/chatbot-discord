from random import randint


async def get_answer() -> str:
    answer = "응"
    if randint(0, 100) % 2 == 0:
        answer = "놉"
    return answer
