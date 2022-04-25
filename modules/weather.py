import bs4
from urllib.request import urlopen, Request
import urllib


async def check_weather(message):
    weather = message.content.split()
    static_weather = urllib.parse.quote("날씨")

    if len(weather) > 1:
        enc_location = urllib.parse.quote(f"{weather[1]}") + f"+{static_weather}" 
    else:
        enc_location = urllib.parse.quote(f"강남구") + f"+{static_weather}"

    try:
        url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={enc_location}&oquery={static_weather}&tqi=hEj1pwp0JXoss7YFECCssssssfw-143894"
        print(url)
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, "html5lib")

        location = soup.find("div", class_="title_area _area_panel").find('h2', class_="title").getText()
        celsius = soup.find('div', class_='temperature_text').find('strong').getText()
        response = f"""현재 {location}의 {celsius} 입니다."""
        response = response.replace("현재 온도", "현재 온도는 ")
    except Exception as e:
        print(e)
        response = "해당 지역의 날씨정보를 불러올 수 없습니다."

    
    await message.channel.send(response)
