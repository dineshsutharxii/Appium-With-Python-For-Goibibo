import pytest
from Pages.HomeScreen import HomeScreen
from Pages.HotelScreen import HotelScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_SearchHotel(BaseTest):
    @pytest.mark.parametrize("city, hotel", dataProvider.get_data("logintest"))
    def test_search_hotel(self, city, hotel):
        home = HomeScreen(self.driver)
        home.gotoHotels().searchHotel(city)

