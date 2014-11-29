from collections import OrderedDict

class CoolingTowerSingleSpeed(object):
    """ Corresponds to IDD object `CoolingTower:SingleSpeed`
        This tower model is based on Merkel's theory, which is also the basis
        for the tower model in ASHRAE's HVAC1 Toolkit. The closed-circuit cooling tower
        is modeled as a counter flow heat exchanger with a single-speed fan drawing air
        through the tower (induced-draft configuration).
        Added fluid bypass as an additional capacity control. 8/2008.
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    """
    internal_name = "CoolingTower:SingleSpeed"
    field_count = 33

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoolingTower:SingleSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Fan Power"] = None
        self._data["Design U-Factor Times Area Value"] = None
        self._data["Free Convection Air Flow Rate"] = None
        self._data["Free Convection Air Flow Rate Sizing Factor"] = None
        self._data["Free Convection U-Factor Times Area Value"] = None
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = None
        self._data["Performance Input Method"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["Nominal Capacity"] = None
        self._data["Free Convection Capacity"] = None
        self._data["Free Convection Nominal Capacity Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Capacity Control"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
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
            self.design_fan_power = None
        else:
            self.design_fan_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_ufactor_times_area_value = None
        else:
            self.design_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_air_flow_rate = None
        else:
            self.free_convection_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_air_flow_rate_sizing_factor = None
        else:
            self.free_convection_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value = None
        else:
            self.free_convection_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value_sizing_factor = None
        else:
            self.free_convection_ufactor_times_area_value_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_capacity = None
        else:
            self.free_convection_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity_sizing_factor = None
        else:
            self.free_convection_nominal_capacity_sizing_factor = vals[i]
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
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_control = None
        else:
            self.capacity_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
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
        Tower Name

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
        Name of tower water inlet node

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
        Name of tower water outlet node

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
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_water_flow_rate`
        Leave field blank if tower performance input method is NominalCapacity

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
    def design_fan_power(self):
        """Get design_fan_power

        Returns:
            float: the value of `design_fan_power` or None if not set
        """
        return self._data["Design Fan Power"]

    @design_fan_power.setter
    def design_fan_power(self, value=None):
        """  Corresponds to IDD Field `design_fan_power`
        This is the fan motor electric input power

        Args:
            value (float): value for IDD Field `design_fan_power`
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
                                 'for field `design_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_fan_power`')

        self._data["Design Fan Power"] = value

    @property
    def design_ufactor_times_area_value(self):
        """Get design_ufactor_times_area_value

        Returns:
            float: the value of `design_ufactor_times_area_value` or None if not set
        """
        return self._data["Design U-Factor Times Area Value"]

    @design_ufactor_times_area_value.setter
    def design_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `design_ufactor_times_area_value`
        Leave field blank if tower performance input method is NominalCapacity

        Args:
            value (float): value for IDD Field `design_ufactor_times_area_value`
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
                                 'for field `design_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `design_ufactor_times_area_value`')

        self._data["Design U-Factor Times Area Value"] = value

    @property
    def free_convection_air_flow_rate(self):
        """Get free_convection_air_flow_rate

        Returns:
            float: the value of `free_convection_air_flow_rate` or None if not set
        """
        return self._data["Free Convection Air Flow Rate"]

    @free_convection_air_flow_rate.setter
    def free_convection_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `free_convection_air_flow_rate`

        Args:
            value (float): value for IDD Field `free_convection_air_flow_rate`
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
                                 'for field `free_convection_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_air_flow_rate`')

        self._data["Free Convection Air Flow Rate"] = value

    @property
    def free_convection_air_flow_rate_sizing_factor(self):
        """Get free_convection_air_flow_rate_sizing_factor

        Returns:
            float: the value of `free_convection_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Free Convection Air Flow Rate Sizing Factor"]

    @free_convection_air_flow_rate_sizing_factor.setter
    def free_convection_air_flow_rate_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_air_flow_rate_sizing_factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `free_convection_air_flow_rate_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_air_flow_rate_sizing_factor`')

        self._data["Free Convection Air Flow Rate Sizing Factor"] = value

    @property
    def free_convection_ufactor_times_area_value(self):
        """Get free_convection_ufactor_times_area_value

        Returns:
            float: the value of `free_convection_ufactor_times_area_value` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value"]

    @free_convection_ufactor_times_area_value.setter
    def free_convection_ufactor_times_area_value(self, value=0.0 ):
        """  Corresponds to IDD Field `free_convection_ufactor_times_area_value`

        Args:
            value (float): value for IDD Field `free_convection_ufactor_times_area_value`
                Unit: W/K
                Default value: 0.0
                value >= 0.0
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
                                 'for field `free_convection_ufactor_times_area_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `free_convection_ufactor_times_area_value`')

        self._data["Free Convection U-Factor Times Area Value"] = value

    @property
    def free_convection_ufactor_times_area_value_sizing_factor(self):
        """Get free_convection_ufactor_times_area_value_sizing_factor

        Returns:
            float: the value of `free_convection_ufactor_times_area_value_sizing_factor` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value Sizing Factor"]

    @free_convection_ufactor_times_area_value_sizing_factor.setter
    def free_convection_ufactor_times_area_value_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_ufactor_times_area_value_sizing_factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `free_convection_ufactor_times_area_value_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')

        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=UFactorTimesAreaAndDesignWaterFlowRate ):
        """  Corresponds to IDD Field `performance_input_method`
        User can define tower thermal performance by specifying the tower UA,
        the Design Air Flow Rate and the Design Water Flow Rate,
        or by specifying the tower nominal capacity

        Args:
            value (str): value for IDD Field `performance_input_method`
                Default value: UFactorTimesAreaAndDesignWaterFlowRate
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
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Nominal tower capacity times (1.25) gives the actual tower
        heat rejection at these operating conditions.

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
    def free_convection_capacity(self):
        """Get free_convection_capacity

        Returns:
            float: the value of `free_convection_capacity` or None if not set
        """
        return self._data["Free Convection Capacity"]

    @free_convection_capacity.setter
    def free_convection_capacity(self, value=None):
        """  Corresponds to IDD Field `free_convection_capacity`
        Tower capacity in free convection regime with entering water at 35C (95F),
        leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature
        and 35C (95F) dry-bulb temperature. Design water flow rate assumed to be
        5.382E-8 m3/s per watt of nominal tower capacity (3 gpm/ton). Tower free
        convection capacity times (1.25) gives the actual tower heat rejection at these
        operating conditions.

        Args:
            value (float): value for IDD Field `free_convection_capacity`
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
                                 'for field `free_convection_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_capacity`')

        self._data["Free Convection Capacity"] = value

    @property
    def free_convection_nominal_capacity_sizing_factor(self):
        """Get free_convection_nominal_capacity_sizing_factor

        Returns:
            float: the value of `free_convection_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Free Convection Nominal Capacity Sizing Factor"]

    @free_convection_nominal_capacity_sizing_factor.setter
    def free_convection_nominal_capacity_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_nominal_capacity_sizing_factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `free_convection_nominal_capacity_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')

        self._data["Free Convection Nominal Capacity Sizing Factor"] = value

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
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

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
        Enter the outdoor dry-bulb temperature when the basin heater turns on

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
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `evaporation_loss_mode`

        Args:
            value (str): value for IDD Field `evaporation_loss_mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
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
    def evaporation_loss_factor(self, value=0.2 ):
        """  Corresponds to IDD Field `evaporation_loss_factor`
        Rate of water evaporation from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [%/K].

        Args:
            value (float): value for IDD Field `evaporation_loss_factor`
                Unit: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
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
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

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
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `blowdown_calculation_mode`

        Args:
            value (str): value for IDD Field `blowdown_calculation_mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
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
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

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
        Makeup water usage due to blowdown results from occasionally draining a small amount
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
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
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1 ):
        """  Corresponds to IDD Field `number_of_cells`

        Args:
            value (int): value for IDD Field `number_of_cells`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')

        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value=MinimalCell ):
        """  Corresponds to IDD Field `cell_control`

        Args:
            value (str): value for IDD Field `cell_control`
                Default value: MinimalCell
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
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')

        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33 ):
        """  Corresponds to IDD Field `cell_minimum_water_flow_rate_fraction`
        The allowable minimal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_minimum_water_flow_rate_fraction`
                Default value: 0.33
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
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')

        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5 ):
        """  Corresponds to IDD Field `cell_maximum_water_flow_rate_fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_maximum_water_flow_rate_fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')

        self._data["Cell Maximum Water Flow Rate Fraction"] = value

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
        out.append(self._to_str(self.water_inlet_node_name))
        out.append(self._to_str(self.water_outlet_node_name))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.design_air_flow_rate))
        out.append(self._to_str(self.design_fan_power))
        out.append(self._to_str(self.design_ufactor_times_area_value))
        out.append(self._to_str(self.free_convection_air_flow_rate))
        out.append(self._to_str(self.free_convection_air_flow_rate_sizing_factor))
        out.append(self._to_str(self.free_convection_ufactor_times_area_value))
        out.append(self._to_str(self.free_convection_ufactor_times_area_value_sizing_factor))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.free_convection_capacity))
        out.append(self._to_str(self.free_convection_nominal_capacity_sizing_factor))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        out.append(self._to_str(self.evaporation_loss_mode))
        out.append(self._to_str(self.evaporation_loss_factor))
        out.append(self._to_str(self.drift_loss_percent))
        out.append(self._to_str(self.blowdown_calculation_mode))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        out.append(self._to_str(self.blowdown_makeup_water_usage_schedule_name))
        out.append(self._to_str(self.supply_water_storage_tank_name))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.capacity_control))
        out.append(self._to_str(self.number_of_cells))
        out.append(self._to_str(self.cell_control))
        out.append(self._to_str(self.cell_minimum_water_flow_rate_fraction))
        out.append(self._to_str(self.cell_maximum_water_flow_rate_fraction))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)

