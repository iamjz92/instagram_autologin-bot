
from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
import login


#open chrome and navigate to Instagram
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.instagram.com/') 

#Accept cookies popup window
acceptCookies = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
acceptCookies.click()
sleep (2)

#add Instagram Credentials and login
username_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username_box.send_keys('Your_Username or email address') 
sleep(2)
password_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password_box.send_keys('Your_Password') 
login_box = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button") 
login_box.click() 
sleep(2)

#close save login credential popup
saveLogin_popup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section')
saveLogin_popup.close()
