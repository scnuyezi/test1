from common.common import click,tap_per,swipe_per
from appium import webdriver
import time

def jdjr_sign(driver:webdriver.Remote):
    print('开始京东签到')
    try:
        click(driver, 'id', 'com.jd.jrapp:id/btn_jump') #点击跳过
    except:
        print("没有定位到跳过")
    try:
        swipe_per(driver,0.5,0.6,0.5,0.4)
        click(driver, 'xpath','//*[@text="每日签到"]')
        print('点击每日签到')
    except:
        tap_per(driver,0.5,0.75) #领取钢镚
        print('从界面点击图片进入签到')
    time.sleep(5)
    tap_per(driver, 0.5, 0.4) #点击签到
    print('点击签到')
    tap_per(driver, 0.9, 0.775)  #双签界面
    print('双签界面')
    tap_per(driver, 0.83, 0.44)  # 跳转京东
    print('跳转京东')
    tap_per(driver, 0.5, 0.23)  # 签到领京豆
    print('签到领京豆')
    click(driver, 'id', 'com.jingdong.app.mall:id/gd')  # 关闭京东签到
    print('签到领京豆')
    click(driver, 'id', 'com.jd.jrapp: id / common_webview_navbar_left')  # 关闭京东
    print('关闭京东')
    tap_per(driver, 0.9, 0.775)  # 双签界面
    print('双签界面')
    tap_per(driver, 0.5, 0.8)  # 领取双签奖励
    print('领取双签奖励')



