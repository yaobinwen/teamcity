# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class Environment(TeamCityObject):
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
        'os_type': 'str'
    }

    attribute_map = {
        'os_type': 'osType'
    }

    def __init__(self, os_type=None, teamcity=None):  # noqa: E501
        """Environment - a model defined in Swagger"""  # noqa: E501

        self._os_type = None
        self.discriminator = None

        if os_type is not None:
            self.os_type = os_type
        super(Environment, self).__init__(teamcity=teamcity)

    @property
    def os_type(self):
        """Gets the os_type of this Environment.  # noqa: E501


        :return: The os_type of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this Environment.


        :param os_type: The os_type of this Environment.  # noqa: E501
        :type: str
        """

        self._os_type = os_type
