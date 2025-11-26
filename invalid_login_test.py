import time
from selenium.webdriver.common.by import By


def test_invalid_login(start_browser):
    driver = start_browser
    driver.find_element(By.XPATH, "//a[@id='login-btn']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("xyz@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("xyz123")
    error_element = driver.find_element(By.XPATH,"//div[@class='invalid-feedback is-invalid']")
    error_text = error_element.text
    assert error_text=="invalid login credentials"
    time.sleep(5)
    driver.quit()