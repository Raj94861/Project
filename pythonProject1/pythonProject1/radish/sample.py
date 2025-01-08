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



def brow_lun(context):
    context.browser = webdriver.Chrome

@given('I launch and open the browser chrome')
def launchandopenbrowser(step):
    # if(browser=='chrome'):
    #     step.context.driver=webdriver.Chrome()
    # elif(browser=='firefox'):
    #     options=FirefoxOptions()
    #     step.context.driver=webdriver.Firefox(options=options)

    # elif(browser=='edge'):
    step.context.driver=webdriver.Edge()

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
    step.context.driver.get("https://google.com")
    step.context.driver.maximize_window()
@when('launch the url')
def launchurl(step):
    step.context.driver.get("https://en-gb.facebook.com/reg")
    time.sleep(5)


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

