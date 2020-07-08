from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="/home/yeswanth/PycharmProjects/seleniumcorse/drivers/chromedriver")
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,1000)", "")     # scroll down page by pixcel
print("scrolled window with in the pixcel range")
time.sleep(5)
# scroll down the page till element is visible
flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", flag)
print("scrolled the page till the element is found")
time.sleep(4)
# scroll down the page till end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)
print("scrolled the page till the end")
driver.close()
