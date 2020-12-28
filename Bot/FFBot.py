from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import BotEngine

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)

chromedriver_path = "C:/Users/User/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)

BotEngine.init(driver)

driver.close()
