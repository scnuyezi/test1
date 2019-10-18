from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time,configparser,sys
sys.path.append('..')

time_out = 10

def sendKeys(driver:webdriver.Chrome,text,*local):
    start_time = time.time()
    end_time = 0
    try:
        element = WebDriverWait(driver,time_out).until(lambda x:x.find_element(*local))
        end_time = time.time()
    except:
        print("定位失败：%s" %local)
    else:
        element.send_keys(text)
        use_time = round((end_time - start_time) / 1000,2)
        print("定位 %s 用时%s s" % ( local,use_time ))

def click(driver:webdriver.Chrome,*local):
    start_time = time.time()
    end_time = 0
    try:
        element = WebDriverWait(driver, time_out).until(lambda x:x.find_element(*local))
        end_time = time.time()
    except:
        print("定位失败：%s" % local)
    else:
        element.click()
        use_time = round((end_time - start_time) / 1000,2)
        print("定位 %s 用时%s s" % ( local,use_time ))

def addOption():
    option = webdriver.ChromeOptions()
    #
    option_path = r'-user-data-dir="C:\Users\Yezi\AppData\Local\Google\Chrome\User Data"'
    option.add_argument(option_path)
    return option


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('https://www.smzdm.com/')
    driver.maximize_window()
    click(driver,'link text','登录')
    driver.switch_to.frame('J_login_iframe')
    sendKeys(driver,'username','id','username')
    sendKeys(driver, 'password', 'xpath', '//input[@id="password"]')
    time.sleep(20)

    my_config = configparser.ConfigParser()
    config_path = '../config/webcookies.ini'
    my_config.read('config_path')
    with open('config_path','w') as fp:
        my_config.set('smzdm','cookies',driver.get_cookies())
        my_config.write(fp)
