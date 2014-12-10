""" Data objects in group "External Interface"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ExternalInterface(DataObject):

    """Corresponds to IDD object `ExternalInterface` This object activates the
    external interface of EnergyPlus.

    If the object
    ExternalInterface is present, then all ExtnernalInterface:* objects will receive
    their values from the BCVTB interface or from FMUs at each zone time step.
    If this object is not present, then the values of these objects will be fixed at the
    value declared in the "initial value" field of the corresponding object, and a
    warning will be written to the EnergyPlus error file.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name of external interface',
                                       {'name': u'Name of External Interface',
                                        'pyname': u'name_of_external_interface',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'PtolemyServer',
                                                            u'FunctionalMockupUnitImport',
                                                            u'FunctionalMockupUnitExport'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 0,
               'name': u'ExternalInterface',
               'pyname': u'ExternalInterface',
               'required-object': False,
               'unique-object': False}

    @property
    def name_of_external_interface(self):
        """field `Name of External Interface`

        |  Name of External Interface
        |  Currently, the only valid entries are PtolemyServer, FunctionalMockupUnitImport, and FunctionalMockupUnitExport.

        Args:
            value (str): value for IDD Field `Name of External Interface`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name_of_external_interface` or None if not set

        """
        return self["Name of External Interface"]

    @name_of_external_interface.setter
    def name_of_external_interface(self, value=None):
        """Corresponds to IDD field `Name of External Interface`"""
        self["Name of External Interface"] = value




class ExternalInterfaceSchedule(DataObject):

    """ Corresponds to IDD object `ExternalInterface:Schedule`
        A ExternalInterface:Schedule contains only one value,
        which is used during the warm-up period and the system sizing.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 3,
               'name': u'ExternalInterface:Schedule',
               'pyname': u'ExternalInterfaceSchedule',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value




class ExternalInterfaceVariable(DataObject):

    """ Corresponds to IDD object `ExternalInterface:Variable`
        This input object is similar to EnergyManagementSystem:GlobalVariable. However, at
        the beginning of each zone time step, its value is set to the value received from the
        external interface. During the warm-up period and the system sizing, its value
        is set to the value specified by the field "initial value." This object can be used
        to move data into Erl subroutines.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 0,
               'name': u'ExternalInterface:Variable',
               'pyname': u'ExternalInterfaceVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value




