from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys as k
from selenium.webdriver.chrome.options import Options
import os
import sys
import codecs
import time

#parse args----------------------------------------------------------------------
if str(sys.argv[1]) == "--start" :
	start = int(sys.argv[2])
	if start < 2
		start = 2
	
if str(sys.argv[3]) == "--end" :
	end = int(sys.argv[4])
#-------------------------------------------------------------------------------

#to save html page
completeName = os.path.join('C:\\Users\\Marco\\Desktop\\selenium_proj', 'page.html')

driver = wd.Chrome()
driver.get('http://tntvillage.scambioetico.org/?releaselist')

#write page 1
file_object = codecs.open(completeName, "a+", "utf-8")
file_object.write(driver.page_source)

active_page = 2
#2,5 --> da 2 a 4
for current_page in range(start, end+1):
	print("current page: "+str(current_page))
	print("active page: "+str(active_page)+"\n")
	
	gotopage = driver.find_element_by_xpath('//*[@id="form_go_to_page"]/input[1]')
	gotopage.send_keys(current_page)
	search = driver.find_element_by_xpath('//*[@id="go_btn"]')
	search.click()
	
	time.sleep(2)
	#check if page has been turned correctly
	active_page = driver.find_element_by_xpath('//*[@class="active"][@style="color:#fff;background-color:#006699;"]')
	active_page = int(active_page.text)
	
	
	
	if active_page == current_page+1 :
		print ("active_page is: "+active_page)
		print ("page has been turned correctly\n")
	
	#if current_page == 
	
	file_object.write(driver.page_source)
