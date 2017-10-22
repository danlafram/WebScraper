import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver



# Chrome driver executable is in py directory, no need to specify path
driver = webdriver.Chrome()

url = 'https://www.instagram.com/explore/tags/'

driver.get(url + str(sys.argv[1]) + "/")


links = [a.get_attribute('href') for a in driver.find_elements_by_css_selector('div._f2mse a')]

# print (links)


for link in range(4):
	# Create driver
	driver2 = webdriver.Chrome()
	# Go to URL of user
	driver2.get(links[link])
	# Get user's URL
	username = [a.get_attribute('href') for a in driver2.find_elements_by_css_selector('div._eeohz a')]
	# Go to user's profile
	driver2.get(username[0])
	# Print username from profile page
	print (driver2.find_element_by_class_name('_rf3jb').text)
	# Loop over Posts, Followers and Following
	for elem in driver2.find_elements_by_xpath('//span[@class = "_fd86t"]'):
		# Print Posts, Followers, Following
		print (elem.text)


# driver.get(links[0])

# username = [a.get_attribute('href') for a in driver.find_elements_by_css_selector('div._eeohz a')]

# driver.get(username[0])

# print ("Printing username: ")

# print (driver.find_element_by_class_name('_rf3jb').text)

# # Number of posts, followers following
# for elem in driver.find_elements_by_xpath('//span[@class = "_fd86t"]'):
# 	print (elem.text)
