from collections import OrderedDict

class ChillerHeaterPerformanceElectricEir(object):
    """ Corresponds to IDD object `ChillerHeaterPerformance:Electric:EIR`
        This chiller model is a generic chiller-heater where the cooling mode performance is a
        function of condenser entering or leaving fluid temperature and the heating mode performance
        is typically a function of condenser leaving fluid temperature. Performance at off-reference
        conditions is modeled using three polynomial equations per mode. Six curve objects are required.
    """
    internal_name = "ChillerHeaterPerformance:Electric:EIR"
    field_count = 29

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ChillerHeaterPerformance:Electric:EIR`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Cooling Mode Evaporator Capacity"] = None
        self._data["Reference Cooling Mode COP"] = None
        self._data["Reference Cooling Mode Leaving Chilled Water Temperature"] = None
        self._data["Reference Cooling Mode Entering Condenser Fluid Temperature"] = None
        self._data["Reference Cooling Mode Leaving Condenser Water Temperature"] = None
        self._data["Reference Heating Mode Cooling Capacity Ratio"] = None
        self._data["Reference Heating Mode Cooling Power Input Ratio"] = None
        self._data["Reference Heating Mode Leaving Chilled Water Temperature"] = None
        self._data["Reference Heating Mode Leaving Condenser Water Temperature"] = None
        self._data["Reference Heating Mode Entering Condenser Fluid Temperature"] = None
        self._data["Heating Mode Entering Chilled Water Temperature Low Limit"] = None
        self._data["Chilled Water Flow Mode Type"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Design Hot Water Flow Rate"] = None
        self._data["Compressor Motor Efficiency"] = None
        self._data["Condenser Type"] = None
        self._data["Cooling Mode Temperature Curve Condenser Water Independent Variable"] = None
        self._data["Cooling Mode Cooling Capacity Function of Temperature Curve Name"] = None
        self._data["Cooling Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Cooling Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Cooling Mode Cooling Capacity Optimum Part Load Ratio"] = None
        self._data["Heating Mode Temperature Curve Condenser Water Independent Variable"] = None
        self._data["Heating Mode Cooling Capacity Function of Temperature Curve Name"] = None
        self._data["Heating Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Heating Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Heating Mode Cooling Capacity Optimum Part Load Ratio"] = None
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
            self.reference_cooling_mode_evaporator_capacity = None
        else:
            self.reference_cooling_mode_evaporator_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_cooling_mode_cop = None
        else:
            self.reference_cooling_mode_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_cooling_mode_leaving_chilled_water_temperature = None
        else:
            self.reference_cooling_mode_leaving_chilled_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_cooling_mode_entering_condenser_fluid_temperature = None
        else:
            self.reference_cooling_mode_entering_condenser_fluid_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_cooling_mode_leaving_condenser_water_temperature = None
        else:
            self.reference_cooling_mode_leaving_condenser_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_heating_mode_cooling_capacity_ratio = None
        else:
            self.reference_heating_mode_cooling_capacity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_heating_mode_cooling_power_input_ratio = None
        else:
            self.reference_heating_mode_cooling_power_input_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_heating_mode_leaving_chilled_water_temperature = None
        else:
            self.reference_heating_mode_leaving_chilled_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_heating_mode_leaving_condenser_water_temperature = None
        else:
            self.reference_heating_mode_leaving_condenser_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_heating_mode_entering_condenser_fluid_temperature = None
        else:
            self.reference_heating_mode_entering_condenser_fluid_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_mode_entering_chilled_water_temperature_low_limit = None
        else:
            self.heating_mode_entering_chilled_water_temperature_low_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_flow_mode_type = None
        else:
            self.chilled_water_flow_mode_type = vals[i]
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
            self.design_hot_water_flow_rate = None
        else:
            self.design_hot_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compressor_motor_efficiency = None
        else:
            self.compressor_motor_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_mode_temperature_curve_condenser_water_independent_variable = None
        else:
            self.cooling_mode_temperature_curve_condenser_water_independent_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_mode_cooling_capacity_function_of_temperature_curve_name = None
        else:
            self.cooling_mode_cooling_capacity_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_mode_cooling_capacity_optimum_part_load_ratio = None
        else:
            self.cooling_mode_cooling_capacity_optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_mode_temperature_curve_condenser_water_independent_variable = None
        else:
            self.heating_mode_temperature_curve_condenser_water_independent_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_mode_cooling_capacity_function_of_temperature_curve_name = None
        else:
            self.heating_mode_cooling_capacity_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_mode_cooling_capacity_optimum_part_load_ratio = None
        else:
            self.heating_mode_cooling_capacity_optimum_part_load_ratio = vals[i]
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
    def reference_cooling_mode_evaporator_capacity(self):
        """Get reference_cooling_mode_evaporator_capacity

        Returns:
            float: the value of `reference_cooling_mode_evaporator_capacity` or None if not set
        """
        return self._data["Reference Cooling Mode Evaporator Capacity"]

    @reference_cooling_mode_evaporator_capacity.setter
    def reference_cooling_mode_evaporator_capacity(self, value=None):
        """  Corresponds to IDD Field `reference_cooling_mode_evaporator_capacity`

        Args:
            value (float): value for IDD Field `reference_cooling_mode_evaporator_capacity`
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
                                 'for field `reference_cooling_mode_evaporator_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_cooling_mode_evaporator_capacity`')

        self._data["Reference Cooling Mode Evaporator Capacity"] = value

    @property
    def reference_cooling_mode_cop(self):
        """Get reference_cooling_mode_cop

        Returns:
            float: the value of `reference_cooling_mode_cop` or None if not set
        """
        return self._data["Reference Cooling Mode COP"]

    @reference_cooling_mode_cop.setter
    def reference_cooling_mode_cop(self, value=None):
        """  Corresponds to IDD Field `reference_cooling_mode_cop`
        Efficiency of the chiller compressor (cooling output/compressor energy input).

        Args:
            value (float): value for IDD Field `reference_cooling_mode_cop`
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
                                 'for field `reference_cooling_mode_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_cooling_mode_cop`')

        self._data["Reference Cooling Mode COP"] = value

    @property
    def reference_cooling_mode_leaving_chilled_water_temperature(self):
        """Get reference_cooling_mode_leaving_chilled_water_temperature

        Returns:
            float: the value of `reference_cooling_mode_leaving_chilled_water_temperature` or None if not set
        """
        return self._data["Reference Cooling Mode Leaving Chilled Water Temperature"]

    @reference_cooling_mode_leaving_chilled_water_temperature.setter
    def reference_cooling_mode_leaving_chilled_water_temperature(self, value=6.67 ):
        """  Corresponds to IDD Field `reference_cooling_mode_leaving_chilled_water_temperature`

        Args:
            value (float): value for IDD Field `reference_cooling_mode_leaving_chilled_water_temperature`
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
                                 'for field `reference_cooling_mode_leaving_chilled_water_temperature`'.format(value))

        self._data["Reference Cooling Mode Leaving Chilled Water Temperature"] = value

    @property
    def reference_cooling_mode_entering_condenser_fluid_temperature(self):
        """Get reference_cooling_mode_entering_condenser_fluid_temperature

        Returns:
            float: the value of `reference_cooling_mode_entering_condenser_fluid_temperature` or None if not set
        """
        return self._data["Reference Cooling Mode Entering Condenser Fluid Temperature"]

    @reference_cooling_mode_entering_condenser_fluid_temperature.setter
    def reference_cooling_mode_entering_condenser_fluid_temperature(self, value=29.44 ):
        """  Corresponds to IDD Field `reference_cooling_mode_entering_condenser_fluid_temperature`

        Args:
            value (float): value for IDD Field `reference_cooling_mode_entering_condenser_fluid_temperature`
                Unit: C
                Default value: 29.44
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_cooling_mode_entering_condenser_fluid_temperature`'.format(value))

        self._data["Reference Cooling Mode Entering Condenser Fluid Temperature"] = value

    @property
    def reference_cooling_mode_leaving_condenser_water_temperature(self):
        """Get reference_cooling_mode_leaving_condenser_water_temperature

        Returns:
            float: the value of `reference_cooling_mode_leaving_condenser_water_temperature` or None if not set
        """
        return self._data["Reference Cooling Mode Leaving Condenser Water Temperature"]

    @reference_cooling_mode_leaving_condenser_water_temperature.setter
    def reference_cooling_mode_leaving_condenser_water_temperature(self, value=35.0 ):
        """  Corresponds to IDD Field `reference_cooling_mode_leaving_condenser_water_temperature`

        Args:
            value (float): value for IDD Field `reference_cooling_mode_leaving_condenser_water_temperature`
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
                                 'for field `reference_cooling_mode_leaving_condenser_water_temperature`'.format(value))

        self._data["Reference Cooling Mode Leaving Condenser Water Temperature"] = value

    @property
    def reference_heating_mode_cooling_capacity_ratio(self):
        """Get reference_heating_mode_cooling_capacity_ratio

        Returns:
            float: the value of `reference_heating_mode_cooling_capacity_ratio` or None if not set
        """
        return self._data["Reference Heating Mode Cooling Capacity Ratio"]

    @reference_heating_mode_cooling_capacity_ratio.setter
    def reference_heating_mode_cooling_capacity_ratio(self, value=0.75 ):
        """  Corresponds to IDD Field `reference_heating_mode_cooling_capacity_ratio`
        During simultaneous cooling-heating mode, this ratio is relative to the Reference Cooling Mode Cooling Capacity
        (Evaporator capacity at simul clg-htg mode ref condition)/ (Evaporator capacity at cooling mode ref condition)

        Args:
            value (float): value for IDD Field `reference_heating_mode_cooling_capacity_ratio`
                Default value: 0.75
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_heating_mode_cooling_capacity_ratio`'.format(value))

        self._data["Reference Heating Mode Cooling Capacity Ratio"] = value

    @property
    def reference_heating_mode_cooling_power_input_ratio(self):
        """Get reference_heating_mode_cooling_power_input_ratio

        Returns:
            float: the value of `reference_heating_mode_cooling_power_input_ratio` or None if not set
        """
        return self._data["Reference Heating Mode Cooling Power Input Ratio"]

    @reference_heating_mode_cooling_power_input_ratio.setter
    def reference_heating_mode_cooling_power_input_ratio(self, value=1.38 ):
        """  Corresponds to IDD Field `reference_heating_mode_cooling_power_input_ratio`
        During simultaneous cooling-heating mode, this ratio is relative to the Reference Cooling Mode COP
        (Power at simultaneous clg-htg mode reference condition)/ (Power at cooling mode reference condition)

        Args:
            value (float): value for IDD Field `reference_heating_mode_cooling_power_input_ratio`
                Default value: 1.38
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
                                 'for field `reference_heating_mode_cooling_power_input_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_heating_mode_cooling_power_input_ratio`')

        self._data["Reference Heating Mode Cooling Power Input Ratio"] = value

    @property
    def reference_heating_mode_leaving_chilled_water_temperature(self):
        """Get reference_heating_mode_leaving_chilled_water_temperature

        Returns:
            float: the value of `reference_heating_mode_leaving_chilled_water_temperature` or None if not set
        """
        return self._data["Reference Heating Mode Leaving Chilled Water Temperature"]

    @reference_heating_mode_leaving_chilled_water_temperature.setter
    def reference_heating_mode_leaving_chilled_water_temperature(self, value=6.67 ):
        """  Corresponds to IDD Field `reference_heating_mode_leaving_chilled_water_temperature`
        During simultaneous cooling-heating mode

        Args:
            value (float): value for IDD Field `reference_heating_mode_leaving_chilled_water_temperature`
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
                                 'for field `reference_heating_mode_leaving_chilled_water_temperature`'.format(value))

        self._data["Reference Heating Mode Leaving Chilled Water Temperature"] = value

    @property
    def reference_heating_mode_leaving_condenser_water_temperature(self):
        """Get reference_heating_mode_leaving_condenser_water_temperature

        Returns:
            float: the value of `reference_heating_mode_leaving_condenser_water_temperature` or None if not set
        """
        return self._data["Reference Heating Mode Leaving Condenser Water Temperature"]

    @reference_heating_mode_leaving_condenser_water_temperature.setter
    def reference_heating_mode_leaving_condenser_water_temperature(self, value=49.0 ):
        """  Corresponds to IDD Field `reference_heating_mode_leaving_condenser_water_temperature`
        During simultaneous cooling-heating mode

        Args:
            value (float): value for IDD Field `reference_heating_mode_leaving_condenser_water_temperature`
                Unit: C
                Default value: 49.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_heating_mode_leaving_condenser_water_temperature`'.format(value))

        self._data["Reference Heating Mode Leaving Condenser Water Temperature"] = value

    @property
    def reference_heating_mode_entering_condenser_fluid_temperature(self):
        """Get reference_heating_mode_entering_condenser_fluid_temperature

        Returns:
            float: the value of `reference_heating_mode_entering_condenser_fluid_temperature` or None if not set
        """
        return self._data["Reference Heating Mode Entering Condenser Fluid Temperature"]

    @reference_heating_mode_entering_condenser_fluid_temperature.setter
    def reference_heating_mode_entering_condenser_fluid_temperature(self, value=29.44 ):
        """  Corresponds to IDD Field `reference_heating_mode_entering_condenser_fluid_temperature`

        Args:
            value (float): value for IDD Field `reference_heating_mode_entering_condenser_fluid_temperature`
                Unit: C
                Default value: 29.44
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_heating_mode_entering_condenser_fluid_temperature`'.format(value))

        self._data["Reference Heating Mode Entering Condenser Fluid Temperature"] = value

    @property
    def heating_mode_entering_chilled_water_temperature_low_limit(self):
        """Get heating_mode_entering_chilled_water_temperature_low_limit

        Returns:
            float: the value of `heating_mode_entering_chilled_water_temperature_low_limit` or None if not set
        """
        return self._data["Heating Mode Entering Chilled Water Temperature Low Limit"]

    @heating_mode_entering_chilled_water_temperature_low_limit.setter
    def heating_mode_entering_chilled_water_temperature_low_limit(self, value=12.22 ):
        """  Corresponds to IDD Field `heating_mode_entering_chilled_water_temperature_low_limit`
        During simultaneous cooling-heating mode

        Args:
            value (float): value for IDD Field `heating_mode_entering_chilled_water_temperature_low_limit`
                Unit: C
                Default value: 12.22
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `heating_mode_entering_chilled_water_temperature_low_limit`'.format(value))

        self._data["Heating Mode Entering Chilled Water Temperature Low Limit"] = value

    @property
    def chilled_water_flow_mode_type(self):
        """Get chilled_water_flow_mode_type

        Returns:
            str: the value of `chilled_water_flow_mode_type` or None if not set
        """
        return self._data["Chilled Water Flow Mode Type"]

    @chilled_water_flow_mode_type.setter
    def chilled_water_flow_mode_type(self, value="ConstantFlow"):
        """  Corresponds to IDD Field `chilled_water_flow_mode_type`
        Sets chilled water flow rate to either constant or variable.

        Args:
            value (str): value for IDD Field `chilled_water_flow_mode_type`
                Accepted values are:
                      - ConstantFlow
                      - VariableFlow
                Default value: ConstantFlow
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
                                 'for field `chilled_water_flow_mode_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_flow_mode_type`')
            vals = set()
            vals.add("ConstantFlow")
            vals.add("VariableFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chilled_water_flow_mode_type`'.format(value))

        self._data["Chilled Water Flow Mode Type"] = value

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
    def design_hot_water_flow_rate(self):
        """Get design_hot_water_flow_rate

        Returns:
            float: the value of `design_hot_water_flow_rate` or None if not set
        """
        return self._data["Design Hot Water Flow Rate"]

    @design_hot_water_flow_rate.setter
    def design_hot_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_hot_water_flow_rate`

        Args:
            value (float): value for IDD Field `design_hot_water_flow_rate`
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
                                 'for field `design_hot_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_hot_water_flow_rate`')

        self._data["Design Hot Water Flow Rate"] = value

    @property
    def compressor_motor_efficiency(self):
        """Get compressor_motor_efficiency

        Returns:
            float: the value of `compressor_motor_efficiency` or None if not set
        """
        return self._data["Compressor Motor Efficiency"]

    @compressor_motor_efficiency.setter
    def compressor_motor_efficiency(self, value=1.0 ):
        """  Corresponds to IDD Field `compressor_motor_efficiency`
        Fraction of compressor electrical energy that must be rejected by the condenser.
        Enter 1.0 or leave this field blank for a hermetic compressor.

        Args:
            value (float): value for IDD Field `compressor_motor_efficiency`
                Default value: 1.0
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
                                 'for field `compressor_motor_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `compressor_motor_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `compressor_motor_efficiency`')

        self._data["Compressor Motor Efficiency"] = value

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
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

    @property
    def cooling_mode_temperature_curve_condenser_water_independent_variable(self):
        """Get cooling_mode_temperature_curve_condenser_water_independent_variable

        Returns:
            str: the value of `cooling_mode_temperature_curve_condenser_water_independent_variable` or None if not set
        """
        return self._data["Cooling Mode Temperature Curve Condenser Water Independent Variable"]

    @cooling_mode_temperature_curve_condenser_water_independent_variable.setter
    def cooling_mode_temperature_curve_condenser_water_independent_variable(self, value="EnteringCondenser"):
        """  Corresponds to IDD Field `cooling_mode_temperature_curve_condenser_water_independent_variable`
        Sets the second independent variable in the three temperature dependent performance
        curves to either the leaving or entering condenser water temperature. Manufacturers
        express the performance of their chillers using either the leaving condenser water
        temperature (to the tower) or the entering condenser water temperature (from the tower).
        Cooling mode is generally a stronger function of Entering Condenser Fluid Temperature

        Args:
            value (str): value for IDD Field `cooling_mode_temperature_curve_condenser_water_independent_variable`
                Accepted values are:
                      - EnteringCondenser
                      - LeavingCondenser
                Default value: EnteringCondenser
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
                                 'for field `cooling_mode_temperature_curve_condenser_water_independent_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_mode_temperature_curve_condenser_water_independent_variable`')
            vals = set()
            vals.add("EnteringCondenser")
            vals.add("LeavingCondenser")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_mode_temperature_curve_condenser_water_independent_variable`'.format(value))

        self._data["Cooling Mode Temperature Curve Condenser Water Independent Variable"] = value

    @property
    def cooling_mode_cooling_capacity_function_of_temperature_curve_name(self):
        """Get cooling_mode_cooling_capacity_function_of_temperature_curve_name

        Returns:
            str: the value of `cooling_mode_cooling_capacity_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Mode Cooling Capacity Function of Temperature Curve Name"]

    @cooling_mode_cooling_capacity_function_of_temperature_curve_name.setter
    def cooling_mode_cooling_capacity_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_mode_cooling_capacity_function_of_temperature_curve_name`
        Cooling capacity as a function of leaving chilled water temperature
        and either entering or leaving condenser fluid temperature
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*TCond + e*TCond**2 + f*CWS*TCond
        If ClgModeCondWaterCurveInputVariable = EnteringCondenser, TCond = ECT
        If ClgModeCondWaterCurveInputVariable = LeavingCondenser, TCond = LCT
        CWS = supply (leaving) chilled water temperature(C)
        LCT = leaving condenser fluid temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `cooling_mode_cooling_capacity_function_of_temperature_curve_name`
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
                                 'for field `cooling_mode_cooling_capacity_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_mode_cooling_capacity_function_of_temperature_curve_name`')

        self._data["Cooling Mode Cooling Capacity Function of Temperature Curve Name"] = value

    @property
    def cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        Electric Input Ratio (EIR) as a function of supply (leaving) chilled water temperature
        and leaving condenser fluid temperature.   EIR = 1/COP.
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*TCond + e*TCond**2 + f*CWS*TCond
        If ClgModeCondWaterCurveInputVariable = EnteringCondenser, TCond = ECT
        If ClgModeCondWaterCurveInputVariable = LeavingCondenser, TCond = LCT
        CWS = supply (leaving) chilled water temperature(C)
        LCT = leaving condenser fluid temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
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
                                 'for field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Cooling Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Cooling Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        Electric Input Ratio (EIR) as a function of Part Load Ratio (PLR)
        EIR = 1/COP
        Table:OneIndependentVariable object can also be used
        Table:TwoIndependentVariables object can also be used
        Bicubic = a + b*TCond + c*TCond**2 + d*PLR + e*PLR**2 + f*TCond*PLR +g*0 + h*PLR**3+i*0+j*0
        If ClgModeCondWaterCurveInputVariable = EnteringCondenser, TCond = ECT
        If ClgModeCondWaterCurveInputVariable = LeavingCondenser, TCond = LCT
        Normally, a bicubic curve here should be in terms of LCT rather than ECT
        Also, a bicubic curve is more applicable for variable-speed compressor motor drives
        or
        Quadratic = a + b*PLR + c*PLR**2
        PLR = part load ratio (cooling load/steady-state capacity)
        LCT = leaving condenser fluid temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
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
                                 'for field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Cooling Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def cooling_mode_cooling_capacity_optimum_part_load_ratio(self):
        """Get cooling_mode_cooling_capacity_optimum_part_load_ratio

        Returns:
            float: the value of `cooling_mode_cooling_capacity_optimum_part_load_ratio` or None if not set
        """
        return self._data["Cooling Mode Cooling Capacity Optimum Part Load Ratio"]

    @cooling_mode_cooling_capacity_optimum_part_load_ratio.setter
    def cooling_mode_cooling_capacity_optimum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `cooling_mode_cooling_capacity_optimum_part_load_ratio`
        Optimum part load ratio where the chiller is most efficient.
        Must be greater than or equal to the Minimum Part Load Ratio
        and less than or equal to the Maximum Part Load Ratio.
        The Min/Max PLR are taken from their assoicated EIR-FPLR curve references.

        Args:
            value (float): value for IDD Field `cooling_mode_cooling_capacity_optimum_part_load_ratio`
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
                                 'for field `cooling_mode_cooling_capacity_optimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_mode_cooling_capacity_optimum_part_load_ratio`')

        self._data["Cooling Mode Cooling Capacity Optimum Part Load Ratio"] = value

    @property
    def heating_mode_temperature_curve_condenser_water_independent_variable(self):
        """Get heating_mode_temperature_curve_condenser_water_independent_variable

        Returns:
            str: the value of `heating_mode_temperature_curve_condenser_water_independent_variable` or None if not set
        """
        return self._data["Heating Mode Temperature Curve Condenser Water Independent Variable"]

    @heating_mode_temperature_curve_condenser_water_independent_variable.setter
    def heating_mode_temperature_curve_condenser_water_independent_variable(self, value="LeavingCondenser"):
        """  Corresponds to IDD Field `heating_mode_temperature_curve_condenser_water_independent_variable`
        Sets the second independent variable in the three temperature dependent performance
        curves to either the leaving or entering condenser water temperature. Manufacturers
        express the performance of their chillers using either the leaving condenser water
        temperature (to the tower) or the entering condenser water temperature (from the tower).
        Heating mode (or Simul Clg/Htg Load) should be a function of Leaving Condenser Fluid Temperature
        Only use EnteringCondenser as a last resort in case no performance data exists for LeavingCondenser

        Args:
            value (str): value for IDD Field `heating_mode_temperature_curve_condenser_water_independent_variable`
                Accepted values are:
                      - EnteringCondenser
                      - LeavingCondenser
                Default value: LeavingCondenser
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
                                 'for field `heating_mode_temperature_curve_condenser_water_independent_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_mode_temperature_curve_condenser_water_independent_variable`')
            vals = set()
            vals.add("EnteringCondenser")
            vals.add("LeavingCondenser")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_mode_temperature_curve_condenser_water_independent_variable`'.format(value))

        self._data["Heating Mode Temperature Curve Condenser Water Independent Variable"] = value

    @property
    def heating_mode_cooling_capacity_function_of_temperature_curve_name(self):
        """Get heating_mode_cooling_capacity_function_of_temperature_curve_name

        Returns:
            str: the value of `heating_mode_cooling_capacity_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Heating Mode Cooling Capacity Function of Temperature Curve Name"]

    @heating_mode_cooling_capacity_function_of_temperature_curve_name.setter
    def heating_mode_cooling_capacity_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_mode_cooling_capacity_function_of_temperature_curve_name`
        Evaporator (cooling) capacity as a function of leaving chilled water temperature
        and leaving condenser fluid temperature when in heating or simultaneous cool/heat mode
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*TCond + e*TCond**2 + f*CWS*TCond
        If independent variable = EnteringCondenser, TCond = ECT
        If independent variable = LeavingCondenser, TCond = LCT
        CWS = supply (leaving) chilled water temperature(C)
        LCT = leaving condenser fluid temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `heating_mode_cooling_capacity_function_of_temperature_curve_name`
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
                                 'for field `heating_mode_cooling_capacity_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_mode_cooling_capacity_function_of_temperature_curve_name`')

        self._data["Heating Mode Cooling Capacity Function of Temperature Curve Name"] = value

    @property
    def heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Heating Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        Electric Input Ratio (EIR) as a function of leaving chilled water temperature when in heating or simultaneous cool/heat mode
        and leaving condenser fluid temperature.   EIR = 1/COP.
        Table:TwoIndependentVariables object can also be used
        curve = a + b*CWS + c*CWS**2 + d*TCond + e*TCond**2 + f*CWS*TCond
        If independent variable = EnteringCondenser, TCond = ECT
        If independent variable = LeavingCondenser, TCond = LCT
        CWS = leaving chilled water temperature(C)
        LCT = leaving condenser fluid temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
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
                                 'for field `heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Heating Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Heating Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        Electric Input Ratio (EIR) as a function of Part Load Ratio (PLR) when in heating or simultaneous cool/heat mode
        EIR = 1/COP
        Table:OneIndependentVariable object can also be used
        Table:TwoIndependentVariables object can also be used
        Bicubic = a + b*LCT + c*LCT**2 + d*PLR + e*PLR**2 + f*LCT*PLR + g*0 + h*PLR**3 + i*0 + j*0
        Normally, a bicubic curve here should be in terms of LCT rather than ECT
        Also, a bicubic curve is more applicable for variable-speed compressor motor drives
        or
        Quadratic = a + b*PLR + c*PLR**2
        PLR = part load ratio (cooling load/steady-state capacity)
        LCT = leaving condenser fluid temperature(C)
        ECT = entering condenser fluid temperature(C)

        Args:
            value (str): value for IDD Field `heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
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
                                 'for field `heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Heating Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def heating_mode_cooling_capacity_optimum_part_load_ratio(self):
        """Get heating_mode_cooling_capacity_optimum_part_load_ratio

        Returns:
            float: the value of `heating_mode_cooling_capacity_optimum_part_load_ratio` or None if not set
        """
        return self._data["Heating Mode Cooling Capacity Optimum Part Load Ratio"]

    @heating_mode_cooling_capacity_optimum_part_load_ratio.setter
    def heating_mode_cooling_capacity_optimum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `heating_mode_cooling_capacity_optimum_part_load_ratio`
        Optimum part load ratio where the chiller is most efficient when in heating or simultaneous cool/heat mode.
        Must be greater than or equal to the Minimum Part Load Ratio
        and less than or equal to the Maximum Part Load Ratio.
        The Min/Max PLR are taken from their assoicated EIR-FPLR curve references.

        Args:
            value (float): value for IDD Field `heating_mode_cooling_capacity_optimum_part_load_ratio`
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
                                 'for field `heating_mode_cooling_capacity_optimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_mode_cooling_capacity_optimum_part_load_ratio`')

        self._data["Heating Mode Cooling Capacity Optimum Part Load Ratio"] = value

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
        out.append(self._to_str(self.reference_cooling_mode_evaporator_capacity))
        out.append(self._to_str(self.reference_cooling_mode_cop))
        out.append(self._to_str(self.reference_cooling_mode_leaving_chilled_water_temperature))
        out.append(self._to_str(self.reference_cooling_mode_entering_condenser_fluid_temperature))
        out.append(self._to_str(self.reference_cooling_mode_leaving_condenser_water_temperature))
        out.append(self._to_str(self.reference_heating_mode_cooling_capacity_ratio))
        out.append(self._to_str(self.reference_heating_mode_cooling_power_input_ratio))
        out.append(self._to_str(self.reference_heating_mode_leaving_chilled_water_temperature))
        out.append(self._to_str(self.reference_heating_mode_leaving_condenser_water_temperature))
        out.append(self._to_str(self.reference_heating_mode_entering_condenser_fluid_temperature))
        out.append(self._to_str(self.heating_mode_entering_chilled_water_temperature_low_limit))
        out.append(self._to_str(self.chilled_water_flow_mode_type))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.design_hot_water_flow_rate))
        out.append(self._to_str(self.compressor_motor_efficiency))
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.cooling_mode_temperature_curve_condenser_water_independent_variable))
        out.append(self._to_str(self.cooling_mode_cooling_capacity_function_of_temperature_curve_name))
        out.append(self._to_str(self.cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.cooling_mode_cooling_capacity_optimum_part_load_ratio))
        out.append(self._to_str(self.heating_mode_temperature_curve_condenser_water_independent_variable))
        out.append(self._to_str(self.heating_mode_cooling_capacity_function_of_temperature_curve_name))
        out.append(self._to_str(self.heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.heating_mode_cooling_capacity_optimum_part_load_ratio))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)