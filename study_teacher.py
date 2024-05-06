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

    match=r'openTask\(.+\)'
    result=re.findall(match,html)
    for link in result:
        link=link.split("&#39;,&#39;")
        taskId=link[0].replace('openTask(&#39;','')
        userTaskId=link[1]
        libActivityId=link[2].replace('&#39;)','')
        url='https://www.101eduyun.com/sunrise/student/cloudActivity/resource/openTask.do?taskId='+taskId+'&userTaskId='+userTaskId+'&libActivityId='+libActivityId+'&academicYear=2023'
        print(url)

    match_2=r'activitynm=".+?\('
    result_2=re.findall(match_2,html)
    for name in result_2:
        name=name.replace('activitynm="','')
        name=name.replace('(','')
        print(name)
    r=input('')
    os.system('cls')
