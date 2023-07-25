# Crate , Update, Read, Delete
import pytest
# Request
# Faker
# PyTest

import requests


def test_get_req():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    token = 90
    assert response.status_code == 200
    assert len(response.json()) > 0
    return response


@pytest.fixture
def test_post_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=payload)
    # tO verify that Expected Result == Actual Result
    assert response.status_code == 200
    print(response.text)
    print(response.json()["token"])
    return response.json()["token"]


# URL
# Headers
# Payload


@pytest.fixture
def test_post_create_booking():
    payload_create_booking = {
        "firstname": "Pramod",
        "lastname": "Dutta",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-12-28",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        "Content-Type": "application/json",
    }
    # Additonal Information that we need to send the to Server to let server know that we are
    # sending a json payload in the request

    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers,
                             json=payload_create_booking)
    print(response.json())
    booking_id = response.json()["bookingid"]
    print(booking_id)
    print(response.headers)
    assert response.status_code == 200
    return booking_id

    # More Assert - More No of Testcases - More No Assertion
    # Passing the data between the Testcases


#
#
def test_put_req(test_post_create_token, test_post_create_booking):
    payload_create_booking = {
        "firstname": "Amit",
        "lastname": "Singh",
        "totalprice": 1337,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-12-28",
            "checkout": "2024-01-02"
        },
        "additionalneeds": "Breakfast,Lunch"
    }

    temp_token = "token=" + test_post_create_token
    print(temp_token)
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/" + str(test_post_create_booking)
    response = requests.put(url_put, headers=headers,
                            json=payload_create_booking)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200


#
#
def test_delete_req(test_post_create_token, test_post_create_booking):
    temp_token = "token=" + test_post_create_token
    print(temp_token)
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    url_delete = "https://restful-booker.herokuapp.com/booking/" + str(test_post_create_booking)
    response = requests.delete(url_delete, headers=headers)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 201

# Verify that Creating a Booking and Updating it and Delete it