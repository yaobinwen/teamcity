# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.agent_requirements import AgentRequirements  # noqa: F401,E501
# from dohq_teamcity.models.agents import Agents  # noqa: F401,E501
# from dohq_teamcity.models.artifact_dependencies import ArtifactDependencies  # noqa: F401,E501
# from dohq_teamcity.models.branches import Branches  # noqa: F401,E501
# from dohq_teamcity.models.build_type import BuildType  # noqa: F401,E501
# from dohq_teamcity.models.build_types import BuildTypes  # noqa: F401,E501
# from dohq_teamcity.models.builds import Builds  # noqa: F401,E501
# from dohq_teamcity.models.features import Features  # noqa: F401,E501
# from dohq_teamcity.models.investigations import Investigations  # noqa: F401,E501
# from dohq_teamcity.models.links import Links  # noqa: F401,E501
# from dohq_teamcity.models.project import Project  # noqa: F401,E501
# from dohq_teamcity.models.properties import Properties  # noqa: F401,E501
# from dohq_teamcity.models.snapshot_dependencies import SnapshotDependencies  # noqa: F401,E501
# from dohq_teamcity.models.steps import Steps  # noqa: F401,E501
# from dohq_teamcity.models.triggers import Triggers  # noqa: F401,E501
# from dohq_teamcity.models.vcs_root_entries import VcsRootEntries  # noqa: F401,E501
# from dohq_teamcity.models.vcs_root_instances import VcsRootInstances  # noqa: F401,E501


