import bs4
from urllib.request import urlopen, Request
import urllib


async def check_weather(message):
    weather = message.content.split()
    if len(weather) > 1:
        enc_location = urllib.parse.quote(f"{weather[1]}+날씨")
    else:
        enc_location = urllib.parse.quote("강남+날씨")

    try:
        url = f"https://search.naver.com/search.naver?id=utf8&query={enc_location}"
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, "html5lib")

        response = f"""현재 {soup.find('span', class_='btn_select').find('em').text}의 기온은 {soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text}도 입니다.
{soup.find('p', class_='cast_txt').text}"""
    except Exception as e:
        print(e)
        response = "해당 지역의 날씨정보를 불러올 수 없습니다."

    await message.channel.send(response)
