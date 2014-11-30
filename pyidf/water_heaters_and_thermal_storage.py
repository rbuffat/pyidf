from collections import OrderedDict

class WaterHeaterMixed(object):
    """ Corresponds to IDD object `WaterHeater:Mixed`
        Water heater with well-mixed, single-node water tank. May be used to model a tankless
        water heater (small tank volume), a hot water storage tank (zero heater capacity), or
        a heat pump water heater (see WaterHeater:HeatPump.)
    
    """
    internal_name = "WaterHeater:Mixed"
    field_count = 41
    required_fields = ["Name", "Setpoint Temperature Schedule Name", "Heater Fuel Type", "Heater Thermal Efficiency", "Ambient Temperature Indicator"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterHeater:Mixed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tank Volume"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
        self._data["Deadband Temperature Difference"] = None
        self._data["Maximum Temperature Limit"] = None
        self._data["Heater Control Type"] = None
        self._data["Heater Maximum Capacity"] = None
        self._data["Heater Minimum Capacity"] = None
        self._data["Heater Ignition Minimum Flow Rate"] = None
        self._data["Heater Ignition Delay"] = None
        self._data["Heater Fuel Type"] = None
        self._data["Heater Thermal Efficiency"] = None
        self._data["Part Load Factor Curve Name"] = None
        self._data["Off Cycle Parasitic Fuel Consumption Rate"] = None
        self._data["Off Cycle Parasitic Fuel Type"] = None
        self._data["Off Cycle Parasitic Heat Fraction to Tank"] = None
        self._data["On Cycle Parasitic Fuel Consumption Rate"] = None
        self._data["On Cycle Parasitic Fuel Type"] = None
        self._data["On Cycle Parasitic Heat Fraction to Tank"] = None
        self._data["Ambient Temperature Indicator"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Off Cycle Loss Coefficient to Ambient Temperature"] = None
        self._data["Off Cycle Loss Fraction to Zone"] = None
        self._data["On Cycle Loss Coefficient to Ambient Temperature"] = None
        self._data["On Cycle Loss Fraction to Zone"] = None
        self._data["Peak Use Flow Rate"] = None
        self._data["Use Flow Rate Fraction Schedule Name"] = None
        self._data["Cold Water Supply Temperature Schedule Name"] = None
        self._data["Use Side Inlet Node Name"] = None
        self._data["Use Side Outlet Node Name"] = None
        self._data["Use Side Effectiveness"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Source Side Effectiveness"] = None
        self._data["Use Side Design Flow Rate"] = None
        self._data["Source Side Design Flow Rate"] = None
        self._data["Indirect Water Heating Recovery Time"] = None
        self._data["Source Side Flow Control Mode"] = None
        self._data["Indirect Alternate Setpoint Temperature Schedule Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_volume = None
        else:
            self.tank_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.deadband_temperature_difference = None
        else:
            self.deadband_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_temperature_limit = None
        else:
            self.maximum_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_control_type = None
        else:
            self.heater_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_maximum_capacity = None
        else:
            self.heater_maximum_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_minimum_capacity = None
        else:
            self.heater_minimum_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_ignition_minimum_flow_rate = None
        else:
            self.heater_ignition_minimum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_ignition_delay = None
        else:
            self.heater_ignition_delay = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_fuel_type = None
        else:
            self.heater_fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_thermal_efficiency = None
        else:
            self.heater_thermal_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.part_load_factor_curve_name = None
        else:
            self.part_load_factor_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_fuel_consumption_rate = None
        else:
            self.off_cycle_parasitic_fuel_consumption_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_fuel_type = None
        else:
            self.off_cycle_parasitic_fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_heat_fraction_to_tank = None
        else:
            self.off_cycle_parasitic_heat_fraction_to_tank = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_fuel_consumption_rate = None
        else:
            self.on_cycle_parasitic_fuel_consumption_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_fuel_type = None
        else:
            self.on_cycle_parasitic_fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_heat_fraction_to_tank = None
        else:
            self.on_cycle_parasitic_heat_fraction_to_tank = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_indicator = None
        else:
            self.ambient_temperature_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_loss_coefficient_to_ambient_temperature = None
        else:
            self.off_cycle_loss_coefficient_to_ambient_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_loss_fraction_to_zone = None
        else:
            self.off_cycle_loss_fraction_to_zone = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_loss_coefficient_to_ambient_temperature = None
        else:
            self.on_cycle_loss_coefficient_to_ambient_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_loss_fraction_to_zone = None
        else:
            self.on_cycle_loss_fraction_to_zone = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.peak_use_flow_rate = None
        else:
            self.peak_use_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_flow_rate_fraction_schedule_name = None
        else:
            self.use_flow_rate_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_water_supply_temperature_schedule_name = None
        else:
            self.cold_water_supply_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_inlet_node_name = None
        else:
            self.use_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_outlet_node_name = None
        else:
            self.use_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_effectiveness = None
        else:
            self.use_side_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_effectiveness = None
        else:
            self.source_side_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_design_flow_rate = None
        else:
            self.use_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_design_flow_rate = None
        else:
            self.source_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indirect_water_heating_recovery_time = None
        else:
            self.indirect_water_heating_recovery_time = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_flow_control_mode = None
        else:
            self.source_side_flow_control_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indirect_alternate_setpoint_temperature_schedule_name = None
        else:
            self.indirect_alternate_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def tank_volume(self):
        """Get tank_volume

        Returns:
            float: the value of `tank_volume` or None if not set
        """
        return self._data["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=0.0 ):
        """  Corresponds to IDD Field `tank_volume`

        Args:
            value (float): value for IDD Field `tank_volume`
                Units: m3
                IP-Units: gal
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
                                 'for field `tank_volume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tank_volume`')

        self._data["Tank Volume"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """Get deadband_temperature_difference

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set
        """
        return self._data["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=0.0 ):
        """  Corresponds to IDD Field `deadband_temperature_difference`

        Args:
            value (float): value for IDD Field `deadband_temperature_difference`
                Units: deltaC
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
                                 'for field `deadband_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deadband_temperature_difference`')

        self._data["Deadband Temperature Difference"] = value

    @property
    def maximum_temperature_limit(self):
        """Get maximum_temperature_limit

        Returns:
            float: the value of `maximum_temperature_limit` or None if not set
        """
        return self._data["Maximum Temperature Limit"]

    @maximum_temperature_limit.setter
    def maximum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `maximum_temperature_limit`

        Args:
            value (float): value for IDD Field `maximum_temperature_limit`
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
                                 'for field `maximum_temperature_limit`'.format(value))

        self._data["Maximum Temperature Limit"] = value

    @property
    def heater_control_type(self):
        """Get heater_control_type

        Returns:
            str: the value of `heater_control_type` or None if not set
        """
        return self._data["Heater Control Type"]

    @heater_control_type.setter
    def heater_control_type(self, value="Cycle"):
        """  Corresponds to IDD Field `heater_control_type`

        Args:
            value (str): value for IDD Field `heater_control_type`
                Accepted values are:
                      - Cycle
                      - Modulate
                Default value: Cycle
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heater_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heater_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heater_control_type`')
            vals = {}
            vals["cycle"] = "Cycle"
            vals["modulate"] = "Modulate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heater_control_type`'.format(value))
            value = vals[value_lower]

        self._data["Heater Control Type"] = value

    @property
    def heater_maximum_capacity(self):
        """Get heater_maximum_capacity

        Returns:
            float: the value of `heater_maximum_capacity` or None if not set
        """
        return self._data["Heater Maximum Capacity"]

    @heater_maximum_capacity.setter
    def heater_maximum_capacity(self, value=None):
        """  Corresponds to IDD Field `heater_maximum_capacity`

        Args:
            value (float): value for IDD Field `heater_maximum_capacity`
                Units: W
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
                                 'for field `heater_maximum_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_maximum_capacity`')

        self._data["Heater Maximum Capacity"] = value

    @property
    def heater_minimum_capacity(self):
        """Get heater_minimum_capacity

        Returns:
            float: the value of `heater_minimum_capacity` or None if not set
        """
        return self._data["Heater Minimum Capacity"]

    @heater_minimum_capacity.setter
    def heater_minimum_capacity(self, value=None):
        """  Corresponds to IDD Field `heater_minimum_capacity`
        Only used when Heater Control Type is set to Modulate

        Args:
            value (float): value for IDD Field `heater_minimum_capacity`
                Units: W
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
                                 'for field `heater_minimum_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_minimum_capacity`')

        self._data["Heater Minimum Capacity"] = value

    @property
    def heater_ignition_minimum_flow_rate(self):
        """Get heater_ignition_minimum_flow_rate

        Returns:
            float: the value of `heater_ignition_minimum_flow_rate` or None if not set
        """
        return self._data["Heater Ignition Minimum Flow Rate"]

    @heater_ignition_minimum_flow_rate.setter
    def heater_ignition_minimum_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `heater_ignition_minimum_flow_rate`
        Not yet implemented

        Args:
            value (float): value for IDD Field `heater_ignition_minimum_flow_rate`
                Units: m3/s
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
                                 'for field `heater_ignition_minimum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_ignition_minimum_flow_rate`')

        self._data["Heater Ignition Minimum Flow Rate"] = value

    @property
    def heater_ignition_delay(self):
        """Get heater_ignition_delay

        Returns:
            float: the value of `heater_ignition_delay` or None if not set
        """
        return self._data["Heater Ignition Delay"]

    @heater_ignition_delay.setter
    def heater_ignition_delay(self, value=0.0 ):
        """  Corresponds to IDD Field `heater_ignition_delay`
        Not yet implemented

        Args:
            value (float): value for IDD Field `heater_ignition_delay`
                Units: s
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
                                 'for field `heater_ignition_delay`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_ignition_delay`')

        self._data["Heater Ignition Delay"] = value

    @property
    def heater_fuel_type(self):
        """Get heater_fuel_type

        Returns:
            str: the value of `heater_fuel_type` or None if not set
        """
        return self._data["Heater Fuel Type"]

    @heater_fuel_type.setter
    def heater_fuel_type(self, value=None):
        """  Corresponds to IDD Field `heater_fuel_type`

        Args:
            value (str): value for IDD Field `heater_fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - OtherFuel1
                      - OtherFuel2
                      - Steam
                      - DistrictHeating
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heater_fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heater_fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heater_fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["steam"] = "Steam"
            vals["districtheating"] = "DistrictHeating"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heater_fuel_type`'.format(value))
            value = vals[value_lower]

        self._data["Heater Fuel Type"] = value

    @property
    def heater_thermal_efficiency(self):
        """Get heater_thermal_efficiency

        Returns:
            float: the value of `heater_thermal_efficiency` or None if not set
        """
        return self._data["Heater Thermal Efficiency"]

    @heater_thermal_efficiency.setter
    def heater_thermal_efficiency(self, value=None):
        """  Corresponds to IDD Field `heater_thermal_efficiency`

        Args:
            value (float): value for IDD Field `heater_thermal_efficiency`
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
                                 'for field `heater_thermal_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heater_thermal_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `heater_thermal_efficiency`')

        self._data["Heater Thermal Efficiency"] = value

    @property
    def part_load_factor_curve_name(self):
        """Get part_load_factor_curve_name

        Returns:
            str: the value of `part_load_factor_curve_name` or None if not set
        """
        return self._data["Part Load Factor Curve Name"]

    @part_load_factor_curve_name.setter
    def part_load_factor_curve_name(self, value=None):
        """  Corresponds to IDD Field `part_load_factor_curve_name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `part_load_factor_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `part_load_factor_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `part_load_factor_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `part_load_factor_curve_name`')

        self._data["Part Load Factor Curve Name"] = value

    @property
    def off_cycle_parasitic_fuel_consumption_rate(self):
        """Get off_cycle_parasitic_fuel_consumption_rate

        Returns:
            float: the value of `off_cycle_parasitic_fuel_consumption_rate` or None if not set
        """
        return self._data["Off Cycle Parasitic Fuel Consumption Rate"]

    @off_cycle_parasitic_fuel_consumption_rate.setter
    def off_cycle_parasitic_fuel_consumption_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `off_cycle_parasitic_fuel_consumption_rate`

        Args:
            value (float): value for IDD Field `off_cycle_parasitic_fuel_consumption_rate`
                Units: W
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
                                 'for field `off_cycle_parasitic_fuel_consumption_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_parasitic_fuel_consumption_rate`')

        self._data["Off Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def off_cycle_parasitic_fuel_type(self):
        """Get off_cycle_parasitic_fuel_type

        Returns:
            str: the value of `off_cycle_parasitic_fuel_type` or None if not set
        """
        return self._data["Off Cycle Parasitic Fuel Type"]

    @off_cycle_parasitic_fuel_type.setter
    def off_cycle_parasitic_fuel_type(self, value=None):
        """  Corresponds to IDD Field `off_cycle_parasitic_fuel_type`

        Args:
            value (str): value for IDD Field `off_cycle_parasitic_fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - OtherFuel1
                      - OtherFuel2
                      - Steam
                      - DistrictHeating
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `off_cycle_parasitic_fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `off_cycle_parasitic_fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `off_cycle_parasitic_fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["steam"] = "Steam"
            vals["districtheating"] = "DistrictHeating"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `off_cycle_parasitic_fuel_type`'.format(value))
            value = vals[value_lower]

        self._data["Off Cycle Parasitic Fuel Type"] = value

    @property
    def off_cycle_parasitic_heat_fraction_to_tank(self):
        """Get off_cycle_parasitic_heat_fraction_to_tank

        Returns:
            float: the value of `off_cycle_parasitic_heat_fraction_to_tank` or None if not set
        """
        return self._data["Off Cycle Parasitic Heat Fraction to Tank"]

    @off_cycle_parasitic_heat_fraction_to_tank.setter
    def off_cycle_parasitic_heat_fraction_to_tank(self, value=0.0 ):
        """  Corresponds to IDD Field `off_cycle_parasitic_heat_fraction_to_tank`

        Args:
            value (float): value for IDD Field `off_cycle_parasitic_heat_fraction_to_tank`
                Default value: 0.0
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
                                 'for field `off_cycle_parasitic_heat_fraction_to_tank`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_parasitic_heat_fraction_to_tank`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `off_cycle_parasitic_heat_fraction_to_tank`')

        self._data["Off Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def on_cycle_parasitic_fuel_consumption_rate(self):
        """Get on_cycle_parasitic_fuel_consumption_rate

        Returns:
            float: the value of `on_cycle_parasitic_fuel_consumption_rate` or None if not set
        """
        return self._data["On Cycle Parasitic Fuel Consumption Rate"]

    @on_cycle_parasitic_fuel_consumption_rate.setter
    def on_cycle_parasitic_fuel_consumption_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `on_cycle_parasitic_fuel_consumption_rate`

        Args:
            value (float): value for IDD Field `on_cycle_parasitic_fuel_consumption_rate`
                Units: W
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
                                 'for field `on_cycle_parasitic_fuel_consumption_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_parasitic_fuel_consumption_rate`')

        self._data["On Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def on_cycle_parasitic_fuel_type(self):
        """Get on_cycle_parasitic_fuel_type

        Returns:
            str: the value of `on_cycle_parasitic_fuel_type` or None if not set
        """
        return self._data["On Cycle Parasitic Fuel Type"]

    @on_cycle_parasitic_fuel_type.setter
    def on_cycle_parasitic_fuel_type(self, value=None):
        """  Corresponds to IDD Field `on_cycle_parasitic_fuel_type`

        Args:
            value (str): value for IDD Field `on_cycle_parasitic_fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - OtherFuel1
                      - OtherFuel2
                      - Steam
                      - DistrictHeating
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `on_cycle_parasitic_fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `on_cycle_parasitic_fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `on_cycle_parasitic_fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["steam"] = "Steam"
            vals["districtheating"] = "DistrictHeating"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `on_cycle_parasitic_fuel_type`'.format(value))
            value = vals[value_lower]

        self._data["On Cycle Parasitic Fuel Type"] = value

    @property
    def on_cycle_parasitic_heat_fraction_to_tank(self):
        """Get on_cycle_parasitic_heat_fraction_to_tank

        Returns:
            float: the value of `on_cycle_parasitic_heat_fraction_to_tank` or None if not set
        """
        return self._data["On Cycle Parasitic Heat Fraction to Tank"]

    @on_cycle_parasitic_heat_fraction_to_tank.setter
    def on_cycle_parasitic_heat_fraction_to_tank(self, value=0.0 ):
        """  Corresponds to IDD Field `on_cycle_parasitic_heat_fraction_to_tank`

        Args:
            value (float): value for IDD Field `on_cycle_parasitic_heat_fraction_to_tank`
                Default value: 0.0
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
                                 'for field `on_cycle_parasitic_heat_fraction_to_tank`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_parasitic_heat_fraction_to_tank`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `on_cycle_parasitic_heat_fraction_to_tank`')

        self._data["On Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def ambient_temperature_indicator(self):
        """Get ambient_temperature_indicator

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set
        """
        return self._data["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_indicator`

        Args:
            value (str): value for IDD Field `ambient_temperature_indicator`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_indicator`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ambient_temperature_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_schedule_name`')

        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_zone_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_zone_name`')

        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_outdoor_air_node_name`
        required for Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `ambient_temperature_outdoor_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_outdoor_air_node_name`')

        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def off_cycle_loss_coefficient_to_ambient_temperature(self):
        """Get off_cycle_loss_coefficient_to_ambient_temperature

        Returns:
            float: the value of `off_cycle_loss_coefficient_to_ambient_temperature` or None if not set
        """
        return self._data["Off Cycle Loss Coefficient to Ambient Temperature"]

    @off_cycle_loss_coefficient_to_ambient_temperature.setter
    def off_cycle_loss_coefficient_to_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `off_cycle_loss_coefficient_to_ambient_temperature`

        Args:
            value (float): value for IDD Field `off_cycle_loss_coefficient_to_ambient_temperature`
                Units: W/K
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
                                 'for field `off_cycle_loss_coefficient_to_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_loss_coefficient_to_ambient_temperature`')

        self._data["Off Cycle Loss Coefficient to Ambient Temperature"] = value

    @property
    def off_cycle_loss_fraction_to_zone(self):
        """Get off_cycle_loss_fraction_to_zone

        Returns:
            float: the value of `off_cycle_loss_fraction_to_zone` or None if not set
        """
        return self._data["Off Cycle Loss Fraction to Zone"]

    @off_cycle_loss_fraction_to_zone.setter
    def off_cycle_loss_fraction_to_zone(self, value=1.0 ):
        """  Corresponds to IDD Field `off_cycle_loss_fraction_to_zone`

        Args:
            value (float): value for IDD Field `off_cycle_loss_fraction_to_zone`
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
                                 'for field `off_cycle_loss_fraction_to_zone`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_loss_fraction_to_zone`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `off_cycle_loss_fraction_to_zone`')

        self._data["Off Cycle Loss Fraction to Zone"] = value

    @property
    def on_cycle_loss_coefficient_to_ambient_temperature(self):
        """Get on_cycle_loss_coefficient_to_ambient_temperature

        Returns:
            float: the value of `on_cycle_loss_coefficient_to_ambient_temperature` or None if not set
        """
        return self._data["On Cycle Loss Coefficient to Ambient Temperature"]

    @on_cycle_loss_coefficient_to_ambient_temperature.setter
    def on_cycle_loss_coefficient_to_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `on_cycle_loss_coefficient_to_ambient_temperature`

        Args:
            value (float): value for IDD Field `on_cycle_loss_coefficient_to_ambient_temperature`
                Units: W/K
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
                                 'for field `on_cycle_loss_coefficient_to_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_loss_coefficient_to_ambient_temperature`')

        self._data["On Cycle Loss Coefficient to Ambient Temperature"] = value

    @property
    def on_cycle_loss_fraction_to_zone(self):
        """Get on_cycle_loss_fraction_to_zone

        Returns:
            float: the value of `on_cycle_loss_fraction_to_zone` or None if not set
        """
        return self._data["On Cycle Loss Fraction to Zone"]

    @on_cycle_loss_fraction_to_zone.setter
    def on_cycle_loss_fraction_to_zone(self, value=1.0 ):
        """  Corresponds to IDD Field `on_cycle_loss_fraction_to_zone`

        Args:
            value (float): value for IDD Field `on_cycle_loss_fraction_to_zone`
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
                                 'for field `on_cycle_loss_fraction_to_zone`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_loss_fraction_to_zone`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `on_cycle_loss_fraction_to_zone`')

        self._data["On Cycle Loss Fraction to Zone"] = value

    @property
    def peak_use_flow_rate(self):
        """Get peak_use_flow_rate

        Returns:
            float: the value of `peak_use_flow_rate` or None if not set
        """
        return self._data["Peak Use Flow Rate"]

    @peak_use_flow_rate.setter
    def peak_use_flow_rate(self, value=None):
        """  Corresponds to IDD Field `peak_use_flow_rate`
        Only used if Use Side Node connections are blank

        Args:
            value (float): value for IDD Field `peak_use_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `peak_use_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `peak_use_flow_rate`')

        self._data["Peak Use Flow Rate"] = value

    @property
    def use_flow_rate_fraction_schedule_name(self):
        """Get use_flow_rate_fraction_schedule_name

        Returns:
            str: the value of `use_flow_rate_fraction_schedule_name` or None if not set
        """
        return self._data["Use Flow Rate Fraction Schedule Name"]

    @use_flow_rate_fraction_schedule_name.setter
    def use_flow_rate_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `use_flow_rate_fraction_schedule_name`
        Only used if Use Side Node connections are blank

        Args:
            value (str): value for IDD Field `use_flow_rate_fraction_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_flow_rate_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_flow_rate_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_flow_rate_fraction_schedule_name`')

        self._data["Use Flow Rate Fraction Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """Get cold_water_supply_temperature_schedule_name

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set
        """
        return self._data["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `cold_water_supply_temperature_schedule_name`
        Only used if Use Side Node connections are blank
        Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `cold_water_supply_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cold_water_supply_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_water_supply_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cold_water_supply_temperature_schedule_name`')

        self._data["Cold Water Supply Temperature Schedule Name"] = value

    @property
    def use_side_inlet_node_name(self):
        """Get use_side_inlet_node_name

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set
        """
        return self._data["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_inlet_node_name`')

        self._data["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """Get use_side_outlet_node_name

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set
        """
        return self._data["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_outlet_node_name`')

        self._data["Use Side Outlet Node Name"] = value

    @property
    def use_side_effectiveness(self):
        """Get use_side_effectiveness

        Returns:
            float: the value of `use_side_effectiveness` or None if not set
        """
        return self._data["Use Side Effectiveness"]

    @use_side_effectiveness.setter
    def use_side_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `use_side_effectiveness`

        Args:
            value (float): value for IDD Field `use_side_effectiveness`
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
                                 'for field `use_side_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `use_side_effectiveness`')

        self._data["Use Side Effectiveness"] = value

    @property
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def source_side_effectiveness(self):
        """Get source_side_effectiveness

        Returns:
            float: the value of `source_side_effectiveness` or None if not set
        """
        return self._data["Source Side Effectiveness"]

    @source_side_effectiveness.setter
    def source_side_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `source_side_effectiveness`

        Args:
            value (float): value for IDD Field `source_side_effectiveness`
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
                                 'for field `source_side_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `source_side_effectiveness`')

        self._data["Source Side Effectiveness"] = value

    @property
    def use_side_design_flow_rate(self):
        """Get use_side_design_flow_rate

        Returns:
            float: the value of `use_side_design_flow_rate` or None if not set
        """
        return self._data["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `use_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `use_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `use_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_design_flow_rate`')

        self._data["Use Side Design Flow Rate"] = value

    @property
    def source_side_design_flow_rate(self):
        """Get source_side_design_flow_rate

        Returns:
            float: the value of `source_side_design_flow_rate` or None if not set
        """
        return self._data["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `source_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_design_flow_rate`')

        self._data["Source Side Design Flow Rate"] = value

    @property
    def indirect_water_heating_recovery_time(self):
        """Get indirect_water_heating_recovery_time

        Returns:
            float: the value of `indirect_water_heating_recovery_time` or None if not set
        """
        return self._data["Indirect Water Heating Recovery Time"]

    @indirect_water_heating_recovery_time.setter
    def indirect_water_heating_recovery_time(self, value=1.5 ):
        """  Corresponds to IDD Field `indirect_water_heating_recovery_time`
        Parameter for autosizing design flow rates for indirectly heated water tanks
        Time required to raise temperature of entire tank from 14.4C to 57.2C

        Args:
            value (float): value for IDD Field `indirect_water_heating_recovery_time`
                Units: hr
                Default value: 1.5
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
                                 'for field `indirect_water_heating_recovery_time`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `indirect_water_heating_recovery_time`')

        self._data["Indirect Water Heating Recovery Time"] = value

    @property
    def source_side_flow_control_mode(self):
        """Get source_side_flow_control_mode

        Returns:
            str: the value of `source_side_flow_control_mode` or None if not set
        """
        return self._data["Source Side Flow Control Mode"]

    @source_side_flow_control_mode.setter
    def source_side_flow_control_mode(self, value="IndirectHeatPrimarySetpoint"):
        """  Corresponds to IDD Field `source_side_flow_control_mode`
        StorageTank mode always requests flow unless tank is at its Maximum Temperature Limit
        IndirectHeatPrimarySetpoint mode requests flow whenever primary setpoint calls for heat
        IndirectHeatAlternateSetpoint mode requests flow whenever alternate indirect setpoint calls for heat

        Args:
            value (str): value for IDD Field `source_side_flow_control_mode`
                Accepted values are:
                      - StorageTank
                      - IndirectHeatPrimarySetpoint
                      - IndirectHeatAlternateSetpoint
                Default value: IndirectHeatPrimarySetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_flow_control_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_flow_control_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_flow_control_mode`')
            vals = {}
            vals["storagetank"] = "StorageTank"
            vals["indirectheatprimarysetpoint"] = "IndirectHeatPrimarySetpoint"
            vals["indirectheatalternatesetpoint"] = "IndirectHeatAlternateSetpoint"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `source_side_flow_control_mode`'.format(value))
            value = vals[value_lower]

        self._data["Source Side Flow Control Mode"] = value

    @property
    def indirect_alternate_setpoint_temperature_schedule_name(self):
        """Get indirect_alternate_setpoint_temperature_schedule_name

        Returns:
            str: the value of `indirect_alternate_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Indirect Alternate Setpoint Temperature Schedule Name"]

    @indirect_alternate_setpoint_temperature_schedule_name.setter
    def indirect_alternate_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `indirect_alternate_setpoint_temperature_schedule_name`
        This field is only used if the previous is set to IndirectHeatAlternateSetpoint

        Args:
            value (str): value for IDD Field `indirect_alternate_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `indirect_alternate_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `indirect_alternate_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `indirect_alternate_setpoint_temperature_schedule_name`')

        self._data["Indirect Alternate Setpoint Temperature Schedule Name"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class WaterHeaterStratified(object):
    """ Corresponds to IDD object `WaterHeater:Stratified`
        Water heater with stratified, multi-node water tank. May be used to model a tankless
        water heater (small tank volume), a hot water storage tank (zero heater capacity), or
        a heat pump water heater (see WaterHeater:HeatPump.)
    
    """
    internal_name = "WaterHeater:Stratified"
    field_count = 65
    required_fields = ["Name", "Tank Volume", "Tank Height", "Heater 1 Setpoint Temperature Schedule Name", "Heater 2 Setpoint Temperature Schedule Name", "Heater Fuel Type", "Heater Thermal Efficiency", "Ambient Temperature Indicator"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterHeater:Stratified`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Tank Volume"] = None
        self._data["Tank Height"] = None
        self._data["Tank Shape"] = None
        self._data["Tank Perimeter"] = None
        self._data["Maximum Temperature Limit"] = None
        self._data["Heater Priority Control"] = None
        self._data["Heater 1 Setpoint Temperature Schedule Name"] = None
        self._data["Heater 1 Deadband Temperature Difference"] = None
        self._data["Heater 1 Capacity"] = None
        self._data["Heater 1 Height"] = None
        self._data["Heater 2 Setpoint Temperature Schedule Name"] = None
        self._data["Heater 2 Deadband Temperature Difference"] = None
        self._data["Heater 2 Capacity"] = None
        self._data["Heater 2 Height"] = None
        self._data["Heater Fuel Type"] = None
        self._data["Heater Thermal Efficiency"] = None
        self._data["Off Cycle Parasitic Fuel Consumption Rate"] = None
        self._data["Off Cycle Parasitic Fuel Type"] = None
        self._data["Off Cycle Parasitic Heat Fraction to Tank"] = None
        self._data["Off Cycle Parasitic Height"] = None
        self._data["On Cycle Parasitic Fuel Consumption Rate"] = None
        self._data["On Cycle Parasitic Fuel Type"] = None
        self._data["On Cycle Parasitic Heat Fraction to Tank"] = None
        self._data["On Cycle Parasitic Height"] = None
        self._data["Ambient Temperature Indicator"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = None
        self._data["Skin Loss Fraction to Zone"] = None
        self._data["Off Cycle Flue Loss Coefficient to Ambient Temperature"] = None
        self._data["Off Cycle Flue Loss Fraction to Zone"] = None
        self._data["Peak Use Flow Rate"] = None
        self._data["Use Flow Rate Fraction Schedule Name"] = None
        self._data["Cold Water Supply Temperature Schedule Name"] = None
        self._data["Use Side Inlet Node Name"] = None
        self._data["Use Side Outlet Node Name"] = None
        self._data["Use Side Effectiveness"] = None
        self._data["Use Side Inlet Height"] = None
        self._data["Use Side Outlet Height"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Source Side Effectiveness"] = None
        self._data["Source Side Inlet Height"] = None
        self._data["Source Side Outlet Height"] = None
        self._data["Inlet Mode"] = None
        self._data["Use Side Design Flow Rate"] = None
        self._data["Source Side Design Flow Rate"] = None
        self._data["Indirect Water Heating Recovery Time"] = None
        self._data["Number of Nodes"] = None
        self._data["Additional Destratification Conductivity"] = None
        self._data["Node 1 Additional Loss Coefficient"] = None
        self._data["Node 2 Additional Loss Coefficient"] = None
        self._data["Node 3 Additional Loss Coefficient"] = None
        self._data["Node 4 Additional Loss Coefficient"] = None
        self._data["Node 5 Additional Loss Coefficient"] = None
        self._data["Node 6 Additional Loss Coefficient"] = None
        self._data["Node 7 Additional Loss Coefficient"] = None
        self._data["Node 8 Additional Loss Coefficient"] = None
        self._data["Node 9 Additional Loss Coefficient"] = None
        self._data["Node 10 Additional Loss Coefficient"] = None
        self._data["Source Side Flow Control Mode"] = None
        self._data["Indirect Alternate Setpoint Temperature Schedule Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_volume = None
        else:
            self.tank_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_height = None
        else:
            self.tank_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_shape = None
        else:
            self.tank_shape = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_perimeter = None
        else:
            self.tank_perimeter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_temperature_limit = None
        else:
            self.maximum_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_priority_control = None
        else:
            self.heater_priority_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_1_setpoint_temperature_schedule_name = None
        else:
            self.heater_1_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_1_deadband_temperature_difference = None
        else:
            self.heater_1_deadband_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_1_capacity = None
        else:
            self.heater_1_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_1_height = None
        else:
            self.heater_1_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_2_setpoint_temperature_schedule_name = None
        else:
            self.heater_2_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_2_deadband_temperature_difference = None
        else:
            self.heater_2_deadband_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_2_capacity = None
        else:
            self.heater_2_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_2_height = None
        else:
            self.heater_2_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_fuel_type = None
        else:
            self.heater_fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heater_thermal_efficiency = None
        else:
            self.heater_thermal_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_fuel_consumption_rate = None
        else:
            self.off_cycle_parasitic_fuel_consumption_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_fuel_type = None
        else:
            self.off_cycle_parasitic_fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_heat_fraction_to_tank = None
        else:
            self.off_cycle_parasitic_heat_fraction_to_tank = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_height = None
        else:
            self.off_cycle_parasitic_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_fuel_consumption_rate = None
        else:
            self.on_cycle_parasitic_fuel_consumption_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_fuel_type = None
        else:
            self.on_cycle_parasitic_fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_heat_fraction_to_tank = None
        else:
            self.on_cycle_parasitic_heat_fraction_to_tank = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_height = None
        else:
            self.on_cycle_parasitic_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_indicator = None
        else:
            self.ambient_temperature_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = None
        else:
            self.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.skin_loss_fraction_to_zone = None
        else:
            self.skin_loss_fraction_to_zone = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_flue_loss_coefficient_to_ambient_temperature = None
        else:
            self.off_cycle_flue_loss_coefficient_to_ambient_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_flue_loss_fraction_to_zone = None
        else:
            self.off_cycle_flue_loss_fraction_to_zone = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.peak_use_flow_rate = None
        else:
            self.peak_use_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_flow_rate_fraction_schedule_name = None
        else:
            self.use_flow_rate_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_water_supply_temperature_schedule_name = None
        else:
            self.cold_water_supply_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_inlet_node_name = None
        else:
            self.use_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_outlet_node_name = None
        else:
            self.use_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_effectiveness = None
        else:
            self.use_side_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_inlet_height = None
        else:
            self.use_side_inlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_outlet_height = None
        else:
            self.use_side_outlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_effectiveness = None
        else:
            self.source_side_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_inlet_height = None
        else:
            self.source_side_inlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_outlet_height = None
        else:
            self.source_side_outlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_mode = None
        else:
            self.inlet_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_design_flow_rate = None
        else:
            self.use_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_design_flow_rate = None
        else:
            self.source_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indirect_water_heating_recovery_time = None
        else:
            self.indirect_water_heating_recovery_time = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_nodes = None
        else:
            self.number_of_nodes = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.additional_destratification_conductivity = None
        else:
            self.additional_destratification_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_1_additional_loss_coefficient = None
        else:
            self.node_1_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_2_additional_loss_coefficient = None
        else:
            self.node_2_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_3_additional_loss_coefficient = None
        else:
            self.node_3_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_4_additional_loss_coefficient = None
        else:
            self.node_4_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_5_additional_loss_coefficient = None
        else:
            self.node_5_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_6_additional_loss_coefficient = None
        else:
            self.node_6_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_7_additional_loss_coefficient = None
        else:
            self.node_7_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_8_additional_loss_coefficient = None
        else:
            self.node_8_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_9_additional_loss_coefficient = None
        else:
            self.node_9_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_10_additional_loss_coefficient = None
        else:
            self.node_10_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_flow_control_mode = None
        else:
            self.source_side_flow_control_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indirect_alternate_setpoint_temperature_schedule_name = None
        else:
            self.indirect_alternate_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

    @property
    def tank_volume(self):
        """Get tank_volume

        Returns:
            float: the value of `tank_volume` or None if not set
        """
        return self._data["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=None):
        """  Corresponds to IDD Field `tank_volume`

        Args:
            value (float): value for IDD Field `tank_volume`
                Units: m3
                IP-Units: gal
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
                                 'for field `tank_volume`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_volume`')

        self._data["Tank Volume"] = value

    @property
    def tank_height(self):
        """Get tank_height

        Returns:
            float: the value of `tank_height` or None if not set
        """
        return self._data["Tank Height"]

    @tank_height.setter
    def tank_height(self, value=None):
        """  Corresponds to IDD Field `tank_height`
        Height is measured in the axial direction for horizontal cylinders

        Args:
            value (float): value for IDD Field `tank_height`
                Units: m
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
                                 'for field `tank_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_height`')

        self._data["Tank Height"] = value

    @property
    def tank_shape(self):
        """Get tank_shape

        Returns:
            str: the value of `tank_shape` or None if not set
        """
        return self._data["Tank Shape"]

    @tank_shape.setter
    def tank_shape(self, value="VerticalCylinder"):
        """  Corresponds to IDD Field `tank_shape`

        Args:
            value (str): value for IDD Field `tank_shape`
                Accepted values are:
                      - VerticalCylinder
                      - HorizontalCylinder
                      - Other
                Default value: VerticalCylinder
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `tank_shape`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_shape`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `tank_shape`')
            vals = {}
            vals["verticalcylinder"] = "VerticalCylinder"
            vals["horizontalcylinder"] = "HorizontalCylinder"
            vals["other"] = "Other"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `tank_shape`'.format(value))
            value = vals[value_lower]

        self._data["Tank Shape"] = value

    @property
    def tank_perimeter(self):
        """Get tank_perimeter

        Returns:
            float: the value of `tank_perimeter` or None if not set
        """
        return self._data["Tank Perimeter"]

    @tank_perimeter.setter
    def tank_perimeter(self, value=None):
        """  Corresponds to IDD Field `tank_perimeter`
        Only used if Tank Shape is Other

        Args:
            value (float): value for IDD Field `tank_perimeter`
                Units: m
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
                                 'for field `tank_perimeter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tank_perimeter`')

        self._data["Tank Perimeter"] = value

    @property
    def maximum_temperature_limit(self):
        """Get maximum_temperature_limit

        Returns:
            float: the value of `maximum_temperature_limit` or None if not set
        """
        return self._data["Maximum Temperature Limit"]

    @maximum_temperature_limit.setter
    def maximum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `maximum_temperature_limit`

        Args:
            value (float): value for IDD Field `maximum_temperature_limit`
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
                                 'for field `maximum_temperature_limit`'.format(value))

        self._data["Maximum Temperature Limit"] = value

    @property
    def heater_priority_control(self):
        """Get heater_priority_control

        Returns:
            str: the value of `heater_priority_control` or None if not set
        """
        return self._data["Heater Priority Control"]

    @heater_priority_control.setter
    def heater_priority_control(self, value="MasterSlave"):
        """  Corresponds to IDD Field `heater_priority_control`

        Args:
            value (str): value for IDD Field `heater_priority_control`
                Accepted values are:
                      - MasterSlave
                      - Simultaneous
                Default value: MasterSlave
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heater_priority_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heater_priority_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heater_priority_control`')
            vals = {}
            vals["masterslave"] = "MasterSlave"
            vals["simultaneous"] = "Simultaneous"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heater_priority_control`'.format(value))
            value = vals[value_lower]

        self._data["Heater Priority Control"] = value

    @property
    def heater_1_setpoint_temperature_schedule_name(self):
        """Get heater_1_setpoint_temperature_schedule_name

        Returns:
            str: the value of `heater_1_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Heater 1 Setpoint Temperature Schedule Name"]

    @heater_1_setpoint_temperature_schedule_name.setter
    def heater_1_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `heater_1_setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `heater_1_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heater_1_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heater_1_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heater_1_setpoint_temperature_schedule_name`')

        self._data["Heater 1 Setpoint Temperature Schedule Name"] = value

    @property
    def heater_1_deadband_temperature_difference(self):
        """Get heater_1_deadband_temperature_difference

        Returns:
            float: the value of `heater_1_deadband_temperature_difference` or None if not set
        """
        return self._data["Heater 1 Deadband Temperature Difference"]

    @heater_1_deadband_temperature_difference.setter
    def heater_1_deadband_temperature_difference(self, value=0.0 ):
        """  Corresponds to IDD Field `heater_1_deadband_temperature_difference`

        Args:
            value (float): value for IDD Field `heater_1_deadband_temperature_difference`
                Units: deltaC
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
                                 'for field `heater_1_deadband_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_1_deadband_temperature_difference`')

        self._data["Heater 1 Deadband Temperature Difference"] = value

    @property
    def heater_1_capacity(self):
        """Get heater_1_capacity

        Returns:
            float: the value of `heater_1_capacity` or None if not set
        """
        return self._data["Heater 1 Capacity"]

    @heater_1_capacity.setter
    def heater_1_capacity(self, value=None):
        """  Corresponds to IDD Field `heater_1_capacity`

        Args:
            value (float): value for IDD Field `heater_1_capacity`
                Units: W
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
                                 'for field `heater_1_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_1_capacity`')

        self._data["Heater 1 Capacity"] = value

    @property
    def heater_1_height(self):
        """Get heater_1_height

        Returns:
            float: the value of `heater_1_height` or None if not set
        """
        return self._data["Heater 1 Height"]

    @heater_1_height.setter
    def heater_1_height(self, value=None):
        """  Corresponds to IDD Field `heater_1_height`

        Args:
            value (float): value for IDD Field `heater_1_height`
                Units: m
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
                                 'for field `heater_1_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_1_height`')

        self._data["Heater 1 Height"] = value

    @property
    def heater_2_setpoint_temperature_schedule_name(self):
        """Get heater_2_setpoint_temperature_schedule_name

        Returns:
            str: the value of `heater_2_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Heater 2 Setpoint Temperature Schedule Name"]

    @heater_2_setpoint_temperature_schedule_name.setter
    def heater_2_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `heater_2_setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `heater_2_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heater_2_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heater_2_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heater_2_setpoint_temperature_schedule_name`')

        self._data["Heater 2 Setpoint Temperature Schedule Name"] = value

    @property
    def heater_2_deadband_temperature_difference(self):
        """Get heater_2_deadband_temperature_difference

        Returns:
            float: the value of `heater_2_deadband_temperature_difference` or None if not set
        """
        return self._data["Heater 2 Deadband Temperature Difference"]

    @heater_2_deadband_temperature_difference.setter
    def heater_2_deadband_temperature_difference(self, value=0.0 ):
        """  Corresponds to IDD Field `heater_2_deadband_temperature_difference`

        Args:
            value (float): value for IDD Field `heater_2_deadband_temperature_difference`
                Units: deltaC
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
                                 'for field `heater_2_deadband_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_2_deadband_temperature_difference`')

        self._data["Heater 2 Deadband Temperature Difference"] = value

    @property
    def heater_2_capacity(self):
        """Get heater_2_capacity

        Returns:
            float: the value of `heater_2_capacity` or None if not set
        """
        return self._data["Heater 2 Capacity"]

    @heater_2_capacity.setter
    def heater_2_capacity(self, value=None):
        """  Corresponds to IDD Field `heater_2_capacity`

        Args:
            value (float): value for IDD Field `heater_2_capacity`
                Units: W
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
                                 'for field `heater_2_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_2_capacity`')

        self._data["Heater 2 Capacity"] = value

    @property
    def heater_2_height(self):
        """Get heater_2_height

        Returns:
            float: the value of `heater_2_height` or None if not set
        """
        return self._data["Heater 2 Height"]

    @heater_2_height.setter
    def heater_2_height(self, value=None):
        """  Corresponds to IDD Field `heater_2_height`

        Args:
            value (float): value for IDD Field `heater_2_height`
                Units: m
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
                                 'for field `heater_2_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heater_2_height`')

        self._data["Heater 2 Height"] = value

    @property
    def heater_fuel_type(self):
        """Get heater_fuel_type

        Returns:
            str: the value of `heater_fuel_type` or None if not set
        """
        return self._data["Heater Fuel Type"]

    @heater_fuel_type.setter
    def heater_fuel_type(self, value=None):
        """  Corresponds to IDD Field `heater_fuel_type`

        Args:
            value (str): value for IDD Field `heater_fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - OtherFuel1
                      - OtherFuel2
                      - Steam
                      - DistrictHeating
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heater_fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heater_fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heater_fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["steam"] = "Steam"
            vals["districtheating"] = "DistrictHeating"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heater_fuel_type`'.format(value))
            value = vals[value_lower]

        self._data["Heater Fuel Type"] = value

    @property
    def heater_thermal_efficiency(self):
        """Get heater_thermal_efficiency

        Returns:
            float: the value of `heater_thermal_efficiency` or None if not set
        """
        return self._data["Heater Thermal Efficiency"]

    @heater_thermal_efficiency.setter
    def heater_thermal_efficiency(self, value=None):
        """  Corresponds to IDD Field `heater_thermal_efficiency`

        Args:
            value (float): value for IDD Field `heater_thermal_efficiency`
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
                                 'for field `heater_thermal_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heater_thermal_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `heater_thermal_efficiency`')

        self._data["Heater Thermal Efficiency"] = value

    @property
    def off_cycle_parasitic_fuel_consumption_rate(self):
        """Get off_cycle_parasitic_fuel_consumption_rate

        Returns:
            float: the value of `off_cycle_parasitic_fuel_consumption_rate` or None if not set
        """
        return self._data["Off Cycle Parasitic Fuel Consumption Rate"]

    @off_cycle_parasitic_fuel_consumption_rate.setter
    def off_cycle_parasitic_fuel_consumption_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `off_cycle_parasitic_fuel_consumption_rate`

        Args:
            value (float): value for IDD Field `off_cycle_parasitic_fuel_consumption_rate`
                Units: W
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
                                 'for field `off_cycle_parasitic_fuel_consumption_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_parasitic_fuel_consumption_rate`')

        self._data["Off Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def off_cycle_parasitic_fuel_type(self):
        """Get off_cycle_parasitic_fuel_type

        Returns:
            str: the value of `off_cycle_parasitic_fuel_type` or None if not set
        """
        return self._data["Off Cycle Parasitic Fuel Type"]

    @off_cycle_parasitic_fuel_type.setter
    def off_cycle_parasitic_fuel_type(self, value=None):
        """  Corresponds to IDD Field `off_cycle_parasitic_fuel_type`

        Args:
            value (str): value for IDD Field `off_cycle_parasitic_fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - OtherFuel1
                      - OtherFuel2
                      - Steam
                      - DistrictHeating
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `off_cycle_parasitic_fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `off_cycle_parasitic_fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `off_cycle_parasitic_fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["steam"] = "Steam"
            vals["districtheating"] = "DistrictHeating"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `off_cycle_parasitic_fuel_type`'.format(value))
            value = vals[value_lower]

        self._data["Off Cycle Parasitic Fuel Type"] = value

    @property
    def off_cycle_parasitic_heat_fraction_to_tank(self):
        """Get off_cycle_parasitic_heat_fraction_to_tank

        Returns:
            float: the value of `off_cycle_parasitic_heat_fraction_to_tank` or None if not set
        """
        return self._data["Off Cycle Parasitic Heat Fraction to Tank"]

    @off_cycle_parasitic_heat_fraction_to_tank.setter
    def off_cycle_parasitic_heat_fraction_to_tank(self, value=0.0 ):
        """  Corresponds to IDD Field `off_cycle_parasitic_heat_fraction_to_tank`

        Args:
            value (float): value for IDD Field `off_cycle_parasitic_heat_fraction_to_tank`
                Default value: 0.0
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
                                 'for field `off_cycle_parasitic_heat_fraction_to_tank`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_parasitic_heat_fraction_to_tank`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `off_cycle_parasitic_heat_fraction_to_tank`')

        self._data["Off Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def off_cycle_parasitic_height(self):
        """Get off_cycle_parasitic_height

        Returns:
            float: the value of `off_cycle_parasitic_height` or None if not set
        """
        return self._data["Off Cycle Parasitic Height"]

    @off_cycle_parasitic_height.setter
    def off_cycle_parasitic_height(self, value=0.0 ):
        """  Corresponds to IDD Field `off_cycle_parasitic_height`

        Args:
            value (float): value for IDD Field `off_cycle_parasitic_height`
                Units: m
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
                                 'for field `off_cycle_parasitic_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_parasitic_height`')

        self._data["Off Cycle Parasitic Height"] = value

    @property
    def on_cycle_parasitic_fuel_consumption_rate(self):
        """Get on_cycle_parasitic_fuel_consumption_rate

        Returns:
            float: the value of `on_cycle_parasitic_fuel_consumption_rate` or None if not set
        """
        return self._data["On Cycle Parasitic Fuel Consumption Rate"]

    @on_cycle_parasitic_fuel_consumption_rate.setter
    def on_cycle_parasitic_fuel_consumption_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `on_cycle_parasitic_fuel_consumption_rate`

        Args:
            value (float): value for IDD Field `on_cycle_parasitic_fuel_consumption_rate`
                Units: W
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
                                 'for field `on_cycle_parasitic_fuel_consumption_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_parasitic_fuel_consumption_rate`')

        self._data["On Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def on_cycle_parasitic_fuel_type(self):
        """Get on_cycle_parasitic_fuel_type

        Returns:
            str: the value of `on_cycle_parasitic_fuel_type` or None if not set
        """
        return self._data["On Cycle Parasitic Fuel Type"]

    @on_cycle_parasitic_fuel_type.setter
    def on_cycle_parasitic_fuel_type(self, value=None):
        """  Corresponds to IDD Field `on_cycle_parasitic_fuel_type`

        Args:
            value (str): value for IDD Field `on_cycle_parasitic_fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - OtherFuel1
                      - OtherFuel2
                      - Steam
                      - DistrictHeating
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `on_cycle_parasitic_fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `on_cycle_parasitic_fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `on_cycle_parasitic_fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["steam"] = "Steam"
            vals["districtheating"] = "DistrictHeating"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `on_cycle_parasitic_fuel_type`'.format(value))
            value = vals[value_lower]

        self._data["On Cycle Parasitic Fuel Type"] = value

    @property
    def on_cycle_parasitic_heat_fraction_to_tank(self):
        """Get on_cycle_parasitic_heat_fraction_to_tank

        Returns:
            float: the value of `on_cycle_parasitic_heat_fraction_to_tank` or None if not set
        """
        return self._data["On Cycle Parasitic Heat Fraction to Tank"]

    @on_cycle_parasitic_heat_fraction_to_tank.setter
    def on_cycle_parasitic_heat_fraction_to_tank(self, value=0.0 ):
        """  Corresponds to IDD Field `on_cycle_parasitic_heat_fraction_to_tank`

        Args:
            value (float): value for IDD Field `on_cycle_parasitic_heat_fraction_to_tank`
                Default value: 0.0
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
                                 'for field `on_cycle_parasitic_heat_fraction_to_tank`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_parasitic_heat_fraction_to_tank`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `on_cycle_parasitic_heat_fraction_to_tank`')

        self._data["On Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def on_cycle_parasitic_height(self):
        """Get on_cycle_parasitic_height

        Returns:
            float: the value of `on_cycle_parasitic_height` or None if not set
        """
        return self._data["On Cycle Parasitic Height"]

    @on_cycle_parasitic_height.setter
    def on_cycle_parasitic_height(self, value=0.0 ):
        """  Corresponds to IDD Field `on_cycle_parasitic_height`

        Args:
            value (float): value for IDD Field `on_cycle_parasitic_height`
                Units: m
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
                                 'for field `on_cycle_parasitic_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_parasitic_height`')

        self._data["On Cycle Parasitic Height"] = value

    @property
    def ambient_temperature_indicator(self):
        """Get ambient_temperature_indicator

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set
        """
        return self._data["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_indicator`

        Args:
            value (str): value for IDD Field `ambient_temperature_indicator`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_indicator`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ambient_temperature_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_schedule_name`')

        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_zone_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_zone_name`')

        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_outdoor_air_node_name`
        required for Ambient Temperature Indicater=Outdoors

        Args:
            value (str): value for IDD Field `ambient_temperature_outdoor_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_outdoor_air_node_name`')

        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(self):
        """Get uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature

        Returns:
            float: the value of `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature` or None if not set
        """
        return self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"]

    @uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature.setter
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`

        Args:
            value (float): value for IDD Field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`
                Units: W/m2-K
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
                                 'for field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`')

        self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = value

    @property
    def skin_loss_fraction_to_zone(self):
        """Get skin_loss_fraction_to_zone

        Returns:
            float: the value of `skin_loss_fraction_to_zone` or None if not set
        """
        return self._data["Skin Loss Fraction to Zone"]

    @skin_loss_fraction_to_zone.setter
    def skin_loss_fraction_to_zone(self, value=1.0 ):
        """  Corresponds to IDD Field `skin_loss_fraction_to_zone`

        Args:
            value (float): value for IDD Field `skin_loss_fraction_to_zone`
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
                                 'for field `skin_loss_fraction_to_zone`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `skin_loss_fraction_to_zone`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `skin_loss_fraction_to_zone`')

        self._data["Skin Loss Fraction to Zone"] = value

    @property
    def off_cycle_flue_loss_coefficient_to_ambient_temperature(self):
        """Get off_cycle_flue_loss_coefficient_to_ambient_temperature

        Returns:
            float: the value of `off_cycle_flue_loss_coefficient_to_ambient_temperature` or None if not set
        """
        return self._data["Off Cycle Flue Loss Coefficient to Ambient Temperature"]

    @off_cycle_flue_loss_coefficient_to_ambient_temperature.setter
    def off_cycle_flue_loss_coefficient_to_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `off_cycle_flue_loss_coefficient_to_ambient_temperature`

        Args:
            value (float): value for IDD Field `off_cycle_flue_loss_coefficient_to_ambient_temperature`
                Units: W/K
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
                                 'for field `off_cycle_flue_loss_coefficient_to_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_flue_loss_coefficient_to_ambient_temperature`')

        self._data["Off Cycle Flue Loss Coefficient to Ambient Temperature"] = value

    @property
    def off_cycle_flue_loss_fraction_to_zone(self):
        """Get off_cycle_flue_loss_fraction_to_zone

        Returns:
            float: the value of `off_cycle_flue_loss_fraction_to_zone` or None if not set
        """
        return self._data["Off Cycle Flue Loss Fraction to Zone"]

    @off_cycle_flue_loss_fraction_to_zone.setter
    def off_cycle_flue_loss_fraction_to_zone(self, value=1.0 ):
        """  Corresponds to IDD Field `off_cycle_flue_loss_fraction_to_zone`

        Args:
            value (float): value for IDD Field `off_cycle_flue_loss_fraction_to_zone`
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
                                 'for field `off_cycle_flue_loss_fraction_to_zone`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_flue_loss_fraction_to_zone`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `off_cycle_flue_loss_fraction_to_zone`')

        self._data["Off Cycle Flue Loss Fraction to Zone"] = value

    @property
    def peak_use_flow_rate(self):
        """Get peak_use_flow_rate

        Returns:
            float: the value of `peak_use_flow_rate` or None if not set
        """
        return self._data["Peak Use Flow Rate"]

    @peak_use_flow_rate.setter
    def peak_use_flow_rate(self, value=None):
        """  Corresponds to IDD Field `peak_use_flow_rate`
        Only used if Use Side Node connections are blank

        Args:
            value (float): value for IDD Field `peak_use_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `peak_use_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `peak_use_flow_rate`')

        self._data["Peak Use Flow Rate"] = value

    @property
    def use_flow_rate_fraction_schedule_name(self):
        """Get use_flow_rate_fraction_schedule_name

        Returns:
            str: the value of `use_flow_rate_fraction_schedule_name` or None if not set
        """
        return self._data["Use Flow Rate Fraction Schedule Name"]

    @use_flow_rate_fraction_schedule_name.setter
    def use_flow_rate_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `use_flow_rate_fraction_schedule_name`
        If blank, defaults to 1.0 at all times
        Only used if use side node connections are blank

        Args:
            value (str): value for IDD Field `use_flow_rate_fraction_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_flow_rate_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_flow_rate_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_flow_rate_fraction_schedule_name`')

        self._data["Use Flow Rate Fraction Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """Get cold_water_supply_temperature_schedule_name

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set
        """
        return self._data["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `cold_water_supply_temperature_schedule_name`
        Only used if use side node connections are blank
        Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `cold_water_supply_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cold_water_supply_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_water_supply_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cold_water_supply_temperature_schedule_name`')

        self._data["Cold Water Supply Temperature Schedule Name"] = value

    @property
    def use_side_inlet_node_name(self):
        """Get use_side_inlet_node_name

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set
        """
        return self._data["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_inlet_node_name`')

        self._data["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """Get use_side_outlet_node_name

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set
        """
        return self._data["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_outlet_node_name`')

        self._data["Use Side Outlet Node Name"] = value

    @property
    def use_side_effectiveness(self):
        """Get use_side_effectiveness

        Returns:
            float: the value of `use_side_effectiveness` or None if not set
        """
        return self._data["Use Side Effectiveness"]

    @use_side_effectiveness.setter
    def use_side_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `use_side_effectiveness`
        The use side effectiveness in the stratified tank model is a simplified analogy of
        a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        use mass flow rate that directly mixes with the tank fluid. And one minus the
        effectiveness is the fraction that bypasses the tank. The use side mass flow rate
        that bypasses the tank is mixed with the fluid or water leaving the stratified tank.

        Args:
            value (float): value for IDD Field `use_side_effectiveness`
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
                                 'for field `use_side_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `use_side_effectiveness`')

        self._data["Use Side Effectiveness"] = value

    @property
    def use_side_inlet_height(self):
        """Get use_side_inlet_height

        Returns:
            float: the value of `use_side_inlet_height` or None if not set
        """
        return self._data["Use Side Inlet Height"]

    @use_side_inlet_height.setter
    def use_side_inlet_height(self, value=0.0 ):
        """  Corresponds to IDD Field `use_side_inlet_height`
        Defaults to bottom of tank

        Args:
            value (float): value for IDD Field `use_side_inlet_height`
                Units: m
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
                                 'for field `use_side_inlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_inlet_height`')

        self._data["Use Side Inlet Height"] = value

    @property
    def use_side_outlet_height(self):
        """Get use_side_outlet_height

        Returns:
            float: the value of `use_side_outlet_height` or None if not set
        """
        return self._data["Use Side Outlet Height"]

    @use_side_outlet_height.setter
    def use_side_outlet_height(self, value=None):
        """  Corresponds to IDD Field `use_side_outlet_height`
        Defaults to top of tank

        Args:
            value (float): value for IDD Field `use_side_outlet_height`
                Units: m
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
                                 'for field `use_side_outlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_outlet_height`')

        self._data["Use Side Outlet Height"] = value

    @property
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def source_side_effectiveness(self):
        """Get source_side_effectiveness

        Returns:
            float: the value of `source_side_effectiveness` or None if not set
        """
        return self._data["Source Side Effectiveness"]

    @source_side_effectiveness.setter
    def source_side_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `source_side_effectiveness`
        The source side effectiveness in the stratified tank model is a simplified analogy of
        a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        source mass flow rate that directly mixes with the tank fluid. And one minus the
        effectiveness is the fraction that bypasses the tank. The source side mass flow rate
        that bypasses the tank is mixed with the fluid or water leaving the stratified tank.

        Args:
            value (float): value for IDD Field `source_side_effectiveness`
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
                                 'for field `source_side_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `source_side_effectiveness`')

        self._data["Source Side Effectiveness"] = value

    @property
    def source_side_inlet_height(self):
        """Get source_side_inlet_height

        Returns:
            float: the value of `source_side_inlet_height` or None if not set
        """
        return self._data["Source Side Inlet Height"]

    @source_side_inlet_height.setter
    def source_side_inlet_height(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_height`
        Defaults to top of tank

        Args:
            value (float): value for IDD Field `source_side_inlet_height`
                Units: m
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
                                 'for field `source_side_inlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_inlet_height`')

        self._data["Source Side Inlet Height"] = value

    @property
    def source_side_outlet_height(self):
        """Get source_side_outlet_height

        Returns:
            float: the value of `source_side_outlet_height` or None if not set
        """
        return self._data["Source Side Outlet Height"]

    @source_side_outlet_height.setter
    def source_side_outlet_height(self, value=0.0 ):
        """  Corresponds to IDD Field `source_side_outlet_height`
        Defaults to bottom of tank

        Args:
            value (float): value for IDD Field `source_side_outlet_height`
                Units: m
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
                                 'for field `source_side_outlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_outlet_height`')

        self._data["Source Side Outlet Height"] = value

    @property
    def inlet_mode(self):
        """Get inlet_mode

        Returns:
            str: the value of `inlet_mode` or None if not set
        """
        return self._data["Inlet Mode"]

    @inlet_mode.setter
    def inlet_mode(self, value="Fixed"):
        """  Corresponds to IDD Field `inlet_mode`

        Args:
            value (str): value for IDD Field `inlet_mode`
                Accepted values are:
                      - Fixed
                      - Seeking
                Default value: Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_mode`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["seeking"] = "Seeking"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `inlet_mode`'.format(value))
            value = vals[value_lower]

        self._data["Inlet Mode"] = value

    @property
    def use_side_design_flow_rate(self):
        """Get use_side_design_flow_rate

        Returns:
            float: the value of `use_side_design_flow_rate` or None if not set
        """
        return self._data["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `use_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `use_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `use_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_design_flow_rate`')

        self._data["Use Side Design Flow Rate"] = value

    @property
    def source_side_design_flow_rate(self):
        """Get source_side_design_flow_rate

        Returns:
            float: the value of `source_side_design_flow_rate` or None if not set
        """
        return self._data["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `source_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_design_flow_rate`')

        self._data["Source Side Design Flow Rate"] = value

    @property
    def indirect_water_heating_recovery_time(self):
        """Get indirect_water_heating_recovery_time

        Returns:
            float: the value of `indirect_water_heating_recovery_time` or None if not set
        """
        return self._data["Indirect Water Heating Recovery Time"]

    @indirect_water_heating_recovery_time.setter
    def indirect_water_heating_recovery_time(self, value=1.5 ):
        """  Corresponds to IDD Field `indirect_water_heating_recovery_time`
        Parameter for autosizing design flow rates for indirectly heated water tanks
        time required to raise temperature of entire tank from 14.4C to 57.2C

        Args:
            value (float): value for IDD Field `indirect_water_heating_recovery_time`
                Units: hr
                Default value: 1.5
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
                                 'for field `indirect_water_heating_recovery_time`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `indirect_water_heating_recovery_time`')

        self._data["Indirect Water Heating Recovery Time"] = value

    @property
    def number_of_nodes(self):
        """Get number_of_nodes

        Returns:
            int: the value of `number_of_nodes` or None if not set
        """
        return self._data["Number of Nodes"]

    @number_of_nodes.setter
    def number_of_nodes(self, value=1 ):
        """  Corresponds to IDD Field `number_of_nodes`

        Args:
            value (int): value for IDD Field `number_of_nodes`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_nodes`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_nodes`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `number_of_nodes`')

        self._data["Number of Nodes"] = value

    @property
    def additional_destratification_conductivity(self):
        """Get additional_destratification_conductivity

        Returns:
            float: the value of `additional_destratification_conductivity` or None if not set
        """
        return self._data["Additional Destratification Conductivity"]

    @additional_destratification_conductivity.setter
    def additional_destratification_conductivity(self, value=0.0 ):
        """  Corresponds to IDD Field `additional_destratification_conductivity`

        Args:
            value (float): value for IDD Field `additional_destratification_conductivity`
                Units: W/m-K
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
                                 'for field `additional_destratification_conductivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `additional_destratification_conductivity`')

        self._data["Additional Destratification Conductivity"] = value

    @property
    def node_1_additional_loss_coefficient(self):
        """Get node_1_additional_loss_coefficient

        Returns:
            float: the value of `node_1_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 1 Additional Loss Coefficient"]

    @node_1_additional_loss_coefficient.setter
    def node_1_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_1_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_1_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_1_additional_loss_coefficient`'.format(value))

        self._data["Node 1 Additional Loss Coefficient"] = value

    @property
    def node_2_additional_loss_coefficient(self):
        """Get node_2_additional_loss_coefficient

        Returns:
            float: the value of `node_2_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 2 Additional Loss Coefficient"]

    @node_2_additional_loss_coefficient.setter
    def node_2_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_2_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_2_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_2_additional_loss_coefficient`'.format(value))

        self._data["Node 2 Additional Loss Coefficient"] = value

    @property
    def node_3_additional_loss_coefficient(self):
        """Get node_3_additional_loss_coefficient

        Returns:
            float: the value of `node_3_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 3 Additional Loss Coefficient"]

    @node_3_additional_loss_coefficient.setter
    def node_3_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_3_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_3_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_3_additional_loss_coefficient`'.format(value))

        self._data["Node 3 Additional Loss Coefficient"] = value

    @property
    def node_4_additional_loss_coefficient(self):
        """Get node_4_additional_loss_coefficient

        Returns:
            float: the value of `node_4_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 4 Additional Loss Coefficient"]

    @node_4_additional_loss_coefficient.setter
    def node_4_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_4_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_4_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_4_additional_loss_coefficient`'.format(value))

        self._data["Node 4 Additional Loss Coefficient"] = value

    @property
    def node_5_additional_loss_coefficient(self):
        """Get node_5_additional_loss_coefficient

        Returns:
            float: the value of `node_5_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 5 Additional Loss Coefficient"]

    @node_5_additional_loss_coefficient.setter
    def node_5_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_5_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_5_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_5_additional_loss_coefficient`'.format(value))

        self._data["Node 5 Additional Loss Coefficient"] = value

    @property
    def node_6_additional_loss_coefficient(self):
        """Get node_6_additional_loss_coefficient

        Returns:
            float: the value of `node_6_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 6 Additional Loss Coefficient"]

    @node_6_additional_loss_coefficient.setter
    def node_6_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_6_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_6_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_6_additional_loss_coefficient`'.format(value))

        self._data["Node 6 Additional Loss Coefficient"] = value

    @property
    def node_7_additional_loss_coefficient(self):
        """Get node_7_additional_loss_coefficient

        Returns:
            float: the value of `node_7_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 7 Additional Loss Coefficient"]

    @node_7_additional_loss_coefficient.setter
    def node_7_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_7_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_7_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_7_additional_loss_coefficient`'.format(value))

        self._data["Node 7 Additional Loss Coefficient"] = value

    @property
    def node_8_additional_loss_coefficient(self):
        """Get node_8_additional_loss_coefficient

        Returns:
            float: the value of `node_8_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 8 Additional Loss Coefficient"]

    @node_8_additional_loss_coefficient.setter
    def node_8_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_8_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_8_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_8_additional_loss_coefficient`'.format(value))

        self._data["Node 8 Additional Loss Coefficient"] = value

    @property
    def node_9_additional_loss_coefficient(self):
        """Get node_9_additional_loss_coefficient

        Returns:
            float: the value of `node_9_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 9 Additional Loss Coefficient"]

    @node_9_additional_loss_coefficient.setter
    def node_9_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_9_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_9_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_9_additional_loss_coefficient`'.format(value))

        self._data["Node 9 Additional Loss Coefficient"] = value

    @property
    def node_10_additional_loss_coefficient(self):
        """Get node_10_additional_loss_coefficient

        Returns:
            float: the value of `node_10_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 10 Additional Loss Coefficient"]

    @node_10_additional_loss_coefficient.setter
    def node_10_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_10_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_10_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_10_additional_loss_coefficient`'.format(value))

        self._data["Node 10 Additional Loss Coefficient"] = value

    @property
    def source_side_flow_control_mode(self):
        """Get source_side_flow_control_mode

        Returns:
            str: the value of `source_side_flow_control_mode` or None if not set
        """
        return self._data["Source Side Flow Control Mode"]

    @source_side_flow_control_mode.setter
    def source_side_flow_control_mode(self, value="IndirectHeatPrimarySetpoint"):
        """  Corresponds to IDD Field `source_side_flow_control_mode`
        StorageTank mode always requests flow unless tank is at its Maximum Temperature Limit
        IndirectHeatPrimarySetpoint mode requests flow whenever primary setpoint for heater 1 calls for heat
        IndirectHeatAlternateSetpoint mode requests flow whenever alternate indirect setpoint calls for heat

        Args:
            value (str): value for IDD Field `source_side_flow_control_mode`
                Accepted values are:
                      - StorageTank
                      - IndirectHeatPrimarySetpoint
                      - IndirectHeatAlternateSetpoint
                Default value: IndirectHeatPrimarySetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_flow_control_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_flow_control_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_flow_control_mode`')
            vals = {}
            vals["storagetank"] = "StorageTank"
            vals["indirectheatprimarysetpoint"] = "IndirectHeatPrimarySetpoint"
            vals["indirectheatalternatesetpoint"] = "IndirectHeatAlternateSetpoint"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `source_side_flow_control_mode`'.format(value))
            value = vals[value_lower]

        self._data["Source Side Flow Control Mode"] = value

    @property
    def indirect_alternate_setpoint_temperature_schedule_name(self):
        """Get indirect_alternate_setpoint_temperature_schedule_name

        Returns:
            str: the value of `indirect_alternate_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Indirect Alternate Setpoint Temperature Schedule Name"]

    @indirect_alternate_setpoint_temperature_schedule_name.setter
    def indirect_alternate_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `indirect_alternate_setpoint_temperature_schedule_name`
        This field is only used if the previous is set to IndirectHeatAlternateSetpoint

        Args:
            value (str): value for IDD Field `indirect_alternate_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `indirect_alternate_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `indirect_alternate_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `indirect_alternate_setpoint_temperature_schedule_name`')

        self._data["Indirect Alternate Setpoint Temperature Schedule Name"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class WaterHeaterSizing(object):
    """ Corresponds to IDD object `WaterHeater:Sizing`
        This input object is used with WaterHeater:Mixed or
        with WaterHeater:Stratified to autosize tank volume and heater capacity
        This object is not needed if water heaters are not autosized.
    
    """
    internal_name = "WaterHeater:Sizing"
    field_count = 16
    required_fields = ["WaterHeater Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterHeater:Sizing`
        """
        self._data = OrderedDict()
        self._data["WaterHeater Name"] = None
        self._data["Design Mode"] = None
        self._data["Time Storage Can Meet Peak Draw"] = None
        self._data["Time for Tank Recovery"] = None
        self._data["Nominal Tank Volume for Autosizing Plant Connections"] = None
        self._data["Number of Bedrooms"] = None
        self._data["Number of Bathrooms"] = None
        self._data["Storage Capacity per Person"] = None
        self._data["Recovery Capacity per Person"] = None
        self._data["Storage Capacity per Floor Area"] = None
        self._data["Recovery Capacity per Floor Area"] = None
        self._data["Number of Units"] = None
        self._data["Storage Capacity per Unit"] = None
        self._data["Recovery Capacity PerUnit"] = None
        self._data["Storage Capacity per Collector Area"] = None
        self._data["Height Aspect Ratio"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.waterheater_name = None
        else:
            self.waterheater_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_mode = None
        else:
            self.design_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.time_storage_can_meet_peak_draw = None
        else:
            self.time_storage_can_meet_peak_draw = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.time_for_tank_recovery = None
        else:
            self.time_for_tank_recovery = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_tank_volume_for_autosizing_plant_connections = None
        else:
            self.nominal_tank_volume_for_autosizing_plant_connections = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_bedrooms = None
        else:
            self.number_of_bedrooms = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_bathrooms = None
        else:
            self.number_of_bathrooms = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.storage_capacity_per_person = None
        else:
            self.storage_capacity_per_person = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recovery_capacity_per_person = None
        else:
            self.recovery_capacity_per_person = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.storage_capacity_per_floor_area = None
        else:
            self.storage_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recovery_capacity_per_floor_area = None
        else:
            self.recovery_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_units = None
        else:
            self.number_of_units = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.storage_capacity_per_unit = None
        else:
            self.storage_capacity_per_unit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recovery_capacity_perunit = None
        else:
            self.recovery_capacity_perunit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.storage_capacity_per_collector_area = None
        else:
            self.storage_capacity_per_collector_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_aspect_ratio = None
        else:
            self.height_aspect_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def waterheater_name(self):
        """Get waterheater_name

        Returns:
            str: the value of `waterheater_name` or None if not set
        """
        return self._data["WaterHeater Name"]

    @waterheater_name.setter
    def waterheater_name(self, value=None):
        """  Corresponds to IDD Field `waterheater_name`

        Args:
            value (str): value for IDD Field `waterheater_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `waterheater_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `waterheater_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `waterheater_name`')

        self._data["WaterHeater Name"] = value

    @property
    def design_mode(self):
        """Get design_mode

        Returns:
            str: the value of `design_mode` or None if not set
        """
        return self._data["Design Mode"]

    @design_mode.setter
    def design_mode(self, value=None):
        """  Corresponds to IDD Field `design_mode`

        Args:
            value (str): value for IDD Field `design_mode`
                Accepted values are:
                      - PeakDraw
                      - ResidentialHUD-FHAMinimum
                      - PerPerson
                      - PerFloorArea
                      - PerUnit
                      - PerSolarCollectorArea
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_mode`')
            vals = {}
            vals["peakdraw"] = "PeakDraw"
            vals["residentialhud-fhaminimum"] = "ResidentialHUD-FHAMinimum"
            vals["perperson"] = "PerPerson"
            vals["perfloorarea"] = "PerFloorArea"
            vals["perunit"] = "PerUnit"
            vals["persolarcollectorarea"] = "PerSolarCollectorArea"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `design_mode`'.format(value))
            value = vals[value_lower]

        self._data["Design Mode"] = value

    @property
    def time_storage_can_meet_peak_draw(self):
        """Get time_storage_can_meet_peak_draw

        Returns:
            float: the value of `time_storage_can_meet_peak_draw` or None if not set
        """
        return self._data["Time Storage Can Meet Peak Draw"]

    @time_storage_can_meet_peak_draw.setter
    def time_storage_can_meet_peak_draw(self, value=None):
        """  Corresponds to IDD Field `time_storage_can_meet_peak_draw`
        Only used for Design Mode = PeakDraw

        Args:
            value (float): value for IDD Field `time_storage_can_meet_peak_draw`
                Units: hr
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
                                 'for field `time_storage_can_meet_peak_draw`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `time_storage_can_meet_peak_draw`')

        self._data["Time Storage Can Meet Peak Draw"] = value

    @property
    def time_for_tank_recovery(self):
        """Get time_for_tank_recovery

        Returns:
            float: the value of `time_for_tank_recovery` or None if not set
        """
        return self._data["Time for Tank Recovery"]

    @time_for_tank_recovery.setter
    def time_for_tank_recovery(self, value=None):
        """  Corresponds to IDD Field `time_for_tank_recovery`
        Only used for Design Mode = PeakDraw

        Args:
            value (float): value for IDD Field `time_for_tank_recovery`
                Units: hr
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
                                 'for field `time_for_tank_recovery`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `time_for_tank_recovery`')

        self._data["Time for Tank Recovery"] = value

    @property
    def nominal_tank_volume_for_autosizing_plant_connections(self):
        """Get nominal_tank_volume_for_autosizing_plant_connections

        Returns:
            float: the value of `nominal_tank_volume_for_autosizing_plant_connections` or None if not set
        """
        return self._data["Nominal Tank Volume for Autosizing Plant Connections"]

    @nominal_tank_volume_for_autosizing_plant_connections.setter
    def nominal_tank_volume_for_autosizing_plant_connections(self, value=None):
        """  Corresponds to IDD Field `nominal_tank_volume_for_autosizing_plant_connections`
        Only used if Design Mode = PeakDraw and the water heater also
        has autosized flow rates for connections on the demand side of a plant loop

        Args:
            value (float): value for IDD Field `nominal_tank_volume_for_autosizing_plant_connections`
                Units: m3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_tank_volume_for_autosizing_plant_connections`'.format(value))

        self._data["Nominal Tank Volume for Autosizing Plant Connections"] = value

    @property
    def number_of_bedrooms(self):
        """Get number_of_bedrooms

        Returns:
            int: the value of `number_of_bedrooms` or None if not set
        """
        return self._data["Number of Bedrooms"]

    @number_of_bedrooms.setter
    def number_of_bedrooms(self, value=None):
        """  Corresponds to IDD Field `number_of_bedrooms`
        Only used for Design Mode = ResidentialHUD-FHAMinimum

        Args:
            value (int): value for IDD Field `number_of_bedrooms`
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
                                 'for field `number_of_bedrooms`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_bedrooms`')

        self._data["Number of Bedrooms"] = value

    @property
    def number_of_bathrooms(self):
        """Get number_of_bathrooms

        Returns:
            int: the value of `number_of_bathrooms` or None if not set
        """
        return self._data["Number of Bathrooms"]

    @number_of_bathrooms.setter
    def number_of_bathrooms(self, value=None):
        """  Corresponds to IDD Field `number_of_bathrooms`
        Only used for Design Mode = ResidentialHUD-FHAMinimum

        Args:
            value (int): value for IDD Field `number_of_bathrooms`
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
                                 'for field `number_of_bathrooms`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_bathrooms`')

        self._data["Number of Bathrooms"] = value

    @property
    def storage_capacity_per_person(self):
        """Get storage_capacity_per_person

        Returns:
            float: the value of `storage_capacity_per_person` or None if not set
        """
        return self._data["Storage Capacity per Person"]

    @storage_capacity_per_person.setter
    def storage_capacity_per_person(self, value=None):
        """  Corresponds to IDD Field `storage_capacity_per_person`
        Only used for Design Mode = PerPerson

        Args:
            value (float): value for IDD Field `storage_capacity_per_person`
                Units: m3/Person
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
                                 'for field `storage_capacity_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `storage_capacity_per_person`')

        self._data["Storage Capacity per Person"] = value

    @property
    def recovery_capacity_per_person(self):
        """Get recovery_capacity_per_person

        Returns:
            float: the value of `recovery_capacity_per_person` or None if not set
        """
        return self._data["Recovery Capacity per Person"]

    @recovery_capacity_per_person.setter
    def recovery_capacity_per_person(self, value=None):
        """  Corresponds to IDD Field `recovery_capacity_per_person`
        Only used for Design Mode = PerPerson

        Args:
            value (float): value for IDD Field `recovery_capacity_per_person`
                Units: m3/hr-person
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
                                 'for field `recovery_capacity_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `recovery_capacity_per_person`')

        self._data["Recovery Capacity per Person"] = value

    @property
    def storage_capacity_per_floor_area(self):
        """Get storage_capacity_per_floor_area

        Returns:
            float: the value of `storage_capacity_per_floor_area` or None if not set
        """
        return self._data["Storage Capacity per Floor Area"]

    @storage_capacity_per_floor_area.setter
    def storage_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `storage_capacity_per_floor_area`
        Only used for Design Mode = PerFloorArea

        Args:
            value (float): value for IDD Field `storage_capacity_per_floor_area`
                Units: m3/m2
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
                                 'for field `storage_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `storage_capacity_per_floor_area`')

        self._data["Storage Capacity per Floor Area"] = value

    @property
    def recovery_capacity_per_floor_area(self):
        """Get recovery_capacity_per_floor_area

        Returns:
            float: the value of `recovery_capacity_per_floor_area` or None if not set
        """
        return self._data["Recovery Capacity per Floor Area"]

    @recovery_capacity_per_floor_area.setter
    def recovery_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `recovery_capacity_per_floor_area`
        Only used for Design Mode = PerFloorArea

        Args:
            value (float): value for IDD Field `recovery_capacity_per_floor_area`
                Units: m3/hr-m2
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
                                 'for field `recovery_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `recovery_capacity_per_floor_area`')

        self._data["Recovery Capacity per Floor Area"] = value

    @property
    def number_of_units(self):
        """Get number_of_units

        Returns:
            float: the value of `number_of_units` or None if not set
        """
        return self._data["Number of Units"]

    @number_of_units.setter
    def number_of_units(self, value=None):
        """  Corresponds to IDD Field `number_of_units`
        Only used for Design Mode = PerUnit

        Args:
            value (float): value for IDD Field `number_of_units`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_units`'.format(value))

        self._data["Number of Units"] = value

    @property
    def storage_capacity_per_unit(self):
        """Get storage_capacity_per_unit

        Returns:
            float: the value of `storage_capacity_per_unit` or None if not set
        """
        return self._data["Storage Capacity per Unit"]

    @storage_capacity_per_unit.setter
    def storage_capacity_per_unit(self, value=None):
        """  Corresponds to IDD Field `storage_capacity_per_unit`
        Only used for Design Mode = PerUnit

        Args:
            value (float): value for IDD Field `storage_capacity_per_unit`
                Units: m3
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
                                 'for field `storage_capacity_per_unit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `storage_capacity_per_unit`')

        self._data["Storage Capacity per Unit"] = value

    @property
    def recovery_capacity_perunit(self):
        """Get recovery_capacity_perunit

        Returns:
            float: the value of `recovery_capacity_perunit` or None if not set
        """
        return self._data["Recovery Capacity PerUnit"]

    @recovery_capacity_perunit.setter
    def recovery_capacity_perunit(self, value=None):
        """  Corresponds to IDD Field `recovery_capacity_perunit`
        Only used for Design Mode = PerUnit

        Args:
            value (float): value for IDD Field `recovery_capacity_perunit`
                Units: m3/hr
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
                                 'for field `recovery_capacity_perunit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `recovery_capacity_perunit`')

        self._data["Recovery Capacity PerUnit"] = value

    @property
    def storage_capacity_per_collector_area(self):
        """Get storage_capacity_per_collector_area

        Returns:
            float: the value of `storage_capacity_per_collector_area` or None if not set
        """
        return self._data["Storage Capacity per Collector Area"]

    @storage_capacity_per_collector_area.setter
    def storage_capacity_per_collector_area(self, value=None):
        """  Corresponds to IDD Field `storage_capacity_per_collector_area`
        Only used for Design Mode = PerSolarCollectorArea

        Args:
            value (float): value for IDD Field `storage_capacity_per_collector_area`
                Units: m3/m2
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
                                 'for field `storage_capacity_per_collector_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `storage_capacity_per_collector_area`')

        self._data["Storage Capacity per Collector Area"] = value

    @property
    def height_aspect_ratio(self):
        """Get height_aspect_ratio

        Returns:
            float: the value of `height_aspect_ratio` or None if not set
        """
        return self._data["Height Aspect Ratio"]

    @height_aspect_ratio.setter
    def height_aspect_ratio(self, value=None):
        """  Corresponds to IDD Field `height_aspect_ratio`
        only used if for WaterHeater:Stratified

        Args:
            value (float): value for IDD Field `height_aspect_ratio`
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
                                 'for field `height_aspect_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `height_aspect_ratio`')

        self._data["Height Aspect Ratio"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class WaterHeaterHeatPump(object):
    """ Corresponds to IDD object `WaterHeater:HeatPump`
        This object models an air-source heat pump for water heating.
        WaterHeater:HeatPump is a compound object that references other component objects -
        Coil:WaterHeating:AirToWaterHeatPump, Fan:OnOff, WaterHeater:Mixed
    
    """
    internal_name = "WaterHeater:HeatPump"
    field_count = 35
    required_fields = ["Name", "Compressor Setpoint Temperature Schedule Name", "Condenser Water Inlet Node Name", "Condenser Water Outlet Node Name", "Inlet Air Configuration", "Tank Object Type", "Tank Name", "DX Coil Object Type", "DX Coil Name", "Compressor Location", "Fan Object Type", "Fan Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterHeater:HeatPump`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Compressor Setpoint Temperature Schedule Name"] = None
        self._data["Dead Band Temperature Difference"] = None
        self._data["Condenser Water Inlet Node Name"] = None
        self._data["Condenser Water Outlet Node Name"] = None
        self._data["Condenser Water Flow Rate"] = None
        self._data["Evaporator Air Flow Rate"] = None
        self._data["Inlet Air Configuration"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Node Name"] = None
        self._data["Exhaust Air Node Name"] = None
        self._data["Inlet Air Temperature Schedule Name"] = None
        self._data["Inlet Air Humidity Schedule Name"] = None
        self._data["Inlet Air Zone Name"] = None
        self._data["Tank Object Type"] = None
        self._data["Tank Name"] = None
        self._data["Tank Use Side Inlet Node Name"] = None
        self._data["Tank Use Side Outlet Node Name"] = None
        self._data["DX Coil Object Type"] = None
        self._data["DX Coil Name"] = None
        self._data["Minimum Inlet Air Temperature for Compressor Operation"] = None
        self._data["Compressor Location"] = None
        self._data["Compressor Ambient Temperature Schedule Name"] = None
        self._data["Fan Object Type"] = None
        self._data["Fan Name"] = None
        self._data["Fan Placement"] = None
        self._data["On Cycle Parasitic Electric Load"] = None
        self._data["Off Cycle Parasitic Electric Load"] = None
        self._data["Parasitic Heat Rejection Location"] = None
        self._data["Inlet Air Mixer Node Name"] = None
        self._data["Outlet Air Splitter Node Name"] = None
        self._data["Inlet Air Mixer Schedule Name"] = None
        self._data["Control Sensor Location In Stratified Tank"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compressor_setpoint_temperature_schedule_name = None
        else:
            self.compressor_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dead_band_temperature_difference = None
        else:
            self.dead_band_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_water_inlet_node_name = None
        else:
            self.condenser_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_water_outlet_node_name = None
        else:
            self.condenser_water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_water_flow_rate = None
        else:
            self.condenser_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporator_air_flow_rate = None
        else:
            self.evaporator_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_air_configuration = None
        else:
            self.inlet_air_configuration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_node_name = None
        else:
            self.outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_node_name = None
        else:
            self.exhaust_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_air_temperature_schedule_name = None
        else:
            self.inlet_air_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_air_humidity_schedule_name = None
        else:
            self.inlet_air_humidity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_air_zone_name = None
        else:
            self.inlet_air_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_object_type = None
        else:
            self.tank_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_name = None
        else:
            self.tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_use_side_inlet_node_name = None
        else:
            self.tank_use_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_use_side_outlet_node_name = None
        else:
            self.tank_use_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dx_coil_object_type = None
        else:
            self.dx_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dx_coil_name = None
        else:
            self.dx_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_inlet_air_temperature_for_compressor_operation = None
        else:
            self.minimum_inlet_air_temperature_for_compressor_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compressor_location = None
        else:
            self.compressor_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compressor_ambient_temperature_schedule_name = None
        else:
            self.compressor_ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_object_type = None
        else:
            self.fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.on_cycle_parasitic_electric_load = None
        else:
            self.on_cycle_parasitic_electric_load = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.off_cycle_parasitic_electric_load = None
        else:
            self.off_cycle_parasitic_electric_load = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parasitic_heat_rejection_location = None
        else:
            self.parasitic_heat_rejection_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_air_mixer_node_name = None
        else:
            self.inlet_air_mixer_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_air_splitter_node_name = None
        else:
            self.outlet_air_splitter_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_air_mixer_schedule_name = None
        else:
            self.inlet_air_mixer_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_sensor_location_in_stratified_tank = None
        else:
            self.control_sensor_location_in_stratified_tank = vals[i]
        i += 1
        if i >= len(vals):
            return

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
        Unique name for this instance of a heat pump water heater.

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.
        Schedule values of 0 denote the heat pump compressor is off and the parasitic electric
        energy is also off.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def compressor_setpoint_temperature_schedule_name(self):
        """Get compressor_setpoint_temperature_schedule_name

        Returns:
            str: the value of `compressor_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Compressor Setpoint Temperature Schedule Name"]

    @compressor_setpoint_temperature_schedule_name.setter
    def compressor_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `compressor_setpoint_temperature_schedule_name`
        Defines the cut-out temperature where the heat pump compressor turns off.
        The heat pump compressor setpoint temperature should always be greater
        than the water tank's heater (element or burner) setpoint temperature.

        Args:
            value (str): value for IDD Field `compressor_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `compressor_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compressor_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `compressor_setpoint_temperature_schedule_name`')

        self._data["Compressor Setpoint Temperature Schedule Name"] = value

    @property
    def dead_band_temperature_difference(self):
        """Get dead_band_temperature_difference

        Returns:
            float: the value of `dead_band_temperature_difference` or None if not set
        """
        return self._data["Dead Band Temperature Difference"]

    @dead_band_temperature_difference.setter
    def dead_band_temperature_difference(self, value=5.0 ):
        """  Corresponds to IDD Field `dead_band_temperature_difference`
        Setpoint temperature minus the dead band temperature difference defines
        the cut-in temperature where the heat pump compressor turns on.
        The water tank's heater (element or burner) setpoint temperature
        should always be less than the heat pump compressor cut-in temperature.

        Args:
            value (float): value for IDD Field `dead_band_temperature_difference`
                Units: deltaC
                Default value: 5.0
                value > 0.0
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
                                 'for field `dead_band_temperature_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dead_band_temperature_difference`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `dead_band_temperature_difference`')

        self._data["Dead Band Temperature Difference"] = value

    @property
    def condenser_water_inlet_node_name(self):
        """Get condenser_water_inlet_node_name

        Returns:
            str: the value of `condenser_water_inlet_node_name` or None if not set
        """
        return self._data["Condenser Water Inlet Node Name"]

    @condenser_water_inlet_node_name.setter
    def condenser_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_water_inlet_node_name`
        Should match the field Source Outlet Node Name in the water heater tank object.
        Should also match the Condenser Water Inlet Node Name in the associated
        DX coil object.

        Args:
            value (str): value for IDD Field `condenser_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_water_inlet_node_name`')

        self._data["Condenser Water Inlet Node Name"] = value

    @property
    def condenser_water_outlet_node_name(self):
        """Get condenser_water_outlet_node_name

        Returns:
            str: the value of `condenser_water_outlet_node_name` or None if not set
        """
        return self._data["Condenser Water Outlet Node Name"]

    @condenser_water_outlet_node_name.setter
    def condenser_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_water_outlet_node_name`
        Should match the field Source Inlet Node Name in water heater tank object.
        Should also match the Condenser Water Outlet Node Name in the associated
        DX Coil object.

        Args:
            value (str): value for IDD Field `condenser_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_water_outlet_node_name`')

        self._data["Condenser Water Outlet Node Name"] = value

    @property
    def condenser_water_flow_rate(self):
        """Get condenser_water_flow_rate

        Returns:
            float: the value of `condenser_water_flow_rate` or None if not set
        """
        return self._data["Condenser Water Flow Rate"]

    @condenser_water_flow_rate.setter
    def condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `condenser_water_flow_rate`
        Actual water flow rate through the heat pump's water coil (condenser).
        If autocalculated, the water flow rate is set equal to 4.487E-8 m3/s/W times
        the rated heating capacity of the heat pump's DX coil.

        Args:
            value (float): value for IDD Field `condenser_water_flow_rate`
                Units: m3/s
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
                                 'for field `condenser_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `condenser_water_flow_rate`')

        self._data["Condenser Water Flow Rate"] = value

    @property
    def evaporator_air_flow_rate(self):
        """Get evaporator_air_flow_rate

        Returns:
            float: the value of `evaporator_air_flow_rate` or None if not set
        """
        return self._data["Evaporator Air Flow Rate"]

    @evaporator_air_flow_rate.setter
    def evaporator_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `evaporator_air_flow_rate`
        Actual air flow rate across the heat pump's air coil (evaporator).
        If autocalculated, the air flow rate is set equal to 5.035E-5 m3/s/W times
        the rated heating capacity of the heat pump's DX coil.

        Args:
            value (float): value for IDD Field `evaporator_air_flow_rate`
                Units: m3/s
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
                                 'for field `evaporator_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `evaporator_air_flow_rate`')

        self._data["Evaporator Air Flow Rate"] = value

    @property
    def inlet_air_configuration(self):
        """Get inlet_air_configuration

        Returns:
            str: the value of `inlet_air_configuration` or None if not set
        """
        return self._data["Inlet Air Configuration"]

    @inlet_air_configuration.setter
    def inlet_air_configuration(self, value=None):
        """  Corresponds to IDD Field `inlet_air_configuration`
        Defines the configuration of the airflow path through the air coil and fan section.

        Args:
            value (str): value for IDD Field `inlet_air_configuration`
                Accepted values are:
                      - Schedule
                      - ZoneAirOnly
                      - OutdoorAirOnly
                      - ZoneAndOutdoorAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_air_configuration`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_air_configuration`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_air_configuration`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["zoneaironly"] = "ZoneAirOnly"
            vals["outdooraironly"] = "OutdoorAirOnly"
            vals["zoneandoutdoorair"] = "ZoneAndOutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `inlet_air_configuration`'.format(value))
            value = vals[value_lower]

        self._data["Inlet Air Configuration"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_inlet_node_name`
        Zone air exhaust node name if Inlet Air Configuration is ZoneAirOnly or
        ZoneAndOutdoorAir.
        Simply a unique Node Name if Inlet Air Configuration is Schedule.
        Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')

        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`
        Zone Air Inlet Node Name if Inlet Air Configuration is ZoneAirOnly or
        ZoneAndOutdoorAir.
        Simply a unique Node Name if Inlet Air Configuration is Schedule.
        Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def outdoor_air_node_name(self):
        """Get outdoor_air_node_name

        Returns:
            str: the value of `outdoor_air_node_name` or None if not set
        """
        return self._data["Outdoor Air Node Name"]

    @outdoor_air_node_name.setter
    def outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_node_name`
        Outdoor air node name if inlet air configuration is ZoneAndOutdoorAir
        or OutdoorAirOnly, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `outdoor_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_node_name`')

        self._data["Outdoor Air Node Name"] = value

    @property
    def exhaust_air_node_name(self):
        """Get exhaust_air_node_name

        Returns:
            str: the value of `exhaust_air_node_name` or None if not set
        """
        return self._data["Exhaust Air Node Name"]

    @exhaust_air_node_name.setter
    def exhaust_air_node_name(self, value=None):
        """  Corresponds to IDD Field `exhaust_air_node_name`
        Simply a unique Node Name if Inlet Air Configuration is ZoneAndOutdoorAir
        or OutdoorAirOnly, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `exhaust_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exhaust_air_node_name`')

        self._data["Exhaust Air Node Name"] = value

    @property
    def inlet_air_temperature_schedule_name(self):
        """Get inlet_air_temperature_schedule_name

        Returns:
            str: the value of `inlet_air_temperature_schedule_name` or None if not set
        """
        return self._data["Inlet Air Temperature Schedule Name"]

    @inlet_air_temperature_schedule_name.setter
    def inlet_air_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `inlet_air_temperature_schedule_name`
        Used only if Inlet Air Configuration is Schedule, otherwise leave blank.
        Schedule values should be degrees C.

        Args:
            value (str): value for IDD Field `inlet_air_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_air_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_air_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_air_temperature_schedule_name`')

        self._data["Inlet Air Temperature Schedule Name"] = value

    @property
    def inlet_air_humidity_schedule_name(self):
        """Get inlet_air_humidity_schedule_name

        Returns:
            str: the value of `inlet_air_humidity_schedule_name` or None if not set
        """
        return self._data["Inlet Air Humidity Schedule Name"]

    @inlet_air_humidity_schedule_name.setter
    def inlet_air_humidity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `inlet_air_humidity_schedule_name`
        Used only if Inlet Air Configuration is Schedule, otherwise leave blank.
        Schedule values are entered as a fraction (e.g. 0.5 is equal to 50%RH)

        Args:
            value (str): value for IDD Field `inlet_air_humidity_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_air_humidity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_air_humidity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_air_humidity_schedule_name`')

        self._data["Inlet Air Humidity Schedule Name"] = value

    @property
    def inlet_air_zone_name(self):
        """Get inlet_air_zone_name

        Returns:
            str: the value of `inlet_air_zone_name` or None if not set
        """
        return self._data["Inlet Air Zone Name"]

    @inlet_air_zone_name.setter
    def inlet_air_zone_name(self, value=None):
        """  Corresponds to IDD Field `inlet_air_zone_name`
        Used only if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir.
        Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `inlet_air_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_air_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_air_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_air_zone_name`')

        self._data["Inlet Air Zone Name"] = value

    @property
    def tank_object_type(self):
        """Get tank_object_type

        Returns:
            str: the value of `tank_object_type` or None if not set
        """
        return self._data["Tank Object Type"]

    @tank_object_type.setter
    def tank_object_type(self, value="WaterHeater:Mixed"):
        """  Corresponds to IDD Field `tank_object_type`
        Specify the type of water heater tank used by this heat pump water heater.

        Args:
            value (str): value for IDD Field `tank_object_type`
                Accepted values are:
                      - WaterHeater:Mixed
                      - WaterHeater:Stratified
                Default value: WaterHeater:Mixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `tank_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `tank_object_type`')
            vals = {}
            vals["waterheater:mixed"] = "WaterHeater:Mixed"
            vals["waterheater:stratified"] = "WaterHeater:Stratified"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `tank_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Tank Object Type"] = value

    @property
    def tank_name(self):
        """Get tank_name

        Returns:
            str: the value of `tank_name` or None if not set
        """
        return self._data["Tank Name"]

    @tank_name.setter
    def tank_name(self, value=None):
        """  Corresponds to IDD Field `tank_name`
        Needs to match the name used in the corresponding Water Heater object.

        Args:
            value (str): value for IDD Field `tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `tank_name`')

        self._data["Tank Name"] = value

    @property
    def tank_use_side_inlet_node_name(self):
        """Get tank_use_side_inlet_node_name

        Returns:
            str: the value of `tank_use_side_inlet_node_name` or None if not set
        """
        return self._data["Tank Use Side Inlet Node Name"]

    @tank_use_side_inlet_node_name.setter
    def tank_use_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `tank_use_side_inlet_node_name`
        Used only when the heat pump water heater is connected to a plant loop,
        otherwise leave blank. Needs to match the name used in the corresponding
        Water Heater object when connected to a plant loop.

        Args:
            value (str): value for IDD Field `tank_use_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `tank_use_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_use_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `tank_use_side_inlet_node_name`')

        self._data["Tank Use Side Inlet Node Name"] = value

    @property
    def tank_use_side_outlet_node_name(self):
        """Get tank_use_side_outlet_node_name

        Returns:
            str: the value of `tank_use_side_outlet_node_name` or None if not set
        """
        return self._data["Tank Use Side Outlet Node Name"]

    @tank_use_side_outlet_node_name.setter
    def tank_use_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `tank_use_side_outlet_node_name`
        Used only when the heat pump water heater is connected to a plant loop,
        otherwise leave blank. Needs to match the name used in the corresponding
        Water Heater object when connected to a plant loop.

        Args:
            value (str): value for IDD Field `tank_use_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `tank_use_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_use_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `tank_use_side_outlet_node_name`')

        self._data["Tank Use Side Outlet Node Name"] = value

    @property
    def dx_coil_object_type(self):
        """Get dx_coil_object_type

        Returns:
            str: the value of `dx_coil_object_type` or None if not set
        """
        return self._data["DX Coil Object Type"]

    @dx_coil_object_type.setter
    def dx_coil_object_type(self, value="Coil:WaterHeating:AirToWaterHeatPump"):
        """  Corresponds to IDD Field `dx_coil_object_type`
        Specify the type of DX coil used by this heat pump water heater. The only
        valid choice is Coil:WaterHeating:AirToWaterHeatPump.

        Args:
            value (str): value for IDD Field `dx_coil_object_type`
                Accepted values are:
                      - Coil:WaterHeating:AirToWaterHeatPump
                Default value: Coil:WaterHeating:AirToWaterHeatPump
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dx_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dx_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dx_coil_object_type`')
            vals = {}
            vals["coil:waterheating:airtowaterheatpump"] = "Coil:WaterHeating:AirToWaterHeatPump"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `dx_coil_object_type`'.format(value))
            value = vals[value_lower]

        self._data["DX Coil Object Type"] = value

    @property
    def dx_coil_name(self):
        """Get dx_coil_name

        Returns:
            str: the value of `dx_coil_name` or None if not set
        """
        return self._data["DX Coil Name"]

    @dx_coil_name.setter
    def dx_coil_name(self, value=None):
        """  Corresponds to IDD Field `dx_coil_name`
        Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump object.

        Args:
            value (str): value for IDD Field `dx_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dx_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dx_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dx_coil_name`')

        self._data["DX Coil Name"] = value

    @property
    def minimum_inlet_air_temperature_for_compressor_operation(self):
        """Get minimum_inlet_air_temperature_for_compressor_operation

        Returns:
            float: the value of `minimum_inlet_air_temperature_for_compressor_operation` or None if not set
        """
        return self._data["Minimum Inlet Air Temperature for Compressor Operation"]

    @minimum_inlet_air_temperature_for_compressor_operation.setter
    def minimum_inlet_air_temperature_for_compressor_operation(self, value=10.0 ):
        """  Corresponds to IDD Field `minimum_inlet_air_temperature_for_compressor_operation`
        Heat pump compressor will not operate when the inlet air dry-bulb temperature
        is below this value.

        Args:
            value (float): value for IDD Field `minimum_inlet_air_temperature_for_compressor_operation`
                Units: C
                Default value: 10.0
                value >= 5.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_inlet_air_temperature_for_compressor_operation`'.format(value))
            if value < 5.0:
                raise ValueError('value need to be greater or equal 5.0 '
                                 'for field `minimum_inlet_air_temperature_for_compressor_operation`')

        self._data["Minimum Inlet Air Temperature for Compressor Operation"] = value

    @property
    def compressor_location(self):
        """Get compressor_location

        Returns:
            str: the value of `compressor_location` or None if not set
        """
        return self._data["Compressor Location"]

    @compressor_location.setter
    def compressor_location(self, value=None):
        """  Corresponds to IDD Field `compressor_location`
        If Zone is selected, Inlet Air Configuration must be ZoneAirOnly or
        ZoneAndOutdoorAir. If Schedule is selected, then you must provide a
        Compressor Ambient Temperature Schedule Name below.

        Args:
            value (str): value for IDD Field `compressor_location`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `compressor_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compressor_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `compressor_location`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `compressor_location`'.format(value))
            value = vals[value_lower]

        self._data["Compressor Location"] = value

    @property
    def compressor_ambient_temperature_schedule_name(self):
        """Get compressor_ambient_temperature_schedule_name

        Returns:
            str: the value of `compressor_ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Compressor Ambient Temperature Schedule Name"]

    @compressor_ambient_temperature_schedule_name.setter
    def compressor_ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `compressor_ambient_temperature_schedule_name`
        Used only if Compressor Location is Schedule, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `compressor_ambient_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `compressor_ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compressor_ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `compressor_ambient_temperature_schedule_name`')

        self._data["Compressor Ambient Temperature Schedule Name"] = value

    @property
    def fan_object_type(self):
        """Get fan_object_type

        Returns:
            str: the value of `fan_object_type` or None if not set
        """
        return self._data["Fan Object Type"]

    @fan_object_type.setter
    def fan_object_type(self, value="Fan:OnOff"):
        """  Corresponds to IDD Field `fan_object_type`
        Specify the type of fan used by this heat pump water heater. The only
        valid choice is Fan:OnOff.

        Args:
            value (str): value for IDD Field `fan_object_type`
                Accepted values are:
                      - Fan:OnOff
                Default value: Fan:OnOff
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `fan_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Fan Object Type"] = value

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `fan_name`
        Needs to match the name used in the corresponding Fan:OnOff object.

        Args:
            value (str): value for IDD Field `fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_name`')

        self._data["Fan Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="DrawThrough"):
        """  Corresponds to IDD Field `fan_placement`
        BlowThrough means the fan is located before the air coil (upstream).
        DrawThrough means the fan is located after the air coil (downstream).

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: DrawThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_placement`')
            vals = {}
            vals["blowthrough"] = "BlowThrough"
            vals["drawthrough"] = "DrawThrough"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `fan_placement`'.format(value))
            value = vals[value_lower]

        self._data["Fan Placement"] = value

    @property
    def on_cycle_parasitic_electric_load(self):
        """Get on_cycle_parasitic_electric_load

        Returns:
            float: the value of `on_cycle_parasitic_electric_load` or None if not set
        """
        return self._data["On Cycle Parasitic Electric Load"]

    @on_cycle_parasitic_electric_load.setter
    def on_cycle_parasitic_electric_load(self, value=0.0 ):
        """  Corresponds to IDD Field `on_cycle_parasitic_electric_load`
        Parasitic electric power consumed when the heat pump compressor operates.
        Does not contribute to water heating but can impact the zone air heat balance.

        Args:
            value (float): value for IDD Field `on_cycle_parasitic_electric_load`
                Units: W
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
                                 'for field `on_cycle_parasitic_electric_load`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `on_cycle_parasitic_electric_load`')

        self._data["On Cycle Parasitic Electric Load"] = value

    @property
    def off_cycle_parasitic_electric_load(self):
        """Get off_cycle_parasitic_electric_load

        Returns:
            float: the value of `off_cycle_parasitic_electric_load` or None if not set
        """
        return self._data["Off Cycle Parasitic Electric Load"]

    @off_cycle_parasitic_electric_load.setter
    def off_cycle_parasitic_electric_load(self, value=0.0 ):
        """  Corresponds to IDD Field `off_cycle_parasitic_electric_load`
        Parasitic electric power consumed when the heat pump compressor is off.
        Does not contribute to water heating but can impact the zone air heat balance.
        Off-cycle parasitic power is 0 when the availability schedule is 0.

        Args:
            value (float): value for IDD Field `off_cycle_parasitic_electric_load`
                Units: W
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
                                 'for field `off_cycle_parasitic_electric_load`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `off_cycle_parasitic_electric_load`')

        self._data["Off Cycle Parasitic Electric Load"] = value

    @property
    def parasitic_heat_rejection_location(self):
        """Get parasitic_heat_rejection_location

        Returns:
            str: the value of `parasitic_heat_rejection_location` or None if not set
        """
        return self._data["Parasitic Heat Rejection Location"]

    @parasitic_heat_rejection_location.setter
    def parasitic_heat_rejection_location(self, value="Outdoors"):
        """  Corresponds to IDD Field `parasitic_heat_rejection_location`
        This field determines if the parasitic electric load impacts the zone air
        heat balance. If Zone is selected, Inlet Air Configuration must be
        ZoneAirOnly or ZoneAndOutdoorAir.

        Args:
            value (str): value for IDD Field `parasitic_heat_rejection_location`
                Accepted values are:
                      - Zone
                      - Outdoors
                Default value: Outdoors
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `parasitic_heat_rejection_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parasitic_heat_rejection_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parasitic_heat_rejection_location`')
            vals = {}
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `parasitic_heat_rejection_location`'.format(value))
            value = vals[value_lower]

        self._data["Parasitic Heat Rejection Location"] = value

    @property
    def inlet_air_mixer_node_name(self):
        """Get inlet_air_mixer_node_name

        Returns:
            str: the value of `inlet_air_mixer_node_name` or None if not set
        """
        return self._data["Inlet Air Mixer Node Name"]

    @inlet_air_mixer_node_name.setter
    def inlet_air_mixer_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_air_mixer_node_name`
        Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        leave field blank.

        Args:
            value (str): value for IDD Field `inlet_air_mixer_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_air_mixer_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_air_mixer_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_air_mixer_node_name`')

        self._data["Inlet Air Mixer Node Name"] = value

    @property
    def outlet_air_splitter_node_name(self):
        """Get outlet_air_splitter_node_name

        Returns:
            str: the value of `outlet_air_splitter_node_name` or None if not set
        """
        return self._data["Outlet Air Splitter Node Name"]

    @outlet_air_splitter_node_name.setter
    def outlet_air_splitter_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_air_splitter_node_name`
        Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        leave field blank.

        Args:
            value (str): value for IDD Field `outlet_air_splitter_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_air_splitter_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_air_splitter_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_air_splitter_node_name`')

        self._data["Outlet Air Splitter Node Name"] = value

    @property
    def inlet_air_mixer_schedule_name(self):
        """Get inlet_air_mixer_schedule_name

        Returns:
            str: the value of `inlet_air_mixer_schedule_name` or None if not set
        """
        return self._data["Inlet Air Mixer Schedule Name"]

    @inlet_air_mixer_schedule_name.setter
    def inlet_air_mixer_schedule_name(self, value=None):
        """  Corresponds to IDD Field `inlet_air_mixer_schedule_name`
        Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        leave field blank. Schedule values define whether the heat pump draws its
        inlet air from the zone, outdoors or a combination of zone and outdoor air.
        A schedule value of 0 denotes inlet air is drawn only from the zone.
        A schedule value of 1 denotes inlet air is drawn only from outdoors.
        Schedule values between 0 and 1 denote a mixture of zone and outdoor air
        proportional to the schedule value.

        Args:
            value (str): value for IDD Field `inlet_air_mixer_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_air_mixer_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_air_mixer_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_air_mixer_schedule_name`')

        self._data["Inlet Air Mixer Schedule Name"] = value

    @property
    def control_sensor_location_in_stratified_tank(self):
        """Get control_sensor_location_in_stratified_tank

        Returns:
            str: the value of `control_sensor_location_in_stratified_tank` or None if not set
        """
        return self._data["Control Sensor Location In Stratified Tank"]

    @control_sensor_location_in_stratified_tank.setter
    def control_sensor_location_in_stratified_tank(self, value="Heater1"):
        """  Corresponds to IDD Field `control_sensor_location_in_stratified_tank`
        Used to indicate height of control sensor if Tank Object Type is WaterHeater:Stratified

        Args:
            value (str): value for IDD Field `control_sensor_location_in_stratified_tank`
                Accepted values are:
                      - Heater1
                      - Heater2
                      - SourceInlet
                      - SourceOutlet
                      - UseInlet
                      - UseOutlet
                Default value: Heater1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_sensor_location_in_stratified_tank`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_sensor_location_in_stratified_tank`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_sensor_location_in_stratified_tank`')
            vals = {}
            vals["heater1"] = "Heater1"
            vals["heater2"] = "Heater2"
            vals["sourceinlet"] = "SourceInlet"
            vals["sourceoutlet"] = "SourceOutlet"
            vals["useinlet"] = "UseInlet"
            vals["useoutlet"] = "UseOutlet"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `control_sensor_location_in_stratified_tank`'.format(value))
            value = vals[value_lower]

        self._data["Control Sensor Location In Stratified Tank"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ThermalStorageIceSimple(object):
    """ Corresponds to IDD object `ThermalStorage:Ice:Simple`
        This ice storage model is a simplified model
        It requires a setpoint placed on the Chilled Water Side Outlet Node
        It should be placed in the chilled water supply side outlet branch
        followed by a pipe.
        Use the PlantEquipmentOperation:ComponentSetpoint plant operation scheme.
    
    """
    internal_name = "ThermalStorage:Ice:Simple"
    field_count = 5
    required_fields = ["Name", "Ice Storage Type", "Capacity", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermalStorage:Ice:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Ice Storage Type"] = None
        self._data["Capacity"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ice_storage_type = None
        else:
            self.ice_storage_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacity = None
        else:
            self.capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def ice_storage_type(self):
        """Get ice_storage_type

        Returns:
            str: the value of `ice_storage_type` or None if not set
        """
        return self._data["Ice Storage Type"]

    @ice_storage_type.setter
    def ice_storage_type(self, value=None):
        """  Corresponds to IDD Field `ice_storage_type`
        IceOnCoilInternal = Ice-on-Coil, internal melt
        IceOnCoilExternal = Ice-on-Coil, external melt

        Args:
            value (str): value for IDD Field `ice_storage_type`
                Accepted values are:
                      - IceOnCoilInternal
                      - IceOnCoilExternal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ice_storage_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ice_storage_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ice_storage_type`')
            vals = {}
            vals["iceoncoilinternal"] = "IceOnCoilInternal"
            vals["iceoncoilexternal"] = "IceOnCoilExternal"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ice_storage_type`'.format(value))
            value = vals[value_lower]

        self._data["Ice Storage Type"] = value

    @property
    def capacity(self):
        """Get capacity

        Returns:
            float: the value of `capacity` or None if not set
        """
        return self._data["Capacity"]

    @capacity.setter
    def capacity(self, value=None):
        """  Corresponds to IDD Field `capacity`

        Args:
            value (float): value for IDD Field `capacity`
                Units: GJ
                IP-Units: ton-hrs
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `capacity`'.format(value))

        self._data["Capacity"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ThermalStorageIceDetailed(object):
    """ Corresponds to IDD object `ThermalStorage:Ice:Detailed`
        This input syntax is intended to describe a thermal storage system that
        includes smaller containers filled with water that are placed in a larger
        tank or series of tanks.
        The model uses polynomial equations to describe the system performance.
    
    """
    internal_name = "ThermalStorage:Ice:Detailed"
    field_count = 15
    required_fields = ["Name", "Capacity", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermalStorage:Ice:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Capacity"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Discharging Curve Object Type"] = None
        self._data["Discharging Curve Name"] = None
        self._data["Charging Curve Object Type"] = None
        self._data["Charging Curve Name"] = None
        self._data["Timestep of the Curve Data"] = None
        self._data["Parasitic Electric Load During Discharging"] = None
        self._data["Parasitic Electric Load During Charging"] = None
        self._data["Tank Loss Coefficient"] = None
        self._data["Freezing Temperature of Storage Medium"] = None
        self._data["Thaw Process Indicator"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacity = None
        else:
            self.capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharging_curve_object_type = None
        else:
            self.discharging_curve_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharging_curve_name = None
        else:
            self.discharging_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.charging_curve_object_type = None
        else:
            self.charging_curve_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.charging_curve_name = None
        else:
            self.charging_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.timestep_of_the_curve_data = None
        else:
            self.timestep_of_the_curve_data = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parasitic_electric_load_during_discharging = None
        else:
            self.parasitic_electric_load_during_discharging = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parasitic_electric_load_during_charging = None
        else:
            self.parasitic_electric_load_during_charging = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_loss_coefficient = None
        else:
            self.tank_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.freezing_temperature_of_storage_medium = None
        else:
            self.freezing_temperature_of_storage_medium = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thaw_process_indicator = None
        else:
            self.thaw_process_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def capacity(self):
        """Get capacity

        Returns:
            float: the value of `capacity` or None if not set
        """
        return self._data["Capacity"]

    @capacity.setter
    def capacity(self, value=None):
        """  Corresponds to IDD Field `capacity`
        This includes only the latent storage capacity

        Args:
            value (float): value for IDD Field `capacity`
                Units: GJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `capacity`'.format(value))

        self._data["Capacity"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def discharging_curve_object_type(self):
        """Get discharging_curve_object_type

        Returns:
            str: the value of `discharging_curve_object_type` or None if not set
        """
        return self._data["Discharging Curve Object Type"]

    @discharging_curve_object_type.setter
    def discharging_curve_object_type(self, value=None):
        """  Corresponds to IDD Field `discharging_curve_object_type`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `discharging_curve_object_type`
                Accepted values are:
                      - Curve:QuadraticLinear
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `discharging_curve_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `discharging_curve_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `discharging_curve_object_type`')
            vals = {}
            vals["curve:quadraticlinear"] = "Curve:QuadraticLinear"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `discharging_curve_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Discharging Curve Object Type"] = value

    @property
    def discharging_curve_name(self):
        """Get discharging_curve_name

        Returns:
            str: the value of `discharging_curve_name` or None if not set
        """
        return self._data["Discharging Curve Name"]

    @discharging_curve_name.setter
    def discharging_curve_name(self, value=None):
        """  Corresponds to IDD Field `discharging_curve_name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `discharging_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `discharging_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `discharging_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `discharging_curve_name`')

        self._data["Discharging Curve Name"] = value

    @property
    def charging_curve_object_type(self):
        """Get charging_curve_object_type

        Returns:
            str: the value of `charging_curve_object_type` or None if not set
        """
        return self._data["Charging Curve Object Type"]

    @charging_curve_object_type.setter
    def charging_curve_object_type(self, value=None):
        """  Corresponds to IDD Field `charging_curve_object_type`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `charging_curve_object_type`
                Accepted values are:
                      - Curve:QuadraticLinear
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `charging_curve_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `charging_curve_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `charging_curve_object_type`')
            vals = {}
            vals["curve:quadraticlinear"] = "Curve:QuadraticLinear"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `charging_curve_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Charging Curve Object Type"] = value

    @property
    def charging_curve_name(self):
        """Get charging_curve_name

        Returns:
            str: the value of `charging_curve_name` or None if not set
        """
        return self._data["Charging Curve Name"]

    @charging_curve_name.setter
    def charging_curve_name(self, value=None):
        """  Corresponds to IDD Field `charging_curve_name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `charging_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `charging_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `charging_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `charging_curve_name`')

        self._data["Charging Curve Name"] = value

    @property
    def timestep_of_the_curve_data(self):
        """Get timestep_of_the_curve_data

        Returns:
            float: the value of `timestep_of_the_curve_data` or None if not set
        """
        return self._data["Timestep of the Curve Data"]

    @timestep_of_the_curve_data.setter
    def timestep_of_the_curve_data(self, value=None):
        """  Corresponds to IDD Field `timestep_of_the_curve_data`

        Args:
            value (float): value for IDD Field `timestep_of_the_curve_data`
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
                                 'for field `timestep_of_the_curve_data`'.format(value))

        self._data["Timestep of the Curve Data"] = value

    @property
    def parasitic_electric_load_during_discharging(self):
        """Get parasitic_electric_load_during_discharging

        Returns:
            float: the value of `parasitic_electric_load_during_discharging` or None if not set
        """
        return self._data["Parasitic Electric Load During Discharging"]

    @parasitic_electric_load_during_discharging.setter
    def parasitic_electric_load_during_discharging(self, value=None):
        """  Corresponds to IDD Field `parasitic_electric_load_during_discharging`

        Args:
            value (float): value for IDD Field `parasitic_electric_load_during_discharging`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `parasitic_electric_load_during_discharging`'.format(value))

        self._data["Parasitic Electric Load During Discharging"] = value

    @property
    def parasitic_electric_load_during_charging(self):
        """Get parasitic_electric_load_during_charging

        Returns:
            float: the value of `parasitic_electric_load_during_charging` or None if not set
        """
        return self._data["Parasitic Electric Load During Charging"]

    @parasitic_electric_load_during_charging.setter
    def parasitic_electric_load_during_charging(self, value=None):
        """  Corresponds to IDD Field `parasitic_electric_load_during_charging`

        Args:
            value (float): value for IDD Field `parasitic_electric_load_during_charging`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `parasitic_electric_load_during_charging`'.format(value))

        self._data["Parasitic Electric Load During Charging"] = value

    @property
    def tank_loss_coefficient(self):
        """Get tank_loss_coefficient

        Returns:
            float: the value of `tank_loss_coefficient` or None if not set
        """
        return self._data["Tank Loss Coefficient"]

    @tank_loss_coefficient.setter
    def tank_loss_coefficient(self, value=None):
        """  Corresponds to IDD Field `tank_loss_coefficient`
        This is the fraction the total storage capacity that is lost or melts
        each hour

        Args:
            value (float): value for IDD Field `tank_loss_coefficient`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `tank_loss_coefficient`'.format(value))

        self._data["Tank Loss Coefficient"] = value

    @property
    def freezing_temperature_of_storage_medium(self):
        """Get freezing_temperature_of_storage_medium

        Returns:
            float: the value of `freezing_temperature_of_storage_medium` or None if not set
        """
        return self._data["Freezing Temperature of Storage Medium"]

    @freezing_temperature_of_storage_medium.setter
    def freezing_temperature_of_storage_medium(self, value=0.0 ):
        """  Corresponds to IDD Field `freezing_temperature_of_storage_medium`
        This temperature is typically 0C for water.
        Simply changing this temperature without adjusting the performance
        parameters input above is inappropriate and not advised.

        Args:
            value (float): value for IDD Field `freezing_temperature_of_storage_medium`
                Units: C
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
                                 'for field `freezing_temperature_of_storage_medium`'.format(value))

        self._data["Freezing Temperature of Storage Medium"] = value

    @property
    def thaw_process_indicator(self):
        """Get thaw_process_indicator

        Returns:
            str: the value of `thaw_process_indicator` or None if not set
        """
        return self._data["Thaw Process Indicator"]

    @thaw_process_indicator.setter
    def thaw_process_indicator(self, value="OutsideMelt"):
        """  Corresponds to IDD Field `thaw_process_indicator`
        This field determines whether the system uses internal or external melt
        during discharging.  This will then have an impact on charging performance.

        Args:
            value (str): value for IDD Field `thaw_process_indicator`
                Accepted values are:
                      - InsideMelt
                      - OutsideMelt
                Default value: OutsideMelt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thaw_process_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thaw_process_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thaw_process_indicator`')
            vals = {}
            vals["insidemelt"] = "InsideMelt"
            vals["outsidemelt"] = "OutsideMelt"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `thaw_process_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Thaw Process Indicator"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ThermalStorageChilledWaterMixed(object):
    """ Corresponds to IDD object `ThermalStorage:ChilledWater:Mixed`
        Chilled water storage with a well-mixed, single-node tank. The chilled water is
        "used" by drawing from the "Use Side" of the water tank.  The tank is indirectly
        charged by circulating cold water through the "Source Side" of the water tank.
    
    """
    internal_name = "ThermalStorage:ChilledWater:Mixed"
    field_count = 22
    required_fields = ["Name", "Ambient Temperature Indicator"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermalStorage:ChilledWater:Mixed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tank Volume"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
        self._data["Deadband Temperature Difference"] = None
        self._data["Minimum Temperature Limit"] = None
        self._data["Nominal Cooling Capacity"] = None
        self._data["Ambient Temperature Indicator"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Heat Gain Coefficient from Ambient Temperature"] = None
        self._data["Use Side Inlet Node Name"] = None
        self._data["Use Side Outlet Node Name"] = None
        self._data["Use Side Heat Transfer Effectiveness"] = None
        self._data["Use Side Availability Schedule Name"] = None
        self._data["Use Side Design Flow Rate"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Source Side Heat Transfer Effectiveness"] = None
        self._data["Source Side Availability Schedule Name"] = None
        self._data["Source Side Design Flow Rate"] = None
        self._data["Tank Recovery Time"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_volume = None
        else:
            self.tank_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.deadband_temperature_difference = None
        else:
            self.deadband_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_temperature_limit = None
        else:
            self.minimum_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_cooling_capacity = None
        else:
            self.nominal_cooling_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_indicator = None
        else:
            self.ambient_temperature_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_gain_coefficient_from_ambient_temperature = None
        else:
            self.heat_gain_coefficient_from_ambient_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_inlet_node_name = None
        else:
            self.use_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_outlet_node_name = None
        else:
            self.use_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_heat_transfer_effectiveness = None
        else:
            self.use_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_availability_schedule_name = None
        else:
            self.use_side_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_design_flow_rate = None
        else:
            self.use_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_heat_transfer_effectiveness = None
        else:
            self.source_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_availability_schedule_name = None
        else:
            self.source_side_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_design_flow_rate = None
        else:
            self.source_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_recovery_time = None
        else:
            self.tank_recovery_time = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def tank_volume(self):
        """Get tank_volume

        Returns:
            float: the value of `tank_volume` or None if not set
        """
        return self._data["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=0.1 ):
        """  Corresponds to IDD Field `tank_volume`

        Args:
            value (float): value for IDD Field `tank_volume`
                Units: m3
                IP-Units: gal
                Default value: 0.1
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
                                 'for field `tank_volume`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_volume`')

        self._data["Tank Volume"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """Get deadband_temperature_difference

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set
        """
        return self._data["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=0.5 ):
        """  Corresponds to IDD Field `deadband_temperature_difference`

        Args:
            value (float): value for IDD Field `deadband_temperature_difference`
                Units: deltaC
                Default value: 0.5
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
                                 'for field `deadband_temperature_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `deadband_temperature_difference`')

        self._data["Deadband Temperature Difference"] = value

    @property
    def minimum_temperature_limit(self):
        """Get minimum_temperature_limit

        Returns:
            float: the value of `minimum_temperature_limit` or None if not set
        """
        return self._data["Minimum Temperature Limit"]

    @minimum_temperature_limit.setter
    def minimum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `minimum_temperature_limit`

        Args:
            value (float): value for IDD Field `minimum_temperature_limit`
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
                                 'for field `minimum_temperature_limit`'.format(value))

        self._data["Minimum Temperature Limit"] = value

    @property
    def nominal_cooling_capacity(self):
        """Get nominal_cooling_capacity

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set
        """
        return self._data["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_cooling_capacity`

        Args:
            value (float): value for IDD Field `nominal_cooling_capacity`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_cooling_capacity`'.format(value))

        self._data["Nominal Cooling Capacity"] = value

    @property
    def ambient_temperature_indicator(self):
        """Get ambient_temperature_indicator

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set
        """
        return self._data["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_indicator`

        Args:
            value (str): value for IDD Field `ambient_temperature_indicator`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_indicator`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ambient_temperature_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_schedule_name`')

        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_zone_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_zone_name`')

        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_outdoor_air_node_name`
        required when field Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `ambient_temperature_outdoor_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_outdoor_air_node_name`')

        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def heat_gain_coefficient_from_ambient_temperature(self):
        """Get heat_gain_coefficient_from_ambient_temperature

        Returns:
            float: the value of `heat_gain_coefficient_from_ambient_temperature` or None if not set
        """
        return self._data["Heat Gain Coefficient from Ambient Temperature"]

    @heat_gain_coefficient_from_ambient_temperature.setter
    def heat_gain_coefficient_from_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `heat_gain_coefficient_from_ambient_temperature`

        Args:
            value (float): value for IDD Field `heat_gain_coefficient_from_ambient_temperature`
                Units: W/K
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
                                 'for field `heat_gain_coefficient_from_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_gain_coefficient_from_ambient_temperature`')

        self._data["Heat Gain Coefficient from Ambient Temperature"] = value

    @property
    def use_side_inlet_node_name(self):
        """Get use_side_inlet_node_name

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set
        """
        return self._data["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_inlet_node_name`')

        self._data["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """Get use_side_outlet_node_name

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set
        """
        return self._data["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_outlet_node_name`')

        self._data["Use Side Outlet Node Name"] = value

    @property
    def use_side_heat_transfer_effectiveness(self):
        """Get use_side_heat_transfer_effectiveness

        Returns:
            float: the value of `use_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Use Side Heat Transfer Effectiveness"]

    @use_side_heat_transfer_effectiveness.setter
    def use_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `use_side_heat_transfer_effectiveness`

        Args:
            value (float): value for IDD Field `use_side_heat_transfer_effectiveness`
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
                                 'for field `use_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')

        self._data["Use Side Heat Transfer Effectiveness"] = value

    @property
    def use_side_availability_schedule_name(self):
        """Get use_side_availability_schedule_name

        Returns:
            str: the value of `use_side_availability_schedule_name` or None if not set
        """
        return self._data["Use Side Availability Schedule Name"]

    @use_side_availability_schedule_name.setter
    def use_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `use_side_availability_schedule_name`
        Availability schedule name for use side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `use_side_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_availability_schedule_name`')

        self._data["Use Side Availability Schedule Name"] = value

    @property
    def use_side_design_flow_rate(self):
        """Get use_side_design_flow_rate

        Returns:
            float: the value of `use_side_design_flow_rate` or None if not set
        """
        return self._data["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `use_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `use_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `use_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_design_flow_rate`')

        self._data["Use Side Design Flow Rate"] = value

    @property
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def source_side_heat_transfer_effectiveness(self):
        """Get source_side_heat_transfer_effectiveness

        Returns:
            float: the value of `source_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Source Side Heat Transfer Effectiveness"]

    @source_side_heat_transfer_effectiveness.setter
    def source_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `source_side_heat_transfer_effectiveness`

        Args:
            value (float): value for IDD Field `source_side_heat_transfer_effectiveness`
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
                                 'for field `source_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')

        self._data["Source Side Heat Transfer Effectiveness"] = value

    @property
    def source_side_availability_schedule_name(self):
        """Get source_side_availability_schedule_name

        Returns:
            str: the value of `source_side_availability_schedule_name` or None if not set
        """
        return self._data["Source Side Availability Schedule Name"]

    @source_side_availability_schedule_name.setter
    def source_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `source_side_availability_schedule_name`
        Availability schedule name for source side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `source_side_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_availability_schedule_name`')

        self._data["Source Side Availability Schedule Name"] = value

    @property
    def source_side_design_flow_rate(self):
        """Get source_side_design_flow_rate

        Returns:
            float: the value of `source_side_design_flow_rate` or None if not set
        """
        return self._data["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `source_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_design_flow_rate`')

        self._data["Source Side Design Flow Rate"] = value

    @property
    def tank_recovery_time(self):
        """Get tank_recovery_time

        Returns:
            float: the value of `tank_recovery_time` or None if not set
        """
        return self._data["Tank Recovery Time"]

    @tank_recovery_time.setter
    def tank_recovery_time(self, value=4.0 ):
        """  Corresponds to IDD Field `tank_recovery_time`
        Parameter for autosizing design flow rates for indirectly cooled water tanks
        time required to lower temperature of entire tank from 14.4C to 9.0C

        Args:
            value (float): value for IDD Field `tank_recovery_time`
                Units: hr
                Default value: 4.0
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
                                 'for field `tank_recovery_time`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_recovery_time`')

        self._data["Tank Recovery Time"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ThermalStorageChilledWaterStratified(object):
    """ Corresponds to IDD object `ThermalStorage:ChilledWater:Stratified`
        Chilled water storage with astratified, multi-node tank. The chilled water is
        "used" by drawing from the "Use Side" of the water tank.  The tank is indirectly
        charged by circulating cold water through the "Source Side" of the water tank.
    
    """
    internal_name = "ThermalStorage:ChilledWater:Stratified"
    field_count = 43
    required_fields = ["Name", "Tank Volume", "Tank Height", "Ambient Temperature Indicator"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermalStorage:ChilledWater:Stratified`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tank Volume"] = None
        self._data["Tank Height"] = None
        self._data["Tank Shape"] = None
        self._data["Tank Perimeter"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
        self._data["Deadband Temperature Difference"] = None
        self._data["Temperature Sensor Height"] = None
        self._data["Minimum Temperature Limit"] = None
        self._data["Nominal Cooling Capacity"] = None
        self._data["Ambient Temperature Indicator"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = None
        self._data["Use Side Inlet Node Name"] = None
        self._data["Use Side Outlet Node Name"] = None
        self._data["Use Side Heat Transfer Effectiveness"] = None
        self._data["Use Side Availability Schedule Name"] = None
        self._data["Use Side Inlet Height"] = None
        self._data["Use Side Outlet Height"] = None
        self._data["Use Side Design Flow Rate"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Source Side Heat Transfer Effectiveness"] = None
        self._data["Source Side Availability Schedule Name"] = None
        self._data["Source Side Inlet Height"] = None
        self._data["Source Side Outlet Height"] = None
        self._data["Source Side Design Flow Rate"] = None
        self._data["Tank Recovery Time"] = None
        self._data["Inlet Mode"] = None
        self._data["Number of Nodes"] = None
        self._data["Additional Destratification Conductivity"] = None
        self._data["Node 1 Additional Loss Coefficient"] = None
        self._data["Node 2 Additional Loss Coefficient"] = None
        self._data["Node 3 Additional Loss Coefficient"] = None
        self._data["Node 4 Additional Loss Coefficient"] = None
        self._data["Node 5 Additional Loss Coefficient"] = None
        self._data["Node 6 Additional Loss Coefficient"] = None
        self._data["Node 7 Additional Loss Coefficient"] = None
        self._data["Node 8 Additional Loss Coefficient"] = None
        self._data["Node 9 Additional Loss Coefficient"] = None
        self._data["Node 10 Additional Loss Coefficient"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_volume = None
        else:
            self.tank_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_height = None
        else:
            self.tank_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_shape = None
        else:
            self.tank_shape = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_perimeter = None
        else:
            self.tank_perimeter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.deadband_temperature_difference = None
        else:
            self.deadband_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_sensor_height = None
        else:
            self.temperature_sensor_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_temperature_limit = None
        else:
            self.minimum_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_cooling_capacity = None
        else:
            self.nominal_cooling_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_indicator = None
        else:
            self.ambient_temperature_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = None
        else:
            self.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_inlet_node_name = None
        else:
            self.use_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_outlet_node_name = None
        else:
            self.use_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_heat_transfer_effectiveness = None
        else:
            self.use_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_availability_schedule_name = None
        else:
            self.use_side_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_inlet_height = None
        else:
            self.use_side_inlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_outlet_height = None
        else:
            self.use_side_outlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_side_design_flow_rate = None
        else:
            self.use_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_heat_transfer_effectiveness = None
        else:
            self.source_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_availability_schedule_name = None
        else:
            self.source_side_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_inlet_height = None
        else:
            self.source_side_inlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_outlet_height = None
        else:
            self.source_side_outlet_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_side_design_flow_rate = None
        else:
            self.source_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_recovery_time = None
        else:
            self.tank_recovery_time = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_mode = None
        else:
            self.inlet_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_nodes = None
        else:
            self.number_of_nodes = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.additional_destratification_conductivity = None
        else:
            self.additional_destratification_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_1_additional_loss_coefficient = None
        else:
            self.node_1_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_2_additional_loss_coefficient = None
        else:
            self.node_2_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_3_additional_loss_coefficient = None
        else:
            self.node_3_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_4_additional_loss_coefficient = None
        else:
            self.node_4_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_5_additional_loss_coefficient = None
        else:
            self.node_5_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_6_additional_loss_coefficient = None
        else:
            self.node_6_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_7_additional_loss_coefficient = None
        else:
            self.node_7_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_8_additional_loss_coefficient = None
        else:
            self.node_8_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_9_additional_loss_coefficient = None
        else:
            self.node_9_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_10_additional_loss_coefficient = None
        else:
            self.node_10_additional_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def tank_volume(self):
        """Get tank_volume

        Returns:
            float: the value of `tank_volume` or None if not set
        """
        return self._data["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=None):
        """  Corresponds to IDD Field `tank_volume`

        Args:
            value (float): value for IDD Field `tank_volume`
                Units: m3
                IP-Units: gal
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
                                 'for field `tank_volume`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_volume`')

        self._data["Tank Volume"] = value

    @property
    def tank_height(self):
        """Get tank_height

        Returns:
            float: the value of `tank_height` or None if not set
        """
        return self._data["Tank Height"]

    @tank_height.setter
    def tank_height(self, value=None):
        """  Corresponds to IDD Field `tank_height`
        Height is measured in the axial direction for horizontal cylinders

        Args:
            value (float): value for IDD Field `tank_height`
                Units: m
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
                                 'for field `tank_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_height`')

        self._data["Tank Height"] = value

    @property
    def tank_shape(self):
        """Get tank_shape

        Returns:
            str: the value of `tank_shape` or None if not set
        """
        return self._data["Tank Shape"]

    @tank_shape.setter
    def tank_shape(self, value="VerticalCylinder"):
        """  Corresponds to IDD Field `tank_shape`

        Args:
            value (str): value for IDD Field `tank_shape`
                Accepted values are:
                      - VerticalCylinder
                      - HorizontalCylinder
                      - Other
                Default value: VerticalCylinder
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `tank_shape`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_shape`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `tank_shape`')
            vals = {}
            vals["verticalcylinder"] = "VerticalCylinder"
            vals["horizontalcylinder"] = "HorizontalCylinder"
            vals["other"] = "Other"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `tank_shape`'.format(value))
            value = vals[value_lower]

        self._data["Tank Shape"] = value

    @property
    def tank_perimeter(self):
        """Get tank_perimeter

        Returns:
            float: the value of `tank_perimeter` or None if not set
        """
        return self._data["Tank Perimeter"]

    @tank_perimeter.setter
    def tank_perimeter(self, value=None):
        """  Corresponds to IDD Field `tank_perimeter`
        Only used if Tank Shape is Other

        Args:
            value (float): value for IDD Field `tank_perimeter`
                Units: m
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
                                 'for field `tank_perimeter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tank_perimeter`')

        self._data["Tank Perimeter"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """Get deadband_temperature_difference

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set
        """
        return self._data["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=0.0 ):
        """  Corresponds to IDD Field `deadband_temperature_difference`

        Args:
            value (float): value for IDD Field `deadband_temperature_difference`
                Units: deltaC
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
                                 'for field `deadband_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deadband_temperature_difference`')

        self._data["Deadband Temperature Difference"] = value

    @property
    def temperature_sensor_height(self):
        """Get temperature_sensor_height

        Returns:
            float: the value of `temperature_sensor_height` or None if not set
        """
        return self._data["Temperature Sensor Height"]

    @temperature_sensor_height.setter
    def temperature_sensor_height(self, value=None):
        """  Corresponds to IDD Field `temperature_sensor_height`

        Args:
            value (float): value for IDD Field `temperature_sensor_height`
                Units: m
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
                                 'for field `temperature_sensor_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_sensor_height`')

        self._data["Temperature Sensor Height"] = value

    @property
    def minimum_temperature_limit(self):
        """Get minimum_temperature_limit

        Returns:
            float: the value of `minimum_temperature_limit` or None if not set
        """
        return self._data["Minimum Temperature Limit"]

    @minimum_temperature_limit.setter
    def minimum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `minimum_temperature_limit`

        Args:
            value (float): value for IDD Field `minimum_temperature_limit`
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
                                 'for field `minimum_temperature_limit`'.format(value))

        self._data["Minimum Temperature Limit"] = value

    @property
    def nominal_cooling_capacity(self):
        """Get nominal_cooling_capacity

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set
        """
        return self._data["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_cooling_capacity`

        Args:
            value (float): value for IDD Field `nominal_cooling_capacity`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_cooling_capacity`'.format(value))

        self._data["Nominal Cooling Capacity"] = value

    @property
    def ambient_temperature_indicator(self):
        """Get ambient_temperature_indicator

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set
        """
        return self._data["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_indicator`

        Args:
            value (str): value for IDD Field `ambient_temperature_indicator`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_indicator`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ambient_temperature_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_schedule_name`')

        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_zone_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_zone_name`')

        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_outdoor_air_node_name`
        required for Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `ambient_temperature_outdoor_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_outdoor_air_node_name`')

        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(self):
        """Get uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature

        Returns:
            float: the value of `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature` or None if not set
        """
        return self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"]

    @uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature.setter
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`

        Args:
            value (float): value for IDD Field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`
                Units: W/m2-K
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
                                 'for field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`')

        self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = value

    @property
    def use_side_inlet_node_name(self):
        """Get use_side_inlet_node_name

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set
        """
        return self._data["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_inlet_node_name`')

        self._data["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """Get use_side_outlet_node_name

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set
        """
        return self._data["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_outlet_node_name`')

        self._data["Use Side Outlet Node Name"] = value

    @property
    def use_side_heat_transfer_effectiveness(self):
        """Get use_side_heat_transfer_effectiveness

        Returns:
            float: the value of `use_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Use Side Heat Transfer Effectiveness"]

    @use_side_heat_transfer_effectiveness.setter
    def use_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `use_side_heat_transfer_effectiveness`
        The use side effectiveness in the stratified tank model is a simplified analogy of
        a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        use mass flow rate that directly mixes with the tank fluid. And one minus the
        effectiveness is the fraction that bypasses the tank. The use side mass flow rate
        that bypasses the tank is mixed with the fluid or water leaving the stratified tank.

        Args:
            value (float): value for IDD Field `use_side_heat_transfer_effectiveness`
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
                                 'for field `use_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')

        self._data["Use Side Heat Transfer Effectiveness"] = value

    @property
    def use_side_availability_schedule_name(self):
        """Get use_side_availability_schedule_name

        Returns:
            str: the value of `use_side_availability_schedule_name` or None if not set
        """
        return self._data["Use Side Availability Schedule Name"]

    @use_side_availability_schedule_name.setter
    def use_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `use_side_availability_schedule_name`
        Availability schedule name for use side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `use_side_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `use_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_side_availability_schedule_name`')

        self._data["Use Side Availability Schedule Name"] = value

    @property
    def use_side_inlet_height(self):
        """Get use_side_inlet_height

        Returns:
            float: the value of `use_side_inlet_height` or None if not set
        """
        return self._data["Use Side Inlet Height"]

    @use_side_inlet_height.setter
    def use_side_inlet_height(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_height`
        Defaults to top of tank

        Args:
            value (float): value for IDD Field `use_side_inlet_height`
                Units: m
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
                                 'for field `use_side_inlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_inlet_height`')

        self._data["Use Side Inlet Height"] = value

    @property
    def use_side_outlet_height(self):
        """Get use_side_outlet_height

        Returns:
            float: the value of `use_side_outlet_height` or None if not set
        """
        return self._data["Use Side Outlet Height"]

    @use_side_outlet_height.setter
    def use_side_outlet_height(self, value=0.0 ):
        """  Corresponds to IDD Field `use_side_outlet_height`
        Defaults to bottom of tank

        Args:
            value (float): value for IDD Field `use_side_outlet_height`
                Units: m
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
                                 'for field `use_side_outlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_outlet_height`')

        self._data["Use Side Outlet Height"] = value

    @property
    def use_side_design_flow_rate(self):
        """Get use_side_design_flow_rate

        Returns:
            float: the value of `use_side_design_flow_rate` or None if not set
        """
        return self._data["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `use_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `use_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `use_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_design_flow_rate`')

        self._data["Use Side Design Flow Rate"] = value

    @property
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def source_side_heat_transfer_effectiveness(self):
        """Get source_side_heat_transfer_effectiveness

        Returns:
            float: the value of `source_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Source Side Heat Transfer Effectiveness"]

    @source_side_heat_transfer_effectiveness.setter
    def source_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `source_side_heat_transfer_effectiveness`
        The source side effectiveness in the stratified tank model is a simplified analogy of
        a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        source mass flow rate that directly mixes with the tank fluid. And one minus the
        effectiveness is the fraction that bypasses the tank. The source side mass flow rate
        that bypasses the tank is mixed with the fluid or water leaving the stratified tank.

        Args:
            value (float): value for IDD Field `source_side_heat_transfer_effectiveness`
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
                                 'for field `source_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')

        self._data["Source Side Heat Transfer Effectiveness"] = value

    @property
    def source_side_availability_schedule_name(self):
        """Get source_side_availability_schedule_name

        Returns:
            str: the value of `source_side_availability_schedule_name` or None if not set
        """
        return self._data["Source Side Availability Schedule Name"]

    @source_side_availability_schedule_name.setter
    def source_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `source_side_availability_schedule_name`
        Availability schedule name for use side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `source_side_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `source_side_availability_schedule_name`')

        self._data["Source Side Availability Schedule Name"] = value

    @property
    def source_side_inlet_height(self):
        """Get source_side_inlet_height

        Returns:
            float: the value of `source_side_inlet_height` or None if not set
        """
        return self._data["Source Side Inlet Height"]

    @source_side_inlet_height.setter
    def source_side_inlet_height(self, value=0.0 ):
        """  Corresponds to IDD Field `source_side_inlet_height`
        Defaults to bottom of tank

        Args:
            value (float): value for IDD Field `source_side_inlet_height`
                Units: m
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
                                 'for field `source_side_inlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_inlet_height`')

        self._data["Source Side Inlet Height"] = value

    @property
    def source_side_outlet_height(self):
        """Get source_side_outlet_height

        Returns:
            float: the value of `source_side_outlet_height` or None if not set
        """
        return self._data["Source Side Outlet Height"]

    @source_side_outlet_height.setter
    def source_side_outlet_height(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_height`
        Defaults to top of tank

        Args:
            value (float): value for IDD Field `source_side_outlet_height`
                Units: m
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
                                 'for field `source_side_outlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_outlet_height`')

        self._data["Source Side Outlet Height"] = value

    @property
    def source_side_design_flow_rate(self):
        """Get source_side_design_flow_rate

        Returns:
            float: the value of `source_side_design_flow_rate` or None if not set
        """
        return self._data["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_design_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `source_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_design_flow_rate`')

        self._data["Source Side Design Flow Rate"] = value

    @property
    def tank_recovery_time(self):
        """Get tank_recovery_time

        Returns:
            float: the value of `tank_recovery_time` or None if not set
        """
        return self._data["Tank Recovery Time"]

    @tank_recovery_time.setter
    def tank_recovery_time(self, value=4.0 ):
        """  Corresponds to IDD Field `tank_recovery_time`
        Parameter for autosizing design flow rates for indirectly cooled water tanks
        time required to lower temperature of entire tank from 14.4C to 9.0C

        Args:
            value (float): value for IDD Field `tank_recovery_time`
                Units: hr
                Default value: 4.0
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
                                 'for field `tank_recovery_time`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_recovery_time`')

        self._data["Tank Recovery Time"] = value

    @property
    def inlet_mode(self):
        """Get inlet_mode

        Returns:
            str: the value of `inlet_mode` or None if not set
        """
        return self._data["Inlet Mode"]

    @inlet_mode.setter
    def inlet_mode(self, value="Fixed"):
        """  Corresponds to IDD Field `inlet_mode`

        Args:
            value (str): value for IDD Field `inlet_mode`
                Accepted values are:
                      - Fixed
                      - Seeking
                Default value: Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_mode`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["seeking"] = "Seeking"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `inlet_mode`'.format(value))
            value = vals[value_lower]

        self._data["Inlet Mode"] = value

    @property
    def number_of_nodes(self):
        """Get number_of_nodes

        Returns:
            int: the value of `number_of_nodes` or None if not set
        """
        return self._data["Number of Nodes"]

    @number_of_nodes.setter
    def number_of_nodes(self, value=1 ):
        """  Corresponds to IDD Field `number_of_nodes`

        Args:
            value (int): value for IDD Field `number_of_nodes`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_nodes`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_nodes`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `number_of_nodes`')

        self._data["Number of Nodes"] = value

    @property
    def additional_destratification_conductivity(self):
        """Get additional_destratification_conductivity

        Returns:
            float: the value of `additional_destratification_conductivity` or None if not set
        """
        return self._data["Additional Destratification Conductivity"]

    @additional_destratification_conductivity.setter
    def additional_destratification_conductivity(self, value=0.0 ):
        """  Corresponds to IDD Field `additional_destratification_conductivity`

        Args:
            value (float): value for IDD Field `additional_destratification_conductivity`
                Units: W/m-K
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
                                 'for field `additional_destratification_conductivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `additional_destratification_conductivity`')

        self._data["Additional Destratification Conductivity"] = value

    @property
    def node_1_additional_loss_coefficient(self):
        """Get node_1_additional_loss_coefficient

        Returns:
            float: the value of `node_1_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 1 Additional Loss Coefficient"]

    @node_1_additional_loss_coefficient.setter
    def node_1_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_1_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_1_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_1_additional_loss_coefficient`'.format(value))

        self._data["Node 1 Additional Loss Coefficient"] = value

    @property
    def node_2_additional_loss_coefficient(self):
        """Get node_2_additional_loss_coefficient

        Returns:
            float: the value of `node_2_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 2 Additional Loss Coefficient"]

    @node_2_additional_loss_coefficient.setter
    def node_2_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_2_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_2_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_2_additional_loss_coefficient`'.format(value))

        self._data["Node 2 Additional Loss Coefficient"] = value

    @property
    def node_3_additional_loss_coefficient(self):
        """Get node_3_additional_loss_coefficient

        Returns:
            float: the value of `node_3_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 3 Additional Loss Coefficient"]

    @node_3_additional_loss_coefficient.setter
    def node_3_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_3_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_3_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_3_additional_loss_coefficient`'.format(value))

        self._data["Node 3 Additional Loss Coefficient"] = value

    @property
    def node_4_additional_loss_coefficient(self):
        """Get node_4_additional_loss_coefficient

        Returns:
            float: the value of `node_4_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 4 Additional Loss Coefficient"]

    @node_4_additional_loss_coefficient.setter
    def node_4_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_4_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_4_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_4_additional_loss_coefficient`'.format(value))

        self._data["Node 4 Additional Loss Coefficient"] = value

    @property
    def node_5_additional_loss_coefficient(self):
        """Get node_5_additional_loss_coefficient

        Returns:
            float: the value of `node_5_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 5 Additional Loss Coefficient"]

    @node_5_additional_loss_coefficient.setter
    def node_5_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_5_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_5_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_5_additional_loss_coefficient`'.format(value))

        self._data["Node 5 Additional Loss Coefficient"] = value

    @property
    def node_6_additional_loss_coefficient(self):
        """Get node_6_additional_loss_coefficient

        Returns:
            float: the value of `node_6_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 6 Additional Loss Coefficient"]

    @node_6_additional_loss_coefficient.setter
    def node_6_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_6_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_6_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_6_additional_loss_coefficient`'.format(value))

        self._data["Node 6 Additional Loss Coefficient"] = value

    @property
    def node_7_additional_loss_coefficient(self):
        """Get node_7_additional_loss_coefficient

        Returns:
            float: the value of `node_7_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 7 Additional Loss Coefficient"]

    @node_7_additional_loss_coefficient.setter
    def node_7_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_7_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_7_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_7_additional_loss_coefficient`'.format(value))

        self._data["Node 7 Additional Loss Coefficient"] = value

    @property
    def node_8_additional_loss_coefficient(self):
        """Get node_8_additional_loss_coefficient

        Returns:
            float: the value of `node_8_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 8 Additional Loss Coefficient"]

    @node_8_additional_loss_coefficient.setter
    def node_8_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_8_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_8_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_8_additional_loss_coefficient`'.format(value))

        self._data["Node 8 Additional Loss Coefficient"] = value

    @property
    def node_9_additional_loss_coefficient(self):
        """Get node_9_additional_loss_coefficient

        Returns:
            float: the value of `node_9_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 9 Additional Loss Coefficient"]

    @node_9_additional_loss_coefficient.setter
    def node_9_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_9_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_9_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_9_additional_loss_coefficient`'.format(value))

        self._data["Node 9 Additional Loss Coefficient"] = value

    @property
    def node_10_additional_loss_coefficient(self):
        """Get node_10_additional_loss_coefficient

        Returns:
            float: the value of `node_10_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 10 Additional Loss Coefficient"]

    @node_10_additional_loss_coefficient.setter
    def node_10_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_10_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_10_additional_loss_coefficient`
                Units: W/m2-K
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
                                 'for field `node_10_additional_loss_coefficient`'.format(value))

        self._data["Node 10 Additional Loss Coefficient"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])