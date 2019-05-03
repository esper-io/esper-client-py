import esperclient
from esperclient.rest import ApiException
from utils import get_esper_credentials, get_enterprise_for_env,\
    get_application_for_enterprise, get_version_for_app


esper_creds = get_esper_credentials()

# Configuration
configuration = esperclient.Configuration()
configuration.host = esper_creds.get('host')
configuration.api_key['Authorization'] = esper_creds.get('key')
configuration.api_key_prefix['Authorization'] = 'Bearer'

# global values -  to reduce api calls
enterprise_id = get_enterprise_for_env()
application_id = get_application_for_enterprise(enterprise_id)
version_id = get_version_for_app(application_id, enterprise_id)
app_file = '/path/to/apk/file'


def test_application_list():
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_all_applications(enterprise_id)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->get_all_applications: %s\n" % e)

    assert api_response.count > 0, "At least one application is needed for testing"
    assert api_response.results[0].id is not None, "Id cannot be null"


def test_application_detail():
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_application(application_id, enterprise_id)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->get_application: %s\n" % e)

    assert api_response.id is not None, "Id cannot be null"


def test_application_upload_delete():
    # upload
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
    enterprise = enterprise_id

    try:
        api_response = api_instance.upload(enterprise_id, enterprise, app_file)
        print(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->upload: %s\n" % e)

    assert api_response.application.is_active, "application not successful, app not active"
    assert len(api_response.application.versions) > 0, "No version present for app"

    # delete
    application_id = api_response.application.id
    try:
        # Delete an application
        api_instance.delete_application(application_id, enterprise_id)
    except ApiException as e:
        print("Exception when calling ApplicationApi->delete_application: %s\n" % e)


def test_app_version_list():
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
    #version_code = 'version_code_example'  # str | filter by version code (optional)
    #build_number = 'build_number_example'  # str | filter by build number (optional)
    #limit = 20  # int | Number of results to return per page. (optional) (default to 20)
    #offset = 56  # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_app_versions(application_id, enterprise_id)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->get_app_versions: %s\n" % e)

    assert api_response.count > 0, "No active version is present"
    assert api_response.results[0].id is not None, "Id cannot be None"

def test_app_version_detail():
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))

    try:
        api_response = api_instance.get_app_version(version_id, application_id, enterprise_id)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->get_app_version: %s\n" % e)

    assert api_response.id is not None, "Id cannot be None"

def test_app_version_delete():
    api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
    version_id = '2b233cc3-ec02-4319-8601-43edcd5a3ed7'  # replace with valid uui
    application_id = 'c968e4a2-7e30-49fd-a548-85f11f05e972'  # replace with valid uuid

    try:
        # Delete app version
        api_instance.delete_app_version(version_id, application_id, enterprise_id)
    except ApiException as e:
        print("Exception when calling ApplicationApi->delete_app_version: %s\n" % e)
