#!/usr/bin/python3
import asyncio
import discord
import settings
import time

from command import (please_make_decision,
                     russian_roulette,
                     weather,
                     hungry,
                     keywords)

token = settings.TOKEN

client = discord.Client()
russian_roulette = russian_roulette.Game()
weather = weather.Now()
hungry = hungry.MealTime()

@client.event
async def on_ready():
    '''
    누군가 들어왔다? Logging하는 부분
    '''
    response = client.user.name + ' 님이 들어오셨어요!'
    print(response)
    
@client.event
async def on_member_join(member):
    '''
    유저가 접속하였을 때 dm으로 메시지를 보내는 기능
    '''
    await member.create_dm()
    await member.dm_channel.send(
        f'안뇽! 어서와ㅏ {member.name}!'
    )

@client.event
async def on_message(message):
    '''
    채널에 입력된 메시지를 parsing 하여 무언가 처리하고싶으면
    여기서 분기를 생성하면 됨.
    '''

    print('message log >> {}'.format(message.content))
    # 결정이 혼자놀기 Loop-back
    if message.author == client.user:
        # 여기서는 아무것도 하지 않는다.
        return

    # 김결정 ~ ?  에 반응한다. 
    # 예시 : 김결정 나 이거 할까? >> [ㅇㅇ , ㄴㄴ]
    if message.content[0:3] == '김결정' and message.content[-1] == '?':
        response = please_make_decision.action()
        await message.channel.send(response)

    # !둠칫둠칫 을 입력하면 반응한다.
    # 설정한 간격마다 (( )) 를 뿌려주면서 트월킹을한다. 요망한자식
    if message.content == '!둠칫둠칫':
        if settings.DANCE is True:
            settings.DANCE = False
        else:
            settings.DANCE = True
            while settings.DANCE:
                await message.channel.send('))')
                time.sleep(0.5)
                await message.channel.send('((')
                time.sleep(0.5)
                
    # !발사 입력하면 반응한다.
    # 러시안 룰렛을 진행한다.
    if message.content.find('!발사') == 0:
        response = russian_roulette.action()
        await message.channel.send(response)

    # !날씨 (지역) 입력하면 반응한다.
    if message.content[0:3] == '!날씨':
        response = weather.check_param(message)
        await message.channel.send(response)
    
    # 배고파 혹은 배고파! 라고 입력하면 반응한다.
    if message.content == '배고파' or message.content == '배고파!' :
        response = hungry.ask()
        await message.channel.send(response)

    # 밥해줘 혹은 밥해줘! 라고 입력하면 반응한다.
    if message.content == '밥해줘' or message.content == '밥해줘!' :
        response = hungry.please_feed_me()
        await message.channel.send(response)

    # 다른 키워드들에 대한 처리를 하는 부분이다.
    # command 의 keywords.py 참조
    other_response = keywords.find_multi(message)
    if other_response:
        await message.channel.send(other_response)


# 최종적으로 김결정을 실행하는 부분이다.
client.run(token)
