import sys,os
sys.path.append(os.path.abspath(os.getcwd()))
from webcommon.baseView import *

class SmzdmClass():
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.url= 'https://www.smzdm.com/'

    def openUrl(self):
        self.driver.get(self.url)

    def sign(self):
        click(self.driver,'link text','登录')
        self.driver.switch_to.frame('J_login_iframe')
        sendKeys(self.driver,'username','id','username')
        sendKeys(self.driver, 'password', 'xpath', '//input[@id="password"]')


if __name__ =='__main__':
    option = addOption()
    driver = webdriver.Chrome(options = option)
    my_class = SmzdmClass(driver)
    my_class.openUrl()
    my_class.sign()


