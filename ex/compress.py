from selenium.webdriver.edge.options import Options
from selenium import webdriver
import win32gui
import win32con


edge_options = Options()
# 使用无头模式
edge_options.add_argument('--headless')
# 禁用GPU，防止无头模式出现莫名的BUG
edge_options.add_argument('--disable-gpu')

# 将参数传给浏览器
browser = webdriver.Edge(options=edge_options)

# 启动浏览器
url = "https://www.ilovepdf.com/zh-cn/compress_pdf"
browser.get(url)
print(browser.title)

# 关闭浏览器
browser.quit()
