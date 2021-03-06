# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.entries import Entries  # noqa: F401,E501


class MetaData(TeamCityObject):
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
        'entries': 'Entries'
    }

    attribute_map = {
        'id': 'id',
        'entries': 'entries'
    }

    def __init__(self, id=None, entries=None, teamcity=None):  # noqa: E501
        """MetaData - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._entries = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if entries is not None:
            self.entries = entries
        super(MetaData, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this MetaData.  # noqa: E501


        :return: The id of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetaData.


        :param id: The id of this MetaData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def entries(self):
        """Gets the entries of this MetaData.  # noqa: E501


        :return: The entries of this MetaData.  # noqa: E501
        :rtype: Entries
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this MetaData.


        :param entries: The entries of this MetaData.  # noqa: E501
        :type: Entries
        """

        self._entries = entries
