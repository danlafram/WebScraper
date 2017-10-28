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

username = ""
user_url = ""
user_posts = 0
user_followers = 0
user_following = 0
user_profile_picture = ""
user_recents = ""

def extractLinksFromTopPosts():
	# Chrome driver executable is in py directory, no need to specify path
	driver = webdriver.Chrome()

	url = 'https://www.instagram.com/explore/locations/215009654/ottawa-ontario/'

	driver.get(url)

	# List of links of all the pictures on the page
	return [a.get_attribute('href') for a in driver.find_elements_by_css_selector('div._f2mse a')]

def parseLinks():
	links = extractLinksFromTopPosts()

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
		return json.loads(str_tags)

def extractDataFromJSON():
	tags_json = parseLinks()
	# Extract wanted data form JSON object
	user_followers = tags_json['entry_data']['ProfilePage'][0]['user']['followed_by']['count']
	user_following = tags_json['entry_data']['ProfilePage'][0]['user']['follows']['count']
	username = tags_json['entry_data']['ProfilePage'][0]['user']['username']
	user_posts = tags_json['entry_data']['ProfilePage'][0]['user']['media']['count']
	user_profile_picture = tags_json['entry_data']['ProfilePage'][0]['user']['profile_pic_url_hd']
	print (user_followers)
	print (user_following)
	print (username)
	print (user_posts)
	print(user_profile_picture)

#def storeData():
	# Call method when ready to store data from extracted JSON


extractDataFromJSON()
