from selenium import webdriver
from guvi_hack_test.page_objects.LoginPage import Login
from selenium.webdriver.chrome.service import Service


class Test_login:
    baseurl = "http://adactinhotelapp.com/SearchHotel.php"
    username = "evanchgladson"
    password = "Password@123"

    def test_login(self):
        serv_obj = Service("C:\\chrome_driver\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.set_username()
        self.lp.set_password()
        self.lp.click_login()
