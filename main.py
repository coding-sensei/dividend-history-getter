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
