import requests


def getlocalweather():
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    key = '305352a281cda8c6a698836d63e13076'
    data = {'key': key, "city": 131002}
    req = requests.post(url, data)
    info = dict(req.json())
    info = dict(info)
    # print(info)
    newinfo = info['lives'][0]
    # print(newinfo)
    # print("你查询的当地天气信息如下：")
    # print("省市：", newinfo['province']+newinfo['city'])
    # print("城市：", newinfo['city'])
    # print("编码：", newinfo['adcode'])
    # print("天气：", newinfo['weather'])
    # print("气温：", newinfo['temperature']+'℃')
    # print("风向：", newinfo['winddirection'])
    # print("风力：", newinfo['windpower'])
    # print("湿度：", newinfo['humidity'])
    # print("报告时间：", newinfo['reporttime'])
    content = f'''    河北省廊坊市 安次区     天气：{newinfo['weather']}
    气温：{newinfo['temperature']}℃  风向：{newinfo['winddirection']}  风力：{newinfo['windpower']}  湿度：{newinfo['humidity']}
    报告时间：{newinfo['reporttime']}'''
    print(content)
    return content


if __name__ == "__main__":
    getlocalweather()
