from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

FB_EMAIL = "FB_Email"
FB_PASSWORD = "Password"


chrome_web_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_web_driver)
driver.get("https://tinder.com")
sleep(2)
log_in = driver.find_element_by_xpath('//*[@id="u-264510806"]/div/div[1]/div/main/div[1]/div/div/div/div/header/'
                                      'div/div[2]/div[2]/a/span')
log_in.click()

sleep(2)
more_options = driver.find_element_by_xpath('//*[@id="u-1992891882"]/div/div/div[1]/div/div[3]/span/button')
more_options.click()

sleep(2)
sign_in_facebook = driver.find_element_by_xpath('//*[@id="u-1992891882"]/div/div/div[1]/div/div[3]/span/div[3]/button')
sign_in_facebook.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(2)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(FB_EMAIL)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)



driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# #Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()