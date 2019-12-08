#!/usr/bin/python3
import asyncio
import discord
from dotenv import load_dotenv
import random
import os
from urllib.request import urlopen, Request
import urllib
import bs4
import time

load_dotenv()
token = os.getenv('DISCORD_TOKEN_TEST')

client = discord.Client()

dance = False

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'삐까삐까? (대충{member.name}를 환영한다는 의미)'
    )

@client.event
async def on_message(message):
    msg = message.content.split(' ')

    if message.author == client.user:
        return

    print(client.user.name)
    if msg[0] == client.user.name:
        if msg[1] == '백만볼트':
            await message.channel.send('끠까 츄!!!!!!!!!!!!!!')
            if random.randint(1,5) == 3:
                await message.channel.send('오마에와 모 신데이루')
                if random.randint(1,10) == 3:
                    await message.channel.send('나아ㅏㅏ니이~~~~~')
            elif random.randint(1,5) == 2:
                await message.channel.send('귀찮네..')
            elif random.randint(1,5) == 5:
                await message.channel.send('나는 나보다 약한녀석따위의 말을 듣지 않는다.')

        if msg[1] == '전광석화':
            await message.channel.send('피까피까!!')
            if random.randint(1,5) == 3:
                await message.channel.send('슥슥 슥슥')
                if random.randint(1,10) == 3:
                    await message.channel.send('FLEX')
        if msg[1] == '물어':
            await message.channel.send('ㅗ')
            if random.randint(1,5) == 3:
                await message.channel.send('ㅋ')
        
        if msg[1] == '진화!':
            await message.channel.send('네 저는 이제 라이츕니다. ㅅㄱㅂ')
            time.sleep(2)
            if random.randint(1,10) > 4:
                await(message.channel.send('ㅎㅇ 진화에 성공했따.'))
                client.user.name = '라이츄'
                client.__setattr__.display_name = '라이츄'
            else:
                await(message.channel.send('ㅅㄱ 진화에 실패했따.'))
                await(message.channel.send('-노오력이 부족하다-'))
        if msg[1] == '너프':
            await message.channel.send('네 저는 이제 피카츕니다. ㅎㅇ')
            client.user.name = '피카츄'
            client.__setattr__.display_name = '피카츄'
        
    if msg[0] == '두둠칫':
        global dance
        if dance is True:
            dance = False
        else:
            dance = True
            while dance:
                await message.channel.send('(ว˙∇˙)ง')
                time.sleep(0.5)
                await message.channel.send('(ง˙∇˙)ว')
                time.sleep(0.5)


client.run(token)

