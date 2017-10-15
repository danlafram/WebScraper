import sys
import time
import requests
import threading
from bs4 import BeautifulSoup
from selenium import webdriver

# Chrome driver executable is in py directory, no need to specify path
driver = webdriver.Chrome()

url = 'https://www.instagram.com/explore/tags/'

driver.get(url + str(sys.argv[1]) + "/")


links = [a.get_attribute('href') for a in driver.find_elements_by_css_selector('div._f2mse a')]

driver.get(links[0])

r = requests.get(links[0])

data = r.text

soup = BeautifulSoup(data, "lxml")
print soup
for link in soup.find_all('a'):
	print(link.get('href'))

# def worker(link): 
# 	# Thread worker function

# threads = []

# for i in range(5):
# 	t = threading.Thread(target=worker, args=(i,))
# 	threads.append(t)
# 	t.start()
