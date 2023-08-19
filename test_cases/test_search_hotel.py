import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from guvi_hack_test.page_objects.LoginPage import Login
from guvi_hack_test.page_objects.searchHotelPage import searchHotel


class Test_search_hotel:
    url = searchHotel.baseurl
    user_name = searchHotel.username
    pwd = searchHotel.password

    def test_loc_hotel(self):
        serv_obj = Service("C:\\chrome_driver\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.set_username()
        self.lp.set_password()
        self.lp.click_login()

        self.search = searchHotel(self.driver)
        self.search.set_loc()
        self.search.set_hotel_name()
        self.search.roomType()
        self.search.NumOfRooms()
        self.search.DatePickIn()
        self.search.DatePickOut()
        self.search.NumOfAdult()
        self.search.NumOfChild()
        self.search.search_btn()
