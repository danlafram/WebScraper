import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome() # Chrome driver executable is in py directory, no need to specify path

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
