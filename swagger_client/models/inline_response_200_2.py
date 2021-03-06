# coding: utf-8

"""
    Arbitrage Watcher RESTful API

    Provides the set of endpoints to manage arbitrage watcher service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2002(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, is_stopped=None):
        """
        InlineResponse2002 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_stopped': 'bool'
        }

        self.attribute_map = {
            'is_stopped': 'is_stopped'
        }

        self._is_stopped = is_stopped

    @property
    def is_stopped(self):
        """
        Gets the is_stopped of this InlineResponse2002.

        :return: The is_stopped of this InlineResponse2002.
        :rtype: bool
        """
        return self._is_stopped

    @is_stopped.setter
    def is_stopped(self, is_stopped):
        """
        Sets the is_stopped of this InlineResponse2002.

        :param is_stopped: The is_stopped of this InlineResponse2002.
        :type: bool
        """

        self._is_stopped = is_stopped

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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
