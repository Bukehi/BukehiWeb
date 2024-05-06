import subprocess
import http.client
import urllib
import json
import time

def weibo():
    conn_1 = http.client.HTTPSConnection('apis.tianapi.com')  # 接口域名
    params_1 = urllib.parse.urlencode({'key': 'e9aaa8a03ba4cb9aab841671e091ab2f'})
    headers_1 = {'Content-type': 'application/x-www-form-urlencoded'}
    conn_1.request('POST', '/weibohot/index', params_1, headers_1)
    tianapi_1 = conn_1.getresponse()
    results_1 = tianapi_1.read()
    data_1 = results_1.decode('utf-8')
    dict_data_1 = json.loads(data_1)
    content = ""
    j = 0
    for i in dict_data_1["result"]["list"]:
        j+=1
        content = content + f"{j}.  {i['hotword']}  {i['hotwordnum']}  {i['hottag']}\n"
    print(content)
    return content

if __name__ == "__main__":
    content=weibo()
    time.sleep(3)