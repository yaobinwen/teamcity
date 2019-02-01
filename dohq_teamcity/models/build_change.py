# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.build import Build  # noqa: F401,E501


class BuildChange(TeamCityObject):
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
        'next_build': 'Build',
        'prev_build': 'Build'
    }

    attribute_map = {
        'next_build': 'nextBuild',
        'prev_build': 'prevBuild'
    }

    def __init__(self, next_build=None, prev_build=None, teamcity=None):  # noqa: E501
        """BuildChange - a model defined in Swagger"""  # noqa: E501

        self._next_build = None
        self._prev_build = None
        self.discriminator = None

        if next_build is not None:
            self.next_build = next_build
        if prev_build is not None:
            self.prev_build = prev_build
        super(BuildChange, self).__init__(teamcity=teamcity)

    @property
    def next_build(self):
        """Gets the next_build of this BuildChange.  # noqa: E501


        :return: The next_build of this BuildChange.  # noqa: E501
        :rtype: Build
        """
        return self._next_build

    @next_build.setter
    def next_build(self, next_build):
        """Sets the next_build of this BuildChange.


        :param next_build: The next_build of this BuildChange.  # noqa: E501
        :type: Build
        """

        self._next_build = next_build

    @property
    def prev_build(self):
        """Gets the prev_build of this BuildChange.  # noqa: E501


        :return: The prev_build of this BuildChange.  # noqa: E501
        :rtype: Build
        """
        return self._prev_build

    @prev_build.setter
    def prev_build(self, prev_build):
        """Sets the prev_build of this BuildChange.


        :param prev_build: The prev_build of this BuildChange.  # noqa: E501
        :type: Build
        """

        self._prev_build = prev_build
