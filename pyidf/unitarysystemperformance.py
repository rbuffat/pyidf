from collections import OrderedDict

class UnitarySystemPerformanceHeatPumpMultispeed(object):
    """ Corresponds to IDD object `UnitarySystemPerformance:HeatPump:Multispeed`
        The UnitarySystemPerformance object is used to specify the air flow ratio at each
        operating speed. This object is primarily used for multispeed coils to allow operation
        at alternate flow rates different from those specified in the coil object.
    """
    internal_name = "UnitarySystemPerformance:HeatPump:Multispeed"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UnitarySystemPerformance:HeatPump:Multispeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Number of Speeds for Heating"] = None
        self._data["Number of Speeds for Cooling"] = None
        self._data["Speed 1 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 1 Supply Air Flow Ratio During Cooling Operation"] = None
        self._data["Speed 2 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 2 Supply Air Flow Ratio During Cooling Operation"] = None
        self._data["Speed 3 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 3 Supply Air Flow Ratio During Cooling Operation"] = None
        self._data["Speed 4 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 4 Supply Air Flow Ratio During Cooling Operation"] = None

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
            self.number_of_speeds_for_heating = None
        else:
            self.number_of_speeds_for_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_speeds_for_cooling = None
        else:
            self.number_of_speeds_for_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_1_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_1_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_1_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_1_supply_air_flow_ratio_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_2_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_2_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_2_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_2_supply_air_flow_ratio_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_3_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_3_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_3_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_3_supply_air_flow_ratio_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_4_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_4_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_4_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_4_supply_air_flow_ratio_during_cooling_operation = vals[i]
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
    def number_of_speeds_for_heating(self):
        """Get number_of_speeds_for_heating

        Returns:
            int: the value of `number_of_speeds_for_heating` or None if not set
        """
        return self._data["Number of Speeds for Heating"]

    @number_of_speeds_for_heating.setter
    def number_of_speeds_for_heating(self, value=None):
        """  Corresponds to IDD Field `number_of_speeds_for_heating`
        Used only for Multi speed coils
        Enter the number of the following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `number_of_speeds_for_heating`
                value >= 0
                value <= 10
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
                                 'for field `number_of_speeds_for_heating`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_speeds_for_heating`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `number_of_speeds_for_heating`')

        self._data["Number of Speeds for Heating"] = value

    @property
    def number_of_speeds_for_cooling(self):
        """Get number_of_speeds_for_cooling

        Returns:
            int: the value of `number_of_speeds_for_cooling` or None if not set
        """
        return self._data["Number of Speeds for Cooling"]

    @number_of_speeds_for_cooling.setter
    def number_of_speeds_for_cooling(self, value=None):
        """  Corresponds to IDD Field `number_of_speeds_for_cooling`
        Used only for Multi speed coils
        Enter the number of the following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `number_of_speeds_for_cooling`
                value >= 0
                value <= 10
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
                                 'for field `number_of_speeds_for_cooling`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_speeds_for_cooling`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `number_of_speeds_for_cooling`')

        self._data["Number of Speeds for Cooling"] = value

    @property
    def speed_1_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_1_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_1_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 1 Supply Air Flow Ratio During Heating Operation"]

    @speed_1_supply_air_flow_ratio_during_heating_operation.setter
    def speed_1_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_1_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_1_supply_air_flow_ratio_during_heating_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_1_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_1_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 1 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_1_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_1_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_1_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 1 Supply Air Flow Ratio During Cooling Operation"]

    @speed_1_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_1_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_1_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_1_supply_air_flow_ratio_during_cooling_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_1_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_1_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 1 Supply Air Flow Ratio During Cooling Operation"] = value

    @property
    def speed_2_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_2_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_2_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 2 Supply Air Flow Ratio During Heating Operation"]

    @speed_2_supply_air_flow_ratio_during_heating_operation.setter
    def speed_2_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_2_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the next highest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_2_supply_air_flow_ratio_during_heating_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_2_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_2_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 2 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_2_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_2_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_2_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 2 Supply Air Flow Ratio During Cooling Operation"]

    @speed_2_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_2_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_2_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_2_supply_air_flow_ratio_during_cooling_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_2_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_2_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 2 Supply Air Flow Ratio During Cooling Operation"] = value

    @property
    def speed_3_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_3_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_3_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 3 Supply Air Flow Ratio During Heating Operation"]

    @speed_3_supply_air_flow_ratio_during_heating_operation.setter
    def speed_3_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_3_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the next highest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_3_supply_air_flow_ratio_during_heating_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_3_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_3_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 3 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_3_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_3_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_3_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 3 Supply Air Flow Ratio During Cooling Operation"]

    @speed_3_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_3_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_3_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_3_supply_air_flow_ratio_during_cooling_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_3_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_3_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 3 Supply Air Flow Ratio During Cooling Operation"] = value

    @property
    def speed_4_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_4_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_4_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 4 Supply Air Flow Ratio During Heating Operation"]

    @speed_4_supply_air_flow_ratio_during_heating_operation.setter
    def speed_4_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_4_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the next highest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_4_supply_air_flow_ratio_during_heating_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_4_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_4_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 4 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_4_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_4_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_4_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 4 Supply Air Flow Ratio During Cooling Operation"]

    @speed_4_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_4_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_4_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_4_supply_air_flow_ratio_during_cooling_operation`
                Unit: m3/s
                value > 0.0
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
                                 'for field `speed_4_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_4_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 4 Supply Air Flow Ratio During Cooling Operation"] = value

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
        out.append(self._to_str(self.number_of_speeds_for_heating))
        out.append(self._to_str(self.number_of_speeds_for_cooling))
        out.append(self._to_str(self.speed_1_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_1_supply_air_flow_ratio_during_cooling_operation))
        out.append(self._to_str(self.speed_2_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_2_supply_air_flow_ratio_during_cooling_operation))
        out.append(self._to_str(self.speed_3_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_3_supply_air_flow_ratio_during_cooling_operation))
        out.append(self._to_str(self.speed_4_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_4_supply_air_flow_ratio_during_cooling_operation))
        return ",".join(out)