import requests
from bs4 import BeautifulSoup
#from cwb_town_id import town_name_cvt2_id

def get_weather_today_day(town_id, day):
    url = "https://www.cwb.gov.tw/V8/C/W/Town/MOD/Week/{}_Week_PC.html?".format(town_id) # 6300100臺北市松山區
    res=requests.get(url)
    soup=BeautifulSoup(res.text, "html.parser")

    i = day
    day = soup.find('th',id="PC7_D{}".format(i)).text # 日期&星期
    dayMaxT = soup.find('td', headers="PC7_MaxT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天最高溫
    dayMinT = soup.find('td', headers="PC7_MinT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天最低溫
    dayMaxAT = soup.find('td', headers="PC7_MaxAT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天體感最高溫
    dayMinAT = soup.find('td', headers="PC7_MinAT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天體感最低溫
    dayWx = soup.find('td', headers="PC7_Wx PC7_D{} PC7_D{}D".format(i,i)).find('img')['title'] # 白天天氣現象
    dayPoP = soup.find('td', headers="PC7_Po PC7_D{} PC7_D{}D".format(i,i)).text # 白天降雨機率
    uvi = soup.find('td', headers="PC7_UVI PC7_D{} PC7_D{}D".format(i,i)).find('strong').text # 紫外線
    uviR = soup.find('td', headers="PC7_UVI PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 紫外線量級

    info_weather_today_day = "{}\n氣溫{}~{}℃\n體感溫度 {}~{}℃\n降雨機率 {}\n紫外線 {} {}".format(dayWx, dayMaxT, dayMinT, dayMaxAT, dayMinAT, dayPoP, uvi, uviR)
    print(day)
    print(info_weather_today_day)
    print("====================")
    return info_weather_today_day

def get_weather_today_night(town_id, day):
    url = "https://www.cwb.gov.tw/V8/C/W/Town/MOD/Week/{}_Week_PC.html?".format(town_id) # 6300100臺北市松山區
    res=requests.get(url)
    soup=BeautifulSoup(res.text, "html.parser")

    i = day
    day = soup.find('th',id="PC7_D{}".format(i)).text # 日期&星期
    nightMaxT = soup.find('td', headers="PC7_MaxT PC7_D{} PC7_D{}N".format(i,i)).find('span').text # 晚上最高溫
    nightMinT = soup.find('td', headers="PC7_MinT PC7_D{} PC7_D{}N".format(i,i)).find('span').text # 晚上最低溫
    nightMaxAT = soup.find('td', headers="PC7_MaxAT PC7_D{} PC7_D{}N".format(i,i)).find('span').text # 晚上體感最高溫
    nightMinAT = soup.find('td', headers="PC7_MinAT PC7_D{} PC7_D{}N".format(i,i)).find('span').text # 晚上體感最低溫
    nightWx = soup.find('td', headers="PC7_Wx PC7_D{} PC7_D{}N".format(i,i)).find('img')['title'] # 晚天天氣現象
    nightPoP = soup.find('td', headers="PC7_Po PC7_D{} PC7_D{}N".format(i,i)).text # 晚上降雨機率
    
    info_weather_today_night = "{}\n氣溫{}~{}℃\n體感溫度 {}~{}℃\n降雨機率 {}".format(nightWx, nightMaxT, nightMinT, nightMaxAT, nightMinAT, nightPoP)
    print(day)
    print(info_weather_today_night)
    print("====================")
    return info_weather_today_night

def get_weather_tomorrow_day(town_id, day):
    url = "https://www.cwb.gov.tw/V8/C/W/Town/MOD/Week/{}_Week_PC.html?".format(town_id) # 6300100臺北市松山區
    res=requests.get(url)
    soup=BeautifulSoup(res.text, "html.parser")
    
    i = day + 1
    day = soup.find('th',id="PC7_D{}".format(i)).text # 日期&星期
    dayMaxT = soup.find('td', headers="PC7_MaxT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天最高溫
    dayMinT = soup.find('td', headers="PC7_MinT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天最低溫
    dayMaxAT = soup.find('td', headers="PC7_MaxAT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天體感最高溫
    dayMinAT = soup.find('td', headers="PC7_MinAT PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 白天體感最低溫
    dayWx = soup.find('td', headers="PC7_Wx PC7_D{} PC7_D{}D".format(i,i)).find('img')['title'] # 白天天氣現象
    dayPoP = soup.find('td', headers="PC7_Po PC7_D{} PC7_D{}D".format(i,i)).text # 白天降雨機率
    uvi = soup.find('td', headers="PC7_UVI PC7_D{} PC7_D{}D".format(i,i)).find('strong').text # 紫外線
    uviR = soup.find('td', headers="PC7_UVI PC7_D{} PC7_D{}D".format(i,i)).find('span').text # 紫外線量級

    info_weather_tomorrow_day = "{}\n氣溫{}~{}℃\n體感溫度 {}~{}℃\n降雨機率 {}\n紫外線 {} {}".format(dayWx, dayMaxT, dayMinT, dayMaxAT, dayMinAT, dayPoP, uvi, uviR)
    print(day)
    print(info_weather_tomorrow_day)
    print("====================")
    return info_weather_tomorrow_day