from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", "/home/seluser/Downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")

driver = webdriver.Remote("http://localhost:4444/wd/hub", options=options)
driver.set_window_size(1280, 2000)

driver.get("https://youraccountonline.electricireland.ie/")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "txtEmail"))).send_keys("YOUREMAIL")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "txtPassword"))).send_keys("YOURPASSWORD")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/form/button"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/nav/div/ul[2]/li[4]/a"))).click()

sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/main/div/div/div[6]/div[2]/p/a"))).click()

sleep(5)

driver.close()