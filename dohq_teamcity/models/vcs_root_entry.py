# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.vcs_root import VcsRoot  # noqa: F401,E501


class VcsRootEntry(TeamCityObject):
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
        'checkout_rules': 'str',
        'id': 'str',
        'inherited': 'bool',
        'vcs_root': 'VcsRoot'
    }

    attribute_map = {
        'checkout_rules': 'checkout-rules',
        'id': 'id',
        'inherited': 'inherited',
        'vcs_root': 'vcs-root'
    }

    def __init__(self, checkout_rules=None, id=None, inherited=False, vcs_root=None, teamcity=None):  # noqa: E501
        """VcsRootEntry - a model defined in Swagger"""  # noqa: E501

        self._checkout_rules = None
        self._id = None
        self._inherited = None
        self._vcs_root = None
        self.discriminator = None

        if checkout_rules is not None:
            self.checkout_rules = checkout_rules
        if id is not None:
            self.id = id
        if inherited is not None:
            self.inherited = inherited
        if vcs_root is not None:
            self.vcs_root = vcs_root
        super(VcsRootEntry, self).__init__(teamcity=teamcity)

    @property
    def checkout_rules(self):
        """Gets the checkout_rules of this VcsRootEntry.  # noqa: E501


        :return: The checkout_rules of this VcsRootEntry.  # noqa: E501
        :rtype: str
        """
        return self._checkout_rules

    @checkout_rules.setter
    def checkout_rules(self, checkout_rules):
        """Sets the checkout_rules of this VcsRootEntry.


        :param checkout_rules: The checkout_rules of this VcsRootEntry.  # noqa: E501
        :type: str
        """

        self._checkout_rules = checkout_rules

    @property
    def id(self):
        """Gets the id of this VcsRootEntry.  # noqa: E501


        :return: The id of this VcsRootEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcsRootEntry.


        :param id: The id of this VcsRootEntry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inherited(self):
        """Gets the inherited of this VcsRootEntry.  # noqa: E501


        :return: The inherited of this VcsRootEntry.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this VcsRootEntry.


        :param inherited: The inherited of this VcsRootEntry.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

    @property
    def vcs_root(self):
        """Gets the vcs_root of this VcsRootEntry.  # noqa: E501


        :return: The vcs_root of this VcsRootEntry.  # noqa: E501
        :rtype: VcsRoot
        """
        return self._vcs_root

    @vcs_root.setter
    def vcs_root(self, vcs_root):
        """Sets the vcs_root of this VcsRootEntry.


        :param vcs_root: The vcs_root of this VcsRootEntry.  # noqa: E501
        :type: VcsRoot
        """

        self._vcs_root = vcs_root

