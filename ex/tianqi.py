import requests


def tianqi():
    url = 'https://weather.cma.cn/'
    res = requests.get(url)
    print(res)
    print(res.text)

    if __name__ == "__main__":
        tianqi()
