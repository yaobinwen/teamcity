# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.file_change import FileChange  # noqa: F401,E501


class FileChanges(TeamCityObject):
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
        'count': 'int',
        'file': 'list[FileChange]'
    }

    attribute_map = {
        'count': 'count',
        'file': 'file'
    }

    def __init__(self, count=None, file=None, teamcity=None):  # noqa: E501
        """FileChanges - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._file = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if file is not None:
            self.file = file
        super(FileChanges, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this FileChanges.  # noqa: E501


        :return: The count of this FileChanges.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this FileChanges.


        :param count: The count of this FileChanges.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def file(self):
        """Gets the file of this FileChanges.  # noqa: E501


        :return: The file of this FileChanges.  # noqa: E501
        :rtype: list[FileChange]
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileChanges.


        :param file: The file of this FileChanges.  # noqa: E501
        :type: list[FileChange]
        """

        self._file = file
