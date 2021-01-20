from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random



def timer():
    invest = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    returns = ['5%', '10%', '15%', '20%', '7%', '8%', '11%', '30%', '35%']
    r1 = random.randint(0, 3)
    r2 = random.randint(4, 5)
    r3 = random.randint(6, 7)
    r4 = random.randint(8, 10)
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSeIFHTkQJUVNG4A_zSon38EhSApuGJHXmgv2x6wjw17vb0CgA/viewform')
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    print(radiobuttons[r1].click(),r1)
    browser.implicitly_wait(100)
    print(radiobuttons[r2].click(),r2)
    browser.implicitly_wait(100)
    print(textboxes[0].send_keys(random.choice(invest)))
    browser.implicitly_wait(100)
    print(radiobuttons[r3].click(),r3)
    browser.implicitly_wait(100)
    print(textboxes[1].send_keys(random.choice(returns)))
    browser.implicitly_wait(100)
    print(radiobuttons[r4].click(),r4)
    browser.implicitly_wait(100)
    print(submitbutton[4].click())
    browser.close()

for i in range(2):
    timer()

