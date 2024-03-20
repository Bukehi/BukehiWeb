import bs4

with open('BukehiWeb/index.html', 'r', encoding='utf-8') as f:
    html = f
    soup = bs4.BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        print(
            f"""https://officeweb365.101eduyun.com/?ssl=1&furl=https://bukehi.github.io/BukehiWeb{link.get('href')}""")
