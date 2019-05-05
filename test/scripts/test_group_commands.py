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
group_id = get_group_for_enterprise(enterprise_id)

def test_group_app_install():
    api_instance = esperclient.GroupCommandsApi(esperclient.ApiClient(configuration))
    group_id = '7b3963ce-61f5-474b-8fc7-7f9fcf2aa1cc'  # replace with valid uuid
    command_args = esperclient.GroupCommandArgs(app_version='2f81b955-4a30-4b1b-a99f-b4016ba24854')
    data = esperclient.GroupCommandRequest(command='INSTALL', command_args=command_args)

    try:
        api_response = api_instance.run_group_command(enterprise_id, group_id, data)
        print(api_response)
    except ApiException as e:
        print("Exception when calling GroupCommandsApi->run_group_command: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"
    assert api_response.state == 'Command Initiated', "Command could not be initiated"

def test_group_command_status_get():
    api_instance = esperclient.GroupCommandsApi(esperclient.ApiClient(configuration))
    command_id = '381bbcc0-078e-407a-ac3a-f4bc4895023d'  # replace with valid uuid
    group_id = '7b3963ce-61f5-474b-8fc7-7f9fcf2aa1cc'  # replace with valid uuid

    try:
        api_response = api_instance.get_group_command(command_id, group_id, enterprise_id)
        print(api_response)
    except ApiException as e:
        print("Exception when calling GroupCommandsApi->get_group_command: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"

def test_group_command_reboot():
    api_instance = esperclient.GroupCommandsApi(esperclient.ApiClient(configuration))
    group_id = '7b3963ce-61f5-474b-8fc7-7f9fcf2aa1cc'  # replace with valid uuid
    command_args = esperclient.GroupCommandArgs()
    data = esperclient.GroupCommandRequest(command='REBOOT', command_args=command_args)

    try:
        api_response = api_instance.run_group_command(enterprise_id, group_id, data)
        print(api_response)
    except ApiException as e:
        print("Exception when calling GroupCommandsApi->run_group_command: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"
    assert api_response.state == 'Command Initiated', "Command could not be initiated"