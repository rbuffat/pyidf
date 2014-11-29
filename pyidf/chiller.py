from collections import OrderedDict

class ChillerElectricEir(object):
    """ Corresponds to IDD object `Chiller:Electric:EIR`
        This chiller model is the empirical model from the DOE-2 building Energy
        simulation program. Chiller performance at off-reference conditions is modeled
        using three polynomial equations. Three curves objects are required.
    """
    internal_name = "Chiller:Electric:EIR"
    field_count = 33

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:Electric:EIR`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Capacity"] = None
        self._data["Reference COP"] = None
        self._data["Reference Leaving Chilled Water Temperature"] = None
        self._data["Reference Entering Condenser Fluid Temperature"] = None
        self._data["Reference Chilled Water Flow Rate"] = None
        self._data["Reference Condenser Fluid Flow Rate"] = None
        self._data["Cooling Capacity Function of Temperature Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Minimum Unloading Ratio"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Condenser Type"] = None
        self._data["Condenser Fan Power Ratio"] = None
        self._data["Fraction of Compressor Electric Consumption Rejected by Condenser"] = None
        self._data["Leaving Chilled Water Lower Temperature Limit"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Design Heat Recovery Water Flow Rate"] = None
        self._data["Heat Recovery Inlet Node Name"] = None
        self._data["Heat Recovery Outlet Node Name"] = None
        self._data["Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Condenser Heat Recovery Relative Capacity Fraction"] = None
        self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"] = None
        self._data["Heat Recovery Leaving Temperature Setpoint Node Name"] = None

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
            self.reference_capacity = None
        else:
            self.reference_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_cop = None
        else:
            self.reference_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_leaving_chilled_water_temperature = None
        else:
            self.reference_leaving_chilled_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_entering_condenser_fluid_temperature = None
        else:
            self.reference_entering_condenser_fluid_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_chilled_water_flow_rate = None
        else:
            self.reference_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_condenser_fluid_flow_rate = None
        else:
            self.reference_condenser_fluid_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_function_of_temperature_curve_name = None
        else:
            self.cooling_capacity_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_unloading_ratio = None
        else:
            self.minimum_unloading_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_fan_power_ratio = None
        else:
            self.condenser_fan_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_compressor_electric_consumption_rejected_by_condenser = None
        else:
            self.fraction_of_compressor_electric_consumption_rejected_by_condenser = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaving_chilled_water_lower_temperature_limit = None
        else:
            self.leaving_chilled_water_lower_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_heat_recovery_water_flow_rate = None
        else:
            self.design_heat_recovery_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_node_name = None
        else:
            self.heat_recovery_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_outlet_node_name = None
        else:
            self.heat_recovery_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_heat_recovery_relative_capacity_fraction = None
        else:
            self.condenser_heat_recovery_relative_capacity_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_high_temperature_limit_schedule_name = None
        else:
            self.heat_recovery_inlet_high_temperature_limit_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_leaving_temperature_setpoint_node_name = None
        else:
            self.heat_recovery_leaving_temperature_setpoint_node_name = vals[i]
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
    def reference_capacity(self):
        """Get reference_capacity

        Returns:
            float: the value of `reference_capacity` or None if not set
        """
        return self._data["Reference Capacity"]

    @reference_capacity.setter
    def reference_capacity(self, value=None):
        """  Corresponds to IDD Field `reference_capacity`

        Args:
            value (float): value for IDD Field `reference_capacity`
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
                                 'for field `reference_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_capacity`')

        self._data["Reference Capacity"] = value

    @property
    def reference_cop(self):
        """Get reference_cop

        Returns:
            float: the value of `reference_cop` or None if not set
        """
        return self._data["Reference COP"]

    @reference_cop.setter
    def reference_cop(self, value=None):
        """  Corresponds to IDD Field `reference_cop`
        Efficiency of the chiller compressor (cooling output/compressor energy input).
        Condenser fan power should not be included here.

        Args:
            value (float): value for IDD Field `reference_cop`
                Unit: W/W
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
                                 'for field `reference_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_cop`')

        self._data["Reference COP"] = value

    @property
    def reference_leaving_chilled_water_temperature(self):
        """Get reference_leaving_chilled_water_temperature

        Returns:
            float: the value of `reference_leaving_chilled_water_temperature` or None if not set
        """
        return self._data["Reference Leaving Chilled Water Temperature"]

    @reference_leaving_chilled_water_temperature.setter
    def reference_leaving_chilled_water_temperature(self, value=6.67 ):
        """  Corresponds to IDD Field `reference_leaving_chilled_water_temperature`

        Args:
            value (float): value for IDD Field `reference_leaving_chilled_water_temperature`
                Unit: C
                Default value: 6.67
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
                                 'for field `reference_leaving_chilled_water_temperature`'.format(value))

        self._data["Reference Leaving Chilled Water Temperature"] = value

    @property
    def reference_entering_condenser_fluid_temperature(self):
        """Get reference_entering_condenser_fluid_temperature

        Returns:
            float: the value of `reference_entering_condenser_fluid_temperature` or None if not set
        """
        return self._data["Reference Entering Condenser Fluid Temperature"]

    @reference_entering_condenser_fluid_temperature.setter
    def reference_entering_condenser_fluid_temperature(self, value=29.4 ):
        """  Corresponds to IDD Field `reference_entering_condenser_fluid_temperature`

        Args:
            value (float): value for IDD Field `reference_entering_condenser_fluid_temperature`
                Unit: C
                Default value: 29.4
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
                                 'for field `reference_entering_condenser_fluid_temperature`'.format(value))

        self._data["Reference Entering Condenser Fluid Temperature"] = value

    @property
    def reference_chilled_water_flow_rate(self):
        """Get reference_chilled_water_flow_rate

        Returns:
            float: the value of `reference_chilled_water_flow_rate` or None if not set
        """
        return self._data["Reference Chilled Water Flow Rate"]

    @reference_chilled_water_flow_rate.setter
    def reference_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `reference_chilled_water_flow_rate`

        Args:
            value (float): value for IDD Field `reference_chilled_water_flow_rate`
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
                                 'for field `reference_chilled_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_chilled_water_flow_rate`')

        self._data["Reference Chilled Water Flow Rate"] = value

    @property
    def reference_condenser_fluid_flow_rate(self):
        """Get reference_condenser_fluid_flow_rate

        Returns:
            float: the value of `reference_condenser_fluid_flow_rate` or None if not set
        """
        return self._data["Reference Condenser Fluid Flow Rate"]

    @reference_condenser_fluid_flow_rate.setter
    def reference_condenser_fluid_flow_rate(self, value=None):
        """  Corresponds to IDD Field `reference_condenser_fluid_flow_rate`
        This field is only used for Condenser Type = AirCooled or EvaporativelyCooled
        when Heat Recovery is specified

        Args:
            value (float): value for IDD Field `reference_condenser_fluid_flow_rate`
                Unit: m3/s
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
                                 'for field `reference_condenser_fluid_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `reference_condenser_fluid_flow_rate`')

        self._data["Reference Condenser Fluid Flow Rate"] = value

    @property
    def cooling_capacity_function_of_temperature_curve_name(self):
        """Get cooling_capacity_function_of_temperature_curve_name

        Returns:
            str: the value of `cooling_capacity_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Capacity Function of Temperature Curve Name"]

    @cooling_capacity_function_of_temperature_curve_name.setter
    def cooling_capacity_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_function_of_temperature_curve_name`
        Cooling capacity as a function of CW supply temp and entering condenser temp
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*ECT + e*ECT**2 + f*CWS*ECT
        CWS = supply (leaving) chilled water temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `cooling_capacity_function_of_temperature_curve_name`
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
                                 'for field `cooling_capacity_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_capacity_function_of_temperature_curve_name`')

        self._data["Cooling Capacity Function of Temperature Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        Electric Input Ratio (EIR) as a function of temperature
        EIR = 1/COP
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*ECT + e*ECT**2 + f*CWS*ECT
        CWS = supply (leaving) chilled water temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
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
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        Electric Input Ratio (EIR) as a function of Part Load Ratio (PLR)
        EIR = 1/COP
        Table:OneIndependentVariable object can also be used
        quadratic curve = a + b*PLR + c*PLR**2
        PLR = part load ratio (cooling load/steady state capacity)

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
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
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=0.1 ):
        """  Corresponds to IDD Field `minimum_part_load_ratio`
        Part load ratio below which the chiller starts cycling on/off to meet the load.
        Must be less than or equal to Maximum Part Load Ratio.

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
                Default value: 0.1
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `maximum_part_load_ratio`
        Maximum allowable part load ratio. Must be greater than or equal to Minimum Part Load Ratio.

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `optimum_part_load_ratio`
        Optimum part load ratio where the chiller is most efficient.
        Must be greater than or equal to the Minimum Part Load Ratio
        and less than or equal to the Maximum Part Load Ratio.

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def minimum_unloading_ratio(self):
        """Get minimum_unloading_ratio

        Returns:
            float: the value of `minimum_unloading_ratio` or None if not set
        """
        return self._data["Minimum Unloading Ratio"]

    @minimum_unloading_ratio.setter
    def minimum_unloading_ratio(self, value=0.2 ):
        """  Corresponds to IDD Field `minimum_unloading_ratio`
        Part load ratio where the chiller can no longer unload and false loading begins.
        Minimum unloading ratio must be greater than or equal to the Minimum Part Load Ratio
        and less than or equal to the Maximum Part Load Ratio.

        Args:
            value (float): value for IDD Field `minimum_unloading_ratio`
                Default value: 0.2
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
                                 'for field `minimum_unloading_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_unloading_ratio`')

        self._data["Minimum Unloading Ratio"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`
        Not required if air-cooled or evaporativly-cooled

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`
        Not required if air-cooled or evaporatively-cooled

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="WaterCooled"):
        """  Corresponds to IDD Field `condenser_type`

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - WaterCooled
                      - EvaporativelyCooled
                Default value: WaterCooled
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
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            vals = set()
            vals.add("AirCooled")
            vals.add("WaterCooled")
            vals.add("EvaporativelyCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

    @property
    def condenser_fan_power_ratio(self):
        """Get condenser_fan_power_ratio

        Returns:
            float: the value of `condenser_fan_power_ratio` or None if not set
        """
        return self._data["Condenser Fan Power Ratio"]

    @condenser_fan_power_ratio.setter
    def condenser_fan_power_ratio(self, value=0.0 ):
        """  Corresponds to IDD Field `condenser_fan_power_ratio`
        Use for air-cooled or evaporatively-cooled condensers.
        Ratio of condenser fan power to reference chiller capacity

        Args:
            value (float): value for IDD Field `condenser_fan_power_ratio`
                Unit: W/W
                Default value: 0.0
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
                                 'for field `condenser_fan_power_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `condenser_fan_power_ratio`')

        self._data["Condenser Fan Power Ratio"] = value

    @property
    def fraction_of_compressor_electric_consumption_rejected_by_condenser(self):
        """Get fraction_of_compressor_electric_consumption_rejected_by_condenser

        Returns:
            float: the value of `fraction_of_compressor_electric_consumption_rejected_by_condenser` or None if not set
        """
        return self._data["Fraction of Compressor Electric Consumption Rejected by Condenser"]

    @fraction_of_compressor_electric_consumption_rejected_by_condenser.setter
    def fraction_of_compressor_electric_consumption_rejected_by_condenser(self, value=1.0 ):
        """  Corresponds to IDD Field `fraction_of_compressor_electric_consumption_rejected_by_condenser`
        Fraction of compressor electrical energy that must be rejected by the condenser.
        Enter a value of 1.0 when modeling hermetic chillers.
        For open chillers, enter the compressor motor efficiency.
        This value should be greater than 0.6 for praticle applications.

        Args:
            value (float): value for IDD Field `fraction_of_compressor_electric_consumption_rejected_by_condenser`
                Default value: 1.0
                value > 0.0
                value <= 1.0
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
                                 'for field `fraction_of_compressor_electric_consumption_rejected_by_condenser`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fraction_of_compressor_electric_consumption_rejected_by_condenser`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_compressor_electric_consumption_rejected_by_condenser`')

        self._data["Fraction of Compressor Electric Consumption Rejected by Condenser"] = value

    @property
    def leaving_chilled_water_lower_temperature_limit(self):
        """Get leaving_chilled_water_lower_temperature_limit

        Returns:
            float: the value of `leaving_chilled_water_lower_temperature_limit` or None if not set
        """
        return self._data["Leaving Chilled Water Lower Temperature Limit"]

    @leaving_chilled_water_lower_temperature_limit.setter
    def leaving_chilled_water_lower_temperature_limit(self, value=2.0 ):
        """  Corresponds to IDD Field `leaving_chilled_water_lower_temperature_limit`

        Args:
            value (float): value for IDD Field `leaving_chilled_water_lower_temperature_limit`
                Unit: C
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
                                 'for field `leaving_chilled_water_lower_temperature_limit`'.format(value))

        self._data["Leaving Chilled Water Lower Temperature Limit"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode`'.format(value))

        self._data["Chiller Flow Mode"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """Get design_heat_recovery_water_flow_rate

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self._data["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_heat_recovery_water_flow_rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.

        Args:
            value (float): value for IDD Field `design_heat_recovery_water_flow_rate`
                Unit: m3/s
                Default value: 0.0
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
                                 'for field `design_heat_recovery_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_heat_recovery_water_flow_rate`')

        self._data["Design Heat Recovery Water Flow Rate"] = value

    @property
    def heat_recovery_inlet_node_name(self):
        """Get heat_recovery_inlet_node_name

        Returns:
            str: the value of `heat_recovery_inlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Inlet Node Name"]

    @heat_recovery_inlet_node_name.setter
    def heat_recovery_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_node_name`
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
                                 'for field `heat_recovery_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_node_name`')

        self._data["Heat Recovery Inlet Node Name"] = value

    @property
    def heat_recovery_outlet_node_name(self):
        """Get heat_recovery_outlet_node_name

        Returns:
            str: the value of `heat_recovery_outlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Outlet Node Name"]

    @heat_recovery_outlet_node_name.setter
    def heat_recovery_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_outlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_outlet_node_name`
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
                                 'for field `heat_recovery_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_outlet_node_name`')

        self._data["Heat Recovery Outlet Node Name"] = value

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
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `basin_heater_capacity`
        This field is only used for Condenser Type = EvaporativelyCooled and for periods
        when the basin heater is available (field Basin Heater Operating Schedule Name).
        For this situation, the heater maintains the basin water temperature at the basin heater
        setpoint temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when the chiller is not operating.

        Args:
            value (float): value for IDD Field `basin_heater_capacity`
                Unit: W/K
                Default value: 0.0
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')

        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `basin_heater_setpoint_temperature`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Enter the outdoor dry-bulb temperature when the basin heater turns on.

        Args:
            value (float): value for IDD Field `basin_heater_setpoint_temperature`
                Unit: C
                Default value: 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')

        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `basin_heater_operating_schedule_name`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `basin_heater_operating_schedule_name`
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
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')

        self._data["Basin Heater Operating Schedule Name"] = value

    @property
    def condenser_heat_recovery_relative_capacity_fraction(self):
        """Get condenser_heat_recovery_relative_capacity_fraction

        Returns:
            float: the value of `condenser_heat_recovery_relative_capacity_fraction` or None if not set
        """
        return self._data["Condenser Heat Recovery Relative Capacity Fraction"]

    @condenser_heat_recovery_relative_capacity_fraction.setter
    def condenser_heat_recovery_relative_capacity_fraction(self, value=None):
        """  Corresponds to IDD Field `condenser_heat_recovery_relative_capacity_fraction`
        This optional field is the fraction of total rejected heat that can be recovered at full load

        Args:
            value (float): value for IDD Field `condenser_heat_recovery_relative_capacity_fraction`
                value >= 0.0
                value <= 1.0
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
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`')

        self._data["Condenser Heat Recovery Relative Capacity Fraction"] = value

    @property
    def heat_recovery_inlet_high_temperature_limit_schedule_name(self):
        """Get heat_recovery_inlet_high_temperature_limit_schedule_name

        Returns:
            str: the value of `heat_recovery_inlet_high_temperature_limit_schedule_name` or None if not set
        """
        return self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"]

    @heat_recovery_inlet_high_temperature_limit_schedule_name.setter
    def heat_recovery_inlet_high_temperature_limit_schedule_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_high_temperature_limit_schedule_name`
        This optional schedule of temperatures will turn off heat recovery if inlet exceeds the value

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_high_temperature_limit_schedule_name`
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
                                 'for field `heat_recovery_inlet_high_temperature_limit_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_high_temperature_limit_schedule_name`')

        self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"] = value

    @property
    def heat_recovery_leaving_temperature_setpoint_node_name(self):
        """Get heat_recovery_leaving_temperature_setpoint_node_name

        Returns:
            str: the value of `heat_recovery_leaving_temperature_setpoint_node_name` or None if not set
        """
        return self._data["Heat Recovery Leaving Temperature Setpoint Node Name"]

    @heat_recovery_leaving_temperature_setpoint_node_name.setter
    def heat_recovery_leaving_temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_leaving_temperature_setpoint_node_name`
        This optional field provides control over the heat recovery
        Using this triggers a model more suited to series bundle and chillers with higher temperature heat recovery
        If this field is not used, the bundles are modeled as being in parallel

        Args:
            value (str): value for IDD Field `heat_recovery_leaving_temperature_setpoint_node_name`
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
                                 'for field `heat_recovery_leaving_temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_leaving_temperature_setpoint_node_name`')

        self._data["Heat Recovery Leaving Temperature Setpoint Node Name"] = value

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
        out.append(self._to_str(self.reference_capacity))
        out.append(self._to_str(self.reference_cop))
        out.append(self._to_str(self.reference_leaving_chilled_water_temperature))
        out.append(self._to_str(self.reference_entering_condenser_fluid_temperature))
        out.append(self._to_str(self.reference_chilled_water_flow_rate))
        out.append(self._to_str(self.reference_condenser_fluid_flow_rate))
        out.append(self._to_str(self.cooling_capacity_function_of_temperature_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.minimum_unloading_ratio))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.condenser_fan_power_ratio))
        out.append(self._to_str(self.fraction_of_compressor_electric_consumption_rejected_by_condenser))
        out.append(self._to_str(self.leaving_chilled_water_lower_temperature_limit))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.design_heat_recovery_water_flow_rate))
        out.append(self._to_str(self.heat_recovery_inlet_node_name))
        out.append(self._to_str(self.heat_recovery_outlet_node_name))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        out.append(self._to_str(self.condenser_heat_recovery_relative_capacity_fraction))
        out.append(self._to_str(self.heat_recovery_inlet_high_temperature_limit_schedule_name))
        out.append(self._to_str(self.heat_recovery_leaving_temperature_setpoint_node_name))
        return ",".join(out)

class ChillerElectricReformulatedEir(object):
    """ Corresponds to IDD object `Chiller:Electric:ReformulatedEIR`
        This chiller model is an empirical model, a reformulated version of Chiller:Electric:EIR
        where the performance is a function of condenser leaving fluid Temperature instead of
        condenser entering fluid Temperature. Chiller performance at off-reference conditions is
        modeled using three polynomial equations. Three curve objects are required.
    """
    internal_name = "Chiller:Electric:ReformulatedEIR"
    field_count = 28

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:Electric:ReformulatedEIR`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Capacity"] = None
        self._data["Reference COP"] = None
        self._data["Reference Leaving Chilled Water Temperature"] = None
        self._data["Reference Leaving Condenser Water Temperature"] = None
        self._data["Reference Chilled Water Flow Rate"] = None
        self._data["Reference Condenser Water Flow Rate"] = None
        self._data["Cooling Capacity Function of Temperature Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Minimum Unloading Ratio"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Fraction of Compressor Electric Consumption Rejected by Condenser"] = None
        self._data["Leaving Chilled Water Lower Temperature Limit"] = None
        self._data["Chiller Flow Mode Type"] = None
        self._data["Design Heat Recovery Water Flow Rate"] = None
        self._data["Heat Recovery Inlet Node Name"] = None
        self._data["Heat Recovery Outlet Node Name"] = None
        self._data["Sizing Factor"] = None
        self._data["Condenser Heat Recovery Relative Capacity Fraction"] = None
        self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"] = None
        self._data["Heat Recovery Leaving Temperature Setpoint Node Name"] = None

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
            self.reference_capacity = None
        else:
            self.reference_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_cop = None
        else:
            self.reference_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_leaving_chilled_water_temperature = None
        else:
            self.reference_leaving_chilled_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_leaving_condenser_water_temperature = None
        else:
            self.reference_leaving_condenser_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_chilled_water_flow_rate = None
        else:
            self.reference_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_condenser_water_flow_rate = None
        else:
            self.reference_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_function_of_temperature_curve_name = None
        else:
            self.cooling_capacity_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_unloading_ratio = None
        else:
            self.minimum_unloading_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_compressor_electric_consumption_rejected_by_condenser = None
        else:
            self.fraction_of_compressor_electric_consumption_rejected_by_condenser = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaving_chilled_water_lower_temperature_limit = None
        else:
            self.leaving_chilled_water_lower_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode_type = None
        else:
            self.chiller_flow_mode_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_heat_recovery_water_flow_rate = None
        else:
            self.design_heat_recovery_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_node_name = None
        else:
            self.heat_recovery_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_outlet_node_name = None
        else:
            self.heat_recovery_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_heat_recovery_relative_capacity_fraction = None
        else:
            self.condenser_heat_recovery_relative_capacity_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_high_temperature_limit_schedule_name = None
        else:
            self.heat_recovery_inlet_high_temperature_limit_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_leaving_temperature_setpoint_node_name = None
        else:
            self.heat_recovery_leaving_temperature_setpoint_node_name = vals[i]
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
    def reference_capacity(self):
        """Get reference_capacity

        Returns:
            float: the value of `reference_capacity` or None if not set
        """
        return self._data["Reference Capacity"]

    @reference_capacity.setter
    def reference_capacity(self, value=None):
        """  Corresponds to IDD Field `reference_capacity`

        Args:
            value (float): value for IDD Field `reference_capacity`
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
                                 'for field `reference_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_capacity`')

        self._data["Reference Capacity"] = value

    @property
    def reference_cop(self):
        """Get reference_cop

        Returns:
            float: the value of `reference_cop` or None if not set
        """
        return self._data["Reference COP"]

    @reference_cop.setter
    def reference_cop(self, value=None):
        """  Corresponds to IDD Field `reference_cop`
        Efficiency of the chiller compressor (cooling output/compressor energy input).
        Condenser fan power should not be included here.

        Args:
            value (float): value for IDD Field `reference_cop`
                Unit: W/W
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
                                 'for field `reference_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_cop`')

        self._data["Reference COP"] = value

    @property
    def reference_leaving_chilled_water_temperature(self):
        """Get reference_leaving_chilled_water_temperature

        Returns:
            float: the value of `reference_leaving_chilled_water_temperature` or None if not set
        """
        return self._data["Reference Leaving Chilled Water Temperature"]

    @reference_leaving_chilled_water_temperature.setter
    def reference_leaving_chilled_water_temperature(self, value=6.67 ):
        """  Corresponds to IDD Field `reference_leaving_chilled_water_temperature`

        Args:
            value (float): value for IDD Field `reference_leaving_chilled_water_temperature`
                Unit: C
                Default value: 6.67
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
                                 'for field `reference_leaving_chilled_water_temperature`'.format(value))

        self._data["Reference Leaving Chilled Water Temperature"] = value

    @property
    def reference_leaving_condenser_water_temperature(self):
        """Get reference_leaving_condenser_water_temperature

        Returns:
            float: the value of `reference_leaving_condenser_water_temperature` or None if not set
        """
        return self._data["Reference Leaving Condenser Water Temperature"]

    @reference_leaving_condenser_water_temperature.setter
    def reference_leaving_condenser_water_temperature(self, value=35.0 ):
        """  Corresponds to IDD Field `reference_leaving_condenser_water_temperature`

        Args:
            value (float): value for IDD Field `reference_leaving_condenser_water_temperature`
                Unit: C
                Default value: 35.0
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
                                 'for field `reference_leaving_condenser_water_temperature`'.format(value))

        self._data["Reference Leaving Condenser Water Temperature"] = value

    @property
    def reference_chilled_water_flow_rate(self):
        """Get reference_chilled_water_flow_rate

        Returns:
            float: the value of `reference_chilled_water_flow_rate` or None if not set
        """
        return self._data["Reference Chilled Water Flow Rate"]

    @reference_chilled_water_flow_rate.setter
    def reference_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `reference_chilled_water_flow_rate`

        Args:
            value (float): value for IDD Field `reference_chilled_water_flow_rate`
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
                                 'for field `reference_chilled_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_chilled_water_flow_rate`')

        self._data["Reference Chilled Water Flow Rate"] = value

    @property
    def reference_condenser_water_flow_rate(self):
        """Get reference_condenser_water_flow_rate

        Returns:
            float: the value of `reference_condenser_water_flow_rate` or None if not set
        """
        return self._data["Reference Condenser Water Flow Rate"]

    @reference_condenser_water_flow_rate.setter
    def reference_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `reference_condenser_water_flow_rate`

        Args:
            value (float): value for IDD Field `reference_condenser_water_flow_rate`
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
                                 'for field `reference_condenser_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_condenser_water_flow_rate`')

        self._data["Reference Condenser Water Flow Rate"] = value

    @property
    def cooling_capacity_function_of_temperature_curve_name(self):
        """Get cooling_capacity_function_of_temperature_curve_name

        Returns:
            str: the value of `cooling_capacity_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Capacity Function of Temperature Curve Name"]

    @cooling_capacity_function_of_temperature_curve_name.setter
    def cooling_capacity_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_function_of_temperature_curve_name`
        Cooling capacity as a function of supply (leaving) chilled water temperature
        and leaving condenser fluid temperature
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*LCT + e*LCT**2 + f*CWS*LCT
        CWS = supply (leaving) chilled water temperature(C)
        LCT = leaving condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `cooling_capacity_function_of_temperature_curve_name`
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
                                 'for field `cooling_capacity_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_capacity_function_of_temperature_curve_name`')

        self._data["Cooling Capacity Function of Temperature Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        Electric Input Ratio (EIR) as a function of supply (leaving) chilled water temperature
        and leaving condenser fluid temperature.   EIR = 1/COP.
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*LCT + e*LCT**2 + f*CWS*LCT
        CWS = supply (leaving) chilled water temperature(C)
        LCT = leaving condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
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
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        Electric Input Ratio (EIR) as a function of Part Load Ratio (PLR)
        EIR = 1/COP
        Table:TwoIndependentVariables object can also be used
        curve = a + b*LCT + c*LCT**2 + d*PLR + e*PLR**2 + f*LCT*PLR + g*0 + h*PLR**3
        + i*0 + j*0
        PLR = part load ratio (cooling load/steady state capacity)
        LCT = leaving condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
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
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=0.1 ):
        """  Corresponds to IDD Field `minimum_part_load_ratio`
        Part load ratio below which the chiller starts cycling on/off to meet the load.
        Must be less than or equal to Maximum Part Load Ratio.

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
                Default value: 0.1
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `maximum_part_load_ratio`
        Maximum allowable part load ratio. Must be greater than or equal to Minimum Part Load Ratio.

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `optimum_part_load_ratio`
        Optimum part load ratio where the chiller is most efficient.
        Must be greater than or equal to the Minimum Part Load Ratio
        and less than or equal to the Maximum Part Load Ratio.

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def minimum_unloading_ratio(self):
        """Get minimum_unloading_ratio

        Returns:
            float: the value of `minimum_unloading_ratio` or None if not set
        """
        return self._data["Minimum Unloading Ratio"]

    @minimum_unloading_ratio.setter
    def minimum_unloading_ratio(self, value=0.2 ):
        """  Corresponds to IDD Field `minimum_unloading_ratio`
        Part load ratio where the chiller can no longer unload and false loading begins.
        Minimum unloading ratio must be greater than or equal to the Minimum Part Load Ratio
        and less than or equal to the Maximum Part Load Ratio.

        Args:
            value (float): value for IDD Field `minimum_unloading_ratio`
                Default value: 0.2
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
                                 'for field `minimum_unloading_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_unloading_ratio`')

        self._data["Minimum Unloading Ratio"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def fraction_of_compressor_electric_consumption_rejected_by_condenser(self):
        """Get fraction_of_compressor_electric_consumption_rejected_by_condenser

        Returns:
            float: the value of `fraction_of_compressor_electric_consumption_rejected_by_condenser` or None if not set
        """
        return self._data["Fraction of Compressor Electric Consumption Rejected by Condenser"]

    @fraction_of_compressor_electric_consumption_rejected_by_condenser.setter
    def fraction_of_compressor_electric_consumption_rejected_by_condenser(self, value=1.0 ):
        """  Corresponds to IDD Field `fraction_of_compressor_electric_consumption_rejected_by_condenser`
        Fraction of compressor electrical energy that must be rejected by the condenser.
        Enter a value of 1.0 when modeling hermetic chillers.
        For open chillers, enter the compressor motor efficiency.
        This value should be greater than 0.6 for praticle applications.

        Args:
            value (float): value for IDD Field `fraction_of_compressor_electric_consumption_rejected_by_condenser`
                Default value: 1.0
                value > 0.0
                value <= 1.0
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
                                 'for field `fraction_of_compressor_electric_consumption_rejected_by_condenser`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fraction_of_compressor_electric_consumption_rejected_by_condenser`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_compressor_electric_consumption_rejected_by_condenser`')

        self._data["Fraction of Compressor Electric Consumption Rejected by Condenser"] = value

    @property
    def leaving_chilled_water_lower_temperature_limit(self):
        """Get leaving_chilled_water_lower_temperature_limit

        Returns:
            float: the value of `leaving_chilled_water_lower_temperature_limit` or None if not set
        """
        return self._data["Leaving Chilled Water Lower Temperature Limit"]

    @leaving_chilled_water_lower_temperature_limit.setter
    def leaving_chilled_water_lower_temperature_limit(self, value=2.0 ):
        """  Corresponds to IDD Field `leaving_chilled_water_lower_temperature_limit`

        Args:
            value (float): value for IDD Field `leaving_chilled_water_lower_temperature_limit`
                Unit: C
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
                                 'for field `leaving_chilled_water_lower_temperature_limit`'.format(value))

        self._data["Leaving Chilled Water Lower Temperature Limit"] = value

    @property
    def chiller_flow_mode_type(self):
        """Get chiller_flow_mode_type

        Returns:
            str: the value of `chiller_flow_mode_type` or None if not set
        """
        return self._data["Chiller Flow Mode Type"]

    @chiller_flow_mode_type.setter
    def chiller_flow_mode_type(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode_type`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode_type`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode_type`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode_type`'.format(value))

        self._data["Chiller Flow Mode Type"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """Get design_heat_recovery_water_flow_rate

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self._data["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_heat_recovery_water_flow_rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.

        Args:
            value (float): value for IDD Field `design_heat_recovery_water_flow_rate`
                Unit: m3/s
                Default value: 0.0
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
                                 'for field `design_heat_recovery_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_heat_recovery_water_flow_rate`')

        self._data["Design Heat Recovery Water Flow Rate"] = value

    @property
    def heat_recovery_inlet_node_name(self):
        """Get heat_recovery_inlet_node_name

        Returns:
            str: the value of `heat_recovery_inlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Inlet Node Name"]

    @heat_recovery_inlet_node_name.setter
    def heat_recovery_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_node_name`
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
                                 'for field `heat_recovery_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_node_name`')

        self._data["Heat Recovery Inlet Node Name"] = value

    @property
    def heat_recovery_outlet_node_name(self):
        """Get heat_recovery_outlet_node_name

        Returns:
            str: the value of `heat_recovery_outlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Outlet Node Name"]

    @heat_recovery_outlet_node_name.setter
    def heat_recovery_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_outlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_outlet_node_name`
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
                                 'for field `heat_recovery_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_outlet_node_name`')

        self._data["Heat Recovery Outlet Node Name"] = value

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
    def condenser_heat_recovery_relative_capacity_fraction(self):
        """Get condenser_heat_recovery_relative_capacity_fraction

        Returns:
            float: the value of `condenser_heat_recovery_relative_capacity_fraction` or None if not set
        """
        return self._data["Condenser Heat Recovery Relative Capacity Fraction"]

    @condenser_heat_recovery_relative_capacity_fraction.setter
    def condenser_heat_recovery_relative_capacity_fraction(self, value=None):
        """  Corresponds to IDD Field `condenser_heat_recovery_relative_capacity_fraction`
        This optional field is the fraction of total rejected heat that can be recovered at full load

        Args:
            value (float): value for IDD Field `condenser_heat_recovery_relative_capacity_fraction`
                value >= 0.0
                value <= 1.0
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
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`')

        self._data["Condenser Heat Recovery Relative Capacity Fraction"] = value

    @property
    def heat_recovery_inlet_high_temperature_limit_schedule_name(self):
        """Get heat_recovery_inlet_high_temperature_limit_schedule_name

        Returns:
            str: the value of `heat_recovery_inlet_high_temperature_limit_schedule_name` or None if not set
        """
        return self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"]

    @heat_recovery_inlet_high_temperature_limit_schedule_name.setter
    def heat_recovery_inlet_high_temperature_limit_schedule_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_high_temperature_limit_schedule_name`
        This optional schedule of temperatures will turn off heat recovery if inlet exceeds the value

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_high_temperature_limit_schedule_name`
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
                                 'for field `heat_recovery_inlet_high_temperature_limit_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_high_temperature_limit_schedule_name`')

        self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"] = value

    @property
    def heat_recovery_leaving_temperature_setpoint_node_name(self):
        """Get heat_recovery_leaving_temperature_setpoint_node_name

        Returns:
            str: the value of `heat_recovery_leaving_temperature_setpoint_node_name` or None if not set
        """
        return self._data["Heat Recovery Leaving Temperature Setpoint Node Name"]

    @heat_recovery_leaving_temperature_setpoint_node_name.setter
    def heat_recovery_leaving_temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_leaving_temperature_setpoint_node_name`
        This optional field provides control over the heat recovery
        Using this triggers a model more suited to series bundle and chillers with higher temperature heat recovery
        If this field is not used, the bundles are modeled as being in parallel

        Args:
            value (str): value for IDD Field `heat_recovery_leaving_temperature_setpoint_node_name`
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
                                 'for field `heat_recovery_leaving_temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_leaving_temperature_setpoint_node_name`')

        self._data["Heat Recovery Leaving Temperature Setpoint Node Name"] = value

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
        out.append(self._to_str(self.reference_capacity))
        out.append(self._to_str(self.reference_cop))
        out.append(self._to_str(self.reference_leaving_chilled_water_temperature))
        out.append(self._to_str(self.reference_leaving_condenser_water_temperature))
        out.append(self._to_str(self.reference_chilled_water_flow_rate))
        out.append(self._to_str(self.reference_condenser_water_flow_rate))
        out.append(self._to_str(self.cooling_capacity_function_of_temperature_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.minimum_unloading_ratio))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.fraction_of_compressor_electric_consumption_rejected_by_condenser))
        out.append(self._to_str(self.leaving_chilled_water_lower_temperature_limit))
        out.append(self._to_str(self.chiller_flow_mode_type))
        out.append(self._to_str(self.design_heat_recovery_water_flow_rate))
        out.append(self._to_str(self.heat_recovery_inlet_node_name))
        out.append(self._to_str(self.heat_recovery_outlet_node_name))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.condenser_heat_recovery_relative_capacity_fraction))
        out.append(self._to_str(self.heat_recovery_inlet_high_temperature_limit_schedule_name))
        out.append(self._to_str(self.heat_recovery_leaving_temperature_setpoint_node_name))
        return ",".join(out)

