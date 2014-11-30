from collections import OrderedDict

class AvailabilityManagerScheduled(object):
    """ Corresponds to IDD object `AvailabilityManager:Scheduled`
        Determines the availability of a loop or system: whether it is on or off.
        Schedule overrides fan/pump schedule.
    
    """
    internal_name = "AvailabilityManager:Scheduled"
    field_count = 2
    required_fields = ["Name", "Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:Scheduled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Name"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)

class AvailabilityManagerScheduledOn(object):
    """ Corresponds to IDD object `AvailabilityManager:ScheduledOn`
        Determines the availability of a loop or system: only controls the turn on action.
        Schedule overrides fan/pump schedule.
    
    """
    internal_name = "AvailabilityManager:ScheduledOn"
    field_count = 2
    required_fields = ["Name", "Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:ScheduledOn`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Name"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)

class AvailabilityManagerScheduledOff(object):
    """ Corresponds to IDD object `AvailabilityManager:ScheduledOff`
        Determines the availability of a loop or system: only controls the turn off action.
        Schedule overrides fan/pump schedule.
    
    """
    internal_name = "AvailabilityManager:ScheduledOff"
    field_count = 2
    required_fields = ["Name", "Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:ScheduledOff`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Name"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)

class AvailabilityManagerOptimumStart(object):
    """ Corresponds to IDD object `AvailabilityManager:OptimumStart`
        Determines the optimal start of HVAC systems before occupancy.
    
    """
    internal_name = "AvailabilityManager:OptimumStart"
    field_count = 14
    required_fields = ["Name", "Applicability Schedule Name", "Fan Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:OptimumStart`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Applicability Schedule Name"] = None
        self._data["Fan Schedule Name"] = None
        self._data["Control Type"] = None
        self._data["Control Zone Name"] = None
        self._data["Zone List Name"] = None
        self._data["Maximum Value for Optimum Start Time"] = None
        self._data["Control Algorithm"] = None
        self._data["Constant Temperature Gradient during Cooling"] = None
        self._data["Constant Temperature Gradient during Heating"] = None
        self._data["Initial Temperature Gradient during Cooling"] = None
        self._data["Initial Temperature Gradient during Heating"] = None
        self._data["Constant Start Time"] = None
        self._data["Number of Previous Days"] = None

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
            self.applicability_schedule_name = None
        else:
            self.applicability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_schedule_name = None
        else:
            self.fan_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_list_name = None
        else:
            self.zone_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_for_optimum_start_time = None
        else:
            self.maximum_value_for_optimum_start_time = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_algorithm = None
        else:
            self.control_algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_temperature_gradient_during_cooling = None
        else:
            self.constant_temperature_gradient_during_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_temperature_gradient_during_heating = None
        else:
            self.constant_temperature_gradient_during_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_temperature_gradient_during_cooling = None
        else:
            self.initial_temperature_gradient_during_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_temperature_gradient_during_heating = None
        else:
            self.initial_temperature_gradient_during_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_start_time = None
        else:
            self.constant_start_time = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_previous_days = None
        else:
            self.number_of_previous_days = vals[i]
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
    def applicability_schedule_name(self):
        """Get applicability_schedule_name

        Returns:
            str: the value of `applicability_schedule_name` or None if not set
        """
        return self._data["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `applicability_schedule_name`

        Args:
            value (str): value for IDD Field `applicability_schedule_name`
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
                                 'for field `applicability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `applicability_schedule_name`')

        self._data["Applicability Schedule Name"] = value

    @property
    def fan_schedule_name(self):
        """Get fan_schedule_name

        Returns:
            str: the value of `fan_schedule_name` or None if not set
        """
        return self._data["Fan Schedule Name"]

    @fan_schedule_name.setter
    def fan_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fan_schedule_name`

        Args:
            value (str): value for IDD Field `fan_schedule_name`
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
                                 'for field `fan_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_schedule_name`')

        self._data["Fan Schedule Name"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value="ControlZone"):
        """  Corresponds to IDD Field `control_type`

        Args:
            value (str): value for IDD Field `control_type`
                Accepted values are:
                      - StayOff
                      - ControlZone
                      - MaximumofZoneList
                Default value: ControlZone
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
                                 'for field `control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_type`')
            vals = set()
            vals.add("StayOff")
            vals.add("ControlZone")
            vals.add("MaximumofZoneList")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_type`'.format(value))

        self._data["Control Type"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `control_zone_name`

        Args:
            value (str): value for IDD Field `control_zone_name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')

        self._data["Control Zone Name"] = value

    @property
    def zone_list_name(self):
        """Get zone_list_name

        Returns:
            str: the value of `zone_list_name` or None if not set
        """
        return self._data["Zone List Name"]

    @zone_list_name.setter
    def zone_list_name(self, value=None):
        """  Corresponds to IDD Field `zone_list_name`

        Args:
            value (str): value for IDD Field `zone_list_name`
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
                                 'for field `zone_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_list_name`')

        self._data["Zone List Name"] = value

    @property
    def maximum_value_for_optimum_start_time(self):
        """Get maximum_value_for_optimum_start_time

        Returns:
            float: the value of `maximum_value_for_optimum_start_time` or None if not set
        """
        return self._data["Maximum Value for Optimum Start Time"]

    @maximum_value_for_optimum_start_time.setter
    def maximum_value_for_optimum_start_time(self, value=6.0 ):
        """  Corresponds to IDD Field `maximum_value_for_optimum_start_time`
        this is the maximum number of hours that a system can start before occupancy

        Args:
            value (float): value for IDD Field `maximum_value_for_optimum_start_time`
                Units: hr
                Default value: 6.0
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
                                 'for field `maximum_value_for_optimum_start_time`'.format(value))

        self._data["Maximum Value for Optimum Start Time"] = value

    @property
    def control_algorithm(self):
        """Get control_algorithm

        Returns:
            str: the value of `control_algorithm` or None if not set
        """
        return self._data["Control Algorithm"]

    @control_algorithm.setter
    def control_algorithm(self, value="AdaptiveASHRAE"):
        """  Corresponds to IDD Field `control_algorithm`

        Args:
            value (str): value for IDD Field `control_algorithm`
                Accepted values are:
                      - ConstantTemperatureGradient
                      - AdaptiveTemperatureGradient
                      - AdaptiveASHRAE
                      - ConstantStartTime
                Default value: AdaptiveASHRAE
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
                                 'for field `control_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_algorithm`')
            vals = set()
            vals.add("ConstantTemperatureGradient")
            vals.add("AdaptiveTemperatureGradient")
            vals.add("AdaptiveASHRAE")
            vals.add("ConstantStartTime")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_algorithm`'.format(value))

        self._data["Control Algorithm"] = value

    @property
    def constant_temperature_gradient_during_cooling(self):
        """Get constant_temperature_gradient_during_cooling

        Returns:
            float: the value of `constant_temperature_gradient_during_cooling` or None if not set
        """
        return self._data["Constant Temperature Gradient during Cooling"]

    @constant_temperature_gradient_during_cooling.setter
    def constant_temperature_gradient_during_cooling(self, value=None):
        """  Corresponds to IDD Field `constant_temperature_gradient_during_cooling`

        Args:
            value (float): value for IDD Field `constant_temperature_gradient_during_cooling`
                Units: deltaC/hr
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
                                 'for field `constant_temperature_gradient_during_cooling`'.format(value))

        self._data["Constant Temperature Gradient during Cooling"] = value

    @property
    def constant_temperature_gradient_during_heating(self):
        """Get constant_temperature_gradient_during_heating

        Returns:
            float: the value of `constant_temperature_gradient_during_heating` or None if not set
        """
        return self._data["Constant Temperature Gradient during Heating"]

    @constant_temperature_gradient_during_heating.setter
    def constant_temperature_gradient_during_heating(self, value=None):
        """  Corresponds to IDD Field `constant_temperature_gradient_during_heating`

        Args:
            value (float): value for IDD Field `constant_temperature_gradient_during_heating`
                Units: deltaC/hr
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
                                 'for field `constant_temperature_gradient_during_heating`'.format(value))

        self._data["Constant Temperature Gradient during Heating"] = value

    @property
    def initial_temperature_gradient_during_cooling(self):
        """Get initial_temperature_gradient_during_cooling

        Returns:
            float: the value of `initial_temperature_gradient_during_cooling` or None if not set
        """
        return self._data["Initial Temperature Gradient during Cooling"]

    @initial_temperature_gradient_during_cooling.setter
    def initial_temperature_gradient_during_cooling(self, value=None):
        """  Corresponds to IDD Field `initial_temperature_gradient_during_cooling`

        Args:
            value (float): value for IDD Field `initial_temperature_gradient_during_cooling`
                Units: deltaC/hr
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
                                 'for field `initial_temperature_gradient_during_cooling`'.format(value))

        self._data["Initial Temperature Gradient during Cooling"] = value

    @property
    def initial_temperature_gradient_during_heating(self):
        """Get initial_temperature_gradient_during_heating

        Returns:
            float: the value of `initial_temperature_gradient_during_heating` or None if not set
        """
        return self._data["Initial Temperature Gradient during Heating"]

    @initial_temperature_gradient_during_heating.setter
    def initial_temperature_gradient_during_heating(self, value=None):
        """  Corresponds to IDD Field `initial_temperature_gradient_during_heating`

        Args:
            value (float): value for IDD Field `initial_temperature_gradient_during_heating`
                Units: deltaC/hr
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
                                 'for field `initial_temperature_gradient_during_heating`'.format(value))

        self._data["Initial Temperature Gradient during Heating"] = value

    @property
    def constant_start_time(self):
        """Get constant_start_time

        Returns:
            float: the value of `constant_start_time` or None if not set
        """
        return self._data["Constant Start Time"]

    @constant_start_time.setter
    def constant_start_time(self, value=None):
        """  Corresponds to IDD Field `constant_start_time`
        this is the number of hours before occupancy for a system

        Args:
            value (float): value for IDD Field `constant_start_time`
                Units: hr
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
                                 'for field `constant_start_time`'.format(value))

        self._data["Constant Start Time"] = value

    @property
    def number_of_previous_days(self):
        """Get number_of_previous_days

        Returns:
            int: the value of `number_of_previous_days` or None if not set
        """
        return self._data["Number of Previous Days"]

    @number_of_previous_days.setter
    def number_of_previous_days(self, value=2 ):
        """  Corresponds to IDD Field `number_of_previous_days`
        this is the number of days that their actual temperature
        gradients will be used in the AdaptiveTemperatureGradient method

        Args:
            value (int): value for IDD Field `number_of_previous_days`
                Units: days
                Default value: 2
                value >= 2
                value <= 5
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
                                 'for field `number_of_previous_days`'.format(value))
            if value < 2:
                raise ValueError('value need to be greater or equal 2 '
                                 'for field `number_of_previous_days`')
            if value > 5:
                raise ValueError('value need to be smaller 5 '
                                 'for field `number_of_previous_days`')

        self._data["Number of Previous Days"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.applicability_schedule_name))
        out.append(self._to_str(self.fan_schedule_name))
        out.append(self._to_str(self.control_type))
        out.append(self._to_str(self.control_zone_name))
        out.append(self._to_str(self.zone_list_name))
        out.append(self._to_str(self.maximum_value_for_optimum_start_time))
        out.append(self._to_str(self.control_algorithm))
        out.append(self._to_str(self.constant_temperature_gradient_during_cooling))
        out.append(self._to_str(self.constant_temperature_gradient_during_heating))
        out.append(self._to_str(self.initial_temperature_gradient_during_cooling))
        out.append(self._to_str(self.initial_temperature_gradient_during_heating))
        out.append(self._to_str(self.constant_start_time))
        out.append(self._to_str(self.number_of_previous_days))
        return ",".join(out)

