from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from guvi_hack_test.page_objects.select_hotel_page import selectHotel


class Test_selectHotel:

    def test_select_hotel(self):
        serv_obj = Service("C:\\chrome_driver\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.select = selectHotel(self.driver)
        self.select.radio_btn()
        self.select.continue_btn()
