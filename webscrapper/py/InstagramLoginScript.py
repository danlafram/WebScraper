import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# First argument: Instagram username
# Second argument: Instagram password (NEVER SAVED/STORED)
# Third argument: What you want to search (Hashtag)



driver = webdriver.Chrome() # Chrome driver executable is in py directory, no need to specify path
                            
driver.get("https://www.instagram.com") 
                            

if len(sys.argv) == 4:

	if driver.find_element_by_xpath("//a[contains(text(), 'Log in')]") is None:
		print "Could not find login button"
	else:
		print "Found login button"
		driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()

	# Input Instagram credentials

	if driver.find_element_by_name("username"):
		print "Found username input"
		driver.find_element_by_name("username").send_keys(str(sys.argv[1]))
	else:
		print "Username input NOT FOUND"

	if driver.find_element_by_name("password"):
		print "Found password input"
		driver.find_element_by_name("password").send_keys(str(sys.argv[2])) 
	else:
		print "Password input NOT FOUND"

	if driver.find_element_by_xpath("//button[contains(text(), 'Log in')]"):
		print "Log in button found"
		driver.find_element_by_xpath("//button[contains(text(), 'Log in')]").click()
	else:
		print "Log in button NOT FOUND"

	time.sleep(1)

	driver.get('https://www.instagram.com/explore/tags/' + str(sys.argv[3]) + "/")

else:
	print len(sys.argv)
	print "No credentials provided"