class BuildType(TeamCityObject):
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
        'internal_id': 'str',
        'name': 'str',
        'template_flag': 'bool',
        'type': 'str',
        'paused': 'bool',
        'uuid': 'str',
        'description': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'project_internal_id': 'str',
        'href': 'str',
        'web_url': 'str',
        'inherited': 'bool',
        'links': 'Links',
        'project': 'Project',
        'templates': 'BuildTypes',
        'template': 'BuildType',
        'vcs_root_entries': 'VcsRootEntries',
        'settings': 'Properties',
        'parameters': 'Properties',
        'steps': 'Steps',
        'features': 'Features',
        'triggers': 'Triggers',
        'snapshot_dependencies': 'SnapshotDependencies',
        'artifact_dependencies': 'ArtifactDependencies',
        'agent_requirements': 'AgentRequirements',
        'branches': 'Branches',
        'builds': 'Builds',
        'investigations': 'Investigations',
        'compatible_agents': 'Agents',
        'vcs_root_instances': 'VcsRootInstances',
        'locator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'internal_id': 'internalId',
        'name': 'name',
        'template_flag': 'templateFlag',
        'type': 'type',
        'paused': 'paused',
        'uuid': 'uuid',
        'description': 'description',
        'project_name': 'projectName',
        'project_id': 'projectId',
        'project_internal_id': 'projectInternalId',
        'href': 'href',
        'web_url': 'webUrl',
        'inherited': 'inherited',
        'links': 'links',
        'project': 'project',
        'templates': 'templates',
        'template': 'template',
        'vcs_root_entries': 'vcs-root-entries',
        'settings': 'settings',
        'parameters': 'parameters',
        'steps': 'steps',
        'features': 'features',
        'triggers': 'triggers',
        'snapshot_dependencies': 'snapshot-dependencies',
        'artifact_dependencies': 'artifact-dependencies',
        'agent_requirements': 'agent-requirements',
        'branches': 'branches',
        'builds': 'builds',
        'investigations': 'investigations',
        'compatible_agents': 'compatibleAgents',
        'vcs_root_instances': 'vcsRootInstances',
        'locator': 'locator'
    }

    def __init__(self, id=None, internal_id=None, name=None, template_flag=False, type=None, paused=False, uuid=None, description=None, project_name=None, project_id=None, project_internal_id=None, href=None, web_url=None, inherited=False, links=None, project=None, templates=None, template=None, vcs_root_entries=None, settings=None, parameters=None, steps=None, features=None, triggers=None, snapshot_dependencies=None, artifact_dependencies=None, agent_requirements=None, branches=None, builds=None, investigations=None, compatible_agents=None, vcs_root_instances=None, locator=None, teamcity=None):  # noqa: E501
        """BuildType - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._internal_id = None
        self._name = None
        self._template_flag = None
        self._type = None
        self._paused = None
        self._uuid = None
        self._description = None
        self._project_name = None
        self._project_id = None
        self._project_internal_id = None
        self._href = None
        self._web_url = None
        self._inherited = None
        self._links = None
        self._project = None
        self._templates = None
        self._template = None
        self._vcs_root_entries = None
        self._settings = None
        self._parameters = None
        self._steps = None
        self._features = None
        self._triggers = None
        self._snapshot_dependencies = None
        self._artifact_dependencies = None
        self._agent_requirements = None
        self._branches = None
        self._builds = None
        self._investigations = None
        self._compatible_agents = None
        self._vcs_root_instances = None
        self._locator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if internal_id is not None:
            self.internal_id = internal_id
        if name is not None:
            self.name = name
        if template_flag is not None:
            self.template_flag = template_flag
        if type is not None:
            self.type = type
        if paused is not None:
            self.paused = paused
        if uuid is not None:
            self.uuid = uuid
        if description is not None:
            self.description = description
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if project_internal_id is not None:
            self.project_internal_id = project_internal_id
        if href is not None:
            self.href = href
        if web_url is not None:
            self.web_url = web_url
        if inherited is not None:
            self.inherited = inherited
        if links is not None:
            self.links = links
        if project is not None:
            self.project = project
        if templates is not None:
            self.templates = templates
        if template is not None:
            self.template = template
        if vcs_root_entries is not None:
            self.vcs_root_entries = vcs_root_entries
        if settings is not None:
            self.settings = settings
        if parameters is not None:
            self.parameters = parameters
        if steps is not None:
            self.steps = steps
        if features is not None:
            self.features = features
        if triggers is not None:
            self.triggers = triggers
        if snapshot_dependencies is not None:
            self.snapshot_dependencies = snapshot_dependencies
        if artifact_dependencies is not None:
            self.artifact_dependencies = artifact_dependencies
        if agent_requirements is not None:
            self.agent_requirements = agent_requirements
        if branches is not None:
            self.branches = branches
        if builds is not None:
            self.builds = builds
        if investigations is not None:
            self.investigations = investigations
        if compatible_agents is not None:
            self.compatible_agents = compatible_agents
        if vcs_root_instances is not None:
            self.vcs_root_instances = vcs_root_instances
        if locator is not None:
            self.locator = locator
        super(BuildType, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this BuildType.  # noqa: E501


        :return: The id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BuildType.


        :param id: The id of this BuildType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_id(self):
        """Gets the internal_id of this BuildType.  # noqa: E501


        :return: The internal_id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this BuildType.


        :param internal_id: The internal_id of this BuildType.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def name(self):
        """Gets the name of this BuildType.  # noqa: E501


        :return: The name of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildType.


        :param name: The name of this BuildType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def template_flag(self):
        """Gets the template_flag of this BuildType.  # noqa: E501


        :return: The template_flag of this BuildType.  # noqa: E501
        :rtype: bool
        """
        return self._template_flag

    @template_flag.setter
    def template_flag(self, template_flag):
        """Sets the template_flag of this BuildType.


        :param template_flag: The template_flag of this BuildType.  # noqa: E501
        :type: bool
        """

        self._template_flag = template_flag

    @property
    def type(self):
        """Gets the type of this BuildType.  # noqa: E501


        :return: The type of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BuildType.


        :param type: The type of this BuildType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def paused(self):
        """Gets the paused of this BuildType.  # noqa: E501


        :return: The paused of this BuildType.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this BuildType.


        :param paused: The paused of this BuildType.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def uuid(self):
        """Gets the uuid of this BuildType.  # noqa: E501


        :return: The uuid of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this BuildType.


        :param uuid: The uuid of this BuildType.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def description(self):
        """Gets the description of this BuildType.  # noqa: E501


        :return: The description of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BuildType.


        :param description: The description of this BuildType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_name(self):
        """Gets the project_name of this BuildType.  # noqa: E501


        :return: The project_name of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this BuildType.


        :param project_name: The project_name of this BuildType.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this BuildType.  # noqa: E501


        :return: The project_id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BuildType.


        :param project_id: The project_id of this BuildType.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_internal_id(self):
        """Gets the project_internal_id of this BuildType.  # noqa: E501


        :return: The project_internal_id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._project_internal_id

    @project_internal_id.setter
    def project_internal_id(self, project_internal_id):
        """Sets the project_internal_id of this BuildType.


        :param project_internal_id: The project_internal_id of this BuildType.  # noqa: E501
        :type: str
        """

        self._project_internal_id = project_internal_id

    @property
    def href(self):
        """Gets the href of this BuildType.  # noqa: E501


        :return: The href of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BuildType.


        :param href: The href of this BuildType.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def web_url(self):
        """Gets the web_url of this BuildType.  # noqa: E501


        :return: The web_url of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this BuildType.


        :param web_url: The web_url of this BuildType.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    @property
    def inherited(self):
        """Gets the inherited of this BuildType.  # noqa: E501


        :return: The inherited of this BuildType.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this BuildType.


        :param inherited: The inherited of this BuildType.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

    @property
    def links(self):
        """Gets the links of this BuildType.  # noqa: E501


        :return: The links of this BuildType.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BuildType.


        :param links: The links of this BuildType.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def project(self):
        """Gets the project of this BuildType.  # noqa: E501


        :return: The project of this BuildType.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this BuildType.


        :param project: The project of this BuildType.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def templates(self):
        """Gets the templates of this BuildType.  # noqa: E501


        :return: The templates of this BuildType.  # noqa: E501
        :rtype: BuildTypes
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this BuildType.


        :param templates: The templates of this BuildType.  # noqa: E501
        :type: BuildTypes
        """

        self._templates = templates

    @property
    def template(self):
        """Gets the template of this BuildType.  # noqa: E501


        :return: The template of this BuildType.  # noqa: E501
        :rtype: BuildType
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this BuildType.


        :param template: The template of this BuildType.  # noqa: E501
        :type: BuildType
        """

        self._template = template

    @property
    def vcs_root_entries(self):
        """Gets the vcs_root_entries of this BuildType.  # noqa: E501


        :return: The vcs_root_entries of this BuildType.  # noqa: E501
        :rtype: VcsRootEntries
        """
        return self._vcs_root_entries

    @vcs_root_entries.setter
    def vcs_root_entries(self, vcs_root_entries):
        """Sets the vcs_root_entries of this BuildType.


        :param vcs_root_entries: The vcs_root_entries of this BuildType.  # noqa: E501
        :type: VcsRootEntries
        """

        self._vcs_root_entries = vcs_root_entries

    @property
    def settings(self):
        """Gets the settings of this BuildType.  # noqa: E501


        :return: The settings of this BuildType.  # noqa: E501
        :rtype: Properties
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this BuildType.


        :param settings: The settings of this BuildType.  # noqa: E501
        :type: Properties
        """

        self._settings = settings

    @property
    def parameters(self):
        """Gets the parameters of this BuildType.  # noqa: E501


        :return: The parameters of this BuildType.  # noqa: E501
        :rtype: Properties
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BuildType.


        :param parameters: The parameters of this BuildType.  # noqa: E501
        :type: Properties
        """

        self._parameters = parameters

    @property
    def steps(self):
        """Gets the steps of this BuildType.  # noqa: E501


        :return: The steps of this BuildType.  # noqa: E501
        :rtype: Steps
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this BuildType.


        :param steps: The steps of this BuildType.  # noqa: E501
        :type: Steps
        """

        self._steps = steps

    @property
    def features(self):
        """Gets the features of this BuildType.  # noqa: E501


        :return: The features of this BuildType.  # noqa: E501
        :rtype: Features
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BuildType.


        :param features: The features of this BuildType.  # noqa: E501
        :type: Features
        """

        self._features = features

    @property
    def triggers(self):
        """Gets the triggers of this BuildType.  # noqa: E501


        :return: The triggers of this BuildType.  # noqa: E501
        :rtype: Triggers
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this BuildType.


        :param triggers: The triggers of this BuildType.  # noqa: E501
        :type: Triggers
        """

        self._triggers = triggers

    @property
    def snapshot_dependencies(self):
        """Gets the snapshot_dependencies of this BuildType.  # noqa: E501


        :return: The snapshot_dependencies of this BuildType.  # noqa: E501
        :rtype: SnapshotDependencies
        """
        return self._snapshot_dependencies

    @snapshot_dependencies.setter
    def snapshot_dependencies(self, snapshot_dependencies):
        """Sets the snapshot_dependencies of this BuildType.


        :param snapshot_dependencies: The snapshot_dependencies of this BuildType.  # noqa: E501
        :type: SnapshotDependencies
        """

        self._snapshot_dependencies = snapshot_dependencies

    @property
    def artifact_dependencies(self):
        """Gets the artifact_dependencies of this BuildType.  # noqa: E501


        :return: The artifact_dependencies of this BuildType.  # noqa: E501
        :rtype: ArtifactDependencies
        """
        return self._artifact_dependencies

    @artifact_dependencies.setter
    def artifact_dependencies(self, artifact_dependencies):
        """Sets the artifact_dependencies of this BuildType.


        :param artifact_dependencies: The artifact_dependencies of this BuildType.  # noqa: E501
        :type: ArtifactDependencies
        """

        self._artifact_dependencies = artifact_dependencies

    @property
    def agent_requirements(self):
        """Gets the agent_requirements of this BuildType.  # noqa: E501


        :return: The agent_requirements of this BuildType.  # noqa: E501
        :rtype: AgentRequirements
        """
        return self._agent_requirements

    @agent_requirements.setter
    def agent_requirements(self, agent_requirements):
        """Sets the agent_requirements of this BuildType.


        :param agent_requirements: The agent_requirements of this BuildType.  # noqa: E501
        :type: AgentRequirements
        """

        self._agent_requirements = agent_requirements

    @property
    def branches(self):
        """Gets the branches of this BuildType.  # noqa: E501


        :return: The branches of this BuildType.  # noqa: E501
        :rtype: Branches
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        """Sets the branches of this BuildType.


        :param branches: The branches of this BuildType.  # noqa: E501
        :type: Branches
        """

        self._branches = branches

    @property
    def builds(self):
        """Gets the builds of this BuildType.  # noqa: E501


        :return: The builds of this BuildType.  # noqa: E501
        :rtype: Builds
        """
        return self._builds

    @builds.setter
    def builds(self, builds):
        """Sets the builds of this BuildType.


        :param builds: The builds of this BuildType.  # noqa: E501
        :type: Builds
        """

        self._builds = builds

    @property
    def investigations(self):
        """Gets the investigations of this BuildType.  # noqa: E501


        :return: The investigations of this BuildType.  # noqa: E501
        :rtype: Investigations
        """
        return self._investigations

    @investigations.setter
    def investigations(self, investigations):
        """Sets the investigations of this BuildType.


        :param investigations: The investigations of this BuildType.  # noqa: E501
        :type: Investigations
        """

        self._investigations = investigations

    @property
    def compatible_agents(self):
        """Gets the compatible_agents of this BuildType.  # noqa: E501


        :return: The compatible_agents of this BuildType.  # noqa: E501
        :rtype: Agents
        """
        return self._compatible_agents

    @compatible_agents.setter
    def compatible_agents(self, compatible_agents):
        """Sets the compatible_agents of this BuildType.


        :param compatible_agents: The compatible_agents of this BuildType.  # noqa: E501
        :type: Agents
        """

        self._compatible_agents = compatible_agents

    @property
    def vcs_root_instances(self):
        """Gets the vcs_root_instances of this BuildType.  # noqa: E501


        :return: The vcs_root_instances of this BuildType.  # noqa: E501
        :rtype: VcsRootInstances
        """
        return self._vcs_root_instances

    @vcs_root_instances.setter
    def vcs_root_instances(self, vcs_root_instances):
        """Sets the vcs_root_instances of this BuildType.


        :param vcs_root_instances: The vcs_root_instances of this BuildType.  # noqa: E501
        :type: VcsRootInstances
        """

        self._vcs_root_instances = vcs_root_instances

    @property
    def locator(self):
        """Gets the locator of this BuildType.  # noqa: E501


        :return: The locator of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this BuildType.


        :param locator: The locator of this BuildType.  # noqa: E501
        :type: str
        """

        self._locator = locator