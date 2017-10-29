import re
import sys
import ast
import time
import json
import requests
import mysql.connector
from bs4 import BeautifulSoup
from selenium import webdriver
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'scraper',
  'raise_on_warnings': True,
}

# First argument: Instagram username
# Second argument: Instagram password (NEVER SAVED/STORED)

# Chrome driver executable is in py directory, no need to specify path
driver = webdriver.Chrome()

def loggin():
	driver.get("https://www.instagram.com")

	if driver.find_element_by_xpath("//a[contains(text(), 'Log in')]") is None:
			print "Could not find login button"
	else:
		driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()

	# Input Instagram credentials
	if driver.find_element_by_name("username"):
		driver.find_element_by_name("username").send_keys(str(sys.argv[1]))
	else:
		print "Username input NOT FOUND"

	if driver.find_element_by_name("password"):
		driver.find_element_by_name("password").send_keys(str(sys.argv[2])) 
	else:
		print "Password input NOT FOUND"

	if driver.find_element_by_xpath("//button[contains(text(), 'Log in')]"):
		driver.find_element_by_xpath("//button[contains(text(), 'Log in')]").click()
	else:
		print "Log in button NOT FOUND"
	time.sleep(1)
	extractLinksFromFollowing()

def extractLinksFromFollowing():
	url = 'https://www.instagram.com/adamdelduca/'
	driver.get(url)
	# Find following link and click to display modal
	links = [a.get_attribute('href') for a in driver.find_elements_by_class_name('_t98z6')]
	# Display Following modal (driver required)
	driver.find_elements_by_class_name('_t98z6')[2].click()
	# Wait for modal to pop
	time.sleep(0.5)
	# Extract following href's from modal
	following = [a.get_attribute('href') for a in driver.find_elements_by_class_name('_o5iw8')]
	parseFollowing(following)

def parseLinks():

def parseFollowing(following):
	str_tags_arr = []
	for user in range(len(following)):
		# Get request of user's page
		r = requests.get(following[user])
		# Get html of user's page
		html = r.text
		# Turn html into soup object
		soup = BeautifulSoup(html, 'lxml')
		# Extract all scirpt tags from soup
		tags = soup.find_all('script')
		# Extract script tag containing important data
		str_tags = str(tags[1])
		# Remove front end of script tag to only have JS object
		str_tags = str_tags.split('_sharedData = ', 1)[-1]
		# Remove back end of script tag to only have JS object
		str_tags = str_tags.replace(" ", "").rstrip(str_tags[-10:])
		# Turn new JS object string into JSON object
		str_tags_arr.append(json.loads(str_tags))
	extactDataFromJSON(str_tags_arr)

def extactDataFromJSON(tags_json):
	for i in range(len(tags_json)):
		# Check if user has over 500 followers
		if (tags_json[i]['entry_data']['ProfilePage'][0]['user']['followed_by']['count'] > 500):
			# Extract wanted data form JSON object
			user_followers = tags_json[i]['entry_data']['ProfilePage'][0]['user']['followed_by']['count']
			user_following = tags_json[i]['entry_data']['ProfilePage'][0]['user']['follows']['count']
			username = tags_json[i]['entry_data']['ProfilePage'][0]['user']['username']
			user_posts = tags_json[i]['entry_data']['ProfilePage'][0]['user']['media']['count']
			user_profile_picture = tags_json[i]['entry_data']['ProfilePage'][0]['user']['profile_pic_url_hd']
			user_url = ('https://instagram.com/' + username)
			user_recents = ""
			storeData(username, user_url, user_posts, user_followers, user_following, user_profile_picture, user_recents)

def storeData(username, user_url, user_posts, user_followers, user_following, user_profile_picture, user_recents):
	try:
		cnx = mysql.connector.connect(**config)

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cursor = cnx.cursor()
		add_info = ("INSERT INTO user_info "
               "(username, user_url, user_posts, user_followers, user_following, user_profile_picture, user_recents) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
		info_data = (username, user_url, user_posts, user_followers, user_following, user_profile_picture, user_recents)
		cursor.execute(add_info, info_data)
		cnx.commit()
		cursor.close()
		cnx.close()


loggin()