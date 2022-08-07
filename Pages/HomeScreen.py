from Pages.BasePage import BasePage
from Pages.CoupleHotelScreen import CoupleHotelScreen
from Pages.HotelScreen import HotelScreen


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoHotels(self):
        self.click("hotels_ID")
        return HotelScreen(self.driver)

    def gotoCoupleHotel(self):
        self.click("coupleHotel_XPATH")
        return CoupleHotelScreen(self.driver)

    def bookFlight(self):
        pass

    def gotoTrain(self):
        pass

    def gotoBus(self):
        pass

    def bookCab(self):
        pass
