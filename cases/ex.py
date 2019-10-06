import sys,configparser,time,json
sys.path.append('..')
from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait



my_config = configparser.ConfigParser()
config_path = '../config/web.ini'
my_config.read(config_path)

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

driver = webdriver.Chrome(options= option)
driver.get(my_config.get('jdjr','url'))
driver.maximize_window()

# 加载cookies
cookies_path = '../config/jdjr.txt'
with open(cookies_path,'r') as fp:
    my_cookies = json.load(fp)
for cookie in my_cookies:
    driver.add_cookie(cookie)

driver.get(my_config.get('jdjr','url'))

with open(cookies_path,'w') as fp:
    my_cookies = driver.get_cookies()
    json.dump(my_cookies,fp)

element = driver.find_elements('xpath','//div[@class="btn-text"]')
for el in element:
    print(el.text)
    if el.text == '立即开户':
        el.click()
        print('点击完毕')




# 手工登陆获取cookies
# element = WebDriverWait(driver,10).until(lambda  x:x.find_element('partial link text','请登录'))
# time.sleep(2)
# element.click()
# WebDriverWait(driver,10).until(lambda  x:x.find_element('link text','账户登录')).click()
# WebDriverWait(driver,10).until(lambda x:x.find_element('id','loginname')).send_keys('ni8ma44')
# WebDriverWait(driver,10).until(lambda x:x.find_element('id','nloginpwd')).send_keys('yu311178')
# WebDriverWait(driver,10).until(lambda  x:x.find_element('link text','登    录')).click()
# time.sleep(20)
# my_cookies = driver.get_cookies()
# print(my_cookies)
# cookies_path = '../config/jdjr.txt'
# with open(cookies_path,'w') as fp:
#     json.dump(my_cookies,fp)