class ExternalInterfaceActuator(DataObject):

    """ Corresponds to IDD object `ExternalInterface:Actuator`
        Hardware portion of EMS used to set up actuators in the model
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component unique name',
                                       {'name': u'Actuated Component Unique Name',
                                        'pyname': u'actuated_component_unique_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component type',
                                       {'name': u'Actuated Component Type',
                                        'pyname': u'actuated_component_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component control type',
                                       {'name': u'Actuated Component Control Type',
                                        'pyname': u'actuated_component_control_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'optional initial value',
                                       {'name': u'Optional Initial Value',
                                        'pyname': u'optional_initial_value',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 4,
               'name': u'ExternalInterface:Actuator',
               'pyname': u'ExternalInterfaceActuator',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set

        """
        return self["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """Corresponds to IDD field `Actuated Component Unique Name`"""
        self["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_type` or None if not set

        """
        return self["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Type`"""
        self["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_control_type` or None if not set

        """
        return self["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Control Type`"""
        self["Actuated Component Control Type"] = value

    @property
    def optional_initial_value(self):
        """field `Optional Initial Value`

        |  If specified, it is used during warm-up and system sizing.
        |  If not specified, then the actuator only overwrites the
        |  actuated component after the warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Optional Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `optional_initial_value` or None if not set

        """
        return self["Optional Initial Value"]

    @optional_initial_value.setter
    def optional_initial_value(self, value=None):
        """Corresponds to IDD field `Optional Initial Value`"""
        self["Optional Initial Value"] = value




class ExternalInterfaceFunctionalMockupUnitImport(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport`
        This object declares an FMU
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'fmu file name',
                                       {'name': u'FMU File Name',
                                        'pyname': u'fmu_file_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu timeout',
                                       {'name': u'FMU Timeout',
                                        'pyname': u'fmu_timeout',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'ms'}),
                                      (u'fmu loggingon',
                                       {'name': u'FMU LoggingOn',
                                        'pyname': u'fmu_loggingon',
                                        'default': 0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 0,
               'name': u'ExternalInterface:FunctionalMockupUnitImport',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitImport',
               'required-object': False,
               'unique-object': False}

    @property
    def fmu_file_name(self):
        """field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_file_name` or None if not set

        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """Corresponds to IDD field `FMU File Name`"""
        self["FMU File Name"] = value

    @property
    def fmu_timeout(self):
        """field `FMU Timeout`

        |  in milli-seconds
        |  Units: ms

        Args:
            value (float): value for IDD Field `FMU Timeout`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fmu_timeout` or None if not set

        """
        return self["FMU Timeout"]

    @fmu_timeout.setter
    def fmu_timeout(self, value=None):
        """Corresponds to IDD field `FMU Timeout`"""
        self["FMU Timeout"] = value

    @property
    def fmu_loggingon(self):
        """field `FMU LoggingOn`

        Args:
            value (int): value for IDD Field `FMU LoggingOn`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `fmu_loggingon` or None if not set

        """
        return self["FMU LoggingOn"]

    @fmu_loggingon.setter
    def fmu_loggingon(self, value=None):
        """Corresponds to IDD field `FMU LoggingOn`"""
        self["FMU LoggingOn"] = value




class ExternalInterfaceFunctionalMockupUnitImportFromVariable(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:From:Variable`
        This object declares an FMU input variable
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'output:variable index key name',
                                       {'name': u'Output:Variable Index Key Name',
                                        'pyname': u'outputvariable_index_key_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'output:variable name',
                                       {'name': u'Output:Variable Name',
                                        'pyname': u'outputvariable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'fmu file name',
                                       {'name': u'FMU File Name',
                                        'pyname': u'fmu_file_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fmu instance name',
                                       {'name': u'FMU Instance Name',
                                        'pyname': u'fmu_instance_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 5,
               'name': u'ExternalInterface:FunctionalMockupUnitImport:From:Variable',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitImportFromVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def outputvariable_index_key_name(self):
        """field `Output:Variable Index Key Name`


        Args:
            value (str): value for IDD Field `Output:Variable Index Key Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self["Output:Variable Index Key Name"]

    @outputvariable_index_key_name.setter
    def outputvariable_index_key_name(self, value=None):
        """  Corresponds to IDD field `Output:Variable Index Key Name`

        """
        self["Output:Variable Index Key Name"] = value

    @property
    def outputvariable_name(self):
        """field `Output:Variable Name`


        Args:
            value (str): value for IDD Field `Output:Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outputvariable_name` or None if not set
        """
        return self["Output:Variable Name"]

    @outputvariable_name.setter
    def outputvariable_name(self, value=None):
        """  Corresponds to IDD field `Output:Variable Name`

        """
        self["Output:Variable Name"] = value

    @property
    def fmu_file_name(self):
        """field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_file_name` or None if not set

        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """Corresponds to IDD field `FMU File Name`"""
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_instance_name` or None if not set

        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """Corresponds to IDD field `FMU Instance Name`"""
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value




class ExternalInterfaceFunctionalMockupUnitImportToSchedule(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits names',
                                       {'name': u'Schedule Type Limits Names',
                                        'pyname': u'schedule_type_limits_names',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fmu file name',
                                       {'name': u'FMU File Name',
                                        'pyname': u'fmu_file_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fmu instance name',
                                       {'name': u'FMU Instance Name',
                                        'pyname': u'fmu_instance_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 6,
               'name': u'ExternalInterface:FunctionalMockupUnitImport:To:Schedule',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitImportToSchedule',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def schedule_type_limits_names(self):
        """field `Schedule Type Limits Names`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Names`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_names` or None if not set

        """
        return self["Schedule Type Limits Names"]

    @schedule_type_limits_names.setter
    def schedule_type_limits_names(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Names`"""
        self["Schedule Type Limits Names"] = value

    @property
    def fmu_file_name(self):
        """field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_file_name` or None if not set

        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """Corresponds to IDD field `FMU File Name`"""
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_instance_name` or None if not set

        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """Corresponds to IDD field `FMU Instance Name`"""
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value




class ExternalInterfaceFunctionalMockupUnitImportToActuator(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component unique name',
                                       {'name': u'Actuated Component Unique Name',
                                        'pyname': u'actuated_component_unique_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component type',
                                       {'name': u'Actuated Component Type',
                                        'pyname': u'actuated_component_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component control type',
                                       {'name': u'Actuated Component Control Type',
                                        'pyname': u'actuated_component_control_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu file name',
                                       {'name': u'FMU File Name',
                                        'pyname': u'fmu_file_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fmu instance name',
                                       {'name': u'FMU Instance Name',
                                        'pyname': u'fmu_instance_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 8,
               'name': u'ExternalInterface:FunctionalMockupUnitImport:To:Actuator',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitImportToActuator',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a read-only variable for use in Erl programs
        |  no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set

        """
        return self["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """Corresponds to IDD field `Actuated Component Unique Name`"""
        self["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_type` or None if not set

        """
        return self["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Type`"""
        self["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_control_type` or None if not set

        """
        return self["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Control Type`"""
        self["Actuated Component Control Type"] = value

    @property
    def fmu_file_name(self):
        """field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_file_name` or None if not set

        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """Corresponds to IDD field `FMU File Name`"""
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_instance_name` or None if not set

        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """Corresponds to IDD field `FMU Instance Name`"""
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value




class ExternalInterfaceFunctionalMockupUnitImportToVariable(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu file name',
                                       {'name': u'FMU File Name',
                                        'pyname': u'fmu_file_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fmu instance name',
                                       {'name': u'FMU Instance Name',
                                        'pyname': u'fmu_instance_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 5,
               'name': u'ExternalInterface:FunctionalMockupUnitImport:To:Variable',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitImportToVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def fmu_file_name(self):
        """field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_file_name` or None if not set

        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """Corresponds to IDD field `FMU File Name`"""
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_instance_name` or None if not set

        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """Corresponds to IDD field `FMU Instance Name`"""
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value




class ExternalInterfaceFunctionalMockupUnitExportFromVariable(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:From:Variable`
        This object declares an FMU input variable
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'output:variable index key name',
                                       {'name': u'Output:Variable Index Key Name',
                                        'pyname': u'outputvariable_index_key_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'output:variable name',
                                       {'name': u'Output:Variable Name',
                                        'pyname': u'outputvariable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 3,
               'name': u'ExternalInterface:FunctionalMockupUnitExport:From:Variable',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitExportFromVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def outputvariable_index_key_name(self):
        """field `Output:Variable Index Key Name`


        Args:
            value (str): value for IDD Field `Output:Variable Index Key Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self["Output:Variable Index Key Name"]

    @outputvariable_index_key_name.setter
    def outputvariable_index_key_name(self, value=None):
        """  Corresponds to IDD field `Output:Variable Index Key Name`

        """
        self["Output:Variable Index Key Name"] = value

    @property
    def outputvariable_name(self):
        """field `Output:Variable Name`


        Args:
            value (str): value for IDD Field `Output:Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outputvariable_name` or None if not set
        """
        return self["Output:Variable Name"]

    @outputvariable_name.setter
    def outputvariable_name(self, value=None):
        """  Corresponds to IDD field `Output:Variable Name`

        """
        self["Output:Variable Name"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value




class ExternalInterfaceFunctionalMockupUnitExportToSchedule(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits names',
                                       {'name': u'Schedule Type Limits Names',
                                        'pyname': u'schedule_type_limits_names',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 4,
               'name': u'ExternalInterface:FunctionalMockupUnitExport:To:Schedule',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitExportToSchedule',
               'required-object': False,
               'unique-object': False}

    @property
    def schedule_name(self):
        """field `Schedule Name`

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def schedule_type_limits_names(self):
        """field `Schedule Type Limits Names`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Names`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_names` or None if not set

        """
        return self["Schedule Type Limits Names"]

    @schedule_type_limits_names.setter
    def schedule_type_limits_names(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Names`"""
        self["Schedule Type Limits Names"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value




class ExternalInterfaceFunctionalMockupUnitExportToActuator(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component unique name',
                                       {'name': u'Actuated Component Unique Name',
                                        'pyname': u'actuated_component_unique_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component type',
                                       {'name': u'Actuated Component Type',
                                        'pyname': u'actuated_component_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component control type',
                                       {'name': u'Actuated Component Control Type',
                                        'pyname': u'actuated_component_control_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 6,
               'name': u'ExternalInterface:FunctionalMockupUnitExport:To:Actuator',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitExportToActuator',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a read-only variable for use in Erl programs
        |  no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set

        """
        return self["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """Corresponds to IDD field `Actuated Component Unique Name`"""
        self["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_type` or None if not set

        """
        return self["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Type`"""
        self["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_control_type` or None if not set

        """
        return self["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Control Type`"""
        self["Actuated Component Control Type"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value




class ExternalInterfaceFunctionalMockupUnitExportToVariable(DataObject):

    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fmu variable name',
                                       {'name': u'FMU Variable Name',
                                        'pyname': u'fmu_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'initial value',
                                       {'name': u'Initial Value',
                                        'pyname': u'initial_value',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'External Interface',
               'min-fields': 3,
               'name': u'ExternalInterface:FunctionalMockupUnitExport:To:Variable',
               'pyname': u'ExternalInterfaceFunctionalMockupUnitExportToVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def fmu_variable_name(self):
        """field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fmu_variable_name` or None if not set

        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """Corresponds to IDD field `FMU Variable Name`"""
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """field `Initial Value`

        |  Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_value` or None if not set

        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """Corresponds to IDD field `Initial Value`"""
        self["Initial Value"] = value


