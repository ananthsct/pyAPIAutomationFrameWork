'''
Author-Ananth
Objective :  # Verify createToken
TC1-Verify the status code,header
TC2-Verify the token
TC3-Verify JSON schema
'''
import pytest

from src.constants.apiconstant import url_create_token
from src.helpers.api_wrapper import get_request, post_request
from src.helpers.common_verification import verify_http_code, verify_key_for_not_null_greater_than_zero
from src.helpers.payload_manager import create_token
from src.helpers.utils import get_payload_auth, common_headers


class TestIntegration(object):
    @pytest.fixture(scope="module")
    def before(self):
        print("start")

    def test_token(self):
        response = post_request(url_create_token(), auth=None, headers=common_headers(),
                                payload=create_token(),
                                in_json=False)
        verify_http_code(response, 200)
        print(response.json()["token"])

    @pytest.fixture(scope="module")
    def tear_down(self):
        print("end")
