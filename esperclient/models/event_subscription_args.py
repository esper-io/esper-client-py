# coding: utf-8

"""
ESPER API REFERENCE

OpenAPI spec version: 1.0.0
Contact: developer@esper.io
---------------------------------------------------------

Copyright 2019 Shoonya Enterprises Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



import pprint
import re

import six


class EventSubscriptionArgs(object):
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
        'aws_account_id': 'str'
    }

    attribute_map = {
        'aws_account_id': 'aws_account_id'
    }

    def __init__(self, aws_account_id=None):
        """EventSubscriptionArgs - a model defined in Swagger"""

        self._aws_account_id = None
        self.discriminator = None

        self.aws_account_id = aws_account_id

    @property
    def aws_account_id(self):
        """Gets the aws_account_id of this EventSubscriptionArgs.


        :return: The aws_account_id of this EventSubscriptionArgs.
        :rtype: str
        """
        return self._aws_account_id

    @aws_account_id.setter
    def aws_account_id(self, aws_account_id):
        """Sets the aws_account_id of this EventSubscriptionArgs.


        :param aws_account_id: The aws_account_id of this EventSubscriptionArgs.
        :type: str
        """
        if aws_account_id is None:
            raise ValueError("Invalid value for `aws_account_id`, must not be `None`")
        if aws_account_id is not None and len(aws_account_id) < 1:
            raise ValueError("Invalid value for `aws_account_id`, length must be greater than or equal to `1`")

        self._aws_account_id = aws_account_id

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
        if issubclass(EventSubscriptionArgs, dict):
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
        if not isinstance(other, EventSubscriptionArgs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other