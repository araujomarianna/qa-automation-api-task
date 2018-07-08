from api.api import *
import pytest

class TestClass(object):

    def test_bad_response_address_empty(self):
        """
        Make sure that address is a mandatory parameter

        """
        assert get_response().status_code == 400, "Wrong status code for bad request"

    def test_check_invalid_auth_token(self):
        """
        Make sure a valid token is needed to request from api

        """
        assert get_response({'address': 'Viena'}, False).status_code == 401, "Access should not be authorized"

    def test_check_name_for_each_restaurant(self):
        """
        Make sure there is no restaurant with empty name

        """
        data = get_response_data({'address': 'Viena'})
        for name in get_all_restaurant_info(data, "name"):
            assert len(name) > 0, "There is at least one empty restaurant name"

    def test_search_restaurants_by_super_cuisines(self):
        """
        Checks if restaurants can be filter by super_cuisine

        """
        data = get_response_data({'address': 'Viena', 'super_cuisines': 'Burger'})
        super_cuisines = list(get_all_restaurant_info(data, 'super_cuisines'))
        for super_cuisine in super_cuisines:
            assert 'Burger' in super_cuisine, "Burger not found in super_cuisines"

    def test_search_restaurants_by_cuisines(self):
        """
        Checks if restaurants can be filter by cuisine

        """
        data = get_response_data({'address': 'Viena', 'cuisines': 'chinesisch'})
        cuisines = list(get_all_restaurant_info(data, 'cuisines'))
        for cuisine in cuisines:
            assert 'Chinesisch' in cuisine, "Chinesisch not found in cuisines"

    def test_list_total(self):
        """
        Make sure the total number of ids is equal to the total number of restaurants

        """
        temp_data = get_response_data({'address': 'Viena'})
        total = get_total(temp_data)
        data = get_response_data({'address': 'Viena', 'page_size': total})
        ids = list(get_all_restaurant_info(data, 'id'))
        assert len(ids) == total, "total id numbers are different than total restaurants"

