from selenium import webdriver
wd=webdriver.Chrome(r'E:/chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/test2.html')
radios=wd.find_elements_by_css_selector('input[type="radio"]')
for radio in radios:
    if radio.get_attribute('checked'):
        print(radio.get_attribute('value'))
    elif radio.get_attribute('value')=='小江老师':
        radio.click()
# checkboxs=wd.find_elements_by_css_selector('input[type="checkbox"]')
# for checkbox in checkboxs:
#     if checkbox.get_attribute('checked'):
#         print(checkbox.get_attribute('value'))
elements = wd.find_elements_by_css_selector(
  '#s_checkbox input[checked="checked"]')

for element in elements:
    element.click()

# 再点击 小雷老师
wd.find_element_by_css_selector(
  "#s_checkbox input[value='小雷老师']").click()
input('')
# wd.quit()
