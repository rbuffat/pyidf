from collections import OrderedDict

class AvailabilityManagerAssignmentList(object):
    """ Corresponds to IDD object `AvailabilityManagerAssignmentList`
        Defines the applicable managers used for an AirLoopHVAC or PlantLoop. The priority of
        availability managers is based on a set of rules and are specific to the type of loop.
        The output from each availability manager is an availability status flag:
        NoAction, ForceOff, CycleOn, or CycleOnZoneFansOnly (used only for air loops).
    """
    internal_name = "AvailabilityManagerAssignmentList"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AvailabilityManagerAssignmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Manager 1 Object Type"] = None
        self._data["Availability Manager 1 Name"] = None
        self._data["Availability Manager 2 Object Type"] = None
        self._data["Availability Manager 2 Name"] = None
        self._data["Availability Manager 3 Object Type"] = None
        self._data["Availability Manager 3 Name"] = None
        self._data["Availability Manager 4 Object Type"] = None
        self._data["Availability Manager 4 Name"] = None
        self._data["Availability Manager 5 Object Type"] = None
        self._data["Availability Manager 5 Name"] = None
        self._data["Availability Manager 6 Object Type"] = None
        self._data["Availability Manager 6 Name"] = None

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
            self.availability_manager_1_object_type = None
        else:
            self.availability_manager_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_1_name = None
        else:
            self.availability_manager_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_2_object_type = None
        else:
            self.availability_manager_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_2_name = None
        else:
            self.availability_manager_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_3_object_type = None
        else:
            self.availability_manager_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_3_name = None
        else:
            self.availability_manager_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_4_object_type = None
        else:
            self.availability_manager_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_4_name = None
        else:
            self.availability_manager_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_5_object_type = None
        else:
            self.availability_manager_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_5_name = None
        else:
            self.availability_manager_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_6_object_type = None
        else:
            self.availability_manager_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_6_name = None
        else:
            self.availability_manager_6_name = vals[i]
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
    def availability_manager_1_object_type(self):
        """Get availability_manager_1_object_type

        Returns:
            str: the value of `availability_manager_1_object_type` or None if not set
        """
        return self._data["Availability Manager 1 Object Type"]

    @availability_manager_1_object_type.setter
    def availability_manager_1_object_type(self, value=None):
        """  Corresponds to IDD Field `availability_manager_1_object_type`

        Args:
            value (str): value for IDD Field `availability_manager_1_object_type`
                Accepted values are:
                      - AvailabilityManager:Scheduled
                      - AvailabilityManager:ScheduledOn
                      - AvailabilityManager:ScheduledOff
                      - AvailabilityManager:NightCycle
                      - AvailabilityManager:DifferentialThermostat
                      - AvailabilityManager:HighTemperatureTurnOff
                      - AvailabilityManager:HighTemperatureTurnOn
                      - AvailabilityManager:LowTemperatureTurnOff
                      - AvailabilityManager:LowTemperatureTurnOn
                      - AvailabilityManager:NightVentilation
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
                                 'for field `availability_manager_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_1_object_type`')
            vals = set()
            vals.add("AvailabilityManager:Scheduled")
            vals.add("AvailabilityManager:ScheduledOn")
            vals.add("AvailabilityManager:ScheduledOff")
            vals.add("AvailabilityManager:NightCycle")
            vals.add("AvailabilityManager:DifferentialThermostat")
            vals.add("AvailabilityManager:HighTemperatureTurnOff")
            vals.add("AvailabilityManager:HighTemperatureTurnOn")
            vals.add("AvailabilityManager:LowTemperatureTurnOff")
            vals.add("AvailabilityManager:LowTemperatureTurnOn")
            vals.add("AvailabilityManager:NightVentilation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `availability_manager_1_object_type`'.format(value))

        self._data["Availability Manager 1 Object Type"] = value

    @property
    def availability_manager_1_name(self):
        """Get availability_manager_1_name

        Returns:
            str: the value of `availability_manager_1_name` or None if not set
        """
        return self._data["Availability Manager 1 Name"]

    @availability_manager_1_name.setter
    def availability_manager_1_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_1_name`

        Args:
            value (str): value for IDD Field `availability_manager_1_name`
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
                                 'for field `availability_manager_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_1_name`')

        self._data["Availability Manager 1 Name"] = value

    @property
    def availability_manager_2_object_type(self):
        """Get availability_manager_2_object_type

        Returns:
            str: the value of `availability_manager_2_object_type` or None if not set
        """
        return self._data["Availability Manager 2 Object Type"]

    @availability_manager_2_object_type.setter
    def availability_manager_2_object_type(self, value=None):
        """  Corresponds to IDD Field `availability_manager_2_object_type`

        Args:
            value (str): value for IDD Field `availability_manager_2_object_type`
                Accepted values are:
                      - AvailabilityManager:Scheduled
                      - AvailabilityManager:ScheduledOn
                      - AvailabilityManager:ScheduledOff
                      - AvailabilityManager:NightCycle
                      - AvailabilityManager:DifferentialThermostat
                      - AvailabilityManager:HighTemperatureTurnOff
                      - AvailabilityManager:HighTemperatureTurnOn
                      - AvailabilityManager:LowTemperatureTurnOff
                      - AvailabilityManager:LowTemperatureTurnOn
                      - AvailabilityManager:NightVentilation
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
                                 'for field `availability_manager_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_2_object_type`')
            vals = set()
            vals.add("AvailabilityManager:Scheduled")
            vals.add("AvailabilityManager:ScheduledOn")
            vals.add("AvailabilityManager:ScheduledOff")
            vals.add("AvailabilityManager:NightCycle")
            vals.add("AvailabilityManager:DifferentialThermostat")
            vals.add("AvailabilityManager:HighTemperatureTurnOff")
            vals.add("AvailabilityManager:HighTemperatureTurnOn")
            vals.add("AvailabilityManager:LowTemperatureTurnOff")
            vals.add("AvailabilityManager:LowTemperatureTurnOn")
            vals.add("AvailabilityManager:NightVentilation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `availability_manager_2_object_type`'.format(value))

        self._data["Availability Manager 2 Object Type"] = value

    @property
    def availability_manager_2_name(self):
        """Get availability_manager_2_name

        Returns:
            str: the value of `availability_manager_2_name` or None if not set
        """
        return self._data["Availability Manager 2 Name"]

    @availability_manager_2_name.setter
    def availability_manager_2_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_2_name`

        Args:
            value (str): value for IDD Field `availability_manager_2_name`
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
                                 'for field `availability_manager_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_2_name`')

        self._data["Availability Manager 2 Name"] = value

    @property
    def availability_manager_3_object_type(self):
        """Get availability_manager_3_object_type

        Returns:
            str: the value of `availability_manager_3_object_type` or None if not set
        """
        return self._data["Availability Manager 3 Object Type"]

    @availability_manager_3_object_type.setter
    def availability_manager_3_object_type(self, value=None):
        """  Corresponds to IDD Field `availability_manager_3_object_type`

        Args:
            value (str): value for IDD Field `availability_manager_3_object_type`
                Accepted values are:
                      - AvailabilityManager:Scheduled
                      - AvailabilityManager:ScheduledOn
                      - AvailabilityManager:ScheduledOff
                      - AvailabilityManager:NightCycle
                      - AvailabilityManager:DifferentialThermostat
                      - AvailabilityManager:HighTemperatureTurnOff
                      - AvailabilityManager:HighTemperatureTurnOn
                      - AvailabilityManager:LowTemperatureTurnOff
                      - AvailabilityManager:LowTemperatureTurnOn
                      - AvailabilityManager:NightVentilation
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
                                 'for field `availability_manager_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_3_object_type`')
            vals = set()
            vals.add("AvailabilityManager:Scheduled")
            vals.add("AvailabilityManager:ScheduledOn")
            vals.add("AvailabilityManager:ScheduledOff")
            vals.add("AvailabilityManager:NightCycle")
            vals.add("AvailabilityManager:DifferentialThermostat")
            vals.add("AvailabilityManager:HighTemperatureTurnOff")
            vals.add("AvailabilityManager:HighTemperatureTurnOn")
            vals.add("AvailabilityManager:LowTemperatureTurnOff")
            vals.add("AvailabilityManager:LowTemperatureTurnOn")
            vals.add("AvailabilityManager:NightVentilation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `availability_manager_3_object_type`'.format(value))

        self._data["Availability Manager 3 Object Type"] = value

    @property
    def availability_manager_3_name(self):
        """Get availability_manager_3_name

        Returns:
            str: the value of `availability_manager_3_name` or None if not set
        """
        return self._data["Availability Manager 3 Name"]

    @availability_manager_3_name.setter
    def availability_manager_3_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_3_name`

        Args:
            value (str): value for IDD Field `availability_manager_3_name`
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
                                 'for field `availability_manager_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_3_name`')

        self._data["Availability Manager 3 Name"] = value

    @property
    def availability_manager_4_object_type(self):
        """Get availability_manager_4_object_type

        Returns:
            str: the value of `availability_manager_4_object_type` or None if not set
        """
        return self._data["Availability Manager 4 Object Type"]

    @availability_manager_4_object_type.setter
    def availability_manager_4_object_type(self, value=None):
        """  Corresponds to IDD Field `availability_manager_4_object_type`

        Args:
            value (str): value for IDD Field `availability_manager_4_object_type`
                Accepted values are:
                      - AvailabilityManager:Scheduled
                      - AvailabilityManager:ScheduledOn
                      - AvailabilityManager:ScheduledOff
                      - AvailabilityManager:NightCycle
                      - AvailabilityManager:DifferentialThermostat
                      - AvailabilityManager:HighTemperatureTurnOff
                      - AvailabilityManager:HighTemperatureTurnOn
                      - AvailabilityManager:LowTemperatureTurnOff
                      - AvailabilityManager:LowTemperatureTurnOn
                      - AvailabilityManager:NightVentilation
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
                                 'for field `availability_manager_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_4_object_type`')
            vals = set()
            vals.add("AvailabilityManager:Scheduled")
            vals.add("AvailabilityManager:ScheduledOn")
            vals.add("AvailabilityManager:ScheduledOff")
            vals.add("AvailabilityManager:NightCycle")
            vals.add("AvailabilityManager:DifferentialThermostat")
            vals.add("AvailabilityManager:HighTemperatureTurnOff")
            vals.add("AvailabilityManager:HighTemperatureTurnOn")
            vals.add("AvailabilityManager:LowTemperatureTurnOff")
            vals.add("AvailabilityManager:LowTemperatureTurnOn")
            vals.add("AvailabilityManager:NightVentilation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `availability_manager_4_object_type`'.format(value))

        self._data["Availability Manager 4 Object Type"] = value

    @property
    def availability_manager_4_name(self):
        """Get availability_manager_4_name

        Returns:
            str: the value of `availability_manager_4_name` or None if not set
        """
        return self._data["Availability Manager 4 Name"]

    @availability_manager_4_name.setter
    def availability_manager_4_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_4_name`

        Args:
            value (str): value for IDD Field `availability_manager_4_name`
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
                                 'for field `availability_manager_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_4_name`')

        self._data["Availability Manager 4 Name"] = value

    @property
    def availability_manager_5_object_type(self):
        """Get availability_manager_5_object_type

        Returns:
            str: the value of `availability_manager_5_object_type` or None if not set
        """
        return self._data["Availability Manager 5 Object Type"]

    @availability_manager_5_object_type.setter
    def availability_manager_5_object_type(self, value=None):
        """  Corresponds to IDD Field `availability_manager_5_object_type`

        Args:
            value (str): value for IDD Field `availability_manager_5_object_type`
                Accepted values are:
                      - AvailabilityManager:Scheduled
                      - AvailabilityManager:ScheduledOn
                      - AvailabilityManager:ScheduledOff
                      - AvailabilityManager:NightCycle
                      - AvailabilityManager:DifferentialThermostat
                      - AvailabilityManager:HighTemperatureTurnOff
                      - AvailabilityManager:HighTemperatureTurnOn
                      - AvailabilityManager:LowTemperatureTurnOff
                      - AvailabilityManager:LowTemperatureTurnOn
                      - AvailabilityManager:NightVentilation
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
                                 'for field `availability_manager_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_5_object_type`')
            vals = set()
            vals.add("AvailabilityManager:Scheduled")
            vals.add("AvailabilityManager:ScheduledOn")
            vals.add("AvailabilityManager:ScheduledOff")
            vals.add("AvailabilityManager:NightCycle")
            vals.add("AvailabilityManager:DifferentialThermostat")
            vals.add("AvailabilityManager:HighTemperatureTurnOff")
            vals.add("AvailabilityManager:HighTemperatureTurnOn")
            vals.add("AvailabilityManager:LowTemperatureTurnOff")
            vals.add("AvailabilityManager:LowTemperatureTurnOn")
            vals.add("AvailabilityManager:NightVentilation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `availability_manager_5_object_type`'.format(value))

        self._data["Availability Manager 5 Object Type"] = value

    @property
    def availability_manager_5_name(self):
        """Get availability_manager_5_name

        Returns:
            str: the value of `availability_manager_5_name` or None if not set
        """
        return self._data["Availability Manager 5 Name"]

    @availability_manager_5_name.setter
    def availability_manager_5_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_5_name`

        Args:
            value (str): value for IDD Field `availability_manager_5_name`
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
                                 'for field `availability_manager_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_5_name`')

        self._data["Availability Manager 5 Name"] = value

    @property
    def availability_manager_6_object_type(self):
        """Get availability_manager_6_object_type

        Returns:
            str: the value of `availability_manager_6_object_type` or None if not set
        """
        return self._data["Availability Manager 6 Object Type"]

    @availability_manager_6_object_type.setter
    def availability_manager_6_object_type(self, value=None):
        """  Corresponds to IDD Field `availability_manager_6_object_type`

        Args:
            value (str): value for IDD Field `availability_manager_6_object_type`
                Accepted values are:
                      - AvailabilityManager:Scheduled
                      - AvailabilityManager:ScheduledOn
                      - AvailabilityManager:ScheduledOff
                      - AvailabilityManager:NightCycle
                      - AvailabilityManager:DifferentialThermostat
                      - AvailabilityManager:HighTemperatureTurnOff
                      - AvailabilityManager:HighTemperatureTurnOn
                      - AvailabilityManager:LowTemperatureTurnOff
                      - AvailabilityManager:LowTemperatureTurnOn
                      - AvailabilityManager:NightVentilation
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
                                 'for field `availability_manager_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_6_object_type`')
            vals = set()
            vals.add("AvailabilityManager:Scheduled")
            vals.add("AvailabilityManager:ScheduledOn")
            vals.add("AvailabilityManager:ScheduledOff")
            vals.add("AvailabilityManager:NightCycle")
            vals.add("AvailabilityManager:DifferentialThermostat")
            vals.add("AvailabilityManager:HighTemperatureTurnOff")
            vals.add("AvailabilityManager:HighTemperatureTurnOn")
            vals.add("AvailabilityManager:LowTemperatureTurnOff")
            vals.add("AvailabilityManager:LowTemperatureTurnOn")
            vals.add("AvailabilityManager:NightVentilation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `availability_manager_6_object_type`'.format(value))

        self._data["Availability Manager 6 Object Type"] = value

    @property
    def availability_manager_6_name(self):
        """Get availability_manager_6_name

        Returns:
            str: the value of `availability_manager_6_name` or None if not set
        """
        return self._data["Availability Manager 6 Name"]

    @availability_manager_6_name.setter
    def availability_manager_6_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_6_name`

        Args:
            value (str): value for IDD Field `availability_manager_6_name`
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
                                 'for field `availability_manager_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_6_name`')

        self._data["Availability Manager 6 Name"] = value

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
        out.append(self._to_str(self.availability_manager_1_object_type))
        out.append(self._to_str(self.availability_manager_1_name))
        out.append(self._to_str(self.availability_manager_2_object_type))
        out.append(self._to_str(self.availability_manager_2_name))
        out.append(self._to_str(self.availability_manager_3_object_type))
        out.append(self._to_str(self.availability_manager_3_name))
        out.append(self._to_str(self.availability_manager_4_object_type))
        out.append(self._to_str(self.availability_manager_4_name))
        out.append(self._to_str(self.availability_manager_5_object_type))
        out.append(self._to_str(self.availability_manager_5_name))
        out.append(self._to_str(self.availability_manager_6_object_type))
        out.append(self._to_str(self.availability_manager_6_name))
        return ",".join(out)