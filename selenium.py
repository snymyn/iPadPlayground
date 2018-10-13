from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get("http://inventwithpython.com")

"""
# Element finder
try:
	elem = browser.find_element_by_class_name("bookcover")
	print("Found element { } ".format(elem.tag_name))
except:
	print("No class found")
	
"""

link_elem = browser.find_element_by_link_text("Read It Online")
type(link_elem)
link_elem.click() #click the link of link_elem


## save password and input it
# input form
browser.get("https://mail.yahoo.com")
email_elem = browser.find_element_by_id("login-username")
email_elem.send_keys("not_my_real_email")
password_elem = browser.find_element_by_id("login-password")
password_elem.send_keys("1234")
password_elem.submit()


