from ex import resou, rmrb, weather
from datetime import datetime
import time
import requests
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('./date.ini')
upgradedate = config['date']['upgradedate']
date = str(datetime.now())[:10]

if not upgradedate == date:
    rmrb_bool = rmrb.rmrb()
    if rmrb_bool:
        config.set('date', 'upgradedate', date)
        with open('./date.ini', 'w', encoding='utf-8') as f:
            config.write(f)
# 创建内容
content_1 = resou.baidu()
content_2 = weather.getlocalweather()
now = str(datetime.now())
now = now[0:19]
gaokao = datetime(2024, 6, 7)
dates = (gaokao-datetime.now()).days

# 写入文件
head = "本内容的收集整理及封装技术由Bukehi提供\n"
with open('./livefile/热搜.txt', 'w', encoding='utf-8') as f:
    f.write(head + f"距高考还有{dates}天\n该内容更新于 {now}\n" + f"{content_2}\n"
            "百度热搜\n" + content_1)
config.set('date', 'upgradedate', date)
with open('./date.ini', 'w', encoding='utf-8') as f:
    config.write(f)

time.sleep(10)