from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)



browser.get('http://webpage.com')





soup=BeautifulSoup(browser.page_source)


#from lxml.html import fromstring
#import requests
#from itertools import cycle
#from fake_useragent import UserAgent
#
#
#def get_proxies():
#    url = 'https://free-proxy-list.net/'
#    response = requests.get(url)
#    parser = fromstring(response.text)
#    proxies = set()
#    for i in parser.xpath('//tbody/tr')[:10]:
#        if i.xpath('.//td[7][contains(text(),"yes")]'):
#            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#            proxies.add(proxy)
#    return proxies
#
#
##If you are copy pasting proxy ips, put in the list below
##proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
#proxies = get_proxies()
#proxy_pool = cycle(proxies)
#
#ua = UserAgent()
#print(ua.random)
#print(ua.random)
#print(ua.random)
#print(next(proxy_pool))
#print(next(proxy_pool))
#print(next(proxy_pool))
#proxy = next(proxy_pool)
#proxies = {"http": proxy, "https": proxy}
#
#headers = {
#'User-Agent': ua.random }
##headers = {
##'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; #rv:60.0) Gecko/20100101 Firefox/60.0'}
#
#print(headers)
#print(proxies)
#url = 'https://www.streetinsider.com/dividend_history.php?q=cost'
#
#
## Collect first page of artists’ list
#html_content = requests.get(url, headers=headers, proxies=proxies)
#
#print(html_content.text)
#
#print(html_content.status_code)
