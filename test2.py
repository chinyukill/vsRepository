# http://cdn1.python3.vip/files/selenium/sample3.html
from selenium import webdriver
wd = webdriver.Chrome(r'E:/chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')
link=wd.find_element_by_css_selector('a')
link.click()
mainWindow=wd.current_window_handle

# 用这两句也可以：windows = wd.window_handles wd.switch_to.window(windows[-1])
windows = wd.window_handles
print('---------------')
print(windows)
wd.switch_to.window(windows[-1])
print('---------------')
print(wd.title)
print('---------------')
print(wd.window_handles)
print('---------------')
print(wd)
wd.switch_to.window(mainWindow)
print('---------------')
print(wd.title)

wd.quit()
