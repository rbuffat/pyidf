from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class EnergyManagementSystemSensor(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Sensor`
        Declares EMS variable as a sensor
        a list of output variables and meters that can be reported are available after a run on
        the report (.rdd) or meter dictionary file (.mdd) if the Output:VariableDictionary
        has been requested.
    """
    internal_name = "EnergyManagementSystem:Sensor"
    field_count = 3
    required_fields = ["Name", "Output:Variable or Output:Meter Name"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:Sensor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Output:Variable or Output:Meter Index Key Name"] = None
        self._data["Output:Variable or Output:Meter Name"] = None
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
            self.outputvariable_or_outputmeter_index_key_name = None
        else:
            self.outputvariable_or_outputmeter_index_key_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outputvariable_or_outputmeter_name = None
        else:
            self.outputvariable_or_outputmeter_name = vals[i]
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
                                 ' for field `EnergyManagementSystemSensor.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemSensor.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemSensor.name`')
        self._data["Name"] = value

    @property
    def outputvariable_or_outputmeter_index_key_name(self):
        """Get outputvariable_or_outputmeter_index_key_name

        Returns:
            str: the value of `outputvariable_or_outputmeter_index_key_name` or None if not set
        """
        return self._data["Output:Variable or Output:Meter Index Key Name"]

    @outputvariable_or_outputmeter_index_key_name.setter
    def outputvariable_or_outputmeter_index_key_name(self, value=None):
        """  Corresponds to IDD Field `Output:Variable or Output:Meter Index Key Name`

        Args:
            value (str): value for IDD Field `Output:Variable or Output:Meter Index Key Name`
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
                                 ' for field `EnergyManagementSystemSensor.outputvariable_or_outputmeter_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemSensor.outputvariable_or_outputmeter_index_key_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemSensor.outputvariable_or_outputmeter_index_key_name`')
        self._data["Output:Variable or Output:Meter Index Key Name"] = value

    @property
    def outputvariable_or_outputmeter_name(self):
        """Get outputvariable_or_outputmeter_name

        Returns:
            str: the value of `outputvariable_or_outputmeter_name` or None if not set
        """
        return self._data["Output:Variable or Output:Meter Name"]

    @outputvariable_or_outputmeter_name.setter
    def outputvariable_or_outputmeter_name(self, value=None):
        """  Corresponds to IDD Field `Output:Variable or Output:Meter Name`

        Args:
            value (str): value for IDD Field `Output:Variable or Output:Meter Name`
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
                                 ' for field `EnergyManagementSystemSensor.outputvariable_or_outputmeter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemSensor.outputvariable_or_outputmeter_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemSensor.outputvariable_or_outputmeter_name`')
        self._data["Output:Variable or Output:Meter Name"] = value

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
                    raise ValueError("Required field EnergyManagementSystemSensor:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemSensor:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemSensor: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemSensor: {} / {}".format(out_fields,
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

class EnergyManagementSystemActuator(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Actuator`
        Hardware portion of EMS used to set up actuators in the model
    """
    internal_name = "EnergyManagementSystem:Actuator"
    field_count = 4
    required_fields = ["Name", "Actuated Component Unique Name", "Actuated Component Type", "Actuated Component Control Type"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None
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
                                 ' for field `EnergyManagementSystemActuator.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemActuator.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemActuator.name`')
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
                                 ' for field `EnergyManagementSystemActuator.actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemActuator.actuated_component_unique_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemActuator.actuated_component_unique_name`')
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
                                 ' for field `EnergyManagementSystemActuator.actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemActuator.actuated_component_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemActuator.actuated_component_type`')
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
                                 ' for field `EnergyManagementSystemActuator.actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemActuator.actuated_component_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemActuator.actuated_component_control_type`')
        self._data["Actuated Component Control Type"] = value

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
                    raise ValueError("Required field EnergyManagementSystemActuator:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemActuator:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemActuator: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemActuator: {} / {}".format(out_fields,
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

class EnergyManagementSystemProgramCallingManager(object):
    """ Corresponds to IDD object `EnergyManagementSystem:ProgramCallingManager`
        Input EMS program. a program needs a name
        a description of when it should be called
        and then lines of program code for EMS Runtime language
    """
    internal_name = "EnergyManagementSystem:ProgramCallingManager"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 3
    extensible_keys = ["Program Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:ProgramCallingManager`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EnergyPlus Model Calling Point"] = None
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
            self.energyplus_model_calling_point = None
        else:
            self.energyplus_model_calling_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `EnergyManagementSystemProgramCallingManager.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemProgramCallingManager.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemProgramCallingManager.name`')
        self._data["Name"] = value

    @property
    def energyplus_model_calling_point(self):
        """Get energyplus_model_calling_point

        Returns:
            str: the value of `energyplus_model_calling_point` or None if not set
        """
        return self._data["EnergyPlus Model Calling Point"]

    @energyplus_model_calling_point.setter
    def energyplus_model_calling_point(self, value=None):
        """  Corresponds to IDD Field `EnergyPlus Model Calling Point`

        Args:
            value (str): value for IDD Field `EnergyPlus Model Calling Point`
                Accepted values are:
                      - BeginNewEnvironment
                      - AfterNewEnvironmentWarmUpIsComplete
                      - BeginTimestepBeforePredictor
                      - AfterPredictorBeforeHVACManagers
                      - AfterPredictorAfterHVACManagers
                      - InsideHVACSystemIterationLoop
                      - EndOfZoneTimestepBeforeZoneReporting
                      - EndOfZoneTimestepAfterZoneReporting
                      - EndOfSystemTimestepBeforeHVACReporting
                      - EndOfSystemTimestepAfterHVACReporting
                      - EndOfZoneSizing
                      - EndOfSystemSizing
                      - AfterComponentInputReadIn
                      - UserDefinedComponentModel
                      - UnitarySystemSizing
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
                                 ' for field `EnergyManagementSystemProgramCallingManager.energyplus_model_calling_point`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemProgramCallingManager.energyplus_model_calling_point`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemProgramCallingManager.energyplus_model_calling_point`')
            vals = {}
            vals["beginnewenvironment"] = "BeginNewEnvironment"
            vals["afternewenvironmentwarmupiscomplete"] = "AfterNewEnvironmentWarmUpIsComplete"
            vals["begintimestepbeforepredictor"] = "BeginTimestepBeforePredictor"
            vals["afterpredictorbeforehvacmanagers"] = "AfterPredictorBeforeHVACManagers"
            vals["afterpredictorafterhvacmanagers"] = "AfterPredictorAfterHVACManagers"
            vals["insidehvacsystemiterationloop"] = "InsideHVACSystemIterationLoop"
            vals["endofzonetimestepbeforezonereporting"] = "EndOfZoneTimestepBeforeZoneReporting"
            vals["endofzonetimestepafterzonereporting"] = "EndOfZoneTimestepAfterZoneReporting"
            vals["endofsystemtimestepbeforehvacreporting"] = "EndOfSystemTimestepBeforeHVACReporting"
            vals["endofsystemtimestepafterhvacreporting"] = "EndOfSystemTimestepAfterHVACReporting"
            vals["endofzonesizing"] = "EndOfZoneSizing"
            vals["endofsystemsizing"] = "EndOfSystemSizing"
            vals["aftercomponentinputreadin"] = "AfterComponentInputReadIn"
            vals["userdefinedcomponentmodel"] = "UserDefinedComponentModel"
            vals["unitarysystemsizing"] = "UnitarySystemSizing"
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
                                     'field `EnergyManagementSystemProgramCallingManager.energyplus_model_calling_point`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `EnergyManagementSystemProgramCallingManager.energyplus_model_calling_point`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["EnergyPlus Model Calling Point"] = value

    def add_extensible(self,
                       program_name_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            program_name_1 (str): value for IDD Field `Program Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_program_name_1(program_name_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_program_name_1(self, value):
        """ Validates falue of field `Program Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EnergyManagementSystemProgramCallingManager.program_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemProgramCallingManager.program_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemProgramCallingManager.program_name_1`')
        return value

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
                    raise ValueError("Required field EnergyManagementSystemProgramCallingManager:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemProgramCallingManager:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemProgramCallingManager: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemProgramCallingManager: {} / {}".format(out_fields,
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

class EnergyManagementSystemProgram(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Program`
        This input defines an Erl program
        Each field after the name is a line of EMS Runtime Language
    """
    internal_name = "EnergyManagementSystem:Program"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Program Line 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:Program`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `EnergyManagementSystemProgram.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemProgram.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemProgram.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       program_line_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            program_line_1 (str): value for IDD Field `Program Line 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_program_line_1(program_line_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_program_line_1(self, value):
        """ Validates falue of field `Program Line 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EnergyManagementSystemProgram.program_line_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemProgram.program_line_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemProgram.program_line_1`')
        return value

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
                    raise ValueError("Required field EnergyManagementSystemProgram:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemProgram:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemProgram: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemProgram: {} / {}".format(out_fields,
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

class EnergyManagementSystemSubroutine(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Subroutine`
        This input defines an Erl program subroutine
        Each field after the name is a line of EMS Runtime Language
    """
    internal_name = "EnergyManagementSystem:Subroutine"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Program Line"]

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:Subroutine`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `EnergyManagementSystemSubroutine.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemSubroutine.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemSubroutine.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       program_line=None,
                       ):
        """ Add values for extensible fields

        Args:

            program_line (str): value for IDD Field `Program Line`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_program_line(program_line))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_program_line(self, value):
        """ Validates falue of field `Program Line`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EnergyManagementSystemSubroutine.program_line`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemSubroutine.program_line`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemSubroutine.program_line`')
        return value

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
                    raise ValueError("Required field EnergyManagementSystemSubroutine:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemSubroutine:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemSubroutine: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemSubroutine: {} / {}".format(out_fields,
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

class EnergyManagementSystemGlobalVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:GlobalVariable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    internal_name = "EnergyManagementSystem:GlobalVariable"
    field_count = 0
    required_fields = []
    extensible_fields = 1
    format = None
    min_fields = 1
    extensible_keys = ["Erl Variable 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:GlobalVariable`
        """
        self._data = OrderedDict()
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    def add_extensible(self,
                       erl_variable_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            erl_variable_1_name (str): value for IDD Field `Erl Variable 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_erl_variable_1_name(erl_variable_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_erl_variable_1_name(self, value):
        """ Validates falue of field `Erl Variable 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EnergyManagementSystemGlobalVariable.erl_variable_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemGlobalVariable.erl_variable_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemGlobalVariable.erl_variable_1_name`')
        return value

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
                    raise ValueError("Required field EnergyManagementSystemGlobalVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemGlobalVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemGlobalVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemGlobalVariable: {} / {}".format(out_fields,
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

class EnergyManagementSystemOutputVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:OutputVariable`
        This object sets up an EnergyPlus output variable from an Erl variable
    """
    internal_name = "EnergyManagementSystem:OutputVariable"
    field_count = 6
    required_fields = ["Name", "EMS Variable Name", "Type of Data in Variable", "Update Frequency"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:OutputVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EMS Variable Name"] = None
        self._data["Type of Data in Variable"] = None
        self._data["Update Frequency"] = None
        self._data["EMS Program or Subroutine Name"] = None
        self._data["Units"] = None
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
            self.ems_variable_name = None
        else:
            self.ems_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.type_of_data_in_variable = None
        else:
            self.type_of_data_in_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.update_frequency = None
        else:
            self.update_frequency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ems_program_or_subroutine_name = None
        else:
            self.ems_program_or_subroutine_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.units = None
        else:
            self.units = vals[i]
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
                                 ' for field `EnergyManagementSystemOutputVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemOutputVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemOutputVariable.name`')
        self._data["Name"] = value

    @property
    def ems_variable_name(self):
        """Get ems_variable_name

        Returns:
            str: the value of `ems_variable_name` or None if not set
        """
        return self._data["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """  Corresponds to IDD Field `EMS Variable Name`
        must be an acceptable EMS variable

        Args:
            value (str): value for IDD Field `EMS Variable Name`
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
                                 ' for field `EnergyManagementSystemOutputVariable.ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemOutputVariable.ems_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemOutputVariable.ems_variable_name`')
        self._data["EMS Variable Name"] = value

    @property
    def type_of_data_in_variable(self):
        """Get type_of_data_in_variable

        Returns:
            str: the value of `type_of_data_in_variable` or None if not set
        """
        return self._data["Type of Data in Variable"]

    @type_of_data_in_variable.setter
    def type_of_data_in_variable(self, value=None):
        """  Corresponds to IDD Field `Type of Data in Variable`

        Args:
            value (str): value for IDD Field `Type of Data in Variable`
                Accepted values are:
                      - Averaged
                      - Summed
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
                                 ' for field `EnergyManagementSystemOutputVariable.type_of_data_in_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemOutputVariable.type_of_data_in_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemOutputVariable.type_of_data_in_variable`')
            vals = {}
            vals["averaged"] = "Averaged"
            vals["summed"] = "Summed"
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
                                     'field `EnergyManagementSystemOutputVariable.type_of_data_in_variable`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `EnergyManagementSystemOutputVariable.type_of_data_in_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Type of Data in Variable"] = value

    @property
    def update_frequency(self):
        """Get update_frequency

        Returns:
            str: the value of `update_frequency` or None if not set
        """
        return self._data["Update Frequency"]

    @update_frequency.setter
    def update_frequency(self, value=None):
        """  Corresponds to IDD Field `Update Frequency`

        Args:
            value (str): value for IDD Field `Update Frequency`
                Accepted values are:
                      - ZoneTimestep
                      - SystemTimestep
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
                                 ' for field `EnergyManagementSystemOutputVariable.update_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemOutputVariable.update_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemOutputVariable.update_frequency`')
            vals = {}
            vals["zonetimestep"] = "ZoneTimestep"
            vals["systemtimestep"] = "SystemTimestep"
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
                                     'field `EnergyManagementSystemOutputVariable.update_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `EnergyManagementSystemOutputVariable.update_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Update Frequency"] = value

    @property
    def ems_program_or_subroutine_name(self):
        """Get ems_program_or_subroutine_name

        Returns:
            str: the value of `ems_program_or_subroutine_name` or None if not set
        """
        return self._data["EMS Program or Subroutine Name"]

    @ems_program_or_subroutine_name.setter
    def ems_program_or_subroutine_name(self, value=None):
        """  Corresponds to IDD Field `EMS Program or Subroutine Name`
        optional for global scope variables, required for local scope variables

        Args:
            value (str): value for IDD Field `EMS Program or Subroutine Name`
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
                                 ' for field `EnergyManagementSystemOutputVariable.ems_program_or_subroutine_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemOutputVariable.ems_program_or_subroutine_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemOutputVariable.ems_program_or_subroutine_name`')
        self._data["EMS Program or Subroutine Name"] = value

    @property
    def units(self):
        """Get units

        Returns:
            str: the value of `units` or None if not set
        """
        return self._data["Units"]

    @units.setter
    def units(self, value=None):
        """  Corresponds to IDD Field `Units`
        optional but will result in dimensionless units for blank
        EnergyPlus units are standard SI units

        Args:
            value (str): value for IDD Field `Units`
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
                                 ' for field `EnergyManagementSystemOutputVariable.units`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemOutputVariable.units`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemOutputVariable.units`')
        self._data["Units"] = value

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
                    raise ValueError("Required field EnergyManagementSystemOutputVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemOutputVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemOutputVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemOutputVariable: {} / {}".format(out_fields,
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

class EnergyManagementSystemMeteredOutputVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:MeteredOutputVariable`
        This object sets up an EnergyPlus output variable from an Erl variable
    """
    internal_name = "EnergyManagementSystem:MeteredOutputVariable"
    field_count = 9
    required_fields = ["Name", "EMS Variable Name", "Update Frequency", "Resource Type", "Group Type", "End-Use Category"]
    extensible_fields = 0
    format = None
    min_fields = 7
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:MeteredOutputVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EMS Variable Name"] = None
        self._data["Update Frequency"] = None
        self._data["EMS Program or Subroutine Name"] = None
        self._data["Resource Type"] = None
        self._data["Group Type"] = None
        self._data["End-Use Category"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Units"] = None
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
            self.ems_variable_name = None
        else:
            self.ems_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.update_frequency = None
        else:
            self.update_frequency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ems_program_or_subroutine_name = None
        else:
            self.ems_program_or_subroutine_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.resource_type = None
        else:
            self.resource_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.group_type = None
        else:
            self.group_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_category = None
        else:
            self.enduse_category = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.units = None
        else:
            self.units = vals[i]
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.name`')
        self._data["Name"] = value

    @property
    def ems_variable_name(self):
        """Get ems_variable_name

        Returns:
            str: the value of `ems_variable_name` or None if not set
        """
        return self._data["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """  Corresponds to IDD Field `EMS Variable Name`
        must be an acceptable EMS variable, no spaces

        Args:
            value (str): value for IDD Field `EMS Variable Name`
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.ems_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.ems_variable_name`')
        self._data["EMS Variable Name"] = value

    @property
    def update_frequency(self):
        """Get update_frequency

        Returns:
            str: the value of `update_frequency` or None if not set
        """
        return self._data["Update Frequency"]

    @update_frequency.setter
    def update_frequency(self, value=None):
        """  Corresponds to IDD Field `Update Frequency`

        Args:
            value (str): value for IDD Field `Update Frequency`
                Accepted values are:
                      - ZoneTimestep
                      - SystemTimestep
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.update_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.update_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.update_frequency`')
            vals = {}
            vals["zonetimestep"] = "ZoneTimestep"
            vals["systemtimestep"] = "SystemTimestep"
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
                                     'field `EnergyManagementSystemMeteredOutputVariable.update_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `EnergyManagementSystemMeteredOutputVariable.update_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Update Frequency"] = value

    @property
    def ems_program_or_subroutine_name(self):
        """Get ems_program_or_subroutine_name

        Returns:
            str: the value of `ems_program_or_subroutine_name` or None if not set
        """
        return self._data["EMS Program or Subroutine Name"]

    @ems_program_or_subroutine_name.setter
    def ems_program_or_subroutine_name(self, value=None):
        """  Corresponds to IDD Field `EMS Program or Subroutine Name`
        optional for global scope variables, required for local scope variables

        Args:
            value (str): value for IDD Field `EMS Program or Subroutine Name`
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.ems_program_or_subroutine_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.ems_program_or_subroutine_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.ems_program_or_subroutine_name`')
        self._data["EMS Program or Subroutine Name"] = value

    @property
    def resource_type(self):
        """Get resource_type

        Returns:
            str: the value of `resource_type` or None if not set
        """
        return self._data["Resource Type"]

    @resource_type.setter
    def resource_type(self, value=None):
        """  Corresponds to IDD Field `Resource Type`
        choose the type of fuel, water, electricity, pollution or heat rate that should be metered.

        Args:
            value (str): value for IDD Field `Resource Type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - Gasoline
                      - Diesel
                      - Coal
                      - FuelOil#1
                      - FuelOil#2
                      - Propane
                      - OtherFuel1
                      - OtherFuel2
                      - WaterUse
                      - OnSiteWaterProduced
                      - MainsWaterSupply
                      - RainWaterCollected
                      - WellWaterDrawn
                      - CondensateWaterCollected
                      - EnergyTransfer
                      - Steam
                      - DistrictCooling
                      - DistrictHeating
                      - ElectricityProducedOnSite
                      - SolarWaterHeating
                      - SolarAirHeating
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.resource_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.resource_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.resource_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["gasoline"] = "Gasoline"
            vals["diesel"] = "Diesel"
            vals["coal"] = "Coal"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["propane"] = "Propane"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["wateruse"] = "WaterUse"
            vals["onsitewaterproduced"] = "OnSiteWaterProduced"
            vals["mainswatersupply"] = "MainsWaterSupply"
            vals["rainwatercollected"] = "RainWaterCollected"
            vals["wellwaterdrawn"] = "WellWaterDrawn"
            vals["condensatewatercollected"] = "CondensateWaterCollected"
            vals["energytransfer"] = "EnergyTransfer"
            vals["steam"] = "Steam"
            vals["districtcooling"] = "DistrictCooling"
            vals["districtheating"] = "DistrictHeating"
            vals["electricityproducedonsite"] = "ElectricityProducedOnSite"
            vals["solarwaterheating"] = "SolarWaterHeating"
            vals["solarairheating"] = "SolarAirHeating"
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
                                     'field `EnergyManagementSystemMeteredOutputVariable.resource_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `EnergyManagementSystemMeteredOutputVariable.resource_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Resource Type"] = value

    @property
    def group_type(self):
        """Get group_type

        Returns:
            str: the value of `group_type` or None if not set
        """
        return self._data["Group Type"]

    @group_type.setter
    def group_type(self, value=None):
        """  Corresponds to IDD Field `Group Type`
        choose a general classification, building (internal services), HVAC (air sytems), or plant (hydronic systems)

        Args:
            value (str): value for IDD Field `Group Type`
                Accepted values are:
                      - Building
                      - HVAC
                      - Plant
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.group_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.group_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.group_type`')
            vals = {}
            vals["building"] = "Building"
            vals["hvac"] = "HVAC"
            vals["plant"] = "Plant"
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
                                     'field `EnergyManagementSystemMeteredOutputVariable.group_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `EnergyManagementSystemMeteredOutputVariable.group_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Group Type"] = value

    @property
    def enduse_category(self):
        """Get enduse_category

        Returns:
            str: the value of `enduse_category` or None if not set
        """
        return self._data["End-Use Category"]

    @enduse_category.setter
    def enduse_category(self, value=None):
        """  Corresponds to IDD Field `End-Use Category`
        choose how the metered output should be classified for end-use category

        Args:
            value (str): value for IDD Field `End-Use Category`
                Accepted values are:
                      - Heating
                      - Cooling
                      - InteriorLights
                      - ExteriorLights
                      - InteriorEquipment
                      - ExteriorEquipment
                      - Fans
                      - Pumps
                      - HeatRejection
                      - Humidifier
                      - HeatRecovery
                      - WaterSystems
                      - Refrigeration
                      - OnSiteGeneration
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.enduse_category`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.enduse_category`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.enduse_category`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["interiorlights"] = "InteriorLights"
            vals["exteriorlights"] = "ExteriorLights"
            vals["interiorequipment"] = "InteriorEquipment"
            vals["exteriorequipment"] = "ExteriorEquipment"
            vals["fans"] = "Fans"
            vals["pumps"] = "Pumps"
            vals["heatrejection"] = "HeatRejection"
            vals["humidifier"] = "Humidifier"
            vals["heatrecovery"] = "HeatRecovery"
            vals["watersystems"] = "WaterSystems"
            vals["refrigeration"] = "Refrigeration"
            vals["onsitegeneration"] = "OnSiteGeneration"
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
                                     'field `EnergyManagementSystemMeteredOutputVariable.enduse_category`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `EnergyManagementSystemMeteredOutputVariable.enduse_category`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["End-Use Category"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value=None):
        """  Corresponds to IDD Field `End-Use Subcategory`
        enter a user-defined subcategory for this metered output

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def units(self):
        """Get units

        Returns:
            str: the value of `units` or None if not set
        """
        return self._data["Units"]

    @units.setter
    def units(self, value=None):
        """  Corresponds to IDD Field `Units`
        optional but will result in dimensionless units for blank
        EnergyPlus units are standard SI units

        Args:
            value (str): value for IDD Field `Units`
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
                                 ' for field `EnergyManagementSystemMeteredOutputVariable.units`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.units`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemMeteredOutputVariable.units`')
        self._data["Units"] = value

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
                    raise ValueError("Required field EnergyManagementSystemMeteredOutputVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemMeteredOutputVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemMeteredOutputVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemMeteredOutputVariable: {} / {}".format(out_fields,
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

class EnergyManagementSystemTrendVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:TrendVariable`
        This object sets up an EMS trend variable from an Erl variable
        A trend variable logs values across timesteps
    """
    internal_name = "EnergyManagementSystem:TrendVariable"
    field_count = 3
    required_fields = ["Name", "EMS Variable Name", "Number of Timesteps to be Logged"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:TrendVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EMS Variable Name"] = None
        self._data["Number of Timesteps to be Logged"] = None
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
            self.ems_variable_name = None
        else:
            self.ems_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_timesteps_to_be_logged = None
        else:
            self.number_of_timesteps_to_be_logged = vals[i]
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
                                 ' for field `EnergyManagementSystemTrendVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemTrendVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemTrendVariable.name`')
        self._data["Name"] = value

    @property
    def ems_variable_name(self):
        """Get ems_variable_name

        Returns:
            str: the value of `ems_variable_name` or None if not set
        """
        return self._data["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """  Corresponds to IDD Field `EMS Variable Name`
        must be a global scope EMS variable

        Args:
            value (str): value for IDD Field `EMS Variable Name`
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
                                 ' for field `EnergyManagementSystemTrendVariable.ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemTrendVariable.ems_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemTrendVariable.ems_variable_name`')
        self._data["EMS Variable Name"] = value

    @property
    def number_of_timesteps_to_be_logged(self):
        """Get number_of_timesteps_to_be_logged

        Returns:
            int: the value of `number_of_timesteps_to_be_logged` or None if not set
        """
        return self._data["Number of Timesteps to be Logged"]

    @number_of_timesteps_to_be_logged.setter
    def number_of_timesteps_to_be_logged(self, value=None):
        """  Corresponds to IDD Field `Number of Timesteps to be Logged`

        Args:
            value (int): value for IDD Field `Number of Timesteps to be Logged`
                value >= 1
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
                                     'for field `EnergyManagementSystemTrendVariable.number_of_timesteps_to_be_logged`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `EnergyManagementSystemTrendVariable.number_of_timesteps_to_be_logged`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `EnergyManagementSystemTrendVariable.number_of_timesteps_to_be_logged`')
        self._data["Number of Timesteps to be Logged"] = value

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
                    raise ValueError("Required field EnergyManagementSystemTrendVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemTrendVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemTrendVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemTrendVariable: {} / {}".format(out_fields,
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

class EnergyManagementSystemInternalVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:InternalVariable`
        Declares EMS variable as an internal data variable
    """
    internal_name = "EnergyManagementSystem:InternalVariable"
    field_count = 3
    required_fields = ["Name", "Internal Data Type"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:InternalVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Internal Data Index Key Name"] = None
        self._data["Internal Data Type"] = None
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
            self.internal_data_index_key_name = None
        else:
            self.internal_data_index_key_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.internal_data_type = None
        else:
            self.internal_data_type = vals[i]
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
                                 ' for field `EnergyManagementSystemInternalVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemInternalVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemInternalVariable.name`')
        self._data["Name"] = value

    @property
    def internal_data_index_key_name(self):
        """Get internal_data_index_key_name

        Returns:
            str: the value of `internal_data_index_key_name` or None if not set
        """
        return self._data["Internal Data Index Key Name"]

    @internal_data_index_key_name.setter
    def internal_data_index_key_name(self, value=None):
        """  Corresponds to IDD Field `Internal Data Index Key Name`

        Args:
            value (str): value for IDD Field `Internal Data Index Key Name`
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
                                 ' for field `EnergyManagementSystemInternalVariable.internal_data_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemInternalVariable.internal_data_index_key_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemInternalVariable.internal_data_index_key_name`')
        self._data["Internal Data Index Key Name"] = value

    @property
    def internal_data_type(self):
        """Get internal_data_type

        Returns:
            str: the value of `internal_data_type` or None if not set
        """
        return self._data["Internal Data Type"]

    @internal_data_type.setter
    def internal_data_type(self, value=None):
        """  Corresponds to IDD Field `Internal Data Type`

        Args:
            value (str): value for IDD Field `Internal Data Type`
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
                                 ' for field `EnergyManagementSystemInternalVariable.internal_data_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemInternalVariable.internal_data_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemInternalVariable.internal_data_type`')
        self._data["Internal Data Type"] = value

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
                    raise ValueError("Required field EnergyManagementSystemInternalVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemInternalVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemInternalVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemInternalVariable: {} / {}".format(out_fields,
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

class EnergyManagementSystemCurveOrTableIndexVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:CurveOrTableIndexVariable`
        Declares EMS variable that identifies a curve or table
    """
    internal_name = "EnergyManagementSystem:CurveOrTableIndexVariable"
    field_count = 2
    required_fields = ["Name", "Curve or Table Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:CurveOrTableIndexVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Curve or Table Object Name"] = None
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
            self.curve_or_table_object_name = None
        else:
            self.curve_or_table_object_name = vals[i]
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
                                 ' for field `EnergyManagementSystemCurveOrTableIndexVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemCurveOrTableIndexVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemCurveOrTableIndexVariable.name`')
        self._data["Name"] = value

    @property
    def curve_or_table_object_name(self):
        """Get curve_or_table_object_name

        Returns:
            str: the value of `curve_or_table_object_name` or None if not set
        """
        return self._data["Curve or Table Object Name"]

    @curve_or_table_object_name.setter
    def curve_or_table_object_name(self, value=None):
        """  Corresponds to IDD Field `Curve or Table Object Name`

        Args:
            value (str): value for IDD Field `Curve or Table Object Name`
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
                                 ' for field `EnergyManagementSystemCurveOrTableIndexVariable.curve_or_table_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemCurveOrTableIndexVariable.curve_or_table_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemCurveOrTableIndexVariable.curve_or_table_object_name`')
        self._data["Curve or Table Object Name"] = value

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
                    raise ValueError("Required field EnergyManagementSystemCurveOrTableIndexVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemCurveOrTableIndexVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemCurveOrTableIndexVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemCurveOrTableIndexVariable: {} / {}".format(out_fields,
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

class EnergyManagementSystemConstructionIndexVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:ConstructionIndexVariable`
        Declares EMS variable that identifies a construction
    """
    internal_name = "EnergyManagementSystem:ConstructionIndexVariable"
    field_count = 2
    required_fields = ["Name", "Construction Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:ConstructionIndexVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Object Name"] = None
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
            self.construction_object_name = None
        else:
            self.construction_object_name = vals[i]
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
                                 ' for field `EnergyManagementSystemConstructionIndexVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemConstructionIndexVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemConstructionIndexVariable.name`')
        self._data["Name"] = value

    @property
    def construction_object_name(self):
        """Get construction_object_name

        Returns:
            str: the value of `construction_object_name` or None if not set
        """
        return self._data["Construction Object Name"]

    @construction_object_name.setter
    def construction_object_name(self, value=None):
        """  Corresponds to IDD Field `Construction Object Name`

        Args:
            value (str): value for IDD Field `Construction Object Name`
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
                                 ' for field `EnergyManagementSystemConstructionIndexVariable.construction_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EnergyManagementSystemConstructionIndexVariable.construction_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EnergyManagementSystemConstructionIndexVariable.construction_object_name`')
        self._data["Construction Object Name"] = value

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
                    raise ValueError("Required field EnergyManagementSystemConstructionIndexVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnergyManagementSystemConstructionIndexVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnergyManagementSystemConstructionIndexVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnergyManagementSystemConstructionIndexVariable: {} / {}".format(out_fields,
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