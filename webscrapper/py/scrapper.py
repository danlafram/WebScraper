import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome() # Chrome driver executable is in py directory, no need to specify path
driver.get('https://www.instagram.com/');

# Navigate to login page

if driver.find_element_by_xpath("//a[contains(text(), 'Log in')]") is None:
	print "Could not find login button"
else:
	print "Found login button"
	driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()

# Input Instagram credentials

if driver.find_element_by_name("username"):
	print "Found username input"
	driver.find_element_by_name("username").send_keys("") # !! REMOVE BEFORE COMMITING !!
else:
	"Username input NOT FOUND"

if driver.find_element_by_name("password"):
	print "Found password input"
	driver.find_element_by_name("password").send_keys("") # !! REMOVE BEFORE COMMITING !!
else:
	print "Password input NOT FOUND"

if driver.find_element_by_xpath("//button[contains(text(), 'Log in')]"):
	print "Log in button found"
	driver.find_element_by_xpath("//button[contains(text(), 'Log in')]").click()
else:
	print "Log in button NOT FOUND"

time.sleep(2)

driver.get('https://www.instagram.com/explore/tags/' + str(sys.argv[1]) + "/")


# Find and input Search
# time.sleep(2)
# if driver.find_element_by_xpath("//input[@type='text']"):
# 	print "Search input found"
# 	driver.find_element_by_xpath("//input[@type='text']").send_keys("travel")
# 	time.sleep(0.5)
# 	driver.find_element_by_xpath("//input[@type='text']").send_keys(Keys.RETURN)

# else:
# 	print "Search input NOT FOUND"

# driver.quit()