class AvailabilityManagerNightCycle(object):
    """ Corresponds to IDD object `AvailabilityManager:NightCycle`
        Determines the availability of a loop or system: whether it is on or off.
        Depending on zone temperatures, overrides Schedules and forces system Fans on.
    
    """
    internal_name = "AvailabilityManager:NightCycle"
    field_count = 7
    required_fields = ["Name", "Applicability Schedule Name", "Fan Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:NightCycle`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Applicability Schedule Name"] = None
        self._data["Fan Schedule Name"] = None
        self._data["Control Type"] = None
        self._data["Thermostat Tolerance"] = None
        self._data["Cycling Run Time"] = None
        self._data["Control Zone Name"] = None

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
            self.applicability_schedule_name = None
        else:
            self.applicability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_schedule_name = None
        else:
            self.fan_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_tolerance = None
        else:
            self.thermostat_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cycling_run_time = None
        else:
            self.cycling_run_time = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
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
    def applicability_schedule_name(self):
        """Get applicability_schedule_name

        Returns:
            str: the value of `applicability_schedule_name` or None if not set
        """
        return self._data["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `applicability_schedule_name`

        Args:
            value (str): value for IDD Field `applicability_schedule_name`
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
                                 'for field `applicability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `applicability_schedule_name`')

        self._data["Applicability Schedule Name"] = value

    @property
    def fan_schedule_name(self):
        """Get fan_schedule_name

        Returns:
            str: the value of `fan_schedule_name` or None if not set
        """
        return self._data["Fan Schedule Name"]

    @fan_schedule_name.setter
    def fan_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fan_schedule_name`

        Args:
            value (str): value for IDD Field `fan_schedule_name`
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
                                 'for field `fan_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_schedule_name`')

        self._data["Fan Schedule Name"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value="StayOff"):
        """  Corresponds to IDD Field `control_type`
        When AvailabilityManager:NightCycle is used in the zone component availability
        manager assignment list, the key choices for Control Type would only be
        StayOff and CycleOnControlZone

        Args:
            value (str): value for IDD Field `control_type`
                Accepted values are:
                      - StayOff
                      - CycleOnAny
                      - CycleOnControlZone
                      - CycleOnAnyZoneFansOnly
                Default value: StayOff
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
                                 'for field `control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_type`')
            vals = set()
            vals.add("StayOff")
            vals.add("CycleOnAny")
            vals.add("CycleOnControlZone")
            vals.add("CycleOnAnyZoneFansOnly")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_type`'.format(value))

        self._data["Control Type"] = value

    @property
    def thermostat_tolerance(self):
        """Get thermostat_tolerance

        Returns:
            float: the value of `thermostat_tolerance` or None if not set
        """
        return self._data["Thermostat Tolerance"]

    @thermostat_tolerance.setter
    def thermostat_tolerance(self, value=1.0 ):
        """  Corresponds to IDD Field `thermostat_tolerance`

        Args:
            value (float): value for IDD Field `thermostat_tolerance`
                Units: deltaC
                Default value: 1.0
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
                                 'for field `thermostat_tolerance`'.format(value))

        self._data["Thermostat Tolerance"] = value

    @property
    def cycling_run_time(self):
        """Get cycling_run_time

        Returns:
            float: the value of `cycling_run_time` or None if not set
        """
        return self._data["Cycling Run Time"]

    @cycling_run_time.setter
    def cycling_run_time(self, value=3600.0 ):
        """  Corresponds to IDD Field `cycling_run_time`

        Args:
            value (float): value for IDD Field `cycling_run_time`
                Units: s
                Default value: 3600.0
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
                                 'for field `cycling_run_time`'.format(value))

        self._data["Cycling Run Time"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `control_zone_name`
        When AvailabilityManager:NightCycle is used in the zone component availability
        manager assignment list, the Control Zone Name should be the name of the zone in which the
        zone component is.

        Args:
            value (str): value for IDD Field `control_zone_name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')

        self._data["Control Zone Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.applicability_schedule_name))
        out.append(self._to_str(self.fan_schedule_name))
        out.append(self._to_str(self.control_type))
        out.append(self._to_str(self.thermostat_tolerance))
        out.append(self._to_str(self.cycling_run_time))
        out.append(self._to_str(self.control_zone_name))
        return ",".join(out)

class AvailabilityManagerDifferentialThermostat(object):
    """ Corresponds to IDD object `AvailabilityManager:DifferentialThermostat`
        Overrides fan/pump schedules depending on temperature difference between two nodes.
    
    """
    internal_name = "AvailabilityManager:DifferentialThermostat"
    field_count = 5
    required_fields = ["Name", "Hot Node Name", "Cold Node Name", "Temperature Difference On Limit"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:DifferentialThermostat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Hot Node Name"] = None
        self._data["Cold Node Name"] = None
        self._data["Temperature Difference On Limit"] = None
        self._data["Temperature Difference Off Limit"] = None

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
            self.hot_node_name = None
        else:
            self.hot_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cold_node_name = None
        else:
            self.cold_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_difference_on_limit = None
        else:
            self.temperature_difference_on_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_difference_off_limit = None
        else:
            self.temperature_difference_off_limit = vals[i]
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
    def hot_node_name(self):
        """Get hot_node_name

        Returns:
            str: the value of `hot_node_name` or None if not set
        """
        return self._data["Hot Node Name"]

    @hot_node_name.setter
    def hot_node_name(self, value=None):
        """  Corresponds to IDD Field `hot_node_name`

        Args:
            value (str): value for IDD Field `hot_node_name`
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
                                 'for field `hot_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_node_name`')

        self._data["Hot Node Name"] = value

    @property
    def cold_node_name(self):
        """Get cold_node_name

        Returns:
            str: the value of `cold_node_name` or None if not set
        """
        return self._data["Cold Node Name"]

    @cold_node_name.setter
    def cold_node_name(self, value=None):
        """  Corresponds to IDD Field `cold_node_name`

        Args:
            value (str): value for IDD Field `cold_node_name`
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
                                 'for field `cold_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_node_name`')

        self._data["Cold Node Name"] = value

    @property
    def temperature_difference_on_limit(self):
        """Get temperature_difference_on_limit

        Returns:
            float: the value of `temperature_difference_on_limit` or None if not set
        """
        return self._data["Temperature Difference On Limit"]

    @temperature_difference_on_limit.setter
    def temperature_difference_on_limit(self, value=None):
        """  Corresponds to IDD Field `temperature_difference_on_limit`

        Args:
            value (float): value for IDD Field `temperature_difference_on_limit`
                Units: deltaC
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
                                 'for field `temperature_difference_on_limit`'.format(value))

        self._data["Temperature Difference On Limit"] = value

    @property
    def temperature_difference_off_limit(self):
        """Get temperature_difference_off_limit

        Returns:
            float: the value of `temperature_difference_off_limit` or None if not set
        """
        return self._data["Temperature Difference Off Limit"]

    @temperature_difference_off_limit.setter
    def temperature_difference_off_limit(self, value=None):
        """  Corresponds to IDD Field `temperature_difference_off_limit`
        Defaults to Temperature Difference On Limit.

        Args:
            value (float): value for IDD Field `temperature_difference_off_limit`
                Units: deltaC
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
                                 'for field `temperature_difference_off_limit`'.format(value))

        self._data["Temperature Difference Off Limit"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.hot_node_name))
        out.append(self._to_str(self.cold_node_name))
        out.append(self._to_str(self.temperature_difference_on_limit))
        out.append(self._to_str(self.temperature_difference_off_limit))
        return ",".join(out)

class AvailabilityManagerHighTemperatureTurnOff(object):
    """ Corresponds to IDD object `AvailabilityManager:HighTemperatureTurnOff`
        Overrides fan/pump schedules depending on temperature at sensor node.
    
    """
    internal_name = "AvailabilityManager:HighTemperatureTurnOff"
    field_count = 3
    required_fields = ["Name", "Sensor Node Name", "Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:HighTemperatureTurnOff`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Temperature"] = None

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
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature = None
        else:
            self.temperature = vals[i]
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
    def sensor_node_name(self):
        """Get sensor_node_name

        Returns:
            str: the value of `sensor_node_name` or None if not set
        """
        return self._data["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `sensor_node_name`

        Args:
            value (str): value for IDD Field `sensor_node_name`
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
                                 'for field `sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensor_node_name`')

        self._data["Sensor Node Name"] = value

    @property
    def temperature(self):
        """Get temperature

        Returns:
            float: the value of `temperature` or None if not set
        """
        return self._data["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """  Corresponds to IDD Field `temperature`

        Args:
            value (float): value for IDD Field `temperature`
                Units: C
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
                                 'for field `temperature`'.format(value))

        self._data["Temperature"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.sensor_node_name))
        out.append(self._to_str(self.temperature))
        return ",".join(out)

