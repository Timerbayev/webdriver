from selenium import webdriver
import time

link = "http://127.0.0.1:8000//login/signup/"


browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)
input0 = browser.find_element_by_id("id_username")
input0.send_keys("igor")
input1 = browser.find_element_by_id("id_password")
input1.send_keys("12345678")
input2 = browser.find_element_by_id("id_email")
input2.send_keys("igor@mail.ru")
but = browser.find_element_by_css_selector(".for_submit")
but.click()

    
