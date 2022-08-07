import pytest
from Pages.HomeScreen import HomeScreen
from Pages.HotelScreen import HotelScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.scroll_util import ScrollUtil


class Test_SearchCoupleHotel(BaseTest):
    @pytest.mark.parametrize("city, hotel", dataProvider.get_data("logintest"))
    def test_search_couplehotel(self, city, hotel):
        home = HomeScreen(self.driver)
        home.gotoCoupleHotel().searchCoupleHotel(city)
        ScrollUtil.scrollToTextByAndroidUIAutomator(hotel, self.driver)

