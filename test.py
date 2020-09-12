from selenium import webdriver
wd=webdriver.Chrome(r'E:\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')
wd.switch_to.frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]'))
# wd.switch_to.frame('frame1')
elements = wd.find_elements_by_class_name('plant')
for ele in elements:
    print(ele.get_attribute('outerHTML'))
wd.quit()