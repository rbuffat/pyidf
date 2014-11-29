from collections import OrderedDict

class ExternalInterface(object):
    """ Corresponds to IDD object `ExternalInterface`
        This object activates the external interface of EnergyPlus. If the object
        ExternalInterface is present, then all ExtnernalInterface:* objects will receive
        their values from the BCVTB interface or from FMUs at each zone time step.
        If this object is not present, then the values of these objects will be fixed at the
        value declared in the "initial value" field of the corresponding object, and a
        warning will be written to the EnergyPlus error file.
    """
    internal_name = "ExternalInterface"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface`
        """
        self._data = OrderedDict()
        self._data["Name of External Interface"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name_of_external_interface = None
        else:
            self.name_of_external_interface = vals[i]
        i += 1

    @property
    def name_of_external_interface(self):
        """Get name_of_external_interface

        Returns:
            str: the value of `name_of_external_interface` or None if not set
        """
        return self._data["Name of External Interface"]

    @name_of_external_interface.setter
    def name_of_external_interface(self, value=None):
        """  Corresponds to IDD Field `name_of_external_interface`
        Name of External Interface
        Currently, the only valid entries are PtolemyServer, FunctionalMockupUnitImport, and FunctionalMockupUnitExport.

        Args:
            value (str): value for IDD Field `name_of_external_interface`
                Accepted values are:
                      - PtolemyServer
                      - FunctionalMockupUnitImport
                      - FunctionalMockupUnitExport
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name_of_external_interface`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name_of_external_interface`')
            vals = set()
            vals.add("PtolemyServer")
            vals.add("FunctionalMockupUnitImport")
            vals.add("FunctionalMockupUnitExport")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `name_of_external_interface`'.format(value))

        self._data["Name of External Interface"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name_of_external_interface))
        return ",".join(out)

class ExternalInterfaceSchedule(object):
    """ Corresponds to IDD object `ExternalInterface:Schedule`
        A ExternalInterface:Schedule contains only one value,
        which is used during the warm-up period and the system sizing.
    """
    internal_name = "ExternalInterface:Schedule"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:Schedule`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `schedule_type_limits_name`

        Args:
            value (str): value for IDD Field `schedule_type_limits_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_type_limits_name`')

        self._data["Schedule Type Limits Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_type_limits_name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)

class ExternalInterfaceVariable(object):
    """ Corresponds to IDD object `ExternalInterface:Variable`
        This input object is similar to EnergyManagementSystem:GlobalVariable. However, at
        the beginning of each zone time step, its value is set to the value received from the
        external interface. During the warm-up period and the system sizing, its value
        is set to the value specified by the field "initial value." This object can be used
        to move data into Erl subroutines.
    """
    internal_name = "ExternalInterface:Variable"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:Variable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)

