from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import os
from script import script_function

def Spider(href,num):
    os.chdir(r"C:\\Program Files\\Google\\Chrome\Application")
    os.system(r'start chrome --remote-debugging-port=58805 --user-data-dir="E:\selenium"')
    os.chdir(r"G:\\VSCode Asset\\python")

    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:58805")
    s = Service('chromedriver.exe')
    browser = webdriver.Chrome(service = s,options=options)
    browser.get(href)
    sleep(1)

    for i in range(num):
        browser.switch_to.default_content()
        browser.execute_script(script_function(i,i))
        browser.switch_to.default_content()
        browser.switch_to.frame('g_iframe')
        xpath = "/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/a[11]"
        next_one = browser.find_element(By.XPATH,xpath)
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        action = ActionChains(browser)
        action.click(next_one).perform()
        sleep(1)