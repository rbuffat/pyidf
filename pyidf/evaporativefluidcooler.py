from collections import OrderedDict

class EvaporativeFluidCoolerSingleSpeed(object):
    """ Corresponds to IDD object `EvaporativeFluidCooler:SingleSpeed`
        This model is based on Merkel's theory, which is also the basis
        for the cooling tower model in EnergyPlus. The Evaporative fluid cooler
        is modeled as a counter flow heat exchanger.
    """
    internal_name = "EvaporativeFluidCooler:SingleSpeed"
    field_count = 25

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EvaporativeFluidCooler:SingleSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Air Flow Rate Fan Power"] = None
        self._data["Design Spray Water Flow Rate"] = None
        self._data["Performance Input Method"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["Standard Design Capacity"] = None
        self._data["Design Air Flow Rate U-factor Times Area Value"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["User Specified Design Capacity"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wet-bulb Temperature"] = None
        self._data["Capacity Control"] = None
        self._data["Sizing Factor"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None

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
            self.design_spray_water_flow_rate = None
        else:
            self.design_spray_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.standard_design_capacity = None
        else:
            self.standard_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_air_flow_rate_ufactor_times_area_value = None
        else:
            self.design_air_flow_rate_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.user_specified_design_capacity = None
        else:
            self.user_specified_design_capacity = vals[i]
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
            self.capacity_control = None
        else:
            self.capacity_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
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
        Fluid Cooler Name

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
        Name of Fluid Cooler water inlet node

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
        Name of Fluid Cooler water outlet node

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
    def design_spray_water_flow_rate(self):
        """Get design_spray_water_flow_rate

        Returns:
            float: the value of `design_spray_water_flow_rate` or None if not set
        """
        return self._data["Design Spray Water Flow Rate"]

    @design_spray_water_flow_rate.setter
    def design_spray_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_spray_water_flow_rate`

        Args:
            value (float): value for IDD Field `design_spray_water_flow_rate`
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
                                 'for field `design_spray_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_spray_water_flow_rate`')

        self._data["Design Spray Water Flow Rate"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=None):
        """  Corresponds to IDD Field `performance_input_method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler Standard Design
        Capacity or by specifying Design Capacity for Non standard conditions.

        Args:
            value (str): value for IDD Field `performance_input_method`
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

    @property
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self):
        """Get heat_rejection_capacity_and_nominal_capacity_sizing_ratio

        Returns:
            float: the value of `heat_rejection_capacity_and_nominal_capacity_sizing_ratio` or None if not set
        """
        return self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    @heat_rejection_capacity_and_nominal_capacity_sizing_ratio.setter
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self, value=1.25 ):
        """  Corresponds to IDD Field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`

        Args:
            value (float): value for IDD Field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`
                Default value: 1.25
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
                                 'for field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`'.format(value))

        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = value

    @property
    def standard_design_capacity(self):
        """Get standard_design_capacity

        Returns:
            float: the value of `standard_design_capacity` or None if not set
        """
        return self._data["Standard Design Capacity"]

    @standard_design_capacity.setter
    def standard_design_capacity(self, value=None):
        """  Corresponds to IDD Field `standard_design_capacity`
        Standard design capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Standard design capacity times the Heat Rejection Capacity and
        Nominal Capacity Sizing Ratio (e.g. 1.25) gives the actual fluid cooler
        heat rejection at these operating conditions.
        Only used for Performance Input Method = StandardDesignCapacity;
        for other input methods, this field is ignored.
        The standard conditions mentioned above for Standard design capacity are already
        specified in the EnergyPlus. So the input fields such as design entering water
        temp., design entering air wet-bulb and dry-bulb temp. and design water flow rate, if
        provided in the input, will be ignored for the StandardDesignCapacity performance input
        method. Also, the standard conditions are for water as a fluid type so this performance input
        method can only be used with water as a fluid type (as specified in CondenserLoop object).

        Args:
            value (float): value for IDD Field `standard_design_capacity`
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
                                 'for field `standard_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `standard_design_capacity`')

        self._data["Standard Design Capacity"] = value

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
        Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate;
        for other Performance Input Methods, this field is ignored.

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
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_water_flow_rate`
        Input value is ignored if fluid cooler Performance Input Method= StandardDesignCapacity.

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
    def user_specified_design_capacity(self):
        """Get user_specified_design_capacity

        Returns:
            float: the value of `user_specified_design_capacity` or None if not set
        """
        return self._data["User Specified Design Capacity"]

    @user_specified_design_capacity.setter
    def user_specified_design_capacity(self, value=None):
        """  Corresponds to IDD Field `user_specified_design_capacity`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float): value for IDD Field `user_specified_design_capacity`
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
                                 'for field `user_specified_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `user_specified_design_capacity`')

        self._data["User Specified Design Capacity"] = value

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
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Water Temperature must be greater than Design Entering Air Temperature.

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
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Temperature must be greater than Design Entering Air Wet-bulb
        Temperature.

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
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Wet-bulb Temperature must be less than Design Entering Air
        Temperature.

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
    def capacity_control(self):
        """Get capacity_control

        Returns:
            str: the value of `capacity_control` or None if not set
        """
        return self._data["Capacity Control"]

    @capacity_control.setter
    def capacity_control(self, value="FanCycling"):
        """  Corresponds to IDD Field `capacity_control`

        Args:
            value (str): value for IDD Field `capacity_control`
                Accepted values are:
                      - FanCycling
                      - FluidBypass
                Default value: FanCycling
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
                                 'for field `capacity_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_control`')
            vals = set()
            vals.add("FanCycling")
            vals.add("FluidBypass")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `capacity_control`'.format(value))

        self._data["Capacity Control"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `sizing_factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `sizing_factor`
                Default value: 1.0
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
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')

        self._data["Sizing Factor"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value="SaturatedExit"):
        """  Corresponds to IDD Field `evaporation_loss_mode`

        Args:
            value (str): value for IDD Field `evaporation_loss_mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                Default value: SaturatedExit
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
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            vals = set()
            vals.add("LossFactor")
            vals.add("SaturatedExit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `evaporation_loss_mode`'.format(value))

        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=None):
        """  Corresponds to IDD Field `evaporation_loss_factor`
        Rate of water evaporation from the Fluid Cooler and lost to the outdoor air [%/K]
        Empirical correlation is used to calculate default loss factor if it not explicitly provided.

        Args:
            value (float): value for IDD Field `evaporation_loss_factor`
                Unit: percent/K
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
                                 'for field `evaporation_loss_factor`'.format(value))

        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=0.008 ):
        """  Corresponds to IDD Field `drift_loss_percent`
        Rate of drift loss as a percentage of circulating spray water flow rate
        Default value for this field in under investigation. For now Cooling towers drift loss
        percent default value is taken here.

        Args:
            value (float): value for IDD Field `drift_loss_percent`
                Unit: percent
                Default value: 0.008
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
                                 'for field `drift_loss_percent`'.format(value))

        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value="ConcentrationRatio"):
        """  Corresponds to IDD Field `blowdown_calculation_mode`

        Args:
            value (str): value for IDD Field `blowdown_calculation_mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                Default value: ConcentrationRatio
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
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            vals = set()
            vals.add("ConcentrationRatio")
            vals.add("ScheduledRate")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `blowdown_calculation_mode`'.format(value))

        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0 ):
        """  Corresponds to IDD Field `blowdown_concentration_ratio`
        Characterizes the rate of blowdown in the Evaporative Fluid Cooler.
        Blowdown is water intentionally drained from the basin in order to offset the build
        up of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Default value for this field in under investigation. For now Cooling towers
        Blowdown Concentration Ratio percent default value is taken here.

        Args:
            value (float): value for IDD Field `blowdown_concentration_ratio`
                Default value: 3.0
                value >= 2.0
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
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')

        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `blowdown_makeup_water_usage_schedule_name`
        Makeup water usage due to blowdown results from occasionally draining a small
        amount of water in the Fluid Cooler basin to purge scale or other contaminants to
        reduce their concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `blowdown_makeup_water_usage_schedule_name`
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
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')

        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_water_storage_tank_name`

        Args:
            value (str): value for IDD Field `supply_water_storage_tank_name`
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
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')

        self._data["Supply Water Storage Tank Name"] = value

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
        out.append(self._to_str(self.design_air_flow_rate))
        out.append(self._to_str(self.design_air_flow_rate_fan_power))
        out.append(self._to_str(self.design_spray_water_flow_rate))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio))
        out.append(self._to_str(self.standard_design_capacity))
        out.append(self._to_str(self.design_air_flow_rate_ufactor_times_area_value))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.user_specified_design_capacity))
        out.append(self._to_str(self.design_entering_water_temperature))
        out.append(self._to_str(self.design_entering_air_temperature))
        out.append(self._to_str(self.design_entering_air_wetbulb_temperature))
        out.append(self._to_str(self.capacity_control))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.evaporation_loss_mode))
        out.append(self._to_str(self.evaporation_loss_factor))
        out.append(self._to_str(self.drift_loss_percent))
        out.append(self._to_str(self.blowdown_calculation_mode))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        out.append(self._to_str(self.blowdown_makeup_water_usage_schedule_name))
        out.append(self._to_str(self.supply_water_storage_tank_name))
        return ",".join(out)

class EvaporativeFluidCoolerTwoSpeed(object):
    """ Corresponds to IDD object `EvaporativeFluidCooler:TwoSpeed`
        This model is based on Merkel's theory, which is also the basis
        for the cooling tower model in EnergyPlus. The Evaporative fluid cooler
        is modeled as a counter flow heat exchanger.
    """
    internal_name = "EvaporativeFluidCooler:TwoSpeed"
    field_count = 34

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EvaporativeFluidCooler:TwoSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["High Fan Speed Air Flow Rate"] = None
        self._data["High Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Air Flow Rate"] = None
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = None
        self._data["Low Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Fan Power Sizing Factor"] = None
        self._data["Design Spray Water Flow Rate"] = None
        self._data["Performance Input Method"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["High Speed Standard Design Capacity"] = None
        self._data["Low Speed Standard Design Capacity"] = None
        self._data["Low Speed Standard Capacity Sizing Factor"] = None
        self._data["High Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["High Speed User Specified Design Capacity"] = None
        self._data["Low Speed User Specified Design Capacity"] = None
        self._data["Low Speed User Specified Design Capacity Sizing Factor"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wet-bulb Temperature"] = None
        self._data["High Speed Sizing Factor"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None

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
            self.design_spray_water_flow_rate = None
        else:
            self.design_spray_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_speed_standard_design_capacity = None
        else:
            self.high_speed_standard_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_speed_standard_design_capacity = None
        else:
            self.low_speed_standard_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_speed_standard_capacity_sizing_factor = None
        else:
            self.low_speed_standard_capacity_sizing_factor = vals[i]
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
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_speed_user_specified_design_capacity = None
        else:
            self.high_speed_user_specified_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_speed_user_specified_design_capacity = None
        else:
            self.low_speed_user_specified_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_speed_user_specified_design_capacity_sizing_factor = None
        else:
            self.low_speed_user_specified_design_capacity_sizing_factor = vals[i]
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
            self.high_speed_sizing_factor = None
        else:
            self.high_speed_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
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
    def high_fan_speed_air_flow_rate(self):
        """Get high_fan_speed_air_flow_rate

        Returns:
            float: the value of `high_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["High Fan Speed Air Flow Rate"]

    @high_fan_speed_air_flow_rate.setter
    def high_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `high_fan_speed_air_flow_rate`

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
        Low speed air flow rate must be less than high speed air flow rate

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
        This field is only used if the previous field is set to autocalculate

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
    def design_spray_water_flow_rate(self):
        """Get design_spray_water_flow_rate

        Returns:
            float: the value of `design_spray_water_flow_rate` or None if not set
        """
        return self._data["Design Spray Water Flow Rate"]

    @design_spray_water_flow_rate.setter
    def design_spray_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_spray_water_flow_rate`

        Args:
            value (float): value for IDD Field `design_spray_water_flow_rate`
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
                                 'for field `design_spray_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_spray_water_flow_rate`')

        self._data["Design Spray Water Flow Rate"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=None):
        """  Corresponds to IDD Field `performance_input_method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler Standard Design
        Capacity or by specifying Design Capacity for Non standard conditions.

        Args:
            value (str): value for IDD Field `performance_input_method`
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

    @property
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self):
        """Get heat_rejection_capacity_and_nominal_capacity_sizing_ratio

        Returns:
            float: the value of `heat_rejection_capacity_and_nominal_capacity_sizing_ratio` or None if not set
        """
        return self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    @heat_rejection_capacity_and_nominal_capacity_sizing_ratio.setter
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self, value=1.25 ):
        """  Corresponds to IDD Field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`

        Args:
            value (float): value for IDD Field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`
                Default value: 1.25
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
                                 'for field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`'.format(value))

        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = value

    @property
    def high_speed_standard_design_capacity(self):
        """Get high_speed_standard_design_capacity

        Returns:
            float: the value of `high_speed_standard_design_capacity` or None if not set
        """
        return self._data["High Speed Standard Design Capacity"]

    @high_speed_standard_design_capacity.setter
    def high_speed_standard_design_capacity(self, value=None):
        """  Corresponds to IDD Field `high_speed_standard_design_capacity`
        Standard design capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Standard design capacity times the Heat Rejection Capacity and
        Nominal Capacity Sizing Ratio (e.g. 1.25) gives the actual fluid cooler
        heat rejection at these operating conditions.
        Only used for Performance Input Method = StandardDesignCapacity;
        for other input methods, this field is ignored.
        The standard conditions mentioned above for Standard design capacity are already
        specified in the EnergyPlus. So the input fields such as design entering water
        temp., design entering air wet-bulb and dry-bulb temp. and design water flow rate, if
        provided in the input, will be ignored for the StandardDesignCapacity performance input
        method. Also, the standard conditions are for water as a fluid type so this performance input
        method can only be used with water as a fluid type (as specified in CondenserLoop object).

        Args:
            value (float): value for IDD Field `high_speed_standard_design_capacity`
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
                                 'for field `high_speed_standard_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_standard_design_capacity`')

        self._data["High Speed Standard Design Capacity"] = value

    @property
    def low_speed_standard_design_capacity(self):
        """Get low_speed_standard_design_capacity

        Returns:
            float: the value of `low_speed_standard_design_capacity` or None if not set
        """
        return self._data["Low Speed Standard Design Capacity"]

    @low_speed_standard_design_capacity.setter
    def low_speed_standard_design_capacity(self, value=None):
        """  Corresponds to IDD Field `low_speed_standard_design_capacity`
        Standard design capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Standard design capacity times the Heat Rejection Capacity and
        Nominal Capacity Sizing Ratio (e.g. 1.25) gives the actual fluid cooler
        heat rejection at these operating conditions.
        Only used for Performance Input Method = StandardDesignCapacity;
        for other input methods, this field is ignored.
        The standard conditions mentioned above for Standard design capacity are already
        specified in the EnergyPlus. So the input fields such as design entering water
        temp., design entering air wet-bulb and dry-bulb temp. and design water flow rate, if
        provided in the input, will be ignored for the StandardDesignCapacity performance input
        method. Also, the standard conditions are for water as a fluid type so this performance input
        method can only be used with water as a fluid type (as specified in CondenserLoop object).

        Args:
            value (float): value for IDD Field `low_speed_standard_design_capacity`
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
                                 'for field `low_speed_standard_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_standard_design_capacity`')

        self._data["Low Speed Standard Design Capacity"] = value

    @property
    def low_speed_standard_capacity_sizing_factor(self):
        """Get low_speed_standard_capacity_sizing_factor

        Returns:
            float: the value of `low_speed_standard_capacity_sizing_factor` or None if not set
        """
        return self._data["Low Speed Standard Capacity Sizing Factor"]

    @low_speed_standard_capacity_sizing_factor.setter
    def low_speed_standard_capacity_sizing_factor(self, value=0.5 ):
        """  Corresponds to IDD Field `low_speed_standard_capacity_sizing_factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `low_speed_standard_capacity_sizing_factor`
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
                                 'for field `low_speed_standard_capacity_sizing_factor`'.format(value))

        self._data["Low Speed Standard Capacity Sizing Factor"] = value

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
        Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate;
        for other Performance Input Methods, this field is ignored.

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
        Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate;
        for other input methods, this field is ignored.
        Low speed fluid cooler UA must be less than high speed fluid cooler UA

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
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_water_flow_rate`
        Input value is ignored if fluid cooler Performance Input Method= StandardDesignCapacity

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
    def high_speed_user_specified_design_capacity(self):
        """Get high_speed_user_specified_design_capacity

        Returns:
            float: the value of `high_speed_user_specified_design_capacity` or None if not set
        """
        return self._data["High Speed User Specified Design Capacity"]

    @high_speed_user_specified_design_capacity.setter
    def high_speed_user_specified_design_capacity(self, value=None):
        """  Corresponds to IDD Field `high_speed_user_specified_design_capacity`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float): value for IDD Field `high_speed_user_specified_design_capacity`
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
                                 'for field `high_speed_user_specified_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_user_specified_design_capacity`')

        self._data["High Speed User Specified Design Capacity"] = value

    @property
    def low_speed_user_specified_design_capacity(self):
        """Get low_speed_user_specified_design_capacity

        Returns:
            float: the value of `low_speed_user_specified_design_capacity` or None if not set
        """
        return self._data["Low Speed User Specified Design Capacity"]

    @low_speed_user_specified_design_capacity.setter
    def low_speed_user_specified_design_capacity(self, value=None):
        """  Corresponds to IDD Field `low_speed_user_specified_design_capacity`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float): value for IDD Field `low_speed_user_specified_design_capacity`
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
                                 'for field `low_speed_user_specified_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_user_specified_design_capacity`')

        self._data["Low Speed User Specified Design Capacity"] = value

    @property
    def low_speed_user_specified_design_capacity_sizing_factor(self):
        """Get low_speed_user_specified_design_capacity_sizing_factor

        Returns:
            float: the value of `low_speed_user_specified_design_capacity_sizing_factor` or None if not set
        """
        return self._data["Low Speed User Specified Design Capacity Sizing Factor"]

    @low_speed_user_specified_design_capacity_sizing_factor.setter
    def low_speed_user_specified_design_capacity_sizing_factor(self, value=0.5 ):
        """  Corresponds to IDD Field `low_speed_user_specified_design_capacity_sizing_factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `low_speed_user_specified_design_capacity_sizing_factor`
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
                                 'for field `low_speed_user_specified_design_capacity_sizing_factor`'.format(value))

        self._data["Low Speed User Specified Design Capacity Sizing Factor"] = value

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
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Water Temperature must be greater than Design Entering Air Temperature.

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
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Temperature must be greater than Design Entering Air Wet-bulb
        Temperature.

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
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Wet-bulb Temperature must be less than Design Entering Air
        Temperature.

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
    def high_speed_sizing_factor(self):
        """Get high_speed_sizing_factor

        Returns:
            float: the value of `high_speed_sizing_factor` or None if not set
        """
        return self._data["High Speed Sizing Factor"]

    @high_speed_sizing_factor.setter
    def high_speed_sizing_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `high_speed_sizing_factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `high_speed_sizing_factor`
                Default value: 1.0
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
                                 'for field `high_speed_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_sizing_factor`')

        self._data["High Speed Sizing Factor"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value="SaturatedExit"):
        """  Corresponds to IDD Field `evaporation_loss_mode`

        Args:
            value (str): value for IDD Field `evaporation_loss_mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                Default value: SaturatedExit
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
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            vals = set()
            vals.add("LossFactor")
            vals.add("SaturatedExit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `evaporation_loss_mode`'.format(value))

        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=None):
        """  Corresponds to IDD Field `evaporation_loss_factor`
        Rate of water evaporation from the Fluid Cooler and lost to the outdoor air [%/K]
        Empirical correlation is used to calculate default loss factor if it not explicitly provided.

        Args:
            value (float): value for IDD Field `evaporation_loss_factor`
                Unit: percent/K
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
                                 'for field `evaporation_loss_factor`'.format(value))

        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=0.008 ):
        """  Corresponds to IDD Field `drift_loss_percent`
        Default value is under investigation. For now cooling towers default value is taken.

        Args:
            value (float): value for IDD Field `drift_loss_percent`
                Unit: percent
                Default value: 0.008
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
                                 'for field `drift_loss_percent`'.format(value))

        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value="ConcentrationRatio"):
        """  Corresponds to IDD Field `blowdown_calculation_mode`

        Args:
            value (str): value for IDD Field `blowdown_calculation_mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                Default value: ConcentrationRatio
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
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            vals = set()
            vals.add("ConcentrationRatio")
            vals.add("ScheduledRate")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `blowdown_calculation_mode`'.format(value))

        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0 ):
        """  Corresponds to IDD Field `blowdown_concentration_ratio`
        Characterizes the rate of blowdown in the Evaporative Fluid Cooler.
        Blowdown is water intentionally drained from the Evaporative Fluid Cooler in order to offset the
        build up of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Default value is under investigation. For now cooling towers default value is taken.

        Args:
            value (float): value for IDD Field `blowdown_concentration_ratio`
                Default value: 3.0
                value >= 2.0
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
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')

        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `blowdown_makeup_water_usage_schedule_name`
        Makeup water usage due to blowdown results from occasionally draining some amount
        of water in the Evaporative Fluid Cooler basin to purge scale or other contaminants to reduce
        their concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `blowdown_makeup_water_usage_schedule_name`
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
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')

        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_water_storage_tank_name`

        Args:
            value (str): value for IDD Field `supply_water_storage_tank_name`
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
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')

        self._data["Supply Water Storage Tank Name"] = value

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
        out.append(self._to_str(self.high_fan_speed_air_flow_rate))
        out.append(self._to_str(self.high_fan_speed_fan_power))
        out.append(self._to_str(self.low_fan_speed_air_flow_rate))
        out.append(self._to_str(self.low_fan_speed_air_flow_rate_sizing_factor))
        out.append(self._to_str(self.low_fan_speed_fan_power))
        out.append(self._to_str(self.low_fan_speed_fan_power_sizing_factor))
        out.append(self._to_str(self.design_spray_water_flow_rate))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio))
        out.append(self._to_str(self.high_speed_standard_design_capacity))
        out.append(self._to_str(self.low_speed_standard_design_capacity))
        out.append(self._to_str(self.low_speed_standard_capacity_sizing_factor))
        out.append(self._to_str(self.high_fan_speed_ufactor_times_area_value))
        out.append(self._to_str(self.low_fan_speed_ufactor_times_area_value))
        out.append(self._to_str(self.low_fan_speed_ufactor_times_area_sizing_factor))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.high_speed_user_specified_design_capacity))
        out.append(self._to_str(self.low_speed_user_specified_design_capacity))
        out.append(self._to_str(self.low_speed_user_specified_design_capacity_sizing_factor))
        out.append(self._to_str(self.design_entering_water_temperature))
        out.append(self._to_str(self.design_entering_air_temperature))
        out.append(self._to_str(self.design_entering_air_wetbulb_temperature))
        out.append(self._to_str(self.high_speed_sizing_factor))
        out.append(self._to_str(self.evaporation_loss_mode))
        out.append(self._to_str(self.evaporation_loss_factor))
        out.append(self._to_str(self.drift_loss_percent))
        out.append(self._to_str(self.blowdown_calculation_mode))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        out.append(self._to_str(self.blowdown_makeup_water_usage_schedule_name))
        out.append(self._to_str(self.supply_water_storage_tank_name))
        return ",".join(out)