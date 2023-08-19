from selenium.webdriver.common.by import By


class Login:
    username_byID = "username"
    password_byID = "password"
    login_btn_byID = "login"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self):
        self.driver.find_element(By.ID, self.username_byID).send_keys(username)

    def set_password(self):
        self.driver.find_element(By.ID, self.password_byID).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_btn_byID).click()