class ExternalInterfaceActuator(object):
    """ Corresponds to IDD object `ExternalInterface:Actuator`
        Hardware portion of EMS used to set up actuators in the model
    """
    internal_name = "ExternalInterface:Actuator"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None
        self._data["Optional Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_unique_name = None
        else:
            self.actuated_component_unique_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_type = None
        else:
            self.actuated_component_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_control_type = None
        else:
            self.actuated_component_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optional_initial_value = None
        else:
            self.optional_initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """Get actuated_component_unique_name

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set
        """
        return self._data["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """  Corresponds to IDD Field `actuated_component_unique_name`

        Args:
            value (str): value for IDD Field `actuated_component_unique_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_unique_name`')

        self._data["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """Get actuated_component_type

        Returns:
            str: the value of `actuated_component_type` or None if not set
        """
        return self._data["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_type`

        Args:
            value (str): value for IDD Field `actuated_component_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_type`')

        self._data["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """Get actuated_component_control_type

        Returns:
            str: the value of `actuated_component_control_type` or None if not set
        """
        return self._data["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_control_type`

        Args:
            value (str): value for IDD Field `actuated_component_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_control_type`')

        self._data["Actuated Component Control Type"] = value

    @property
    def optional_initial_value(self):
        """Get optional_initial_value

        Returns:
            float: the value of `optional_initial_value` or None if not set
        """
        return self._data["Optional Initial Value"]

    @optional_initial_value.setter
    def optional_initial_value(self, value=None):
        """  Corresponds to IDD Field `optional_initial_value`
        If specified, it is used during warm-up and system sizing.
        If not specified, then the actuator only overwrites the
        actuated component after the warm-up and system sizing.

        Args:
            value (float): value for IDD Field `optional_initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `optional_initial_value`'.format(value))

        self._data["Optional Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.actuated_component_unique_name))
        out.append(self._to_str(self.actuated_component_type))
        out.append(self._to_str(self.actuated_component_control_type))
        out.append(self._to_str(self.optional_initial_value))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitImport(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport`
        This object declares an FMU
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitImport`
        """
        self._data = OrderedDict()
        self._data["FMU File Name"] = None
        self._data["FMU Timeout"] = None
        self._data["FMU LoggingOn"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_timeout = None
        else:
            self.fmu_timeout = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_loggingon = None
        else:
            self.fmu_loggingon = vals[i]
        i += 1

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self._data["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `fmu_file_name`

        Args:
            value (str): value for IDD Field `fmu_file_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_file_name`')

        self._data["FMU File Name"] = value

    @property
    def fmu_timeout(self):
        """Get fmu_timeout

        Returns:
            float: the value of `fmu_timeout` or None if not set
        """
        return self._data["FMU Timeout"]

    @fmu_timeout.setter
    def fmu_timeout(self, value=0.0 ):
        """  Corresponds to IDD Field `fmu_timeout`
        in milli-seconds

        Args:
            value (float): value for IDD Field `fmu_timeout`
                Unit: ms
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fmu_timeout`'.format(value))

        self._data["FMU Timeout"] = value

    @property
    def fmu_loggingon(self):
        """Get fmu_loggingon

        Returns:
            int: the value of `fmu_loggingon` or None if not set
        """
        return self._data["FMU LoggingOn"]

    @fmu_loggingon.setter
    def fmu_loggingon(self, value=0 ):
        """  Corresponds to IDD Field `fmu_loggingon`

        Args:
            value (int): value for IDD Field `fmu_loggingon`
                Default value: 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `fmu_loggingon`'.format(value))

        self._data["FMU LoggingOn"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.fmu_file_name))
        out.append(self._to_str(self.fmu_timeout))
        out.append(self._to_str(self.fmu_loggingon))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitImportFromVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:From:Variable`
        This object declares an FMU input variable
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:From:Variable"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitImport:From:Variable`
        """
        self._data = OrderedDict()
        self._data["Output:Variable Index Key Name"] = None
        self._data["Output:Variable Name"] = None
        self._data["FMU File Name"] = None
        self._data["FMU Instance Name"] = None
        self._data["FMU Variable Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.outputvariable_index_key_name = None
        else:
            self.outputvariable_index_key_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outputvariable_name = None
        else:
            self.outputvariable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1

    @property
    def outputvariable_index_key_name(self):
        """Get outputvariable_index_key_name

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self._data["Output:Variable Index Key Name"]

    @outputvariable_index_key_name.setter
    def outputvariable_index_key_name(self, value=None):
        """  Corresponds to IDD Field `outputvariable_index_key_name`

        Args:
            value (str): value for IDD Field `outputvariable_index_key_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_index_key_name`')

        self._data["Output:Variable Index Key Name"] = value

    @property
    def outputvariable_name(self):
        """Get outputvariable_name

        Returns:
            str: the value of `outputvariable_name` or None if not set
        """
        return self._data["Output:Variable Name"]

    @outputvariable_name.setter
    def outputvariable_name(self, value=None):
        """  Corresponds to IDD Field `outputvariable_name`

        Args:
            value (str): value for IDD Field `outputvariable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_name`')

        self._data["Output:Variable Name"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self._data["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `fmu_file_name`

        Args:
            value (str): value for IDD Field `fmu_file_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_file_name`')

        self._data["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self._data["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `fmu_instance_name`

        Args:
            value (str): value for IDD Field `fmu_instance_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_instance_name`')

        self._data["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.outputvariable_index_key_name))
        out.append(self._to_str(self.outputvariable_name))
        out.append(self._to_str(self.fmu_file_name))
        out.append(self._to_str(self.fmu_instance_name))
        out.append(self._to_str(self.fmu_variable_name))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitImportToSchedule(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:To:Schedule"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitImport:To:Schedule`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Names"] = None
        self._data["FMU File Name"] = None
        self._data["FMU Instance Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_type_limits_names = None
        else:
            self.schedule_type_limits_names = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def schedule_type_limits_names(self):
        """Get schedule_type_limits_names

        Returns:
            str: the value of `schedule_type_limits_names` or None if not set
        """
        return self._data["Schedule Type Limits Names"]

    @schedule_type_limits_names.setter
    def schedule_type_limits_names(self, value=None):
        """  Corresponds to IDD Field `schedule_type_limits_names`

        Args:
            value (str): value for IDD Field `schedule_type_limits_names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_type_limits_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_type_limits_names`')

        self._data["Schedule Type Limits Names"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self._data["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `fmu_file_name`

        Args:
            value (str): value for IDD Field `fmu_file_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_file_name`')

        self._data["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self._data["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `fmu_instance_name`

        Args:
            value (str): value for IDD Field `fmu_instance_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_instance_name`')

        self._data["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_type_limits_names))
        out.append(self._to_str(self.fmu_file_name))
        out.append(self._to_str(self.fmu_instance_name))
        out.append(self._to_str(self.fmu_variable_name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitImportToActuator(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:To:Actuator"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitImport:To:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None
        self._data["FMU File Name"] = None
        self._data["FMU Instance Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_unique_name = None
        else:
            self.actuated_component_unique_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_type = None
        else:
            self.actuated_component_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_control_type = None
        else:
            self.actuated_component_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a read-only variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """Get actuated_component_unique_name

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set
        """
        return self._data["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """  Corresponds to IDD Field `actuated_component_unique_name`

        Args:
            value (str): value for IDD Field `actuated_component_unique_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_unique_name`')

        self._data["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """Get actuated_component_type

        Returns:
            str: the value of `actuated_component_type` or None if not set
        """
        return self._data["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_type`

        Args:
            value (str): value for IDD Field `actuated_component_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_type`')

        self._data["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """Get actuated_component_control_type

        Returns:
            str: the value of `actuated_component_control_type` or None if not set
        """
        return self._data["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_control_type`

        Args:
            value (str): value for IDD Field `actuated_component_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_control_type`')

        self._data["Actuated Component Control Type"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self._data["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `fmu_file_name`

        Args:
            value (str): value for IDD Field `fmu_file_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_file_name`')

        self._data["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self._data["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `fmu_instance_name`

        Args:
            value (str): value for IDD Field `fmu_instance_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_instance_name`')

        self._data["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.actuated_component_unique_name))
        out.append(self._to_str(self.actuated_component_type))
        out.append(self._to_str(self.actuated_component_control_type))
        out.append(self._to_str(self.fmu_file_name))
        out.append(self._to_str(self.fmu_instance_name))
        out.append(self._to_str(self.fmu_variable_name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitImportToVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:To:Variable"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitImport:To:Variable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["FMU File Name"] = None
        self._data["FMU Instance Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self._data["FMU File Name"]

    @fmu_file_name.setter
    def fmu_file_name(self, value=None):
        """  Corresponds to IDD Field `fmu_file_name`

        Args:
            value (str): value for IDD Field `fmu_file_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_file_name`')

        self._data["FMU File Name"] = value

    @property
    def fmu_instance_name(self):
        """Get fmu_instance_name

        Returns:
            str: the value of `fmu_instance_name` or None if not set
        """
        return self._data["FMU Instance Name"]

    @fmu_instance_name.setter
    def fmu_instance_name(self, value=None):
        """  Corresponds to IDD Field `fmu_instance_name`

        Args:
            value (str): value for IDD Field `fmu_instance_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_instance_name`')

        self._data["FMU Instance Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.fmu_file_name))
        out.append(self._to_str(self.fmu_instance_name))
        out.append(self._to_str(self.fmu_variable_name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitExportFromVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:From:Variable`
        This object declares an FMU input variable
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:From:Variable"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitExport:From:Variable`
        """
        self._data = OrderedDict()
        self._data["Output:Variable Index Key Name"] = None
        self._data["Output:Variable Name"] = None
        self._data["FMU Variable Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.outputvariable_index_key_name = None
        else:
            self.outputvariable_index_key_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outputvariable_name = None
        else:
            self.outputvariable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1

    @property
    def outputvariable_index_key_name(self):
        """Get outputvariable_index_key_name

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self._data["Output:Variable Index Key Name"]

    @outputvariable_index_key_name.setter
    def outputvariable_index_key_name(self, value=None):
        """  Corresponds to IDD Field `outputvariable_index_key_name`

        Args:
            value (str): value for IDD Field `outputvariable_index_key_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_index_key_name`')

        self._data["Output:Variable Index Key Name"] = value

    @property
    def outputvariable_name(self):
        """Get outputvariable_name

        Returns:
            str: the value of `outputvariable_name` or None if not set
        """
        return self._data["Output:Variable Name"]

    @outputvariable_name.setter
    def outputvariable_name(self, value=None):
        """  Corresponds to IDD Field `outputvariable_name`

        Args:
            value (str): value for IDD Field `outputvariable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_name`')

        self._data["Output:Variable Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.outputvariable_index_key_name))
        out.append(self._to_str(self.outputvariable_name))
        out.append(self._to_str(self.fmu_variable_name))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitExportToSchedule(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:To:Schedule"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitExport:To:Schedule`
        """
        self._data = OrderedDict()
        self._data["Schedule Name"] = None
        self._data["Schedule Type Limits Names"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_type_limits_names = None
        else:
            self.schedule_type_limits_names = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`

        Args:
            value (str): value for IDD Field `schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def schedule_type_limits_names(self):
        """Get schedule_type_limits_names

        Returns:
            str: the value of `schedule_type_limits_names` or None if not set
        """
        return self._data["Schedule Type Limits Names"]

    @schedule_type_limits_names.setter
    def schedule_type_limits_names(self, value=None):
        """  Corresponds to IDD Field `schedule_type_limits_names`

        Args:
            value (str): value for IDD Field `schedule_type_limits_names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_type_limits_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_type_limits_names`')

        self._data["Schedule Type Limits Names"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.schedule_type_limits_names))
        out.append(self._to_str(self.fmu_variable_name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitExportToActuator(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:To:Actuator"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitExport:To:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_unique_name = None
        else:
            self.actuated_component_unique_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_type = None
        else:
            self.actuated_component_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_control_type = None
        else:
            self.actuated_component_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a read-only variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """Get actuated_component_unique_name

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set
        """
        return self._data["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """  Corresponds to IDD Field `actuated_component_unique_name`

        Args:
            value (str): value for IDD Field `actuated_component_unique_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_unique_name`')

        self._data["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """Get actuated_component_type

        Returns:
            str: the value of `actuated_component_type` or None if not set
        """
        return self._data["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_type`

        Args:
            value (str): value for IDD Field `actuated_component_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_type`')

        self._data["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """Get actuated_component_control_type

        Returns:
            str: the value of `actuated_component_control_type` or None if not set
        """
        return self._data["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_control_type`

        Args:
            value (str): value for IDD Field `actuated_component_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_control_type`')

        self._data["Actuated Component Control Type"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.actuated_component_unique_name))
        out.append(self._to_str(self.actuated_component_type))
        out.append(self._to_str(self.actuated_component_control_type))
        out.append(self._to_str(self.fmu_variable_name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)

class ExternalInterfaceFunctionalMockupUnitExportToVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:To:Variable"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ExternalInterface:FunctionalMockupUnitExport:To:Variable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def fmu_variable_name(self):
        """Get fmu_variable_name

        Returns:
            str: the value of `fmu_variable_name` or None if not set
        """
        return self._data["FMU Variable Name"]

    @fmu_variable_name.setter
    def fmu_variable_name(self, value=None):
        """  Corresponds to IDD Field `fmu_variable_name`

        Args:
            value (str): value for IDD Field `fmu_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fmu_variable_name`')

        self._data["FMU Variable Name"] = value

    @property
    def initial_value(self):
        """Get initial_value

        Returns:
            float: the value of `initial_value` or None if not set
        """
        return self._data["Initial Value"]

    @initial_value.setter
    def initial_value(self, value=None):
        """  Corresponds to IDD Field `initial_value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `initial_value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_value`'.format(value))

        self._data["Initial Value"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.fmu_variable_name))
        out.append(self._to_str(self.initial_value))
        return ",".join(out)