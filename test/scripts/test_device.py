import esperclient
from esperclient.rest import ApiException
from utils import get_esper_credentials, get_enterprise_for_env,\
    get_device_for_enterprise

esper_creds = get_esper_credentials()

# Configuration
configuration = esperclient.Configuration()
configuration.host = esper_creds.get('host')
configuration.api_key['Authorization'] = esper_creds.get('key')
configuration.api_key_prefix['Authorization'] = 'Bearer'

# global values -  to reduce api calls
enterprise_id = get_enterprise_for_env()
device_id = get_device_for_enterprise(enterprise_id)


def test_device_list():
    api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
    # name = 'name_example' # str | Filter by device name (optional)
    # search = 'search_example' # str | A search term. Search by device name or imei (optional)
    # limit = 20 # int | Number of results to return per page. (optional) (default to 20)
    # offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        # Fetch all devices in an enterprise
        api_response = api_instance.get_all_devices(enterprise_id)
        # print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_all_devices: %s\n" % e)

    assert api_response.count > 0, "Atleast one device is needed for testing"
    assert api_response.results[0].id is not None, "Id cannot be null"


def test_device_detail():
    api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))

    try:
        # Fetch device details by ID
        api_response = api_instance.get_device_by_id(enterprise_id, device_id)
        # print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_by_id: %s\n" % e)

    assert api_response.id is not None, "Id cannot be null"

def test_device_app_installs():
    # create an instance of the API class
    api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
    #device = 'device_example'  # str | filter by device id (optional)
    #package_name = 'package_name_example'  # str | filter by package name (optional)
    #application_name = 'application_name_example'  # str | filter by application name (optional)
    #install_state = 'install_state_example'  # str | filter by install state (optional)
    #limit = 20  # int | Number of results to return per page. (optional) (default to 20)
    #offset = 56  # int | The initial index from which to return the results. (optional)
    #device_id = 'cd2d9e3b-953c-482f-abbc-168910851bad'
    try:
        api_response = api_instance.get_app_installs(enterprise_id, device_id)
        # print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_app_installs: %s\n" % e)

    assert api_response.count is not None
    assert isinstance(api_response.results, list)

def test_device_status():
    api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
    latest_event = 1  # float | Flag to get latest event

    try:
        # Get latest device event
        api_response = api_instance.get_device_event(enterprise_id, device_id, latest_event)
        # print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_event: %s\n" % e)

    assert api_response.count == 1, "Device not sending status events"
    assert api_response.results[0].id is not None
