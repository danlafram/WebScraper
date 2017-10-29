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

def Loggin():
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
	extractLinksFromTopPosts()

def extractLinksFromTopPosts():
	url = 'https://www.instagram.com/adamdelduca/'
	driver.get(url)
	# Find following link and click to display modal
	links = [a.get_attribute('href') for a in driver.find_elements_by_class_name('_t98z6')]
	# Display Following modal (driver required)
	driver.find_elements_by_class_name('_t98z6')[2].click()
	

Loggin()