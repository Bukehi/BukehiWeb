from tkinter import filedialog
import tkinter
import re
import os

root=tkinter.Tk()
root.withdraw()

r = 'r'
start = input('输入回车开始解析：')
os.system('cls')

while r=="r":
    while True:
        file_path = filedialog.askopenfilename(title="选择文件",filetypes=[('HTML','.html'),('TXT','.txt')])
        if not file_path:
            print("您没有选择文件，请重新选择！")
            continue
        break

    with open(file_path,'r',encoding='utf-8') as f:
        html=f.read()

    match=r'discuss/\d{4}/.+?\.mp4'
    result=re.findall(match,html)
    for link in result:
        if ".mp3" in link:
            continue
        print("https://www.101eduyun.com/sunrise/common/attachment/viewAttachment.do?vPath=" + link)

    match_2=r'\.mp4&#39;,&#39;.+?\.mp4'
    result_2=re.findall(match_2,html)
    for name in result_2:
        name=name.replace('.mp4&#39;,&#39;','')
        name=name.replace('.mp4','')
        print(name)
    r=input('')
    os.system('cls')
