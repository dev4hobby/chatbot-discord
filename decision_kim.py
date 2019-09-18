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
token = os.getenv('DISCORD_TOKEN')

bullet = random.randint(1,6)
shot = list()
dance = False
normal_boss = 50.0
world_boss = 50.0
normal_user = 30.0
world_user = 30.0
level = 1
atk = 0.4
meal_count = 0


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'안뇽! 어서와ㅏㅏ {member.name}!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
   
    if message.content[0:6] == ';;play' or message.content[0:3] == ';;p':
        keyword = message.content.split()
        result = ''
        if len(keyword) == 2:
            result = '_['+keyword[1]+']\n'
        elif len(keyword) > 2:
            keyword = [key for key in keyword if key]
            for i in range(1, len(keyword)):
                result += (keyword[i]+' ')
        song_list = open('SongList', 'a')
        song_list.write(result)
        song_list.close()


    if message.content[0:3] == '김결정' and message.content[-1] == '?':
        if random.randint(0,1) == 1:
            response = 'ㅇㅇ'
        else:
            response = 'ㄴㄴ'
        await message.channel.send(response)

    if message.content[0:5] == '!아까그곡':
        result = ''
        max_len = 5
        command = message.content.split()
        try:
            song_fd = open('SongList', 'r')
            song_list = song_fd.read().split('\n')
            song_list = [song for song in song_list if song]
            song_list.reverse()
            song_fd.close()
            if len(command) == 1:
                if len(song_list) < 5:
                    max_len = len(song_list)
                for i in range(max_len):
                    result += (str(song_list[i])+'\n')
            else:
                try:
                    max_len = int(command[1])
                except Exception as e:
                    result = '요청하신 만큼의 노래가 재생되지 않았습니다.\n'
                    max_len = 5

                if len(song_list) < max_len:
                    max_len = len(song_list)

                for i in range(max_len):
                    result += (str(song_list[i])+'\n')

        except Exception as e:
            result = '이전에 재생된 곡이 없거나 잘못된 요청입니다.\n'

        await message.channel.send(result)


    if message.content == '!주사위':
        global world_boss
        global level
        global atk
        dice = list()
        for i in range(2):
            dice.append(random.randint(1,6))
        total_dice = sum(dice)
        response = '[ '+str(dice[0])+', '+str(dice[1])+' ]'+'\n합은 '+str(total_dice)+' 입니다.'
        await message.channel.send(response)
        world_boss -= (total_dice * atk)
        seed = random.randint(1,level)
        if world_boss < 0.0:
            level+=1
            world_boss = normal_boss * seed - (0.1 * seed)
            normal_boss = world_boss
            atk += seed*0.1
        await message.channel.send('월드레벨: '+str(level)+'\n보스 HP: '+str(world_boss)+'\n')  
        
    if message.content == '!둠칫둠칫':
        global dance
        if dance is True:
            dance = False
        else:
            dance = True
            while dance:
                await message.channel.send('))')
                time.sleep(0.5)
                await message.channel.send('((')
                time.sleep(0.5)
                

    if message.content.find('!발사') == 0:
        global shot
        global bullet
        fire = random.randint(1,6)
        print(bullet, fire)
        while fire in shot:
            fire = random.randint(1,6)
            print(fire)
        print(fire)
        if fire == bullet:
            response = 'Boom!\n-사망-\n게임에서 탈락하셨습니다.'
            shot = list()
            bullet = random.randint(1,6)
        else:
            shot.append(fire)
            response = 'click!\n-생존-\n다음 플레이어를 기다려주세요.\n확률 1/'+str(6-len(shot))
        print(shot)
        await message.channel.send(response)

    if message.content == '!러시안룰렛':
        await message.channel.send('https://youtu.be/QslJYDX3o8s')
    
    if message.content[0:3] == '!날씨':
        weather = message.content.split()
        if len(weather) > 1:
            enc_location = urllib.parse.quote(weather[1]+'+날씨')
        else: #if len(weather) == 1: or lower then 1
            enc_location = urllib.parse.quote('판교+날씨')

        try:
            url = 'https://search.naver.com/search.naver?ie=utf8&query='+enc_location 
            req = Request(url)
            page = urlopen(req)
            html = page.read()
            soup = bs4.BeautifulSoup(html, 'html5lib')
        
            await message.channel.send('현재 '
                +soup.find('span', class_='btn_select').find('em').text
                +'의 기온은 '
                +soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
                +'도 입니다.\n'
                +soup.find('p', class_='cast_txt').text+'\n')
        except Exception as e:
            await message.channel.send('죄송합니다. 관련 정보가 없습니다.\n감사합니다.\n')
    
    if message.content == '안녕하살법!':
        await message.channel.send('안녕하살법 받아치기!\n')

    if message.content == '너무해!':
        await message.channel.send('너무해! ᕙ(•̀‸•́‶)ᕗ \n너무해! ᕙ(•̀‸•́‶)ᕗ \n')

    if message.content == '배고파' or message.content == '배고파!' :
        result = random.randint(0,1)
        if result == 1:
            await message.channel.send('밥먹어.\n')
        else:
            await message.channel.send('굶어.\n')
    if message.content == '밥해줘' or message.content == '밥해줘!' :
        global meal_count
        result = random.randint(0,4)
        msg = ''
        okflag = False

        if result == 0:
            msg = '시켜먹어'
        elif result == 1:
            msg = '해먹어'
        elif result == 2:
            msg = '^^ㅗ'
        elif result == 3:
            msg = '시러'
        else:
            okflag = True
            msg = '알겠어'

        if meal_count > 5:
            await message.channel.send('작작해 ㅡ_ㅡㅗ')
            meal_count = 0
        else:
            meal_count+=1
            await message.channel.send(msg)

            if okflag:
                time.sleep(0.5)
                await message.channel.send('음.. 역시 안되겠다. 알아서먹어')
   
    if message.content.find('이시국에') >= 0 or message.content.find('킹시국에') >= 0 or message.content.find('갓시국에') >= 0:
        await message.channel.send('이시국씨 이제 그만 들어가세요.')
    if message.content.find('올란바토르') == 0 :
        await message.channel.send('???: Aㅏ~~')
    if message.content.find('초코우유') >= 0:
        await message.channel.send('근본은 덴마크지...')
    if message.content.find('독일') >= 0:
        await message.channel.send('이봐.. 젊은이....')
    if message.content.find('연어') >= 0:
        await message.channel.send('노르웨이산 연어가 단돈 x000원')
    
    if message.content == '망고나와라!':
        result = '그러게요.. 뭐하고있을까요..'
        await message.channel.send(result)

    if message.content == '도움!':
        result = '`김결정 ~?` : 선장들을 위한 완벽한 친구.\n`!아까그곡` : FredBoat이 재생한 노래를 기억해뒀다가 알려줘요.\n`!주사위` : 주사위를 굴려 월드보스를 조져보세용\n`!둠칫둠칫` : 김결정이 자동으로 춤을 춰줍니다.\n`!발사` : 러시안룰렛. 당신의 운을 시험해보세요.\n`!날씨 ${지역}` : 지역별 날씨를 알려줍니다.\n\n`안녕하살법!`, `배고파`, `밥해줘`, `너무해!`, `초코우유`'
        await message.channel.send(result)


client.run(token)

