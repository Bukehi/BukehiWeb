from ex import weibo, baidu, quanwang
import time
from datetime import datetime
import subprocess

content_1 = weibo.weibo()
content_2 = baidu.baidu()
content_3 = quanwang.quanwang()
now = str(datetime.now())
now = now[0:19]

with open('./livefile/热搜.txt', 'w', encoding='utf-8') as f:
    f.write(f"该内容更新于 {now}\n全网热搜\n" + content_3 + "微博热搜\n" +
            content_1 + "百度热搜\n" + content_2)

subprocess.call(['git', 'add', 'livefile/热搜.txt'])
# subprocess.call(['git', 'add', 'autoupgrade.py'])
subprocess.call(['git', 'commit', '-m', 'upgrade commit'])

for i in range(9):
    result = subprocess.run(['git', 'push', 'school', 'main'],

                            capture_output=True, text=True)
    print(result.stderr)
    if "main -> main" in result.stderr:
        break
    elif "Everything up-to-date" in result.stderr:
        print("已全部上传")
        break
    else:
        print("请检查网络连接…")


time.sleep(10)
