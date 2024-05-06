from ex import resou, one, rmrb, weather
from datetime import datetime
import time
import configparser
import subprocess

# 读取配置文件
config = configparser.ConfigParser()
config.read('./date.ini')
upgradedate = config['date']['upgradedate']
date = str(datetime.now())[:10]

if not upgradedate == date:
    rmrb.rmrb()
# 创建内容
one = one.one()
content_1 = resou.baidu()
content_2 = weather.getlocalweather()
now = str(datetime.now())
now = now[0:19]
gaokao = datetime(2024, 6, 7)
dates = (gaokao-datetime.now()).days

# 写入文件
head = "本内容的收集整理及封装技术由Bukehi提供\n"
with open('./livefile/热搜.txt', 'w', encoding='utf-8') as f:
    f.write(head + f"{one}\n距高考还有{dates}天\n该内容更新于 {now}\n" + f"{content_2}\n"
            "百度热搜\n" + content_1)
if upgradedate == date:
    subprocess.call(['git', 'add', 'livefile/热搜.txt'])
    subprocess.call(['git', 'add', '人民日报/人民日报.pdf'])
    # subprocess.call(['git', 'add', 'autoupgrade.py'])
    subprocess.call(['git', 'commit', '-m', 'upgrade commit'])

    for i in range(9):
        result = subprocess.run(['git', 'push', 'origin', 'main'],

                                capture_output=True, text=True)
        print(result.stderr)
        if "main -> main" in result.stderr:
            break
        elif "Everything up-to-date" in result.stderr:
            print("已全部上传")
            break
        else:
            print("请检查网络连接…")
else:
    config.set('date', 'upgradedate', date)
    with open('./date.ini', 'w', encoding='utf-8') as f:
        config.write(f)
    print("请手动压缩人民日报.pdf后再上传")


time.sleep(10)
