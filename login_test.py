import time



from selenium.webdriver.common.by import By


def test_login(start_browser):
    driver=start_browser
    driver.find_element(By.XPATH,"//a[@id='login-btn']").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("vkarthik.venkatachalam@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Karthik#sangeeta@14")
    driver.find_element(By.XPATH,"//a[@id='login-btn']").click()
    time.sleep(5)
    driver.quit()


