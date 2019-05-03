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


def test_device_command_reboot():
    api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
    command = esperclient.CommandRequest(command='REBOOT')
    try:
        api_response = api_instance.run_command(enterprise_id, device_id, command)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling CommandsApi->run_command: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"
    assert api_response.state == 'Command Initiated', "Command could not be initiated"

def test_device_app_deploy():
    api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
    command_args = esperclient.CommandArgs(app_version='2f81b955-4a30-4b1b-a99f-b4016ba24854')  # replace with valid uuid
    command = esperclient.CommandRequest(command='INSTALL', command_args=command_args)
    try:
        api_response = api_instance.run_command(enterprise_id, device_id, command)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling CommandsApi->run_command: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"
    assert api_response.state == 'Command Initiated', "Command could not be initiated"

def test_device_command_settings_change():
    api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
    command_args = esperclient.CommandArgs(brightness_value=100)
    command = esperclient.CommandRequest(command='SET_BRIGHTNESS_SCALE', command_args=command_args)
    try:
        api_response = api_instance.run_command(enterprise_id, device_id, command)
        # print(api_response)
    except ApiException as e:
        print("Exception when calling CommandsApi->run_command: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"
    assert api_response.state == 'Command Initiated', "Command could not be initiated"

def test_device_command_status_get():
    api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
    command_id = '0fd65c8a-a015-4695-a7b6-6f79c75887df'  # replace with valid uuid
    device_id = 'cd2d9e4b-953c-482f-abbc-168910851bad'  # replace with valid uuid

    try:
        api_response = api_instance.get_command(command_id, device_id, enterprise_id)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling CommandsApi->get_command: %s\n" % e)