class AvailabilityManagerHighTemperatureTurnOn(object):
    """ Corresponds to IDD object `AvailabilityManager:HighTemperatureTurnOn`
        Overrides fan/pump schedules depending on temperature at sensor node.
    
    """
    internal_name = "AvailabilityManager:HighTemperatureTurnOn"
    field_count = 3
    required_fields = ["Name", "Sensor Node Name", "Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:HighTemperatureTurnOn`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Temperature"] = None

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
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature = None
        else:
            self.temperature = vals[i]
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
    def sensor_node_name(self):
        """Get sensor_node_name

        Returns:
            str: the value of `sensor_node_name` or None if not set
        """
        return self._data["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `sensor_node_name`

        Args:
            value (str): value for IDD Field `sensor_node_name`
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
                                 'for field `sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensor_node_name`')

        self._data["Sensor Node Name"] = value

    @property
    def temperature(self):
        """Get temperature

        Returns:
            float: the value of `temperature` or None if not set
        """
        return self._data["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """  Corresponds to IDD Field `temperature`

        Args:
            value (float): value for IDD Field `temperature`
                Units: C
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
                                 'for field `temperature`'.format(value))

        self._data["Temperature"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.sensor_node_name))
        out.append(self._to_str(self.temperature))
        return ",".join(out)