class CoolingTowerTwoSpeed(object):
    """ Corresponds to IDD object `CoolingTower:TwoSpeed`
        This tower model is based on Merkel's theory, which is also the basis
        for the tower model in ASHRAE's HVAC1 Toolkit. The closed-circuit cooling tower
        is modeled as a counter flow heat exchanger with a two-speed fan drawing air
        through the tower (induced-draft configuration).
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    """
    internal_name = "CoolingTower:TwoSpeed"
    field_count = 40

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoolingTower:TwoSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["High Fan Speed Air Flow Rate"] = None
        self._data["High Fan Speed Fan Power"] = None
        self._data["High Fan Speed U-Factor Times Area Value"] = None
        self._data["Low Fan Speed Air Flow Rate"] = None
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = None
        self._data["Low Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Fan Power Sizing Factor"] = None
        self._data["Low Fan Speed U-Factor Times Area Value"] = None
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = None
        self._data["Free Convection Regime Air Flow Rate"] = None
        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = None
        self._data["Free Convection Regime U-Factor Times Area Value"] = None
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = None
        self._data["Performance Input Method"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["High Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity Sizing Factor"] = None
        self._data["Free Convection Nominal Capacity"] = None
        self._data["Free Convection Nominal Capacity Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
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
            self.high_fan_speed_ufactor_times_area_value = None
        else:
            self.high_fan_speed_ufactor_times_area_value = vals[i]
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
            self.free_convection_regime_air_flow_rate = None
        else:
            self.free_convection_regime_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_regime_air_flow_rate_sizing_factor = None
        else:
            self.free_convection_regime_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_regime_ufactor_times_area_value = None
        else:
            self.free_convection_regime_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value_sizing_factor = None
        else:
            self.free_convection_ufactor_times_area_value_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
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
            self.free_convection_nominal_capacity = None
        else:
            self.free_convection_nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity_sizing_factor = None
        else:
            self.free_convection_nominal_capacity_sizing_factor = vals[i]
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
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
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
        Tower Name

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
        Name of tower Water Inlet Node

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
        Name of tower Water Outlet Node

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
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_water_flow_rate`
        Leave field blank if Tower Performance Input Method is NominalCapacity

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
    def high_fan_speed_ufactor_times_area_value(self):
        """Get high_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `high_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["High Fan Speed U-Factor Times Area Value"]

    @high_fan_speed_ufactor_times_area_value.setter
    def high_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `high_fan_speed_ufactor_times_area_value`
        Leave field blank if Tower Performance Input Method is NominalCapacity

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

        self._data["High Fan Speed U-Factor Times Area Value"] = value

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
        Low speed air flow rate must be greater than free convection air flow rate

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
                value > 0.0
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
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`')

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
                value > 0.0
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
                                 'for field `low_fan_speed_fan_power_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_fan_power_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_fan_speed_fan_power_sizing_factor`')

        self._data["Low Fan Speed Fan Power Sizing Factor"] = value

    @property
    def low_fan_speed_ufactor_times_area_value(self):
        """Get low_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["Low Fan Speed U-Factor Times Area Value"]

    @low_fan_speed_ufactor_times_area_value.setter
    def low_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `low_fan_speed_ufactor_times_area_value`
        Leave field blank if tower Performance Input Method is NominalCapacity
        Low speed tower UA must be less than high speed tower UA
        Low speed tower UA must be greater than free convection tower UA

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

        self._data["Low Fan Speed U-Factor Times Area Value"] = value

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
                value > 0.0
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
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`')

        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = value

    @property
    def free_convection_regime_air_flow_rate(self):
        """Get free_convection_regime_air_flow_rate

        Returns:
            float: the value of `free_convection_regime_air_flow_rate` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate"]

    @free_convection_regime_air_flow_rate.setter
    def free_convection_regime_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `free_convection_regime_air_flow_rate`

        Args:
            value (float): value for IDD Field `free_convection_regime_air_flow_rate`
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
                                 'for field `free_convection_regime_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_air_flow_rate`')

        self._data["Free Convection Regime Air Flow Rate"] = value

    @property
    def free_convection_regime_air_flow_rate_sizing_factor(self):
        """Get free_convection_regime_air_flow_rate_sizing_factor

        Returns:
            float: the value of `free_convection_regime_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate Sizing Factor"]

    @free_convection_regime_air_flow_rate_sizing_factor.setter
    def free_convection_regime_air_flow_rate_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_regime_air_flow_rate_sizing_factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `free_convection_regime_air_flow_rate_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')

        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = value

    @property
    def free_convection_regime_ufactor_times_area_value(self):
        """Get free_convection_regime_ufactor_times_area_value

        Returns:
            float: the value of `free_convection_regime_ufactor_times_area_value` or None if not set
        """
        return self._data["Free Convection Regime U-Factor Times Area Value"]

    @free_convection_regime_ufactor_times_area_value.setter
    def free_convection_regime_ufactor_times_area_value(self, value=0.0 ):
        """  Corresponds to IDD Field `free_convection_regime_ufactor_times_area_value`
        Leave field blank if Tower Performance Input Method is NominalCapacity

        Args:
            value (float): value for IDD Field `free_convection_regime_ufactor_times_area_value`
                Unit: W/K
                Default value: 0.0
                value >= 0.0
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
                                 'for field `free_convection_regime_ufactor_times_area_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')

        self._data["Free Convection Regime U-Factor Times Area Value"] = value

    @property
    def free_convection_ufactor_times_area_value_sizing_factor(self):
        """Get free_convection_ufactor_times_area_value_sizing_factor

        Returns:
            float: the value of `free_convection_ufactor_times_area_value_sizing_factor` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value Sizing Factor"]

    @free_convection_ufactor_times_area_value_sizing_factor.setter
    def free_convection_ufactor_times_area_value_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_ufactor_times_area_value_sizing_factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `free_convection_ufactor_times_area_value_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')

        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=UFactorTimesAreaAndDesignWaterFlowRate ):
        """  Corresponds to IDD Field `performance_input_method`
        User can define tower thermal performance by specifying the tower UA,
        the Design Air Flow Rate and the Design Water Flow Rate,
        or by specifying the tower nominal capacity

        Args:
            value (str): value for IDD Field `performance_input_method`
                Default value: UFactorTimesAreaAndDesignWaterFlowRate
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
    def high_speed_nominal_capacity(self):
        """Get high_speed_nominal_capacity

        Returns:
            float: the value of `high_speed_nominal_capacity` or None if not set
        """
        return self._data["High Speed Nominal Capacity"]

    @high_speed_nominal_capacity.setter
    def high_speed_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `high_speed_nominal_capacity`
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature, with the tower fan operating at high speed. Design water
        flow rate assumed to be 5.382E-8 m3/s per watt(3 gpm/ton). Nominal tower capacity
        times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio (e.g. 1.25)
        gives the actual tower heat rejection at these operating conditions.

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
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature, with the tower fan operating at low speed. Design water flow
        rate assumed to be 5.382E-8 m3/s per watt of tower high-speed nominal capacity
        (3 gpm/ton). Nominal tower capacity times the Heat Rejection Capacity and Nominal
        Capacity Sizing Ratio (e.g. 1.25) gives the actual tower heat
        rejection at these operating conditions.

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
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `low_speed_nominal_capacity_sizing_factor`
                Default value: 0.5
                value > 0.0
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
                                 'for field `low_speed_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_speed_nominal_capacity_sizing_factor`')

        self._data["Low Speed Nominal Capacity Sizing Factor"] = value

    @property
    def free_convection_nominal_capacity(self):
        """Get free_convection_nominal_capacity

        Returns:
            float: the value of `free_convection_nominal_capacity` or None if not set
        """
        return self._data["Free Convection Nominal Capacity"]

    @free_convection_nominal_capacity.setter
    def free_convection_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `free_convection_nominal_capacity`
        Tower capacity in free convection regime with entering water at 35C (95F),
        leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature
        and 35C (95F) dry-bulb temperature. Design water flow rate assumed to be
        5.382E-8 m3/s per watt of tower high-speed nominal capacity (3 gpm/ton). Tower
        free convection capacity times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio
        (e.g. 1.25)  gives the actual tower heat rejection at these operating conditions

        Args:
            value (float): value for IDD Field `free_convection_nominal_capacity`
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
                                 'for field `free_convection_nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_nominal_capacity`')

        self._data["Free Convection Nominal Capacity"] = value

    @property
    def free_convection_nominal_capacity_sizing_factor(self):
        """Get free_convection_nominal_capacity_sizing_factor

        Returns:
            float: the value of `free_convection_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Free Convection Nominal Capacity Sizing Factor"]

    @free_convection_nominal_capacity_sizing_factor.setter
    def free_convection_nominal_capacity_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_nominal_capacity_sizing_factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `free_convection_nominal_capacity_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')

        self._data["Free Convection Nominal Capacity Sizing Factor"] = value

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
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

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
        Enter the outdoor dry-bulb temperature when the basin heater turns on

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
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `evaporation_loss_mode`

        Args:
            value (str): value for IDD Field `evaporation_loss_mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
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
    def evaporation_loss_factor(self, value=0.2 ):
        """  Corresponds to IDD Field `evaporation_loss_factor`
        Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [%/K].

        Args:
            value (float): value for IDD Field `evaporation_loss_factor`
                Unit: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
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
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

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
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `blowdown_calculation_mode`

        Args:
            value (str): value for IDD Field `blowdown_calculation_mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
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
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

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
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
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
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1 ):
        """  Corresponds to IDD Field `number_of_cells`

        Args:
            value (int): value for IDD Field `number_of_cells`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')

        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value=MinimalCell ):
        """  Corresponds to IDD Field `cell_control`

        Args:
            value (str): value for IDD Field `cell_control`
                Default value: MinimalCell
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
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')

        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33 ):
        """  Corresponds to IDD Field `cell_minimum_water_flow_rate_fraction`
        The allowable mininal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_minimum_water_flow_rate_fraction`
                Default value: 0.33
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
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')

        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5 ):
        """  Corresponds to IDD Field `cell_maximum_water_flow_rate_fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_maximum_water_flow_rate_fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')

        self._data["Cell Maximum Water Flow Rate Fraction"] = value

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
        out.append(self._to_str(self.water_inlet_node_name))
        out.append(self._to_str(self.water_outlet_node_name))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.high_fan_speed_air_flow_rate))
        out.append(self._to_str(self.high_fan_speed_fan_power))
        out.append(self._to_str(self.high_fan_speed_ufactor_times_area_value))
        out.append(self._to_str(self.low_fan_speed_air_flow_rate))
        out.append(self._to_str(self.low_fan_speed_air_flow_rate_sizing_factor))
        out.append(self._to_str(self.low_fan_speed_fan_power))
        out.append(self._to_str(self.low_fan_speed_fan_power_sizing_factor))
        out.append(self._to_str(self.low_fan_speed_ufactor_times_area_value))
        out.append(self._to_str(self.low_fan_speed_ufactor_times_area_sizing_factor))
        out.append(self._to_str(self.free_convection_regime_air_flow_rate))
        out.append(self._to_str(self.free_convection_regime_air_flow_rate_sizing_factor))
        out.append(self._to_str(self.free_convection_regime_ufactor_times_area_value))
        out.append(self._to_str(self.free_convection_ufactor_times_area_value_sizing_factor))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio))
        out.append(self._to_str(self.high_speed_nominal_capacity))
        out.append(self._to_str(self.low_speed_nominal_capacity))
        out.append(self._to_str(self.low_speed_nominal_capacity_sizing_factor))
        out.append(self._to_str(self.free_convection_nominal_capacity))
        out.append(self._to_str(self.free_convection_nominal_capacity_sizing_factor))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        out.append(self._to_str(self.evaporation_loss_mode))
        out.append(self._to_str(self.evaporation_loss_factor))
        out.append(self._to_str(self.drift_loss_percent))
        out.append(self._to_str(self.blowdown_calculation_mode))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        out.append(self._to_str(self.blowdown_makeup_water_usage_schedule_name))
        out.append(self._to_str(self.supply_water_storage_tank_name))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.number_of_cells))
        out.append(self._to_str(self.cell_control))
        out.append(self._to_str(self.cell_minimum_water_flow_rate_fraction))
        out.append(self._to_str(self.cell_maximum_water_flow_rate_fraction))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)

