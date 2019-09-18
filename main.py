from selenium import webdriver
from lxml.html import fromstring
import requests
from itertools import cycle, islice
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def get_page_content(url, proxy_pool):
    error_titles = ["Access to this page has been denied.", "403 Forbidden"]
    proxies_to_try = list(islice(proxy_pool, 20))
    print("proxies to try")
    print(proxies_to_try)
    print("\n\n")

    for index, proxy in enumerate(proxies_to_try):
        driver = get_configured_webdriver(proxy)
        print("trying to get url")
        driver.get(url)
    #    print(f"|{driver.title}|")
    #    print(driver.page_source)
    #    print("\n\n")
    #    print(driver.title)
        print(f"|{driver.title}|")
        if not driver.title or driver.title in error_titles:
            print(f"{index}. Title not found...retrying")
            continue
        else:
            print(f"title found on {index} attempt")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.findAll("table", {"class": "dividend-history"})
        print(table)
        if table:
            print(f"table found on {index} attempt")
            return driver.page_source
        else:
            print(f"{index}. table not found...retrying")

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
print("proxy list:")
print(proxy_list)
proxy_pool = cycle(proxy_list)

#url = 'https://python.org'
#url = 'https://seekingalpha.com/symbol/COST/dividends/history'
url = 'https://seekingalpha.com/symbol/AAPL/dividends/history'
print(next(proxy_pool))
content = get_page_content(url, proxy_pool)

#print("proxy list:")
#print(proxy_list)
#
#print(next(proxy_pool))


with open("web.html", "w") as text_file:
      text_file.write(content)

#web_content = None
##with open("cost.html", "r") as text_file:
#with open("web.html", "r") as text_file:
#      web_content = text_file.read()
#
##print(web_content)
#
#soup = BeautifulSoup(web_content, "html.parser")
#table = soup.findAll("table", {"class": "dividend-history"})
#print(table)
