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

from esperclient.models.application_version import ApplicationVersion


class Application(object):
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
        'id': 'str',
        'versions': 'list[ApplicationVersion]',
        'application_name': 'str',
        'package_name': 'str',
        'developer': 'str',
        'category': 'str',
        'content_rating': 'str',
        'compatibility': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool',
        'is_hidden': 'bool',
        'enterprise': 'str'
    }

    attribute_map = {
        'id': 'id',
        'versions': 'versions',
        'application_name': 'application_name',
        'package_name': 'package_name',
        'developer': 'developer',
        'category': 'category',
        'content_rating': 'content_rating',
        'compatibility': 'compatibility',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active',
        'is_hidden': 'is_hidden',
        'enterprise': 'enterprise'
    }

    def __init__(self, id=None, versions=None, application_name=None, package_name=None, developer=None, category=None, content_rating=None, compatibility=None, created_on=None, updated_on=None, is_active=None, is_hidden=None, enterprise=None):
        """Application - a model defined in Swagger"""

        self._id = None
        self._versions = None
        self._application_name = None
        self._package_name = None
        self._developer = None
        self._category = None
        self._content_rating = None
        self._compatibility = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self._is_hidden = None
        self._enterprise = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if versions is not None:
            self.versions = versions
        self.application_name = application_name
        self.package_name = package_name
        if developer is not None:
            self.developer = developer
        if category is not None:
            self.category = category
        if content_rating is not None:
            self.content_rating = content_rating
        if compatibility is not None:
            self.compatibility = compatibility
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active
        if is_hidden is not None:
            self.is_hidden = is_hidden
        self.enterprise = enterprise

    @property
    def id(self):
        """Gets the id of this Application.


        :return: The id of this Application.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.


        :param id: The id of this Application.
        :type: str
        """

        self._id = id

    @property
    def versions(self):
        """Gets the versions of this Application.


        :return: The versions of this Application.
        :rtype: list[ApplicationVersion]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Application.


        :param versions: The versions of this Application.
        :type: list[ApplicationVersion]
        """

        self._versions = versions

    @property
    def application_name(self):
        """Gets the application_name of this Application.


        :return: The application_name of this Application.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this Application.


        :param application_name: The application_name of this Application.
        :type: str
        """
        if application_name is None:
            raise ValueError("Invalid value for `application_name`, must not be `None`")
        if application_name is not None and len(application_name) > 255:
            raise ValueError("Invalid value for `application_name`, length must be less than or equal to `255`")
        if application_name is not None and len(application_name) < 1:
            raise ValueError("Invalid value for `application_name`, length must be greater than or equal to `1`")

        self._application_name = application_name

    @property
    def package_name(self):
        """Gets the package_name of this Application.


        :return: The package_name of this Application.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this Application.


        :param package_name: The package_name of this Application.
        :type: str
        """
        if package_name is None:
            raise ValueError("Invalid value for `package_name`, must not be `None`")
        if package_name is not None and len(package_name) > 255:
            raise ValueError("Invalid value for `package_name`, length must be less than or equal to `255`")
        if package_name is not None and len(package_name) < 1:
            raise ValueError("Invalid value for `package_name`, length must be greater than or equal to `1`")

        self._package_name = package_name

    @property
    def developer(self):
        """Gets the developer of this Application.


        :return: The developer of this Application.
        :rtype: str
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this Application.


        :param developer: The developer of this Application.
        :type: str
        """
        if developer is not None and len(developer) > 255:
            raise ValueError("Invalid value for `developer`, length must be less than or equal to `255`")
        if developer is not None and len(developer) < 1:
            raise ValueError("Invalid value for `developer`, length must be greater than or equal to `1`")

        self._developer = developer

    @property
    def category(self):
        """Gets the category of this Application.


        :return: The category of this Application.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Application.


        :param category: The category of this Application.
        :type: str
        """
        if category is not None and len(category) > 255:
            raise ValueError("Invalid value for `category`, length must be less than or equal to `255`")
        if category is not None and len(category) < 1:
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")

        self._category = category

    @property
    def content_rating(self):
        """Gets the content_rating of this Application.


        :return: The content_rating of this Application.
        :rtype: str
        """
        return self._content_rating

    @content_rating.setter
    def content_rating(self, content_rating):
        """Sets the content_rating of this Application.


        :param content_rating: The content_rating of this Application.
        :type: str
        """

        self._content_rating = content_rating

    @property
    def compatibility(self):
        """Gets the compatibility of this Application.


        :return: The compatibility of this Application.
        :rtype: str
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        """Sets the compatibility of this Application.


        :param compatibility: The compatibility of this Application.
        :type: str
        """
        if compatibility is not None and len(compatibility) < 1:
            raise ValueError("Invalid value for `compatibility`, length must be greater than or equal to `1`")

        self._compatibility = compatibility

    @property
    def created_on(self):
        """Gets the created_on of this Application.


        :return: The created_on of this Application.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Application.


        :param created_on: The created_on of this Application.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this Application.


        :return: The updated_on of this Application.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Application.


        :param updated_on: The updated_on of this Application.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this Application.


        :return: The is_active of this Application.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Application.


        :param is_active: The is_active of this Application.
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_hidden(self):
        """Gets the is_hidden of this Application.


        :return: The is_hidden of this Application.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this Application.


        :param is_hidden: The is_hidden of this Application.
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def enterprise(self):
        """Gets the enterprise of this Application.


        :return: The enterprise of this Application.
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this Application.


        :param enterprise: The enterprise of this Application.
        :type: str
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")

        self._enterprise = enterprise

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
        if issubclass(Application, dict):
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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
