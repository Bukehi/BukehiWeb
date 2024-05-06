import requests
from bs4 import BeautifulSoup
import pdfkit


def html_to_pdf(html, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_file(html, to_file, configuration=config)
    print('完成')


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

url = "https://www.zhihu.com/explore"
resp = requests.get(url, headers)
soup = BeautifulSoup(resp.text, 'html.parser')
a = soup.find_all('a', class_="css-1u3u1p5")
j = 0
for i in a:
    j += 1
    link = i.get('href')
    html = requests.get(link)
    with open(f'./zhihu/html{j}.html', 'w') as h:
        h.write(html.text)
    html_to_pdf(f'html{j}.html', f'pdf{j}.pdf')
end = input("")
