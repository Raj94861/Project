from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from radish import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from selenium.webdriver.common.by import By


u_name="//div/br[1]"
input="//input[@placeholder='{}']"
submit="//input[@type='submit']"
itemxpath="//div[normalize-space()='{}']/../../../div[2]//button//"
cart="//a[@class='shopping_cart_link']"

def brow_lun(context):
    context.browser = webdriver.Chrome

@given('User launch and open the browser chrome')
def launchandopenbrowser(step):
    # if(browser=='chrome'):
    #     step.context.driver=webdriver.Chrome()
    # elif(browser=='firefox'):
    #     options=FirefoxOptions()
    #     step.context.driver=webdriver.Firefox(options=options)

    # elif(browser=='edge'):
    step.context.driver=webdriver.Chrome()

    step.context.driver.maximize_window()
    #step.context.driver.close()

@given('I launch and open the browser chrome2')
def launchandopenbrowser2(step):
    # if(browser=='chrome'):
    #     step.context.driver=webdriver.Chrome()
    # elif(browser=='firefox'):
    #     options=FirefoxOptions()
    #     step.context.driver=webdriver.Firefox(options=options)
    #
    # elif(browser=='edge'):
    #     step.context.driver=webdriver.Edge()
    # step.context.driver.get("https://google.com")
    step.context.driver.maximize_window()
@when('User launch the url')
def launchurl(step):
    step.context.driver.get("https://www.saucedemo.com/")
    time.sleep(5)

@when('User providing username and password')
def provideunamepwd(step):
    try:
        # (WebDriverWait(step.context.driver, 10).until
        #  (EC.presence_of_element_located(step.context.driver.find_element(By.XPATH, input.format("Username")).send_keys("standard_user"))))
        #
        # (WebDriverWait(step.context.driver, 10).until
        #  (EC.presence_of_element_located(step.context.driver.find_element(By.XPATH, input.format("Password")).send_keys("secret_sauce"))))
        step.context.driver.find_element(By.XPATH, input.format("Username")).send_keys("standard_user")
        step.context.driver.find_element(By.XPATH, input.format("Password")).send_keys("secret_sauce")
        step.context.driver.find_element(By.XPATH, submit).click()

        time.sleep(10)
    except Exception as e:
        print(e)
        # step.context.driver.get_screenshot_as_base64
@when('User select {item} and clicking add to cart button')
def selectItem(step,item):
    try:
        (WebDriverWait(step.context.driver, 10).until
         (EC.presence_of_element_located(step.context.driver.find_element(By.XPATH, itemxpath.format(item)).click())))

        time.sleep(5)
    except Exception as e:
        print(e)
        step.embed(step.context.driver.get_screenshot_as_base64(),mime_type='image/png',encode_data_to_base64=False)
@then('enter the new user detail')
def new_user(step):

    step.context.driver.find_element(By.XPATH, "//*[@name='firstname']").send_keys("test")
    step.context.driver.find_element(By.XPATH, "//*[@name='lastname']").send_keys("finish")
    step.context.driver.find_element(By.XPATH, "//*[@name='reg_email__']").send_keys("12345")
    step.context.driver.find_element(By.XPATH, "//*[@name='reg_passwd__']").send_keys("aTest")
    step.context.driver.find_element(By.XPATH, "//*[@id='day']").send_keys("10")
    step.context.driver.find_element(By.XPATH, "//*[@id='month']").send_keys("jul")
    step.context.driver.find_element(By.XPATH, "//*[@id='year']").send_keys("1992")
    #step.context.driver.find_element(By.ID,"year").send_keys("1991")
    time.sleep(5)
    print('hello success executed')
    step.context.driver.find_element(By.XPATH, "//*[@type='radio' and @value='2']").click()
    step.context.driver.find_element(By.XPATH, "//*[@name='websubmit']").click()
    print("hello success executed")

