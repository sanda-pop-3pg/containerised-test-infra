from requests import get
from logzero import logger


def test_get_user(api_base_url):
    response = get(f"{api_base_url}/api/users/2")
    user_data = response.json()
    logger.info(f"API returned: {user_data}")
    assert user_data['data']['email'] == 'janet.weaver@reqres.in', 'Wrong user returned {}'.format(user_data)
