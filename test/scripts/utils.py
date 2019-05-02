import esperclient
import os
from esperclient.rest import ApiException

def get_esper_credentials():
    try:
        host = os.environ['ESPER_HOST']
    except KeyError:
        print('ESPER_HOST environment variable not set.')
        return

    try:
        key = os.environ['ESPER_KEY']
    except KeyError:
        print('ESPER_KEY environment variable not set.')
        return

    return {
        'host': host,
        'key': key
    }


# Configuration
configuration = esperclient.Configuration()
esper_creds = get_esper_credentials()
configuration.host = esper_creds.get('host')
configuration.api_key['Authorization'] = esper_creds.get('key')
configuration.api_key_prefix['Authorization'] = 'Bearer'


def get_enterprise_for_env():
    api_instance = esperclient.EnterpriseApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_all_enterprises()
    except ApiException as e:
        print("Exception when calling EnterpriseApi->get_all_enterprises: %s\n" % e)

    return api_response.results[0].id


def get_device_for_enterprise(enterprise_id):
    api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_all_devices(enterprise_id)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_all_devices: %s\n" % e)

    return api_response.results[0].id

def get_group_for_enterprise(enterprise_id):
    api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_all_groups(enterprise_id)
    except ApiException as e:
        print("Exception when calling DeviceGroupApi->get_all_groups: %s\n" % e)

    return api_response.results[0].id

def get_application_for_enterprise(enterprise_id):
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_all_applications(enterprise_id)
    except ApiException as e:
        print("Exception when calling ApplicationApi->get_all_applications: %s\n" % e)

    return api_response.results[0].id

def get_version_for_app(application_id, enterprise_id):
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_app_versions(application_id, enterprise_id)
    except ApiException as e:
        print("Exception when calling ApplicationApi->get_app_versions: %s\n" % e)

    return api_response.results[0].id