class ChillerElectric(object):
    """ Corresponds to IDD object `Chiller:Electric`
        This chiller model is the empirical model from the Building Loads
        and System Thermodynamics (BLAST) program.  Chiller performance
        curves are generated by fitting catalog data to third order
        polynomial equations.  Three sets of coefficients are required.
    """
    internal_name = "Chiller:Electric"
    field_count = 37

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:Electric`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Condenser Type"] = None
        self._data["Nominal Capacity"] = None
        self._data["Nominal COP"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Design Condenser Inlet Temperature"] = None
        self._data["Temperature Rise Coefficient"] = None
        self._data["Design Chilled Water Outlet Temperature"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Fluid Flow Rate"] = None
        self._data["Coefficient 1 of Capacity Ratio Curve"] = None
        self._data["Coefficient 2 of Capacity Ratio Curve"] = None
        self._data["Coefficient 3 of Capacity Ratio Curve"] = None
        self._data["Coefficient 1 of Power Ratio Curve"] = None
        self._data["Coefficient 2 of Power Ratio Curve"] = None
        self._data["Coefficient 3 of Power Ratio Curve"] = None
        self._data["Coefficient 1 of Full Load Ratio Curve"] = None
        self._data["Coefficient 2 of Full Load Ratio Curve"] = None
        self._data["Coefficient 3 of Full Load Ratio Curve"] = None
        self._data["Chilled Water Outlet Temperature Lower Limit"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Design Heat Recovery Water Flow Rate"] = None
        self._data["Heat Recovery Inlet Node Name"] = None
        self._data["Heat Recovery Outlet Node Name"] = None
        self._data["Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Condenser Heat Recovery Relative Capacity Fraction"] = None
        self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"] = None
        self._data["Heat Recovery Leaving Temperature Setpoint Node Name"] = None

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
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cop = None
        else:
            self.nominal_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_inlet_temperature = None
        else:
            self.design_condenser_inlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_rise_coefficient = None
        else:
            self.temperature_rise_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_outlet_temperature = None
        else:
            self.design_chilled_water_outlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_fluid_flow_rate = None
        else:
            self.design_condenser_fluid_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_capacity_ratio_curve = None
        else:
            self.coefficient_1_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_capacity_ratio_curve = None
        else:
            self.coefficient_2_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_capacity_ratio_curve = None
        else:
            self.coefficient_3_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_power_ratio_curve = None
        else:
            self.coefficient_1_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_power_ratio_curve = None
        else:
            self.coefficient_2_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_power_ratio_curve = None
        else:
            self.coefficient_3_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_full_load_ratio_curve = None
        else:
            self.coefficient_1_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_full_load_ratio_curve = None
        else:
            self.coefficient_2_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_full_load_ratio_curve = None
        else:
            self.coefficient_3_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_temperature_lower_limit = None
        else:
            self.chilled_water_outlet_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_heat_recovery_water_flow_rate = None
        else:
            self.design_heat_recovery_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_node_name = None
        else:
            self.heat_recovery_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_outlet_node_name = None
        else:
            self.heat_recovery_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_heat_recovery_relative_capacity_fraction = None
        else:
            self.condenser_heat_recovery_relative_capacity_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_high_temperature_limit_schedule_name = None
        else:
            self.heat_recovery_inlet_high_temperature_limit_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_leaving_temperature_setpoint_node_name = None
        else:
            self.heat_recovery_leaving_temperature_setpoint_node_name = vals[i]
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
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """  Corresponds to IDD Field `condenser_type`

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - WaterCooled
                      - EvaporativelyCooled
                Default value: AirCooled
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
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            vals = set()
            vals.add("AirCooled")
            vals.add("WaterCooled")
            vals.add("EvaporativelyCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

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

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def nominal_cop(self):
        """Get nominal_cop

        Returns:
            float: the value of `nominal_cop` or None if not set
        """
        return self._data["Nominal COP"]

    @nominal_cop.setter
    def nominal_cop(self, value=None):
        """  Corresponds to IDD Field `nominal_cop`

        Args:
            value (float): value for IDD Field `nominal_cop`
                Unit: W/W
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
                                 'for field `nominal_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_cop`')

        self._data["Nominal COP"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_part_load_ratio`

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `optimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def design_condenser_inlet_temperature(self):
        """Get design_condenser_inlet_temperature

        Returns:
            float: the value of `design_condenser_inlet_temperature` or None if not set
        """
        return self._data["Design Condenser Inlet Temperature"]

    @design_condenser_inlet_temperature.setter
    def design_condenser_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `design_condenser_inlet_temperature`

        Args:
            value (float): value for IDD Field `design_condenser_inlet_temperature`
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
                                 'for field `design_condenser_inlet_temperature`'.format(value))

        self._data["Design Condenser Inlet Temperature"] = value

    @property
    def temperature_rise_coefficient(self):
        """Get temperature_rise_coefficient

        Returns:
            float: the value of `temperature_rise_coefficient` or None if not set
        """
        return self._data["Temperature Rise Coefficient"]

    @temperature_rise_coefficient.setter
    def temperature_rise_coefficient(self, value=None):
        """  Corresponds to IDD Field `temperature_rise_coefficient`

        Args:
            value (float): value for IDD Field `temperature_rise_coefficient`
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
                                 'for field `temperature_rise_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_rise_coefficient`')

        self._data["Temperature Rise Coefficient"] = value

    @property
    def design_chilled_water_outlet_temperature(self):
        """Get design_chilled_water_outlet_temperature

        Returns:
            float: the value of `design_chilled_water_outlet_temperature` or None if not set
        """
        return self._data["Design Chilled Water Outlet Temperature"]

    @design_chilled_water_outlet_temperature.setter
    def design_chilled_water_outlet_temperature(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_outlet_temperature`

        Args:
            value (float): value for IDD Field `design_chilled_water_outlet_temperature`
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
                                 'for field `design_chilled_water_outlet_temperature`'.format(value))

        self._data["Design Chilled Water Outlet Temperature"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable volume this is the maximum flow & for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
                Unit: m3/s
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_chilled_water_flow_rate`')

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_fluid_flow_rate(self):
        """Get design_condenser_fluid_flow_rate

        Returns:
            float: the value of `design_condenser_fluid_flow_rate` or None if not set
        """
        return self._data["Design Condenser Fluid Flow Rate"]

    @design_condenser_fluid_flow_rate.setter
    def design_condenser_fluid_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_fluid_flow_rate`
        This field is only used for Condenser Type = AirCooled or EvaporativelyCooled
        when Heat Recovery is specified

        Args:
            value (float): value for IDD Field `design_condenser_fluid_flow_rate`
                Unit: m3/s
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
                                 'for field `design_condenser_fluid_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_condenser_fluid_flow_rate`')

        self._data["Design Condenser Fluid Flow Rate"] = value

    @property
    def coefficient_1_of_capacity_ratio_curve(self):
        """Get coefficient_1_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Capacity Ratio Curve"]

    @coefficient_1_of_capacity_ratio_curve.setter
    def coefficient_1_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_capacity_ratio_curve`
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
                                 'for field `coefficient_1_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Capacity Ratio Curve"] = value

    @property
    def coefficient_2_of_capacity_ratio_curve(self):
        """Get coefficient_2_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Capacity Ratio Curve"]

    @coefficient_2_of_capacity_ratio_curve.setter
    def coefficient_2_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_capacity_ratio_curve`
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
                                 'for field `coefficient_2_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Capacity Ratio Curve"] = value

    @property
    def coefficient_3_of_capacity_ratio_curve(self):
        """Get coefficient_3_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Capacity Ratio Curve"]

    @coefficient_3_of_capacity_ratio_curve.setter
    def coefficient_3_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_capacity_ratio_curve`
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
                                 'for field `coefficient_3_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Capacity Ratio Curve"] = value

    @property
    def coefficient_1_of_power_ratio_curve(self):
        """Get coefficient_1_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Power Ratio Curve"]

    @coefficient_1_of_power_ratio_curve.setter
    def coefficient_1_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_power_ratio_curve`
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
                                 'for field `coefficient_1_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Power Ratio Curve"] = value

    @property
    def coefficient_2_of_power_ratio_curve(self):
        """Get coefficient_2_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Power Ratio Curve"]

    @coefficient_2_of_power_ratio_curve.setter
    def coefficient_2_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_power_ratio_curve`
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
                                 'for field `coefficient_2_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Power Ratio Curve"] = value

    @property
    def coefficient_3_of_power_ratio_curve(self):
        """Get coefficient_3_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Power Ratio Curve"]

    @coefficient_3_of_power_ratio_curve.setter
    def coefficient_3_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_power_ratio_curve`
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
                                 'for field `coefficient_3_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Power Ratio Curve"] = value

    @property
    def coefficient_1_of_full_load_ratio_curve(self):
        """Get coefficient_1_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Full Load Ratio Curve"]

    @coefficient_1_of_full_load_ratio_curve.setter
    def coefficient_1_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_full_load_ratio_curve`
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
                                 'for field `coefficient_1_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Full Load Ratio Curve"] = value

    @property
    def coefficient_2_of_full_load_ratio_curve(self):
        """Get coefficient_2_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Full Load Ratio Curve"]

    @coefficient_2_of_full_load_ratio_curve.setter
    def coefficient_2_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_full_load_ratio_curve`
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
                                 'for field `coefficient_2_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Full Load Ratio Curve"] = value

    @property
    def coefficient_3_of_full_load_ratio_curve(self):
        """Get coefficient_3_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Full Load Ratio Curve"]

    @coefficient_3_of_full_load_ratio_curve.setter
    def coefficient_3_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_full_load_ratio_curve`
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
                                 'for field `coefficient_3_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Full Load Ratio Curve"] = value

    @property
    def chilled_water_outlet_temperature_lower_limit(self):
        """Get chilled_water_outlet_temperature_lower_limit

        Returns:
            float: the value of `chilled_water_outlet_temperature_lower_limit` or None if not set
        """
        return self._data["Chilled Water Outlet Temperature Lower Limit"]

    @chilled_water_outlet_temperature_lower_limit.setter
    def chilled_water_outlet_temperature_lower_limit(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_temperature_lower_limit`

        Args:
            value (float): value for IDD Field `chilled_water_outlet_temperature_lower_limit`
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
                                 'for field `chilled_water_outlet_temperature_lower_limit`'.format(value))

        self._data["Chilled Water Outlet Temperature Lower Limit"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode`'.format(value))

        self._data["Chiller Flow Mode"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """Get design_heat_recovery_water_flow_rate

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self._data["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_heat_recovery_water_flow_rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.

        Args:
            value (float): value for IDD Field `design_heat_recovery_water_flow_rate`
                Unit: m3/s
                Default value: 0.0
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
                                 'for field `design_heat_recovery_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_heat_recovery_water_flow_rate`')

        self._data["Design Heat Recovery Water Flow Rate"] = value

    @property
    def heat_recovery_inlet_node_name(self):
        """Get heat_recovery_inlet_node_name

        Returns:
            str: the value of `heat_recovery_inlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Inlet Node Name"]

    @heat_recovery_inlet_node_name.setter
    def heat_recovery_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_node_name`
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
                                 'for field `heat_recovery_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_node_name`')

        self._data["Heat Recovery Inlet Node Name"] = value

    @property
    def heat_recovery_outlet_node_name(self):
        """Get heat_recovery_outlet_node_name

        Returns:
            str: the value of `heat_recovery_outlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Outlet Node Name"]

    @heat_recovery_outlet_node_name.setter
    def heat_recovery_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_outlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_outlet_node_name`
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
                                 'for field `heat_recovery_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_outlet_node_name`')

        self._data["Heat Recovery Outlet Node Name"] = value

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
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `basin_heater_capacity`
        This field is only used for Condenser Type = EvaporativelyCooled and for periods
        when the basin heater is available (field Basin Heater Operating Schedule Name).
        For this situation, the heater maintains the basin water temperature at the basin heater
        setpoint temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when the chiller is not operating.

        Args:
            value (float): value for IDD Field `basin_heater_capacity`
                Unit: W/K
                Default value: 0.0
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')

        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `basin_heater_setpoint_temperature`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Enter the outdoor dry-bulb temperature when the basin heater turns on.

        Args:
            value (float): value for IDD Field `basin_heater_setpoint_temperature`
                Unit: C
                Default value: 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')

        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `basin_heater_operating_schedule_name`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `basin_heater_operating_schedule_name`
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
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')

        self._data["Basin Heater Operating Schedule Name"] = value

    @property
    def condenser_heat_recovery_relative_capacity_fraction(self):
        """Get condenser_heat_recovery_relative_capacity_fraction

        Returns:
            float: the value of `condenser_heat_recovery_relative_capacity_fraction` or None if not set
        """
        return self._data["Condenser Heat Recovery Relative Capacity Fraction"]

    @condenser_heat_recovery_relative_capacity_fraction.setter
    def condenser_heat_recovery_relative_capacity_fraction(self, value=None):
        """  Corresponds to IDD Field `condenser_heat_recovery_relative_capacity_fraction`
        This optional field is the fraction of total rejected heat that can be recovered at full load

        Args:
            value (float): value for IDD Field `condenser_heat_recovery_relative_capacity_fraction`
                value >= 0.0
                value <= 1.0
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
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `condenser_heat_recovery_relative_capacity_fraction`')

        self._data["Condenser Heat Recovery Relative Capacity Fraction"] = value

    @property
    def heat_recovery_inlet_high_temperature_limit_schedule_name(self):
        """Get heat_recovery_inlet_high_temperature_limit_schedule_name

        Returns:
            str: the value of `heat_recovery_inlet_high_temperature_limit_schedule_name` or None if not set
        """
        return self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"]

    @heat_recovery_inlet_high_temperature_limit_schedule_name.setter
    def heat_recovery_inlet_high_temperature_limit_schedule_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_high_temperature_limit_schedule_name`
        This optional schedule of temperatures will turn off heat recovery if inlet exceeds the value

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_high_temperature_limit_schedule_name`
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
                                 'for field `heat_recovery_inlet_high_temperature_limit_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_high_temperature_limit_schedule_name`')

        self._data["Heat Recovery Inlet High Temperature Limit Schedule Name"] = value

    @property
    def heat_recovery_leaving_temperature_setpoint_node_name(self):
        """Get heat_recovery_leaving_temperature_setpoint_node_name

        Returns:
            str: the value of `heat_recovery_leaving_temperature_setpoint_node_name` or None if not set
        """
        return self._data["Heat Recovery Leaving Temperature Setpoint Node Name"]

    @heat_recovery_leaving_temperature_setpoint_node_name.setter
    def heat_recovery_leaving_temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_leaving_temperature_setpoint_node_name`
        This optional field provides control over the heat recovery
        Using this triggers a model more suited to series bundle and chillers with higher temperature heat recovery
        If this field is not used, the bundles are modeled as being in parallel

        Args:
            value (str): value for IDD Field `heat_recovery_leaving_temperature_setpoint_node_name`
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
                                 'for field `heat_recovery_leaving_temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_leaving_temperature_setpoint_node_name`')

        self._data["Heat Recovery Leaving Temperature Setpoint Node Name"] = value

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
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.nominal_cop))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.design_condenser_inlet_temperature))
        out.append(self._to_str(self.temperature_rise_coefficient))
        out.append(self._to_str(self.design_chilled_water_outlet_temperature))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_fluid_flow_rate))
        out.append(self._to_str(self.coefficient_1_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_1_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_1_of_full_load_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_full_load_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_full_load_ratio_curve))
        out.append(self._to_str(self.chilled_water_outlet_temperature_lower_limit))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.design_heat_recovery_water_flow_rate))
        out.append(self._to_str(self.heat_recovery_inlet_node_name))
        out.append(self._to_str(self.heat_recovery_outlet_node_name))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        out.append(self._to_str(self.condenser_heat_recovery_relative_capacity_fraction))
        out.append(self._to_str(self.heat_recovery_inlet_high_temperature_limit_schedule_name))
        out.append(self._to_str(self.heat_recovery_leaving_temperature_setpoint_node_name))
        return ",".join(out)

class ChillerAbsorptionIndirect(object):
    """ Corresponds to IDD object `Chiller:Absorption:Indirect`
        This indirect absorption chiller model is an enhanced model from the
        Building Loads and System Thermodynamics (BLAST) program.  Chiller
        performance curves are generated by fitting catalog data to third order
        polynomial equations. The chiller capacity is a function of condenser,
        chilled water, and generator temperatures. The heat input is a function
        of part-load ratio, condenser temperature, and chilled water temperature.
    """
    internal_name = "Chiller:Absorption:Indirect"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:Absorption:Indirect`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Nominal Capacity"] = None
        self._data["Nominal Pumping Power"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Design Condenser Inlet Temperature"] = None
        self._data["Condenser Inlet Temperature Lower Limit"] = None
        self._data["Chilled Water Outlet Temperature Lower Limit"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Generator Heat Input Function of Part Load Ratio Curve Name"] = None
        self._data["Pump Electric Input Function of Part Load Ratio Curve Name"] = None
        self._data["Generator Inlet Node Name"] = None
        self._data["Generator Outlet Node Name"] = None
        self._data["Capacity Correction Function of Condenser Temperature Curve Name"] = None
        self._data["Capacity Correction Function of Chilled Water Temperature Curve Name"] = None
        self._data["Capacity Correction Function of Generator Temperature Curve Name"] = None
        self._data["Generator Heat Input Correction Function of Condenser Temperature Curve Name"] = None
        self._data["Generator Heat Input Correction Function of Chilled Water Temperature Curve Name"] = None
        self._data["Generator Heat Source Type"] = None
        self._data["Design Generator Fluid Flow Rate"] = None
        self._data["Temperature Lower Limit Generator Inlet"] = None
        self._data["Degree of Subcooling in Steam Generator"] = None
        self._data["Degree of Subcooling in Steam Condensate Loop"] = None
        self._data["Sizing Factor"] = None

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
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_pumping_power = None
        else:
            self.nominal_pumping_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_inlet_temperature = None
        else:
            self.design_condenser_inlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_temperature_lower_limit = None
        else:
            self.condenser_inlet_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_temperature_lower_limit = None
        else:
            self.chilled_water_outlet_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_water_flow_rate = None
        else:
            self.design_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_heat_input_function_of_part_load_ratio_curve_name = None
        else:
            self.generator_heat_input_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_electric_input_function_of_part_load_ratio_curve_name = None
        else:
            self.pump_electric_input_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_inlet_node_name = None
        else:
            self.generator_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_outlet_node_name = None
        else:
            self.generator_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_correction_function_of_condenser_temperature_curve_name = None
        else:
            self.capacity_correction_function_of_condenser_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_correction_function_of_chilled_water_temperature_curve_name = None
        else:
            self.capacity_correction_function_of_chilled_water_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_correction_function_of_generator_temperature_curve_name = None
        else:
            self.capacity_correction_function_of_generator_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_heat_input_correction_function_of_condenser_temperature_curve_name = None
        else:
            self.generator_heat_input_correction_function_of_condenser_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_heat_input_correction_function_of_chilled_water_temperature_curve_name = None
        else:
            self.generator_heat_input_correction_function_of_chilled_water_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_heat_source_type = None
        else:
            self.generator_heat_source_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_generator_fluid_flow_rate = None
        else:
            self.design_generator_fluid_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_lower_limit_generator_inlet = None
        else:
            self.temperature_lower_limit_generator_inlet = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.degree_of_subcooling_in_steam_generator = None
        else:
            self.degree_of_subcooling_in_steam_generator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.degree_of_subcooling_in_steam_condensate_loop = None
        else:
            self.degree_of_subcooling_in_steam_condensate_loop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
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
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`

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
    def nominal_pumping_power(self):
        """Get nominal_pumping_power

        Returns:
            float: the value of `nominal_pumping_power` or None if not set
        """
        return self._data["Nominal Pumping Power"]

    @nominal_pumping_power.setter
    def nominal_pumping_power(self, value=None):
        """  Corresponds to IDD Field `nominal_pumping_power`

        Args:
            value (float): value for IDD Field `nominal_pumping_power`
                Unit: W
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
                                 'for field `nominal_pumping_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_pumping_power`')

        self._data["Nominal Pumping Power"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_part_load_ratio`

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `optimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def design_condenser_inlet_temperature(self):
        """Get design_condenser_inlet_temperature

        Returns:
            float: the value of `design_condenser_inlet_temperature` or None if not set
        """
        return self._data["Design Condenser Inlet Temperature"]

    @design_condenser_inlet_temperature.setter
    def design_condenser_inlet_temperature(self, value=30.0 ):
        """  Corresponds to IDD Field `design_condenser_inlet_temperature`
        Used only when condenser flow rate is autosized.

        Args:
            value (float): value for IDD Field `design_condenser_inlet_temperature`
                Unit: C
                Default value: 30.0
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
                                 'for field `design_condenser_inlet_temperature`'.format(value))

        self._data["Design Condenser Inlet Temperature"] = value

    @property
    def condenser_inlet_temperature_lower_limit(self):
        """Get condenser_inlet_temperature_lower_limit

        Returns:
            float: the value of `condenser_inlet_temperature_lower_limit` or None if not set
        """
        return self._data["Condenser Inlet Temperature Lower Limit"]

    @condenser_inlet_temperature_lower_limit.setter
    def condenser_inlet_temperature_lower_limit(self, value=15.0 ):
        """  Corresponds to IDD Field `condenser_inlet_temperature_lower_limit`
        Provides warnings when entering condenser temperature is below minimum.
        Capacity is not adjusted when entering condenser temperature is below minimum.

        Args:
            value (float): value for IDD Field `condenser_inlet_temperature_lower_limit`
                Unit: C
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
                                 'for field `condenser_inlet_temperature_lower_limit`'.format(value))

        self._data["Condenser Inlet Temperature Lower Limit"] = value

    @property
    def chilled_water_outlet_temperature_lower_limit(self):
        """Get chilled_water_outlet_temperature_lower_limit

        Returns:
            float: the value of `chilled_water_outlet_temperature_lower_limit` or None if not set
        """
        return self._data["Chilled Water Outlet Temperature Lower Limit"]

    @chilled_water_outlet_temperature_lower_limit.setter
    def chilled_water_outlet_temperature_lower_limit(self, value=5.0 ):
        """  Corresponds to IDD Field `chilled_water_outlet_temperature_lower_limit`
        Capacity is adjusted when leaving chilled water temperature is below minimum.

        Args:
            value (float): value for IDD Field `chilled_water_outlet_temperature_lower_limit`
                Unit: C
                Default value: 5.0
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
                                 'for field `chilled_water_outlet_temperature_lower_limit`'.format(value))

        self._data["Chilled Water Outlet Temperature Lower Limit"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable flow this is the max flow & for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_chilled_water_flow_rate`')

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_water_flow_rate(self):
        """Get design_condenser_water_flow_rate

        Returns:
            float: the value of `design_condenser_water_flow_rate` or None if not set
        """
        return self._data["Design Condenser Water Flow Rate"]

    @design_condenser_water_flow_rate.setter
    def design_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_water_flow_rate`

        Args:
            value (float): value for IDD Field `design_condenser_water_flow_rate`
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
                                 'for field `design_condenser_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_condenser_water_flow_rate`')

        self._data["Design Condenser Water Flow Rate"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode`'.format(value))

        self._data["Chiller Flow Mode"] = value

    @property
    def generator_heat_input_function_of_part_load_ratio_curve_name(self):
        """Get generator_heat_input_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `generator_heat_input_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Generator Heat Input Function of Part Load Ratio Curve Name"]

    @generator_heat_input_function_of_part_load_ratio_curve_name.setter
    def generator_heat_input_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `generator_heat_input_function_of_part_load_ratio_curve_name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `generator_heat_input_function_of_part_load_ratio_curve_name`
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
                                 'for field `generator_heat_input_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_heat_input_function_of_part_load_ratio_curve_name`')

        self._data["Generator Heat Input Function of Part Load Ratio Curve Name"] = value

    @property
    def pump_electric_input_function_of_part_load_ratio_curve_name(self):
        """Get pump_electric_input_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `pump_electric_input_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Pump Electric Input Function of Part Load Ratio Curve Name"]

    @pump_electric_input_function_of_part_load_ratio_curve_name.setter
    def pump_electric_input_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `pump_electric_input_function_of_part_load_ratio_curve_name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `pump_electric_input_function_of_part_load_ratio_curve_name`
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
                                 'for field `pump_electric_input_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_electric_input_function_of_part_load_ratio_curve_name`')

        self._data["Pump Electric Input Function of Part Load Ratio Curve Name"] = value

    @property
    def generator_inlet_node_name(self):
        """Get generator_inlet_node_name

        Returns:
            str: the value of `generator_inlet_node_name` or None if not set
        """
        return self._data["Generator Inlet Node Name"]

    @generator_inlet_node_name.setter
    def generator_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `generator_inlet_node_name`
        Enter the generator inlet node name which connects this chiller to a
        steam or hot water plant, otherwise leave this field blank.
        Generator nodes are used to model heat input to the chiller.

        Args:
            value (str): value for IDD Field `generator_inlet_node_name`
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
                                 'for field `generator_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_inlet_node_name`')

        self._data["Generator Inlet Node Name"] = value

    @property
    def generator_outlet_node_name(self):
        """Get generator_outlet_node_name

        Returns:
            str: the value of `generator_outlet_node_name` or None if not set
        """
        return self._data["Generator Outlet Node Name"]

    @generator_outlet_node_name.setter
    def generator_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `generator_outlet_node_name`
        Enter the generator outlet node name which connects this chiller to a
        steam or hot water plant, otherwise leave this field blank.
        Generator nodes are used to model heat input to the chiller.

        Args:
            value (str): value for IDD Field `generator_outlet_node_name`
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
                                 'for field `generator_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_outlet_node_name`')

        self._data["Generator Outlet Node Name"] = value

    @property
    def capacity_correction_function_of_condenser_temperature_curve_name(self):
        """Get capacity_correction_function_of_condenser_temperature_curve_name

        Returns:
            str: the value of `capacity_correction_function_of_condenser_temperature_curve_name` or None if not set
        """
        return self._data["Capacity Correction Function of Condenser Temperature Curve Name"]

    @capacity_correction_function_of_condenser_temperature_curve_name.setter
    def capacity_correction_function_of_condenser_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `capacity_correction_function_of_condenser_temperature_curve_name`
        Table:OneIndependentVariable object can also be used
        Curve which shows the change in normailized capacity to changes in condenser temperature.

        Args:
            value (str): value for IDD Field `capacity_correction_function_of_condenser_temperature_curve_name`
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
                                 'for field `capacity_correction_function_of_condenser_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_correction_function_of_condenser_temperature_curve_name`')

        self._data["Capacity Correction Function of Condenser Temperature Curve Name"] = value

    @property
    def capacity_correction_function_of_chilled_water_temperature_curve_name(self):
        """Get capacity_correction_function_of_chilled_water_temperature_curve_name

        Returns:
            str: the value of `capacity_correction_function_of_chilled_water_temperature_curve_name` or None if not set
        """
        return self._data["Capacity Correction Function of Chilled Water Temperature Curve Name"]

    @capacity_correction_function_of_chilled_water_temperature_curve_name.setter
    def capacity_correction_function_of_chilled_water_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `capacity_correction_function_of_chilled_water_temperature_curve_name`
        Table:OneIndependentVariable object can also be used
        Curve which shows the change in normailized capacity to changes in leaving chilled water temperature.

        Args:
            value (str): value for IDD Field `capacity_correction_function_of_chilled_water_temperature_curve_name`
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
                                 'for field `capacity_correction_function_of_chilled_water_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_correction_function_of_chilled_water_temperature_curve_name`')

        self._data["Capacity Correction Function of Chilled Water Temperature Curve Name"] = value

    @property
    def capacity_correction_function_of_generator_temperature_curve_name(self):
        """Get capacity_correction_function_of_generator_temperature_curve_name

        Returns:
            str: the value of `capacity_correction_function_of_generator_temperature_curve_name` or None if not set
        """
        return self._data["Capacity Correction Function of Generator Temperature Curve Name"]

    @capacity_correction_function_of_generator_temperature_curve_name.setter
    def capacity_correction_function_of_generator_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `capacity_correction_function_of_generator_temperature_curve_name`
        Table:OneIndependentVariable object can also be used
        Used when generator fluid type is hot water
        Curve which shows the change in normailized capacity to changes in generator temperature.

        Args:
            value (str): value for IDD Field `capacity_correction_function_of_generator_temperature_curve_name`
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
                                 'for field `capacity_correction_function_of_generator_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_correction_function_of_generator_temperature_curve_name`')

        self._data["Capacity Correction Function of Generator Temperature Curve Name"] = value

    @property
    def generator_heat_input_correction_function_of_condenser_temperature_curve_name(self):
        """Get generator_heat_input_correction_function_of_condenser_temperature_curve_name

        Returns:
            str: the value of `generator_heat_input_correction_function_of_condenser_temperature_curve_name` or None if not set
        """
        return self._data["Generator Heat Input Correction Function of Condenser Temperature Curve Name"]

    @generator_heat_input_correction_function_of_condenser_temperature_curve_name.setter
    def generator_heat_input_correction_function_of_condenser_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `generator_heat_input_correction_function_of_condenser_temperature_curve_name`
        Table:OneIndependentVariable object can also be used
        Curve which shows the change in normailized heat input to changes in condenser temperature.

        Args:
            value (str): value for IDD Field `generator_heat_input_correction_function_of_condenser_temperature_curve_name`
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
                                 'for field `generator_heat_input_correction_function_of_condenser_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_heat_input_correction_function_of_condenser_temperature_curve_name`')

        self._data["Generator Heat Input Correction Function of Condenser Temperature Curve Name"] = value

    @property
    def generator_heat_input_correction_function_of_chilled_water_temperature_curve_name(self):
        """Get generator_heat_input_correction_function_of_chilled_water_temperature_curve_name

        Returns:
            str: the value of `generator_heat_input_correction_function_of_chilled_water_temperature_curve_name` or None if not set
        """
        return self._data["Generator Heat Input Correction Function of Chilled Water Temperature Curve Name"]

    @generator_heat_input_correction_function_of_chilled_water_temperature_curve_name.setter
    def generator_heat_input_correction_function_of_chilled_water_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `generator_heat_input_correction_function_of_chilled_water_temperature_curve_name`
        Table:OneIndependentVariable object can also be used
        Curve which shows the change in normailized heat input to changes in leaving chilled water temperature.

        Args:
            value (str): value for IDD Field `generator_heat_input_correction_function_of_chilled_water_temperature_curve_name`
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
                                 'for field `generator_heat_input_correction_function_of_chilled_water_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_heat_input_correction_function_of_chilled_water_temperature_curve_name`')

        self._data["Generator Heat Input Correction Function of Chilled Water Temperature Curve Name"] = value

    @property
    def generator_heat_source_type(self):
        """Get generator_heat_source_type

        Returns:
            str: the value of `generator_heat_source_type` or None if not set
        """
        return self._data["Generator Heat Source Type"]

    @generator_heat_source_type.setter
    def generator_heat_source_type(self, value="Steam"):
        """  Corresponds to IDD Field `generator_heat_source_type`
        The Generator side of the chiller can be connected to a hot water or steam plant where the
        generator inlet and outlet nodes are connected to a plant loop. If the generator is not
        connected to a plant loop, and the generator inlet/outlet nodes are not used, this field should be
        specified as steam or left blank. When a plant is not used, the model assumes steam as the heat source.

        Args:
            value (str): value for IDD Field `generator_heat_source_type`
                Accepted values are:
                      - HotWater
                      - Steam
                Default value: Steam
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
                                 'for field `generator_heat_source_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_heat_source_type`')
            vals = set()
            vals.add("HotWater")
            vals.add("Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_heat_source_type`'.format(value))

        self._data["Generator Heat Source Type"] = value

    @property
    def design_generator_fluid_flow_rate(self):
        """Get design_generator_fluid_flow_rate

        Returns:
            float: the value of `design_generator_fluid_flow_rate` or None if not set
        """
        return self._data["Design Generator Fluid Flow Rate"]

    @design_generator_fluid_flow_rate.setter
    def design_generator_fluid_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_generator_fluid_flow_rate`
        For variable flow this is the max flow and for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_generator_fluid_flow_rate`
                Unit: m3/s
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
                                 'for field `design_generator_fluid_flow_rate`'.format(value))

        self._data["Design Generator Fluid Flow Rate"] = value

    @property
    def temperature_lower_limit_generator_inlet(self):
        """Get temperature_lower_limit_generator_inlet

        Returns:
            float: the value of `temperature_lower_limit_generator_inlet` or None if not set
        """
        return self._data["Temperature Lower Limit Generator Inlet"]

    @temperature_lower_limit_generator_inlet.setter
    def temperature_lower_limit_generator_inlet(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_lower_limit_generator_inlet`
        Provides warnings when entering generator temperature is below minimum.
        Capacity is not adjusted when entering generator temperature is below minimum.

        Args:
            value (float): value for IDD Field `temperature_lower_limit_generator_inlet`
                Unit: C
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
                                 'for field `temperature_lower_limit_generator_inlet`'.format(value))

        self._data["Temperature Lower Limit Generator Inlet"] = value

    @property
    def degree_of_subcooling_in_steam_generator(self):
        """Get degree_of_subcooling_in_steam_generator

        Returns:
            float: the value of `degree_of_subcooling_in_steam_generator` or None if not set
        """
        return self._data["Degree of Subcooling in Steam Generator"]

    @degree_of_subcooling_in_steam_generator.setter
    def degree_of_subcooling_in_steam_generator(self, value=1.0 ):
        """  Corresponds to IDD Field `degree_of_subcooling_in_steam_generator`
        This field is not used when the generator inlet/outlet nodes are not specified or
        the generator is connected to a hot water loop.

        Args:
            value (float): value for IDD Field `degree_of_subcooling_in_steam_generator`
                Unit: C
                Default value: 1.0
                value >= 0.0
                value <= 20.0
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
                                 'for field `degree_of_subcooling_in_steam_generator`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `degree_of_subcooling_in_steam_generator`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `degree_of_subcooling_in_steam_generator`')

        self._data["Degree of Subcooling in Steam Generator"] = value

    @property
    def degree_of_subcooling_in_steam_condensate_loop(self):
        """Get degree_of_subcooling_in_steam_condensate_loop

        Returns:
            float: the value of `degree_of_subcooling_in_steam_condensate_loop` or None if not set
        """
        return self._data["Degree of Subcooling in Steam Condensate Loop"]

    @degree_of_subcooling_in_steam_condensate_loop.setter
    def degree_of_subcooling_in_steam_condensate_loop(self, value=0.0 ):
        """  Corresponds to IDD Field `degree_of_subcooling_in_steam_condensate_loop`
        This field is not used when the generator inlet/outlet nodes are not specified or
        the generator is connected to a hot water loop.

        Args:
            value (float): value for IDD Field `degree_of_subcooling_in_steam_condensate_loop`
                Unit: C
                Default value: 0.0
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
                                 'for field `degree_of_subcooling_in_steam_condensate_loop`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `degree_of_subcooling_in_steam_condensate_loop`')

        self._data["Degree of Subcooling in Steam Condensate Loop"] = value

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
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.nominal_pumping_power))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.design_condenser_inlet_temperature))
        out.append(self._to_str(self.condenser_inlet_temperature_lower_limit))
        out.append(self._to_str(self.chilled_water_outlet_temperature_lower_limit))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.generator_heat_input_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.pump_electric_input_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.generator_inlet_node_name))
        out.append(self._to_str(self.generator_outlet_node_name))
        out.append(self._to_str(self.capacity_correction_function_of_condenser_temperature_curve_name))
        out.append(self._to_str(self.capacity_correction_function_of_chilled_water_temperature_curve_name))
        out.append(self._to_str(self.capacity_correction_function_of_generator_temperature_curve_name))
        out.append(self._to_str(self.generator_heat_input_correction_function_of_condenser_temperature_curve_name))
        out.append(self._to_str(self.generator_heat_input_correction_function_of_chilled_water_temperature_curve_name))
        out.append(self._to_str(self.generator_heat_source_type))
        out.append(self._to_str(self.design_generator_fluid_flow_rate))
        out.append(self._to_str(self.temperature_lower_limit_generator_inlet))
        out.append(self._to_str(self.degree_of_subcooling_in_steam_generator))
        out.append(self._to_str(self.degree_of_subcooling_in_steam_condensate_loop))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)

class ChillerAbsorption(object):
    """ Corresponds to IDD object `Chiller:Absorption`
        This indirect absorption chiller model is the empirical model from the
        Building Loads and System Thermodynamics (BLAST) program.  Chiller
        performance curves are generated by fitting catalog data to third order
        polynomial equations.  Two sets of coefficients are required.
    """
    internal_name = "Chiller:Absorption"
    field_count = 27

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:Absorption`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Nominal Capacity"] = None
        self._data["Nominal Pumping Power"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Design Condenser Inlet Temperature"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Coefficient 1 of the Hot Water or Steam Use Part Load Ratio Curve"] = None
        self._data["Coefficient 2 of the Hot Water or Steam Use Part Load Ratio Curve"] = None
        self._data["Coefficient 3 of the Hot Water or Steam Use Part Load Ratio Curve"] = None
        self._data["Coefficient 1 of the Pump Electric Use Part Load Ratio Curve"] = None
        self._data["Coefficient 2 of the Pump Electric Use Part Load Ratio Curve"] = None
        self._data["Coefficient 3 of the Pump Electric Use Part Load Ratio Curve"] = None
        self._data["Chilled Water Outlet Temperature Lower Limit"] = None
        self._data["Generator Inlet Node Name"] = None
        self._data["Generator Outlet Node Name"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Generator Heat Source Type"] = None
        self._data["Design Generator Fluid Flow Rate"] = None
        self._data["Degree of Subcooling in Steam Generator"] = None
        self._data["Sizing Factor"] = None

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
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_pumping_power = None
        else:
            self.nominal_pumping_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_inlet_temperature = None
        else:
            self.design_condenser_inlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_water_flow_rate = None
        else:
            self.design_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve = None
        else:
            self.coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve = None
        else:
            self.coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve = None
        else:
            self.coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_the_pump_electric_use_part_load_ratio_curve = None
        else:
            self.coefficient_1_of_the_pump_electric_use_part_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_the_pump_electric_use_part_load_ratio_curve = None
        else:
            self.coefficient_2_of_the_pump_electric_use_part_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_the_pump_electric_use_part_load_ratio_curve = None
        else:
            self.coefficient_3_of_the_pump_electric_use_part_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_temperature_lower_limit = None
        else:
            self.chilled_water_outlet_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_inlet_node_name = None
        else:
            self.generator_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_outlet_node_name = None
        else:
            self.generator_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_heat_source_type = None
        else:
            self.generator_heat_source_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_generator_fluid_flow_rate = None
        else:
            self.design_generator_fluid_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.degree_of_subcooling_in_steam_generator = None
        else:
            self.degree_of_subcooling_in_steam_generator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
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
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`

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
    def nominal_pumping_power(self):
        """Get nominal_pumping_power

        Returns:
            float: the value of `nominal_pumping_power` or None if not set
        """
        return self._data["Nominal Pumping Power"]

    @nominal_pumping_power.setter
    def nominal_pumping_power(self, value=None):
        """  Corresponds to IDD Field `nominal_pumping_power`

        Args:
            value (float): value for IDD Field `nominal_pumping_power`
                Unit: W
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
                                 'for field `nominal_pumping_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_pumping_power`')

        self._data["Nominal Pumping Power"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_part_load_ratio`

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `optimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def design_condenser_inlet_temperature(self):
        """Get design_condenser_inlet_temperature

        Returns:
            float: the value of `design_condenser_inlet_temperature` or None if not set
        """
        return self._data["Design Condenser Inlet Temperature"]

    @design_condenser_inlet_temperature.setter
    def design_condenser_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `design_condenser_inlet_temperature`

        Args:
            value (float): value for IDD Field `design_condenser_inlet_temperature`
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
                                 'for field `design_condenser_inlet_temperature`'.format(value))

        self._data["Design Condenser Inlet Temperature"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable volume this is the max flow & for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_chilled_water_flow_rate`')

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_water_flow_rate(self):
        """Get design_condenser_water_flow_rate

        Returns:
            float: the value of `design_condenser_water_flow_rate` or None if not set
        """
        return self._data["Design Condenser Water Flow Rate"]

    @design_condenser_water_flow_rate.setter
    def design_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_water_flow_rate`
        The steam use coefficients below specify the
        steam use as a fraction of chiller operating capacity

        Args:
            value (float): value for IDD Field `design_condenser_water_flow_rate`
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
                                 'for field `design_condenser_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_condenser_water_flow_rate`')

        self._data["Design Condenser Water Flow Rate"] = value

    @property
    def coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve(self):
        """Get coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of the Hot Water or Steam Use Part Load Ratio Curve"]

    @coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve.setter
    def coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve`
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
                                 'for field `coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve`'.format(value))

        self._data["Coefficient 1 of the Hot Water or Steam Use Part Load Ratio Curve"] = value

    @property
    def coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve(self):
        """Get coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of the Hot Water or Steam Use Part Load Ratio Curve"]

    @coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve.setter
    def coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve`
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
                                 'for field `coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve`'.format(value))

        self._data["Coefficient 2 of the Hot Water or Steam Use Part Load Ratio Curve"] = value

    @property
    def coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve(self):
        """Get coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of the Hot Water or Steam Use Part Load Ratio Curve"]

    @coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve.setter
    def coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve`
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
                                 'for field `coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve`'.format(value))

        self._data["Coefficient 3 of the Hot Water or Steam Use Part Load Ratio Curve"] = value

    @property
    def coefficient_1_of_the_pump_electric_use_part_load_ratio_curve(self):
        """Get coefficient_1_of_the_pump_electric_use_part_load_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_the_pump_electric_use_part_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of the Pump Electric Use Part Load Ratio Curve"]

    @coefficient_1_of_the_pump_electric_use_part_load_ratio_curve.setter
    def coefficient_1_of_the_pump_electric_use_part_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_the_pump_electric_use_part_load_ratio_curve`
        The pump electric use coefficients specify the
        pumping power as a Fraction of Nominal pumping power

        Args:
            value (float): value for IDD Field `coefficient_1_of_the_pump_electric_use_part_load_ratio_curve`
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
                                 'for field `coefficient_1_of_the_pump_electric_use_part_load_ratio_curve`'.format(value))

        self._data["Coefficient 1 of the Pump Electric Use Part Load Ratio Curve"] = value

    @property
    def coefficient_2_of_the_pump_electric_use_part_load_ratio_curve(self):
        """Get coefficient_2_of_the_pump_electric_use_part_load_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_the_pump_electric_use_part_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of the Pump Electric Use Part Load Ratio Curve"]

    @coefficient_2_of_the_pump_electric_use_part_load_ratio_curve.setter
    def coefficient_2_of_the_pump_electric_use_part_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_the_pump_electric_use_part_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_the_pump_electric_use_part_load_ratio_curve`
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
                                 'for field `coefficient_2_of_the_pump_electric_use_part_load_ratio_curve`'.format(value))

        self._data["Coefficient 2 of the Pump Electric Use Part Load Ratio Curve"] = value

    @property
    def coefficient_3_of_the_pump_electric_use_part_load_ratio_curve(self):
        """Get coefficient_3_of_the_pump_electric_use_part_load_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_the_pump_electric_use_part_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of the Pump Electric Use Part Load Ratio Curve"]

    @coefficient_3_of_the_pump_electric_use_part_load_ratio_curve.setter
    def coefficient_3_of_the_pump_electric_use_part_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_the_pump_electric_use_part_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_the_pump_electric_use_part_load_ratio_curve`
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
                                 'for field `coefficient_3_of_the_pump_electric_use_part_load_ratio_curve`'.format(value))

        self._data["Coefficient 3 of the Pump Electric Use Part Load Ratio Curve"] = value

    @property
    def chilled_water_outlet_temperature_lower_limit(self):
        """Get chilled_water_outlet_temperature_lower_limit

        Returns:
            float: the value of `chilled_water_outlet_temperature_lower_limit` or None if not set
        """
        return self._data["Chilled Water Outlet Temperature Lower Limit"]

    @chilled_water_outlet_temperature_lower_limit.setter
    def chilled_water_outlet_temperature_lower_limit(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_temperature_lower_limit`

        Args:
            value (float): value for IDD Field `chilled_water_outlet_temperature_lower_limit`
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
                                 'for field `chilled_water_outlet_temperature_lower_limit`'.format(value))

        self._data["Chilled Water Outlet Temperature Lower Limit"] = value

    @property
    def generator_inlet_node_name(self):
        """Get generator_inlet_node_name

        Returns:
            str: the value of `generator_inlet_node_name` or None if not set
        """
        return self._data["Generator Inlet Node Name"]

    @generator_inlet_node_name.setter
    def generator_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `generator_inlet_node_name`

        Args:
            value (str): value for IDD Field `generator_inlet_node_name`
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
                                 'for field `generator_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_inlet_node_name`')

        self._data["Generator Inlet Node Name"] = value

    @property
    def generator_outlet_node_name(self):
        """Get generator_outlet_node_name

        Returns:
            str: the value of `generator_outlet_node_name` or None if not set
        """
        return self._data["Generator Outlet Node Name"]

    @generator_outlet_node_name.setter
    def generator_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `generator_outlet_node_name`

        Args:
            value (str): value for IDD Field `generator_outlet_node_name`
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
                                 'for field `generator_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_outlet_node_name`')

        self._data["Generator Outlet Node Name"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode`'.format(value))

        self._data["Chiller Flow Mode"] = value

    @property
    def generator_heat_source_type(self):
        """Get generator_heat_source_type

        Returns:
            str: the value of `generator_heat_source_type` or None if not set
        """
        return self._data["Generator Heat Source Type"]

    @generator_heat_source_type.setter
    def generator_heat_source_type(self, value="Steam"):
        """  Corresponds to IDD Field `generator_heat_source_type`
        The Generator side of the chiller can be connected to a hot water or steam plant where the
        generator inlet and outlet nodes are connected to a plant loop. If the generator is not
        connected to a plant loop, and the generator inlet/outlet nodes are not used, this field should be
        specified as steam or left blank. When a plant is not used, the model assumes steam as the heat source.

        Args:
            value (str): value for IDD Field `generator_heat_source_type`
                Accepted values are:
                      - Steam
                      - HotWater
                Default value: Steam
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
                                 'for field `generator_heat_source_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_heat_source_type`')
            vals = set()
            vals.add("Steam")
            vals.add("HotWater")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_heat_source_type`'.format(value))

        self._data["Generator Heat Source Type"] = value

    @property
    def design_generator_fluid_flow_rate(self):
        """Get design_generator_fluid_flow_rate

        Returns:
            float: the value of `design_generator_fluid_flow_rate` or None if not set
        """
        return self._data["Design Generator Fluid Flow Rate"]

    @design_generator_fluid_flow_rate.setter
    def design_generator_fluid_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_generator_fluid_flow_rate`

        Args:
            value (float): value for IDD Field `design_generator_fluid_flow_rate`
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
                                 'for field `design_generator_fluid_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_generator_fluid_flow_rate`')

        self._data["Design Generator Fluid Flow Rate"] = value

    @property
    def degree_of_subcooling_in_steam_generator(self):
        """Get degree_of_subcooling_in_steam_generator

        Returns:
            float: the value of `degree_of_subcooling_in_steam_generator` or None if not set
        """
        return self._data["Degree of Subcooling in Steam Generator"]

    @degree_of_subcooling_in_steam_generator.setter
    def degree_of_subcooling_in_steam_generator(self, value=1.0 ):
        """  Corresponds to IDD Field `degree_of_subcooling_in_steam_generator`
        This field is not used when the generator inlet/outlet nodes are not specified or
        the generator is connected to a hot water loop.

        Args:
            value (float): value for IDD Field `degree_of_subcooling_in_steam_generator`
                Unit: C
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
                                 'for field `degree_of_subcooling_in_steam_generator`'.format(value))

        self._data["Degree of Subcooling in Steam Generator"] = value

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
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.nominal_pumping_power))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.design_condenser_inlet_temperature))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve))
        out.append(self._to_str(self.coefficient_1_of_the_pump_electric_use_part_load_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_the_pump_electric_use_part_load_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_the_pump_electric_use_part_load_ratio_curve))
        out.append(self._to_str(self.chilled_water_outlet_temperature_lower_limit))
        out.append(self._to_str(self.generator_inlet_node_name))
        out.append(self._to_str(self.generator_outlet_node_name))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.generator_heat_source_type))
        out.append(self._to_str(self.design_generator_fluid_flow_rate))
        out.append(self._to_str(self.degree_of_subcooling_in_steam_generator))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)

class ChillerConstantCop(object):
    """ Corresponds to IDD object `Chiller:ConstantCOP`
        This constant COP chiller model provides a means of quickly specifying a
        Chiller where performance data is not available.
    """
    internal_name = "Chiller:ConstantCOP"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:ConstantCOP`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Nominal Capacity"] = None
        self._data["Nominal COP"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Condenser Type"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None

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
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cop = None
        else:
            self.nominal_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_water_flow_rate = None
        else:
            self.design_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
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
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def nominal_cop(self):
        """Get nominal_cop

        Returns:
            float: the value of `nominal_cop` or None if not set
        """
        return self._data["Nominal COP"]

    @nominal_cop.setter
    def nominal_cop(self, value=None):
        """  Corresponds to IDD Field `nominal_cop`

        Args:
            value (float): value for IDD Field `nominal_cop`
                Unit: W/W
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
                                 'for field `nominal_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_cop`')

        self._data["Nominal COP"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable volume this is the maximum flow and for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
                Unit: m3/s
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_chilled_water_flow_rate`')

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_water_flow_rate(self):
        """Get design_condenser_water_flow_rate

        Returns:
            float: the value of `design_condenser_water_flow_rate` or None if not set
        """
        return self._data["Design Condenser Water Flow Rate"]

    @design_condenser_water_flow_rate.setter
    def design_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_water_flow_rate`
        This field is not used for Condenser Type = AirCooled or EvaporativelyCooled

        Args:
            value (float): value for IDD Field `design_condenser_water_flow_rate`
                Unit: m3/s
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
                                 'for field `design_condenser_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_condenser_water_flow_rate`')

        self._data["Design Condenser Water Flow Rate"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """  Corresponds to IDD Field `condenser_type`

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - WaterCooled
                      - EvaporativelyCooled
                Default value: AirCooled
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
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            vals = set()
            vals.add("AirCooled")
            vals.add("WaterCooled")
            vals.add("EvaporativelyCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode`'.format(value))

        self._data["Chiller Flow Mode"] = value

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
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `basin_heater_capacity`
        This field is only used for Condenser Type = EvaporativelyCooled and for periods
        when the basin heater is available (field Basin Heater Operating Schedule Name).
        For this situation, the heater maintains the basin water temperature at the basin heater
        setpoint temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when the chiller is not operating.

        Args:
            value (float): value for IDD Field `basin_heater_capacity`
                Unit: W/K
                Default value: 0.0
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')

        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `basin_heater_setpoint_temperature`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Enter the outdoor dry-bulb temperature when the basin heater turns on.

        Args:
            value (float): value for IDD Field `basin_heater_setpoint_temperature`
                Unit: C
                Default value: 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')

        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `basin_heater_operating_schedule_name`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `basin_heater_operating_schedule_name`
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
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')

        self._data["Basin Heater Operating Schedule Name"] = value

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
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.nominal_cop))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        return ",".join(out)

class ChillerEngineDriven(object):
    """ Corresponds to IDD object `Chiller:EngineDriven`
        This chiller model is the empirical model from the Building Loads
        and System Thermodynamics (BLAST) program.  Chiller performance
        curves are generated by fitting catalog data to third order
        polynomial equations.  Three sets of coefficients are required.
    """
    internal_name = "Chiller:EngineDriven"
    field_count = 46

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:EngineDriven`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Condenser Type"] = None
        self._data["Nominal Capacity"] = None
        self._data["Nominal COP"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Design Condenser Inlet Temperature"] = None
        self._data["Temperature Rise Coefficient"] = None
        self._data["Design Chilled Water Outlet Temperature"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Coefficient 1 of Capacity Ratio Curve"] = None
        self._data["Coefficient 2 of Capacity Ratio Curve"] = None
        self._data["Coefficient 3 of Capacity Ratio Curve"] = None
        self._data["Coefficient 1 of Power Ratio Curve"] = None
        self._data["Coefficient 2 of Power Ratio Curve"] = None
        self._data["Coefficient 3 of Power Ratio Curve"] = None
        self._data["Coefficient 1 of Full Load Ratio Curve"] = None
        self._data["Coefficient 2 of Full Load Ratio Curve"] = None
        self._data["Coefficient 3 of Full Load Ratio Curve"] = None
        self._data["Chilled Water Outlet Temperature Lower Limit"] = None
        self._data["Fuel Use Curve Name"] = None
        self._data["Jacket Heat Recovery Curve Name"] = None
        self._data["Lube Heat Recovery Curve Name"] = None
        self._data["Total Exhaust Energy Curve Name"] = None
        self._data["Exhaust Temperature Curve Name"] = None
        self._data["Coefficient 1 of U-Factor Times Area Curve"] = None
        self._data["Coefficient 2 of U-Factor Times Area Curve"] = None
        self._data["Maximum Exhaust Flow per Unit of Power Output"] = None
        self._data["Design Minimum Exhaust Temperature"] = None
        self._data["Fuel Type"] = None
        self._data["Fuel Higher Heating Value"] = None
        self._data["Design Heat Recovery Water Flow Rate"] = None
        self._data["Heat Recovery Inlet Node Name"] = None
        self._data["Heat Recovery Outlet Node Name"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Maximum Temperature for Heat Recovery at Heat Recovery Outlet Node"] = None
        self._data["Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None

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
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cop = None
        else:
            self.nominal_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_inlet_temperature = None
        else:
            self.design_condenser_inlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_rise_coefficient = None
        else:
            self.temperature_rise_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_outlet_temperature = None
        else:
            self.design_chilled_water_outlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_water_flow_rate = None
        else:
            self.design_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_capacity_ratio_curve = None
        else:
            self.coefficient_1_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_capacity_ratio_curve = None
        else:
            self.coefficient_2_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_capacity_ratio_curve = None
        else:
            self.coefficient_3_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_power_ratio_curve = None
        else:
            self.coefficient_1_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_power_ratio_curve = None
        else:
            self.coefficient_2_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_power_ratio_curve = None
        else:
            self.coefficient_3_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_full_load_ratio_curve = None
        else:
            self.coefficient_1_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_full_load_ratio_curve = None
        else:
            self.coefficient_2_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_full_load_ratio_curve = None
        else:
            self.coefficient_3_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_temperature_lower_limit = None
        else:
            self.chilled_water_outlet_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_use_curve_name = None
        else:
            self.fuel_use_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.jacket_heat_recovery_curve_name = None
        else:
            self.jacket_heat_recovery_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lube_heat_recovery_curve_name = None
        else:
            self.lube_heat_recovery_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_exhaust_energy_curve_name = None
        else:
            self.total_exhaust_energy_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_temperature_curve_name = None
        else:
            self.exhaust_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_ufactor_times_area_curve = None
        else:
            self.coefficient_1_of_ufactor_times_area_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_ufactor_times_area_curve = None
        else:
            self.coefficient_2_of_ufactor_times_area_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_exhaust_flow_per_unit_of_power_output = None
        else:
            self.maximum_exhaust_flow_per_unit_of_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_minimum_exhaust_temperature = None
        else:
            self.design_minimum_exhaust_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_higher_heating_value = None
        else:
            self.fuel_higher_heating_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_heat_recovery_water_flow_rate = None
        else:
            self.design_heat_recovery_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_node_name = None
        else:
            self.heat_recovery_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_outlet_node_name = None
        else:
            self.heat_recovery_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node = None
        else:
            self.maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
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
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """  Corresponds to IDD Field `condenser_type`

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - WaterCooled
                      - EvaporativelyCooled
                Default value: AirCooled
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
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            vals = set()
            vals.add("AirCooled")
            vals.add("WaterCooled")
            vals.add("EvaporativelyCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

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

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def nominal_cop(self):
        """Get nominal_cop

        Returns:
            float: the value of `nominal_cop` or None if not set
        """
        return self._data["Nominal COP"]

    @nominal_cop.setter
    def nominal_cop(self, value=None):
        """  Corresponds to IDD Field `nominal_cop`
        Nominal Refrigeration Cycle COP

        Args:
            value (float): value for IDD Field `nominal_cop`
                Unit: W/W
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
                                 'for field `nominal_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_cop`')

        self._data["Nominal COP"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_part_load_ratio`

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `optimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def design_condenser_inlet_temperature(self):
        """Get design_condenser_inlet_temperature

        Returns:
            float: the value of `design_condenser_inlet_temperature` or None if not set
        """
        return self._data["Design Condenser Inlet Temperature"]

    @design_condenser_inlet_temperature.setter
    def design_condenser_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `design_condenser_inlet_temperature`

        Args:
            value (float): value for IDD Field `design_condenser_inlet_temperature`
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
                                 'for field `design_condenser_inlet_temperature`'.format(value))

        self._data["Design Condenser Inlet Temperature"] = value

    @property
    def temperature_rise_coefficient(self):
        """Get temperature_rise_coefficient

        Returns:
            float: the value of `temperature_rise_coefficient` or None if not set
        """
        return self._data["Temperature Rise Coefficient"]

    @temperature_rise_coefficient.setter
    def temperature_rise_coefficient(self, value=None):
        """  Corresponds to IDD Field `temperature_rise_coefficient`

        Args:
            value (float): value for IDD Field `temperature_rise_coefficient`
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
                                 'for field `temperature_rise_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_rise_coefficient`')

        self._data["Temperature Rise Coefficient"] = value

    @property
    def design_chilled_water_outlet_temperature(self):
        """Get design_chilled_water_outlet_temperature

        Returns:
            float: the value of `design_chilled_water_outlet_temperature` or None if not set
        """
        return self._data["Design Chilled Water Outlet Temperature"]

    @design_chilled_water_outlet_temperature.setter
    def design_chilled_water_outlet_temperature(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_outlet_temperature`

        Args:
            value (float): value for IDD Field `design_chilled_water_outlet_temperature`
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
                                 'for field `design_chilled_water_outlet_temperature`'.format(value))

        self._data["Design Chilled Water Outlet Temperature"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable volume this is the maximum flow and for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
                Unit: m3/s
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_chilled_water_flow_rate`')

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_water_flow_rate(self):
        """Get design_condenser_water_flow_rate

        Returns:
            float: the value of `design_condenser_water_flow_rate` or None if not set
        """
        return self._data["Design Condenser Water Flow Rate"]

    @design_condenser_water_flow_rate.setter
    def design_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_water_flow_rate`
        This field is not used for Condenser Type = AirCooled or EvaporativelyCooled

        Args:
            value (float): value for IDD Field `design_condenser_water_flow_rate`
                Unit: m3/s
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
                                 'for field `design_condenser_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_condenser_water_flow_rate`')

        self._data["Design Condenser Water Flow Rate"] = value

    @property
    def coefficient_1_of_capacity_ratio_curve(self):
        """Get coefficient_1_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Capacity Ratio Curve"]

    @coefficient_1_of_capacity_ratio_curve.setter
    def coefficient_1_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_capacity_ratio_curve`
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
                                 'for field `coefficient_1_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Capacity Ratio Curve"] = value

    @property
    def coefficient_2_of_capacity_ratio_curve(self):
        """Get coefficient_2_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Capacity Ratio Curve"]

    @coefficient_2_of_capacity_ratio_curve.setter
    def coefficient_2_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_capacity_ratio_curve`
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
                                 'for field `coefficient_2_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Capacity Ratio Curve"] = value

    @property
    def coefficient_3_of_capacity_ratio_curve(self):
        """Get coefficient_3_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Capacity Ratio Curve"]

    @coefficient_3_of_capacity_ratio_curve.setter
    def coefficient_3_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_capacity_ratio_curve`
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
                                 'for field `coefficient_3_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Capacity Ratio Curve"] = value

    @property
    def coefficient_1_of_power_ratio_curve(self):
        """Get coefficient_1_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Power Ratio Curve"]

    @coefficient_1_of_power_ratio_curve.setter
    def coefficient_1_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_power_ratio_curve`
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
                                 'for field `coefficient_1_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Power Ratio Curve"] = value

    @property
    def coefficient_2_of_power_ratio_curve(self):
        """Get coefficient_2_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Power Ratio Curve"]

    @coefficient_2_of_power_ratio_curve.setter
    def coefficient_2_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_power_ratio_curve`
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
                                 'for field `coefficient_2_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Power Ratio Curve"] = value

    @property
    def coefficient_3_of_power_ratio_curve(self):
        """Get coefficient_3_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Power Ratio Curve"]

    @coefficient_3_of_power_ratio_curve.setter
    def coefficient_3_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_power_ratio_curve`
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
                                 'for field `coefficient_3_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Power Ratio Curve"] = value

    @property
    def coefficient_1_of_full_load_ratio_curve(self):
        """Get coefficient_1_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Full Load Ratio Curve"]

    @coefficient_1_of_full_load_ratio_curve.setter
    def coefficient_1_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_full_load_ratio_curve`
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
                                 'for field `coefficient_1_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Full Load Ratio Curve"] = value

    @property
    def coefficient_2_of_full_load_ratio_curve(self):
        """Get coefficient_2_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Full Load Ratio Curve"]

    @coefficient_2_of_full_load_ratio_curve.setter
    def coefficient_2_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_full_load_ratio_curve`
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
                                 'for field `coefficient_2_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Full Load Ratio Curve"] = value

    @property
    def coefficient_3_of_full_load_ratio_curve(self):
        """Get coefficient_3_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Full Load Ratio Curve"]

    @coefficient_3_of_full_load_ratio_curve.setter
    def coefficient_3_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_full_load_ratio_curve`
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
                                 'for field `coefficient_3_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Full Load Ratio Curve"] = value

    @property
    def chilled_water_outlet_temperature_lower_limit(self):
        """Get chilled_water_outlet_temperature_lower_limit

        Returns:
            float: the value of `chilled_water_outlet_temperature_lower_limit` or None if not set
        """
        return self._data["Chilled Water Outlet Temperature Lower Limit"]

    @chilled_water_outlet_temperature_lower_limit.setter
    def chilled_water_outlet_temperature_lower_limit(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_temperature_lower_limit`
        Special EngineDriven Chiller Parameters Below

        Args:
            value (float): value for IDD Field `chilled_water_outlet_temperature_lower_limit`
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
                                 'for field `chilled_water_outlet_temperature_lower_limit`'.format(value))

        self._data["Chilled Water Outlet Temperature Lower Limit"] = value

    @property
    def fuel_use_curve_name(self):
        """Get fuel_use_curve_name

        Returns:
            str: the value of `fuel_use_curve_name` or None if not set
        """
        return self._data["Fuel Use Curve Name"]

    @fuel_use_curve_name.setter
    def fuel_use_curve_name(self, value=None):
        """  Corresponds to IDD Field `fuel_use_curve_name`
        Curve is a function of Part Load Ratio (PLR)
        Table:OneIndependentVariable object can also be used
        curve = a + b*PLR + c*PLR**2
        PLR = Ratio of evaporator heat transfer rate to nominal capacity

        Args:
            value (str): value for IDD Field `fuel_use_curve_name`
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
                                 'for field `fuel_use_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_use_curve_name`')

        self._data["Fuel Use Curve Name"] = value

    @property
    def jacket_heat_recovery_curve_name(self):
        """Get jacket_heat_recovery_curve_name

        Returns:
            str: the value of `jacket_heat_recovery_curve_name` or None if not set
        """
        return self._data["Jacket Heat Recovery Curve Name"]

    @jacket_heat_recovery_curve_name.setter
    def jacket_heat_recovery_curve_name(self, value=None):
        """  Corresponds to IDD Field `jacket_heat_recovery_curve_name`
        Curve is a function of Part Load Ratio (PLR)
        Table:OneIndependentVariable object can also be used
        curve = a + b*PLR + c*PLR**2
        PLR = Ratio of evaporator heat transfer rate to nominal capacity

        Args:
            value (str): value for IDD Field `jacket_heat_recovery_curve_name`
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
                                 'for field `jacket_heat_recovery_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `jacket_heat_recovery_curve_name`')

        self._data["Jacket Heat Recovery Curve Name"] = value

    @property
    def lube_heat_recovery_curve_name(self):
        """Get lube_heat_recovery_curve_name

        Returns:
            str: the value of `lube_heat_recovery_curve_name` or None if not set
        """
        return self._data["Lube Heat Recovery Curve Name"]

    @lube_heat_recovery_curve_name.setter
    def lube_heat_recovery_curve_name(self, value=None):
        """  Corresponds to IDD Field `lube_heat_recovery_curve_name`
        Curve is a function of Part Load Ratio (PLR)
        Table:OneIndependentVariable object can also be used
        curve = a + b*PLR + c*PLR**2
        PLR = Ratio of evaporator heat transfer rate to nominal capacity

        Args:
            value (str): value for IDD Field `lube_heat_recovery_curve_name`
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
                                 'for field `lube_heat_recovery_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lube_heat_recovery_curve_name`')

        self._data["Lube Heat Recovery Curve Name"] = value

    @property
    def total_exhaust_energy_curve_name(self):
        """Get total_exhaust_energy_curve_name

        Returns:
            str: the value of `total_exhaust_energy_curve_name` or None if not set
        """
        return self._data["Total Exhaust Energy Curve Name"]

    @total_exhaust_energy_curve_name.setter
    def total_exhaust_energy_curve_name(self, value=None):
        """  Corresponds to IDD Field `total_exhaust_energy_curve_name`
        Curve is a function of Part Load Ratio (PLR)
        Table:OneIndependentVariable object can also be used
        curve = a + b*PLR + c*PLR**2
        PLR = Ratio of evaporator heat transfer rate to nominal capacity

        Args:
            value (str): value for IDD Field `total_exhaust_energy_curve_name`
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
                                 'for field `total_exhaust_energy_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `total_exhaust_energy_curve_name`')

        self._data["Total Exhaust Energy Curve Name"] = value

    @property
    def exhaust_temperature_curve_name(self):
        """Get exhaust_temperature_curve_name

        Returns:
            str: the value of `exhaust_temperature_curve_name` or None if not set
        """
        return self._data["Exhaust Temperature Curve Name"]

    @exhaust_temperature_curve_name.setter
    def exhaust_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `exhaust_temperature_curve_name`
        Curve is a function of Part Load Ratio (PLR)
        curve = a + b*PLR + c*PLR**2
        Table:OneIndependentVariable object can also be used
        PLR = Ratio of evaporator heat transfer rate to nominal capacity

        Args:
            value (str): value for IDD Field `exhaust_temperature_curve_name`
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
                                 'for field `exhaust_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_temperature_curve_name`')

        self._data["Exhaust Temperature Curve Name"] = value

    @property
    def coefficient_1_of_ufactor_times_area_curve(self):
        """Get coefficient_1_of_ufactor_times_area_curve

        Returns:
            float: the value of `coefficient_1_of_ufactor_times_area_curve` or None if not set
        """
        return self._data["Coefficient 1 of U-Factor Times Area Curve"]

    @coefficient_1_of_ufactor_times_area_curve.setter
    def coefficient_1_of_ufactor_times_area_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_ufactor_times_area_curve`
        curve = C1 * (nominal capacity)**C2

        Args:
            value (float): value for IDD Field `coefficient_1_of_ufactor_times_area_curve`
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
                                 'for field `coefficient_1_of_ufactor_times_area_curve`'.format(value))

        self._data["Coefficient 1 of U-Factor Times Area Curve"] = value

    @property
    def coefficient_2_of_ufactor_times_area_curve(self):
        """Get coefficient_2_of_ufactor_times_area_curve

        Returns:
            float: the value of `coefficient_2_of_ufactor_times_area_curve` or None if not set
        """
        return self._data["Coefficient 2 of U-Factor Times Area Curve"]

    @coefficient_2_of_ufactor_times_area_curve.setter
    def coefficient_2_of_ufactor_times_area_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_ufactor_times_area_curve`
        curve = C1 * (nominal capacity)**C2
        typical value .9

        Args:
            value (float): value for IDD Field `coefficient_2_of_ufactor_times_area_curve`
                value <= 2.0
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
                                 'for field `coefficient_2_of_ufactor_times_area_curve`'.format(value))
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `coefficient_2_of_ufactor_times_area_curve`')

        self._data["Coefficient 2 of U-Factor Times Area Curve"] = value

    @property
    def maximum_exhaust_flow_per_unit_of_power_output(self):
        """Get maximum_exhaust_flow_per_unit_of_power_output

        Returns:
            float: the value of `maximum_exhaust_flow_per_unit_of_power_output` or None if not set
        """
        return self._data["Maximum Exhaust Flow per Unit of Power Output"]

    @maximum_exhaust_flow_per_unit_of_power_output.setter
    def maximum_exhaust_flow_per_unit_of_power_output(self, value=None):
        """  Corresponds to IDD Field `maximum_exhaust_flow_per_unit_of_power_output`

        Args:
            value (float): value for IDD Field `maximum_exhaust_flow_per_unit_of_power_output`
                Unit: (kg/s)/W
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
                                 'for field `maximum_exhaust_flow_per_unit_of_power_output`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_exhaust_flow_per_unit_of_power_output`')

        self._data["Maximum Exhaust Flow per Unit of Power Output"] = value

    @property
    def design_minimum_exhaust_temperature(self):
        """Get design_minimum_exhaust_temperature

        Returns:
            float: the value of `design_minimum_exhaust_temperature` or None if not set
        """
        return self._data["Design Minimum Exhaust Temperature"]

    @design_minimum_exhaust_temperature.setter
    def design_minimum_exhaust_temperature(self, value=None):
        """  Corresponds to IDD Field `design_minimum_exhaust_temperature`

        Args:
            value (float): value for IDD Field `design_minimum_exhaust_temperature`
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
                                 'for field `design_minimum_exhaust_temperature`'.format(value))

        self._data["Design Minimum Exhaust Temperature"] = value

    @property
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """  Corresponds to IDD Field `fuel_type`

        Args:
            value (str): value for IDD Field `fuel_type`
                Accepted values are:
                      - NaturalGas
                      - PropaneGas
                      - Diesel
                      - Gasoline
                      - FuelOil#1
                      - FuelOil#2
                      - OtherFuel1
                      - OtherFuel2
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
                                 'for field `fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_type`')
            vals = set()
            vals.add("NaturalGas")
            vals.add("PropaneGas")
            vals.add("Diesel")
            vals.add("Gasoline")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fuel_type`'.format(value))

        self._data["Fuel Type"] = value

    @property
    def fuel_higher_heating_value(self):
        """Get fuel_higher_heating_value

        Returns:
            float: the value of `fuel_higher_heating_value` or None if not set
        """
        return self._data["Fuel Higher Heating Value"]

    @fuel_higher_heating_value.setter
    def fuel_higher_heating_value(self, value=None):
        """  Corresponds to IDD Field `fuel_higher_heating_value`

        Args:
            value (float): value for IDD Field `fuel_higher_heating_value`
                Unit: kJ/kg
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
                                 'for field `fuel_higher_heating_value`'.format(value))

        self._data["Fuel Higher Heating Value"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """Get design_heat_recovery_water_flow_rate

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self._data["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_heat_recovery_water_flow_rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.

        Args:
            value (float): value for IDD Field `design_heat_recovery_water_flow_rate`
                Unit: m3/s
                Default value: 0.0
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
                                 'for field `design_heat_recovery_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_heat_recovery_water_flow_rate`')

        self._data["Design Heat Recovery Water Flow Rate"] = value

    @property
    def heat_recovery_inlet_node_name(self):
        """Get heat_recovery_inlet_node_name

        Returns:
            str: the value of `heat_recovery_inlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Inlet Node Name"]

    @heat_recovery_inlet_node_name.setter
    def heat_recovery_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_node_name`
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
                                 'for field `heat_recovery_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_node_name`')

        self._data["Heat Recovery Inlet Node Name"] = value

    @property
    def heat_recovery_outlet_node_name(self):
        """Get heat_recovery_outlet_node_name

        Returns:
            str: the value of `heat_recovery_outlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Outlet Node Name"]

    @heat_recovery_outlet_node_name.setter
    def heat_recovery_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_outlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_outlet_node_name`
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
                                 'for field `heat_recovery_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_outlet_node_name`')

        self._data["Heat Recovery Outlet Node Name"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode`'.format(value))

        self._data["Chiller Flow Mode"] = value

    @property
    def maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node(self):
        """Get maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node

        Returns:
            float: the value of `maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node` or None if not set
        """
        return self._data["Maximum Temperature for Heat Recovery at Heat Recovery Outlet Node"]

    @maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node.setter
    def maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node(self, value=60.0 ):
        """  Corresponds to IDD Field `maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node`

        Args:
            value (float): value for IDD Field `maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node`
                Unit: C
                Default value: 60.0
                value >= 0.0
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
                                 'for field `maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node`')

        self._data["Maximum Temperature for Heat Recovery at Heat Recovery Outlet Node"] = value

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
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `basin_heater_capacity`
        This field is only used for Condenser Type = EvaporativelyCooled and for periods
        when the basin heater is available (field Basin Heater Operating Schedule Name).
        For this situation, the heater maintains the basin water temperature at the basin heater
        setpoint temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when the chiller is not operating.

        Args:
            value (float): value for IDD Field `basin_heater_capacity`
                Unit: W/K
                Default value: 0.0
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')

        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `basin_heater_setpoint_temperature`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Enter the outdoor dry-bulb temperature when the basin heater turns on.

        Args:
            value (float): value for IDD Field `basin_heater_setpoint_temperature`
                Unit: C
                Default value: 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')

        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `basin_heater_operating_schedule_name`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `basin_heater_operating_schedule_name`
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
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')

        self._data["Basin Heater Operating Schedule Name"] = value

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
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.nominal_cop))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.design_condenser_inlet_temperature))
        out.append(self._to_str(self.temperature_rise_coefficient))
        out.append(self._to_str(self.design_chilled_water_outlet_temperature))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.coefficient_1_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_1_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_1_of_full_load_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_full_load_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_full_load_ratio_curve))
        out.append(self._to_str(self.chilled_water_outlet_temperature_lower_limit))
        out.append(self._to_str(self.fuel_use_curve_name))
        out.append(self._to_str(self.jacket_heat_recovery_curve_name))
        out.append(self._to_str(self.lube_heat_recovery_curve_name))
        out.append(self._to_str(self.total_exhaust_energy_curve_name))
        out.append(self._to_str(self.exhaust_temperature_curve_name))
        out.append(self._to_str(self.coefficient_1_of_ufactor_times_area_curve))
        out.append(self._to_str(self.coefficient_2_of_ufactor_times_area_curve))
        out.append(self._to_str(self.maximum_exhaust_flow_per_unit_of_power_output))
        out.append(self._to_str(self.design_minimum_exhaust_temperature))
        out.append(self._to_str(self.fuel_type))
        out.append(self._to_str(self.fuel_higher_heating_value))
        out.append(self._to_str(self.design_heat_recovery_water_flow_rate))
        out.append(self._to_str(self.heat_recovery_inlet_node_name))
        out.append(self._to_str(self.heat_recovery_outlet_node_name))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        return ",".join(out)

class ChillerCombustionTurbine(object):
    """ Corresponds to IDD object `Chiller:CombustionTurbine`
        This chiller model is the empirical model from the Building Loads
        and System Thermodynamics (BLAST) program.  Chiller performance
        curves are generated by fitting catalog data to third order
        polynomial equations.  Three sets of coefficients are required.
    """
    internal_name = "Chiller:CombustionTurbine"
    field_count = 60

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Chiller:CombustionTurbine`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Condenser Type"] = None
        self._data["Nominal Capacity"] = None
        self._data["Nominal COP"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Design Condenser Inlet Temperature"] = None
        self._data["Temperature Rise Coefficient"] = None
        self._data["Design Chilled Water Outlet Temperature"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Coefficient 1 of Capacity Ratio Curve"] = None
        self._data["Coefficient 2 of Capacity Ratio Curve"] = None
        self._data["Coefficient 3 of Capacity Ratio Curve"] = None
        self._data["Coefficient 1 of Power Ratio Curve"] = None
        self._data["Coefficient 2 of Power Ratio Curve"] = None
        self._data["Coefficient 3 of Power Ratio Curve"] = None
        self._data["Coefficient 1 of Full Load Ratio Curve"] = None
        self._data["Coefficient 2 of Full Load Ratio Curve"] = None
        self._data["Coefficient 3 of Full Load Ratio Curve"] = None
        self._data["Chilled Water Outlet Temperature Lower Limit"] = None
        self._data["Coefficient 1 of Fuel Input Curve"] = None
        self._data["Coefficient 2 of Fuel Input Curve"] = None
        self._data["Coefficient 3 of Fuel Input Curve"] = None
        self._data["Coefficient 1 of Temperature Based Fuel Input Curve"] = None
        self._data["Coefficient 2 of Temperature Based Fuel Input Curve"] = None
        self._data["Coefficient 3 of Temperature Based Fuel Input Curve"] = None
        self._data["Coefficient 1 of Exhaust Flow Curve"] = None
        self._data["Coefficient 2 of Exhaust Flow Curve"] = None
        self._data["Coefficient 3 of Exhaust Flow Curve"] = None
        self._data["Coefficient 1 of Exhaust Gas Temperature Curve"] = None
        self._data["Coefficient 2 of Exhaust Gas Temperature Curve"] = None
        self._data["Coefficient 3 of Exhaust Gas Temperature Curve"] = None
        self._data["Coefficient 1 of Temperature Based Exhaust Gas Temperature Curve"] = None
        self._data["Coefficient 2 of Temperature Based Exhaust Gas Temperature Curve"] = None
        self._data["Coefficient 3 of Temperature Based Exhaust Gas Temperature Curve"] = None
        self._data["Coefficient 1 of Recovery Lube Heat Curve"] = None
        self._data["Coefficient 2 of Recovery Lube Heat Curve"] = None
        self._data["Coefficient 3 of Recovery Lube Heat Curve"] = None
        self._data["Coefficient 1 of U-Factor Times Area Curve"] = None
        self._data["Coefficient 2 of U-Factor Times Area Curve"] = None
        self._data["Gas Turbine Engine Capacity"] = None
        self._data["Maximum Exhaust Flow per Unit of Power Output"] = None
        self._data["Design Steam Saturation Temperature"] = None
        self._data["Fuel Higher Heating Value"] = None
        self._data["Design Heat Recovery Water Flow Rate"] = None
        self._data["Heat Recovery Inlet Node Name"] = None
        self._data["Heat Recovery Outlet Node Name"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Fuel Type"] = None
        self._data["Heat Recovery Maximum Temperature"] = None
        self._data["Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None

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
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cop = None
        else:
            self.nominal_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_inlet_temperature = None
        else:
            self.design_condenser_inlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_rise_coefficient = None
        else:
            self.temperature_rise_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_outlet_temperature = None
        else:
            self.design_chilled_water_outlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_water_flow_rate = None
        else:
            self.design_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_capacity_ratio_curve = None
        else:
            self.coefficient_1_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_capacity_ratio_curve = None
        else:
            self.coefficient_2_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_capacity_ratio_curve = None
        else:
            self.coefficient_3_of_capacity_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_power_ratio_curve = None
        else:
            self.coefficient_1_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_power_ratio_curve = None
        else:
            self.coefficient_2_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_power_ratio_curve = None
        else:
            self.coefficient_3_of_power_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_full_load_ratio_curve = None
        else:
            self.coefficient_1_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_full_load_ratio_curve = None
        else:
            self.coefficient_2_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_full_load_ratio_curve = None
        else:
            self.coefficient_3_of_full_load_ratio_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_temperature_lower_limit = None
        else:
            self.chilled_water_outlet_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_fuel_input_curve = None
        else:
            self.coefficient_1_of_fuel_input_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_fuel_input_curve = None
        else:
            self.coefficient_2_of_fuel_input_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_fuel_input_curve = None
        else:
            self.coefficient_3_of_fuel_input_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_temperature_based_fuel_input_curve = None
        else:
            self.coefficient_1_of_temperature_based_fuel_input_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_temperature_based_fuel_input_curve = None
        else:
            self.coefficient_2_of_temperature_based_fuel_input_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_temperature_based_fuel_input_curve = None
        else:
            self.coefficient_3_of_temperature_based_fuel_input_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_exhaust_flow_curve = None
        else:
            self.coefficient_1_of_exhaust_flow_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_exhaust_flow_curve = None
        else:
            self.coefficient_2_of_exhaust_flow_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_exhaust_flow_curve = None
        else:
            self.coefficient_3_of_exhaust_flow_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_exhaust_gas_temperature_curve = None
        else:
            self.coefficient_1_of_exhaust_gas_temperature_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_exhaust_gas_temperature_curve = None
        else:
            self.coefficient_2_of_exhaust_gas_temperature_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_exhaust_gas_temperature_curve = None
        else:
            self.coefficient_3_of_exhaust_gas_temperature_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_temperature_based_exhaust_gas_temperature_curve = None
        else:
            self.coefficient_1_of_temperature_based_exhaust_gas_temperature_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_temperature_based_exhaust_gas_temperature_curve = None
        else:
            self.coefficient_2_of_temperature_based_exhaust_gas_temperature_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_temperature_based_exhaust_gas_temperature_curve = None
        else:
            self.coefficient_3_of_temperature_based_exhaust_gas_temperature_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_recovery_lube_heat_curve = None
        else:
            self.coefficient_1_of_recovery_lube_heat_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_recovery_lube_heat_curve = None
        else:
            self.coefficient_2_of_recovery_lube_heat_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_recovery_lube_heat_curve = None
        else:
            self.coefficient_3_of_recovery_lube_heat_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_ufactor_times_area_curve = None
        else:
            self.coefficient_1_of_ufactor_times_area_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_ufactor_times_area_curve = None
        else:
            self.coefficient_2_of_ufactor_times_area_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_turbine_engine_capacity = None
        else:
            self.gas_turbine_engine_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_exhaust_flow_per_unit_of_power_output = None
        else:
            self.maximum_exhaust_flow_per_unit_of_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_steam_saturation_temperature = None
        else:
            self.design_steam_saturation_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_higher_heating_value = None
        else:
            self.fuel_higher_heating_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_heat_recovery_water_flow_rate = None
        else:
            self.design_heat_recovery_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_inlet_node_name = None
        else:
            self.heat_recovery_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_outlet_node_name = None
        else:
            self.heat_recovery_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_maximum_temperature = None
        else:
            self.heat_recovery_maximum_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
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
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """  Corresponds to IDD Field `condenser_type`

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - WaterCooled
                      - EvaporativelyCooled
                Default value: AirCooled
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
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            vals = set()
            vals.add("AirCooled")
            vals.add("WaterCooled")
            vals.add("EvaporativelyCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

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

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def nominal_cop(self):
        """Get nominal_cop

        Returns:
            float: the value of `nominal_cop` or None if not set
        """
        return self._data["Nominal COP"]

    @nominal_cop.setter
    def nominal_cop(self, value=None):
        """  Corresponds to IDD Field `nominal_cop`

        Args:
            value (float): value for IDD Field `nominal_cop`
                Unit: W/W
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
                                 'for field `nominal_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_cop`')

        self._data["Nominal COP"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
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
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
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
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_part_load_ratio`

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `optimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def design_condenser_inlet_temperature(self):
        """Get design_condenser_inlet_temperature

        Returns:
            float: the value of `design_condenser_inlet_temperature` or None if not set
        """
        return self._data["Design Condenser Inlet Temperature"]

    @design_condenser_inlet_temperature.setter
    def design_condenser_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `design_condenser_inlet_temperature`

        Args:
            value (float): value for IDD Field `design_condenser_inlet_temperature`
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
                                 'for field `design_condenser_inlet_temperature`'.format(value))

        self._data["Design Condenser Inlet Temperature"] = value

    @property
    def temperature_rise_coefficient(self):
        """Get temperature_rise_coefficient

        Returns:
            float: the value of `temperature_rise_coefficient` or None if not set
        """
        return self._data["Temperature Rise Coefficient"]

    @temperature_rise_coefficient.setter
    def temperature_rise_coefficient(self, value=None):
        """  Corresponds to IDD Field `temperature_rise_coefficient`

        Args:
            value (float): value for IDD Field `temperature_rise_coefficient`
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
                                 'for field `temperature_rise_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_rise_coefficient`')

        self._data["Temperature Rise Coefficient"] = value

    @property
    def design_chilled_water_outlet_temperature(self):
        """Get design_chilled_water_outlet_temperature

        Returns:
            float: the value of `design_chilled_water_outlet_temperature` or None if not set
        """
        return self._data["Design Chilled Water Outlet Temperature"]

    @design_chilled_water_outlet_temperature.setter
    def design_chilled_water_outlet_temperature(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_outlet_temperature`

        Args:
            value (float): value for IDD Field `design_chilled_water_outlet_temperature`
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
                                 'for field `design_chilled_water_outlet_temperature`'.format(value))

        self._data["Design Chilled Water Outlet Temperature"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable volume this is the max flow & for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
                Unit: m3/s
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_chilled_water_flow_rate`')

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_water_flow_rate(self):
        """Get design_condenser_water_flow_rate

        Returns:
            float: the value of `design_condenser_water_flow_rate` or None if not set
        """
        return self._data["Design Condenser Water Flow Rate"]

    @design_condenser_water_flow_rate.setter
    def design_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_water_flow_rate`
        This field is not used for Condenser Type = AirCooled or EvaporativelyCooled

        Args:
            value (float): value for IDD Field `design_condenser_water_flow_rate`
                Unit: m3/s
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
                                 'for field `design_condenser_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_condenser_water_flow_rate`')

        self._data["Design Condenser Water Flow Rate"] = value

    @property
    def coefficient_1_of_capacity_ratio_curve(self):
        """Get coefficient_1_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Capacity Ratio Curve"]

    @coefficient_1_of_capacity_ratio_curve.setter
    def coefficient_1_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_capacity_ratio_curve`
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
                                 'for field `coefficient_1_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Capacity Ratio Curve"] = value

    @property
    def coefficient_2_of_capacity_ratio_curve(self):
        """Get coefficient_2_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Capacity Ratio Curve"]

    @coefficient_2_of_capacity_ratio_curve.setter
    def coefficient_2_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_capacity_ratio_curve`
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
                                 'for field `coefficient_2_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Capacity Ratio Curve"] = value

    @property
    def coefficient_3_of_capacity_ratio_curve(self):
        """Get coefficient_3_of_capacity_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_capacity_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Capacity Ratio Curve"]

    @coefficient_3_of_capacity_ratio_curve.setter
    def coefficient_3_of_capacity_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_capacity_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_capacity_ratio_curve`
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
                                 'for field `coefficient_3_of_capacity_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Capacity Ratio Curve"] = value

    @property
    def coefficient_1_of_power_ratio_curve(self):
        """Get coefficient_1_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Power Ratio Curve"]

    @coefficient_1_of_power_ratio_curve.setter
    def coefficient_1_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_power_ratio_curve`
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
                                 'for field `coefficient_1_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Power Ratio Curve"] = value

    @property
    def coefficient_2_of_power_ratio_curve(self):
        """Get coefficient_2_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Power Ratio Curve"]

    @coefficient_2_of_power_ratio_curve.setter
    def coefficient_2_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_power_ratio_curve`
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
                                 'for field `coefficient_2_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Power Ratio Curve"] = value

    @property
    def coefficient_3_of_power_ratio_curve(self):
        """Get coefficient_3_of_power_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_power_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Power Ratio Curve"]

    @coefficient_3_of_power_ratio_curve.setter
    def coefficient_3_of_power_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_power_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_power_ratio_curve`
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
                                 'for field `coefficient_3_of_power_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Power Ratio Curve"] = value

    @property
    def coefficient_1_of_full_load_ratio_curve(self):
        """Get coefficient_1_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_1_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 1 of Full Load Ratio Curve"]

    @coefficient_1_of_full_load_ratio_curve.setter
    def coefficient_1_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_full_load_ratio_curve`
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
                                 'for field `coefficient_1_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 1 of Full Load Ratio Curve"] = value

    @property
    def coefficient_2_of_full_load_ratio_curve(self):
        """Get coefficient_2_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_2_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 2 of Full Load Ratio Curve"]

    @coefficient_2_of_full_load_ratio_curve.setter
    def coefficient_2_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_full_load_ratio_curve`
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
                                 'for field `coefficient_2_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 2 of Full Load Ratio Curve"] = value

    @property
    def coefficient_3_of_full_load_ratio_curve(self):
        """Get coefficient_3_of_full_load_ratio_curve

        Returns:
            float: the value of `coefficient_3_of_full_load_ratio_curve` or None if not set
        """
        return self._data["Coefficient 3 of Full Load Ratio Curve"]

    @coefficient_3_of_full_load_ratio_curve.setter
    def coefficient_3_of_full_load_ratio_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_full_load_ratio_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_full_load_ratio_curve`
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
                                 'for field `coefficient_3_of_full_load_ratio_curve`'.format(value))

        self._data["Coefficient 3 of Full Load Ratio Curve"] = value

    @property
    def chilled_water_outlet_temperature_lower_limit(self):
        """Get chilled_water_outlet_temperature_lower_limit

        Returns:
            float: the value of `chilled_water_outlet_temperature_lower_limit` or None if not set
        """
        return self._data["Chilled Water Outlet Temperature Lower Limit"]

    @chilled_water_outlet_temperature_lower_limit.setter
    def chilled_water_outlet_temperature_lower_limit(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_temperature_lower_limit`
        Special Gas Turbine Chiller Parameters Below

        Args:
            value (float): value for IDD Field `chilled_water_outlet_temperature_lower_limit`
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
                                 'for field `chilled_water_outlet_temperature_lower_limit`'.format(value))

        self._data["Chilled Water Outlet Temperature Lower Limit"] = value

    @property
    def coefficient_1_of_fuel_input_curve(self):
        """Get coefficient_1_of_fuel_input_curve

        Returns:
            float: the value of `coefficient_1_of_fuel_input_curve` or None if not set
        """
        return self._data["Coefficient 1 of Fuel Input Curve"]

    @coefficient_1_of_fuel_input_curve.setter
    def coefficient_1_of_fuel_input_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_fuel_input_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_fuel_input_curve`
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
                                 'for field `coefficient_1_of_fuel_input_curve`'.format(value))

        self._data["Coefficient 1 of Fuel Input Curve"] = value

    @property
    def coefficient_2_of_fuel_input_curve(self):
        """Get coefficient_2_of_fuel_input_curve

        Returns:
            float: the value of `coefficient_2_of_fuel_input_curve` or None if not set
        """
        return self._data["Coefficient 2 of Fuel Input Curve"]

    @coefficient_2_of_fuel_input_curve.setter
    def coefficient_2_of_fuel_input_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_fuel_input_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_fuel_input_curve`
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
                                 'for field `coefficient_2_of_fuel_input_curve`'.format(value))

        self._data["Coefficient 2 of Fuel Input Curve"] = value

    @property
    def coefficient_3_of_fuel_input_curve(self):
        """Get coefficient_3_of_fuel_input_curve

        Returns:
            float: the value of `coefficient_3_of_fuel_input_curve` or None if not set
        """
        return self._data["Coefficient 3 of Fuel Input Curve"]

    @coefficient_3_of_fuel_input_curve.setter
    def coefficient_3_of_fuel_input_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_fuel_input_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_fuel_input_curve`
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
                                 'for field `coefficient_3_of_fuel_input_curve`'.format(value))

        self._data["Coefficient 3 of Fuel Input Curve"] = value

    @property
    def coefficient_1_of_temperature_based_fuel_input_curve(self):
        """Get coefficient_1_of_temperature_based_fuel_input_curve

        Returns:
            float: the value of `coefficient_1_of_temperature_based_fuel_input_curve` or None if not set
        """
        return self._data["Coefficient 1 of Temperature Based Fuel Input Curve"]

    @coefficient_1_of_temperature_based_fuel_input_curve.setter
    def coefficient_1_of_temperature_based_fuel_input_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_temperature_based_fuel_input_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_temperature_based_fuel_input_curve`
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
                                 'for field `coefficient_1_of_temperature_based_fuel_input_curve`'.format(value))

        self._data["Coefficient 1 of Temperature Based Fuel Input Curve"] = value

    @property
    def coefficient_2_of_temperature_based_fuel_input_curve(self):
        """Get coefficient_2_of_temperature_based_fuel_input_curve

        Returns:
            float: the value of `coefficient_2_of_temperature_based_fuel_input_curve` or None if not set
        """
        return self._data["Coefficient 2 of Temperature Based Fuel Input Curve"]

    @coefficient_2_of_temperature_based_fuel_input_curve.setter
    def coefficient_2_of_temperature_based_fuel_input_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_temperature_based_fuel_input_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_temperature_based_fuel_input_curve`
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
                                 'for field `coefficient_2_of_temperature_based_fuel_input_curve`'.format(value))

        self._data["Coefficient 2 of Temperature Based Fuel Input Curve"] = value

    @property
    def coefficient_3_of_temperature_based_fuel_input_curve(self):
        """Get coefficient_3_of_temperature_based_fuel_input_curve

        Returns:
            float: the value of `coefficient_3_of_temperature_based_fuel_input_curve` or None if not set
        """
        return self._data["Coefficient 3 of Temperature Based Fuel Input Curve"]

    @coefficient_3_of_temperature_based_fuel_input_curve.setter
    def coefficient_3_of_temperature_based_fuel_input_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_temperature_based_fuel_input_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_temperature_based_fuel_input_curve`
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
                                 'for field `coefficient_3_of_temperature_based_fuel_input_curve`'.format(value))

        self._data["Coefficient 3 of Temperature Based Fuel Input Curve"] = value

    @property
    def coefficient_1_of_exhaust_flow_curve(self):
        """Get coefficient_1_of_exhaust_flow_curve

        Returns:
            float: the value of `coefficient_1_of_exhaust_flow_curve` or None if not set
        """
        return self._data["Coefficient 1 of Exhaust Flow Curve"]

    @coefficient_1_of_exhaust_flow_curve.setter
    def coefficient_1_of_exhaust_flow_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_exhaust_flow_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_exhaust_flow_curve`
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
                                 'for field `coefficient_1_of_exhaust_flow_curve`'.format(value))

        self._data["Coefficient 1 of Exhaust Flow Curve"] = value

    @property
    def coefficient_2_of_exhaust_flow_curve(self):
        """Get coefficient_2_of_exhaust_flow_curve

        Returns:
            float: the value of `coefficient_2_of_exhaust_flow_curve` or None if not set
        """
        return self._data["Coefficient 2 of Exhaust Flow Curve"]

    @coefficient_2_of_exhaust_flow_curve.setter
    def coefficient_2_of_exhaust_flow_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_exhaust_flow_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_exhaust_flow_curve`
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
                                 'for field `coefficient_2_of_exhaust_flow_curve`'.format(value))

        self._data["Coefficient 2 of Exhaust Flow Curve"] = value

    @property
    def coefficient_3_of_exhaust_flow_curve(self):
        """Get coefficient_3_of_exhaust_flow_curve

        Returns:
            float: the value of `coefficient_3_of_exhaust_flow_curve` or None if not set
        """
        return self._data["Coefficient 3 of Exhaust Flow Curve"]

    @coefficient_3_of_exhaust_flow_curve.setter
    def coefficient_3_of_exhaust_flow_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_exhaust_flow_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_exhaust_flow_curve`
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
                                 'for field `coefficient_3_of_exhaust_flow_curve`'.format(value))

        self._data["Coefficient 3 of Exhaust Flow Curve"] = value

    @property
    def coefficient_1_of_exhaust_gas_temperature_curve(self):
        """Get coefficient_1_of_exhaust_gas_temperature_curve

        Returns:
            float: the value of `coefficient_1_of_exhaust_gas_temperature_curve` or None if not set
        """
        return self._data["Coefficient 1 of Exhaust Gas Temperature Curve"]

    @coefficient_1_of_exhaust_gas_temperature_curve.setter
    def coefficient_1_of_exhaust_gas_temperature_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_exhaust_gas_temperature_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_exhaust_gas_temperature_curve`
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
                                 'for field `coefficient_1_of_exhaust_gas_temperature_curve`'.format(value))

        self._data["Coefficient 1 of Exhaust Gas Temperature Curve"] = value

    @property
    def coefficient_2_of_exhaust_gas_temperature_curve(self):
        """Get coefficient_2_of_exhaust_gas_temperature_curve

        Returns:
            float: the value of `coefficient_2_of_exhaust_gas_temperature_curve` or None if not set
        """
        return self._data["Coefficient 2 of Exhaust Gas Temperature Curve"]

    @coefficient_2_of_exhaust_gas_temperature_curve.setter
    def coefficient_2_of_exhaust_gas_temperature_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_exhaust_gas_temperature_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_exhaust_gas_temperature_curve`
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
                                 'for field `coefficient_2_of_exhaust_gas_temperature_curve`'.format(value))

        self._data["Coefficient 2 of Exhaust Gas Temperature Curve"] = value

    @property
    def coefficient_3_of_exhaust_gas_temperature_curve(self):
        """Get coefficient_3_of_exhaust_gas_temperature_curve

        Returns:
            float: the value of `coefficient_3_of_exhaust_gas_temperature_curve` or None if not set
        """
        return self._data["Coefficient 3 of Exhaust Gas Temperature Curve"]

    @coefficient_3_of_exhaust_gas_temperature_curve.setter
    def coefficient_3_of_exhaust_gas_temperature_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_exhaust_gas_temperature_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_exhaust_gas_temperature_curve`
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
                                 'for field `coefficient_3_of_exhaust_gas_temperature_curve`'.format(value))

        self._data["Coefficient 3 of Exhaust Gas Temperature Curve"] = value

    @property
    def coefficient_1_of_temperature_based_exhaust_gas_temperature_curve(self):
        """Get coefficient_1_of_temperature_based_exhaust_gas_temperature_curve

        Returns:
            float: the value of `coefficient_1_of_temperature_based_exhaust_gas_temperature_curve` or None if not set
        """
        return self._data["Coefficient 1 of Temperature Based Exhaust Gas Temperature Curve"]

    @coefficient_1_of_temperature_based_exhaust_gas_temperature_curve.setter
    def coefficient_1_of_temperature_based_exhaust_gas_temperature_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_temperature_based_exhaust_gas_temperature_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_temperature_based_exhaust_gas_temperature_curve`
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
                                 'for field `coefficient_1_of_temperature_based_exhaust_gas_temperature_curve`'.format(value))

        self._data["Coefficient 1 of Temperature Based Exhaust Gas Temperature Curve"] = value

    @property
    def coefficient_2_of_temperature_based_exhaust_gas_temperature_curve(self):
        """Get coefficient_2_of_temperature_based_exhaust_gas_temperature_curve

        Returns:
            float: the value of `coefficient_2_of_temperature_based_exhaust_gas_temperature_curve` or None if not set
        """
        return self._data["Coefficient 2 of Temperature Based Exhaust Gas Temperature Curve"]

    @coefficient_2_of_temperature_based_exhaust_gas_temperature_curve.setter
    def coefficient_2_of_temperature_based_exhaust_gas_temperature_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_temperature_based_exhaust_gas_temperature_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_temperature_based_exhaust_gas_temperature_curve`
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
                                 'for field `coefficient_2_of_temperature_based_exhaust_gas_temperature_curve`'.format(value))

        self._data["Coefficient 2 of Temperature Based Exhaust Gas Temperature Curve"] = value

    @property
    def coefficient_3_of_temperature_based_exhaust_gas_temperature_curve(self):
        """Get coefficient_3_of_temperature_based_exhaust_gas_temperature_curve

        Returns:
            float: the value of `coefficient_3_of_temperature_based_exhaust_gas_temperature_curve` or None if not set
        """
        return self._data["Coefficient 3 of Temperature Based Exhaust Gas Temperature Curve"]

    @coefficient_3_of_temperature_based_exhaust_gas_temperature_curve.setter
    def coefficient_3_of_temperature_based_exhaust_gas_temperature_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_temperature_based_exhaust_gas_temperature_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_temperature_based_exhaust_gas_temperature_curve`
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
                                 'for field `coefficient_3_of_temperature_based_exhaust_gas_temperature_curve`'.format(value))

        self._data["Coefficient 3 of Temperature Based Exhaust Gas Temperature Curve"] = value

    @property
    def coefficient_1_of_recovery_lube_heat_curve(self):
        """Get coefficient_1_of_recovery_lube_heat_curve

        Returns:
            float: the value of `coefficient_1_of_recovery_lube_heat_curve` or None if not set
        """
        return self._data["Coefficient 1 of Recovery Lube Heat Curve"]

    @coefficient_1_of_recovery_lube_heat_curve.setter
    def coefficient_1_of_recovery_lube_heat_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_recovery_lube_heat_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_recovery_lube_heat_curve`
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
                                 'for field `coefficient_1_of_recovery_lube_heat_curve`'.format(value))

        self._data["Coefficient 1 of Recovery Lube Heat Curve"] = value

    @property
    def coefficient_2_of_recovery_lube_heat_curve(self):
        """Get coefficient_2_of_recovery_lube_heat_curve

        Returns:
            float: the value of `coefficient_2_of_recovery_lube_heat_curve` or None if not set
        """
        return self._data["Coefficient 2 of Recovery Lube Heat Curve"]

    @coefficient_2_of_recovery_lube_heat_curve.setter
    def coefficient_2_of_recovery_lube_heat_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_recovery_lube_heat_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_recovery_lube_heat_curve`
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
                                 'for field `coefficient_2_of_recovery_lube_heat_curve`'.format(value))

        self._data["Coefficient 2 of Recovery Lube Heat Curve"] = value

    @property
    def coefficient_3_of_recovery_lube_heat_curve(self):
        """Get coefficient_3_of_recovery_lube_heat_curve

        Returns:
            float: the value of `coefficient_3_of_recovery_lube_heat_curve` or None if not set
        """
        return self._data["Coefficient 3 of Recovery Lube Heat Curve"]

    @coefficient_3_of_recovery_lube_heat_curve.setter
    def coefficient_3_of_recovery_lube_heat_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_recovery_lube_heat_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_recovery_lube_heat_curve`
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
                                 'for field `coefficient_3_of_recovery_lube_heat_curve`'.format(value))

        self._data["Coefficient 3 of Recovery Lube Heat Curve"] = value

    @property
    def coefficient_1_of_ufactor_times_area_curve(self):
        """Get coefficient_1_of_ufactor_times_area_curve

        Returns:
            float: the value of `coefficient_1_of_ufactor_times_area_curve` or None if not set
        """
        return self._data["Coefficient 1 of U-Factor Times Area Curve"]

    @coefficient_1_of_ufactor_times_area_curve.setter
    def coefficient_1_of_ufactor_times_area_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_ufactor_times_area_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_ufactor_times_area_curve`
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
                                 'for field `coefficient_1_of_ufactor_times_area_curve`'.format(value))

        self._data["Coefficient 1 of U-Factor Times Area Curve"] = value

    @property
    def coefficient_2_of_ufactor_times_area_curve(self):
        """Get coefficient_2_of_ufactor_times_area_curve

        Returns:
            float: the value of `coefficient_2_of_ufactor_times_area_curve` or None if not set
        """
        return self._data["Coefficient 2 of U-Factor Times Area Curve"]

    @coefficient_2_of_ufactor_times_area_curve.setter
    def coefficient_2_of_ufactor_times_area_curve(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_ufactor_times_area_curve`
        typical value .9

        Args:
            value (float): value for IDD Field `coefficient_2_of_ufactor_times_area_curve`
                value <= 2.0
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
                                 'for field `coefficient_2_of_ufactor_times_area_curve`'.format(value))
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `coefficient_2_of_ufactor_times_area_curve`')

        self._data["Coefficient 2 of U-Factor Times Area Curve"] = value

    @property
    def gas_turbine_engine_capacity(self):
        """Get gas_turbine_engine_capacity

        Returns:
            float: the value of `gas_turbine_engine_capacity` or None if not set
        """
        return self._data["Gas Turbine Engine Capacity"]

    @gas_turbine_engine_capacity.setter
    def gas_turbine_engine_capacity(self, value=None):
        """  Corresponds to IDD Field `gas_turbine_engine_capacity`

        Args:
            value (float): value for IDD Field `gas_turbine_engine_capacity`
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
                                 'for field `gas_turbine_engine_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gas_turbine_engine_capacity`')

        self._data["Gas Turbine Engine Capacity"] = value

    @property
    def maximum_exhaust_flow_per_unit_of_power_output(self):
        """Get maximum_exhaust_flow_per_unit_of_power_output

        Returns:
            float: the value of `maximum_exhaust_flow_per_unit_of_power_output` or None if not set
        """
        return self._data["Maximum Exhaust Flow per Unit of Power Output"]

    @maximum_exhaust_flow_per_unit_of_power_output.setter
    def maximum_exhaust_flow_per_unit_of_power_output(self, value=None):
        """  Corresponds to IDD Field `maximum_exhaust_flow_per_unit_of_power_output`

        Args:
            value (float): value for IDD Field `maximum_exhaust_flow_per_unit_of_power_output`
                Unit: (kg/s)/W
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
                                 'for field `maximum_exhaust_flow_per_unit_of_power_output`'.format(value))

        self._data["Maximum Exhaust Flow per Unit of Power Output"] = value

    @property
    def design_steam_saturation_temperature(self):
        """Get design_steam_saturation_temperature

        Returns:
            float: the value of `design_steam_saturation_temperature` or None if not set
        """
        return self._data["Design Steam Saturation Temperature"]

    @design_steam_saturation_temperature.setter
    def design_steam_saturation_temperature(self, value=None):
        """  Corresponds to IDD Field `design_steam_saturation_temperature`

        Args:
            value (float): value for IDD Field `design_steam_saturation_temperature`
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
                                 'for field `design_steam_saturation_temperature`'.format(value))

        self._data["Design Steam Saturation Temperature"] = value

    @property
    def fuel_higher_heating_value(self):
        """Get fuel_higher_heating_value

        Returns:
            float: the value of `fuel_higher_heating_value` or None if not set
        """
        return self._data["Fuel Higher Heating Value"]

    @fuel_higher_heating_value.setter
    def fuel_higher_heating_value(self, value=None):
        """  Corresponds to IDD Field `fuel_higher_heating_value`

        Args:
            value (float): value for IDD Field `fuel_higher_heating_value`
                Unit: kJ/kg
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
                                 'for field `fuel_higher_heating_value`'.format(value))

        self._data["Fuel Higher Heating Value"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """Get design_heat_recovery_water_flow_rate

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self._data["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_heat_recovery_water_flow_rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.

        Args:
            value (float): value for IDD Field `design_heat_recovery_water_flow_rate`
                Unit: m3/s
                Default value: 0.0
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
                                 'for field `design_heat_recovery_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_heat_recovery_water_flow_rate`')

        self._data["Design Heat Recovery Water Flow Rate"] = value

    @property
    def heat_recovery_inlet_node_name(self):
        """Get heat_recovery_inlet_node_name

        Returns:
            str: the value of `heat_recovery_inlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Inlet Node Name"]

    @heat_recovery_inlet_node_name.setter
    def heat_recovery_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_inlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_inlet_node_name`
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
                                 'for field `heat_recovery_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_inlet_node_name`')

        self._data["Heat Recovery Inlet Node Name"] = value

    @property
    def heat_recovery_outlet_node_name(self):
        """Get heat_recovery_outlet_node_name

        Returns:
            str: the value of `heat_recovery_outlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Outlet Node Name"]

    @heat_recovery_outlet_node_name.setter
    def heat_recovery_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_outlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_outlet_node_name`
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
                                 'for field `heat_recovery_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_outlet_node_name`')

        self._data["Heat Recovery Outlet Node Name"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value="NotModulated"):
        """  Corresponds to IDD Field `chiller_flow_mode`
        Select operating mode for fluid flow through the chiller. "NotModulated" is for
        either variable or constant pumping with flow controlled by the external plant system.
        "ConstantFlow" is for constant pumping with flow controlled by chiller to operate at
        full design flow rate.  "LeavingSetpointModulated" is for variable pumping with flow
        controlled by chiller to vary flow to target a leaving temperature setpoint.

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                Accepted values are:
                      - ConstantFlow
                      - LeavingSetpointModulated
                      - NotModulated
                Default value: NotModulated
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
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("LeavingSetpointModulated")
            vals.add("NotModulated")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_flow_mode`'.format(value))

        self._data["Chiller Flow Mode"] = value

    @property
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value="NaturalGas"):
        """  Corresponds to IDD Field `fuel_type`

        Args:
            value (str): value for IDD Field `fuel_type`
                Accepted values are:
                      - NaturalGas
                      - PropaneGas
                      - Diesel
                      - Gasoline
                      - FuelOil#1
                      - FuelOil#2
                      - OtherFuel1
                      - OtherFuel2
                Default value: NaturalGas
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
                                 'for field `fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_type`')
            vals = set()
            vals.add("NaturalGas")
            vals.add("PropaneGas")
            vals.add("Diesel")
            vals.add("Gasoline")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fuel_type`'.format(value))

        self._data["Fuel Type"] = value

    @property
    def heat_recovery_maximum_temperature(self):
        """Get heat_recovery_maximum_temperature

        Returns:
            float: the value of `heat_recovery_maximum_temperature` or None if not set
        """
        return self._data["Heat Recovery Maximum Temperature"]

    @heat_recovery_maximum_temperature.setter
    def heat_recovery_maximum_temperature(self, value=80.0 ):
        """  Corresponds to IDD Field `heat_recovery_maximum_temperature`

        Args:
            value (float): value for IDD Field `heat_recovery_maximum_temperature`
                Unit: C
                Default value: 80.0
                value >= 0.0
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
                                 'for field `heat_recovery_maximum_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_recovery_maximum_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `heat_recovery_maximum_temperature`')

        self._data["Heat Recovery Maximum Temperature"] = value

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
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `basin_heater_capacity`
        This field is only used for Condenser Type = EvaporativelyCooled and for periods
        when the basin heater is available (field Basin Heater Operating Schedule Name).
        For this situation, The heater maintains the basin water temperature at the basin heater
        setpoint temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when the chiller is not operating.

        Args:
            value (float): value for IDD Field `basin_heater_capacity`
                Unit: W/K
                Default value: 0.0
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')

        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `basin_heater_setpoint_temperature`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Enter the outdoor dry-bulb temperature when the basin heater turns on.

        Args:
            value (float): value for IDD Field `basin_heater_setpoint_temperature`
                Unit: C
                Default value: 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')

        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `basin_heater_operating_schedule_name`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `basin_heater_operating_schedule_name`
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
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')

        self._data["Basin Heater Operating Schedule Name"] = value

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
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.nominal_cop))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.design_condenser_inlet_temperature))
        out.append(self._to_str(self.temperature_rise_coefficient))
        out.append(self._to_str(self.design_chilled_water_outlet_temperature))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.coefficient_1_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_capacity_ratio_curve))
        out.append(self._to_str(self.coefficient_1_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_power_ratio_curve))
        out.append(self._to_str(self.coefficient_1_of_full_load_ratio_curve))
        out.append(self._to_str(self.coefficient_2_of_full_load_ratio_curve))
        out.append(self._to_str(self.coefficient_3_of_full_load_ratio_curve))
        out.append(self._to_str(self.chilled_water_outlet_temperature_lower_limit))
        out.append(self._to_str(self.coefficient_1_of_fuel_input_curve))
        out.append(self._to_str(self.coefficient_2_of_fuel_input_curve))
        out.append(self._to_str(self.coefficient_3_of_fuel_input_curve))
        out.append(self._to_str(self.coefficient_1_of_temperature_based_fuel_input_curve))
        out.append(self._to_str(self.coefficient_2_of_temperature_based_fuel_input_curve))
        out.append(self._to_str(self.coefficient_3_of_temperature_based_fuel_input_curve))
        out.append(self._to_str(self.coefficient_1_of_exhaust_flow_curve))
        out.append(self._to_str(self.coefficient_2_of_exhaust_flow_curve))
        out.append(self._to_str(self.coefficient_3_of_exhaust_flow_curve))
        out.append(self._to_str(self.coefficient_1_of_exhaust_gas_temperature_curve))
        out.append(self._to_str(self.coefficient_2_of_exhaust_gas_temperature_curve))
        out.append(self._to_str(self.coefficient_3_of_exhaust_gas_temperature_curve))
        out.append(self._to_str(self.coefficient_1_of_temperature_based_exhaust_gas_temperature_curve))
        out.append(self._to_str(self.coefficient_2_of_temperature_based_exhaust_gas_temperature_curve))
        out.append(self._to_str(self.coefficient_3_of_temperature_based_exhaust_gas_temperature_curve))
        out.append(self._to_str(self.coefficient_1_of_recovery_lube_heat_curve))
        out.append(self._to_str(self.coefficient_2_of_recovery_lube_heat_curve))
        out.append(self._to_str(self.coefficient_3_of_recovery_lube_heat_curve))
        out.append(self._to_str(self.coefficient_1_of_ufactor_times_area_curve))
        out.append(self._to_str(self.coefficient_2_of_ufactor_times_area_curve))
        out.append(self._to_str(self.gas_turbine_engine_capacity))
        out.append(self._to_str(self.maximum_exhaust_flow_per_unit_of_power_output))
        out.append(self._to_str(self.design_steam_saturation_temperature))
        out.append(self._to_str(self.fuel_higher_heating_value))
        out.append(self._to_str(self.design_heat_recovery_water_flow_rate))
        out.append(self._to_str(self.heat_recovery_inlet_node_name))
        out.append(self._to_str(self.heat_recovery_outlet_node_name))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.fuel_type))
        out.append(self._to_str(self.heat_recovery_maximum_temperature))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        return ",".join(out)