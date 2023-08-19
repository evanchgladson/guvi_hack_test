from selenium.webdriver.common.by import By


class selectHotel:
    # locators
    radio_btn = "radiobutton_0"
    continue_btn = "continue"

    def __init__(self, driver):
        self.driver = driver

    def radioBtn(self):
        self.driver.find_element(By.ID, self.radio_btn).click()

    def continueBtn(self):
        self.driver.find_element(By.NAME, self.continue_btn).click()
