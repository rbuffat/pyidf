from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ExternalInterface(DataObject):
    """ Corresponds to IDD object `ExternalInterface`
        This object activates the external interface of EnergyPlus. If the object
        ExternalInterface is present, then all ExtnernalInterface:* objects will receive
        their values from the BCVTB interface or from FMUs at each zone time step.
        If this object is not present, then the values of these objects will be fixed at the
        value declared in the "initial value" field of the corresponding object, and a
        warning will be written to the EnergyPlus error file.
    """
    schema = {'min-fields': 0, 'name': u'ExternalInterface', 'pyname': u'ExternalInterface', 'format': None, 'fields': OrderedDict([(u'name of external interface', {'name': u'Name of External Interface', 'pyname': u'name_of_external_interface', 'required-field': True, 'autosizable': False, 'accepted-values': [u'PtolemyServer', u'FunctionalMockupUnitImport', u'FunctionalMockupUnitExport'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name_of_external_interface(self):
        """Get name_of_external_interface

        Returns:
            str: the value of `name_of_external_interface` or None if not set
        """
        return self["Name of External Interface"]

    @name_of_external_interface.setter
    def name_of_external_interface(self, value=None):
        """  Corresponds to IDD Field `Name of External Interface`
        Name of External Interface
        Currently, the only valid entries are PtolemyServer, FunctionalMockupUnitImport, and FunctionalMockupUnitExport.

        Args:
            value (str): value for IDD Field `Name of External Interface`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name of External Interface"] = value


class ExternalInterfaceSchedule(DataObject):
    """ Corresponds to IDD object `ExternalInterface:Schedule`
        A ExternalInterface:Schedule contains only one value,
        which is used during the warm-up period and the system sizing.
    """
    schema = {'min-fields': 3, 'name': u'ExternalInterface:Schedule', 'pyname': u'ExternalInterfaceSchedule', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'schedule type limits name', {'name': u'Schedule Type Limits Name', 'pyname': u'schedule_type_limits_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Schedule Type Limits Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value


class ExternalInterfaceVariable(DataObject):
    """ Corresponds to IDD object `ExternalInterface:Variable`
        This input object is similar to EnergyManagementSystem:GlobalVariable. However, at
        the beginning of each zone time step, its value is set to the value received from the
        external interface. During the warm-up period and the system sizing, its value
        is set to the value specified by the field "initial value." This object can be used
        to move data into Erl subroutines.
    """
    schema = {'min-fields': 0, 'name': u'ExternalInterface:Variable', 'pyname': u'ExternalInterfaceVariable', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value


class ExternalInterfaceActuator(DataObject):
    """ Corresponds to IDD object `ExternalInterface:Actuator`
        Hardware portion of EMS used to set up actuators in the model
    """
    schema = {'min-fields': 4, 'name': u'ExternalInterface:Actuator', 'pyname': u'ExternalInterfaceActuator', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component unique name', {'name': u'Actuated Component Unique Name', 'pyname': u'actuated_component_unique_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component type', {'name': u'Actuated Component Type', 'pyname': u'actuated_component_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component control type', {'name': u'Actuated Component Control Type', 'pyname': u'actuated_component_control_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'optional initial value', {'name': u'Optional Initial Value', 'pyname': u'optional_initial_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """Get actuated_component_unique_name

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set
        """
        return self["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """Get actuated_component_type

        Returns:
            str: the value of `actuated_component_type` or None if not set
        """
        return self["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """Get actuated_component_control_type

        Returns:
            str: the value of `actuated_component_control_type` or None if not set
        """
        return self["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Control Type"] = value

    @property
    def optional_initial_value(self):
        """Get optional_initial_value

        Returns:
            float: the value of `optional_initial_value` or None if not set
        """
        return self["Optional Initial Value"]

    @optional_initial_value.setter
    def optional_initial_value(self, value=None):
        """  Corresponds to IDD Field `Optional Initial Value`
        If specified, it is used during warm-up and system sizing.
        If not specified, then the actuator only overwrites the
        actuated component after the warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Optional Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Optional Initial Value"] = value


class ExternalInterfaceFunctionalMockupUnitImport(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport`
        This object declares an FMU
    """
    schema = {'min-fields': 0, 'name': u'ExternalInterface:FunctionalMockupUnitImport', 'pyname': u'ExternalInterfaceFunctionalMockupUnitImport', 'format': None, 'fields': OrderedDict([(u'fmu file name', {'name': u'FMU File Name', 'pyname': u'fmu_file_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu timeout', {'name': u'FMU Timeout', 'pyname': u'fmu_timeout', 'default': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'ms'}), (u'fmu loggingon', {'name': u'FMU LoggingOn', 'pyname': u'fmu_loggingon', 'default': 0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU File Name"] = value

    @property
    def fmu_timeout(self):
        """Get fmu_timeout

        Returns:
            float: the value of `fmu_timeout` or None if not set
        """
        return self["FMU Timeout"]

    @fmu_timeout.setter
    def fmu_timeout(self, value=None):
        """  Corresponds to IDD Field `FMU Timeout`
        in milli-seconds

        Args:
            value (float): value for IDD Field `FMU Timeout`
                Units: ms
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Timeout"] = value

    @property
    def fmu_loggingon(self):
        """Get fmu_loggingon

        Returns:
            int: the value of `fmu_loggingon` or None if not set
        """
        return self["FMU LoggingOn"]

    @fmu_loggingon.setter
    def fmu_loggingon(self, value=None):
        """  Corresponds to IDD Field `FMU LoggingOn`

        Args:
            value (int): value for IDD Field `FMU LoggingOn`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU LoggingOn"] = value


class ExternalInterfaceFunctionalMockupUnitImportFromVariable(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:From:Variable`
        This object declares an FMU input variable
    """
    schema = {'min-fields': 5, 'name': u'ExternalInterface:FunctionalMockupUnitImport:From:Variable', 'pyname': u'ExternalInterfaceFunctionalMockupUnitImportFromVariable', 'format': None, 'fields': OrderedDict([(u'output:variable index key name', {'name': u'Output:Variable Index Key Name', 'pyname': u'outputvariable_index_key_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'output:variable name', {'name': u'Output:Variable Name', 'pyname': u'outputvariable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'external-list'}), (u'fmu file name', {'name': u'FMU File Name', 'pyname': u'fmu_file_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fmu instance name', {'name': u'FMU Instance Name', 'pyname': u'fmu_instance_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def outputvariable_index_key_name(self):
        """Get outputvariable_index_key_name

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self["Output:Variable Index Key Name"]

    @outputvariable_index_key_name.setter
    def outputvariable_index_key_name(self, value=None):
        """  Corresponds to IDD Field `Output:Variable Index Key Name`

        Args:
            value (str): value for IDD Field `Output:Variable Index Key Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Output:Variable Index Key Name"] = value

    @property
    def outputvariable_name(self):
        """Get outputvariable_name

        Returns:
            str: the value of `outputvariable_name` or None if not set
        """
        return self["Output:Variable Name"]

    @outputvariable_name.setter
    def outputvariable_name(self, value=None):
        """  Corresponds to IDD Field `Output:Variable Name`

        Args:
            value (str): value for IDD Field `Output:Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Output:Variable Name"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value


class ExternalInterfaceFunctionalMockupUnitImportToSchedule(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    schema = {'min-fields': 6, 'name': u'ExternalInterface:FunctionalMockupUnitImport:To:Schedule', 'pyname': u'ExternalInterfaceFunctionalMockupUnitImportToSchedule', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'schedule type limits names', {'name': u'Schedule Type Limits Names', 'pyname': u'schedule_type_limits_names', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fmu file name', {'name': u'FMU File Name', 'pyname': u'fmu_file_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fmu instance name', {'name': u'FMU Instance Name', 'pyname': u'fmu_instance_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def schedule_type_limits_names(self):
        """Get schedule_type_limits_names

        Returns:
            str: the value of `schedule_type_limits_names` or None if not set
        """
        return self["Schedule Type Limits Names"]

    @schedule_type_limits_names.setter
    def schedule_type_limits_names(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Names`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Schedule Type Limits Names"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value


class ExternalInterfaceFunctionalMockupUnitImportToActuator(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    schema = {'min-fields': 8, 'name': u'ExternalInterface:FunctionalMockupUnitImport:To:Actuator', 'pyname': u'ExternalInterfaceFunctionalMockupUnitImportToActuator', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component unique name', {'name': u'Actuated Component Unique Name', 'pyname': u'actuated_component_unique_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component type', {'name': u'Actuated Component Type', 'pyname': u'actuated_component_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component control type', {'name': u'Actuated Component Control Type', 'pyname': u'actuated_component_control_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu file name', {'name': u'FMU File Name', 'pyname': u'fmu_file_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fmu instance name', {'name': u'FMU Instance Name', 'pyname': u'fmu_instance_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        This name becomes a read-only variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """Get actuated_component_unique_name

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set
        """
        return self["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """Get actuated_component_type

        Returns:
            str: the value of `actuated_component_type` or None if not set
        """
        return self["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """Get actuated_component_control_type

        Returns:
            str: the value of `actuated_component_control_type` or None if not set
        """
        return self["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Control Type"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value


class ExternalInterfaceFunctionalMockupUnitImportToVariable(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    schema = {'min-fields': 5, 'name': u'ExternalInterface:FunctionalMockupUnitImport:To:Variable', 'pyname': u'ExternalInterfaceFunctionalMockupUnitImportToVariable', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu file name', {'name': u'FMU File Name', 'pyname': u'fmu_file_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fmu instance name', {'name': u'FMU Instance Name', 'pyname': u'fmu_instance_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value


class ExternalInterfaceFunctionalMockupUnitExportFromVariable(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:From:Variable`
        This object declares an FMU input variable
    """
    schema = {'min-fields': 3, 'name': u'ExternalInterface:FunctionalMockupUnitExport:From:Variable', 'pyname': u'ExternalInterfaceFunctionalMockupUnitExportFromVariable', 'format': None, 'fields': OrderedDict([(u'output:variable index key name', {'name': u'Output:Variable Index Key Name', 'pyname': u'outputvariable_index_key_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'output:variable name', {'name': u'Output:Variable Name', 'pyname': u'outputvariable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'external-list'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def outputvariable_index_key_name(self):
        """Get outputvariable_index_key_name

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self["Output:Variable Index Key Name"]

    @outputvariable_index_key_name.setter
    def outputvariable_index_key_name(self, value=None):
        """  Corresponds to IDD Field `Output:Variable Index Key Name`

        Args:
            value (str): value for IDD Field `Output:Variable Index Key Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Output:Variable Index Key Name"] = value

    @property
    def outputvariable_name(self):
        """Get outputvariable_name

        Returns:
            str: the value of `outputvariable_name` or None if not set
        """
        return self["Output:Variable Name"]

    @outputvariable_name.setter
    def outputvariable_name(self, value=None):
        """  Corresponds to IDD Field `Output:Variable Name`

        Args:
            value (str): value for IDD Field `Output:Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Output:Variable Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value


class ExternalInterfaceFunctionalMockupUnitExportToSchedule(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    schema = {'min-fields': 4, 'name': u'ExternalInterface:FunctionalMockupUnitExport:To:Schedule', 'pyname': u'ExternalInterfaceFunctionalMockupUnitExportToSchedule', 'format': None, 'fields': OrderedDict([(u'schedule name', {'name': u'Schedule Name', 'pyname': u'schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'schedule type limits names', {'name': u'Schedule Type Limits Names', 'pyname': u'schedule_type_limits_names', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`

        Args:
            value (str): value for IDD Field `Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Schedule Name"] = value

    @property
    def schedule_type_limits_names(self):
        """Get schedule_type_limits_names

        Returns:
            str: the value of `schedule_type_limits_names` or None if not set
        """
        return self["Schedule Type Limits Names"]

    @schedule_type_limits_names.setter
    def schedule_type_limits_names(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Names`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Schedule Type Limits Names"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value


class ExternalInterfaceFunctionalMockupUnitExportToActuator(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    schema = {'min-fields': 6, 'name': u'ExternalInterface:FunctionalMockupUnitExport:To:Actuator', 'pyname': u'ExternalInterfaceFunctionalMockupUnitExportToActuator', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component unique name', {'name': u'Actuated Component Unique Name', 'pyname': u'actuated_component_unique_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component type', {'name': u'Actuated Component Type', 'pyname': u'actuated_component_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'actuated component control type', {'name': u'Actuated Component Control Type', 'pyname': u'actuated_component_control_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        This name becomes a read-only variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """Get actuated_component_unique_name

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set
        """
        return self["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """Get actuated_component_type

        Returns:
            str: the value of `actuated_component_type` or None if not set
        """
        return self["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """Get actuated_component_control_type

        Returns:
            str: the value of `actuated_component_control_type` or None if not set
        """
        return self["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """  Corresponds to IDD Field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Actuated Component Control Type"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value


class ExternalInterfaceFunctionalMockupUnitExportToVariable(DataObject):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    schema = {'min-fields': 3, 'name': u'ExternalInterface:FunctionalMockupUnitExport:To:Variable', 'pyname': u'ExternalInterfaceFunctionalMockupUnitExportToVariable', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fmu variable name', {'name': u'FMU Variable Name', 'pyname': u'fmu_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'initial value', {'name': u'Initial Value', 'pyname': u'initial_value', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' External Interface'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Value"] = value