class CoolingTowerVariableSpeedMerkel(object):
    """ Corresponds to IDD object `CoolingTower:VariableSpeed:Merkel`
        This tower model is based on Merkel's theory, which is also the basis
        for the tower model in ASHRAE's HVAC1 Toolkit. The closed-circuit cooling tower
        is modeled as a counter flow heat exchanger with a variable-speed fan drawing air
        through the tower (induced-draft configuration).
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    """
    internal_name = "CoolingTower:VariableSpeed:Merkel"
    field_count = 40

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoolingTower:VariableSpeed:Merkel`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Performance Input Method"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["Nominal Capacity"] = None
        self._data["Free Convection Nominal Capacity"] = None
        self._data["Free Convection Nominal Capacity Sizing Factor"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Water Flow Rate per Unit of Nominal Capacity"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Air Flow Rate Per Unit of Nominal Capacity"] = None
        self._data["Minimum Air Flow Rate Ratio"] = None
        self._data["Design Fan Power"] = None
        self._data["Design Fan Power Per Unit of Nominal Capacity"] = None
        self._data["Fan Power Modifier Function of Air Flow Rate Ratio Curve Name"] = None
        self._data["Free Convection Regime Air Flow Rate"] = None
        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = None
        self._data["Design Air Flow Rate U-Factor Times Area Value"] = None
        self._data["Free Convection Regime U-Factor Times Area Value"] = None
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = None
        self._data["U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name"] = None
        self._data["U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name"] = None
        self._data["U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
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
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity = None
        else:
            self.free_convection_nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity_sizing_factor = None
        else:
            self.free_convection_nominal_capacity_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_water_flow_rate_per_unit_of_nominal_capacity = None
        else:
            self.design_water_flow_rate_per_unit_of_nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_air_flow_rate = None
        else:
            self.design_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_air_flow_rate_per_unit_of_nominal_capacity = None
        else:
            self.design_air_flow_rate_per_unit_of_nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_air_flow_rate_ratio = None
        else:
            self.minimum_air_flow_rate_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_fan_power = None
        else:
            self.design_fan_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_fan_power_per_unit_of_nominal_capacity = None
        else:
            self.design_fan_power_per_unit_of_nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_power_modifier_function_of_air_flow_rate_ratio_curve_name = None
        else:
            self.fan_power_modifier_function_of_air_flow_rate_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_regime_air_flow_rate = None
        else:
            self.free_convection_regime_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_regime_air_flow_rate_sizing_factor = None
        else:
            self.free_convection_regime_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_air_flow_rate_ufactor_times_area_value = None
        else:
            self.design_air_flow_rate_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_regime_ufactor_times_area_value = None
        else:
            self.free_convection_regime_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value_sizing_factor = None
        else:
            self.free_convection_ufactor_times_area_value_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name = None
        else:
            self.ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name = None
        else:
            self.ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name = None
        else:
            self.ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name = vals[i]
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
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
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
        Tower Name

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
        Name of tower water inlet node

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
        Name of tower water outlet node

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
        User can define tower thermal performance by specifying the tower UA,
        the Design Air Flow Rate and the Design Water Flow Rate,
        or by specifying the tower nominal capacity

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
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature, with the tower fan operating at Design Air Flow Rate (full speed). Design water
        flow rate is as set in Design Water Flow Rate per Unit of Nominal Capacity. Nominal tower capacity
        times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio (e.g. 1.25)
        gives the actual tower heat rejection at these operating conditions.

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
    def free_convection_nominal_capacity(self):
        """Get free_convection_nominal_capacity

        Returns:
            float: the value of `free_convection_nominal_capacity` or None if not set
        """
        return self._data["Free Convection Nominal Capacity"]

    @free_convection_nominal_capacity.setter
    def free_convection_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `free_convection_nominal_capacity`
        required field when performance method is NominalCapacity
        Tower capacity in free convection regime with entering water at 35C (95F),
        leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature
        and 35C (95F) dry-bulb temperature. Design water flow rate is as set
        in Design Water Flow Rate per Unit of Nominal Capacity. Tower
        free convection capacity times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio
        (e.g. 1.25)  gives the actual tower heat rejection at these operating conditions

        Args:
            value (float): value for IDD Field `free_convection_nominal_capacity`
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
                                 'for field `free_convection_nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_nominal_capacity`')

        self._data["Free Convection Nominal Capacity"] = value

    @property
    def free_convection_nominal_capacity_sizing_factor(self):
        """Get free_convection_nominal_capacity_sizing_factor

        Returns:
            float: the value of `free_convection_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Free Convection Nominal Capacity Sizing Factor"]

    @free_convection_nominal_capacity_sizing_factor.setter
    def free_convection_nominal_capacity_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_nominal_capacity_sizing_factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `free_convection_nominal_capacity_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')

        self._data["Free Convection Nominal Capacity Sizing Factor"] = value

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
    def design_water_flow_rate_per_unit_of_nominal_capacity(self):
        """Get design_water_flow_rate_per_unit_of_nominal_capacity

        Returns:
            float: the value of `design_water_flow_rate_per_unit_of_nominal_capacity` or None if not set
        """
        return self._data["Design Water Flow Rate per Unit of Nominal Capacity"]

    @design_water_flow_rate_per_unit_of_nominal_capacity.setter
    def design_water_flow_rate_per_unit_of_nominal_capacity(self, value=5.382e-08 ):
        """  Corresponds to IDD Field `design_water_flow_rate_per_unit_of_nominal_capacity`
        This field is only used if the previous is set to autocalculate and performance input method is NominalCapacity

        Args:
            value (float): value for IDD Field `design_water_flow_rate_per_unit_of_nominal_capacity`
                Unit: m3/s-W
                Default value: 5.382e-08
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate_per_unit_of_nominal_capacity`'.format(value))

        self._data["Design Water Flow Rate per Unit of Nominal Capacity"] = value

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
        This is the air flow rate at full fan speed

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
    def design_air_flow_rate_per_unit_of_nominal_capacity(self):
        """Get design_air_flow_rate_per_unit_of_nominal_capacity

        Returns:
            float: the value of `design_air_flow_rate_per_unit_of_nominal_capacity` or None if not set
        """
        return self._data["Design Air Flow Rate Per Unit of Nominal Capacity"]

    @design_air_flow_rate_per_unit_of_nominal_capacity.setter
    def design_air_flow_rate_per_unit_of_nominal_capacity(self, value=2.76316e-05 ):
        """  Corresponds to IDD Field `design_air_flow_rate_per_unit_of_nominal_capacity`
        This field is only used if the previous is set to autocalculate
        When field is left blank the default scaling factor is adjusted for elevation to increase volume flow at altitude
        When field has a value the scaling factor is used without adjusting for elevation

        Args:
            value (float): value for IDD Field `design_air_flow_rate_per_unit_of_nominal_capacity`
                Unit: m3/s-W
                Default value: 2.76316e-05
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate_per_unit_of_nominal_capacity`'.format(value))

        self._data["Design Air Flow Rate Per Unit of Nominal Capacity"] = value

    @property
    def minimum_air_flow_rate_ratio(self):
        """Get minimum_air_flow_rate_ratio

        Returns:
            float: the value of `minimum_air_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Air Flow Rate Ratio"]

    @minimum_air_flow_rate_ratio.setter
    def minimum_air_flow_rate_ratio(self, value=0.2 ):
        """  Corresponds to IDD Field `minimum_air_flow_rate_ratio`
        Enter the minimum air flow rate ratio. This is typically determined by the variable
        speed drive that controls the fan motor speed. Valid entries are from 0.1 to 0.5.

        Args:
            value (float): value for IDD Field `minimum_air_flow_rate_ratio`
                Default value: 0.2
                value >= 0.1
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_air_flow_rate_ratio`'.format(value))
            if value < 0.1:
                raise ValueError('value need to be greater or equal 0.1 '
                                 'for field `minimum_air_flow_rate_ratio`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `minimum_air_flow_rate_ratio`')

        self._data["Minimum Air Flow Rate Ratio"] = value

    @property
    def design_fan_power(self):
        """Get design_fan_power

        Returns:
            float: the value of `design_fan_power` or None if not set
        """
        return self._data["Design Fan Power"]

    @design_fan_power.setter
    def design_fan_power(self, value=None):
        """  Corresponds to IDD Field `design_fan_power`
        This is the fan motor electric input power at high speed

        Args:
            value (float): value for IDD Field `design_fan_power`
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
                                 'for field `design_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_fan_power`')

        self._data["Design Fan Power"] = value

    @property
    def design_fan_power_per_unit_of_nominal_capacity(self):
        """Get design_fan_power_per_unit_of_nominal_capacity

        Returns:
            float: the value of `design_fan_power_per_unit_of_nominal_capacity` or None if not set
        """
        return self._data["Design Fan Power Per Unit of Nominal Capacity"]

    @design_fan_power_per_unit_of_nominal_capacity.setter
    def design_fan_power_per_unit_of_nominal_capacity(self, value=0.0105 ):
        """  Corresponds to IDD Field `design_fan_power_per_unit_of_nominal_capacity`
        This field is only used if the previous is set to autocalculate
        [W/W] Watts of fan power per Watt of tower nominal capacity

        Args:
            value (float): value for IDD Field `design_fan_power_per_unit_of_nominal_capacity`
                Unit: dimensionless
                Default value: 0.0105
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_fan_power_per_unit_of_nominal_capacity`'.format(value))

        self._data["Design Fan Power Per Unit of Nominal Capacity"] = value

    @property
    def fan_power_modifier_function_of_air_flow_rate_ratio_curve_name(self):
        """Get fan_power_modifier_function_of_air_flow_rate_ratio_curve_name

        Returns:
            str: the value of `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name` or None if not set
        """
        return self._data["Fan Power Modifier Function of Air Flow Rate Ratio Curve Name"]

    @fan_power_modifier_function_of_air_flow_rate_ratio_curve_name.setter
    def fan_power_modifier_function_of_air_flow_rate_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name`
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*AFR + c*AFR**2 + d*AFR**3
        quartic curve = a + b*AFR + c*AFR**2 + d*AFR**3 + e*AFR**4
        x = AFR = Ratio of current operating air flow rate to Design Air Flow Rate

        Args:
            value (str): value for IDD Field `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name`
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
                                 'for field `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name`')

        self._data["Fan Power Modifier Function of Air Flow Rate Ratio Curve Name"] = value

    @property
    def free_convection_regime_air_flow_rate(self):
        """Get free_convection_regime_air_flow_rate

        Returns:
            float: the value of `free_convection_regime_air_flow_rate` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate"]

    @free_convection_regime_air_flow_rate.setter
    def free_convection_regime_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `free_convection_regime_air_flow_rate`

        Args:
            value (float): value for IDD Field `free_convection_regime_air_flow_rate`
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
                                 'for field `free_convection_regime_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_air_flow_rate`')

        self._data["Free Convection Regime Air Flow Rate"] = value

    @property
    def free_convection_regime_air_flow_rate_sizing_factor(self):
        """Get free_convection_regime_air_flow_rate_sizing_factor

        Returns:
            float: the value of `free_convection_regime_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate Sizing Factor"]

    @free_convection_regime_air_flow_rate_sizing_factor.setter
    def free_convection_regime_air_flow_rate_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_regime_air_flow_rate_sizing_factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `free_convection_regime_air_flow_rate_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')

        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = value

    @property
    def design_air_flow_rate_ufactor_times_area_value(self):
        """Get design_air_flow_rate_ufactor_times_area_value

        Returns:
            float: the value of `design_air_flow_rate_ufactor_times_area_value` or None if not set
        """
        return self._data["Design Air Flow Rate U-Factor Times Area Value"]

    @design_air_flow_rate_ufactor_times_area_value.setter
    def design_air_flow_rate_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `design_air_flow_rate_ufactor_times_area_value`
        required field when performance method is UFactorTimesAreaAndDesignWaterFlowRate
        when performance method is NominalCapacity the program will solve for this UA

        Args:
            value (float): value for IDD Field `design_air_flow_rate_ufactor_times_area_value`
                Unit: W/K
                if `value` is None it will not be checked against the
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

        self._data["Design Air Flow Rate U-Factor Times Area Value"] = value

    @property
    def free_convection_regime_ufactor_times_area_value(self):
        """Get free_convection_regime_ufactor_times_area_value

        Returns:
            float: the value of `free_convection_regime_ufactor_times_area_value` or None if not set
        """
        return self._data["Free Convection Regime U-Factor Times Area Value"]

    @free_convection_regime_ufactor_times_area_value.setter
    def free_convection_regime_ufactor_times_area_value(self, value=0.0 ):
        """  Corresponds to IDD Field `free_convection_regime_ufactor_times_area_value`
        required field when performance input method is UFactorTimesAreaAndDesignWaterFlowRate
        Leave field blank if performance input method is NominalCapacity

        Args:
            value (float): value for IDD Field `free_convection_regime_ufactor_times_area_value`
                Unit: W/K
                Default value: 0.0
                value >= 0.0
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
                                 'for field `free_convection_regime_ufactor_times_area_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')

        self._data["Free Convection Regime U-Factor Times Area Value"] = value

    @property
    def free_convection_ufactor_times_area_value_sizing_factor(self):
        """Get free_convection_ufactor_times_area_value_sizing_factor

        Returns:
            float: the value of `free_convection_ufactor_times_area_value_sizing_factor` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value Sizing Factor"]

    @free_convection_ufactor_times_area_value_sizing_factor.setter
    def free_convection_ufactor_times_area_value_sizing_factor(self, value=0.1 ):
        """  Corresponds to IDD Field `free_convection_ufactor_times_area_value_sizing_factor`
        required field when performance input method is UFactorTimesAreaAndDesignWaterFlowRate
        This field is only used if the previous field is set to autocalculate and
        the performance input method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `free_convection_ufactor_times_area_value_sizing_factor`
                Default value: 0.1
                value > 0.0
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
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')

        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = value

    @property
    def ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name(self):
        """Get ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name

        Returns:
            str: the value of `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name` or None if not set
        """
        return self._data["U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name"]

    @ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name.setter
    def ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name`
        This curve describes how tower's design UA changes with variable air flow rate
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*AFR + c*AFR**2 + d*AFR**3
        quartic curve = a + b*AFR + c*AFR**2 + d*AFR**3 + e*AFR**4
        x = AFR = Ratio of current operating air flow rate to Design Air Flow Rate

        Args:
            value (str): value for IDD Field `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name`
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
                                 'for field `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name`')

        self._data["U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name"] = value

    @property
    def ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name(self):
        """Get ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name

        Returns:
            str: the value of `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name` or None if not set
        """
        return self._data["U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name"]

    @ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name.setter
    def ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name(self, value=None):
        """  Corresponds to IDD Field `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name`
        curve describes how tower UA changes with outdoor air wetbulb temperature difference from design wetbulb
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*DeltaWB + c*DeltaWB**2 + d*DeltaWB**3
        quartic curve = a + b*DeltaWB + c*DeltaWB**2 + d*DeltaWB**3 + e*DeltaWB**4
        x = DeltaWB = (design wetbulb temperature in C - current wetbulb temperature in C)
        where design wetbulb temperature of entering air is 25.56C (78F)

        Args:
            value (str): value for IDD Field `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name`
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
                                 'for field `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name`')

        self._data["U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name"] = value

    @property
    def ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name(self):
        """Get ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name

        Returns:
            str: the value of `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name` or None if not set
        """
        return self._data["U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name"]

    @ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name.setter
    def ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name`
        curve describes how tower UA changes with the flow rate of condenser water through the tower
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*WFR + c*WFR**2 + d*WFR**3
        quartic curve = a + b*WFR + c*WFR**2 + d*WFR**3 + e*WFR**4
        x = WFR = Ratio of current operationg water flow rate to Design Water Flow Rate

        Args:
            value (str): value for IDD Field `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name`
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
                                 'for field `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name`')

        self._data["U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name"] = value

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
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

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
        Enter the outdoor dry-bulb temperature when the basin heater turns on

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
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `evaporation_loss_mode`

        Args:
            value (str): value for IDD Field `evaporation_loss_mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
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
    def evaporation_loss_factor(self, value=0.2 ):
        """  Corresponds to IDD Field `evaporation_loss_factor`
        Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [%/K].

        Args:
            value (float): value for IDD Field `evaporation_loss_factor`
                Unit: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
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
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

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
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `blowdown_calculation_mode`

        Args:
            value (str): value for IDD Field `blowdown_calculation_mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
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
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

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
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
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
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1 ):
        """  Corresponds to IDD Field `number_of_cells`

        Args:
            value (int): value for IDD Field `number_of_cells`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')

        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value=MinimalCell ):
        """  Corresponds to IDD Field `cell_control`

        Args:
            value (str): value for IDD Field `cell_control`
                Default value: MinimalCell
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
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')

        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33 ):
        """  Corresponds to IDD Field `cell_minimum_water_flow_rate_fraction`
        The allowable mininal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_minimum_water_flow_rate_fraction`
                Default value: 0.33
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
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')

        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5 ):
        """  Corresponds to IDD Field `cell_maximum_water_flow_rate_fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_maximum_water_flow_rate_fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')

        self._data["Cell Maximum Water Flow Rate Fraction"] = value

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
        out.append(self._to_str(self.water_inlet_node_name))
        out.append(self._to_str(self.water_outlet_node_name))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.free_convection_nominal_capacity))
        out.append(self._to_str(self.free_convection_nominal_capacity_sizing_factor))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.design_water_flow_rate_per_unit_of_nominal_capacity))
        out.append(self._to_str(self.design_air_flow_rate))
        out.append(self._to_str(self.design_air_flow_rate_per_unit_of_nominal_capacity))
        out.append(self._to_str(self.minimum_air_flow_rate_ratio))
        out.append(self._to_str(self.design_fan_power))
        out.append(self._to_str(self.design_fan_power_per_unit_of_nominal_capacity))
        out.append(self._to_str(self.fan_power_modifier_function_of_air_flow_rate_ratio_curve_name))
        out.append(self._to_str(self.free_convection_regime_air_flow_rate))
        out.append(self._to_str(self.free_convection_regime_air_flow_rate_sizing_factor))
        out.append(self._to_str(self.design_air_flow_rate_ufactor_times_area_value))
        out.append(self._to_str(self.free_convection_regime_ufactor_times_area_value))
        out.append(self._to_str(self.free_convection_ufactor_times_area_value_sizing_factor))
        out.append(self._to_str(self.ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name))
        out.append(self._to_str(self.ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name))
        out.append(self._to_str(self.ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        out.append(self._to_str(self.evaporation_loss_mode))
        out.append(self._to_str(self.evaporation_loss_factor))
        out.append(self._to_str(self.drift_loss_percent))
        out.append(self._to_str(self.blowdown_calculation_mode))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        out.append(self._to_str(self.blowdown_makeup_water_usage_schedule_name))
        out.append(self._to_str(self.supply_water_storage_tank_name))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.number_of_cells))
        out.append(self._to_str(self.cell_control))
        out.append(self._to_str(self.cell_minimum_water_flow_rate_fraction))
        out.append(self._to_str(self.cell_maximum_water_flow_rate_fraction))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)

