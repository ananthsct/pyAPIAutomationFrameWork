'''

Author : Ananth
Objective : Create Verify by POST Request
TC#1 - Verify the status Code, Headers
TC#2 - Verify the Body > Booking ID
TC#3 - Verify the JSON Schema is valid

Assertion
Expected Result == Actual Result

'''
import pytest
from src.helpers.api_wrapper import *
from src.constants.apiconstant import base_url, url_create_booking
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers

# Payload
# Base URL
# Verify


class TestIntegration(object):

    @pytest.fixture(scope="module")
    def setup(self):
        print("Before")

    @pytest.mark.run(order=1)
    def test_create_booking_tc1(self):
        response = post_request(url=url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        print(response.status_code)
        print(response.json())
        verify_http_code(response, 200)
        verify_key_for_not_null_greater_than_zero(response.json()["bookingid"])

    # URL -> Separate URL
    # Payload - Separate Payload manager
    # Headers -> Headers Utils
    # Verify - Seperate Verify

'''


    @pytest.mark.run(order=2)
    def test_create_booking_tc2():
        assert True == False


    @pytest.mark.run(order=3)
    def test_create_booking_tc3():
        assert True == True


    def tear_down(self):
        print("End")
        
'''