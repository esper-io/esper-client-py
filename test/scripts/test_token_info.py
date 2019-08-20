import esperclient
from esperclient.rest import ApiException
from utils import get_esper_credentials, get_enterprise_for_env

esper_creds = get_esper_credentials()

# Configuration
configuration = esperclient.Configuration()
configuration.host = esper_creds.get('host')
configuration.api_key['Authorization'] = esper_creds.get('key')
configuration.api_key_prefix['Authorization'] = 'Bearer'


def test_token_info():
    api_instance = esperclient.TokenApi(esperclient.ApiClient(configuration))

    # Enterprise list
    try:
        # List all enterprises
        api_response = api_instance.get_token_info()
        # print(api_response)
    except ApiException as e:
        print("Exception when calling TokenApi->get_token_info: %s\n" % e)

    assert api_response.user is not None
    assert api_response.enterprise is not None
    assert api_response.token is not None
    assert api_response.expires_on is not None
    assert api_response.developer_app is not None
    assert api_response.scope is not None
    assert api_response.created_on is not None
    assert api_response.updated_on is not None
