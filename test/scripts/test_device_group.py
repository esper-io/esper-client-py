import esperclient
from esperclient.rest import ApiException
from utils import get_esper_credentials, get_enterprise_for_env,\
    get_device_for_enterprise, get_group_for_enterprise

esper_creds = get_esper_credentials()

# Configuration
configuration = esperclient.Configuration()
configuration.host = esper_creds.get('host')
configuration.api_key['Authorization'] = esper_creds.get('key')
configuration.api_key_prefix['Authorization'] = 'Bearer'

# global values -  to reduce api calls
enterprise_id = get_enterprise_for_env()
device_id = get_device_for_enterprise(enterprise_id)
group_id = get_group_for_enterprise(enterprise_id)


# List device groups
def test_list_device_group():
    api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
    #name = 'name_example'  # str | filter by group name (optional)
    #limit = 20  # int | Number of results to return per page. (optional) (default to 20)
    #offset = 56  # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_groups(enterprise_id)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->get_all_groups: %s\n" % e)

    assert api_response.count > 0, "Atleast one device group is needed for testing"
    assert api_response.results[0].id is not None, "Id cannot be null"

# Device group detail
def test_device_group_detail():
    # create an instance of the API class
    api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))

    try:
        # Get device group information
        api_response = api_instance.get_group_by_id(group_id, enterprise_id)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->get_group_by_id: %s\n" % e)

    assert api_response.id is not None, "Id cannot be null"

# Create group
def test_create_device_group():
    # create group
    api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
    data = esperclient.DeviceGroup(name='TestBotGroup')  # DeviceGroup |

    try:
        api_response = api_instance.create_group(enterprise_id, data)
        print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->create_group: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"
    assert api_response.name == "TestBotGroup", "Invalid group name"

    # delete
    group_id = api_response.id
    try:
        api_instance.delete_group(group_id, enterprise_id)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->delete_group: %s\n" % e)


# Patch Add device from group
def test_add_device_in_group():
    # create group
    api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
    data = esperclient.DeviceGroup(name='TestBotGroup')  # DeviceGroup |

    try:
        api_response = api_instance.create_group(enterprise_id, data)
        print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->create_group: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"
    assert api_response.device_count == 0, "Invalid device count"

    group_id = api_response.id
    devices = ['63325b67-1564-472a-9bd8-10728984231a', 'cd2d9e3b-953c-482f-abbc-168910851bad']  #Add valid uuid
    data = esperclient.DeviceGroupUpdate(device_ids=devices)  # DeviceGroupUpdate

    try:
        # Partial update group
        api_response = api_instance.partial_update_group(group_id, enterprise_id, data)
        print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->partial_update_group: %s\n" % e)

    assert api_response.device_count == 2, "Invalid device count"

