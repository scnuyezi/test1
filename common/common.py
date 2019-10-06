from selenium.webdriver.support.ui import WebDriverWait
import time

def click(driver, *local):
	WebDriverWait(driver,5).until(lambda x:x.find_element(*local)).click()

def tap_per(driver, x, y,time=3):
	#tap一般用在h5界面上，所以用5s等待
    driver.tap([(driver.get_window_size()['width'] * x , driver.get_window_size()['height'] * y)])
    time.sleep(time)

def swipe_per(driver,x,y,x_end,y_end):
	time.sleep(1.5)
	driver.swipe(driver.get_window_size()['width'] * x,driver.get_window_size()['height'] * y,\
		driver.get_window_size()['width'] * x_end,driver.get_window_size()['height'] * y_end)
	time.sleep(1.5)

