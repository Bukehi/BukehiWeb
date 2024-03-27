# -*- coding: utf-8 -*-
import http.client
import urllib
import json


def one():
    conn = http.client.HTTPSConnection('apis.tianapi.com')  # 接口域名
    params = urllib.parse.urlencode(
        {'key': 'e9aaa8a03ba4cb9aab841671e091ab2f'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/one/index', params, headers)
    tianapi = conn.getresponse()
    result = tianapi.read()
    data = result.decode('utf-8')
    dict_data = json.loads(data)
    content = dict_data["result"]['word']
    return content


if __name__ == "__main__":
    content = one()
    print(content)
