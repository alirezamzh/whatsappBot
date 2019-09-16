from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('Enter name : ')
msg = input('Enter msg : ')
count = int(input('How many times ??? '))
input('Enter Anything ... ')

user = driver.find_element_by_xpath('//span[@title = "{}" ]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    # button = driver.find_element_by_class_name('')
    # button.click()
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
