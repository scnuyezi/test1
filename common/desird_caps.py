from appium import webdriver
from common.configClass import MyConfigParser

def loadCaps(device = 'mate9',activity = None,package = None):
    #获得配置里面的caps信息
    caps = {}
    myparser = MyConfigParser()
    myparser.read('../config/caps.ini')
    if device == "mate9":
        for config in myparser.items('mate9caps'):
            caps[config[0]] = config[1]
    if device == "thunder":
        for config in myparser.items('thundercaps'):
            caps[config[0]] = config[1]
    if activity and package:
        caps['appActivity'] = activity
        caps['appPackage'] = package
    return caps

def startUp(activity = None,package = None):
    if activity and package:
        caps = loadCaps(activity = activity ,package=package )
    else:
        caps = loadCaps()
    print(caps)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    return driver

if __name__ =="__main__":
    startUp('com.jd.jrapp.bm.mainbox.WelcomeActivity','com.jd.jrapp')
    # startUp()