class CoolingTowerVariableSpeed(object):
    """ Corresponds to IDD object `CoolingTower:VariableSpeed`
        This tower model is based on purely empirical algorithms derived from manufacturer's
        performance data or field measurements. The user can select from two existing
        algorithms (CoolTools or YorkCalc), or they can enter their own correlation for
        approach temperature by using a variable speed tower model coefficient object.
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    """
    internal_name = "CoolingTower:VariableSpeed"
    field_count = 30

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoolingTower:VariableSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Model Type"] = None
        self._data["Model Coefficient Name"] = None
        self._data["Design Inlet Air Wet-Bulb Temperature"] = None
        self._data["Design Approach Temperature"] = None
        self._data["Design Range Temperature"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Fan Power"] = None
        self._data["Fan Power Ratio Function of Air Flow Rate Ratio Curve Name"] = None
        self._data["Minimum Air Flow Rate Ratio"] = None
        self._data["Fraction of Tower Capacity in Free Convection Regime"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
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
            self.model_type = None
        else:
            self.model_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.model_coefficient_name = None
        else:
            self.model_coefficient_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_inlet_air_wetbulb_temperature = None
        else:
            self.design_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_approach_temperature = None
        else:
            self.design_approach_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_range_temperature = None
        else:
            self.design_range_temperature = vals[i]
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
            self.design_fan_power = None
        else:
            self.design_fan_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_power_ratio_function_of_air_flow_rate_ratio_curve_name = None
        else:
            self.fan_power_ratio_function_of_air_flow_rate_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_air_flow_rate_ratio = None
        else:
            self.minimum_air_flow_rate_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_tower_capacity_in_free_convection_regime = None
        else:
            self.fraction_of_tower_capacity_in_free_convection_regime = vals[i]
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
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
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
        Tower Name

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
        Name of tower water inlet node

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
        Name of tower water outlet node

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
    def model_type(self):
        """Get model_type

        Returns:
            str: the value of `model_type` or None if not set
        """
        return self._data["Model Type"]

    @model_type.setter
    def model_type(self, value="YorkCalc"):
        """  Corresponds to IDD Field `model_type`
        Determines the coefficients and form of the equation for calculating
        approach temperature

        Args:
            value (str): value for IDD Field `model_type`
                Accepted values are:
                      - CoolToolsCrossFlow
                      - CoolToolsUserDefined
                      - YorkCalc
                      - YorkCalcUserDefined
                Default value: YorkCalc
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
                                 'for field `model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `model_type`')
            vals = set()
            vals.add("CoolToolsCrossFlow")
            vals.add("CoolToolsUserDefined")
            vals.add("YorkCalc")
            vals.add("YorkCalcUserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `model_type`'.format(value))

        self._data["Model Type"] = value

    @property
    def model_coefficient_name(self):
        """Get model_coefficient_name

        Returns:
            str: the value of `model_coefficient_name` or None if not set
        """
        return self._data["Model Coefficient Name"]

    @model_coefficient_name.setter
    def model_coefficient_name(self, value=None):
        """  Corresponds to IDD Field `model_coefficient_name`
        Name of the tower model coefficient object.
        Used only when tower Model Type is either CoolToolsUserDefined or YorkCalcUserDefined.

        Args:
            value (str): value for IDD Field `model_coefficient_name`
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
                                 'for field `model_coefficient_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `model_coefficient_name`')

        self._data["Model Coefficient Name"] = value

    @property
    def design_inlet_air_wetbulb_temperature(self):
        """Get design_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `design_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Inlet Air Wet-Bulb Temperature"]

    @design_inlet_air_wetbulb_temperature.setter
    def design_inlet_air_wetbulb_temperature(self, value=25.6 ):
        """  Corresponds to IDD Field `design_inlet_air_wetbulb_temperature`
        Enter the tower's design inlet air wet-bulb temperature

        Args:
            value (float): value for IDD Field `design_inlet_air_wetbulb_temperature`
                Unit: C
                Default value: 25.6
                value >= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_inlet_air_wetbulb_temperature`'.format(value))
            if value < 20.0:
                raise ValueError('value need to be greater or equal 20.0 '
                                 'for field `design_inlet_air_wetbulb_temperature`')

        self._data["Design Inlet Air Wet-Bulb Temperature"] = value

    @property
    def design_approach_temperature(self):
        """Get design_approach_temperature

        Returns:
            float: the value of `design_approach_temperature` or None if not set
        """
        return self._data["Design Approach Temperature"]

    @design_approach_temperature.setter
    def design_approach_temperature(self, value=3.9 ):
        """  Corresponds to IDD Field `design_approach_temperature`
        Enter the approach temperature corresponding to the design inlet air
        wet-bulb temperature and design range temperature.
        Design approach temp = outlet water temperature minus inlet air wet-bulb temperature
        at design conditions.

        Args:
            value (float): value for IDD Field `design_approach_temperature`
                Unit: deltaC
                Default value: 3.9
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
                                 'for field `design_approach_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_approach_temperature`')

        self._data["Design Approach Temperature"] = value

    @property
    def design_range_temperature(self):
        """Get design_range_temperature

        Returns:
            float: the value of `design_range_temperature` or None if not set
        """
        return self._data["Design Range Temperature"]

    @design_range_temperature.setter
    def design_range_temperature(self, value=5.6 ):
        """  Corresponds to IDD Field `design_range_temperature`
        Enter the range temperature corresponding to the design inlet air
        wet-bulb temperature and design approach temperature.
        Design range = inlet water temperature minus outlet water temperature
        at design conditions.

        Args:
            value (float): value for IDD Field `design_range_temperature`
                Unit: deltaC
                Default value: 5.6
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
                                 'for field `design_range_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_range_temperature`')

        self._data["Design Range Temperature"] = value

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
        Water flow rate through the tower at design conditions

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
        Design (maximum) air flow rate through the tower

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
    def design_fan_power(self):
        """Get design_fan_power

        Returns:
            float: the value of `design_fan_power` or None if not set
        """
        return self._data["Design Fan Power"]

    @design_fan_power.setter
    def design_fan_power(self, value=None):
        """  Corresponds to IDD Field `design_fan_power`
        Enter the fan motor electric input power at design (max) air flow through the tower
        Standard conversion for horsepower is 1 HP = 745.7 W

        Args:
            value (float): value for IDD Field `design_fan_power`
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
                                 'for field `design_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_fan_power`')

        self._data["Design Fan Power"] = value

    @property
    def fan_power_ratio_function_of_air_flow_rate_ratio_curve_name(self):
        """Get fan_power_ratio_function_of_air_flow_rate_ratio_curve_name

        Returns:
            str: the value of `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name` or None if not set
        """
        return self._data["Fan Power Ratio Function of Air Flow Rate Ratio Curve Name"]

    @fan_power_ratio_function_of_air_flow_rate_ratio_curve_name.setter
    def fan_power_ratio_function_of_air_flow_rate_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name`
        Table:OneIndependentVariable object can also be used
        FPR = a + b*AFR + c*AFR**2 + d*AFR**3
        FPR = fraction of the design fan power
        AFR = fraction of the design air flow rate
        If left blank, then fan power is assumed to be proportional to
        (air flow rate ratio)^3

        Args:
            value (str): value for IDD Field `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name`
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
                                 'for field `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name`')

        self._data["Fan Power Ratio Function of Air Flow Rate Ratio Curve Name"] = value

    @property
    def minimum_air_flow_rate_ratio(self):
        """Get minimum_air_flow_rate_ratio

        Returns:
            float: the value of `minimum_air_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Air Flow Rate Ratio"]

    @minimum_air_flow_rate_ratio.setter
    def minimum_air_flow_rate_ratio(self, value=0.2 ):
        """  Corresponds to IDD Field `minimum_air_flow_rate_ratio`
        Enter the minimum air flow rate ratio. This is typically determined by the variable
        speed drive that controls the fan motor speed. Valid entries are from 0.2 to 0.5.

        Args:
            value (float): value for IDD Field `minimum_air_flow_rate_ratio`
                Default value: 0.2
                value >= 0.2
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_air_flow_rate_ratio`'.format(value))
            if value < 0.2:
                raise ValueError('value need to be greater or equal 0.2 '
                                 'for field `minimum_air_flow_rate_ratio`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `minimum_air_flow_rate_ratio`')

        self._data["Minimum Air Flow Rate Ratio"] = value

    @property
    def fraction_of_tower_capacity_in_free_convection_regime(self):
        """Get fraction_of_tower_capacity_in_free_convection_regime

        Returns:
            float: the value of `fraction_of_tower_capacity_in_free_convection_regime` or None if not set
        """
        return self._data["Fraction of Tower Capacity in Free Convection Regime"]

    @fraction_of_tower_capacity_in_free_convection_regime.setter
    def fraction_of_tower_capacity_in_free_convection_regime(self, value=0.125 ):
        """  Corresponds to IDD Field `fraction_of_tower_capacity_in_free_convection_regime`
        Enter the fraction of tower capacity in the free convection regime. This is the
        fraction of the tower capacity, at the current inlet air wet-bulb temperature,
        that is available when the tower fan is off. Manufacturers typically estimate the
        free convection capacity at approximately 10-15%. Values are entered as a fraction
        and can range from 0 to 0.2.

        Args:
            value (float): value for IDD Field `fraction_of_tower_capacity_in_free_convection_regime`
                Default value: 0.125
                value >= 0.0
                value <= 0.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_tower_capacity_in_free_convection_regime`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_tower_capacity_in_free_convection_regime`')
            if value > 0.2:
                raise ValueError('value need to be smaller 0.2 '
                                 'for field `fraction_of_tower_capacity_in_free_convection_regime`')

        self._data["Fraction of Tower Capacity in Free Convection Regime"] = value

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
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

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
        Enter the outdoor dry-bulb temperature when the basin heater turns on

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
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `evaporation_loss_mode`

        Args:
            value (str): value for IDD Field `evaporation_loss_mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
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
    def evaporation_loss_factor(self, value=0.2 ):
        """  Corresponds to IDD Field `evaporation_loss_factor`
        Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [percent/K].

        Args:
            value (float): value for IDD Field `evaporation_loss_factor`
                Unit: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
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
    def drift_loss_percent(self, value=None):
        """  Corresponds to IDD Field `drift_loss_percent`
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

        Args:
            value (float): value for IDD Field `drift_loss_percent`
                Unit: percent
                if `value` is None it will not be checked against the
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
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `blowdown_calculation_mode`

        Args:
            value (str): value for IDD Field `blowdown_calculation_mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
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
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

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
        Makeup water usage due to blowdown results from occasionally draining a small amount
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
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
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1 ):
        """  Corresponds to IDD Field `number_of_cells`

        Args:
            value (int): value for IDD Field `number_of_cells`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')

        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value=MinimalCell ):
        """  Corresponds to IDD Field `cell_control`

        Args:
            value (str): value for IDD Field `cell_control`
                Default value: MinimalCell
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
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')

        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33 ):
        """  Corresponds to IDD Field `cell_minimum_water_flow_rate_fraction`
        The allowable mininal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_minimum_water_flow_rate_fraction`
                Default value: 0.33
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
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')

        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5 ):
        """  Corresponds to IDD Field `cell_maximum_water_flow_rate_fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `cell_maximum_water_flow_rate_fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')

        self._data["Cell Maximum Water Flow Rate Fraction"] = value

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
        out.append(self._to_str(self.water_inlet_node_name))
        out.append(self._to_str(self.water_outlet_node_name))
        out.append(self._to_str(self.model_type))
        out.append(self._to_str(self.model_coefficient_name))
        out.append(self._to_str(self.design_inlet_air_wetbulb_temperature))
        out.append(self._to_str(self.design_approach_temperature))
        out.append(self._to_str(self.design_range_temperature))
        out.append(self._to_str(self.design_water_flow_rate))
        out.append(self._to_str(self.design_air_flow_rate))
        out.append(self._to_str(self.design_fan_power))
        out.append(self._to_str(self.fan_power_ratio_function_of_air_flow_rate_ratio_curve_name))
        out.append(self._to_str(self.minimum_air_flow_rate_ratio))
        out.append(self._to_str(self.fraction_of_tower_capacity_in_free_convection_regime))
        out.append(self._to_str(self.basin_heater_capacity))
        out.append(self._to_str(self.basin_heater_setpoint_temperature))
        out.append(self._to_str(self.basin_heater_operating_schedule_name))
        out.append(self._to_str(self.evaporation_loss_mode))
        out.append(self._to_str(self.evaporation_loss_factor))
        out.append(self._to_str(self.drift_loss_percent))
        out.append(self._to_str(self.blowdown_calculation_mode))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        out.append(self._to_str(self.blowdown_makeup_water_usage_schedule_name))
        out.append(self._to_str(self.supply_water_storage_tank_name))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.number_of_cells))
        out.append(self._to_str(self.cell_control))
        out.append(self._to_str(self.cell_minimum_water_flow_rate_fraction))
        out.append(self._to_str(self.cell_maximum_water_flow_rate_fraction))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)