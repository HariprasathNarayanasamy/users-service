# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserInfoSansPwd(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, user_name: str=None, email: str=None, phone_number_number: str=None,role: str=None):  # noqa: E501
        """UserInfoSansPwd - a model defined in Swagger

        :param user_name: The user_name of this UserInfoSansPwd.  # noqa: E501
        :type user_name: str
        :param role: The role of this UserInfoSansPwd.  # noqa: E501
        :type role: str
        :param last_name: The last_name of this UserInfoSansPwd.  # noqa: E501
        :type last_name: str
        :param email: The email of this UserInfoSansPwd.  # noqa: E501
        :type email: str
        :param phone_number: The phone_number of this UserInfoSansPwd.  # noqa: E501
        :type phone_number: str
        """
        self.swagger_types = {
            'user_name': str,
            'role': str,
            'email': str,
            'phone_number_number': str
        }

        self.attribute_map = {
            'user_name': 'user_name',
            'role': 'role',
            'email': 'email',
            'phone_number': 'phone_number'
        }
        self._user_name = user_name
        self._role = role
        self._email = email
        self._phone_number_number = phone_number_number

    @classmethod
    def from_dict(cls, dikt) -> 'UserInfoSansPwd':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_info_sans_pwd of this UserInfoSansPwd.  # noqa: E501
        :rtype: UserInfoSansPwd
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_name(self) -> str:
        """Gets the user_name of this UserInfoSansPwd.


        :return: The user_name of this UserInfoSansPwd.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str):
        """Sets the user_name of this UserInfoSansPwd.


        :param user_name: The user_name of this UserInfoSansPwd.
        :type user_name: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def role(self) -> str:
        """Gets the role of this UserInfoSansPwd.


        :return: The role of this UserInfoSansPwd.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this UserInfoSansPwd.


        :param role: The role of this UserInfoSansPwd.
        :type role: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    # @property
    # def last_name(self) -> str:
    #     """Gets the last_name of this UserInfoSansPwd.


    #     :return: The last_name of this UserInfoSansPwd.
    #     :rtype: str
    #     """
    #     return self._last_name

    # @last_name.setter
    # def last_name(self, last_name: str):
    #     """Sets the last_name of this UserInfoSansPwd.


    #     :param last_name: The last_name of this UserInfoSansPwd.
    #     :type last_name: str
    #     """

    #     self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this UserInfoSansPwd.


        :return: The email of this UserInfoSansPwd.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserInfoSansPwd.


        :param email: The email of this UserInfoSansPwd.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def phone_number(self) -> str:
        """Gets the phone_number of this UserInfoSansPwd.


        :return: The phone_number of this UserInfoSansPwd.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        """Sets the phone_number of this UserInfoSansPwd.


        :param phone_number: The phone_number of this UserInfoSansPwd.
        :type phone_number: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number