class AvailabilityManagerLowTemperatureTurnOff(object):
    """ Corresponds to IDD object `AvailabilityManager:LowTemperatureTurnOff`
        Overrides fan/pump schedules depending on temperature at sensor node.
    
    """
    internal_name = "AvailabilityManager:LowTemperatureTurnOff"
    field_count = 4
    required_fields = ["Name", "Sensor Node Name", "Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:LowTemperatureTurnOff`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Temperature"] = None
        self._data["Applicability Schedule Name"] = None

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
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature = None
        else:
            self.temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.applicability_schedule_name = None
        else:
            self.applicability_schedule_name = vals[i]
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
    def sensor_node_name(self):
        """Get sensor_node_name

        Returns:
            str: the value of `sensor_node_name` or None if not set
        """
        return self._data["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `sensor_node_name`

        Args:
            value (str): value for IDD Field `sensor_node_name`
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
                                 'for field `sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensor_node_name`')

        self._data["Sensor Node Name"] = value

    @property
    def temperature(self):
        """Get temperature

        Returns:
            float: the value of `temperature` or None if not set
        """
        return self._data["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """  Corresponds to IDD Field `temperature`

        Args:
            value (float): value for IDD Field `temperature`
                Units: C
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
                                 'for field `temperature`'.format(value))

        self._data["Temperature"] = value

    @property
    def applicability_schedule_name(self):
        """Get applicability_schedule_name

        Returns:
            str: the value of `applicability_schedule_name` or None if not set
        """
        return self._data["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `applicability_schedule_name`
        If blank, defaults to always active

        Args:
            value (str): value for IDD Field `applicability_schedule_name`
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
                                 'for field `applicability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `applicability_schedule_name`')

        self._data["Applicability Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.sensor_node_name))
        out.append(self._to_str(self.temperature))
        out.append(self._to_str(self.applicability_schedule_name))
        return ",".join(out)

class AvailabilityManagerLowTemperatureTurnOn(object):
    """ Corresponds to IDD object `AvailabilityManager:LowTemperatureTurnOn`
        Overrides fan/pump schedules depending on temperature at sensor node.
    
    """
    internal_name = "AvailabilityManager:LowTemperatureTurnOn"
    field_count = 3
    required_fields = ["Name", "Sensor Node Name", "Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:LowTemperatureTurnOn`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Temperature"] = None

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
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature = None
        else:
            self.temperature = vals[i]
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
    def sensor_node_name(self):
        """Get sensor_node_name

        Returns:
            str: the value of `sensor_node_name` or None if not set
        """
        return self._data["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `sensor_node_name`

        Args:
            value (str): value for IDD Field `sensor_node_name`
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
                                 'for field `sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensor_node_name`')

        self._data["Sensor Node Name"] = value

    @property
    def temperature(self):
        """Get temperature

        Returns:
            float: the value of `temperature` or None if not set
        """
        return self._data["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """  Corresponds to IDD Field `temperature`

        Args:
            value (float): value for IDD Field `temperature`
                Units: C
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
                                 'for field `temperature`'.format(value))

        self._data["Temperature"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.sensor_node_name))
        out.append(self._to_str(self.temperature))
        return ",".join(out)

