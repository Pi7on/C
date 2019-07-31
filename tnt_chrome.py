from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys as k
from selenium.webdriver.chrome.options import Options
import os
import codecs
import time

#to save html page
completeName = os.path.join('C:\\Users\\Marco\\Desktop\\selenium_proj', 'page.html')

driver = wd.Chrome()
driver.get('http://tntvillage.scambioetico.org/?releaselist')

#write page 1
file_object = codecs.open(completeName, "a+", "utf-8")
file_object.write(driver.page_source)


#da 2 a 9
for current_page in range(2, 12):
	gotopage = driver.find_element_by_xpath('//*[@id="form_go_to_page"]/input[1]')
	gotopage.send_keys(current_page)
	search = driver.find_element_by_xpath('//*[@id="go_btn"]')
	search.click()
	time.sleep(4)
	file_object.write(driver.page_source)




