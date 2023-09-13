from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = YOUR_CHROME_DRIVER_PATH
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.speedtest.net/")
time.sleep(2)

go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_button.click()

time.sleep(60)

download = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download = download.text

upload = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload = upload.text

print(download)
print(upload)
time.sleep(5)


driver.get("https://twitter.com/")
time.sleep(2)

username = YOUR_USERNAME
password = YOUR_PASSWORD

login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div/span/span')
login.click()
time.sleep(3)

user = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
user.send_keys(username)
time.sleep(1)
user.send_keys(Keys.ENTER)

time.sleep(2)

pas = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
pas.send_keys(password)
time.sleep(1)
pas.send_keys(Keys.ENTER)
time.sleep(10)

tweet = f"Hey Internet Provider! My download is {download}, upload is {upload}. Give me nice Internet please. :)"


time.sleep(2)


new_tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
new_tweet.click()
time.sleep(1)
new_tweet.send_keys(tweet)
time.sleep(2)

new_tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
new_tweet.click()

time.sleep(10)

driver.quit()
