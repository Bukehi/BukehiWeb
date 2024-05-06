import time
import subprocess

subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', '"upgrade commit"'])
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
        print(f"正在进行第{i}/8次重连")


time.sleep(10)
