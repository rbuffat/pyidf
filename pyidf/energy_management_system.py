from collections import OrderedDict

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

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:Sensor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Output:Variable or Output:Meter Index Key Name"] = None
        self._data["Output:Variable or Output:Meter Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_or_outputmeter_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_or_outputmeter_index_key_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outputvariable_or_outputmeter_index_key_name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_or_outputmeter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_or_outputmeter_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outputvariable_or_outputmeter_name`')
        self._data["Output:Variable or Output:Meter Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_unique_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `actuated_component_control_type`')
        self._data["Actuated Component Control Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
    field_count = 27
    required_fields = ["Name", "Program Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:ProgramCallingManager`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EnergyPlus Model Calling Point"] = None
        self._data["Program Name 1"] = None
        self._data["Program Name 2"] = None
        self._data["Program Name 3"] = None
        self._data["Program Name 4"] = None
        self._data["Program Name 5"] = None
        self._data["Program Name 6"] = None
        self._data["Program Name 7"] = None
        self._data["Program Name 8"] = None
        self._data["Program Name 9"] = None
        self._data["Program Name 10"] = None
        self._data["Program Name 11"] = None
        self._data["Program Name 12"] = None
        self._data["Program Name 13"] = None
        self._data["Program Name 14"] = None
        self._data["Program Name 15"] = None
        self._data["Program Name 16"] = None
        self._data["Program Name 17"] = None
        self._data["Program Name 18"] = None
        self._data["Program Name 19"] = None
        self._data["Program Name 20"] = None
        self._data["Program Name 21"] = None
        self._data["Program Name 22"] = None
        self._data["Program Name 23"] = None
        self._data["Program Name 24"] = None
        self._data["Program Name 25"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        if len(vals[i]) == 0:
            self.program_name_1 = None
        else:
            self.program_name_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_2 = None
        else:
            self.program_name_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_3 = None
        else:
            self.program_name_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_4 = None
        else:
            self.program_name_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_5 = None
        else:
            self.program_name_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_6 = None
        else:
            self.program_name_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_7 = None
        else:
            self.program_name_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_8 = None
        else:
            self.program_name_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_9 = None
        else:
            self.program_name_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_10 = None
        else:
            self.program_name_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_11 = None
        else:
            self.program_name_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_12 = None
        else:
            self.program_name_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_13 = None
        else:
            self.program_name_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_14 = None
        else:
            self.program_name_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_15 = None
        else:
            self.program_name_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_16 = None
        else:
            self.program_name_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_17 = None
        else:
            self.program_name_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_18 = None
        else:
            self.program_name_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_19 = None
        else:
            self.program_name_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_20 = None
        else:
            self.program_name_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_21 = None
        else:
            self.program_name_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_22 = None
        else:
            self.program_name_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_23 = None
        else:
            self.program_name_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_24 = None
        else:
            self.program_name_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.program_name_25 = None
        else:
            self.program_name_25 = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `energyplus_model_calling_point`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `energyplus_model_calling_point`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `energyplus_model_calling_point`')
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
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `energyplus_model_calling_point`'.format(value))
            value = vals[value_lower]
        self._data["EnergyPlus Model Calling Point"] = value

    @property
    def program_name_1(self):
        """Get program_name_1

        Returns:
            str: the value of `program_name_1` or None if not set
        """
        return self._data["Program Name 1"]

    @program_name_1.setter
    def program_name_1(self, value=None):
        """  Corresponds to IDD Field `Program Name 1`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_1`')
        self._data["Program Name 1"] = value

    @property
    def program_name_2(self):
        """Get program_name_2

        Returns:
            str: the value of `program_name_2` or None if not set
        """
        return self._data["Program Name 2"]

    @program_name_2.setter
    def program_name_2(self, value=None):
        """  Corresponds to IDD Field `Program Name 2`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_2`')
        self._data["Program Name 2"] = value

    @property
    def program_name_3(self):
        """Get program_name_3

        Returns:
            str: the value of `program_name_3` or None if not set
        """
        return self._data["Program Name 3"]

    @program_name_3.setter
    def program_name_3(self, value=None):
        """  Corresponds to IDD Field `Program Name 3`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_3`')
        self._data["Program Name 3"] = value

    @property
    def program_name_4(self):
        """Get program_name_4

        Returns:
            str: the value of `program_name_4` or None if not set
        """
        return self._data["Program Name 4"]

    @program_name_4.setter
    def program_name_4(self, value=None):
        """  Corresponds to IDD Field `Program Name 4`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_4`')
        self._data["Program Name 4"] = value

    @property
    def program_name_5(self):
        """Get program_name_5

        Returns:
            str: the value of `program_name_5` or None if not set
        """
        return self._data["Program Name 5"]

    @program_name_5.setter
    def program_name_5(self, value=None):
        """  Corresponds to IDD Field `Program Name 5`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_5`')
        self._data["Program Name 5"] = value

    @property
    def program_name_6(self):
        """Get program_name_6

        Returns:
            str: the value of `program_name_6` or None if not set
        """
        return self._data["Program Name 6"]

    @program_name_6.setter
    def program_name_6(self, value=None):
        """  Corresponds to IDD Field `Program Name 6`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_6`')
        self._data["Program Name 6"] = value

    @property
    def program_name_7(self):
        """Get program_name_7

        Returns:
            str: the value of `program_name_7` or None if not set
        """
        return self._data["Program Name 7"]

    @program_name_7.setter
    def program_name_7(self, value=None):
        """  Corresponds to IDD Field `Program Name 7`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_7`')
        self._data["Program Name 7"] = value

    @property
    def program_name_8(self):
        """Get program_name_8

        Returns:
            str: the value of `program_name_8` or None if not set
        """
        return self._data["Program Name 8"]

    @program_name_8.setter
    def program_name_8(self, value=None):
        """  Corresponds to IDD Field `Program Name 8`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_8`')
        self._data["Program Name 8"] = value

    @property
    def program_name_9(self):
        """Get program_name_9

        Returns:
            str: the value of `program_name_9` or None if not set
        """
        return self._data["Program Name 9"]

    @program_name_9.setter
    def program_name_9(self, value=None):
        """  Corresponds to IDD Field `Program Name 9`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_9`')
        self._data["Program Name 9"] = value

    @property
    def program_name_10(self):
        """Get program_name_10

        Returns:
            str: the value of `program_name_10` or None if not set
        """
        return self._data["Program Name 10"]

    @program_name_10.setter
    def program_name_10(self, value=None):
        """  Corresponds to IDD Field `Program Name 10`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_10`')
        self._data["Program Name 10"] = value

    @property
    def program_name_11(self):
        """Get program_name_11

        Returns:
            str: the value of `program_name_11` or None if not set
        """
        return self._data["Program Name 11"]

    @program_name_11.setter
    def program_name_11(self, value=None):
        """  Corresponds to IDD Field `Program Name 11`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_11`')
        self._data["Program Name 11"] = value

    @property
    def program_name_12(self):
        """Get program_name_12

        Returns:
            str: the value of `program_name_12` or None if not set
        """
        return self._data["Program Name 12"]

    @program_name_12.setter
    def program_name_12(self, value=None):
        """  Corresponds to IDD Field `Program Name 12`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_12`')
        self._data["Program Name 12"] = value

    @property
    def program_name_13(self):
        """Get program_name_13

        Returns:
            str: the value of `program_name_13` or None if not set
        """
        return self._data["Program Name 13"]

    @program_name_13.setter
    def program_name_13(self, value=None):
        """  Corresponds to IDD Field `Program Name 13`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_13`')
        self._data["Program Name 13"] = value

    @property
    def program_name_14(self):
        """Get program_name_14

        Returns:
            str: the value of `program_name_14` or None if not set
        """
        return self._data["Program Name 14"]

    @program_name_14.setter
    def program_name_14(self, value=None):
        """  Corresponds to IDD Field `Program Name 14`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_14`')
        self._data["Program Name 14"] = value

    @property
    def program_name_15(self):
        """Get program_name_15

        Returns:
            str: the value of `program_name_15` or None if not set
        """
        return self._data["Program Name 15"]

    @program_name_15.setter
    def program_name_15(self, value=None):
        """  Corresponds to IDD Field `Program Name 15`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_15`')
        self._data["Program Name 15"] = value

    @property
    def program_name_16(self):
        """Get program_name_16

        Returns:
            str: the value of `program_name_16` or None if not set
        """
        return self._data["Program Name 16"]

    @program_name_16.setter
    def program_name_16(self, value=None):
        """  Corresponds to IDD Field `Program Name 16`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_16`')
        self._data["Program Name 16"] = value

    @property
    def program_name_17(self):
        """Get program_name_17

        Returns:
            str: the value of `program_name_17` or None if not set
        """
        return self._data["Program Name 17"]

    @program_name_17.setter
    def program_name_17(self, value=None):
        """  Corresponds to IDD Field `Program Name 17`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_17`')
        self._data["Program Name 17"] = value

    @property
    def program_name_18(self):
        """Get program_name_18

        Returns:
            str: the value of `program_name_18` or None if not set
        """
        return self._data["Program Name 18"]

    @program_name_18.setter
    def program_name_18(self, value=None):
        """  Corresponds to IDD Field `Program Name 18`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_18`')
        self._data["Program Name 18"] = value

    @property
    def program_name_19(self):
        """Get program_name_19

        Returns:
            str: the value of `program_name_19` or None if not set
        """
        return self._data["Program Name 19"]

    @program_name_19.setter
    def program_name_19(self, value=None):
        """  Corresponds to IDD Field `Program Name 19`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_19`')
        self._data["Program Name 19"] = value

    @property
    def program_name_20(self):
        """Get program_name_20

        Returns:
            str: the value of `program_name_20` or None if not set
        """
        return self._data["Program Name 20"]

    @program_name_20.setter
    def program_name_20(self, value=None):
        """  Corresponds to IDD Field `Program Name 20`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_20`')
        self._data["Program Name 20"] = value

    @property
    def program_name_21(self):
        """Get program_name_21

        Returns:
            str: the value of `program_name_21` or None if not set
        """
        return self._data["Program Name 21"]

    @program_name_21.setter
    def program_name_21(self, value=None):
        """  Corresponds to IDD Field `Program Name 21`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_21`')
        self._data["Program Name 21"] = value

    @property
    def program_name_22(self):
        """Get program_name_22

        Returns:
            str: the value of `program_name_22` or None if not set
        """
        return self._data["Program Name 22"]

    @program_name_22.setter
    def program_name_22(self, value=None):
        """  Corresponds to IDD Field `Program Name 22`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_22`')
        self._data["Program Name 22"] = value

    @property
    def program_name_23(self):
        """Get program_name_23

        Returns:
            str: the value of `program_name_23` or None if not set
        """
        return self._data["Program Name 23"]

    @program_name_23.setter
    def program_name_23(self, value=None):
        """  Corresponds to IDD Field `Program Name 23`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_23`')
        self._data["Program Name 23"] = value

    @property
    def program_name_24(self):
        """Get program_name_24

        Returns:
            str: the value of `program_name_24` or None if not set
        """
        return self._data["Program Name 24"]

    @program_name_24.setter
    def program_name_24(self, value=None):
        """  Corresponds to IDD Field `Program Name 24`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_24`')
        self._data["Program Name 24"] = value

    @property
    def program_name_25(self):
        """Get program_name_25

        Returns:
            str: the value of `program_name_25` or None if not set
        """
        return self._data["Program Name 25"]

    @program_name_25.setter
    def program_name_25(self, value=None):
        """  Corresponds to IDD Field `Program Name 25`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `Program Name 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `program_name_25`')
        self._data["Program Name 25"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ems_variable_name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `type_of_data_in_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_data_in_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `type_of_data_in_variable`')
            vals = {}
            vals["averaged"] = "Averaged"
            vals["summed"] = "Summed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `type_of_data_in_variable`'.format(value))
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
                raise ValueError('value {} need to be of type str '
                                 'for field `update_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `update_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `update_frequency`')
            vals = {}
            vals["zonetimestep"] = "ZoneTimestep"
            vals["systemtimestep"] = "SystemTimestep"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `update_frequency`'.format(value))
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
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_program_or_subroutine_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_program_or_subroutine_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ems_program_or_subroutine_name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `units`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `units`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `units`')
        self._data["Units"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ems_variable_name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `update_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `update_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `update_frequency`')
            vals = {}
            vals["zonetimestep"] = "ZoneTimestep"
            vals["systemtimestep"] = "SystemTimestep"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `update_frequency`'.format(value))
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
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_program_or_subroutine_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_program_or_subroutine_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ems_program_or_subroutine_name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `resource_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `resource_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `resource_type`')
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
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `resource_type`'.format(value))
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
                raise ValueError('value {} need to be of type str '
                                 'for field `group_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `group_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `group_type`')
            vals = {}
            vals["building"] = "Building"
            vals["hvac"] = "HVAC"
            vals["plant"] = "Plant"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `group_type`'.format(value))
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
                raise ValueError('value {} need to be of type str '
                                 'for field `enduse_category`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_category`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_category`')
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
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `enduse_category`'.format(value))
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
                raise ValueError('value {} need to be of type str '
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `units`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `units`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `units`')
        self._data["Units"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:TrendVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EMS Variable Name"] = None
        self._data["Number of Timesteps to be Logged"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ems_variable_name`')
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
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_timesteps_to_be_logged`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_timesteps_to_be_logged`')
        self._data["Number of Timesteps to be Logged"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:InternalVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Internal Data Index Key Name"] = None
        self._data["Internal Data Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `internal_data_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `internal_data_index_key_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `internal_data_index_key_name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `internal_data_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `internal_data_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `internal_data_type`')
        self._data["Internal Data Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:CurveOrTableIndexVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Curve or Table Object Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `curve_or_table_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `curve_or_table_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `curve_or_table_object_name`')
        self._data["Curve or Table Object Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `EnergyManagementSystem:ConstructionIndexVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Object Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `construction_object_name`')
        self._data["Construction Object Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])