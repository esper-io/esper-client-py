# coding: utf-8

"""
    Esper Manage API

    # Introduction Esper Manage APIs for Cloud are a set of REST-based APIs that help you programmatically control and monitor your enterprise's dedicated Esper endpoint. Using these APIs, one can orchestrate & manage devices that have been provisioned against your endpoint. Furthermore, this API allows you to manage android applications that get installed on such devices. To read more about the various capabilities of Esper endpoints and Esper managed devices, please visit [esper.io](https://esper.io). This guide describes all the available APIs in detail, along with code samples for you to quickly ramp up to using them.  You can find out more about Esper at [https://esper.io](https://esper.io)  We've done our best to keep this document up to date, but if you find any issues, please reach out to us at developer@esper.io.  # SDK    You are welcome to use your favorite HTTP/REST library for your programming language in order to use these APIs, or you can use our official SDK (currently available in [python](https://github.com/esper-io/esper-client-py)) to do so.   # Authentication Client needs to send authentication details to access APIs. Following authentication schemes are supported:  #### Basic Authentication Client can use username and password to authenticate. These are your developer account credentials. For example, the client sends HTTP requests with the Authorization header that contains the word `Basic` followed by a space and a base64-encoded string `username:password`. ##### Base64 encoding Bash  ``` echo 'username:password' | base64 ```  Powershell  ``` [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes(\"username:password\")) ```  **Example request** ```bash curl -X GET \\   https://DOMAIN.shoonyacloud.com/api/enterprise/<enterprise_id>/device/ \\   -H 'Authorization: Basic cl0ZWFkbWluOnNpdG1pbjEyMyQ=' \\   -H 'Content-Type: application/json' \\ ``` You can read more about basic authentication scheme  [here](https://swagger.io/docs/specification/authentication/basic-authentication/)  # Errors The API uses standard HTTP status codes to indicate success or failure. All error responses will have a JSON body in the following format  ``` {   \"errors\": [],   \"message\": \"error message\",   \"status\": 400 } ``` * `errors` -  List of error details * `message` - Error description * `status` - HTTP status code   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@esper.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GroupCommandRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enterprise': 'str',
        'group': 'str',
        'command_args': 'str'
    }

    attribute_map = {
        'enterprise': 'enterprise',
        'group': 'group',
        'command_args': 'command_args'
    }

    def __init__(self, enterprise=None, group=None, command_args=None):  # noqa: E501
        """GroupCommandRequest - a model defined in Swagger"""  # noqa: E501

        self._enterprise = None
        self._group = None
        self._command_args = None
        self.discriminator = None

        self.enterprise = enterprise
        self.group = group
        if command_args is not None:
            self.command_args = command_args

    @property
    def enterprise(self):
        """Gets the enterprise of this GroupCommandRequest.  # noqa: E501


        :return: The enterprise of this GroupCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this GroupCommandRequest.


        :param enterprise: The enterprise of this GroupCommandRequest.  # noqa: E501
        :type: str
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")  # noqa: E501

        self._enterprise = enterprise

    @property
    def group(self):
        """Gets the group of this GroupCommandRequest.  # noqa: E501


        :return: The group of this GroupCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupCommandRequest.


        :param group: The group of this GroupCommandRequest.  # noqa: E501
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def command_args(self):
        """Gets the command_args of this GroupCommandRequest.  # noqa: E501


        :return: The command_args of this GroupCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_args

    @command_args.setter
    def command_args(self, command_args):
        """Sets the command_args of this GroupCommandRequest.


        :param command_args: The command_args of this GroupCommandRequest.  # noqa: E501
        :type: str
        """

        self._command_args = command_args

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GroupCommandRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
