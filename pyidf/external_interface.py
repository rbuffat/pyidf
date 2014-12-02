from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

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
    required_fields = ["Name of External Interface"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface`
        """
        self._data = OrderedDict()
        self._data["Name of External Interface"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name_of_external_interface = None
        else:
            self.name_of_external_interface = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name_of_external_interface(self):
        """Get name_of_external_interface

        Returns:
            str: the value of `name_of_external_interface` or None if not set
        """
        return self._data["Name of External Interface"]

    @name_of_external_interface.setter
    def name_of_external_interface(self, value=None):
        """  Corresponds to IDD Field `Name of External Interface`
        Name of External Interface
        Currently, the only valid entries are PtolemyServer, FunctionalMockupUnitImport, and FunctionalMockupUnitExport.

        Args:
            value (str): value for IDD Field `Name of External Interface`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterface.name_of_external_interface`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterface.name_of_external_interface`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterface.name_of_external_interface`')
            vals = {}
            vals["ptolemyserver"] = "PtolemyServer"
            vals["functionalmockupunitimport"] = "FunctionalMockupUnitImport"
            vals["functionalmockupunitexport"] = "FunctionalMockupUnitExport"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ExternalInterface.name_of_external_interface`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ExternalInterface.name_of_external_interface`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Name of External Interface"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterface:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterface:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterface: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterface: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceSchedule(object):
    """ Corresponds to IDD object `ExternalInterface:Schedule`
        A ExternalInterface:Schedule contains only one value,
        which is used during the warm-up period and the system sizing.
    """
    internal_name = "ExternalInterface:Schedule"
    field_count = 3
    required_fields = ["Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:Schedule`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceSchedule.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceSchedule.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceSchedule.name`')
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
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceSchedule.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceSchedule.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceSchedule.schedule_type_limits_name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceSchedule.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceSchedule:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceSchedule:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceSchedule: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceSchedule: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:Variable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceVariable.name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during warm-up and system sizing.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceVariable.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceVariable: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceActuator(object):
    """ Corresponds to IDD object `ExternalInterface:Actuator`
        Hardware portion of EMS used to set up actuators in the model
    """
    internal_name = "ExternalInterface:Actuator"
    field_count = 5
    required_fields = ["Name", "Actuated Component Unique Name", "Actuated Component Type", "Actuated Component Control Type"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None
        self._data["Optional Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_unique_name = None
        else:
            self.actuated_component_unique_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_type = None
        else:
            self.actuated_component_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_control_type = None
        else:
            self.actuated_component_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.optional_initial_value = None
        else:
            self.optional_initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceActuator.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceActuator.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceActuator.name`')
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
        """  Corresponds to IDD Field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceActuator.actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceActuator.actuated_component_unique_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceActuator.actuated_component_unique_name`')
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
        """  Corresponds to IDD Field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceActuator.actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceActuator.actuated_component_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceActuator.actuated_component_type`')
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
        """  Corresponds to IDD Field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceActuator.actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceActuator.actuated_component_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceActuator.actuated_component_control_type`')
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
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceActuator.optional_initial_value`'.format(value))
        self._data["Optional Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceActuator:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceActuator:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceActuator: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceActuator: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitImport(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport`
        This object declares an FMU
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport"
    field_count = 3
    required_fields = ["FMU File Name", "FMU Timeout", "FMU LoggingOn"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitImport`
        """
        self._data = OrderedDict()
        self._data["FMU File Name"] = None
        self._data["FMU Timeout"] = None
        self._data["FMU LoggingOn"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_timeout = None
        else:
            self.fmu_timeout = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_loggingon = None
        else:
            self.fmu_loggingon = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def fmu_file_name(self):
        """Get fmu_file_name

        Returns:
            str: the value of `fmu_file_name` or None if not set
        """
        return self._data["FMU File Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImport.fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImport.fmu_file_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImport.fmu_file_name`')
        self._data["FMU File Name"] = value

    @property
    def fmu_timeout(self):
        """Get fmu_timeout

        Returns:
            float: the value of `fmu_timeout` or None if not set
        """
        return self._data["FMU Timeout"]

    @fmu_timeout.setter
    def fmu_timeout(self, value=0.0):
        """  Corresponds to IDD Field `FMU Timeout`
        in milli-seconds

        Args:
            value (float): value for IDD Field `FMU Timeout`
                Units: ms
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImport.fmu_timeout`'.format(value))
        self._data["FMU Timeout"] = value

    @property
    def fmu_loggingon(self):
        """Get fmu_loggingon

        Returns:
            int: the value of `fmu_loggingon` or None if not set
        """
        return self._data["FMU LoggingOn"]

    @fmu_loggingon.setter
    def fmu_loggingon(self, value=0):
        """  Corresponds to IDD Field `FMU LoggingOn`

        Args:
            value (int): value for IDD Field `FMU LoggingOn`
                Default value: 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ExternalInterfaceFunctionalMockupUnitImport.fmu_loggingon`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ExternalInterfaceFunctionalMockupUnitImport.fmu_loggingon`'.format(value))
        self._data["FMU LoggingOn"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitImport:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitImport:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImport: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImport: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitImportFromVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:From:Variable`
        This object declares an FMU input variable
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:From:Variable"
    field_count = 5
    required_fields = ["Output:Variable Index Key Name", "Output:Variable Name", "FMU File Name", "FMU Instance Name", "FMU Variable Name"]
    extensible_fields = 0
    format = None
    min_fields = 5
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitImport:From:Variable`
        """
        self._data = OrderedDict()
        self._data["Output:Variable Index Key Name"] = None
        self._data["Output:Variable Name"] = None
        self._data["FMU File Name"] = None
        self._data["FMU Instance Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.outputvariable_index_key_name = None
        else:
            self.outputvariable_index_key_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outputvariable_name = None
        else:
            self.outputvariable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def outputvariable_index_key_name(self):
        """Get outputvariable_index_key_name

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self._data["Output:Variable Index Key Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.outputvariable_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.outputvariable_index_key_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.outputvariable_index_key_name`')
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
        """  Corresponds to IDD Field `Output:Variable Name`

        Args:
            value (str): value for IDD Field `Output:Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.outputvariable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.outputvariable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.outputvariable_name`')
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
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_file_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_file_name`')
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
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_instance_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_instance_name`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportFromVariable.fmu_variable_name`')
        self._data["FMU Variable Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitImportFromVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitImportFromVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportFromVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportFromVariable: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitImportToSchedule(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:To:Schedule"
    field_count = 6
    required_fields = ["Name", "FMU File Name", "FMU Instance Name", "FMU Variable Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 6
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitImport:To:Schedule`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Names"] = None
        self._data["FMU File Name"] = None
        self._data["FMU Instance Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_type_limits_names = None
        else:
            self.schedule_type_limits_names = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.name`')
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
        """  Corresponds to IDD Field `Schedule Type Limits Names`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.schedule_type_limits_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.schedule_type_limits_names`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.schedule_type_limits_names`')
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
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_file_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_file_name`')
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
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_instance_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_instance_name`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.fmu_variable_name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToSchedule.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitImportToSchedule:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitImportToSchedule:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportToSchedule: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportToSchedule: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitImportToActuator(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:To:Actuator"
    field_count = 8
    required_fields = ["Name", "Actuated Component Unique Name", "Actuated Component Type", "Actuated Component Control Type", "FMU File Name", "FMU Instance Name", "FMU Variable Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 8
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitImport:To:Actuator`
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
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_unique_name = None
        else:
            self.actuated_component_unique_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_type = None
        else:
            self.actuated_component_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_control_type = None
        else:
            self.actuated_component_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.name`')
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
        """  Corresponds to IDD Field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_unique_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_unique_name`')
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
        """  Corresponds to IDD Field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_type`')
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
        """  Corresponds to IDD Field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.actuated_component_control_type`')
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
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_file_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_file_name`')
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
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_instance_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_instance_name`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.fmu_variable_name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToActuator.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitImportToActuator:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitImportToActuator:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportToActuator: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportToActuator: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitImportToVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitImport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitImport:To:Variable"
    field_count = 5
    required_fields = ["Name", "FMU File Name", "FMU Instance Name", "FMU Variable Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 5
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitImport:To:Variable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["FMU File Name"] = None
        self._data["FMU Instance Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_file_name = None
        else:
            self.fmu_file_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_instance_name = None
        else:
            self.fmu_instance_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.name`')
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
        """  Corresponds to IDD Field `FMU File Name`

        Args:
            value (str): value for IDD Field `FMU File Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_file_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_file_name`')
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
        """  Corresponds to IDD Field `FMU Instance Name`

        Args:
            value (str): value for IDD Field `FMU Instance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_instance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_instance_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_instance_name`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.fmu_variable_name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitImportToVariable.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitImportToVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitImportToVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportToVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitImportToVariable: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitExportFromVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:From:Variable`
        This object declares an FMU input variable
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:From:Variable"
    field_count = 3
    required_fields = ["Output:Variable Index Key Name", "Output:Variable Name", "FMU Variable Name"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitExport:From:Variable`
        """
        self._data = OrderedDict()
        self._data["Output:Variable Index Key Name"] = None
        self._data["Output:Variable Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.outputvariable_index_key_name = None
        else:
            self.outputvariable_index_key_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outputvariable_name = None
        else:
            self.outputvariable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def outputvariable_index_key_name(self):
        """Get outputvariable_index_key_name

        Returns:
            str: the value of `outputvariable_index_key_name` or None if not set
        """
        return self._data["Output:Variable Index Key Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.outputvariable_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.outputvariable_index_key_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.outputvariable_index_key_name`')
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
        """  Corresponds to IDD Field `Output:Variable Name`

        Args:
            value (str): value for IDD Field `Output:Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.outputvariable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.outputvariable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.outputvariable_name`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportFromVariable.fmu_variable_name`')
        self._data["FMU Variable Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitExportFromVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitExportFromVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportFromVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportFromVariable: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitExportToSchedule(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Schedule`
        This objects contains only one value, which is used during the first
        call of EnergyPlus
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:To:Schedule"
    field_count = 4
    required_fields = ["Schedule Name", "FMU Variable Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitExport:To:Schedule`
        """
        self._data = OrderedDict()
        self._data["Schedule Name"] = None
        self._data["Schedule Type Limits Names"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_type_limits_names = None
        else:
            self.schedule_type_limits_names = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.schedule_name`')
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
        """  Corresponds to IDD Field `Schedule Type Limits Names`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.schedule_type_limits_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.schedule_type_limits_names`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.schedule_type_limits_names`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.fmu_variable_name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToSchedule.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitExportToSchedule:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitExportToSchedule:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportToSchedule: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportToSchedule: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitExportToActuator(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Actuator`
        Hardware portion of EMS used to set up actuators in the model
        that are dynamically updated from the FMU.
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:To:Actuator"
    field_count = 6
    required_fields = ["Name", "Actuated Component Unique Name", "Actuated Component Type", "Actuated Component Control Type", "FMU Variable Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 6
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitExport:To:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_unique_name = None
        else:
            self.actuated_component_unique_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_type = None
        else:
            self.actuated_component_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuated_component_control_type = None
        else:
            self.actuated_component_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.name`')
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
        """  Corresponds to IDD Field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_unique_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_unique_name`')
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
        """  Corresponds to IDD Field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_type`')
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
        """  Corresponds to IDD Field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.actuated_component_control_type`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.fmu_variable_name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToActuator.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitExportToActuator:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitExportToActuator:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportToActuator: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportToActuator: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ExternalInterfaceFunctionalMockupUnitExportToVariable(object):
    """ Corresponds to IDD object `ExternalInterface:FunctionalMockupUnitExport:To:Variable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    internal_name = "ExternalInterface:FunctionalMockupUnitExport:To:Variable"
    field_count = 3
    required_fields = ["Name", "FMU Variable Name", "Initial Value"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ExternalInterface:FunctionalMockupUnitExport:To:Variable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["FMU Variable Name"] = None
        self._data["Initial Value"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fmu_variable_name = None
        else:
            self.fmu_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_value = None
        else:
            self.initial_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToVariable.name`')
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
        """  Corresponds to IDD Field `FMU Variable Name`

        Args:
            value (str): value for IDD Field `FMU Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToVariable.fmu_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToVariable.fmu_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExternalInterfaceFunctionalMockupUnitExportToVariable.fmu_variable_name`')
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
        """  Corresponds to IDD Field `Initial Value`
        Used during the first call of EnergyPlus.

        Args:
            value (float): value for IDD Field `Initial Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ExternalInterfaceFunctionalMockupUnitExportToVariable.initial_value`'.format(value))
        self._data["Initial Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ExternalInterfaceFunctionalMockupUnitExportToVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExternalInterfaceFunctionalMockupUnitExportToVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportToVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExternalInterfaceFunctionalMockupUnitExportToVariable: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])