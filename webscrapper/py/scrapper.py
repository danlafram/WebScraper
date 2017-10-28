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

def queryUserInfo():
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
		query = ("SELECT username, user_url, user_followers FROM user_info ")
		cursor.execute(query)
		for (username, user_url, user_followers) in cursor:
			print("{} who can be found at {} has {} number of followers".format(
				username, user_url, user_followers))
		cursor.close()
		cnx.close()

def extractDataFromTag():
	# Chrome driver executable is in py directory, no need to specify path
	driver = webdriver.Chrome()

	url = 'https://www.instagram.com/explore/tags/'

	driver.get(url + str(sys.argv[1]) + "/")

	links = [a.get_attribute('href') for a in driver.find_elements_by_css_selector('div._f2mse a')]

	for link in range(1):
		# Create driver -> Consider parsing 'top posts' page with soup to avoid second driver
		driver2 = webdriver.Chrome()
		# Go to URL of user
		driver2.get(links[link])
		# Get user's URL
		username = [a.get_attribute('href') for a in driver2.find_elements_by_css_selector('div._eeohz a')]
		# Get request of user's page
		r = requests.get(username[0])
		# Get html of user's page
		html = r.text
		# Turn html into soup object
		soup = BeautifulSoup(html, 'lxml')
		# Extract all scirpt tags from soup
		tags = soup.find_all('script')
		# Extract script tag with important data
		str_tags = str(tags[1])
		# Remove front end of script tag to only have JS object
		str_tags = str_tags.split('_sharedData = ', 1)[-1]
		# Remove back end of script tag to only have JS object
		str_tags = str_tags.replace(" ", "").rstrip(str_tags[-10:])
		# Turn new JS object string into JSON object
		tags_json = json.loads(str_tags)
		# Extract wanted data form JSON object
		num_followers = tags_json['entry_data']['ProfilePage'][0]['user']['followed_by']['count']
		num_following = tags_json['entry_data']['ProfilePage'][0]['user']['follows']['count']
		username = tags_json['entry_data']['ProfilePage'][0]['user']['username']
		num_posts = tags_json['entry_data']['ProfilePage'][0]['user']['media']['count']
		print (num_followers)
		print (num_following)
		print (username)
		print (num_posts)

extractData()