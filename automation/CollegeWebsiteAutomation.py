from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://projects.bmsit.ac.in/')
browser.maximize_window()
mobilenumber = 9036581529
mblNumberInput = browser.find_element_by_id('mobile')
print(mblNumberInput.send_keys(mobilenumber))
LoginBtn = browser.find_element_by_tag_name('button')
LoginBtn.click()
otp = input("enter the OTP")
mblNumberInput = browser.find_element_by_id('otp')
print(mblNumberInput.send_keys(otp))
verifyBtn = browser.find_element_by_tag_name('button')
verifyBtn.click()
browser.implicitly_wait(100)
browser.get('https://projects.bmsit.ac.in/naac/survey')
