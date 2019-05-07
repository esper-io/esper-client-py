import esperclient
from esperclient.rest import ApiException
from utils import get_esper_credentials, get_enterprise_for_env

esper_creds = get_esper_credentials()

# Configuration
configuration = esperclient.Configuration()
configuration.host = esper_creds.get('host')
configuration.api_key['Authorization'] = esper_creds.get('key')
configuration.api_key_prefix['Authorization'] = 'Bearer'


def test_enterprise_list():
    api_instance = esperclient.EnterpriseApi(esperclient.ApiClient(configuration))

    # Enterprise list
    try:
        # List all enterprises
        api_response = api_instance.get_all_enterprises()
        # print(api_response)
    except ApiException as e:
        print("Exception when calling EnterpriseApi->get_all_enterprises: %s\n" % e)

    assert (api_response.count == 1), "Only one enterprise supported"


def test_enterprise_detail():
    api_instance = esperclient.EnterpriseApi(esperclient.ApiClient(configuration))

    # Enterprise detail
    enterprise_id = get_enterprise_for_env()

    try:
        # Get your enterprise information
        api_response = api_instance.get_enterprise(enterprise_id)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling EnterpriseApi->get_enterprise: %s\n" % e)

    assert api_response.is_active
    assert api_response.name is not None
    assert api_response.short_code is not None
    assert api_response.details.registered_name is not None
    assert api_response.details.registered_address is not None
    assert api_response.details.location is not None
    assert api_response.details.zipcode is not None
    assert api_response.details.contact_email is not None

def test_enterprise_partial_update():
    api_instance = esperclient.EnterpriseApi(esperclient.ApiClient(configuration))

    # Enterprise patch
    enterprise_id = get_enterprise_for_env()
    data = esperclient.EnterpriseUpdate(name='Shoonya Default Enterprise')

    try:
        api_response = api_instance.partial_update_enterprise(enterprise_id, data)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling EnterpriseApi->partial_update_enterprise: %s\n" % e)

    assert api_response.name == "Shoonya Default Enterprise", "Enterprise name patch failed"











