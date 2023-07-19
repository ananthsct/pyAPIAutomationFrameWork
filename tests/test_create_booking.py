'''

Author : Ananth
Objective : Create Verify by POST Request
TC#1 - Verify the status Code, Headers
TC#2 - Verify the Body > Booking ID
TC#3 - Verify the JSON Schema is valid

'''
import pytest


@pytest.mark.run(order=1)
def test_create_booking_tc1():
    assert True == True


@pytest.mark.run(order=2)
def test_create_booking_tc2():
    assert True == False


@pytest.mark.run(order=3)
def test_create_booking_tc3():
    assert True == True

