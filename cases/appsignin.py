import time,sys
sys.path.append('..')
from common.desird_caps import startUp
from pageview.smzdm_signin import sm_sigh,sm_zhong
from common.configClass import get_jdjr
from pageview.jdjr import jdjr_sign
from common.common import swipe_per,tap_per


driver = startUp()
time.sleep(5)
sm_sigh(driver)
sm_zhong(driver)
print("切换app")
driver.start_activity(get_jdjr()[1],get_jdjr()[0])
# driver = startUp('com.jd.jrapp.bm.mainbox.WelcomeActivity','com.jd.jrapp')
jdjr_sign(driver)




