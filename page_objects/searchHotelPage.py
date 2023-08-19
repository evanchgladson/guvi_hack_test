# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from guvi_hack_test.page_objects.LoginPage import Login


class searchHotel:

    # locators
    location = "location"
    hotelName = "hotels"
    roomType = "room_type"
    NumOfRooms = "room_nos"
    DatePickIn = "datepick_in"
    DatePickOut = "datepick_out"
    NumOfAdult = "adult_room"
    NumOfChild = "child_room"
    search_btn = "//input[@value='Search']"

    def __init__(self, driver):
        self.driver = driver

    def set_loc(self):
        loc = self.driver.find_element(By.NAME, self.location)
        loc.select_by_visible_text("New York")

    # Hotel Name
    def set_hotel_name(self):
        hotel = Select(self.driver.find_element(By.ID, self.hotelName))
        hotel.select_by_index(2)

    # Room Type
    def set_room_type(self):
        room_type = Select(self.driver.find_element(By.ID, self.roomType))
        room_type.select_by_index(1)

    # Number of rooms
    def set_room_nos(self):
        room_nos = Select(self.driver.find_element(By.ID, self.roomType))
        room_nos.select_by_value("2")

    # Date In
    def set_date_in(self):
        date_pick_in = self.driver.find_element(By.NAME, self.DatePickIn)
        date_pick_in.clear()
        date_pick_in.send_keys("23/08/2023")

    # Date out
    def set_date_out(self):
        date_pick_out = self.driver.find_element(By.NAME, self.DatePickOut)
        date_pick_out.clear()
        date_pick_out.send_keys("24/08/2023")

    # Number of Adult
    def set_NumOfAdult(self):
        Adult = Select(self.driver.find_element(By.ID, self.NumOfAdult))
        Adult.select_by_value("2")

    # Number of Children
    def set_NumOfChild(self):
        child = Select(self.driver.find_element(By.ID, self.NumOfChild))
        child.select_by_index(1)

    # Search
    def set_click(self):
        self.driver.find_element(By.XPATH, self.search_btn).click()




