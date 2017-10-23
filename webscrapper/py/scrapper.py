import re
import sys
import ast
import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver



# Chrome driver executable is in py directory, no need to specify path
driver = webdriver.Chrome()

url = 'https://www.instagram.com/explore/tags/'

driver.get(url + str(sys.argv[1]) + "/")


links = [a.get_attribute('href') for a in driver.find_elements_by_css_selector('div._f2mse a')]

# print (links)





for link in range(1):
	# Create driver
	driver2 = webdriver.Chrome()
	# Go to URL of user
	driver2.get(links[link])
	# Get user's URL
	username = [a.get_attribute('href') for a in driver2.find_elements_by_css_selector('div._eeohz a')]
	# Go to user's profile
	# print (username)
	# (driver2.get(username[0]))
	r = requests.get(username[0])
	html = r.text
	soup = BeautifulSoup(html, 'lxml')
	tags = soup.find_all('script')
	str_tags = str(tags[1])
	str_tags = str_tags.split('_sharedData = ', 1)[-1]
	str_tags = str_tags.replace(" ", "").rstrip(str_tags[-10:])
	tags_json = json.dumps(str_tags)
	tags_json = json.loads(tags_json)
	print (tags_json)
