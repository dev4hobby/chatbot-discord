from time import sleep
from random import randint
from functions.initializer import DANCE


async def shake_your_body(message):
    global DANCE
    DANCE = not DANCE
    while DANCE:
        await message.channel.send("))")
        sleep(0.5)
        await message.channel.send("((")
        sleep(0.5)
