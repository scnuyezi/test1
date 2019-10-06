from common.common import click,swipe_per
import time

def sm_sigh(driver):
    click(driver,'id', 'com.smzdm.client.android:id/tab_usercenter' ) #点击我的
    click(driver, 'id', 'com.smzdm.client.android:id/tv_login_sign') #点击签到
    #关掉签到成功界面
    click(driver,'xpath','//*[@resource-id="com.smzdm.client.android:id/rl_root"]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]')
    #返回
    click(driver, 'xpath','//*[@content-desc="Navigate up"]')


def sm_zhong(driver):
    click(driver, 'id', 'com.smzdm.client.android:id/tab_article')  #点击社区
    try:
        click(driver,'id','com.smzdm.client.android:id/dialog_home_close')
    except:
        pass
    click(driver, 'id', 'com.smzdm.client.android:id/iv_add_tabs') # 点击d导航
    # 进入众测
    click(driver, 'xpath', '//*[@resource-id="com.smzdm.client.android:id/list"]/android.widget.RelativeLayout[15]/android.widget.FrameLayout[1]')
    #进入0元试用
    click(driver, 'xpath', '//*[@resource-id="com.smzdm.client.android:id/layout_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]')
    #滑动到
    time.sleep(3)
    swipe_per(driver,0.5,0.8,0.5,0.4)
    #进入双签
    click(driver,'xpath','//*[@resource-id="com.smzdm.client.android:id/list"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]')
    #第一次签到
    click(driver, 'id', 'com.smzdm.client.android:id/tv_right')
    #提交
    click(driver, 'id', 'com.smzdm.client.android:id/editplan_btn_tijiao')
    #第一个产品
    click(driver, 'xpath', '//*[@resource-id="com.smzdm.client.android:id/list"]/android.widget.FrameLayout[2]')
    #立即申请
    click(driver, 'id', 'com.smzdm.client.android:id/tv_right')
    #提交
    click(driver, 'id', 'com.smzdm.client.android:id/editplan_btn_tijiao')


