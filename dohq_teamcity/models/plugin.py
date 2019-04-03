# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.properties import Properties  # noqa: F401,E501


class Plugin(TeamCityObject):
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
        'name': 'str',
        'display_name': 'str',
        'version': 'str',
        'load_path': 'str',
        'parameters': 'Properties'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'version': 'version',
        'load_path': 'loadPath',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, display_name=None, version=None, load_path=None, parameters=None, teamcity=None):  # noqa: E501
        """Plugin - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._display_name = None
        self._version = None
        self._load_path = None
        self._parameters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if version is not None:
            self.version = version
        if load_path is not None:
            self.load_path = load_path
        if parameters is not None:
            self.parameters = parameters
        super(Plugin, self).__init__(teamcity=teamcity)

    @property
    def name(self):
        """Gets the name of this Plugin.  # noqa: E501


        :return: The name of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plugin.


        :param name: The name of this Plugin.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Plugin.  # noqa: E501


        :return: The display_name of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Plugin.


        :param display_name: The display_name of this Plugin.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def version(self):
        """Gets the version of this Plugin.  # noqa: E501


        :return: The version of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Plugin.


        :param version: The version of this Plugin.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def load_path(self):
        """Gets the load_path of this Plugin.  # noqa: E501


        :return: The load_path of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._load_path

    @load_path.setter
    def load_path(self, load_path):
        """Sets the load_path of this Plugin.


        :param load_path: The load_path of this Plugin.  # noqa: E501
        :type: str
        """

        self._load_path = load_path

    @property
    def parameters(self):
        """Gets the parameters of this Plugin.  # noqa: E501


        :return: The parameters of this Plugin.  # noqa: E501
        :rtype: Properties
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Plugin.


        :param parameters: The parameters of this Plugin.  # noqa: E501
        :type: Properties
        """

        self._parameters = parameters