class AvailabilityManagerNightVentilation(object):
    """ Corresponds to IDD object `AvailabilityManager:NightVentilation`
        depending on zone and outdoor conditions overides fan schedule to do
        precooling with outdoor air
    
    """
    internal_name = "AvailabilityManager:NightVentilation"
    field_count = 8
    required_fields = ["Name", "Applicability Schedule Name", "Fan Schedule Name", "Control Zone Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:NightVentilation`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Applicability Schedule Name"] = None
        self._data["Fan Schedule Name"] = None
        self._data["Ventilation Temperature Schedule Name"] = None
        self._data["Ventilation Temperature Difference"] = None
        self._data["Ventilation Temperature Low Limit"] = None
        self._data["Night Venting Flow Fraction"] = None
        self._data["Control Zone Name"] = None

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
            self.applicability_schedule_name = None
        else:
            self.applicability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_schedule_name = None
        else:
            self.fan_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_temperature_schedule_name = None
        else:
            self.ventilation_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_temperature_difference = None
        else:
            self.ventilation_temperature_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_temperature_low_limit = None
        else:
            self.ventilation_temperature_low_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.night_venting_flow_fraction = None
        else:
            self.night_venting_flow_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
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
    def applicability_schedule_name(self):
        """Get applicability_schedule_name

        Returns:
            str: the value of `applicability_schedule_name` or None if not set
        """
        return self._data["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `applicability_schedule_name`

        Args:
            value (str): value for IDD Field `applicability_schedule_name`
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
                                 'for field `applicability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `applicability_schedule_name`')

        self._data["Applicability Schedule Name"] = value

    @property
    def fan_schedule_name(self):
        """Get fan_schedule_name

        Returns:
            str: the value of `fan_schedule_name` or None if not set
        """
        return self._data["Fan Schedule Name"]

    @fan_schedule_name.setter
    def fan_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fan_schedule_name`

        Args:
            value (str): value for IDD Field `fan_schedule_name`
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
                                 'for field `fan_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_schedule_name`')

        self._data["Fan Schedule Name"] = value

    @property
    def ventilation_temperature_schedule_name(self):
        """Get ventilation_temperature_schedule_name

        Returns:
            str: the value of `ventilation_temperature_schedule_name` or None if not set
        """
        return self._data["Ventilation Temperature Schedule Name"]

    @ventilation_temperature_schedule_name.setter
    def ventilation_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ventilation_temperature_schedule_name`
        One zone temperature must be above this scheduled temperature
        for night ventilation to be enabled

        Args:
            value (str): value for IDD Field `ventilation_temperature_schedule_name`
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
                                 'for field `ventilation_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_temperature_schedule_name`')

        self._data["Ventilation Temperature Schedule Name"] = value

    @property
    def ventilation_temperature_difference(self):
        """Get ventilation_temperature_difference

        Returns:
            float: the value of `ventilation_temperature_difference` or None if not set
        """
        return self._data["Ventilation Temperature Difference"]

    @ventilation_temperature_difference.setter
    def ventilation_temperature_difference(self, value=2.0 ):
        """  Corresponds to IDD Field `ventilation_temperature_difference`
        The outdoor air temperature minus the control zone temperature
        must be greater than the ventilation delta T

        Args:
            value (float): value for IDD Field `ventilation_temperature_difference`
                Units: deltaC
                Default value: 2.0
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
                                 'for field `ventilation_temperature_difference`'.format(value))

        self._data["Ventilation Temperature Difference"] = value

    @property
    def ventilation_temperature_low_limit(self):
        """Get ventilation_temperature_low_limit

        Returns:
            float: the value of `ventilation_temperature_low_limit` or None if not set
        """
        return self._data["Ventilation Temperature Low Limit"]

    @ventilation_temperature_low_limit.setter
    def ventilation_temperature_low_limit(self, value=15.0 ):
        """  Corresponds to IDD Field `ventilation_temperature_low_limit`
        Night ventilation is disabled if any conditioned zone served by
        the system falls below this temperature

        Args:
            value (float): value for IDD Field `ventilation_temperature_low_limit`
                Units: C
                Default value: 15.0
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
                                 'for field `ventilation_temperature_low_limit`'.format(value))

        self._data["Ventilation Temperature Low Limit"] = value

    @property
    def night_venting_flow_fraction(self):
        """Get night_venting_flow_fraction

        Returns:
            float: the value of `night_venting_flow_fraction` or None if not set
        """
        return self._data["Night Venting Flow Fraction"]

    @night_venting_flow_fraction.setter
    def night_venting_flow_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `night_venting_flow_fraction`
        the fraction (could be > 1) of the design system Flow Rate at which
        night ventilation will be done

        Args:
            value (float): value for IDD Field `night_venting_flow_fraction`
                Default value: 1.0
                value >= 0.0
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
                                 'for field `night_venting_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `night_venting_flow_fraction`')

        self._data["Night Venting Flow Fraction"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `control_zone_name`
        When AvailabilityManager:NightVentilation is used in the zone component availability
        manager assignment list, the Control Zone Name should be the name of the zone in which the
        zone component is.

        Args:
            value (str): value for IDD Field `control_zone_name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')

        self._data["Control Zone Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.applicability_schedule_name))
        out.append(self._to_str(self.fan_schedule_name))
        out.append(self._to_str(self.ventilation_temperature_schedule_name))
        out.append(self._to_str(self.ventilation_temperature_difference))
        out.append(self._to_str(self.ventilation_temperature_low_limit))
        out.append(self._to_str(self.night_venting_flow_fraction))
        out.append(self._to_str(self.control_zone_name))
        return ",".join(out)

class AvailabilityManagerHybridVentilation(object):
    """ Corresponds to IDD object `AvailabilityManager:HybridVentilation`
        Depending on zone and outdoor conditions overrides window/door opening controls
        to maximize natural ventilation and turn off an HVAC system when ventilation control
        conditions are met.
        This object (zone ventilation object name) has not been instrumented to work with
        global Zone or Zone List names option for Ventilation:DesignFlowRate.  In order to
        use, you must enter the single <Ventilation:DesignFlowRate> name in that
        field. If it is a part of a global ventilation assignement the name will be
        <Zone Name> <global Ventilation:DesignFlowRate> name.
        Currently, hybrid ventilation manager is restricted to one per zone. It can either be applied
        through the air loop or directly to the zone. If hybrid ventilation manager is applied to an
        air loop and one of the zones served by that air loop also has hybrid ventilation manager,
        then zone hybrid ventilation manager is disabled.
    
    """
    internal_name = "AvailabilityManager:HybridVentilation"
    field_count = 17
    required_fields = ["Name", "Controlled Zone Name", "Ventilation Control Mode Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManager:HybridVentilation`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Controlled Zone Name"] = None
        self._data["Ventilation Control Mode Schedule Name"] = None
        self._data["Use Weather File Rain Indicators"] = None
        self._data["Maximum Wind Speed"] = None
        self._data["Minimum Outdoor Temperature"] = None
        self._data["Maximum Outdoor Temperature"] = None
        self._data["Minimum Outdoor Enthalpy"] = None
        self._data["Maximum Outdoor Enthalpy"] = None
        self._data["Minimum Outdoor Dewpoint"] = None
        self._data["Maximum Outdoor Dewpoint"] = None
        self._data["Minimum Outdoor Ventilation Air Schedule Name"] = None
        self._data["Opening Factor Function of Wind Speed Curve Name"] = None
        self._data["AirflowNetwork Control Type Schedule Name"] = None
        self._data["Simple Airflow Control Type Schedule Name"] = None
        self._data["ZoneVentilation Object Name"] = None

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
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlled_zone_name = None
        else:
            self.controlled_zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_control_mode_schedule_name = None
        else:
            self.ventilation_control_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_rain_indicators = None
        else:
            self.use_weather_file_rain_indicators = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_wind_speed = None
        else:
            self.maximum_wind_speed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature = None
        else:
            self.minimum_outdoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature = None
        else:
            self.maximum_outdoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_enthalpy = None
        else:
            self.minimum_outdoor_enthalpy = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_enthalpy = None
        else:
            self.maximum_outdoor_enthalpy = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_dewpoint = None
        else:
            self.minimum_outdoor_dewpoint = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_dewpoint = None
        else:
            self.maximum_outdoor_dewpoint = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_ventilation_air_schedule_name = None
        else:
            self.minimum_outdoor_ventilation_air_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_factor_function_of_wind_speed_curve_name = None
        else:
            self.opening_factor_function_of_wind_speed_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflownetwork_control_type_schedule_name = None
        else:
            self.airflownetwork_control_type_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_airflow_control_type_schedule_name = None
        else:
            self.simple_airflow_control_type_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zoneventilation_object_name = None
        else:
            self.zoneventilation_object_name = vals[i]
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
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `hvac_air_loop_name`
        Enter the name of an AirLoopHVAC or HVACTemplate:System:* object.
        If this field is left blank, hybrid ventilation managers will be
        simulated for zone equipment control

        Args:
            value (str): value for IDD Field `hvac_air_loop_name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')

        self._data["HVAC Air Loop Name"] = value

    @property
    def controlled_zone_name(self):
        """Get controlled_zone_name

        Returns:
            str: the value of `controlled_zone_name` or None if not set
        """
        return self._data["Controlled Zone Name"]

    @controlled_zone_name.setter
    def controlled_zone_name(self, value=None):
        """  Corresponds to IDD Field `controlled_zone_name`
        the controlled zone name should be a zone where a thermostat or humidistat is located
        served by an air primary loop.

        Args:
            value (str): value for IDD Field `controlled_zone_name`
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
                                 'for field `controlled_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlled_zone_name`')

        self._data["Controlled Zone Name"] = value

    @property
    def ventilation_control_mode_schedule_name(self):
        """Get ventilation_control_mode_schedule_name

        Returns:
            str: the value of `ventilation_control_mode_schedule_name` or None if not set
        """
        return self._data["Ventilation Control Mode Schedule Name"]

    @ventilation_control_mode_schedule_name.setter
    def ventilation_control_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ventilation_control_mode_schedule_name`
        The Ventilation control mode contains appropriate integer control types.
        0 - uncontrolled (Natural ventilation and HVAC system are controlled by themselves)
        1 = Temperature control
        2 = Enthalpy control
        3 = Dewpoint control
        4 = Outdoor ventilation air control

        Args:
            value (str): value for IDD Field `ventilation_control_mode_schedule_name`
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
                                 'for field `ventilation_control_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_control_mode_schedule_name`')

        self._data["Ventilation Control Mode Schedule Name"] = value

    @property
    def use_weather_file_rain_indicators(self):
        """Get use_weather_file_rain_indicators

        Returns:
            str: the value of `use_weather_file_rain_indicators` or None if not set
        """
        return self._data["Use Weather File Rain Indicators"]

    @use_weather_file_rain_indicators.setter
    def use_weather_file_rain_indicators(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_rain_indicators`
        If Yes, ventilation is shutoff when there is rain
        If No, there is no rain control

        Args:
            value (str): value for IDD Field `use_weather_file_rain_indicators`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 'for field `use_weather_file_rain_indicators`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_rain_indicators`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_rain_indicators`'.format(value))

        self._data["Use Weather File Rain Indicators"] = value

    @property
    def maximum_wind_speed(self):
        """Get maximum_wind_speed

        Returns:
            float: the value of `maximum_wind_speed` or None if not set
        """
        return self._data["Maximum Wind Speed"]

    @maximum_wind_speed.setter
    def maximum_wind_speed(self, value=40.0 ):
        """  Corresponds to IDD Field `maximum_wind_speed`
        this is the wind speed above which ventilation is shutoff

        Args:
            value (float): value for IDD Field `maximum_wind_speed`
                Units: m/s
                Default value: 40.0
                value >= 0.0
                value <= 40.0
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
                                 'for field `maximum_wind_speed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_wind_speed`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `maximum_wind_speed`')

        self._data["Maximum Wind Speed"] = value

    @property
    def minimum_outdoor_temperature(self):
        """Get minimum_outdoor_temperature

        Returns:
            float: the value of `minimum_outdoor_temperature` or None if not set
        """
        return self._data["Minimum Outdoor Temperature"]

    @minimum_outdoor_temperature.setter
    def minimum_outdoor_temperature(self, value=-100.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_temperature`
        this is the outdoor temperature below which ventilation is shutoff

        Args:
            value (float): value for IDD Field `minimum_outdoor_temperature`
                Units: C
                Default value: -100.0
                value >= -100.0
                value <= 100.0
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
                                 'for field `minimum_outdoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_outdoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_outdoor_temperature`')

        self._data["Minimum Outdoor Temperature"] = value

    @property
    def maximum_outdoor_temperature(self):
        """Get maximum_outdoor_temperature

        Returns:
            float: the value of `maximum_outdoor_temperature` or None if not set
        """
        return self._data["Maximum Outdoor Temperature"]

    @maximum_outdoor_temperature.setter
    def maximum_outdoor_temperature(self, value=100.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_temperature`
        this is the outdoor temperature above which ventilation is shutoff

        Args:
            value (float): value for IDD Field `maximum_outdoor_temperature`
                Units: C
                Default value: 100.0
                value >= -100.0
                value <= 100.0
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
                                 'for field `maximum_outdoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `maximum_outdoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_outdoor_temperature`')

        self._data["Maximum Outdoor Temperature"] = value

    @property
    def minimum_outdoor_enthalpy(self):
        """Get minimum_outdoor_enthalpy

        Returns:
            float: the value of `minimum_outdoor_enthalpy` or None if not set
        """
        return self._data["Minimum Outdoor Enthalpy"]

    @minimum_outdoor_enthalpy.setter
    def minimum_outdoor_enthalpy(self, value=None):
        """  Corresponds to IDD Field `minimum_outdoor_enthalpy`
        this is the outdoor Enthalpy below which ventilation is shutoff

        Args:
            value (float): value for IDD Field `minimum_outdoor_enthalpy`
                Units: J/kg
                value > 0.0
                value < 300000.0
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
                                 'for field `minimum_outdoor_enthalpy`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_outdoor_enthalpy`')
            if value >= 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `minimum_outdoor_enthalpy`')

        self._data["Minimum Outdoor Enthalpy"] = value

    @property
    def maximum_outdoor_enthalpy(self):
        """Get maximum_outdoor_enthalpy

        Returns:
            float: the value of `maximum_outdoor_enthalpy` or None if not set
        """
        return self._data["Maximum Outdoor Enthalpy"]

    @maximum_outdoor_enthalpy.setter
    def maximum_outdoor_enthalpy(self, value=None):
        """  Corresponds to IDD Field `maximum_outdoor_enthalpy`
        this is the outdoor Enthalpy above which ventilation is shutoff

        Args:
            value (float): value for IDD Field `maximum_outdoor_enthalpy`
                Units: J/kg
                value > 0.0
                value < 300000.0
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
                                 'for field `maximum_outdoor_enthalpy`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_outdoor_enthalpy`')
            if value >= 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `maximum_outdoor_enthalpy`')

        self._data["Maximum Outdoor Enthalpy"] = value

    @property
    def minimum_outdoor_dewpoint(self):
        """Get minimum_outdoor_dewpoint

        Returns:
            float: the value of `minimum_outdoor_dewpoint` or None if not set
        """
        return self._data["Minimum Outdoor Dewpoint"]

    @minimum_outdoor_dewpoint.setter
    def minimum_outdoor_dewpoint(self, value=-100.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_dewpoint`
        this is the outdoor temperature below which ventilation is shutoff
        Applicable only if Ventilation Control Mode = 3

        Args:
            value (float): value for IDD Field `minimum_outdoor_dewpoint`
                Units: C
                Default value: -100.0
                value >= -100.0
                value <= 100.0
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
                                 'for field `minimum_outdoor_dewpoint`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_outdoor_dewpoint`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_outdoor_dewpoint`')

        self._data["Minimum Outdoor Dewpoint"] = value

    @property
    def maximum_outdoor_dewpoint(self):
        """Get maximum_outdoor_dewpoint

        Returns:
            float: the value of `maximum_outdoor_dewpoint` or None if not set
        """
        return self._data["Maximum Outdoor Dewpoint"]

    @maximum_outdoor_dewpoint.setter
    def maximum_outdoor_dewpoint(self, value=100.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_dewpoint`
        this is the outdoor dewpoint above which ventilation is shutoff
        Applicable only if Ventilation Control Mode = 3

        Args:
            value (float): value for IDD Field `maximum_outdoor_dewpoint`
                Units: C
                Default value: 100.0
                value >= -100.0
                value <= 100.0
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
                                 'for field `maximum_outdoor_dewpoint`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `maximum_outdoor_dewpoint`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_outdoor_dewpoint`')

        self._data["Maximum Outdoor Dewpoint"] = value

    @property
    def minimum_outdoor_ventilation_air_schedule_name(self):
        """Get minimum_outdoor_ventilation_air_schedule_name

        Returns:
            str: the value of `minimum_outdoor_ventilation_air_schedule_name` or None if not set
        """
        return self._data["Minimum Outdoor Ventilation Air Schedule Name"]

    @minimum_outdoor_ventilation_air_schedule_name.setter
    def minimum_outdoor_ventilation_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_outdoor_ventilation_air_schedule_name`
        Used only if Ventilation Control Mode = 4

        Args:
            value (str): value for IDD Field `minimum_outdoor_ventilation_air_schedule_name`
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
                                 'for field `minimum_outdoor_ventilation_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_outdoor_ventilation_air_schedule_name`')

        self._data["Minimum Outdoor Ventilation Air Schedule Name"] = value

    @property
    def opening_factor_function_of_wind_speed_curve_name(self):
        """Get opening_factor_function_of_wind_speed_curve_name

        Returns:
            str: the value of `opening_factor_function_of_wind_speed_curve_name` or None if not set
        """
        return self._data["Opening Factor Function of Wind Speed Curve Name"]

    @opening_factor_function_of_wind_speed_curve_name.setter
    def opening_factor_function_of_wind_speed_curve_name(self, value=None):
        """  Corresponds to IDD Field `opening_factor_function_of_wind_speed_curve_name`
        Table:OneIndependentVariable object can also be used
        linear curve = a + b*WS
        quadratic curve = a + b*WS + c*WS**2
        WS = wind speed (m/s)

        Args:
            value (str): value for IDD Field `opening_factor_function_of_wind_speed_curve_name`
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
                                 'for field `opening_factor_function_of_wind_speed_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `opening_factor_function_of_wind_speed_curve_name`')

        self._data["Opening Factor Function of Wind Speed Curve Name"] = value

    @property
    def airflownetwork_control_type_schedule_name(self):
        """Get airflownetwork_control_type_schedule_name

        Returns:
            str: the value of `airflownetwork_control_type_schedule_name` or None if not set
        """
        return self._data["AirflowNetwork Control Type Schedule Name"]

    @airflownetwork_control_type_schedule_name.setter
    def airflownetwork_control_type_schedule_name(self, value=None):
        """  Corresponds to IDD Field `airflownetwork_control_type_schedule_name`
        The schedule is used to incorporate operation of AirflowNetwork large opening
        objects and HVAC system operation.

        Args:
            value (str): value for IDD Field `airflownetwork_control_type_schedule_name`
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
                                 'for field `airflownetwork_control_type_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflownetwork_control_type_schedule_name`')

        self._data["AirflowNetwork Control Type Schedule Name"] = value

    @property
    def simple_airflow_control_type_schedule_name(self):
        """Get simple_airflow_control_type_schedule_name

        Returns:
            str: the value of `simple_airflow_control_type_schedule_name` or None if not set
        """
        return self._data["Simple Airflow Control Type Schedule Name"]

    @simple_airflow_control_type_schedule_name.setter
    def simple_airflow_control_type_schedule_name(self, value=None):
        """  Corresponds to IDD Field `simple_airflow_control_type_schedule_name`
        The schedule is used to incorporate operation of simple airflow objects and HVAC
        system operation.
        The simple airflow objects are Ventilation and Mixing only

        Args:
            value (str): value for IDD Field `simple_airflow_control_type_schedule_name`
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
                                 'for field `simple_airflow_control_type_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_airflow_control_type_schedule_name`')

        self._data["Simple Airflow Control Type Schedule Name"] = value

    @property
    def zoneventilation_object_name(self):
        """Get zoneventilation_object_name

        Returns:
            str: the value of `zoneventilation_object_name` or None if not set
        """
        return self._data["ZoneVentilation Object Name"]

    @zoneventilation_object_name.setter
    def zoneventilation_object_name(self, value=None):
        """  Corresponds to IDD Field `zoneventilation_object_name`
        This fieldhas not been instrumented to work with
        global Zone or Zone List names option for Ventilation:DesignFlowRate.  In order to
        use, you must enter the single <Ventilation:DesignFlowRate> name in this field.
        If it is a part of a global ventilation assignement the name will be
        <Zone Name> <global Ventilation:DesignFlowRate> name.
        The other ZoneVentilation:* and ZoneMixing objects controlled in the same AirLoopHVAC
        will work in the same way as this ventilation object.

        Args:
            value (str): value for IDD Field `zoneventilation_object_name`
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
                                 'for field `zoneventilation_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zoneventilation_object_name`')

        self._data["ZoneVentilation Object Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.hvac_air_loop_name))
        out.append(self._to_str(self.controlled_zone_name))
        out.append(self._to_str(self.ventilation_control_mode_schedule_name))
        out.append(self._to_str(self.use_weather_file_rain_indicators))
        out.append(self._to_str(self.maximum_wind_speed))
        out.append(self._to_str(self.minimum_outdoor_temperature))
        out.append(self._to_str(self.maximum_outdoor_temperature))
        out.append(self._to_str(self.minimum_outdoor_enthalpy))
        out.append(self._to_str(self.maximum_outdoor_enthalpy))
        out.append(self._to_str(self.minimum_outdoor_dewpoint))
        out.append(self._to_str(self.maximum_outdoor_dewpoint))
        out.append(self._to_str(self.minimum_outdoor_ventilation_air_schedule_name))
        out.append(self._to_str(self.opening_factor_function_of_wind_speed_curve_name))
        out.append(self._to_str(self.airflownetwork_control_type_schedule_name))
        out.append(self._to_str(self.simple_airflow_control_type_schedule_name))
        out.append(self._to_str(self.zoneventilation_object_name))
        return ",".join(out)

class AvailabilityManagerAssignmentList(object):
    """ Corresponds to IDD object `AvailabilityManagerAssignmentList`
        Defines the applicable managers used for an AirLoopHVAC or PlantLoop. The priority of
        availability managers is based on a set of rules and are specific to the type of loop.
        The output from each availability manager is an availability status flag:
        NoAction, ForceOff, CycleOn, or CycleOnZoneFansOnly (used only for air loops).
    
    """
    internal_name = "AvailabilityManagerAssignmentList"
    field_count = 13
    required_fields = ["Name", "Availability Manager 1 Object Type", "Availability Manager 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AvailabilityManagerAssignmentList`
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