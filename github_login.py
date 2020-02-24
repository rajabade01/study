from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://github.com/login")

driver.find_element_by_xpath("//input[@id='login_field']").send_keys('rajabade01@gmail.com')
driver.find_element_by_xpath("//input[@id='password']").send_keys("abcd")
driver.find_element_by_xpath("//input[@name='commit']").click()

element = driver.find_element_by_partial_link_text('study').click()
driver.find_element_by_partial_link_text('haker').click()
element = driver.find_elements_by_xpath("//*[contains(text(),'py')]")

elements = driver.find_elements_by_class_name('a')  #css-truncate css-truncate-target
# for i in element:
#     print (i.value_of_css_property('title'))
#print (element.text)

driver.find_element_by_link_text("study").click()
driver.implicitly_wait(2000)
print("testing")