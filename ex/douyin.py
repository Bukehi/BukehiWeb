# -*- coding: utf-8 -*-
import http.client
import urllib
import json
import time


def douyin():
    conn = http.client.HTTPSConnection('apis.tianapi.com')  # 接口域名
    params = urllib.parse.urlencode(
        {'key': 'e9aaa8a03ba4cb9aab841671e091ab2f'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/douyinhot/index', params, headers)
    tianapi = conn.getresponse()
    result = tianapi.read()
    data = result.decode('utf-8')
    dict_data = json.loads(data)
    content = ""
    j = 0
    for i in dict_data["result"]["list"]:
        j += 1
        content = content + str(j) + ". " + f"{i['word']}\n"
    print(content)
    return content


if __name__ == "__main__":
    content_1 = douyin()
    time.sleep(3)
