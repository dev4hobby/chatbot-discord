import json
from discord.ext import commands
from discord import File
from functions.handler import (
    dynamic_message_handler,
    static_message_handler,
    image_message_handler,
)
from functions.initializer import (
    initializer,
)

# from modules.sound import Music
ctx = initializer()
client = commands.Bot(command_prefix=ctx["secrets"].get("MUSIC_PREFIX", "!"))


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")


@client.event
async def on_message(message):
    if message.content.startswith(ctx["secrets"].get("MUSIC_PREFIX", "!")):
        await client.process_commands(message)
    else:
        if ctx["images"].get(message.content):
            await image_message_handler(message, File(ctx["images"][message.content]))
        if ctx["keywords"].get(message.content):
            await static_message_handler(message, ctx["keywords"][message.content])
        else:
            await dynamic_message_handler(message, client)


try:
    # client.add_cog(Music(client))
    client.run(ctx["secrets"].get("DISCORD_TOKEN", None))
except Exception as e:
    print(e)
    print("Check your DISCORD_TOKEN")
