from collections import OrderedDict

class CoilPerformanceDxCooling(object):
    """ Corresponds to IDD object `CoilPerformance:DX:Cooling`
        Used to specify DX cooling coil performance for one mode of operation for a
        Coil:Cooling:DX:TwoStageWithHumidityControlMode object which may reference one to four
        CoilPerformance:DX:Cooling objects depending on the specified number of stages and
        dehumidification modes. In nearly all cases, the Rated Air Flow Rate will be the same
        for all performance objects associated with a given coil. If bypass is specified,
        the Rated Air Flow Rate includes both the bypassed flow and the flow through the
        active part of the coil.
    """
    internal_name = "CoilPerformance:DX:Cooling"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoilPerformance:DX:Cooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Gross Rated Total Cooling Capacity"] = None
        self._data["Gross Rated Sensible Heat Ratio"] = None
        self._data["Gross Rated Cooling COP"] = None
        self._data["Rated Air Flow Rate"] = None
        self._data["Fraction of Air Flow Bypassed Around Coil"] = None
        self._data["Total Cooling Capacity Function of Temperature Curve Name"] = None
        self._data["Total Cooling Capacity Function of Flow Fraction Curve Name"] = None
        self._data["Energy Input Ratio Function of Temperature Curve Name"] = None
        self._data["Energy Input Ratio Function of Flow Fraction Curve Name"] = None
        self._data["Part Load Fraction Correlation Curve Name"] = None
        self._data["Nominal Time for Condensate Removal to Begin"] = None
        self._data["Ratio of Initial Moisture Evaporation Rate and Steady State Latent Capacity"] = None
        self._data["Maximum Cycling Rate"] = None
        self._data["Latent Capacity Time Constant"] = None
        self._data["Condenser Air Inlet Node Name"] = None
        self._data["Condenser Type"] = None
        self._data["Evaporative Condenser Effectiveness"] = None
        self._data["Evaporative Condenser Air Flow Rate"] = None
        self._data["Evaporative Condenser Pump Rated Power Consumption"] = None
        self._data["Sensible Heat Ratio Function of Temperature Curve Name"] = None
        self._data["Sensible Heat Ratio Function of Flow Fraction Curve Name"] = None

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
            self.gross_rated_total_cooling_capacity = None
        else:
            self.gross_rated_total_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gross_rated_sensible_heat_ratio = None
        else:
            self.gross_rated_sensible_heat_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gross_rated_cooling_cop = None
        else:
            self.gross_rated_cooling_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_air_flow_rate = None
        else:
            self.rated_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_air_flow_bypassed_around_coil = None
        else:
            self.fraction_of_air_flow_bypassed_around_coil = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_cooling_capacity_function_of_temperature_curve_name = None
        else:
            self.total_cooling_capacity_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_cooling_capacity_function_of_flow_fraction_curve_name = None
        else:
            self.total_cooling_capacity_function_of_flow_fraction_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.energy_input_ratio_function_of_temperature_curve_name = None
        else:
            self.energy_input_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.energy_input_ratio_function_of_flow_fraction_curve_name = None
        else:
            self.energy_input_ratio_function_of_flow_fraction_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.part_load_fraction_correlation_curve_name = None
        else:
            self.part_load_fraction_correlation_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_time_for_condensate_removal_to_begin = None
        else:
            self.nominal_time_for_condensate_removal_to_begin = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = None
        else:
            self.ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_cycling_rate = None
        else:
            self.maximum_cycling_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latent_capacity_time_constant = None
        else:
            self.latent_capacity_time_constant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_air_inlet_node_name = None
        else:
            self.condenser_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evaporative_condenser_effectiveness = None
        else:
            self.evaporative_condenser_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evaporative_condenser_air_flow_rate = None
        else:
            self.evaporative_condenser_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evaporative_condenser_pump_rated_power_consumption = None
        else:
            self.evaporative_condenser_pump_rated_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_heat_ratio_function_of_temperature_curve_name = None
        else:
            self.sensible_heat_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_heat_ratio_function_of_flow_fraction_curve_name = None
        else:
            self.sensible_heat_ratio_function_of_flow_fraction_curve_name = vals[i]
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
    def gross_rated_total_cooling_capacity(self):
        """Get gross_rated_total_cooling_capacity

        Returns:
            float: the value of `gross_rated_total_cooling_capacity` or None if not set
        """
        return self._data["Gross Rated Total Cooling Capacity"]

    @gross_rated_total_cooling_capacity.setter
    def gross_rated_total_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `gross_rated_total_cooling_capacity`
        Total cooling capacity not accounting for the effect of supply air fan heat
        gross capacity excluding supply air fan heat
        rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and
        air entering the outdoor condenser coil at 35 C dry-bulb/23.9 C wet-bulb

        Args:
            value (float): value for IDD Field `gross_rated_total_cooling_capacity`
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
                                 'for field `gross_rated_total_cooling_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gross_rated_total_cooling_capacity`')

        self._data["Gross Rated Total Cooling Capacity"] = value

    @property
    def gross_rated_sensible_heat_ratio(self):
        """Get gross_rated_sensible_heat_ratio

        Returns:
            float: the value of `gross_rated_sensible_heat_ratio` or None if not set
        """
        return self._data["Gross Rated Sensible Heat Ratio"]

    @gross_rated_sensible_heat_ratio.setter
    def gross_rated_sensible_heat_ratio(self, value=None):
        """  Corresponds to IDD Field `gross_rated_sensible_heat_ratio`
        Rated sensible heat ratio (gross sensible capacity/gross total capacity)
        sensible and total capacities do not include supply fan heat

        Args:
            value (float): value for IDD Field `gross_rated_sensible_heat_ratio`
                value >= 0.5
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
                                 'for field `gross_rated_sensible_heat_ratio`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `gross_rated_sensible_heat_ratio`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `gross_rated_sensible_heat_ratio`')

        self._data["Gross Rated Sensible Heat Ratio"] = value

    @property
    def gross_rated_cooling_cop(self):
        """Get gross_rated_cooling_cop

        Returns:
            float: the value of `gross_rated_cooling_cop` or None if not set
        """
        return self._data["Gross Rated Cooling COP"]

    @gross_rated_cooling_cop.setter
    def gross_rated_cooling_cop(self, value=3.0 ):
        """  Corresponds to IDD Field `gross_rated_cooling_cop`
        Gross cooling capacity divided by power input to the compressor and outdoor fan,
        does not include supply fan heat or supply fan electrical energy input

        Args:
            value (float): value for IDD Field `gross_rated_cooling_cop`
                Unit: W/W
                Default value: 3.0
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
                                 'for field `gross_rated_cooling_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gross_rated_cooling_cop`')

        self._data["Gross Rated Cooling COP"] = value

    @property
    def rated_air_flow_rate(self):
        """Get rated_air_flow_rate

        Returns:
            float: the value of `rated_air_flow_rate` or None if not set
        """
        return self._data["Rated Air Flow Rate"]

    @rated_air_flow_rate.setter
    def rated_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_air_flow_rate`
        Flow rate corresponding to Rated total Cooling capacity, Rated SHR and Rated COP

        Args:
            value (float): value for IDD Field `rated_air_flow_rate`
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
                                 'for field `rated_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_air_flow_rate`')

        self._data["Rated Air Flow Rate"] = value

    @property
    def fraction_of_air_flow_bypassed_around_coil(self):
        """Get fraction_of_air_flow_bypassed_around_coil

        Returns:
            float: the value of `fraction_of_air_flow_bypassed_around_coil` or None if not set
        """
        return self._data["Fraction of Air Flow Bypassed Around Coil"]

    @fraction_of_air_flow_bypassed_around_coil.setter
    def fraction_of_air_flow_bypassed_around_coil(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_of_air_flow_bypassed_around_coil`
        Fraction of Rated Air Flow Rate which bypasses the cooling coil
        in this performance mode.  The remaining portion of the flow
        should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity.
        This is used to model face-split coils on multi-stage units or bypass dampers.
        If total flow rate varies during simulation, the same fraction is bypassed.

        Args:
            value (float): value for IDD Field `fraction_of_air_flow_bypassed_around_coil`
                Default value: 0.0
                value >= 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_air_flow_bypassed_around_coil`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_air_flow_bypassed_around_coil`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_air_flow_bypassed_around_coil`')

        self._data["Fraction of Air Flow Bypassed Around Coil"] = value

    @property
    def total_cooling_capacity_function_of_temperature_curve_name(self):
        """Get total_cooling_capacity_function_of_temperature_curve_name

        Returns:
            str: the value of `total_cooling_capacity_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Total Cooling Capacity Function of Temperature Curve Name"]

    @total_cooling_capacity_function_of_temperature_curve_name.setter
    def total_cooling_capacity_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `total_cooling_capacity_function_of_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb
        wb = entering wet-bulb temperature (C)
        edb = dry-bulb temperature seen by the condenser (C)

        Args:
            value (str): value for IDD Field `total_cooling_capacity_function_of_temperature_curve_name`
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
                                 'for field `total_cooling_capacity_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `total_cooling_capacity_function_of_temperature_curve_name`')

        self._data["Total Cooling Capacity Function of Temperature Curve Name"] = value

    @property
    def total_cooling_capacity_function_of_flow_fraction_curve_name(self):
        """Get total_cooling_capacity_function_of_flow_fraction_curve_name

        Returns:
            str: the value of `total_cooling_capacity_function_of_flow_fraction_curve_name` or None if not set
        """
        return self._data["Total Cooling Capacity Function of Flow Fraction Curve Name"]

    @total_cooling_capacity_function_of_flow_fraction_curve_name.setter
    def total_cooling_capacity_function_of_flow_fraction_curve_name(self, value=None):
        """  Corresponds to IDD Field `total_cooling_capacity_function_of_flow_fraction_curve_name`
        Table:OneIndependentVariable object can also be used
        quadratic curve = a + b*ff + c*ff**2
        cubic curve = a + b*ff + c*ff**2 + d*ff**3
        ff = fraction of the full load flow

        Args:
            value (str): value for IDD Field `total_cooling_capacity_function_of_flow_fraction_curve_name`
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
                                 'for field `total_cooling_capacity_function_of_flow_fraction_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `total_cooling_capacity_function_of_flow_fraction_curve_name`')

        self._data["Total Cooling Capacity Function of Flow Fraction Curve Name"] = value

    @property
    def energy_input_ratio_function_of_temperature_curve_name(self):
        """Get energy_input_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `energy_input_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Energy Input Ratio Function of Temperature Curve Name"]

    @energy_input_ratio_function_of_temperature_curve_name.setter
    def energy_input_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `energy_input_ratio_function_of_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb
        wb = entering wet-bulb temperature (C)
        edb = dry-bulb temperature seen by the condenser (C)

        Args:
            value (str): value for IDD Field `energy_input_ratio_function_of_temperature_curve_name`
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
                                 'for field `energy_input_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `energy_input_ratio_function_of_temperature_curve_name`')

        self._data["Energy Input Ratio Function of Temperature Curve Name"] = value

    @property
    def energy_input_ratio_function_of_flow_fraction_curve_name(self):
        """Get energy_input_ratio_function_of_flow_fraction_curve_name

        Returns:
            str: the value of `energy_input_ratio_function_of_flow_fraction_curve_name` or None if not set
        """
        return self._data["Energy Input Ratio Function of Flow Fraction Curve Name"]

    @energy_input_ratio_function_of_flow_fraction_curve_name.setter
    def energy_input_ratio_function_of_flow_fraction_curve_name(self, value=None):
        """  Corresponds to IDD Field `energy_input_ratio_function_of_flow_fraction_curve_name`
        Table:OneIndependentVariable object can also be used
        quadratic curve = a + b*ff + c*ff**2
        cubic curve = a + b*ff + c*ff**2 + d*ff**3
        ff = fraction of the full load flow

        Args:
            value (str): value for IDD Field `energy_input_ratio_function_of_flow_fraction_curve_name`
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
                                 'for field `energy_input_ratio_function_of_flow_fraction_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `energy_input_ratio_function_of_flow_fraction_curve_name`')

        self._data["Energy Input Ratio Function of Flow Fraction Curve Name"] = value

    @property
    def part_load_fraction_correlation_curve_name(self):
        """Get part_load_fraction_correlation_curve_name

        Returns:
            str: the value of `part_load_fraction_correlation_curve_name` or None if not set
        """
        return self._data["Part Load Fraction Correlation Curve Name"]

    @part_load_fraction_correlation_curve_name.setter
    def part_load_fraction_correlation_curve_name(self, value=None):
        """  Corresponds to IDD Field `part_load_fraction_correlation_curve_name`
        Table:OneIndependentVariable object can also be used
        quadratic curve = a + b*PLR + c*PLR**2
        cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3
        PLR = part load ratio (cooling load/steady state capacity)

        Args:
            value (str): value for IDD Field `part_load_fraction_correlation_curve_name`
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
                                 'for field `part_load_fraction_correlation_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `part_load_fraction_correlation_curve_name`')

        self._data["Part Load Fraction Correlation Curve Name"] = value

    @property
    def nominal_time_for_condensate_removal_to_begin(self):
        """Get nominal_time_for_condensate_removal_to_begin

        Returns:
            float: the value of `nominal_time_for_condensate_removal_to_begin` or None if not set
        """
        return self._data["Nominal Time for Condensate Removal to Begin"]

    @nominal_time_for_condensate_removal_to_begin.setter
    def nominal_time_for_condensate_removal_to_begin(self, value=0.0 ):
        """  Corresponds to IDD Field `nominal_time_for_condensate_removal_to_begin`
        The nominal time for condensate to begin leaving the coil's condensate
        drain line at the coil's rated air flow rate and temperature conditions.
        Nominal time is equal to the ratio of the energy of the coil's maximum
        condensate holding capacity (J) to the coil's steady state latent capacity (W).
        Suggested value is 1000; zero value means latent degradation model is disabled.

        Args:
            value (float): value for IDD Field `nominal_time_for_condensate_removal_to_begin`
                Unit: s
                Default value: 0.0
                value >= 0.0
                value <= 3000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_time_for_condensate_removal_to_begin`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_time_for_condensate_removal_to_begin`')
            if value > 3000.0:
                raise ValueError('value need to be smaller 3000.0 '
                                 'for field `nominal_time_for_condensate_removal_to_begin`')

        self._data["Nominal Time for Condensate Removal to Begin"] = value

    @property
    def ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity(self):
        """Get ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity

        Returns:
            float: the value of `ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity` or None if not set
        """
        return self._data["Ratio of Initial Moisture Evaporation Rate and Steady State Latent Capacity"]

    @ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity.setter
    def ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity`
        Ratio of the initial moisture evaporation rate from the cooling coil (when
        the compressor first turns off) and the coil's steady state latent capacity
        at rated air flow rate and temperature conditions. Suggested value is 1.5; zero value
        means latent degradation model is disabled.

        Args:
            value (float): value for IDD Field `ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 5.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity`')
            if value > 5.0:
                raise ValueError('value need to be smaller 5.0 '
                                 'for field `ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity`')

        self._data["Ratio of Initial Moisture Evaporation Rate and Steady State Latent Capacity"] = value

    @property
    def maximum_cycling_rate(self):
        """Get maximum_cycling_rate

        Returns:
            float: the value of `maximum_cycling_rate` or None if not set
        """
        return self._data["Maximum Cycling Rate"]

    @maximum_cycling_rate.setter
    def maximum_cycling_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `maximum_cycling_rate`
        The maximum on-off cycling rate for the compressor, which occurs at 50% run time
        fraction. Suggested value is 3; zero value means latent degradation model is disabled.

        Args:
            value (float): value for IDD Field `maximum_cycling_rate`
                Unit: cycles/hr
                Default value: 0.0
                value >= 0.0
                value <= 5.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_cycling_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_cycling_rate`')
            if value > 5.0:
                raise ValueError('value need to be smaller 5.0 '
                                 'for field `maximum_cycling_rate`')

        self._data["Maximum Cycling Rate"] = value

    @property
    def latent_capacity_time_constant(self):
        """Get latent_capacity_time_constant

        Returns:
            float: the value of `latent_capacity_time_constant` or None if not set
        """
        return self._data["Latent Capacity Time Constant"]

    @latent_capacity_time_constant.setter
    def latent_capacity_time_constant(self, value=0.0 ):
        """  Corresponds to IDD Field `latent_capacity_time_constant`
        Time constant for the cooling coil's latent capacity to reach steady state after
        startup. Suggested value is 45; zero value means latent degradation model is disabled.

        Args:
            value (float): value for IDD Field `latent_capacity_time_constant`
                Unit: s
                Default value: 0.0
                value >= 0.0
                value <= 500.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `latent_capacity_time_constant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `latent_capacity_time_constant`')
            if value > 500.0:
                raise ValueError('value need to be smaller 500.0 '
                                 'for field `latent_capacity_time_constant`')

        self._data["Latent Capacity Time Constant"] = value

    @property
    def condenser_air_inlet_node_name(self):
        """Get condenser_air_inlet_node_name

        Returns:
            str: the value of `condenser_air_inlet_node_name` or None if not set
        """
        return self._data["Condenser Air Inlet Node Name"]

    @condenser_air_inlet_node_name.setter
    def condenser_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_air_inlet_node_name`
        Enter the name of an outdoor air node. This node name is also specified in
        an OutdoorAir:Node or OutdoorAir:NodeList object.

        Args:
            value (str): value for IDD Field `condenser_air_inlet_node_name`
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
                                 'for field `condenser_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_air_inlet_node_name`')

        self._data["Condenser Air Inlet Node Name"] = value

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
            vals.add("EvaporativelyCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

    @property
    def evaporative_condenser_effectiveness(self):
        """Get evaporative_condenser_effectiveness

        Returns:
            float: the value of `evaporative_condenser_effectiveness` or None if not set
        """
        return self._data["Evaporative Condenser Effectiveness"]

    @evaporative_condenser_effectiveness.setter
    def evaporative_condenser_effectiveness(self, value=0.9 ):
        """  Corresponds to IDD Field `evaporative_condenser_effectiveness`

        Args:
            value (float): value for IDD Field `evaporative_condenser_effectiveness`
                Unit: dimensionless
                Default value: 0.9
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
                                 'for field `evaporative_condenser_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evaporative_condenser_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `evaporative_condenser_effectiveness`')

        self._data["Evaporative Condenser Effectiveness"] = value

    @property
    def evaporative_condenser_air_flow_rate(self):
        """Get evaporative_condenser_air_flow_rate

        Returns:
            float: the value of `evaporative_condenser_air_flow_rate` or None if not set
        """
        return self._data["Evaporative Condenser Air Flow Rate"]

    @evaporative_condenser_air_flow_rate.setter
    def evaporative_condenser_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `evaporative_condenser_air_flow_rate`
        Used to calculate evaporative condenser water use

        Args:
            value (float): value for IDD Field `evaporative_condenser_air_flow_rate`
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
                                 'for field `evaporative_condenser_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `evaporative_condenser_air_flow_rate`')

        self._data["Evaporative Condenser Air Flow Rate"] = value

    @property
    def evaporative_condenser_pump_rated_power_consumption(self):
        """Get evaporative_condenser_pump_rated_power_consumption

        Returns:
            float: the value of `evaporative_condenser_pump_rated_power_consumption` or None if not set
        """
        return self._data["Evaporative Condenser Pump Rated Power Consumption"]

    @evaporative_condenser_pump_rated_power_consumption.setter
    def evaporative_condenser_pump_rated_power_consumption(self, value=0.0 ):
        """  Corresponds to IDD Field `evaporative_condenser_pump_rated_power_consumption`
        Rated power consumed by the evaporative condenser's water pump

        Args:
            value (float): value for IDD Field `evaporative_condenser_pump_rated_power_consumption`
                Unit: W
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
                                 'for field `evaporative_condenser_pump_rated_power_consumption`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evaporative_condenser_pump_rated_power_consumption`')

        self._data["Evaporative Condenser Pump Rated Power Consumption"] = value

    @property
    def sensible_heat_ratio_function_of_temperature_curve_name(self):
        """Get sensible_heat_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `sensible_heat_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Sensible Heat Ratio Function of Temperature Curve Name"]

    @sensible_heat_ratio_function_of_temperature_curve_name.setter
    def sensible_heat_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `sensible_heat_ratio_function_of_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db
        wb = entering wet-bulb temperature seen by the DX cooling coil (C)
        db = entering dry-bulb temperature seen by the DX cooling coil (C)
        entering temperature can be outside air or pretreated air.

        Args:
            value (str): value for IDD Field `sensible_heat_ratio_function_of_temperature_curve_name`
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
                                 'for field `sensible_heat_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensible_heat_ratio_function_of_temperature_curve_name`')

        self._data["Sensible Heat Ratio Function of Temperature Curve Name"] = value

    @property
    def sensible_heat_ratio_function_of_flow_fraction_curve_name(self):
        """Get sensible_heat_ratio_function_of_flow_fraction_curve_name

        Returns:
            str: the value of `sensible_heat_ratio_function_of_flow_fraction_curve_name` or None if not set
        """
        return self._data["Sensible Heat Ratio Function of Flow Fraction Curve Name"]

    @sensible_heat_ratio_function_of_flow_fraction_curve_name.setter
    def sensible_heat_ratio_function_of_flow_fraction_curve_name(self, value=None):
        """  Corresponds to IDD Field `sensible_heat_ratio_function_of_flow_fraction_curve_name`
        Table:OneIndependentVariable object can also be used
        quadratic curve = a + b*ff + c*ff**2
        cubic curve = a + b*ff + c*ff**2 + d*ff**3
        ff = fraction of the full load flow

        Args:
            value (str): value for IDD Field `sensible_heat_ratio_function_of_flow_fraction_curve_name`
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
                                 'for field `sensible_heat_ratio_function_of_flow_fraction_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensible_heat_ratio_function_of_flow_fraction_curve_name`')

        self._data["Sensible Heat Ratio Function of Flow Fraction Curve Name"] = value

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
        out.append(self._to_str(self.gross_rated_total_cooling_capacity))
        out.append(self._to_str(self.gross_rated_sensible_heat_ratio))
        out.append(self._to_str(self.gross_rated_cooling_cop))
        out.append(self._to_str(self.rated_air_flow_rate))
        out.append(self._to_str(self.fraction_of_air_flow_bypassed_around_coil))
        out.append(self._to_str(self.total_cooling_capacity_function_of_temperature_curve_name))
        out.append(self._to_str(self.total_cooling_capacity_function_of_flow_fraction_curve_name))
        out.append(self._to_str(self.energy_input_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.energy_input_ratio_function_of_flow_fraction_curve_name))
        out.append(self._to_str(self.part_load_fraction_correlation_curve_name))
        out.append(self._to_str(self.nominal_time_for_condensate_removal_to_begin))
        out.append(self._to_str(self.ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity))
        out.append(self._to_str(self.maximum_cycling_rate))
        out.append(self._to_str(self.latent_capacity_time_constant))
        out.append(self._to_str(self.condenser_air_inlet_node_name))
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.evaporative_condenser_effectiveness))
        out.append(self._to_str(self.evaporative_condenser_air_flow_rate))
        out.append(self._to_str(self.evaporative_condenser_pump_rated_power_consumption))
        out.append(self._to_str(self.sensible_heat_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.sensible_heat_ratio_function_of_flow_fraction_curve_name))
        return ",".join(out)