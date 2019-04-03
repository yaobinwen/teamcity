# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.branch import Branch  # noqa: F401,E501


class Branches(TeamCityObject):
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
        'href': 'str',
        'branch': 'list[Branch]'
    }

    attribute_map = {
        'count': 'count',
        'href': 'href',
        'branch': 'branch'
    }

    def __init__(self, count=None, href=None, branch=None, teamcity=None):  # noqa: E501
        """Branches - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._href = None
        self._branch = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if branch is not None:
            self.branch = branch
        super(Branches, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this Branches.  # noqa: E501


        :return: The count of this Branches.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Branches.


        :param count: The count of this Branches.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this Branches.  # noqa: E501


        :return: The href of this Branches.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Branches.


        :param href: The href of this Branches.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def branch(self):
        """Gets the branch of this Branches.  # noqa: E501


        :return: The branch of this Branches.  # noqa: E501
        :rtype: list[Branch]
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this Branches.


        :param branch: The branch of this Branches.  # noqa: E501
        :type: list[Branch]
        """

        self._branch = branch