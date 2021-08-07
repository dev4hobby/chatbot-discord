from modules.gotcha import get_result
from modules.decide import get_answer
from modules.shake import shake_your_body
from modules.weather import check_weather
from modules.russian_roulette import Gun

gun = Gun()


async def dynamic_message_handler(message, client):
    status = True
    if message.author == client.user:
        return status

    if message.content.startswith("갓챠"):
        await message.channel.send("50:50 너의 운빨은-")
        await message.channel.send(await get_result())

    elif message.content.startswith("단호박"):
        await message.channel.send(await get_answer())
    elif message.content.startswith("둠칫"):
        await shake_your_body(message)
    elif message.content.startswith("날씨"):
        await check_weather(message)
    elif message.content.startswith("발사"):
        await message.channel.send(gun.action())
    else:
        status = False
    return status


async def static_message_handler(message, response):
    await message.channel.send(response)


async def image_message_handler(message, _file):
    await message.channel.send(file=_file)
