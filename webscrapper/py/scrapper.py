import time
from selenium import webdriver

driver = webdriver.Chrome() # Chrome driver executable is in py directory, no need to specify path
driver.get('https://www.instagram.com/');

if driver.find_element_by_xpath("//*[contains(text(), 'Log in')]") is None:
	print "Could not find login button"
else:
	print "Found login button"
	driver.find_element_by_xpath("//*[contains(text(), 'Log in')]").click()

if driver.find_element_by_xpath("//*[contains(text(), 'Not now')]") is None:
	# Perform usual instagram login
	print "No facebook login option..."
	print "Login to instagram directly"

else:
	# Bypass facebook login to regular login
	print "Bypass facebook login"
	driver.find_element_by_xpath("//*[contains(text(), 'Not now')]").click()

# Returned to original login

driver.find_element_by_xpath("//*[contains(text(), 'Log in')]").click()

# driver.quit()
