from selenium import webdriver
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)

#maximize the window size
driver.maximize_window()
time.sleep(10) # wait
driver.get("https://golookup.com/")

# https://selenium-python.readthedocs.io/locating-elements.html#locating-elements


time.sleep(10) # wait
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
