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

# Create group (Not working | works with enterprise url)
def test_create_device_group():
    api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
    data = esperclient.EnterpriseDeviceGroup(enterprise=enterprise_id, name='TestBotGroup')  # EnterpriseDeviceGroup

    try:
        # Create a device group
        api_response = api_instance.create_group(enterprise_id, data)
        print(api_response)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->create_group: %s\n" % e)


# Delete group (test after create)
def test_delete_group():
    # create an instance of the API class
    api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
    group_id = 'group_id_example'  # str | A UUID string identifying this enterprise device group.

    try:
        # Delete a device group
        api_instance.delete_group(group_id, enterprise_id)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->delete_group: %s\n" % e)


# Patch Add device (Test after create) TBD

# Patch Delete device (Test after create) TBD
