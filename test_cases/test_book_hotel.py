from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from guvi_hack_test.page_objects.LoginPage import Login
from guvi_hack_test.page_objects.book_hotel_page import hotelBooking


class Test_search_hotel:

    def test_loc_hotel(self):
        serv_obj = Service("C:\\chrome_driver\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)

        self.booking = hotelBooking(self.driver)
        self.booking.fname()
        self.booking.lname()
        self.booking.addr()
        self.booking.card_num()
        self.booking.card_type()
        self.booking.exp_month()
        self.booking.exp_year()
        self.booking.cvv()
        self.booking.book()