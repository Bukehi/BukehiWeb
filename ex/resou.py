from bs4 import BeautifulSoup
import requests


def baidu():
    url_baidu = 'https://top.baidu.com/board?tab=realtime'
    resp = requests.get(url_baidu)
    soup = BeautifulSoup(resp.text, 'html.parser')
    alltitle = soup.find_all('div', attrs={'class': 'c-single-text-ellipsis'})
    allcontent = soup.find_all(
        'div', class_=['small_Uvkd3'])
    # print(len(alltitle))
    # print(len(allcontent))
    contents = ''
    i = 1
    for title, content in zip(alltitle, allcontent):
        # print(title.string)
        # print(content.get_text())
        contents += f"{i}. "+title.string + '\n' + content.get_text()+'\n'
        i += 1
    print(contents)
    return contents


if __name__ == '__main__':
    baidu()
