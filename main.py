from selenium import webdriver
from lxml.html import fromstring
import requests
from itertools import cycle
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def get_page_content(url, proxy_pool):
    print(next(proxy_pool))

def get_configured_webdriver(proxy):
    ua = UserAgent()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--proxy-server={}'.format(proxy))
    chrome_options.add_argument('user-agent={}'.format(ua.random))
    chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.
    driver = webdriver.Chrome(options=chrome_options,
          service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    return driver

proxy_list = get_proxies()
proxy_pool = cycle(proxy_list)

proxy = next(proxy_pool)

driver = get_configured_webdriver(proxy)

url = 'https://python.org'
#url = 'https://seekingalpha.com/symbol/COST/dividends/history'
driver.get(url)
print(driver.page_source)
print("\n\n")
print(driver.title)
print(f"|{driver.title}|")
if not driver.title:
    print("title not found, need to retry")
else:
    print("title found")

print(proxy_list)
t = get_page_content(url, proxy_pool)

#soup=BeautifulSoup(browser.page_source)

#with open("web.html", "w") as text_file:
#      text_file.write(driver.page_source)

