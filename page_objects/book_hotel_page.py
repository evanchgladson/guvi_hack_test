from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class hotelBooking:
    # locators
    fname = "first_name"
    lname = "last_name"
    adr = "address"
    cc_number = "cc_num"
    ccType = "cc_type"
    cc_exp_mon = "cc_exp_month"
    cc_exp_yr = "cc_exp_year"
    cc_cvvNum = "cc_cvv"
    bookNow = "book_now"

    def __init__(self, driver):
        self.driver = driver

    def f_name(self):
        self.driver.find_element(By.NAME, self.fname).send_keys("Evanchalin")

    def l_name(self):
        self.driver.find_element(By.NAME, self.lname).send_keys("C K")

    def addr(self):
        self.driver.find_element(By.NAME, self.adr).send_keys("KTC Nagar")

    def card_num(self):
        self.driver.find_element(By.NAME, self.cc_number).send_keys("1234567890123456")

    def card_type(self):
        card = Select(self.driver.find_element(By.NAME, self.ccType))
        card.select_by_visible_text("VISA")

    def exp_month(self):
        exp_mon = Select(self.driver.find_element(By.NAME, self.cc_exp_mon))
        exp_mon.select_by_visible_text("December")

    def exp_year(self):
        self.exp_year = Select(self.driver.find_element(By.NAME, self.cc_exp_yr))
        exp_year.select_by_visible_text("2024")

    def cvv(self):
        self.driver.find_element(By.NAME, self.cc_cvvNum).send_keys("345")

    def book(self):
        self.driver.find_element(By.NAME, self.bookNow).click()