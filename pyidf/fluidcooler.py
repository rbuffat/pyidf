from collections import OrderedDict

class FluidCoolerSingleSpeed(object):
    """ Corresponds to IDD object `FluidCooler:SingleSpeed`
        The fluid cooler is modeled as a cross flow heat exchanger (both streams unmixed) with
        single-speed fans (induced draft configuration).
    """
    internal_name = "FluidCooler:SingleSpeed"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `FluidCooler:SingleSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Performance Input Method"] = None
        self._data["Design Air Flow Rate U-factor Times Area Value"] = None
        self._data["Nominal Capacity"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wetbulb Temperature"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Air Flow Rate Fan Power"] = None
        self._data["Outdoor Air Inlet Node Name"] = None

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
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_air_flow_rate_ufactor_times_area_value = None
        else:
            self.design_air_flow_rate_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_entering_water_temperature = None
        else:
            self.design_entering_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_entering_air_temperature = None
        else:
            self.design_entering_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_entering_air_wetbulb_temperature = None
        else:
            self.design_entering_air_wetbulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_air_flow_rate = None
        else:
            self.design_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_air_flow_rate_fan_power = None
        else:
            self.design_air_flow_rate_fan_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
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
        fluid cooler name

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
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `water_inlet_node_name`
        Name of fluid cooler water inlet node

        Args:
            value (str): value for IDD Field `water_inlet_node_name`
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
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')

        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `water_outlet_node_name`
        Name of fluid cooler water outlet node

        Args:
            value (str): value for IDD Field `water_outlet_node_name`
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
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')

        self._data["Water Outlet Node Name"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=NominalCapacity ):
        """  Corresponds to IDD Field `performance_input_method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler nominal capacity

        Args:
            value (str): value for IDD Field `performance_input_method`
                Default value: NominalCapacity
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
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')

        self._data["Performance Input Method"] = value

    @property
    def design_air_flow_rate_ufactor_times_area_value(self):
        """Get design_air_flow_rate_ufactor_times_area_value

        Returns:
            float: the value of `design_air_flow_rate_ufactor_times_area_value` or None if not set
        """
        return self._data["Design Air Flow Rate U-factor Times Area Value"]

    @design_air_flow_rate_ufactor_times_area_value.setter
    def design_air_flow_rate_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `design_air_flow_rate_ufactor_times_area_value`
        Leave field blank if fluid cooler Performance Input Method is NominalCapacity

        Args:
            value (float): value for IDD Field `design_air_flow_rate_ufactor_times_area_value`
                Unit: W/K
                value > 0.0
                value <= 2100000.0
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
                                 'for field `design_air_flow_rate_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`')

        self._data["Design Air Flow Rate U-factor Times Area Value"] = value

    @property
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`
        Nominal fluid cooler capacity

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def design_entering_water_temperature(self):
        """Get design_entering_water_temperature

        Returns:
            float: the value of `design_entering_water_temperature` or None if not set
        """
        return self._data["Design Entering Water Temperature"]

    @design_entering_water_temperature.setter
    def design_entering_water_temperature(self, value=None):
        """  Corresponds to IDD Field `design_entering_water_temperature`
        Design Entering Water Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `design_entering_water_temperature`
                Unit: C
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
                                 'for field `design_entering_water_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_water_temperature`')

        self._data["Design Entering Water Temperature"] = value

    @property
    def design_entering_air_temperature(self):
        """Get design_entering_air_temperature

        Returns:
            float: the value of `design_entering_air_temperature` or None if not set
        """
        return self._data["Design Entering Air Temperature"]

    @design_entering_air_temperature.setter
    def design_entering_air_temperature(self, value=None):
        """  Corresponds to IDD Field `design_entering_air_temperature`
        Design Entering Air Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Wet-bulb Temperature.

        Args:
            value (float): value for IDD Field `design_entering_air_temperature`
                Unit: C
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
                                 'for field `design_entering_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_temperature`')

        self._data["Design Entering Air Temperature"] = value

    @property
    def design_entering_air_wetbulb_temperature(self):
        """Get design_entering_air_wetbulb_temperature

        Returns:
            float: the value of `design_entering_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Entering Air Wetbulb Temperature"]

    @design_entering_air_wetbulb_temperature.setter
    def design_entering_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `design_entering_air_wetbulb_temperature`
        Design Entering Air Wet-bulb Temperature must be specified for both the performance input methods and
        its value must be less than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `design_entering_air_wetbulb_temperature`
                Unit: C
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
                                 'for field `design_entering_air_wetbulb_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_wetbulb_temperature`')

        self._data["Design Entering Air Wetbulb Temperature"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_water_flow_rate`

        Args:
            value (float): value for IDD Field `design_water_flow_rate`
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
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')

        self._data["Design Water Flow Rate"] = value

    @property
    def design_air_flow_rate(self):
        """Get design_air_flow_rate

        Returns:
            float: the value of `design_air_flow_rate` or None if not set
        """
        return self._data["Design Air Flow Rate"]

    @design_air_flow_rate.setter
    def design_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_air_flow_rate`

        Args:
            value (float): value for IDD Field `design_air_flow_rate`
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
                                 'for field `design_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate`')

        self._data["Design Air Flow Rate"] = value

    @property
    def design_air_flow_rate_fan_power(self):
        """Get design_air_flow_rate_fan_power

        Returns:
            float: the value of `design_air_flow_rate_fan_power` or None if not set
        """
        return self._data["Design Air Flow Rate Fan Power"]

    @design_air_flow_rate_fan_power.setter
    def design_air_flow_rate_fan_power(self, value=None):
        """  Corresponds to IDD Field `design_air_flow_rate_fan_power`
        This is the fan motor electric input power

        Args:
            value (float): value for IDD Field `design_air_flow_rate_fan_power`
                Unit: W
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
                                 'for field `design_air_flow_rate_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate_fan_power`')

        self._data["Design Air Flow Rate Fan Power"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_inlet_node_name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `outdoor_air_inlet_node_name`
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
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')

        self._data["Outdoor Air Inlet Node Name"] = value

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
        out.append(self._to_str(self.water_inlet_node_name))
        out.append(self._to_str(self.water_outlet_node_name))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.design_air_flow_rate_ufactor_times_area_value))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.design_entering_water_temperature))
        out.append(self._to_str(self.design_entering_air_temperature))
        out.append(self._to_str(self.design_entering_air_wetbulb_temperature))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.design_air_flow_rate))
        out.append(self._to_str(self.design_air_flow_rate_fan_power))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        return ",".join(out)

class FluidCoolerTwoSpeed(object):
    """ Corresponds to IDD object `FluidCooler:TwoSpeed`
        The fluid cooler is modeled as a cross flow heat exchanger (both streams unmixed) with
        two-speed fans (induced draft configuration).
    """
    internal_name = "FluidCooler:TwoSpeed"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `FluidCooler:TwoSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Performance Input Method"] = None
        self._data["High Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = None
        self._data["High Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity Sizing Factor"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wet-bulb Temperature"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["High Fan Speed Air Flow Rate"] = None
        self._data["High Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Air Flow Rate"] = None
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = None
        self._data["Low Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Fan Power Sizing Factor"] = None
        self._data["Outdoor Air Inlet Node Name"] = None

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
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_fan_speed_ufactor_times_area_value = None
        else:
            self.high_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_value = None
        else:
            self.low_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_sizing_factor = None
        else:
            self.low_fan_speed_ufactor_times_area_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_speed_nominal_capacity = None
        else:
            self.high_speed_nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_speed_nominal_capacity = None
        else:
            self.low_speed_nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_speed_nominal_capacity_sizing_factor = None
        else:
            self.low_speed_nominal_capacity_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_entering_water_temperature = None
        else:
            self.design_entering_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_entering_air_temperature = None
        else:
            self.design_entering_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_entering_air_wetbulb_temperature = None
        else:
            self.design_entering_air_wetbulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_fan_speed_air_flow_rate = None
        else:
            self.high_fan_speed_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_fan_speed_fan_power = None
        else:
            self.high_fan_speed_fan_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate = None
        else:
            self.low_fan_speed_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate_sizing_factor = None
        else:
            self.low_fan_speed_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power = None
        else:
            self.low_fan_speed_fan_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power_sizing_factor = None
        else:
            self.low_fan_speed_fan_power_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
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
        fluid cooler name

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
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `water_inlet_node_name`
        Name of fluid cooler water inlet node

        Args:
            value (str): value for IDD Field `water_inlet_node_name`
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
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')

        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `water_outlet_node_name`
        Name of fluid cooler water outlet node

        Args:
            value (str): value for IDD Field `water_outlet_node_name`
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
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')

        self._data["Water Outlet Node Name"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=NominalCapacity ):
        """  Corresponds to IDD Field `performance_input_method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler nominal capacity

        Args:
            value (str): value for IDD Field `performance_input_method`
                Default value: NominalCapacity
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
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')

        self._data["Performance Input Method"] = value

    @property
    def high_fan_speed_ufactor_times_area_value(self):
        """Get high_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `high_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["High Fan Speed U-factor Times Area Value"]

    @high_fan_speed_ufactor_times_area_value.setter
    def high_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `high_fan_speed_ufactor_times_area_value`
        Leave field blank if fluid cooler Performance Input Method is NominalCapacity

        Args:
            value (float): value for IDD Field `high_fan_speed_ufactor_times_area_value`
                Unit: W/K
                value > 0.0
                value <= 2100000.0
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
                                 'for field `high_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')

        self._data["High Fan Speed U-factor Times Area Value"] = value

    @property
    def low_fan_speed_ufactor_times_area_value(self):
        """Get low_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["Low Fan Speed U-factor Times Area Value"]

    @low_fan_speed_ufactor_times_area_value.setter
    def low_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `low_fan_speed_ufactor_times_area_value`
        Leave field blank if fluid cooler Performance Input Method is NominalCapacity
        Low speed fluid cooler UA must be less than high speed fluid cooler UA
        Low speed fluid cooler UA must be greater than free convection fluid cooler UA

        Args:
            value (float): value for IDD Field `low_fan_speed_ufactor_times_area_value`
                Unit: W/K
                value > 0.0
                value <= 300000.0
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
                                 'for field `low_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')

        self._data["Low Fan Speed U-factor Times Area Value"] = value

    @property
    def low_fan_speed_ufactor_times_area_sizing_factor(self):
        """Get low_fan_speed_ufactor_times_area_sizing_factor

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed U-Factor Times Area Sizing Factor"]

    @low_fan_speed_ufactor_times_area_sizing_factor.setter
    def low_fan_speed_ufactor_times_area_sizing_factor(self, value=0.6 ):
        """  Corresponds to IDD Field `low_fan_speed_ufactor_times_area_sizing_factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `low_fan_speed_ufactor_times_area_sizing_factor`
                Default value: 0.6
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
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`'.format(value))

        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = value

    @property
    def high_speed_nominal_capacity(self):
        """Get high_speed_nominal_capacity

        Returns:
            float: the value of `high_speed_nominal_capacity` or None if not set
        """
        return self._data["High Speed Nominal Capacity"]

    @high_speed_nominal_capacity.setter
    def high_speed_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `high_speed_nominal_capacity`
        Nominal fluid cooler capacity at high fan speed

        Args:
            value (float): value for IDD Field `high_speed_nominal_capacity`
                Unit: W
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
                                 'for field `high_speed_nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_nominal_capacity`')

        self._data["High Speed Nominal Capacity"] = value

    @property
    def low_speed_nominal_capacity(self):
        """Get low_speed_nominal_capacity

        Returns:
            float: the value of `low_speed_nominal_capacity` or None if not set
        """
        return self._data["Low Speed Nominal Capacity"]

    @low_speed_nominal_capacity.setter
    def low_speed_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `low_speed_nominal_capacity`
        Nominal fluid cooler capacity at low fan speed

        Args:
            value (float): value for IDD Field `low_speed_nominal_capacity`
                Unit: W
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
                                 'for field `low_speed_nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_nominal_capacity`')

        self._data["Low Speed Nominal Capacity"] = value

    @property
    def low_speed_nominal_capacity_sizing_factor(self):
        """Get low_speed_nominal_capacity_sizing_factor

        Returns:
            float: the value of `low_speed_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Low Speed Nominal Capacity Sizing Factor"]

    @low_speed_nominal_capacity_sizing_factor.setter
    def low_speed_nominal_capacity_sizing_factor(self, value=0.5 ):
        """  Corresponds to IDD Field `low_speed_nominal_capacity_sizing_factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is NominalCapacity

        Args:
            value (float): value for IDD Field `low_speed_nominal_capacity_sizing_factor`
                Default value: 0.5
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
                                 'for field `low_speed_nominal_capacity_sizing_factor`'.format(value))

        self._data["Low Speed Nominal Capacity Sizing Factor"] = value

    @property
    def design_entering_water_temperature(self):
        """Get design_entering_water_temperature

        Returns:
            float: the value of `design_entering_water_temperature` or None if not set
        """
        return self._data["Design Entering Water Temperature"]

    @design_entering_water_temperature.setter
    def design_entering_water_temperature(self, value=None):
        """  Corresponds to IDD Field `design_entering_water_temperature`
        Design Entering Water Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `design_entering_water_temperature`
                Unit: C
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
                                 'for field `design_entering_water_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_water_temperature`')

        self._data["Design Entering Water Temperature"] = value

    @property
    def design_entering_air_temperature(self):
        """Get design_entering_air_temperature

        Returns:
            float: the value of `design_entering_air_temperature` or None if not set
        """
        return self._data["Design Entering Air Temperature"]

    @design_entering_air_temperature.setter
    def design_entering_air_temperature(self, value=None):
        """  Corresponds to IDD Field `design_entering_air_temperature`
        Design Entering Air Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Wet-bulb Temperature.

        Args:
            value (float): value for IDD Field `design_entering_air_temperature`
                Unit: C
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
                                 'for field `design_entering_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_temperature`')

        self._data["Design Entering Air Temperature"] = value

    @property
    def design_entering_air_wetbulb_temperature(self):
        """Get design_entering_air_wetbulb_temperature

        Returns:
            float: the value of `design_entering_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Entering Air Wet-bulb Temperature"]

    @design_entering_air_wetbulb_temperature.setter
    def design_entering_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `design_entering_air_wetbulb_temperature`
        Design Entering Air Wet-bulb Temperature must be specified for both the performance input methods and
        its value must be less than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `design_entering_air_wetbulb_temperature`
                Unit: C
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
                                 'for field `design_entering_air_wetbulb_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_wetbulb_temperature`')

        self._data["Design Entering Air Wet-bulb Temperature"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_water_flow_rate`

        Args:
            value (float): value for IDD Field `design_water_flow_rate`
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
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')

        self._data["Design Water Flow Rate"] = value

    @property
    def high_fan_speed_air_flow_rate(self):
        """Get high_fan_speed_air_flow_rate

        Returns:
            float: the value of `high_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["High Fan Speed Air Flow Rate"]

    @high_fan_speed_air_flow_rate.setter
    def high_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `high_fan_speed_air_flow_rate`
        Air Flow Rate at High Fan Speed must be greater than Air Flow Rate at Low Fan Speed

        Args:
            value (float): value for IDD Field `high_fan_speed_air_flow_rate`
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
                                 'for field `high_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_air_flow_rate`')

        self._data["High Fan Speed Air Flow Rate"] = value

    @property
    def high_fan_speed_fan_power(self):
        """Get high_fan_speed_fan_power

        Returns:
            float: the value of `high_fan_speed_fan_power` or None if not set
        """
        return self._data["High Fan Speed Fan Power"]

    @high_fan_speed_fan_power.setter
    def high_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `high_fan_speed_fan_power`
        This is the fan motor electric input power at high speed

        Args:
            value (float): value for IDD Field `high_fan_speed_fan_power`
                Unit: W
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
                                 'for field `high_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_fan_power`')

        self._data["High Fan Speed Fan Power"] = value

    @property
    def low_fan_speed_air_flow_rate(self):
        """Get low_fan_speed_air_flow_rate

        Returns:
            float: the value of `low_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate"]

    @low_fan_speed_air_flow_rate.setter
    def low_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `low_fan_speed_air_flow_rate`
        Air Flow Rate at Low Fan Speed must be less than Air Flow Rate at High Fan Speed

        Args:
            value (float): value for IDD Field `low_fan_speed_air_flow_rate`
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
                                 'for field `low_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_air_flow_rate`')

        self._data["Low Fan Speed Air Flow Rate"] = value

    @property
    def low_fan_speed_air_flow_rate_sizing_factor(self):
        """Get low_fan_speed_air_flow_rate_sizing_factor

        Returns:
            float: the value of `low_fan_speed_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate Sizing Factor"]

    @low_fan_speed_air_flow_rate_sizing_factor.setter
    def low_fan_speed_air_flow_rate_sizing_factor(self, value=0.5 ):
        """  Corresponds to IDD Field `low_fan_speed_air_flow_rate_sizing_factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `low_fan_speed_air_flow_rate_sizing_factor`
                Default value: 0.5
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
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`'.format(value))

        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = value

    @property
    def low_fan_speed_fan_power(self):
        """Get low_fan_speed_fan_power

        Returns:
            float: the value of `low_fan_speed_fan_power` or None if not set
        """
        return self._data["Low Fan Speed Fan Power"]

    @low_fan_speed_fan_power.setter
    def low_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `low_fan_speed_fan_power`
        This is the fan motor electric input power at low speed

        Args:
            value (float): value for IDD Field `low_fan_speed_fan_power`
                Unit: W
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
                                 'for field `low_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_fan_power`')

        self._data["Low Fan Speed Fan Power"] = value

    @property
    def low_fan_speed_fan_power_sizing_factor(self):
        """Get low_fan_speed_fan_power_sizing_factor

        Returns:
            float: the value of `low_fan_speed_fan_power_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Fan Power Sizing Factor"]

    @low_fan_speed_fan_power_sizing_factor.setter
    def low_fan_speed_fan_power_sizing_factor(self, value=0.16 ):
        """  Corresponds to IDD Field `low_fan_speed_fan_power_sizing_factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `low_fan_speed_fan_power_sizing_factor`
                Default value: 0.16
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
                                 'for field `low_fan_speed_fan_power_sizing_factor`'.format(value))

        self._data["Low Fan Speed Fan Power Sizing Factor"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `outdoor_air_inlet_node_name`
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
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')

        self._data["Outdoor Air Inlet Node Name"] = value

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
        out.append(self._to_str(self.water_inlet_node_name))
        out.append(self._to_str(self.water_outlet_node_name))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.high_fan_speed_ufactor_times_area_value))
        out.append(self._to_str(self.low_fan_speed_ufactor_times_area_value))
        out.append(self._to_str(self.low_fan_speed_ufactor_times_area_sizing_factor))
        out.append(self._to_str(self.high_speed_nominal_capacity))
        out.append(self._to_str(self.low_speed_nominal_capacity))
        out.append(self._to_str(self.low_speed_nominal_capacity_sizing_factor))
        out.append(self._to_str(self.design_entering_water_temperature))
        out.append(self._to_str(self.design_entering_air_temperature))
        out.append(self._to_str(self.design_entering_air_wetbulb_temperature))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.high_fan_speed_air_flow_rate))
        out.append(self._to_str(self.high_fan_speed_fan_power))
        out.append(self._to_str(self.low_fan_speed_air_flow_rate))
        out.append(self._to_str(self.low_fan_speed_air_flow_rate_sizing_factor))
        out.append(self._to_str(self.low_fan_speed_fan_power))
        out.append(self._to_str(self.low_fan_speed_fan_power_sizing_factor))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        return ",".join(out)