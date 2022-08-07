from Pages.BasePage import BasePage


class CoupleHotelScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def searchCoupleHotel(self, city):
        self.click("searchAnywhere_XPATH")
        self.type("searchText_ID", city)
        self.clickIndex("selectLocationCoupleHotel_ID", 0)
        self.click("checkInOutDate_ACCESSIBILITYID")
        self.click("checkInDate_XPATH")
        self.click("checkOutDate_XPATH")
        self.click("cotinue_ID")
        self.click("getARoom_XPATH")

