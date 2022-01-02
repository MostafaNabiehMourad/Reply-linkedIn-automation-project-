from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep 


driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()  

driver.get('https://www.linkedin.com/')
input_username = driver.find_element_by_xpath('//div[@class="sign-in-form__form-input-container"]//input[@autocomplete="username"]')
input_username.send_keys('your email')
input_password = driver.find_element_by_xpath('//div[@class="sign-in-form__form-input-container"]//input[@autocomplete="current-password"]')
input_password.send_keys('your password')
driver.find_element_by_xpath('//button[@class="sign-in-form__submit-button"]').click()
driver.get('https://www.linkedin.com/feed/update/urn:li:activity:6882641313880129536/')

element_love=driver.find_elements_by_xpath("//span[@class='reactions-react-button comments-comment-social-bar__reaction-action-button']")
ele = driver.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view comments-comment-social-bar__reply-action-button comments-comment-social-bar__action-button button reply']")
count = 0
for i in element_love:
    hover = ActionChains(driver).move_to_element(i)
    hover.perform()
    sleep(2)
    driver.find_element_by_xpath("//button[@aria-label='Love']").click()
    ele[count].click()
    sleep(2)
    ele[count].send_keys("❤ ")
    sleep(2)
    driver.find_element_by_xpath("//button[@class='comments-comment-box__submit-button mt3 artdeco-button artdeco-button--1 artdeco-button--primary ember-view']").click()
    count+=1
driver.close()

