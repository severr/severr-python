# coding: utf-8

"""
    Severr API

    Get your application events and errors to Severr via the *Severr API*.

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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

from pprint import pformat
from six import iteritems
import re


class CustomData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, string_data=None, double_data=None):
        """
        CustomData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'string_data': 'CustomStringData',
            'double_data': 'CustomDoubleData'
        }

        self.attribute_map = {
            'string_data': 'stringData',
            'double_data': 'doubleData'
        }

        self._string_data = string_data
        self._double_data = double_data

    @property
    def string_data(self):
        """
        Gets the string_data of this CustomData.


        :return: The string_data of this CustomData.
        :rtype: CustomStringData
        """
        return self._string_data

    @string_data.setter
    def string_data(self, string_data):
        """
        Sets the string_data of this CustomData.


        :param string_data: The string_data of this CustomData.
        :type: CustomStringData
        """

        self._string_data = string_data

    @property
    def double_data(self):
        """
        Gets the double_data of this CustomData.


        :return: The double_data of this CustomData.
        :rtype: CustomDoubleData
        """
        return self._double_data

    @double_data.setter
    def double_data(self, double_data):
        """
        Sets the double_data of this CustomData.


        :param double_data: The double_data of this CustomData.
        :type: CustomDoubleData
        """

        self._double_data = double_data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
