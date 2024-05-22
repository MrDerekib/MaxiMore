from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from credentials import username, password
import config

import time

print(config.username, config.password)
username = config.username
password = config.password

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://eam.indraweb.net/maximo/webclient/login/login.jsp")

#  Login

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "username"))
)

input_username = driver.find_element(By.ID, "username")
input_username.clear()
input_username.send_keys(username)
input_password = driver.find_element(By.ID, "password")
input_password.clear()
input_password.send_keys(password + Keys.ENTER)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "mx8_ns_menu_WO_MODULE_a_tnode"))
)

nav_bar = driver.find_element(By.ID, "mx8_ns_menu_WO_MODULE_a_tnode")
nav_bar.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "mx8_ns_menu_WO_MODULE_sub_changeapp_WO_TR_a_tnode"))
)

nav_bar_child = driver.find_element(By.ID, "mx8_ns_menu_WO_MODULE_sub_changeapp_WO_TR_a_tnode")
nav_bar_child.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="mx20_tfrow_[C:4]_txt-tb"]'))
)

input_search = driver.find_element(By.XPATH, '//*[@id="mx20_tfrow_[C:4]_txt-tb"]') #CLIENTE
input_search.clear()
input_search.send_keys("=TMB")

time.sleep(1)

input_search2 = driver.find_element(By.XPATH, '//*[@id="mx20_tfrow_[C:14]_txt-tb"]') # CLASIFICACIÓN
input_search2.clear()

input_search2.send_keys("EXPENDEDORAS AUTOMÁTICAS DE BILLETES" + Keys.ENTER)

time.sleep(600)

driver.quit()