from collections import OrderedDict

class CoolingTowerPerformanceCoolTools(object):
    """ Corresponds to IDD object `CoolingTowerPerformance:CoolTools`
        This object is used to define coefficients for the approach temperature
        correlation for a variable speed cooling tower when tower Model Type is
        specified as CoolToolsUserDefined in the object CoolingTower:VariableSpeed.
    """
    internal_name = "CoolingTowerPerformance:CoolTools"
    field_count = 44

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoolingTowerPerformance:CoolTools`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Minimum Range Temperature"] = None
        self._data["Maximum Range Temperature"] = None
        self._data["Minimum Approach Temperature"] = None
        self._data["Maximum Approach Temperature"] = None
        self._data["Minimum Water Flow Rate Ratio"] = None
        self._data["Maximum Water Flow Rate Ratio"] = None
        self._data["Coefficient 1"] = None
        self._data["Coefficient 2"] = None
        self._data["Coefficient 3"] = None
        self._data["Coefficient 4"] = None
        self._data["Coefficient 5"] = None
        self._data["Coefficient 6"] = None
        self._data["Coefficient 7"] = None
        self._data["Coefficient 8"] = None
        self._data["Coefficient 9"] = None
        self._data["Coefficient 10"] = None
        self._data["Coefficient 11"] = None
        self._data["Coefficient 12"] = None
        self._data["Coefficient 13"] = None
        self._data["Coefficient 14"] = None
        self._data["Coefficient 15"] = None
        self._data["Coefficient 16"] = None
        self._data["Coefficient 17"] = None
        self._data["Coefficient 18"] = None
        self._data["Coefficient 19"] = None
        self._data["Coefficient 20"] = None
        self._data["Coefficient 21"] = None
        self._data["Coefficient 22"] = None
        self._data["Coefficient 23"] = None
        self._data["Coefficient 24"] = None
        self._data["Coefficient 25"] = None
        self._data["Coefficient 26"] = None
        self._data["Coefficient 27"] = None
        self._data["Coefficient 28"] = None
        self._data["Coefficient 29"] = None
        self._data["Coefficient 30"] = None
        self._data["Coefficient 31"] = None
        self._data["Coefficient 32"] = None
        self._data["Coefficient 33"] = None
        self._data["Coefficient 34"] = None
        self._data["Coefficient 35"] = None

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
            self.minimum_inlet_air_wetbulb_temperature = None
        else:
            self.minimum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_inlet_air_wetbulb_temperature = None
        else:
            self.maximum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_range_temperature = None
        else:
            self.minimum_range_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_range_temperature = None
        else:
            self.maximum_range_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_approach_temperature = None
        else:
            self.minimum_approach_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_approach_temperature = None
        else:
            self.maximum_approach_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_water_flow_rate_ratio = None
        else:
            self.minimum_water_flow_rate_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate_ratio = None
        else:
            self.maximum_water_flow_rate_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1 = None
        else:
            self.coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2 = None
        else:
            self.coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3 = None
        else:
            self.coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_4 = None
        else:
            self.coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_5 = None
        else:
            self.coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_6 = None
        else:
            self.coefficient_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_7 = None
        else:
            self.coefficient_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_8 = None
        else:
            self.coefficient_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_9 = None
        else:
            self.coefficient_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_10 = None
        else:
            self.coefficient_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_11 = None
        else:
            self.coefficient_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_12 = None
        else:
            self.coefficient_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_13 = None
        else:
            self.coefficient_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_14 = None
        else:
            self.coefficient_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_15 = None
        else:
            self.coefficient_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_16 = None
        else:
            self.coefficient_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_17 = None
        else:
            self.coefficient_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_18 = None
        else:
            self.coefficient_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_19 = None
        else:
            self.coefficient_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_20 = None
        else:
            self.coefficient_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_21 = None
        else:
            self.coefficient_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_22 = None
        else:
            self.coefficient_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_23 = None
        else:
            self.coefficient_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_24 = None
        else:
            self.coefficient_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_25 = None
        else:
            self.coefficient_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_26 = None
        else:
            self.coefficient_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_27 = None
        else:
            self.coefficient_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_28 = None
        else:
            self.coefficient_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_29 = None
        else:
            self.coefficient_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_30 = None
        else:
            self.coefficient_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_31 = None
        else:
            self.coefficient_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_32 = None
        else:
            self.coefficient_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_33 = None
        else:
            self.coefficient_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_34 = None
        else:
            self.coefficient_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_35 = None
        else:
            self.coefficient_35 = vals[i]
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
    def minimum_inlet_air_wetbulb_temperature(self):
        """Get minimum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `minimum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Minimum Inlet Air Wet-Bulb Temperature"]

    @minimum_inlet_air_wetbulb_temperature.setter
    def minimum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_inlet_air_wetbulb_temperature`
        Minimum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `minimum_inlet_air_wetbulb_temperature`
                Unit: C
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
                                 'for field `minimum_inlet_air_wetbulb_temperature`'.format(value))

        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def maximum_inlet_air_wetbulb_temperature(self):
        """Get maximum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `maximum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Maximum Inlet Air Wet-Bulb Temperature"]

    @maximum_inlet_air_wetbulb_temperature.setter
    def maximum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_inlet_air_wetbulb_temperature`
        Maximum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `maximum_inlet_air_wetbulb_temperature`
                Unit: C
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
                                 'for field `maximum_inlet_air_wetbulb_temperature`'.format(value))

        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def minimum_range_temperature(self):
        """Get minimum_range_temperature

        Returns:
            float: the value of `minimum_range_temperature` or None if not set
        """
        return self._data["Minimum Range Temperature"]

    @minimum_range_temperature.setter
    def minimum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_range_temperature`
        Minimum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `minimum_range_temperature`
                Unit: deltaC
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
                                 'for field `minimum_range_temperature`'.format(value))

        self._data["Minimum Range Temperature"] = value

    @property
    def maximum_range_temperature(self):
        """Get maximum_range_temperature

        Returns:
            float: the value of `maximum_range_temperature` or None if not set
        """
        return self._data["Maximum Range Temperature"]

    @maximum_range_temperature.setter
    def maximum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_range_temperature`
        Maximum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `maximum_range_temperature`
                Unit: deltaC
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
                                 'for field `maximum_range_temperature`'.format(value))

        self._data["Maximum Range Temperature"] = value

    @property
    def minimum_approach_temperature(self):
        """Get minimum_approach_temperature

        Returns:
            float: the value of `minimum_approach_temperature` or None if not set
        """
        return self._data["Minimum Approach Temperature"]

    @minimum_approach_temperature.setter
    def minimum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_approach_temperature`
        Minimum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `minimum_approach_temperature`
                Unit: deltaC
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
                                 'for field `minimum_approach_temperature`'.format(value))

        self._data["Minimum Approach Temperature"] = value

    @property
    def maximum_approach_temperature(self):
        """Get maximum_approach_temperature

        Returns:
            float: the value of `maximum_approach_temperature` or None if not set
        """
        return self._data["Maximum Approach Temperature"]

    @maximum_approach_temperature.setter
    def maximum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_approach_temperature`
        Maximum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `maximum_approach_temperature`
                Unit: deltaC
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
                                 'for field `maximum_approach_temperature`'.format(value))

        self._data["Maximum Approach Temperature"] = value

    @property
    def minimum_water_flow_rate_ratio(self):
        """Get minimum_water_flow_rate_ratio

        Returns:
            float: the value of `minimum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Water Flow Rate Ratio"]

    @minimum_water_flow_rate_ratio.setter
    def minimum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_water_flow_rate_ratio`
        Minimum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `minimum_water_flow_rate_ratio`
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
                                 'for field `minimum_water_flow_rate_ratio`'.format(value))

        self._data["Minimum Water Flow Rate Ratio"] = value

    @property
    def maximum_water_flow_rate_ratio(self):
        """Get maximum_water_flow_rate_ratio

        Returns:
            float: the value of `maximum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Maximum Water Flow Rate Ratio"]

    @maximum_water_flow_rate_ratio.setter
    def maximum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_water_flow_rate_ratio`
        Maximum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `maximum_water_flow_rate_ratio`
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
                                 'for field `maximum_water_flow_rate_ratio`'.format(value))

        self._data["Maximum Water Flow Rate Ratio"] = value

    @property
    def coefficient_1(self):
        """Get coefficient_1

        Returns:
            float: the value of `coefficient_1` or None if not set
        """
        return self._data["Coefficient 1"]

    @coefficient_1.setter
    def coefficient_1(self, value=None):
        """  Corresponds to IDD Field `coefficient_1`

        Args:
            value (float): value for IDD Field `coefficient_1`
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
                                 'for field `coefficient_1`'.format(value))

        self._data["Coefficient 1"] = value

    @property
    def coefficient_2(self):
        """Get coefficient_2

        Returns:
            float: the value of `coefficient_2` or None if not set
        """
        return self._data["Coefficient 2"]

    @coefficient_2.setter
    def coefficient_2(self, value=None):
        """  Corresponds to IDD Field `coefficient_2`

        Args:
            value (float): value for IDD Field `coefficient_2`
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
                                 'for field `coefficient_2`'.format(value))

        self._data["Coefficient 2"] = value

    @property
    def coefficient_3(self):
        """Get coefficient_3

        Returns:
            float: the value of `coefficient_3` or None if not set
        """
        return self._data["Coefficient 3"]

    @coefficient_3.setter
    def coefficient_3(self, value=None):
        """  Corresponds to IDD Field `coefficient_3`

        Args:
            value (float): value for IDD Field `coefficient_3`
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
                                 'for field `coefficient_3`'.format(value))

        self._data["Coefficient 3"] = value

    @property
    def coefficient_4(self):
        """Get coefficient_4

        Returns:
            float: the value of `coefficient_4` or None if not set
        """
        return self._data["Coefficient 4"]

    @coefficient_4.setter
    def coefficient_4(self, value=None):
        """  Corresponds to IDD Field `coefficient_4`

        Args:
            value (float): value for IDD Field `coefficient_4`
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
                                 'for field `coefficient_4`'.format(value))

        self._data["Coefficient 4"] = value

    @property
    def coefficient_5(self):
        """Get coefficient_5

        Returns:
            float: the value of `coefficient_5` or None if not set
        """
        return self._data["Coefficient 5"]

    @coefficient_5.setter
    def coefficient_5(self, value=None):
        """  Corresponds to IDD Field `coefficient_5`

        Args:
            value (float): value for IDD Field `coefficient_5`
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
                                 'for field `coefficient_5`'.format(value))

        self._data["Coefficient 5"] = value

    @property
    def coefficient_6(self):
        """Get coefficient_6

        Returns:
            float: the value of `coefficient_6` or None if not set
        """
        return self._data["Coefficient 6"]

    @coefficient_6.setter
    def coefficient_6(self, value=None):
        """  Corresponds to IDD Field `coefficient_6`

        Args:
            value (float): value for IDD Field `coefficient_6`
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
                                 'for field `coefficient_6`'.format(value))

        self._data["Coefficient 6"] = value

    @property
    def coefficient_7(self):
        """Get coefficient_7

        Returns:
            float: the value of `coefficient_7` or None if not set
        """
        return self._data["Coefficient 7"]

    @coefficient_7.setter
    def coefficient_7(self, value=None):
        """  Corresponds to IDD Field `coefficient_7`

        Args:
            value (float): value for IDD Field `coefficient_7`
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
                                 'for field `coefficient_7`'.format(value))

        self._data["Coefficient 7"] = value

    @property
    def coefficient_8(self):
        """Get coefficient_8

        Returns:
            float: the value of `coefficient_8` or None if not set
        """
        return self._data["Coefficient 8"]

    @coefficient_8.setter
    def coefficient_8(self, value=None):
        """  Corresponds to IDD Field `coefficient_8`

        Args:
            value (float): value for IDD Field `coefficient_8`
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
                                 'for field `coefficient_8`'.format(value))

        self._data["Coefficient 8"] = value

    @property
    def coefficient_9(self):
        """Get coefficient_9

        Returns:
            float: the value of `coefficient_9` or None if not set
        """
        return self._data["Coefficient 9"]

    @coefficient_9.setter
    def coefficient_9(self, value=None):
        """  Corresponds to IDD Field `coefficient_9`

        Args:
            value (float): value for IDD Field `coefficient_9`
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
                                 'for field `coefficient_9`'.format(value))

        self._data["Coefficient 9"] = value

    @property
    def coefficient_10(self):
        """Get coefficient_10

        Returns:
            float: the value of `coefficient_10` or None if not set
        """
        return self._data["Coefficient 10"]

    @coefficient_10.setter
    def coefficient_10(self, value=None):
        """  Corresponds to IDD Field `coefficient_10`

        Args:
            value (float): value for IDD Field `coefficient_10`
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
                                 'for field `coefficient_10`'.format(value))

        self._data["Coefficient 10"] = value

    @property
    def coefficient_11(self):
        """Get coefficient_11

        Returns:
            float: the value of `coefficient_11` or None if not set
        """
        return self._data["Coefficient 11"]

    @coefficient_11.setter
    def coefficient_11(self, value=None):
        """  Corresponds to IDD Field `coefficient_11`

        Args:
            value (float): value for IDD Field `coefficient_11`
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
                                 'for field `coefficient_11`'.format(value))

        self._data["Coefficient 11"] = value

    @property
    def coefficient_12(self):
        """Get coefficient_12

        Returns:
            float: the value of `coefficient_12` or None if not set
        """
        return self._data["Coefficient 12"]

    @coefficient_12.setter
    def coefficient_12(self, value=None):
        """  Corresponds to IDD Field `coefficient_12`

        Args:
            value (float): value for IDD Field `coefficient_12`
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
                                 'for field `coefficient_12`'.format(value))

        self._data["Coefficient 12"] = value

    @property
    def coefficient_13(self):
        """Get coefficient_13

        Returns:
            float: the value of `coefficient_13` or None if not set
        """
        return self._data["Coefficient 13"]

    @coefficient_13.setter
    def coefficient_13(self, value=None):
        """  Corresponds to IDD Field `coefficient_13`

        Args:
            value (float): value for IDD Field `coefficient_13`
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
                                 'for field `coefficient_13`'.format(value))

        self._data["Coefficient 13"] = value

    @property
    def coefficient_14(self):
        """Get coefficient_14

        Returns:
            float: the value of `coefficient_14` or None if not set
        """
        return self._data["Coefficient 14"]

    @coefficient_14.setter
    def coefficient_14(self, value=None):
        """  Corresponds to IDD Field `coefficient_14`

        Args:
            value (float): value for IDD Field `coefficient_14`
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
                                 'for field `coefficient_14`'.format(value))

        self._data["Coefficient 14"] = value

    @property
    def coefficient_15(self):
        """Get coefficient_15

        Returns:
            float: the value of `coefficient_15` or None if not set
        """
        return self._data["Coefficient 15"]

    @coefficient_15.setter
    def coefficient_15(self, value=None):
        """  Corresponds to IDD Field `coefficient_15`

        Args:
            value (float): value for IDD Field `coefficient_15`
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
                                 'for field `coefficient_15`'.format(value))

        self._data["Coefficient 15"] = value

    @property
    def coefficient_16(self):
        """Get coefficient_16

        Returns:
            float: the value of `coefficient_16` or None if not set
        """
        return self._data["Coefficient 16"]

    @coefficient_16.setter
    def coefficient_16(self, value=None):
        """  Corresponds to IDD Field `coefficient_16`

        Args:
            value (float): value for IDD Field `coefficient_16`
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
                                 'for field `coefficient_16`'.format(value))

        self._data["Coefficient 16"] = value

    @property
    def coefficient_17(self):
        """Get coefficient_17

        Returns:
            float: the value of `coefficient_17` or None if not set
        """
        return self._data["Coefficient 17"]

    @coefficient_17.setter
    def coefficient_17(self, value=None):
        """  Corresponds to IDD Field `coefficient_17`

        Args:
            value (float): value for IDD Field `coefficient_17`
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
                                 'for field `coefficient_17`'.format(value))

        self._data["Coefficient 17"] = value

    @property
    def coefficient_18(self):
        """Get coefficient_18

        Returns:
            float: the value of `coefficient_18` or None if not set
        """
        return self._data["Coefficient 18"]

    @coefficient_18.setter
    def coefficient_18(self, value=None):
        """  Corresponds to IDD Field `coefficient_18`

        Args:
            value (float): value for IDD Field `coefficient_18`
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
                                 'for field `coefficient_18`'.format(value))

        self._data["Coefficient 18"] = value

    @property
    def coefficient_19(self):
        """Get coefficient_19

        Returns:
            float: the value of `coefficient_19` or None if not set
        """
        return self._data["Coefficient 19"]

    @coefficient_19.setter
    def coefficient_19(self, value=None):
        """  Corresponds to IDD Field `coefficient_19`

        Args:
            value (float): value for IDD Field `coefficient_19`
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
                                 'for field `coefficient_19`'.format(value))

        self._data["Coefficient 19"] = value

    @property
    def coefficient_20(self):
        """Get coefficient_20

        Returns:
            float: the value of `coefficient_20` or None if not set
        """
        return self._data["Coefficient 20"]

    @coefficient_20.setter
    def coefficient_20(self, value=None):
        """  Corresponds to IDD Field `coefficient_20`

        Args:
            value (float): value for IDD Field `coefficient_20`
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
                                 'for field `coefficient_20`'.format(value))

        self._data["Coefficient 20"] = value

    @property
    def coefficient_21(self):
        """Get coefficient_21

        Returns:
            float: the value of `coefficient_21` or None if not set
        """
        return self._data["Coefficient 21"]

    @coefficient_21.setter
    def coefficient_21(self, value=None):
        """  Corresponds to IDD Field `coefficient_21`

        Args:
            value (float): value for IDD Field `coefficient_21`
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
                                 'for field `coefficient_21`'.format(value))

        self._data["Coefficient 21"] = value

    @property
    def coefficient_22(self):
        """Get coefficient_22

        Returns:
            float: the value of `coefficient_22` or None if not set
        """
        return self._data["Coefficient 22"]

    @coefficient_22.setter
    def coefficient_22(self, value=None):
        """  Corresponds to IDD Field `coefficient_22`

        Args:
            value (float): value for IDD Field `coefficient_22`
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
                                 'for field `coefficient_22`'.format(value))

        self._data["Coefficient 22"] = value

    @property
    def coefficient_23(self):
        """Get coefficient_23

        Returns:
            float: the value of `coefficient_23` or None if not set
        """
        return self._data["Coefficient 23"]

    @coefficient_23.setter
    def coefficient_23(self, value=None):
        """  Corresponds to IDD Field `coefficient_23`

        Args:
            value (float): value for IDD Field `coefficient_23`
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
                                 'for field `coefficient_23`'.format(value))

        self._data["Coefficient 23"] = value

    @property
    def coefficient_24(self):
        """Get coefficient_24

        Returns:
            float: the value of `coefficient_24` or None if not set
        """
        return self._data["Coefficient 24"]

    @coefficient_24.setter
    def coefficient_24(self, value=None):
        """  Corresponds to IDD Field `coefficient_24`

        Args:
            value (float): value for IDD Field `coefficient_24`
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
                                 'for field `coefficient_24`'.format(value))

        self._data["Coefficient 24"] = value

    @property
    def coefficient_25(self):
        """Get coefficient_25

        Returns:
            float: the value of `coefficient_25` or None if not set
        """
        return self._data["Coefficient 25"]

    @coefficient_25.setter
    def coefficient_25(self, value=None):
        """  Corresponds to IDD Field `coefficient_25`

        Args:
            value (float): value for IDD Field `coefficient_25`
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
                                 'for field `coefficient_25`'.format(value))

        self._data["Coefficient 25"] = value

    @property
    def coefficient_26(self):
        """Get coefficient_26

        Returns:
            float: the value of `coefficient_26` or None if not set
        """
        return self._data["Coefficient 26"]

    @coefficient_26.setter
    def coefficient_26(self, value=None):
        """  Corresponds to IDD Field `coefficient_26`

        Args:
            value (float): value for IDD Field `coefficient_26`
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
                                 'for field `coefficient_26`'.format(value))

        self._data["Coefficient 26"] = value

    @property
    def coefficient_27(self):
        """Get coefficient_27

        Returns:
            float: the value of `coefficient_27` or None if not set
        """
        return self._data["Coefficient 27"]

    @coefficient_27.setter
    def coefficient_27(self, value=None):
        """  Corresponds to IDD Field `coefficient_27`

        Args:
            value (float): value for IDD Field `coefficient_27`
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
                                 'for field `coefficient_27`'.format(value))

        self._data["Coefficient 27"] = value

    @property
    def coefficient_28(self):
        """Get coefficient_28

        Returns:
            float: the value of `coefficient_28` or None if not set
        """
        return self._data["Coefficient 28"]

    @coefficient_28.setter
    def coefficient_28(self, value=None):
        """  Corresponds to IDD Field `coefficient_28`

        Args:
            value (float): value for IDD Field `coefficient_28`
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
                                 'for field `coefficient_28`'.format(value))

        self._data["Coefficient 28"] = value

    @property
    def coefficient_29(self):
        """Get coefficient_29

        Returns:
            float: the value of `coefficient_29` or None if not set
        """
        return self._data["Coefficient 29"]

    @coefficient_29.setter
    def coefficient_29(self, value=None):
        """  Corresponds to IDD Field `coefficient_29`

        Args:
            value (float): value for IDD Field `coefficient_29`
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
                                 'for field `coefficient_29`'.format(value))

        self._data["Coefficient 29"] = value

    @property
    def coefficient_30(self):
        """Get coefficient_30

        Returns:
            float: the value of `coefficient_30` or None if not set
        """
        return self._data["Coefficient 30"]

    @coefficient_30.setter
    def coefficient_30(self, value=None):
        """  Corresponds to IDD Field `coefficient_30`

        Args:
            value (float): value for IDD Field `coefficient_30`
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
                                 'for field `coefficient_30`'.format(value))

        self._data["Coefficient 30"] = value

    @property
    def coefficient_31(self):
        """Get coefficient_31

        Returns:
            float: the value of `coefficient_31` or None if not set
        """
        return self._data["Coefficient 31"]

    @coefficient_31.setter
    def coefficient_31(self, value=None):
        """  Corresponds to IDD Field `coefficient_31`

        Args:
            value (float): value for IDD Field `coefficient_31`
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
                                 'for field `coefficient_31`'.format(value))

        self._data["Coefficient 31"] = value

    @property
    def coefficient_32(self):
        """Get coefficient_32

        Returns:
            float: the value of `coefficient_32` or None if not set
        """
        return self._data["Coefficient 32"]

    @coefficient_32.setter
    def coefficient_32(self, value=None):
        """  Corresponds to IDD Field `coefficient_32`

        Args:
            value (float): value for IDD Field `coefficient_32`
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
                                 'for field `coefficient_32`'.format(value))

        self._data["Coefficient 32"] = value

    @property
    def coefficient_33(self):
        """Get coefficient_33

        Returns:
            float: the value of `coefficient_33` or None if not set
        """
        return self._data["Coefficient 33"]

    @coefficient_33.setter
    def coefficient_33(self, value=None):
        """  Corresponds to IDD Field `coefficient_33`

        Args:
            value (float): value for IDD Field `coefficient_33`
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
                                 'for field `coefficient_33`'.format(value))

        self._data["Coefficient 33"] = value

    @property
    def coefficient_34(self):
        """Get coefficient_34

        Returns:
            float: the value of `coefficient_34` or None if not set
        """
        return self._data["Coefficient 34"]

    @coefficient_34.setter
    def coefficient_34(self, value=None):
        """  Corresponds to IDD Field `coefficient_34`

        Args:
            value (float): value for IDD Field `coefficient_34`
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
                                 'for field `coefficient_34`'.format(value))

        self._data["Coefficient 34"] = value

    @property
    def coefficient_35(self):
        """Get coefficient_35

        Returns:
            float: the value of `coefficient_35` or None if not set
        """
        return self._data["Coefficient 35"]

    @coefficient_35.setter
    def coefficient_35(self, value=None):
        """  Corresponds to IDD Field `coefficient_35`

        Args:
            value (float): value for IDD Field `coefficient_35`
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
                                 'for field `coefficient_35`'.format(value))

        self._data["Coefficient 35"] = value

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
        out.append(self._to_str(self.minimum_inlet_air_wetbulb_temperature))
        out.append(self._to_str(self.maximum_inlet_air_wetbulb_temperature))
        out.append(self._to_str(self.minimum_range_temperature))
        out.append(self._to_str(self.maximum_range_temperature))
        out.append(self._to_str(self.minimum_approach_temperature))
        out.append(self._to_str(self.maximum_approach_temperature))
        out.append(self._to_str(self.minimum_water_flow_rate_ratio))
        out.append(self._to_str(self.maximum_water_flow_rate_ratio))
        out.append(self._to_str(self.coefficient_1))
        out.append(self._to_str(self.coefficient_2))
        out.append(self._to_str(self.coefficient_3))
        out.append(self._to_str(self.coefficient_4))
        out.append(self._to_str(self.coefficient_5))
        out.append(self._to_str(self.coefficient_6))
        out.append(self._to_str(self.coefficient_7))
        out.append(self._to_str(self.coefficient_8))
        out.append(self._to_str(self.coefficient_9))
        out.append(self._to_str(self.coefficient_10))
        out.append(self._to_str(self.coefficient_11))
        out.append(self._to_str(self.coefficient_12))
        out.append(self._to_str(self.coefficient_13))
        out.append(self._to_str(self.coefficient_14))
        out.append(self._to_str(self.coefficient_15))
        out.append(self._to_str(self.coefficient_16))
        out.append(self._to_str(self.coefficient_17))
        out.append(self._to_str(self.coefficient_18))
        out.append(self._to_str(self.coefficient_19))
        out.append(self._to_str(self.coefficient_20))
        out.append(self._to_str(self.coefficient_21))
        out.append(self._to_str(self.coefficient_22))
        out.append(self._to_str(self.coefficient_23))
        out.append(self._to_str(self.coefficient_24))
        out.append(self._to_str(self.coefficient_25))
        out.append(self._to_str(self.coefficient_26))
        out.append(self._to_str(self.coefficient_27))
        out.append(self._to_str(self.coefficient_28))
        out.append(self._to_str(self.coefficient_29))
        out.append(self._to_str(self.coefficient_30))
        out.append(self._to_str(self.coefficient_31))
        out.append(self._to_str(self.coefficient_32))
        out.append(self._to_str(self.coefficient_33))
        out.append(self._to_str(self.coefficient_34))
        out.append(self._to_str(self.coefficient_35))
        return ",".join(out)

class CoolingTowerPerformanceYorkCalc(object):
    """ Corresponds to IDD object `CoolingTowerPerformance:YorkCalc`
        This object is used to define coefficients for the approach temperature
        correlation for a variable speed cooling tower when tower Model Type is
        specified as YorkCalcUserDefined in the object CoolingTower:VariableSpeed.
    """
    internal_name = "CoolingTowerPerformance:YorkCalc"
    field_count = 37

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoolingTowerPerformance:YorkCalc`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Minimum Range Temperature"] = None
        self._data["Maximum Range Temperature"] = None
        self._data["Minimum Approach Temperature"] = None
        self._data["Maximum Approach Temperature"] = None
        self._data["Minimum Water Flow Rate Ratio"] = None
        self._data["Maximum Water Flow Rate Ratio"] = None
        self._data["Maximum Liquid to Gas Ratio"] = None
        self._data["Coefficient 1"] = None
        self._data["Coefficient 2"] = None
        self._data["Coefficient 3"] = None
        self._data["Coefficient 4"] = None
        self._data["Coefficient 5"] = None
        self._data["Coefficient 6"] = None
        self._data["Coefficient 7"] = None
        self._data["Coefficient 8"] = None
        self._data["Coefficient 9"] = None
        self._data["Coefficient 10"] = None
        self._data["Coefficient 11"] = None
        self._data["Coefficient 12"] = None
        self._data["Coefficient 13"] = None
        self._data["Coefficient 14"] = None
        self._data["Coefficient 15"] = None
        self._data["Coefficient 16"] = None
        self._data["Coefficient 17"] = None
        self._data["Coefficient 18"] = None
        self._data["Coefficient 19"] = None
        self._data["Coefficient 20"] = None
        self._data["Coefficient 21"] = None
        self._data["Coefficient 22"] = None
        self._data["Coefficient 23"] = None
        self._data["Coefficient 24"] = None
        self._data["Coefficient 25"] = None
        self._data["Coefficient 26"] = None
        self._data["Coefficient 27"] = None

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
            self.minimum_inlet_air_wetbulb_temperature = None
        else:
            self.minimum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_inlet_air_wetbulb_temperature = None
        else:
            self.maximum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_range_temperature = None
        else:
            self.minimum_range_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_range_temperature = None
        else:
            self.maximum_range_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_approach_temperature = None
        else:
            self.minimum_approach_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_approach_temperature = None
        else:
            self.maximum_approach_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_water_flow_rate_ratio = None
        else:
            self.minimum_water_flow_rate_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate_ratio = None
        else:
            self.maximum_water_flow_rate_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_liquid_to_gas_ratio = None
        else:
            self.maximum_liquid_to_gas_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1 = None
        else:
            self.coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2 = None
        else:
            self.coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3 = None
        else:
            self.coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_4 = None
        else:
            self.coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_5 = None
        else:
            self.coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_6 = None
        else:
            self.coefficient_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_7 = None
        else:
            self.coefficient_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_8 = None
        else:
            self.coefficient_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_9 = None
        else:
            self.coefficient_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_10 = None
        else:
            self.coefficient_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_11 = None
        else:
            self.coefficient_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_12 = None
        else:
            self.coefficient_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_13 = None
        else:
            self.coefficient_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_14 = None
        else:
            self.coefficient_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_15 = None
        else:
            self.coefficient_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_16 = None
        else:
            self.coefficient_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_17 = None
        else:
            self.coefficient_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_18 = None
        else:
            self.coefficient_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_19 = None
        else:
            self.coefficient_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_20 = None
        else:
            self.coefficient_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_21 = None
        else:
            self.coefficient_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_22 = None
        else:
            self.coefficient_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_23 = None
        else:
            self.coefficient_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_24 = None
        else:
            self.coefficient_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_25 = None
        else:
            self.coefficient_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_26 = None
        else:
            self.coefficient_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_27 = None
        else:
            self.coefficient_27 = vals[i]
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
    def minimum_inlet_air_wetbulb_temperature(self):
        """Get minimum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `minimum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Minimum Inlet Air Wet-Bulb Temperature"]

    @minimum_inlet_air_wetbulb_temperature.setter
    def minimum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_inlet_air_wetbulb_temperature`
        Minimum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `minimum_inlet_air_wetbulb_temperature`
                Unit: C
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
                                 'for field `minimum_inlet_air_wetbulb_temperature`'.format(value))

        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def maximum_inlet_air_wetbulb_temperature(self):
        """Get maximum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `maximum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Maximum Inlet Air Wet-Bulb Temperature"]

    @maximum_inlet_air_wetbulb_temperature.setter
    def maximum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_inlet_air_wetbulb_temperature`
        Maximum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `maximum_inlet_air_wetbulb_temperature`
                Unit: C
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
                                 'for field `maximum_inlet_air_wetbulb_temperature`'.format(value))

        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def minimum_range_temperature(self):
        """Get minimum_range_temperature

        Returns:
            float: the value of `minimum_range_temperature` or None if not set
        """
        return self._data["Minimum Range Temperature"]

    @minimum_range_temperature.setter
    def minimum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_range_temperature`
        Minimum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `minimum_range_temperature`
                Unit: deltaC
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
                                 'for field `minimum_range_temperature`'.format(value))

        self._data["Minimum Range Temperature"] = value

    @property
    def maximum_range_temperature(self):
        """Get maximum_range_temperature

        Returns:
            float: the value of `maximum_range_temperature` or None if not set
        """
        return self._data["Maximum Range Temperature"]

    @maximum_range_temperature.setter
    def maximum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_range_temperature`
        Maximum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `maximum_range_temperature`
                Unit: deltaC
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
                                 'for field `maximum_range_temperature`'.format(value))

        self._data["Maximum Range Temperature"] = value

    @property
    def minimum_approach_temperature(self):
        """Get minimum_approach_temperature

        Returns:
            float: the value of `minimum_approach_temperature` or None if not set
        """
        return self._data["Minimum Approach Temperature"]

    @minimum_approach_temperature.setter
    def minimum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_approach_temperature`
        Minimum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `minimum_approach_temperature`
                Unit: deltaC
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
                                 'for field `minimum_approach_temperature`'.format(value))

        self._data["Minimum Approach Temperature"] = value

    @property
    def maximum_approach_temperature(self):
        """Get maximum_approach_temperature

        Returns:
            float: the value of `maximum_approach_temperature` or None if not set
        """
        return self._data["Maximum Approach Temperature"]

    @maximum_approach_temperature.setter
    def maximum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_approach_temperature`
        Maximum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `maximum_approach_temperature`
                Unit: deltaC
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
                                 'for field `maximum_approach_temperature`'.format(value))

        self._data["Maximum Approach Temperature"] = value

    @property
    def minimum_water_flow_rate_ratio(self):
        """Get minimum_water_flow_rate_ratio

        Returns:
            float: the value of `minimum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Water Flow Rate Ratio"]

    @minimum_water_flow_rate_ratio.setter
    def minimum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_water_flow_rate_ratio`
        Minimum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `minimum_water_flow_rate_ratio`
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
                                 'for field `minimum_water_flow_rate_ratio`'.format(value))

        self._data["Minimum Water Flow Rate Ratio"] = value

    @property
    def maximum_water_flow_rate_ratio(self):
        """Get maximum_water_flow_rate_ratio

        Returns:
            float: the value of `maximum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Maximum Water Flow Rate Ratio"]

    @maximum_water_flow_rate_ratio.setter
    def maximum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_water_flow_rate_ratio`
        Maximum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `maximum_water_flow_rate_ratio`
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
                                 'for field `maximum_water_flow_rate_ratio`'.format(value))

        self._data["Maximum Water Flow Rate Ratio"] = value

    @property
    def maximum_liquid_to_gas_ratio(self):
        """Get maximum_liquid_to_gas_ratio

        Returns:
            float: the value of `maximum_liquid_to_gas_ratio` or None if not set
        """
        return self._data["Maximum Liquid to Gas Ratio"]

    @maximum_liquid_to_gas_ratio.setter
    def maximum_liquid_to_gas_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_liquid_to_gas_ratio`
        Maximum liquid (water) to gas (air) ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `maximum_liquid_to_gas_ratio`
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
                                 'for field `maximum_liquid_to_gas_ratio`'.format(value))

        self._data["Maximum Liquid to Gas Ratio"] = value

    @property
    def coefficient_1(self):
        """Get coefficient_1

        Returns:
            float: the value of `coefficient_1` or None if not set
        """
        return self._data["Coefficient 1"]

    @coefficient_1.setter
    def coefficient_1(self, value=None):
        """  Corresponds to IDD Field `coefficient_1`

        Args:
            value (float): value for IDD Field `coefficient_1`
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
                                 'for field `coefficient_1`'.format(value))

        self._data["Coefficient 1"] = value

    @property
    def coefficient_2(self):
        """Get coefficient_2

        Returns:
            float: the value of `coefficient_2` or None if not set
        """
        return self._data["Coefficient 2"]

    @coefficient_2.setter
    def coefficient_2(self, value=None):
        """  Corresponds to IDD Field `coefficient_2`

        Args:
            value (float): value for IDD Field `coefficient_2`
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
                                 'for field `coefficient_2`'.format(value))

        self._data["Coefficient 2"] = value

    @property
    def coefficient_3(self):
        """Get coefficient_3

        Returns:
            float: the value of `coefficient_3` or None if not set
        """
        return self._data["Coefficient 3"]

    @coefficient_3.setter
    def coefficient_3(self, value=None):
        """  Corresponds to IDD Field `coefficient_3`

        Args:
            value (float): value for IDD Field `coefficient_3`
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
                                 'for field `coefficient_3`'.format(value))

        self._data["Coefficient 3"] = value

    @property
    def coefficient_4(self):
        """Get coefficient_4

        Returns:
            float: the value of `coefficient_4` or None if not set
        """
        return self._data["Coefficient 4"]

    @coefficient_4.setter
    def coefficient_4(self, value=None):
        """  Corresponds to IDD Field `coefficient_4`

        Args:
            value (float): value for IDD Field `coefficient_4`
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
                                 'for field `coefficient_4`'.format(value))

        self._data["Coefficient 4"] = value

    @property
    def coefficient_5(self):
        """Get coefficient_5

        Returns:
            float: the value of `coefficient_5` or None if not set
        """
        return self._data["Coefficient 5"]

    @coefficient_5.setter
    def coefficient_5(self, value=None):
        """  Corresponds to IDD Field `coefficient_5`

        Args:
            value (float): value for IDD Field `coefficient_5`
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
                                 'for field `coefficient_5`'.format(value))

        self._data["Coefficient 5"] = value

    @property
    def coefficient_6(self):
        """Get coefficient_6

        Returns:
            float: the value of `coefficient_6` or None if not set
        """
        return self._data["Coefficient 6"]

    @coefficient_6.setter
    def coefficient_6(self, value=None):
        """  Corresponds to IDD Field `coefficient_6`

        Args:
            value (float): value for IDD Field `coefficient_6`
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
                                 'for field `coefficient_6`'.format(value))

        self._data["Coefficient 6"] = value

    @property
    def coefficient_7(self):
        """Get coefficient_7

        Returns:
            float: the value of `coefficient_7` or None if not set
        """
        return self._data["Coefficient 7"]

    @coefficient_7.setter
    def coefficient_7(self, value=None):
        """  Corresponds to IDD Field `coefficient_7`

        Args:
            value (float): value for IDD Field `coefficient_7`
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
                                 'for field `coefficient_7`'.format(value))

        self._data["Coefficient 7"] = value

    @property
    def coefficient_8(self):
        """Get coefficient_8

        Returns:
            float: the value of `coefficient_8` or None if not set
        """
        return self._data["Coefficient 8"]

    @coefficient_8.setter
    def coefficient_8(self, value=None):
        """  Corresponds to IDD Field `coefficient_8`

        Args:
            value (float): value for IDD Field `coefficient_8`
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
                                 'for field `coefficient_8`'.format(value))

        self._data["Coefficient 8"] = value

    @property
    def coefficient_9(self):
        """Get coefficient_9

        Returns:
            float: the value of `coefficient_9` or None if not set
        """
        return self._data["Coefficient 9"]

    @coefficient_9.setter
    def coefficient_9(self, value=None):
        """  Corresponds to IDD Field `coefficient_9`

        Args:
            value (float): value for IDD Field `coefficient_9`
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
                                 'for field `coefficient_9`'.format(value))

        self._data["Coefficient 9"] = value

    @property
    def coefficient_10(self):
        """Get coefficient_10

        Returns:
            float: the value of `coefficient_10` or None if not set
        """
        return self._data["Coefficient 10"]

    @coefficient_10.setter
    def coefficient_10(self, value=None):
        """  Corresponds to IDD Field `coefficient_10`

        Args:
            value (float): value for IDD Field `coefficient_10`
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
                                 'for field `coefficient_10`'.format(value))

        self._data["Coefficient 10"] = value

    @property
    def coefficient_11(self):
        """Get coefficient_11

        Returns:
            float: the value of `coefficient_11` or None if not set
        """
        return self._data["Coefficient 11"]

    @coefficient_11.setter
    def coefficient_11(self, value=None):
        """  Corresponds to IDD Field `coefficient_11`

        Args:
            value (float): value for IDD Field `coefficient_11`
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
                                 'for field `coefficient_11`'.format(value))

        self._data["Coefficient 11"] = value

    @property
    def coefficient_12(self):
        """Get coefficient_12

        Returns:
            float: the value of `coefficient_12` or None if not set
        """
        return self._data["Coefficient 12"]

    @coefficient_12.setter
    def coefficient_12(self, value=None):
        """  Corresponds to IDD Field `coefficient_12`

        Args:
            value (float): value for IDD Field `coefficient_12`
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
                                 'for field `coefficient_12`'.format(value))

        self._data["Coefficient 12"] = value

    @property
    def coefficient_13(self):
        """Get coefficient_13

        Returns:
            float: the value of `coefficient_13` or None if not set
        """
        return self._data["Coefficient 13"]

    @coefficient_13.setter
    def coefficient_13(self, value=None):
        """  Corresponds to IDD Field `coefficient_13`

        Args:
            value (float): value for IDD Field `coefficient_13`
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
                                 'for field `coefficient_13`'.format(value))

        self._data["Coefficient 13"] = value

    @property
    def coefficient_14(self):
        """Get coefficient_14

        Returns:
            float: the value of `coefficient_14` or None if not set
        """
        return self._data["Coefficient 14"]

    @coefficient_14.setter
    def coefficient_14(self, value=None):
        """  Corresponds to IDD Field `coefficient_14`

        Args:
            value (float): value for IDD Field `coefficient_14`
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
                                 'for field `coefficient_14`'.format(value))

        self._data["Coefficient 14"] = value

    @property
    def coefficient_15(self):
        """Get coefficient_15

        Returns:
            float: the value of `coefficient_15` or None if not set
        """
        return self._data["Coefficient 15"]

    @coefficient_15.setter
    def coefficient_15(self, value=None):
        """  Corresponds to IDD Field `coefficient_15`

        Args:
            value (float): value for IDD Field `coefficient_15`
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
                                 'for field `coefficient_15`'.format(value))

        self._data["Coefficient 15"] = value

    @property
    def coefficient_16(self):
        """Get coefficient_16

        Returns:
            float: the value of `coefficient_16` or None if not set
        """
        return self._data["Coefficient 16"]

    @coefficient_16.setter
    def coefficient_16(self, value=None):
        """  Corresponds to IDD Field `coefficient_16`

        Args:
            value (float): value for IDD Field `coefficient_16`
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
                                 'for field `coefficient_16`'.format(value))

        self._data["Coefficient 16"] = value

    @property
    def coefficient_17(self):
        """Get coefficient_17

        Returns:
            float: the value of `coefficient_17` or None if not set
        """
        return self._data["Coefficient 17"]

    @coefficient_17.setter
    def coefficient_17(self, value=None):
        """  Corresponds to IDD Field `coefficient_17`

        Args:
            value (float): value for IDD Field `coefficient_17`
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
                                 'for field `coefficient_17`'.format(value))

        self._data["Coefficient 17"] = value

    @property
    def coefficient_18(self):
        """Get coefficient_18

        Returns:
            float: the value of `coefficient_18` or None if not set
        """
        return self._data["Coefficient 18"]

    @coefficient_18.setter
    def coefficient_18(self, value=None):
        """  Corresponds to IDD Field `coefficient_18`

        Args:
            value (float): value for IDD Field `coefficient_18`
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
                                 'for field `coefficient_18`'.format(value))

        self._data["Coefficient 18"] = value

    @property
    def coefficient_19(self):
        """Get coefficient_19

        Returns:
            float: the value of `coefficient_19` or None if not set
        """
        return self._data["Coefficient 19"]

    @coefficient_19.setter
    def coefficient_19(self, value=None):
        """  Corresponds to IDD Field `coefficient_19`

        Args:
            value (float): value for IDD Field `coefficient_19`
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
                                 'for field `coefficient_19`'.format(value))

        self._data["Coefficient 19"] = value

    @property
    def coefficient_20(self):
        """Get coefficient_20

        Returns:
            float: the value of `coefficient_20` or None if not set
        """
        return self._data["Coefficient 20"]

    @coefficient_20.setter
    def coefficient_20(self, value=None):
        """  Corresponds to IDD Field `coefficient_20`

        Args:
            value (float): value for IDD Field `coefficient_20`
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
                                 'for field `coefficient_20`'.format(value))

        self._data["Coefficient 20"] = value

    @property
    def coefficient_21(self):
        """Get coefficient_21

        Returns:
            float: the value of `coefficient_21` or None if not set
        """
        return self._data["Coefficient 21"]

    @coefficient_21.setter
    def coefficient_21(self, value=None):
        """  Corresponds to IDD Field `coefficient_21`

        Args:
            value (float): value for IDD Field `coefficient_21`
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
                                 'for field `coefficient_21`'.format(value))

        self._data["Coefficient 21"] = value

    @property
    def coefficient_22(self):
        """Get coefficient_22

        Returns:
            float: the value of `coefficient_22` or None if not set
        """
        return self._data["Coefficient 22"]

    @coefficient_22.setter
    def coefficient_22(self, value=None):
        """  Corresponds to IDD Field `coefficient_22`

        Args:
            value (float): value for IDD Field `coefficient_22`
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
                                 'for field `coefficient_22`'.format(value))

        self._data["Coefficient 22"] = value

    @property
    def coefficient_23(self):
        """Get coefficient_23

        Returns:
            float: the value of `coefficient_23` or None if not set
        """
        return self._data["Coefficient 23"]

    @coefficient_23.setter
    def coefficient_23(self, value=None):
        """  Corresponds to IDD Field `coefficient_23`

        Args:
            value (float): value for IDD Field `coefficient_23`
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
                                 'for field `coefficient_23`'.format(value))

        self._data["Coefficient 23"] = value

    @property
    def coefficient_24(self):
        """Get coefficient_24

        Returns:
            float: the value of `coefficient_24` or None if not set
        """
        return self._data["Coefficient 24"]

    @coefficient_24.setter
    def coefficient_24(self, value=None):
        """  Corresponds to IDD Field `coefficient_24`

        Args:
            value (float): value for IDD Field `coefficient_24`
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
                                 'for field `coefficient_24`'.format(value))

        self._data["Coefficient 24"] = value

    @property
    def coefficient_25(self):
        """Get coefficient_25

        Returns:
            float: the value of `coefficient_25` or None if not set
        """
        return self._data["Coefficient 25"]

    @coefficient_25.setter
    def coefficient_25(self, value=None):
        """  Corresponds to IDD Field `coefficient_25`

        Args:
            value (float): value for IDD Field `coefficient_25`
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
                                 'for field `coefficient_25`'.format(value))

        self._data["Coefficient 25"] = value

    @property
    def coefficient_26(self):
        """Get coefficient_26

        Returns:
            float: the value of `coefficient_26` or None if not set
        """
        return self._data["Coefficient 26"]

    @coefficient_26.setter
    def coefficient_26(self, value=None):
        """  Corresponds to IDD Field `coefficient_26`

        Args:
            value (float): value for IDD Field `coefficient_26`
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
                                 'for field `coefficient_26`'.format(value))

        self._data["Coefficient 26"] = value

    @property
    def coefficient_27(self):
        """Get coefficient_27

        Returns:
            float: the value of `coefficient_27` or None if not set
        """
        return self._data["Coefficient 27"]

    @coefficient_27.setter
    def coefficient_27(self, value=None):
        """  Corresponds to IDD Field `coefficient_27`

        Args:
            value (float): value for IDD Field `coefficient_27`
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
                                 'for field `coefficient_27`'.format(value))

        self._data["Coefficient 27"] = value

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
        out.append(self._to_str(self.minimum_inlet_air_wetbulb_temperature))
        out.append(self._to_str(self.maximum_inlet_air_wetbulb_temperature))
        out.append(self._to_str(self.minimum_range_temperature))
        out.append(self._to_str(self.maximum_range_temperature))
        out.append(self._to_str(self.minimum_approach_temperature))
        out.append(self._to_str(self.maximum_approach_temperature))
        out.append(self._to_str(self.minimum_water_flow_rate_ratio))
        out.append(self._to_str(self.maximum_water_flow_rate_ratio))
        out.append(self._to_str(self.maximum_liquid_to_gas_ratio))
        out.append(self._to_str(self.coefficient_1))
        out.append(self._to_str(self.coefficient_2))
        out.append(self._to_str(self.coefficient_3))
        out.append(self._to_str(self.coefficient_4))
        out.append(self._to_str(self.coefficient_5))
        out.append(self._to_str(self.coefficient_6))
        out.append(self._to_str(self.coefficient_7))
        out.append(self._to_str(self.coefficient_8))
        out.append(self._to_str(self.coefficient_9))
        out.append(self._to_str(self.coefficient_10))
        out.append(self._to_str(self.coefficient_11))
        out.append(self._to_str(self.coefficient_12))
        out.append(self._to_str(self.coefficient_13))
        out.append(self._to_str(self.coefficient_14))
        out.append(self._to_str(self.coefficient_15))
        out.append(self._to_str(self.coefficient_16))
        out.append(self._to_str(self.coefficient_17))
        out.append(self._to_str(self.coefficient_18))
        out.append(self._to_str(self.coefficient_19))
        out.append(self._to_str(self.coefficient_20))
        out.append(self._to_str(self.coefficient_21))
        out.append(self._to_str(self.coefficient_22))
        out.append(self._to_str(self.coefficient_23))
        out.append(self._to_str(self.coefficient_24))
        out.append(self._to_str(self.coefficient_25))
        out.append(self._to_str(self.coefficient_26))
        out.append(self._to_str(self.coefficient_27))
        return ",".join(out)