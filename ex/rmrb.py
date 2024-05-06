from bs4 import BeautifulSoup
from tqdm import tqdm
from PyPDF2 import PdfWriter
import requests
import datetime
import os
import time


def rmrb():
    now_with_ = datetime.datetime.now().strftime("%Y-%m/%d")
    now_without_ = datetime.datetime.now().strftime("%Y%m%d")
    res = requests.get(
        f'http://paper.people.com.cn/rmrb/html/{now_with_}/nbs.D110000renmrb_01.htm')
    soup = BeautifulSoup(res.text, 'html.parser')
    ranges = len(soup.find_all('div', {'class': 'swiper-slide'}))

    for i in tqdm(range(1, ranges+1), desc="正在下载："):
        if i < 10:
            value = "0"+str(i)
        elif i >= 10:
            value = str(i)
        url = f'http://paper.people.com.cn/rmrb/images/{now_with_}/{value}/rmrb{now_without_}{value}.pdf'
        resp = requests.get(url)
        for trial in range(0, 9):
            if res.status_code == 200:
                with open(f'./人民日报/人民日报{value}.pdf', 'wb') as file:
                    file.write(resp.content)
                break
            else:
                print(resp.status_code)
                print('网络错误，正在重试')
                continue

    target_path = './人民日报'
    if os.path.isfile('./人民日报/人民日报.pdf'):
        os.remove('./人民日报/人民日报.pdf')
    pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

    file_merger = PdfWriter()
    for pdf in tqdm(pdf_lst, desc="正在合并"):
        file_merger.append(pdf)
    file_merger.write("./人民日报/人民日报.pdf")

    for i in tqdm(range(1, ranges+1), desc="正在清理缓存："):
        if i < 10:
            value = "0"+str(i)
        elif i >= 10:
            value = str(i)
        os.remove(f"./人民日报/人民日报{value}.pdf")


if __name__ == "__main__":
    rmrb()
    time.sleep(5)
