from collections import OrderedDict

class ZoneHvacIdealLoadsAirSystem(object):
    """ Corresponds to IDD object `ZoneHVAC:IdealLoadsAirSystem`
        Ideal system used to calculate loads without modeling a full HVAC system. All that is
        required for the ideal system are zone controls, zone equipment configurations, and
        the ideal loads system component. This component can be thought of as an ideal unit
        that mixes zone air with the specified amount of outdoor air and then adds or removes
        heat and moisture at 100% efficiency in order to meet the specified controls. Energy
        use is reported as DistrictHeating and DistrictCooling.
    
    """
    internal_name = "ZoneHVAC:IdealLoadsAirSystem"
    field_count = 27
    required_fields = ["Name", "Zone Supply Air Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:IdealLoadsAirSystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Supply Air Node Name"] = None
        self._data["Zone Exhaust Air Node Name"] = None
        self._data["Maximum Heating Supply Air Temperature"] = None
        self._data["Minimum Cooling Supply Air Temperature"] = None
        self._data["Maximum Heating Supply Air Humidity Ratio"] = None
        self._data["Minimum Cooling Supply Air Humidity Ratio"] = None
        self._data["Heating Limit"] = None
        self._data["Maximum Heating Air Flow Rate"] = None
        self._data["Maximum Sensible Heating Capacity"] = None
        self._data["Cooling Limit"] = None
        self._data["Maximum Cooling Air Flow Rate"] = None
        self._data["Maximum Total Cooling Capacity"] = None
        self._data["Heating Availability Schedule Name"] = None
        self._data["Cooling Availability Schedule Name"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Cooling Sensible Heat Ratio"] = None
        self._data["Humidification Control Type"] = None
        self._data["Design Specification Outdoor Air Object Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Demand Controlled Ventilation Type"] = None
        self._data["Outdoor Air Economizer Type"] = None
        self._data["Heat Recovery Type"] = None
        self._data["Sensible Heat Recovery Effectiveness"] = None
        self._data["Latent Heat Recovery Effectiveness"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.zone_supply_air_node_name = None
        else:
            self.zone_supply_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_exhaust_air_node_name = None
        else:
            self.zone_exhaust_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_heating_supply_air_temperature = None
        else:
            self.maximum_heating_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_cooling_supply_air_temperature = None
        else:
            self.minimum_cooling_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_heating_supply_air_humidity_ratio = None
        else:
            self.maximum_heating_supply_air_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_cooling_supply_air_humidity_ratio = None
        else:
            self.minimum_cooling_supply_air_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_limit = None
        else:
            self.heating_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_heating_air_flow_rate = None
        else:
            self.maximum_heating_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_sensible_heating_capacity = None
        else:
            self.maximum_sensible_heating_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_limit = None
        else:
            self.cooling_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_cooling_air_flow_rate = None
        else:
            self.maximum_cooling_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_total_cooling_capacity = None
        else:
            self.maximum_total_cooling_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_availability_schedule_name = None
        else:
            self.heating_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_availability_schedule_name = None
        else:
            self.cooling_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_sensible_heat_ratio = None
        else:
            self.cooling_sensible_heat_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidification_control_type = None
        else:
            self.humidification_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_controlled_ventilation_type = None
        else:
            self.demand_controlled_ventilation_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_economizer_type = None
        else:
            self.outdoor_air_economizer_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_type = None
        else:
            self.heat_recovery_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensible_heat_recovery_effectiveness = None
        else:
            self.sensible_heat_recovery_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_heat_recovery_effectiveness = None
        else:
            self.latent_heat_recovery_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def zone_supply_air_node_name(self):
        """Get zone_supply_air_node_name

        Returns:
            str: the value of `zone_supply_air_node_name` or None if not set
        """
        return self._data["Zone Supply Air Node Name"]

    @zone_supply_air_node_name.setter
    def zone_supply_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Supply Air Node Name`
        Must match a zone air inlet node name.

        Args:
            value (str): value for IDD Field `Zone Supply Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_supply_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_supply_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_supply_air_node_name`')
        self._data["Zone Supply Air Node Name"] = value

    @property
    def zone_exhaust_air_node_name(self):
        """Get zone_exhaust_air_node_name

        Returns:
            str: the value of `zone_exhaust_air_node_name` or None if not set
        """
        return self._data["Zone Exhaust Air Node Name"]

    @zone_exhaust_air_node_name.setter
    def zone_exhaust_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Exhaust Air Node Name`
        Should match a zone air exhaust node name.
        This field is optional, but is required if this
        this object is used with other forced air equipment.

        Args:
            value (str): value for IDD Field `Zone Exhaust Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_exhaust_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_exhaust_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_exhaust_air_node_name`')
        self._data["Zone Exhaust Air Node Name"] = value

    @property
    def maximum_heating_supply_air_temperature(self):
        """Get maximum_heating_supply_air_temperature

        Returns:
            float: the value of `maximum_heating_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Heating Supply Air Temperature"]

    @maximum_heating_supply_air_temperature.setter
    def maximum_heating_supply_air_temperature(self, value=50.0):
        """  Corresponds to IDD Field `Maximum Heating Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Maximum Heating Supply Air Temperature`
                Units: C
                Default value: 50.0
                value > 0.0
                value < 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_heating_supply_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_heating_supply_air_temperature`')
            if value >= 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_heating_supply_air_temperature`')
        self._data["Maximum Heating Supply Air Temperature"] = value

    @property
    def minimum_cooling_supply_air_temperature(self):
        """Get minimum_cooling_supply_air_temperature

        Returns:
            float: the value of `minimum_cooling_supply_air_temperature` or None if not set
        """
        return self._data["Minimum Cooling Supply Air Temperature"]

    @minimum_cooling_supply_air_temperature.setter
    def minimum_cooling_supply_air_temperature(self, value=13.0):
        """  Corresponds to IDD Field `Minimum Cooling Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Minimum Cooling Supply Air Temperature`
                Units: C
                Default value: 13.0
                value > -100.0
                value < 50.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_cooling_supply_air_temperature`'.format(value))
            if value <= -100.0:
                raise ValueError('value need to be greater -100.0 '
                                 'for field `minimum_cooling_supply_air_temperature`')
            if value >= 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `minimum_cooling_supply_air_temperature`')
        self._data["Minimum Cooling Supply Air Temperature"] = value

    @property
    def maximum_heating_supply_air_humidity_ratio(self):
        """Get maximum_heating_supply_air_humidity_ratio

        Returns:
            float: the value of `maximum_heating_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Maximum Heating Supply Air Humidity Ratio"]

    @maximum_heating_supply_air_humidity_ratio.setter
    def maximum_heating_supply_air_humidity_ratio(self, value=0.0156):
        """  Corresponds to IDD Field `Maximum Heating Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Maximum Heating Supply Air Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.0156
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_heating_supply_air_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_heating_supply_air_humidity_ratio`')
        self._data["Maximum Heating Supply Air Humidity Ratio"] = value

    @property
    def minimum_cooling_supply_air_humidity_ratio(self):
        """Get minimum_cooling_supply_air_humidity_ratio

        Returns:
            float: the value of `minimum_cooling_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Minimum Cooling Supply Air Humidity Ratio"]

    @minimum_cooling_supply_air_humidity_ratio.setter
    def minimum_cooling_supply_air_humidity_ratio(self, value=0.0077):
        """  Corresponds to IDD Field `Minimum Cooling Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Minimum Cooling Supply Air Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.0077
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_cooling_supply_air_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_cooling_supply_air_humidity_ratio`')
        self._data["Minimum Cooling Supply Air Humidity Ratio"] = value

    @property
    def heating_limit(self):
        """Get heating_limit

        Returns:
            str: the value of `heating_limit` or None if not set
        """
        return self._data["Heating Limit"]

    @heating_limit.setter
    def heating_limit(self, value="NoLimit"):
        """  Corresponds to IDD Field `Heating Limit`

        Args:
            value (str): value for IDD Field `Heating Limit`
                Accepted values are:
                      - NoLimit
                      - LimitFlowRate
                      - LimitCapacity
                      - LimitFlowRateAndCapacity
                Default value: NoLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_limit`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_limit`')
            vals = {}
            vals["nolimit"] = "NoLimit"
            vals["limitflowrate"] = "LimitFlowRate"
            vals["limitcapacity"] = "LimitCapacity"
            vals["limitflowrateandcapacity"] = "LimitFlowRateAndCapacity"
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
                                     'field `heating_limit`'.format(value))
            value = vals[value_lower]
        self._data["Heating Limit"] = value

    @property
    def maximum_heating_air_flow_rate(self):
        """Get maximum_heating_air_flow_rate

        Returns:
            float: the value of `maximum_heating_air_flow_rate` or None if not set
        """
        return self._data["Maximum Heating Air Flow Rate"]

    @maximum_heating_air_flow_rate.setter
    def maximum_heating_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Heating Air Flow Rate`
        This field is ignored if Heating Limit = NoLimit
        If this field is blank, there is no limit.

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Heating Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Heating Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_heating_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_heating_air_flow_rate`')
        self._data["Maximum Heating Air Flow Rate"] = value

    @property
    def maximum_sensible_heating_capacity(self):
        """Get maximum_sensible_heating_capacity

        Returns:
            float: the value of `maximum_sensible_heating_capacity` or None if not set
        """
        return self._data["Maximum Sensible Heating Capacity"]

    @maximum_sensible_heating_capacity.setter
    def maximum_sensible_heating_capacity(self, value=None):
        """  Corresponds to IDD Field `Maximum Sensible Heating Capacity`
        This field is ignored if Heating Limit = NoLimit
        If this field is blank, there is no limit.

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Sensible Heating Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Sensible Heating Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_sensible_heating_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_sensible_heating_capacity`')
        self._data["Maximum Sensible Heating Capacity"] = value

    @property
    def cooling_limit(self):
        """Get cooling_limit

        Returns:
            str: the value of `cooling_limit` or None if not set
        """
        return self._data["Cooling Limit"]

    @cooling_limit.setter
    def cooling_limit(self, value="NoLimit"):
        """  Corresponds to IDD Field `Cooling Limit`

        Args:
            value (str): value for IDD Field `Cooling Limit`
                Accepted values are:
                      - NoLimit
                      - LimitFlowRate
                      - LimitCapacity
                      - LimitFlowRateAndCapacity
                Default value: NoLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_limit`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_limit`')
            vals = {}
            vals["nolimit"] = "NoLimit"
            vals["limitflowrate"] = "LimitFlowRate"
            vals["limitcapacity"] = "LimitCapacity"
            vals["limitflowrateandcapacity"] = "LimitFlowRateAndCapacity"
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
                                     'field `cooling_limit`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Limit"] = value

    @property
    def maximum_cooling_air_flow_rate(self):
        """Get maximum_cooling_air_flow_rate

        Returns:
            float: the value of `maximum_cooling_air_flow_rate` or None if not set
        """
        return self._data["Maximum Cooling Air Flow Rate"]

    @maximum_cooling_air_flow_rate.setter
    def maximum_cooling_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Cooling Air Flow Rate`
        This field is ignored if Cooling Limit = NoLimit
        This field is required if Outdoor Air Economizer Type is anything other than NoEconomizer.

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cooling Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Cooling Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_cooling_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_cooling_air_flow_rate`')
        self._data["Maximum Cooling Air Flow Rate"] = value

    @property
    def maximum_total_cooling_capacity(self):
        """Get maximum_total_cooling_capacity

        Returns:
            float: the value of `maximum_total_cooling_capacity` or None if not set
        """
        return self._data["Maximum Total Cooling Capacity"]

    @maximum_total_cooling_capacity.setter
    def maximum_total_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `Maximum Total Cooling Capacity`
        This field is ignored if Cooling Limit = NoLimit

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Total Cooling Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Total Cooling Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_total_cooling_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_total_cooling_capacity`')
        self._data["Maximum Total Cooling Capacity"] = value

    @property
    def heating_availability_schedule_name(self):
        """Get heating_availability_schedule_name

        Returns:
            str: the value of `heating_availability_schedule_name` or None if not set
        """
        return self._data["Heating Availability Schedule Name"]

    @heating_availability_schedule_name.setter
    def heating_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Availability Schedule Name`
        If blank, heating is always available.

        Args:
            value (str): value for IDD Field `Heating Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_availability_schedule_name`')
        self._data["Heating Availability Schedule Name"] = value

    @property
    def cooling_availability_schedule_name(self):
        """Get cooling_availability_schedule_name

        Returns:
            str: the value of `cooling_availability_schedule_name` or None if not set
        """
        return self._data["Cooling Availability Schedule Name"]

    @cooling_availability_schedule_name.setter
    def cooling_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Availability Schedule Name`
        If blank, cooling is always available.

        Args:
            value (str): value for IDD Field `Cooling Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_availability_schedule_name`')
        self._data["Cooling Availability Schedule Name"] = value

    @property
    def dehumidification_control_type(self):
        """Get dehumidification_control_type

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self._data["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="ConstantSensibleHeatRatio"):
        """  Corresponds to IDD Field `Dehumidification Control Type`
        ConstantSensibleHeatRatio means that the ideal loads system
        will be controlled to meet the sensible cooling load, and the
        latent cooling rate will be computed using a constant
        sensible heat ratio (SHR)
        Humidistat means that there is a ZoneControl:Humidistat for this
        zone and the ideal loads system will attempt to satisfy the humidistat.
        None means that there is no dehumidification.
        ConstantSupplyHumidityRatio means that during cooling the supply air
        will always be at the Minimum Cooling Supply Humidity Ratio.

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Accepted values are:
                      - ConstantSensibleHeatRatio
                      - Humidistat
                      - None
                      - ConstantSupplyHumidityRatio
                Default value: ConstantSensibleHeatRatio
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `dehumidification_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dehumidification_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dehumidification_control_type`')
            vals = {}
            vals["constantsensibleheatratio"] = "ConstantSensibleHeatRatio"
            vals["humidistat"] = "Humidistat"
            vals["none"] = "None"
            vals["constantsupplyhumidityratio"] = "ConstantSupplyHumidityRatio"
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
                                     'field `dehumidification_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Dehumidification Control Type"] = value

    @property
    def cooling_sensible_heat_ratio(self):
        """Get cooling_sensible_heat_ratio

        Returns:
            float: the value of `cooling_sensible_heat_ratio` or None if not set
        """
        return self._data["Cooling Sensible Heat Ratio"]

    @cooling_sensible_heat_ratio.setter
    def cooling_sensible_heat_ratio(self, value=0.7):
        """  Corresponds to IDD Field `Cooling Sensible Heat Ratio`
        This field is applicable only when Dehumidification Control Type is ConstantSensibleHeatRatio

        Args:
            value (float): value for IDD Field `Cooling Sensible Heat Ratio`
                Units: dimensionless
                Default value: 0.7
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cooling_sensible_heat_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_sensible_heat_ratio`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cooling_sensible_heat_ratio`')
        self._data["Cooling Sensible Heat Ratio"] = value

    @property
    def humidification_control_type(self):
        """Get humidification_control_type

        Returns:
            str: the value of `humidification_control_type` or None if not set
        """
        return self._data["Humidification Control Type"]

    @humidification_control_type.setter
    def humidification_control_type(self, value="None"):
        """  Corresponds to IDD Field `Humidification Control Type`
        None means that there is no humidification.
        Humidistat means that there is a ZoneControl:Humidistat for this
        zone and the ideal loads system will attempt to satisfy the humidistat.
        ConstantSupplyHumidityRatio means that during heating the supply air
        will always be at the Maximum Heating Supply Humidity Ratio.

        Args:
            value (str): value for IDD Field `Humidification Control Type`
                Accepted values are:
                      - None
                      - Humidistat
                      - ConstantSupplyHumidityRatio
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `humidification_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `humidification_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `humidification_control_type`')
            vals = {}
            vals["none"] = "None"
            vals["humidistat"] = "Humidistat"
            vals["constantsupplyhumidityratio"] = "ConstantSupplyHumidityRatio"
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
                                     'field `humidification_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Humidification Control Type"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """Get design_specification_outdoor_air_object_name

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification Outdoor Air Object Name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the minimum
        outdoor air flow rate will be computed using these specifications. The outdoor air
        flow rate will also be affected by the next two fields.
        If this field is blank, there will be no outdoor air and the remaining fields will
        be ignored.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name`')
        self._data["Design Specification Outdoor Air Object Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        This field is required if the system provides outdoor air
        Enter the name of an outdoor air node. This node name is also specified in
        an OutdoorAir:Node or OutdoorAir:NodeList object.

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def demand_controlled_ventilation_type(self):
        """Get demand_controlled_ventilation_type

        Returns:
            str: the value of `demand_controlled_ventilation_type` or None if not set
        """
        return self._data["Demand Controlled Ventilation Type"]

    @demand_controlled_ventilation_type.setter
    def demand_controlled_ventilation_type(self, value="None"):
        """  Corresponds to IDD Field `Demand Controlled Ventilation Type`
        This field controls how the minimum outdoor air flow rate is calculated.
        None means that design occupancy will be uased to compute the minimum outdoor air flow rate
        OccupancySchedule means that current occupancy level will be used.
        CO2Setpoint means that the design occupancy will be used to compute the minimum outdoor air flow
        reate and the outdoor air flow rate may be increased if necessary to maintain the indoor air carbon
        dioxide setpoint defined in a ZoneControl:ContaminantController object.

        Args:
            value (str): value for IDD Field `Demand Controlled Ventilation Type`
                Accepted values are:
                      - None
                      - OccupancySchedule
                      - CO2Setpoint
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_controlled_ventilation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_controlled_ventilation_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_controlled_ventilation_type`')
            vals = {}
            vals["none"] = "None"
            vals["occupancyschedule"] = "OccupancySchedule"
            vals["co2setpoint"] = "CO2Setpoint"
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
                                     'field `demand_controlled_ventilation_type`'.format(value))
            value = vals[value_lower]
        self._data["Demand Controlled Ventilation Type"] = value

    @property
    def outdoor_air_economizer_type(self):
        """Get outdoor_air_economizer_type

        Returns:
            str: the value of `outdoor_air_economizer_type` or None if not set
        """
        return self._data["Outdoor Air Economizer Type"]

    @outdoor_air_economizer_type.setter
    def outdoor_air_economizer_type(self, value="NoEconomizer"):
        """  Corresponds to IDD Field `Outdoor Air Economizer Type`
        DifferentialDryBulb and DifferentialEnthalpy will increase the outdoor air flow rate
        when there is a cooling load and the outdoor air temperature or enthalpy
        is below the zone exhaust air temperature or enthalpy.

        Args:
            value (str): value for IDD Field `Outdoor Air Economizer Type`
                Accepted values are:
                      - NoEconomizer
                      - DifferentialDryBulb
                      - DifferentialEnthalpy
                Default value: NoEconomizer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_economizer_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_economizer_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_economizer_type`')
            vals = {}
            vals["noeconomizer"] = "NoEconomizer"
            vals["differentialdrybulb"] = "DifferentialDryBulb"
            vals["differentialenthalpy"] = "DifferentialEnthalpy"
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
                                     'field `outdoor_air_economizer_type`'.format(value))
            value = vals[value_lower]
        self._data["Outdoor Air Economizer Type"] = value

    @property
    def heat_recovery_type(self):
        """Get heat_recovery_type

        Returns:
            str: the value of `heat_recovery_type` or None if not set
        """
        return self._data["Heat Recovery Type"]

    @heat_recovery_type.setter
    def heat_recovery_type(self, value="None"):
        """  Corresponds to IDD Field `Heat Recovery Type`

        Args:
            value (str): value for IDD Field `Heat Recovery Type`
                Accepted values are:
                      - None
                      - Sensible
                      - Enthalpy
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_recovery_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_recovery_type`')
            vals = {}
            vals["none"] = "None"
            vals["sensible"] = "Sensible"
            vals["enthalpy"] = "Enthalpy"
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
                                     'field `heat_recovery_type`'.format(value))
            value = vals[value_lower]
        self._data["Heat Recovery Type"] = value

    @property
    def sensible_heat_recovery_effectiveness(self):
        """Get sensible_heat_recovery_effectiveness

        Returns:
            float: the value of `sensible_heat_recovery_effectiveness` or None if not set
        """
        return self._data["Sensible Heat Recovery Effectiveness"]

    @sensible_heat_recovery_effectiveness.setter
    def sensible_heat_recovery_effectiveness(self, value=0.7):
        """  Corresponds to IDD Field `Sensible Heat Recovery Effectiveness`

        Args:
            value (float): value for IDD Field `Sensible Heat Recovery Effectiveness`
                Units: dimensionless
                Default value: 0.7
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `sensible_heat_recovery_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sensible_heat_recovery_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `sensible_heat_recovery_effectiveness`')
        self._data["Sensible Heat Recovery Effectiveness"] = value

    @property
    def latent_heat_recovery_effectiveness(self):
        """Get latent_heat_recovery_effectiveness

        Returns:
            float: the value of `latent_heat_recovery_effectiveness` or None if not set
        """
        return self._data["Latent Heat Recovery Effectiveness"]

    @latent_heat_recovery_effectiveness.setter
    def latent_heat_recovery_effectiveness(self, value=0.65):
        """  Corresponds to IDD Field `Latent Heat Recovery Effectiveness`
        Applicable only if Heat Recovery Type is Enthalpy.

        Args:
            value (float): value for IDD Field `Latent Heat Recovery Effectiveness`
                Units: dimensionless
                Default value: 0.65
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `latent_heat_recovery_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `latent_heat_recovery_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `latent_heat_recovery_effectiveness`')
        self._data["Latent Heat Recovery Effectiveness"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacFourPipeFanCoil(object):
    """ Corresponds to IDD object `ZoneHVAC:FourPipeFanCoil`
        Four pipe fan coil system. Forced-convection hydronic heating-cooling unit with
        supply fan, hot water heating coil, chilled water cooling coil, and fixed-position
        outdoor air mixer.
    
    """
    internal_name = "ZoneHVAC:FourPipeFanCoil"
    field_count = 26
    required_fields = ["Name", "Capacity Control Method", "Maximum Supply Air Flow Rate", "Maximum Outdoor Air Flow Rate", "Air Inlet Node Name", "Air Outlet Node Name", "Supply Air Fan Object Type", "Supply Air Fan Name", "Cooling Coil Object Type", "Cooling Coil Name", "Maximum Cold Water Flow Rate", "Heating Coil Object Type", "Heating Coil Name", "Maximum Hot Water Flow Rate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:FourPipeFanCoil`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Capacity Control Method"] = None
        self._data["Maximum Supply Air Flow Rate"] = None
        self._data["Low Speed Supply Air Flow Ratio"] = None
        self._data["Medium Speed Supply Air Flow Ratio"] = None
        self._data["Maximum Outdoor Air Flow Rate"] = None
        self._data["Outdoor Air Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Mixer Object Type"] = None
        self._data["Outdoor Air Mixer Name"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Maximum Cold Water Flow Rate"] = None
        self._data["Minimum Cold Water Flow Rate"] = None
        self._data["Cooling Convergence Tolerance"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Maximum Hot Water Flow Rate"] = None
        self._data["Minimum Hot Water Flow Rate"] = None
        self._data["Heating Convergence Tolerance"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.capacity_control_method = None
        else:
            self.capacity_control_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_supply_air_flow_ratio = None
        else:
            self.low_speed_supply_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.medium_speed_supply_air_flow_ratio = None
        else:
            self.medium_speed_supply_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_schedule_name = None
        else:
            self.outdoor_air_schedule_name = vals[i]
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
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_cold_water_flow_rate = None
        else:
            self.maximum_cold_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_cold_water_flow_rate = None
        else:
            self.minimum_cold_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_flow_rate = None
        else:
            self.maximum_hot_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_flow_rate = None
        else:
            self.minimum_hot_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def capacity_control_method(self):
        """Get capacity_control_method

        Returns:
            str: the value of `capacity_control_method` or None if not set
        """
        return self._data["Capacity Control Method"]

    @capacity_control_method.setter
    def capacity_control_method(self, value=None):
        """  Corresponds to IDD Field `Capacity Control Method`

        Args:
            value (str): value for IDD Field `Capacity Control Method`
                Accepted values are:
                      - ConstantFanVariableFlow
                      - CyclingFan
                      - VariableFanVariableFlow
                      - VariableFanConstantFlow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `capacity_control_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_control_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `capacity_control_method`')
            vals = {}
            vals["constantfanvariableflow"] = "ConstantFanVariableFlow"
            vals["cyclingfan"] = "CyclingFan"
            vals["variablefanvariableflow"] = "VariableFanVariableFlow"
            vals["variablefanconstantflow"] = "VariableFanConstantFlow"
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
                                     'field `capacity_control_method`'.format(value))
            value = vals[value_lower]
        self._data["Capacity Control Method"] = value

    @property
    def maximum_supply_air_flow_rate(self):
        """Get maximum_supply_air_flow_rate

        Returns:
            float: the value of `maximum_supply_air_flow_rate` or None if not set
        """
        return self._data["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_supply_air_flow_rate`'.format(value))
        self._data["Maximum Supply Air Flow Rate"] = value

    @property
    def low_speed_supply_air_flow_ratio(self):
        """Get low_speed_supply_air_flow_ratio

        Returns:
            float: the value of `low_speed_supply_air_flow_ratio` or None if not set
        """
        return self._data["Low Speed Supply Air Flow Ratio"]

    @low_speed_supply_air_flow_ratio.setter
    def low_speed_supply_air_flow_ratio(self, value=0.33):
        """  Corresponds to IDD Field `Low Speed Supply Air Flow Ratio`

        Args:
            value (float): value for IDD Field `Low Speed Supply Air Flow Ratio`
                Default value: 0.33
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_supply_air_flow_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_supply_air_flow_ratio`')
        self._data["Low Speed Supply Air Flow Ratio"] = value

    @property
    def medium_speed_supply_air_flow_ratio(self):
        """Get medium_speed_supply_air_flow_ratio

        Returns:
            float: the value of `medium_speed_supply_air_flow_ratio` or None if not set
        """
        return self._data["Medium Speed Supply Air Flow Ratio"]

    @medium_speed_supply_air_flow_ratio.setter
    def medium_speed_supply_air_flow_ratio(self, value=0.66):
        """  Corresponds to IDD Field `Medium Speed Supply Air Flow Ratio`
        Medium Speed Supply Air Flow Ratio should be greater
        than Low Speed Supply Air Flow Ratio

        Args:
            value (float): value for IDD Field `Medium Speed Supply Air Flow Ratio`
                Default value: 0.66
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `medium_speed_supply_air_flow_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `medium_speed_supply_air_flow_ratio`')
        self._data["Medium Speed Supply Air Flow Ratio"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """Get maximum_outdoor_air_flow_rate

        Returns:
            float: the value of `maximum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_outdoor_air_flow_rate`'.format(value))
        self._data["Maximum Outdoor Air Flow Rate"] = value

    @property
    def outdoor_air_schedule_name(self):
        """Get outdoor_air_schedule_name

        Returns:
            str: the value of `outdoor_air_schedule_name` or None if not set
        """
        return self._data["Outdoor Air Schedule Name"]

    @outdoor_air_schedule_name.setter
    def outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Schedule Name`
        Value of schedule multiplies maximum outdoor air flow rate

        Args:
            value (str): value for IDD Field `Outdoor Air Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_schedule_name`')
        self._data["Outdoor Air Schedule Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def outdoor_air_mixer_object_type(self):
        """Get outdoor_air_mixer_object_type

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set
        """
        return self._data["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Object Type`
        currently only one type OutdoorAir:Mixer object is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`
                Accepted values are:
                      - OutdoorAir:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = {}
            vals["outdoorair:mixer"] = "OutdoorAir:Mixer"
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
                                     'field `outdoor_air_mixer_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """Get outdoor_air_mixer_name

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set
        """
        return self._data["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_name`')
        self._data["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`
        Fan type must be according to capacity control method (see I/O)
        For ConstantFanVariableFlow a Fan:OnOff or Fan:ConstantVolume is valid.
        For CyclingFan, a Fan:OnOff is valid.
        For VariableFanVariableFlow or VariableFanConstantFlow a Fan:VariableVolume is valid.
        The fans inlet node should be the same as the outdoor air mixers mixed air node.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                      - Fan:VariableVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
            vals["fan:variablevolume"] = "Fan:VariableVolume"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatExchangerAssisted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatExchangerAssisted"
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
                                     'field `cooling_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Cooling Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_name`')
        self._data["Cooling Coil Name"] = value

    @property
    def maximum_cold_water_flow_rate(self):
        """Get maximum_cold_water_flow_rate

        Returns:
            float: the value of `maximum_cold_water_flow_rate` or None if not set
        """
        return self._data["Maximum Cold Water Flow Rate"]

    @maximum_cold_water_flow_rate.setter
    def maximum_cold_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Cold Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cold Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Cold Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_cold_water_flow_rate`'.format(value))
        self._data["Maximum Cold Water Flow Rate"] = value

    @property
    def minimum_cold_water_flow_rate(self):
        """Get minimum_cold_water_flow_rate

        Returns:
            float: the value of `minimum_cold_water_flow_rate` or None if not set
        """
        return self._data["Minimum Cold Water Flow Rate"]

    @minimum_cold_water_flow_rate.setter
    def minimum_cold_water_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Cold Water Flow Rate`

        Args:
            value (float): value for IDD Field `Minimum Cold Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_cold_water_flow_rate`'.format(value))
        self._data["Minimum Cold Water Flow Rate"] = value

    @property
    def cooling_convergence_tolerance(self):
        """Get cooling_convergence_tolerance

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set
        """
        return self._data["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Cooling Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cooling_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_convergence_tolerance`')
        self._data["Cooling Convergence Tolerance"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
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
                                     'field `heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def maximum_hot_water_flow_rate(self):
        """Get maximum_hot_water_flow_rate

        Returns:
            float: the value of `maximum_hot_water_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water Flow Rate"]

    @maximum_hot_water_flow_rate.setter
    def maximum_hot_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_flow_rate`'.format(value))
        self._data["Maximum Hot Water Flow Rate"] = value

    @property
    def minimum_hot_water_flow_rate(self):
        """Get minimum_hot_water_flow_rate

        Returns:
            float: the value of `minimum_hot_water_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water Flow Rate"]

    @minimum_hot_water_flow_rate.setter
    def minimum_hot_water_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water Flow Rate`

        Args:
            value (float): value for IDD Field `Minimum Hot Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_flow_rate`'.format(value))
        self._data["Minimum Hot Water Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Heating Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_convergence_tolerance`')
        self._data["Heating Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacWindowAirConditioner(object):
    """ Corresponds to IDD object `ZoneHVAC:WindowAirConditioner`
        Window air conditioner. Forced-convection cooling-only unit with supply fan, direct
        expansion (DX) cooling coil, and fixed-position outdoor air mixer.
    
    """
    internal_name = "ZoneHVAC:WindowAirConditioner"
    field_count = 17
    required_fields = ["Name", "Maximum Supply Air Flow Rate", "Maximum Outdoor Air Flow Rate", "Air Inlet Node Name", "Air Outlet Node Name", "Outdoor Air Mixer Object Type", "Outdoor Air Mixer Name", "Supply Air Fan Object Type", "Supply Air Fan Name", "Cooling Coil Object Type", "DX Cooling Coil Name", "Fan Placement"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:WindowAirConditioner`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Maximum Supply Air Flow Rate"] = None
        self._data["Maximum Outdoor Air Flow Rate"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Mixer Object Type"] = None
        self._data["Outdoor Air Mixer Name"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["DX Cooling Coil Name"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Fan Placement"] = None
        self._data["Cooling Convergence Tolerance"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
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
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dx_cooling_coil_name = None
        else:
            self.dx_cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
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
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def maximum_supply_air_flow_rate(self):
        """Get maximum_supply_air_flow_rate

        Returns:
            float: the value of `maximum_supply_air_flow_rate` or None if not set
        """
        return self._data["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_supply_air_flow_rate`'.format(value))
        self._data["Maximum Supply Air Flow Rate"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """Get maximum_outdoor_air_flow_rate

        Returns:
            float: the value of `maximum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_outdoor_air_flow_rate`'.format(value))
        self._data["Maximum Outdoor Air Flow Rate"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def outdoor_air_mixer_object_type(self):
        """Get outdoor_air_mixer_object_type

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set
        """
        return self._data["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Object Type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`
                Accepted values are:
                      - OutdoorAir:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = {}
            vals["outdoorair:mixer"] = "OutdoorAir:Mixer"
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
                                     'field `outdoor_air_mixer_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """Get outdoor_air_mixer_name

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set
        """
        return self._data["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_name`')
        self._data["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`
        Fan:ConstantVolume only works when continuous fan operation is used the entire
        simulation (all supply air fan operating mode schedule values are greater than 0).
        If any fan operating mode schedule values are 0 a Fan:OnOff object must be used.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`
        Fan type Fan:ConstantVolume is used with continuous fan
        and fan type Fan:OnOff is used with cycling Fan.

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:dx:singlespeed"] = "Coil:Cooling:DX:SingleSpeed"
            vals["coilsystem:cooling:dx:heatexchangerassisted"] = "CoilSystem:Cooling:DX:HeatExchangerAssisted"
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
                                     'field `cooling_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def dx_cooling_coil_name(self):
        """Get dx_cooling_coil_name

        Returns:
            str: the value of `dx_cooling_coil_name` or None if not set
        """
        return self._data["DX Cooling Coil Name"]

    @dx_cooling_coil_name.setter
    def dx_cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `DX Cooling Coil Name`

        Args:
            value (str): value for IDD Field `DX Cooling Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `dx_cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dx_cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dx_cooling_coil_name`')
        self._data["DX Cooling Coil Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote
        cycling fan operation (fan cycles with cooling coil). Schedule values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value=None):
        """  Corresponds to IDD Field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def cooling_convergence_tolerance(self):
        """Get cooling_convergence_tolerance

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set
        """
        return self._data["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Cooling Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cooling_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_convergence_tolerance`')
        self._data["Cooling Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacPackagedTerminalAirConditioner(object):
    """ Corresponds to IDD object `ZoneHVAC:PackagedTerminalAirConditioner`
        Packaged terminal air conditioner (PTAC).  Forced-convection heating-cooling unit
        with supply fan, direct expansion (DX) cooling coil, heating coil (gas, electric, hot
        water, or steam) and fixed-position outdoor air mixer.
    
    """
    internal_name = "ZoneHVAC:PackagedTerminalAirConditioner"
    field_count = 22
    required_fields = ["Name", "Availability Schedule Name", "Air Inlet Node Name", "Air Outlet Node Name", "Outdoor Air Mixer Object Type", "Outdoor Air Mixer Name", "Supply Air Flow Rate During Cooling Operation", "Supply Air Flow Rate During Heating Operation", "Outdoor Air Flow Rate During Cooling Operation", "Outdoor Air Flow Rate During Heating Operation", "Supply Air Fan Object Type", "Supply Air Fan Name", "Heating Coil Object Type", "Heating Coil Name", "Cooling Coil Object Type", "Cooling Coil Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:PackagedTerminalAirConditioner`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Mixer Object Type"] = None
        self._data["Outdoor Air Mixer Name"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = None
        self._data["Outdoor Air Flow Rate During Heating Operation"] = None
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
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
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        Unique name for this packaged terminal air conditioner object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Schedule values of 0 denote the unit is off.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        Air inlet node for the PTAC must be a zone air exhaust Node.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`
        Air outlet node for the PTAC must be a zone air inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def outdoor_air_mixer_object_type(self):
        """Get outdoor_air_mixer_object_type

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set
        """
        return self._data["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Object Type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`
                Accepted values are:
                      - OutdoorAir:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = {}
            vals["outdoorair:mixer"] = "OutdoorAir:Mixer"
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
                                     'field `outdoor_air_mixer_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """Get outdoor_air_mixer_name

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set
        """
        return self._data["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Name`
        Needs to match the name of the PTAC outdoor air mixer object.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_name`')
        self._data["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Cooling Operation`
        Must be less than or equal to fan size.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')
        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Heating Operation`
        Must be less than or equal to fan size.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')
        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
        Must be less than or equal to fan size.
        Only used when supply air fan operating mode schedule values specify continuous fan
        (schedule values greater than 0 specify continuous fan operation).
        This air flow rate is used when no heating or cooling is required and the cooling or
        heating coil is off. If this field is left blank or zero, the supply air flow rate
        from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`')
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_during_cooling_operation(self):
        """Get outdoor_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Cooling Operation"]

    @outdoor_air_flow_rate_during_cooling_operation.setter
    def outdoor_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Cooling Operation`
        Must be less than or equal to supply air flow rate during cooling operation.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Cooling Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`')
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = value

    @property
    def outdoor_air_flow_rate_during_heating_operation(self):
        """Get outdoor_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Heating Operation"]

    @outdoor_air_flow_rate_during_heating_operation.setter
    def outdoor_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Heating Operation`
        Must be less than or equal to supply air flow rate during heating operation.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Heating Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`')
        self._data["Outdoor Air Flow Rate During Heating Operation"] = value

    @property
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"]

    @outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
        Only used when supply air fan operating mode schedule values specify continuous fan
        (schedule values greater than 0 specify continuous fan operation).
        This air flow rate is used when no heating or cooling is required and the cooling or
        heating coil is off. If this field is left blank or zero, the outdoor air flow rate
        from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`')
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`
        Fan:ConstantVolume only works when continuous fan operation is used the entire
        simulation (all supply air fan operating mode schedule values are greater than 0).
        If any fan operating mode schedule values are 0 a Fan:OnOff object must be used.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`
        Needs to match in the fan object.

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`
        Select the type of heating coil.

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`
        Needs to match in the heating coil object.

        Args:
            value (str): value for IDD Field `Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`
        Select the type of Cooling Coil.
        Only works with Coil:Cooling:DX:SingleSpeed or
        CoilSystem:Cooling:DX:HeatExchangerAssisted or
        Coil:Cooling:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Cooling:DX:VariableSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:dx:singlespeed"] = "Coil:Cooling:DX:SingleSpeed"
            vals["coil:cooling:dx:variablespeed"] = "Coil:Cooling:DX:VariableSpeed"
            vals["coilsystem:cooling:dx:heatexchangerassisted"] = "CoilSystem:Cooling:DX:HeatExchangerAssisted"
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
                                     'field `cooling_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Name`
        Needs to match a DX cooling coil object.

        Args:
            value (str): value for IDD Field `Cooling Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_name`')
        self._data["Cooling Coil Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="DrawThrough"):
        """  Corresponds to IDD Field `Fan Placement`
        Select fan placement as either blow through or draw through.

        Args:
            value (str): value for IDD Field `Fan Placement`
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
            except ValueError:
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
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacPackagedTerminalHeatPump(object):
    """ Corresponds to IDD object `ZoneHVAC:PackagedTerminalHeatPump`
        Packaged terminal heat pump (PTHP). Forced-convection heating-cooling unit with
        supply fan, direct expansion (DX) cooling coil, DX heating coil (air-to-air heat
        pump), supplemental heating coil (gas, electric, hot water, or steam), and
        fixed-position outdoor air mixer.
    
    """
    internal_name = "ZoneHVAC:PackagedTerminalHeatPump"
    field_count = 29
    required_fields = ["Name", "Air Inlet Node Name", "Air Outlet Node Name", "Outdoor Air Mixer Object Type", "Outdoor Air Mixer Name", "Supply Air Flow Rate During Cooling Operation", "Supply Air Flow Rate During Heating Operation", "Outdoor Air Flow Rate During Cooling Operation", "Outdoor Air Flow Rate During Heating Operation", "Supply Air Fan Object Type", "Supply Air Fan Name", "Heating Coil Object Type", "Heating Coil Name", "Cooling Coil Object Type", "Cooling Coil Name", "Supplemental Heating Coil Object Type", "Supplemental Heating Coil Name", "Maximum Supply Air Temperature from Supplemental Heater"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:PackagedTerminalHeatPump`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Mixer Object Type"] = None
        self._data["Outdoor Air Mixer Name"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = None
        self._data["Outdoor Air Flow Rate During Heating Operation"] = None
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Heating Convergence Tolerance"] = None
        self._data["Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Cooling Convergence Tolerance"] = None
        self._data["Supplemental Heating Coil Object Type"] = None
        self._data["Supplemental Heating Coil Name"] = None
        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = None
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = None
        self._data["Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_drybulb_temperature_for_compressor_operation = None
        else:
            self.minimum_outdoor_drybulb_temperature_for_compressor_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature_from_supplemental_heater = None
        else:
            self.maximum_supply_air_temperature_from_supplemental_heater = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
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
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        Unique name for this packaged terminal heat pump object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.
        Schedule values of 0 denote the unit is off.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        Air inlet node for the PTHP must be a zone air exhaust node.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`
        Air outlet node for the PTHP must be a zone air inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def outdoor_air_mixer_object_type(self):
        """Get outdoor_air_mixer_object_type

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set
        """
        return self._data["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Object Type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`
                Accepted values are:
                      - OutdoorAir:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = {}
            vals["outdoorair:mixer"] = "OutdoorAir:Mixer"
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
                                     'field `outdoor_air_mixer_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """Get outdoor_air_mixer_name

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set
        """
        return self._data["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Name`
        Needs to match name of outdoor air mixer object.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_name`')
        self._data["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Cooling Operation`
        Must be less than or equal to fan size.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')
        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Heating Operation`
        Must be less than or equal to fan size.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')
        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
        Must be less than or equal to fan size.
        Only used when heat pump fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the supply air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`')
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_during_cooling_operation(self):
        """Get outdoor_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Cooling Operation"]

    @outdoor_air_flow_rate_during_cooling_operation.setter
    def outdoor_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Cooling Operation`
        Must be less than or equal to supply air flow rate during cooling operation.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Cooling Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`')
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = value

    @property
    def outdoor_air_flow_rate_during_heating_operation(self):
        """Get outdoor_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Heating Operation"]

    @outdoor_air_flow_rate_during_heating_operation.setter
    def outdoor_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Heating Operation`
        Must be less than or equal to supply air flow rate during heating operation.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Heating Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`')
        self._data["Outdoor Air Flow Rate During Heating Operation"] = value

    @property
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"]

    @outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
        Only used when heat pump Fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the outdoor air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`')
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`
        Fan:ConstantVolume only works with fan operating mode is continuous.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`
        Needs to match a fan object.

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`
        Only works with Coil:Heating:DX:SingleSpeed or
        Coil:Heating:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:DX:SingleSpeed
                      - Coil:Heating:DX:VariableSpeed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:dx:singlespeed"] = "Coil:Heating:DX:SingleSpeed"
            vals["coil:heating:dx:variablespeed"] = "Coil:Heating:DX:VariableSpeed"
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
                                     'field `heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`
        Needs to match in the DX Heating Coil object.

        Args:
            value (str): value for IDD Field `Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Heating Convergence Tolerance`
        Defines Heating convergence tolerence as a fraction of Heating load to be met.

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`
                Units: dimensionless
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_convergence_tolerance`')
        self._data["Heating Convergence Tolerance"] = value

    @property
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(self):
        """Get minimum_outdoor_drybulb_temperature_for_compressor_operation

        Returns:
            float: the value of `minimum_outdoor_drybulb_temperature_for_compressor_operation` or None if not set
        """
        return self._data["Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"]

    @minimum_outdoor_drybulb_temperature_for_compressor_operation.setter
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(self, value=-8.0):
        """  Corresponds to IDD Field `Minimum Outdoor Dry-Bulb Temperature for Compressor Operation`
        Needs to match the corresponding minimum outdoor temperature defined
        in the DX Heating Coil object.

        Args:
            value (float): value for IDD Field `Minimum Outdoor Dry-Bulb Temperature for Compressor Operation`
                Units: C
                Default value: -8.0
                value >= -20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_outdoor_drybulb_temperature_for_compressor_operation`'.format(value))
            if value < -20.0:
                raise ValueError('value need to be greater or equal -20.0 '
                                 'for field `minimum_outdoor_drybulb_temperature_for_compressor_operation`')
        self._data["Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`
        Only works with Coil:Cooling:DX:SingleSpeed or
        CoilSystem:Cooling:DX:HeatExchangerAssisted or
        Coil:Cooling:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Cooling:DX:VariableSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:dx:singlespeed"] = "Coil:Cooling:DX:SingleSpeed"
            vals["coil:cooling:dx:variablespeed"] = "Coil:Cooling:DX:VariableSpeed"
            vals["coilsystem:cooling:dx:heatexchangerassisted"] = "CoilSystem:Cooling:DX:HeatExchangerAssisted"
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
                                     'field `cooling_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Name`
        Needs to match in the DX Cooling Coil object.

        Args:
            value (str): value for IDD Field `Cooling Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_name`')
        self._data["Cooling Coil Name"] = value

    @property
    def cooling_convergence_tolerance(self):
        """Get cooling_convergence_tolerance

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set
        """
        return self._data["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Cooling Convergence Tolerance`
        Defines Cooling convergence tolerence as a fraction of the Cooling load to be met.

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`
                Units: dimensionless
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cooling_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_convergence_tolerance`')
        self._data["Cooling Convergence Tolerance"] = value

    @property
    def supplemental_heating_coil_object_type(self):
        """Get supplemental_heating_coil_object_type

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set
        """
        return self._data["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Supplemental Heating Coil Object Type`
        works with gas, electric, hot water and steam heating coil.

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = {}
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `supplemental_heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """Get supplemental_heating_coil_name

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set
        """
        return self._data["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Supplemental Heating Coil Name`
        Needs to match in the supplemental heating coil object.

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supplemental_heating_coil_name`')
        self._data["Supplemental Heating Coil Name"] = value

    @property
    def maximum_supply_air_temperature_from_supplemental_heater(self):
        """Get maximum_supply_air_temperature_from_supplemental_heater

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set
        """
        return self._data["Maximum Supply Air Temperature from Supplemental Heater"]

    @maximum_supply_air_temperature_from_supplemental_heater.setter
    def maximum_supply_air_temperature_from_supplemental_heater(self, value=None):
        """  Corresponds to IDD Field `Maximum Supply Air Temperature from Supplemental Heater`
        Supply air temperature from the supplemental heater will not exceed this value.

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature from Supplemental Heater`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Supply Air Temperature from Supplemental Heater"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_supply_air_temperature_from_supplemental_heater`'.format(value))
        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self):
        """Get maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0):
        """  Corresponds to IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
        Supplemental heater will not operate when outdoor temperature exceeds this value.

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
                Units: C
                Default value: 21.0
                value <= 21.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`'.format(value))
            if value > 21.0:
                raise ValueError('value need to be smaller 21.0 '
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`')
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="DrawThrough"):
        """  Corresponds to IDD Field `Fan Placement`
        Select fan placement as either blow through or draw through.

        Args:
            value (str): value for IDD Field `Fan Placement`
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
            except ValueError:
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
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule that controls fan operation. Schedule values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacWaterToAirHeatPump(object):
    """ Corresponds to IDD object `ZoneHVAC:WaterToAirHeatPump`
        Water-to-air heat pump. Forced-convection heating-cooling unit with supply fan,
        water-to-air cooling and heating coils, supplemental heating coil (gas, electric, hot
        water, or steam), and fixed-position outdoor air mixer.
    
    """
    internal_name = "ZoneHVAC:WaterToAirHeatPump"
    field_count = 32
    required_fields = ["Name", "Air Inlet Node Name", "Air Outlet Node Name", "Supply Air Flow Rate During Cooling Operation", "Supply Air Flow Rate During Heating Operation", "Outdoor Air Flow Rate During Cooling Operation", "Outdoor Air Flow Rate During Heating Operation", "Supply Air Fan Object Type", "Supply Air Fan Name", "Heating Coil Object Type", "Heating Coil Name", "Cooling Coil Object Type", "Cooling Coil Name", "Supplemental Heating Coil Object Type", "Supplemental Heating Coil Name", "Maximum Supply Air Temperature from Supplemental Heater"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:WaterToAirHeatPump`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Mixer Object Type"] = None
        self._data["Outdoor Air Mixer Name"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = None
        self._data["Outdoor Air Flow Rate During Heating Operation"] = None
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Maximum Cycling Rate"] = None
        self._data["Heat Pump Time Constant"] = None
        self._data["Fraction of On-Cycle Power Use"] = None
        self._data["Heat Pump Fan Delay Time"] = None
        self._data["Supplemental Heating Coil Object Type"] = None
        self._data["Supplemental Heating Coil Name"] = None
        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = None
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = None
        self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"] = None
        self._data["Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Heat Pump Coil Water Flow Mode"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_cycling_rate = None
        else:
            self.maximum_cycling_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_pump_time_constant = None
        else:
            self.heat_pump_time_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_oncycle_power_use = None
        else:
            self.fraction_of_oncycle_power_use = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_pump_fan_delay_time = None
        else:
            self.heat_pump_fan_delay_time = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature_from_supplemental_heater = None
        else:
            self.maximum_supply_air_temperature_from_supplemental_heater = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_drybulb_temperature_sensor_node_name = None
        else:
            self.outdoor_drybulb_temperature_sensor_node_name = vals[i]
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
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_pump_coil_water_flow_mode = None
        else:
            self.heat_pump_coil_water_flow_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def outdoor_air_mixer_object_type(self):
        """Get outdoor_air_mixer_object_type

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set
        """
        return self._data["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Object Type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`
                Accepted values are:
                      - OutdoorAir:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = {}
            vals["outdoorair:mixer"] = "OutdoorAir:Mixer"
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
                                     'field `outdoor_air_mixer_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """Get outdoor_air_mixer_name

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set
        """
        return self._data["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Name`
        This optional field specifies the name of the outdoor air mixer object.
        When used, this name needs to match name of outdoor air mixer object.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_mixer_name`')
        self._data["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Cooling Operation`
        Must be less than or equal to fan size.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')
        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Heating Operation`
        Must be less than or equal to fan size.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')
        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
        Must be less than or equal to fan size.
        Only used when heat pump fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the supply air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`')
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_during_cooling_operation(self):
        """Get outdoor_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Cooling Operation"]

    @outdoor_air_flow_rate_during_cooling_operation.setter
    def outdoor_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Cooling Operation`
        Must be less than or equal to supply air flow rate during cooling operation.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Cooling Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`')
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = value

    @property
    def outdoor_air_flow_rate_during_heating_operation(self):
        """Get outdoor_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Heating Operation"]

    @outdoor_air_flow_rate_during_heating_operation.setter
    def outdoor_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Heating Operation`
        Must be less than or equal to supply air flow rate during heating operation.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Heating Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`')
        self._data["Outdoor Air Flow Rate During Heating Operation"] = value

    @property
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"]

    @outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
        Only used when heat pump Fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the outdoor air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`')
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`
        Only works with On/Off Fan

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`
        Needs to match Fan:OnOff object

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:WaterToAirHeatPump:EquationFit
                      - Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:watertoairheatpump:equationfit"] = "Coil:Heating:WaterToAirHeatPump:EquationFit"
            vals["coil:heating:watertoairheatpump:variablespeedequationfit"] = "Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit"
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
                                     'field `heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`
        Needs to match in the water-to-air heatpump heating coil object

        Args:
            value (str): value for IDD Field `Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:WaterToAirHeatPump:EquationFit
                      - Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:watertoairheatpump:equationfit"] = "Coil:Cooling:WaterToAirHeatPump:EquationFit"
            vals["coil:cooling:watertoairheatpump:variablespeedequationfit"] = "Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit"
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
                                     'field `cooling_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Name`
        Needs to match in the water-to-air heatpump cooling coil object

        Args:
            value (str): value for IDD Field `Cooling Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_name`')
        self._data["Cooling Coil Name"] = value

    @property
    def maximum_cycling_rate(self):
        """Get maximum_cycling_rate

        Returns:
            float: the value of `maximum_cycling_rate` or None if not set
        """
        return self._data["Maximum Cycling Rate"]

    @maximum_cycling_rate.setter
    def maximum_cycling_rate(self, value=2.5):
        """  Corresponds to IDD Field `Maximum Cycling Rate`
        The maximum on-off cycling rate for the compressor
        Suggested value is 2.5 for a typical heat pump

        Args:
            value (float): value for IDD Field `Maximum Cycling Rate`
                Units: cycles/hr
                Default value: 2.5
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
            except ValueError:
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
    def heat_pump_time_constant(self):
        """Get heat_pump_time_constant

        Returns:
            float: the value of `heat_pump_time_constant` or None if not set
        """
        return self._data["Heat Pump Time Constant"]

    @heat_pump_time_constant.setter
    def heat_pump_time_constant(self, value=60.0):
        """  Corresponds to IDD Field `Heat Pump Time Constant`
        Time constant for the cooling coil's capacity to reach steady state after startup
        Suggested value is 60 for a typical heat pump

        Args:
            value (float): value for IDD Field `Heat Pump Time Constant`
                Units: s
                Default value: 60.0
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_pump_time_constant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_pump_time_constant`')
            if value > 500.0:
                raise ValueError('value need to be smaller 500.0 '
                                 'for field `heat_pump_time_constant`')
        self._data["Heat Pump Time Constant"] = value

    @property
    def fraction_of_oncycle_power_use(self):
        """Get fraction_of_oncycle_power_use

        Returns:
            float: the value of `fraction_of_oncycle_power_use` or None if not set
        """
        return self._data["Fraction of On-Cycle Power Use"]

    @fraction_of_oncycle_power_use.setter
    def fraction_of_oncycle_power_use(self, value=0.01):
        """  Corresponds to IDD Field `Fraction of On-Cycle Power Use`
        The fraction of on-cycle power use to adjust the part load fraction based on
        the off-cycle power consumption due to crankcase heaters, controls, fans, and etc.
        Suggested value is 0.01 for a typical heat pump

        Args:
            value (float): value for IDD Field `Fraction of On-Cycle Power Use`
                Default value: 0.01
                value >= 0.0
                value <= 0.05
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_oncycle_power_use`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_oncycle_power_use`')
            if value > 0.05:
                raise ValueError('value need to be smaller 0.05 '
                                 'for field `fraction_of_oncycle_power_use`')
        self._data["Fraction of On-Cycle Power Use"] = value

    @property
    def heat_pump_fan_delay_time(self):
        """Get heat_pump_fan_delay_time

        Returns:
            float: the value of `heat_pump_fan_delay_time` or None if not set
        """
        return self._data["Heat Pump Fan Delay Time"]

    @heat_pump_fan_delay_time.setter
    def heat_pump_fan_delay_time(self, value=60.0):
        """  Corresponds to IDD Field `Heat Pump Fan Delay Time`
        Programmed time delay for heat pump fan to shut off after compressor cycle off.
        Only required when fan operating mode is cycling
        Enter 0 when fan operating mode is continuous

        Args:
            value (float): value for IDD Field `Heat Pump Fan Delay Time`
                Units: s
                Default value: 60.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_pump_fan_delay_time`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_pump_fan_delay_time`')
        self._data["Heat Pump Fan Delay Time"] = value

    @property
    def supplemental_heating_coil_object_type(self):
        """Get supplemental_heating_coil_object_type

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set
        """
        return self._data["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Supplemental Heating Coil Object Type`
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = {}
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `supplemental_heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """Get supplemental_heating_coil_name

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set
        """
        return self._data["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Supplemental Heating Coil Name`
        Needs to match in the supplemental heating coil object

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supplemental_heating_coil_name`')
        self._data["Supplemental Heating Coil Name"] = value

    @property
    def maximum_supply_air_temperature_from_supplemental_heater(self):
        """Get maximum_supply_air_temperature_from_supplemental_heater

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set
        """
        return self._data["Maximum Supply Air Temperature from Supplemental Heater"]

    @maximum_supply_air_temperature_from_supplemental_heater.setter
    def maximum_supply_air_temperature_from_supplemental_heater(self, value=None):
        """  Corresponds to IDD Field `Maximum Supply Air Temperature from Supplemental Heater`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature from Supplemental Heater`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Supply Air Temperature from Supplemental Heater"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_supply_air_temperature_from_supplemental_heater`'.format(value))
        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self):
        """Get maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0):
        """  Corresponds to IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
                Units: C
                Default value: 21.0
                value <= 21.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`'.format(value))
            if value > 21.0:
                raise ValueError('value need to be smaller 21.0 '
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`')
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def outdoor_drybulb_temperature_sensor_node_name(self):
        """Get outdoor_drybulb_temperature_sensor_node_name

        Returns:
            str: the value of `outdoor_drybulb_temperature_sensor_node_name` or None if not set
        """
        return self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"]

    @outdoor_drybulb_temperature_sensor_node_name.setter
    def outdoor_drybulb_temperature_sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Dry-Bulb Temperature Sensor Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Dry-Bulb Temperature Sensor Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`')
        self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule that controls fan operation. Schedule values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil). Schedule values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def heat_pump_coil_water_flow_mode(self):
        """Get heat_pump_coil_water_flow_mode

        Returns:
            str: the value of `heat_pump_coil_water_flow_mode` or None if not set
        """
        return self._data["Heat Pump Coil Water Flow Mode"]

    @heat_pump_coil_water_flow_mode.setter
    def heat_pump_coil_water_flow_mode(self, value="Cycling"):
        """  Corresponds to IDD Field `Heat Pump Coil Water Flow Mode`
        used only when the heat pump coils are of the type WaterToAirHeatPump:EquationFit
        Constant results in 100% water flow regardless of compressor PLR
        Cycling results in water flow that matches compressor PLR
        ConstantOnDemand results in 100% water flow whenever the coil is on, but is 0% whenever the coil has no load

        Args:
            value (str): value for IDD Field `Heat Pump Coil Water Flow Mode`
                Accepted values are:
                      - Constant
                      - Cycling
                      - ConstantOnDemand
                Default value: Cycling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_pump_coil_water_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_pump_coil_water_flow_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_pump_coil_water_flow_mode`')
            vals = {}
            vals["constant"] = "Constant"
            vals["cycling"] = "Cycling"
            vals["constantondemand"] = "ConstantOnDemand"
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
                                     'field `heat_pump_coil_water_flow_mode`'.format(value))
            value = vals[value_lower]
        self._data["Heat Pump Coil Water Flow Mode"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacDehumidifierDx(object):
    """ Corresponds to IDD object `ZoneHVAC:Dehumidifier:DX`
        This object calculates the performance of zone (room) air dehumidifiers.
        Meant to model conventional direct expansion (DX) cooling-based room air
        dehumidifiers (reject 100% of condenser heat to the zone air), but this
        object might be able to be used to model other room air dehumidifier types.
    
    """
    internal_name = "ZoneHVAC:Dehumidifier:DX"
    field_count = 14
    required_fields = ["Name", "Air Inlet Node Name", "Air Outlet Node Name", "Rated Water Removal", "Rated Energy Factor", "Rated Air Flow Rate", "Water Removal Curve Name", "Energy Factor Curve Name", "Part Load Fraction Correlation Curve Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:Dehumidifier:DX`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Rated Water Removal"] = None
        self._data["Rated Energy Factor"] = None
        self._data["Rated Air Flow Rate"] = None
        self._data["Water Removal Curve Name"] = None
        self._data["Energy Factor Curve Name"] = None
        self._data["Part Load Fraction Correlation Curve Name"] = None
        self._data["Minimum Dry-Bulb Temperature for Dehumidifier Operation"] = None
        self._data["Maximum Dry-Bulb Temperature for Dehumidifier Operation"] = None
        self._data["Off-Cycle Parasitic Electric Load"] = None
        self._data["Condensate Collection Water Storage Tank Name"] = None
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
            self.rated_water_removal = None
        else:
            self.rated_water_removal = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_energy_factor = None
        else:
            self.rated_energy_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_air_flow_rate = None
        else:
            self.rated_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_removal_curve_name = None
        else:
            self.water_removal_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.energy_factor_curve_name = None
        else:
            self.energy_factor_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.part_load_fraction_correlation_curve_name = None
        else:
            self.part_load_fraction_correlation_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_drybulb_temperature_for_dehumidifier_operation = None
        else:
            self.minimum_drybulb_temperature_for_dehumidifier_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_drybulb_temperature_for_dehumidifier_operation = None
        else:
            self.maximum_drybulb_temperature_for_dehumidifier_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.offcycle_parasitic_electric_load = None
        else:
            self.offcycle_parasitic_electric_load = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_collection_water_storage_tank_name = None
        else:
            self.condensate_collection_water_storage_tank_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        Unique name for this direct expansion (DX) zone dehumidifier object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.
        Schedule values of 0 denote the unit is off.
        Schedule values >0.0 (usually 1.0) indicate that the dehumidifier is available to operate.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        Air inlet node for the dehumidifier must be a zone air exhaust node.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`
        Air outlet node for the dehumidifier must be a zone air inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def rated_water_removal(self):
        """Get rated_water_removal

        Returns:
            float: the value of `rated_water_removal` or None if not set
        """
        return self._data["Rated Water Removal"]

    @rated_water_removal.setter
    def rated_water_removal(self, value=None):
        """  Corresponds to IDD Field `Rated Water Removal`
        Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.

        Args:
            value (float): value for IDD Field `Rated Water Removal`
                Units: L/day
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_water_removal`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_water_removal`')
        self._data["Rated Water Removal"] = value

    @property
    def rated_energy_factor(self):
        """Get rated_energy_factor

        Returns:
            float: the value of `rated_energy_factor` or None if not set
        """
        return self._data["Rated Energy Factor"]

    @rated_energy_factor.setter
    def rated_energy_factor(self, value=None):
        """  Corresponds to IDD Field `Rated Energy Factor`
        Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.

        Args:
            value (float): value for IDD Field `Rated Energy Factor`
                Units: L/kWh
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_energy_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_energy_factor`')
        self._data["Rated Energy Factor"] = value

    @property
    def rated_air_flow_rate(self):
        """Get rated_air_flow_rate

        Returns:
            float: the value of `rated_air_flow_rate` or None if not set
        """
        return self._data["Rated Air Flow Rate"]

    @rated_air_flow_rate.setter
    def rated_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Rated Air Flow Rate`

        Args:
            value (float): value for IDD Field `Rated Air Flow Rate`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_air_flow_rate`')
        self._data["Rated Air Flow Rate"] = value

    @property
    def water_removal_curve_name(self):
        """Get water_removal_curve_name

        Returns:
            str: the value of `water_removal_curve_name` or None if not set
        """
        return self._data["Water Removal Curve Name"]

    @water_removal_curve_name.setter
    def water_removal_curve_name(self, value=None):
        """  Corresponds to IDD Field `Water Removal Curve Name`
        Table:TwoIndependentVariable object can also be used
        Name of a curve that describes the water removal rate (normalized to rated conditions)
        as a function of the dry-bulb temperature and relative humidity of the air
        entering the dehumidifier.
        Curve output = (actual water removal/rated water removal) = a + b*T + c*T**2 + d*RH +
        e*RH**2 + f*T*RH
        T = inlet air dry-bulb temperature (C)
        RH = inlet air RH (%)

        Args:
            value (str): value for IDD Field `Water Removal Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_removal_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_removal_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_removal_curve_name`')
        self._data["Water Removal Curve Name"] = value

    @property
    def energy_factor_curve_name(self):
        """Get energy_factor_curve_name

        Returns:
            str: the value of `energy_factor_curve_name` or None if not set
        """
        return self._data["Energy Factor Curve Name"]

    @energy_factor_curve_name.setter
    def energy_factor_curve_name(self, value=None):
        """  Corresponds to IDD Field `Energy Factor Curve Name`
        Table:TwoIndependentVariable object can also be used
        Name of a curve that describes the energy factor (normalized to rated conditions)
        as a function of the dry-bulb temperature and relative humidity of the air
        entering the dehumidifier.
        Curve output = (actual energy factor/rated energy factor) = a + b*T + c*T**2 + d*RH +
        e*RH**2 + f*T*RH
        T = inlet air dry-bulb temperature (C)
        RH = inlet air RH (%)

        Args:
            value (str): value for IDD Field `Energy Factor Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `energy_factor_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `energy_factor_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `energy_factor_curve_name`')
        self._data["Energy Factor Curve Name"] = value

    @property
    def part_load_fraction_correlation_curve_name(self):
        """Get part_load_fraction_correlation_curve_name

        Returns:
            str: the value of `part_load_fraction_correlation_curve_name` or None if not set
        """
        return self._data["Part Load Fraction Correlation Curve Name"]

    @part_load_fraction_correlation_curve_name.setter
    def part_load_fraction_correlation_curve_name(self, value=None):
        """  Corresponds to IDD Field `Part Load Fraction Correlation Curve Name`
        Table:OneIndependentVariable can also be used
        Name of a curve that describes the part load fraction (PLF) of the system as
        a function of the part load ratio. Used to calculate dehumidifier run time fraction
        and electric power.
        quadratic curve = a + b*PLR + c*PLR**2
        cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3
        PLR = part load ratio (dehumidification load/steady state water removal capacity)

        Args:
            value (str): value for IDD Field `Part Load Fraction Correlation Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `part_load_fraction_correlation_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `part_load_fraction_correlation_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `part_load_fraction_correlation_curve_name`')
        self._data["Part Load Fraction Correlation Curve Name"] = value

    @property
    def minimum_drybulb_temperature_for_dehumidifier_operation(self):
        """Get minimum_drybulb_temperature_for_dehumidifier_operation

        Returns:
            float: the value of `minimum_drybulb_temperature_for_dehumidifier_operation` or None if not set
        """
        return self._data["Minimum Dry-Bulb Temperature for Dehumidifier Operation"]

    @minimum_drybulb_temperature_for_dehumidifier_operation.setter
    def minimum_drybulb_temperature_for_dehumidifier_operation(self, value=10.0):
        """  Corresponds to IDD Field `Minimum Dry-Bulb Temperature for Dehumidifier Operation`
        Dehumidifier shut off if inlet air (zone) temperature is below this value.
        This value must be less than the Maximum Dry-Bulb Temperature for Dehumidifier Operation.

        Args:
            value (float): value for IDD Field `Minimum Dry-Bulb Temperature for Dehumidifier Operation`
                Units: C
                Default value: 10.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_drybulb_temperature_for_dehumidifier_operation`'.format(value))
        self._data["Minimum Dry-Bulb Temperature for Dehumidifier Operation"] = value

    @property
    def maximum_drybulb_temperature_for_dehumidifier_operation(self):
        """Get maximum_drybulb_temperature_for_dehumidifier_operation

        Returns:
            float: the value of `maximum_drybulb_temperature_for_dehumidifier_operation` or None if not set
        """
        return self._data["Maximum Dry-Bulb Temperature for Dehumidifier Operation"]

    @maximum_drybulb_temperature_for_dehumidifier_operation.setter
    def maximum_drybulb_temperature_for_dehumidifier_operation(self, value=35.0):
        """  Corresponds to IDD Field `Maximum Dry-Bulb Temperature for Dehumidifier Operation`
        Dehumidifier shut off if inlet air (zone) temperature is above this value.
        This value must be greater than the Minimum Dry-Bulb Temperature for Dehumidifier Operation.

        Args:
            value (float): value for IDD Field `Maximum Dry-Bulb Temperature for Dehumidifier Operation`
                Units: C
                Default value: 35.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_drybulb_temperature_for_dehumidifier_operation`'.format(value))
        self._data["Maximum Dry-Bulb Temperature for Dehumidifier Operation"] = value

    @property
    def offcycle_parasitic_electric_load(self):
        """Get offcycle_parasitic_electric_load

        Returns:
            float: the value of `offcycle_parasitic_electric_load` or None if not set
        """
        return self._data["Off-Cycle Parasitic Electric Load"]

    @offcycle_parasitic_electric_load.setter
    def offcycle_parasitic_electric_load(self, value=0.0):
        """  Corresponds to IDD Field `Off-Cycle Parasitic Electric Load`
        Parasitic electric power consumed when the dehumidifier is available to operate, but
        does not operate (i.e., no high humidity load to be met).
        Off cycle parasitic power is 0 when the availability schedule is 0.
        This electric load is considered as a heat gain to the zone air.

        Args:
            value (float): value for IDD Field `Off-Cycle Parasitic Electric Load`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `offcycle_parasitic_electric_load`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `offcycle_parasitic_electric_load`')
        self._data["Off-Cycle Parasitic Electric Load"] = value

    @property
    def condensate_collection_water_storage_tank_name(self):
        """Get condensate_collection_water_storage_tank_name

        Returns:
            str: the value of `condensate_collection_water_storage_tank_name` or None if not set
        """
        return self._data["Condensate Collection Water Storage Tank Name"]

    @condensate_collection_water_storage_tank_name.setter
    def condensate_collection_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Condensate Collection Water Storage Tank Name`
        Name of storage tank used to collect water removed by the dehumidifier.

        Args:
            value (str): value for IDD Field `Condensate Collection Water Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `condensate_collection_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condensate_collection_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condensate_collection_water_storage_tank_name`')
        self._data["Condensate Collection Water Storage Tank Name"] = value

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

class ZoneHvacEnergyRecoveryVentilator(object):
    """ Corresponds to IDD object `ZoneHVAC:EnergyRecoveryVentilator`
        This compound component models a stand-alone energy recovery ventilator (ERV)
        that conditions outdoor ventilation air and supplies that air directly to a zone.
        The ERV unit is modeled as a collection of components: air-to-air heat exchanger,
        supply air fan, exhaust air fan and an optional controller to avoid overheating
        of the supply air (economizer or free cooling operation).
    
    """
    internal_name = "ZoneHVAC:EnergyRecoveryVentilator"
    field_count = 11
    required_fields = ["Name", "Heat Exchanger Name", "Supply Air Flow Rate", "Exhaust Air Flow Rate", "Supply Air Fan Name", "Exhaust Air Fan Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:EnergyRecoveryVentilator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Heat Exchanger Name"] = None
        self._data["Supply Air Flow Rate"] = None
        self._data["Exhaust Air Flow Rate"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Exhaust Air Fan Name"] = None
        self._data["Controller Name"] = None
        self._data["Ventilation Rate per Unit Floor Area"] = None
        self._data["Ventilation Rate per Occupant"] = None
        self._data["Availability Manager List Name"] = None
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
            self.heat_exchanger_name = None
        else:
            self.heat_exchanger_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate = None
        else:
            self.supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_flow_rate = None
        else:
            self.exhaust_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_fan_name = None
        else:
            self.exhaust_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_name = None
        else:
            self.controller_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ventilation_rate_per_unit_floor_area = None
        else:
            self.ventilation_rate_per_unit_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ventilation_rate_per_occupant = None
        else:
            self.ventilation_rate_per_occupant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def heat_exchanger_name(self):
        """Get heat_exchanger_name

        Returns:
            str: the value of `heat_exchanger_name` or None if not set
        """
        return self._data["Heat Exchanger Name"]

    @heat_exchanger_name.setter
    def heat_exchanger_name(self, value=None):
        """  Corresponds to IDD Field `Heat Exchanger Name`
        Heat exchanger type must be HeatExchanger:AirToAir:SensibleAndLatent

        Args:
            value (str): value for IDD Field `Heat Exchanger Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_exchanger_name`')
        self._data["Heat Exchanger Name"] = value

    @property
    def supply_air_flow_rate(self):
        """Get supply_air_flow_rate

        Returns:
            float: the value of `supply_air_flow_rate` or None if not set
        """
        return self._data["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate`
        This flow rate must match the supply fan's air flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate`')
        self._data["Supply Air Flow Rate"] = value

    @property
    def exhaust_air_flow_rate(self):
        """Get exhaust_air_flow_rate

        Returns:
            float: the value of `exhaust_air_flow_rate` or None if not set
        """
        return self._data["Exhaust Air Flow Rate"]

    @exhaust_air_flow_rate.setter
    def exhaust_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Flow Rate`
        This flow rate must match the supply fan air flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Exhaust Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Exhaust Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `exhaust_air_flow_rate`')
        self._data["Exhaust Air Flow Rate"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`
        Fan type must be Fan:OnOff

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def exhaust_air_fan_name(self):
        """Get exhaust_air_fan_name

        Returns:
            str: the value of `exhaust_air_fan_name` or None if not set
        """
        return self._data["Exhaust Air Fan Name"]

    @exhaust_air_fan_name.setter
    def exhaust_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Fan Name`
        Fan type must be Fan:OnOff

        Args:
            value (str): value for IDD Field `Exhaust Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exhaust_air_fan_name`')
        self._data["Exhaust Air Fan Name"] = value

    @property
    def controller_name(self):
        """Get controller_name

        Returns:
            str: the value of `controller_name` or None if not set
        """
        return self._data["Controller Name"]

    @controller_name.setter
    def controller_name(self, value=None):
        """  Corresponds to IDD Field `Controller Name`
        Enter the name of a ZoneHVAC:EnergyRecoveryVentilator:Controller object.

        Args:
            value (str): value for IDD Field `Controller Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_name`')
        self._data["Controller Name"] = value

    @property
    def ventilation_rate_per_unit_floor_area(self):
        """Get ventilation_rate_per_unit_floor_area

        Returns:
            float: the value of `ventilation_rate_per_unit_floor_area` or None if not set
        """
        return self._data["Ventilation Rate per Unit Floor Area"]

    @ventilation_rate_per_unit_floor_area.setter
    def ventilation_rate_per_unit_floor_area(self, value=None):
        """  Corresponds to IDD Field `Ventilation Rate per Unit Floor Area`
        0.000508 m3/s-m2 corresponds to 0.1 ft3/min-ft2
        Used only when supply and exhaust air flow rates are autosized.

        Args:
            value (float): value for IDD Field `Ventilation Rate per Unit Floor Area`
                Units: m3/s-m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `ventilation_rate_per_unit_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ventilation_rate_per_unit_floor_area`')
        self._data["Ventilation Rate per Unit Floor Area"] = value

    @property
    def ventilation_rate_per_occupant(self):
        """Get ventilation_rate_per_occupant

        Returns:
            float: the value of `ventilation_rate_per_occupant` or None if not set
        """
        return self._data["Ventilation Rate per Occupant"]

    @ventilation_rate_per_occupant.setter
    def ventilation_rate_per_occupant(self, value=None):
        """  Corresponds to IDD Field `Ventilation Rate per Occupant`
        0.00236 m3/s-person corresponds to 5 ft3/min-person
        Used only when supply and exhaust air flow rates are autosized.

        Args:
            value (float): value for IDD Field `Ventilation Rate per Occupant`
                Units: m3/s-person
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `ventilation_rate_per_occupant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ventilation_rate_per_occupant`')
        self._data["Ventilation Rate per Occupant"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

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

class ZoneHvacEnergyRecoveryVentilatorController(object):
    """ Corresponds to IDD object `ZoneHVAC:EnergyRecoveryVentilator:Controller`
        This controller is used exclusively by the ZoneHVAC:EnergyRecoveryVentilator object
        to allow economizer (free cooling) operation when possible.
    
    """
    internal_name = "ZoneHVAC:EnergyRecoveryVentilator:Controller"
    field_count = 13
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:EnergyRecoveryVentilator:Controller`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Temperature High Limit"] = None
        self._data["Temperature Low Limit"] = None
        self._data["Enthalpy High Limit"] = None
        self._data["Dewpoint Temperature Limit"] = None
        self._data["Electronic Enthalpy Limit Curve Name"] = None
        self._data["Exhaust Air Temperature Limit"] = None
        self._data["Exhaust Air Enthalpy Limit"] = None
        self._data["Time of Day Economizer Flow Control Schedule Name"] = None
        self._data["High Humidity Control Flag"] = None
        self._data["Humidistat Control Zone Name"] = None
        self._data["High Humidity Outdoor Air Flow Ratio"] = None
        self._data["Control High Indoor Humidity Based on Outdoor Humidity Ratio"] = None
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
            self.temperature_high_limit = None
        else:
            self.temperature_high_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_low_limit = None
        else:
            self.temperature_low_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enthalpy_high_limit = None
        else:
            self.enthalpy_high_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_limit = None
        else:
            self.dewpoint_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electronic_enthalpy_limit_curve_name = None
        else:
            self.electronic_enthalpy_limit_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_temperature_limit = None
        else:
            self.exhaust_air_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_enthalpy_limit = None
        else:
            self.exhaust_air_enthalpy_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.time_of_day_economizer_flow_control_schedule_name = None
        else:
            self.time_of_day_economizer_flow_control_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_humidity_control_flag = None
        else:
            self.high_humidity_control_flag = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidistat_control_zone_name = None
        else:
            self.humidistat_control_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_humidity_outdoor_air_flow_ratio = None
        else:
            self.high_humidity_outdoor_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = None
        else:
            self.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def temperature_high_limit(self):
        """Get temperature_high_limit

        Returns:
            float: the value of `temperature_high_limit` or None if not set
        """
        return self._data["Temperature High Limit"]

    @temperature_high_limit.setter
    def temperature_high_limit(self, value=None):
        """  Corresponds to IDD Field `Temperature High Limit`
        Enter the maximum outdoor dry-bulb temperature limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `Temperature High Limit`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_high_limit`'.format(value))
        self._data["Temperature High Limit"] = value

    @property
    def temperature_low_limit(self):
        """Get temperature_low_limit

        Returns:
            float: the value of `temperature_low_limit` or None if not set
        """
        return self._data["Temperature Low Limit"]

    @temperature_low_limit.setter
    def temperature_low_limit(self, value=None):
        """  Corresponds to IDD Field `Temperature Low Limit`
        Enter the minimum outdoor dry-bulb temperature limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `Temperature Low Limit`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_low_limit`'.format(value))
        self._data["Temperature Low Limit"] = value

    @property
    def enthalpy_high_limit(self):
        """Get enthalpy_high_limit

        Returns:
            float: the value of `enthalpy_high_limit` or None if not set
        """
        return self._data["Enthalpy High Limit"]

    @enthalpy_high_limit.setter
    def enthalpy_high_limit(self, value=None):
        """  Corresponds to IDD Field `Enthalpy High Limit`
        Enter the maximum outdoor enthalpy limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `Enthalpy High Limit`
                Units: J/kg
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_high_limit`'.format(value))
        self._data["Enthalpy High Limit"] = value

    @property
    def dewpoint_temperature_limit(self):
        """Get dewpoint_temperature_limit

        Returns:
            float: the value of `dewpoint_temperature_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Limit"]

    @dewpoint_temperature_limit.setter
    def dewpoint_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Limit`
        Enter the maximum outdoor dewpoint temperature limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Limit`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_limit`'.format(value))
        self._data["Dewpoint Temperature Limit"] = value

    @property
    def electronic_enthalpy_limit_curve_name(self):
        """Get electronic_enthalpy_limit_curve_name

        Returns:
            str: the value of `electronic_enthalpy_limit_curve_name` or None if not set
        """
        return self._data["Electronic Enthalpy Limit Curve Name"]

    @electronic_enthalpy_limit_curve_name.setter
    def electronic_enthalpy_limit_curve_name(self, value=None):
        """  Corresponds to IDD Field `Electronic Enthalpy Limit Curve Name`
        Table:OneIndependentVariable object can also be used
        Enter the name of a quadratic or cubic curve which defines the maximum outdoor
        humidity ratio (function of outdoor dry-bulb temperature) for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (str): value for IDD Field `Electronic Enthalpy Limit Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `electronic_enthalpy_limit_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electronic_enthalpy_limit_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electronic_enthalpy_limit_curve_name`')
        self._data["Electronic Enthalpy Limit Curve Name"] = value

    @property
    def exhaust_air_temperature_limit(self):
        """Get exhaust_air_temperature_limit

        Returns:
            str: the value of `exhaust_air_temperature_limit` or None if not set
        """
        return self._data["Exhaust Air Temperature Limit"]

    @exhaust_air_temperature_limit.setter
    def exhaust_air_temperature_limit(self, value="NoExhaustAirTemperatureLimit"):
        """  Corresponds to IDD Field `Exhaust Air Temperature Limit`

        Args:
            value (str): value for IDD Field `Exhaust Air Temperature Limit`
                Accepted values are:
                      - ExhaustAirTemperatureLimit
                      - NoExhaustAirTemperatureLimit
                Default value: NoExhaustAirTemperatureLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_temperature_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_temperature_limit`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exhaust_air_temperature_limit`')
            vals = {}
            vals["exhaustairtemperaturelimit"] = "ExhaustAirTemperatureLimit"
            vals["noexhaustairtemperaturelimit"] = "NoExhaustAirTemperatureLimit"
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
                                     'field `exhaust_air_temperature_limit`'.format(value))
            value = vals[value_lower]
        self._data["Exhaust Air Temperature Limit"] = value

    @property
    def exhaust_air_enthalpy_limit(self):
        """Get exhaust_air_enthalpy_limit

        Returns:
            str: the value of `exhaust_air_enthalpy_limit` or None if not set
        """
        return self._data["Exhaust Air Enthalpy Limit"]

    @exhaust_air_enthalpy_limit.setter
    def exhaust_air_enthalpy_limit(self, value="NoExhaustAirEnthalpyLimit"):
        """  Corresponds to IDD Field `Exhaust Air Enthalpy Limit`

        Args:
            value (str): value for IDD Field `Exhaust Air Enthalpy Limit`
                Accepted values are:
                      - ExhaustAirEnthalpyLimit
                      - NoExhaustAirEnthalpyLimit
                Default value: NoExhaustAirEnthalpyLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_enthalpy_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_enthalpy_limit`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exhaust_air_enthalpy_limit`')
            vals = {}
            vals["exhaustairenthalpylimit"] = "ExhaustAirEnthalpyLimit"
            vals["noexhaustairenthalpylimit"] = "NoExhaustAirEnthalpyLimit"
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
                                     'field `exhaust_air_enthalpy_limit`'.format(value))
            value = vals[value_lower]
        self._data["Exhaust Air Enthalpy Limit"] = value

    @property
    def time_of_day_economizer_flow_control_schedule_name(self):
        """Get time_of_day_economizer_flow_control_schedule_name

        Returns:
            str: the value of `time_of_day_economizer_flow_control_schedule_name` or None if not set
        """
        return self._data["Time of Day Economizer Flow Control Schedule Name"]

    @time_of_day_economizer_flow_control_schedule_name.setter
    def time_of_day_economizer_flow_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Time of Day Economizer Flow Control Schedule Name`
        Schedule values greater than 0 indicate economizer operation is active. This
        schedule may be used with or without the High Humidity Control option.
        When used together, high humidity control has priority over economizer control.

        Args:
            value (str): value for IDD Field `Time of Day Economizer Flow Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_of_day_economizer_flow_control_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_of_day_economizer_flow_control_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `time_of_day_economizer_flow_control_schedule_name`')
        self._data["Time of Day Economizer Flow Control Schedule Name"] = value

    @property
    def high_humidity_control_flag(self):
        """Get high_humidity_control_flag

        Returns:
            str: the value of `high_humidity_control_flag` or None if not set
        """
        return self._data["High Humidity Control Flag"]

    @high_humidity_control_flag.setter
    def high_humidity_control_flag(self, value="No"):
        """  Corresponds to IDD Field `High Humidity Control Flag`
        Select Yes to modify air flow rates based on a zone humidistat.
        Select No to disable this feature.

        Args:
            value (str): value for IDD Field `High Humidity Control Flag`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `high_humidity_control_flag`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `high_humidity_control_flag`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `high_humidity_control_flag`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `high_humidity_control_flag`'.format(value))
            value = vals[value_lower]
        self._data["High Humidity Control Flag"] = value

    @property
    def humidistat_control_zone_name(self):
        """Get humidistat_control_zone_name

        Returns:
            str: the value of `humidistat_control_zone_name` or None if not set
        """
        return self._data["Humidistat Control Zone Name"]

    @humidistat_control_zone_name.setter
    def humidistat_control_zone_name(self, value=None):
        """  Corresponds to IDD Field `Humidistat Control Zone Name`
        Enter the name of the zone where the humidistat is located.

        Args:
            value (str): value for IDD Field `Humidistat Control Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `humidistat_control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `humidistat_control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `humidistat_control_zone_name`')
        self._data["Humidistat Control Zone Name"] = value

    @property
    def high_humidity_outdoor_air_flow_ratio(self):
        """Get high_humidity_outdoor_air_flow_ratio

        Returns:
            float: the value of `high_humidity_outdoor_air_flow_ratio` or None if not set
        """
        return self._data["High Humidity Outdoor Air Flow Ratio"]

    @high_humidity_outdoor_air_flow_ratio.setter
    def high_humidity_outdoor_air_flow_ratio(self, value=1.0):
        """  Corresponds to IDD Field `High Humidity Outdoor Air Flow Ratio`
        Enter the ratio of supply (outdoor) air to the maximum supply air flow rate when modified
        air flow rates are active based on high indoor humidity.

        Args:
            value (float): value for IDD Field `High Humidity Outdoor Air Flow Ratio`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_humidity_outdoor_air_flow_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_humidity_outdoor_air_flow_ratio`')
        self._data["High Humidity Outdoor Air Flow Ratio"] = value

    @property
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(self):
        """Get control_high_indoor_humidity_based_on_outdoor_humidity_ratio

        Returns:
            str: the value of `control_high_indoor_humidity_based_on_outdoor_humidity_ratio` or None if not set
        """
        return self._data["Control High Indoor Humidity Based on Outdoor Humidity Ratio"]

    @control_high_indoor_humidity_based_on_outdoor_humidity_ratio.setter
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(self, value="Yes"):
        """  Corresponds to IDD Field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`
        If NO is selected, the air flow rate is modified any time indoor relative
        humidity is above humidistat setpoint. If YES is selected, outdoor air flow
        rate is modified any time indoor relative humidity is above the humidistat
        setpoint AND the outdoor humidity ratio is less than the indoor humidity ratio.

        Args:
            value (str): value for IDD Field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))
            value = vals[value_lower]
        self._data["Control High Indoor Humidity Based on Outdoor Humidity Ratio"] = value

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

class ZoneHvacUnitVentilator(object):
    """ Corresponds to IDD object `ZoneHVAC:UnitVentilator`
        Unit ventilator. Forced-convection ventilation unit with supply fan (constant-volume
        or variable-volume), optional chilled water cooling coil, optional heating coil
        (gas, electric, hot water, or steam) and controllable outdoor air mixer.
    
    """
    internal_name = "ZoneHVAC:UnitVentilator"
    field_count = 25
    required_fields = ["Name", "Maximum Supply Air Flow Rate", "Outdoor Air Control Type", "Minimum Outdoor Air Flow Rate", "Minimum Outdoor Air Schedule Name", "Maximum Outdoor Air Flow Rate", "Maximum Outdoor Air Fraction or Temperature Schedule Name", "Air Inlet Node Name", "Air Outlet Node Name", "Outdoor Air Node Name", "Exhaust Air Node Name", "Mixed Air Node Name", "Supply Air Fan Object Type", "Supply Air Fan Name", "Coil Option"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:UnitVentilator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Maximum Supply Air Flow Rate"] = None
        self._data["Outdoor Air Control Type"] = None
        self._data["Minimum Outdoor Air Flow Rate"] = None
        self._data["Minimum Outdoor Air Schedule Name"] = None
        self._data["Maximum Outdoor Air Flow Rate"] = None
        self._data["Maximum Outdoor Air Fraction or Temperature Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Node Name"] = None
        self._data["Exhaust Air Node Name"] = None
        self._data["Mixed Air Node Name"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Coil Option"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Heating Convergence Tolerance"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Cooling Convergence Tolerance"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_control_type = None
        else:
            self.outdoor_air_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_flow_rate = None
        else:
            self.minimum_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_schedule_name = None
        else:
            self.minimum_outdoor_air_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_fraction_or_temperature_schedule_name = None
        else:
            self.maximum_outdoor_air_fraction_or_temperature_schedule_name = vals[i]
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
            self.mixed_air_node_name = None
        else:
            self.mixed_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coil_option = None
        else:
            self.coil_option = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def maximum_supply_air_flow_rate(self):
        """Get maximum_supply_air_flow_rate

        Returns:
            float: the value of `maximum_supply_air_flow_rate` or None if not set
        """
        return self._data["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_supply_air_flow_rate`')
        self._data["Maximum Supply Air Flow Rate"] = value

    @property
    def outdoor_air_control_type(self):
        """Get outdoor_air_control_type

        Returns:
            str: the value of `outdoor_air_control_type` or None if not set
        """
        return self._data["Outdoor Air Control Type"]

    @outdoor_air_control_type.setter
    def outdoor_air_control_type(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Control Type`

        Args:
            value (str): value for IDD Field `Outdoor Air Control Type`
                Accepted values are:
                      - FixedAmount
                      - VariablePercent
                      - FixedTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_control_type`')
            vals = {}
            vals["fixedamount"] = "FixedAmount"
            vals["variablepercent"] = "VariablePercent"
            vals["fixedtemperature"] = "FixedTemperature"
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
                                     'field `outdoor_air_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Outdoor Air Control Type"] = value

    @property
    def minimum_outdoor_air_flow_rate(self):
        """Get minimum_outdoor_air_flow_rate

        Returns:
            float: the value of `minimum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Minimum Outdoor Air Flow Rate"]

    @minimum_outdoor_air_flow_rate.setter
    def minimum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Minimum Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Outdoor Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Minimum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_outdoor_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_outdoor_air_flow_rate`')
        self._data["Minimum Outdoor Air Flow Rate"] = value

    @property
    def minimum_outdoor_air_schedule_name(self):
        """Get minimum_outdoor_air_schedule_name

        Returns:
            str: the value of `minimum_outdoor_air_schedule_name` or None if not set
        """
        return self._data["Minimum Outdoor Air Schedule Name"]

    @minimum_outdoor_air_schedule_name.setter
    def minimum_outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Outdoor Air Schedule Name`
        schedule values multiply the minimum outdoor air flow rate

        Args:
            value (str): value for IDD Field `Minimum Outdoor Air Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_outdoor_air_schedule_name`')
        self._data["Minimum Outdoor Air Schedule Name"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """Get maximum_outdoor_air_flow_rate

        Returns:
            float: the value of `maximum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_outdoor_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_outdoor_air_flow_rate`')
        self._data["Maximum Outdoor Air Flow Rate"] = value

    @property
    def maximum_outdoor_air_fraction_or_temperature_schedule_name(self):
        """Get maximum_outdoor_air_fraction_or_temperature_schedule_name

        Returns:
            str: the value of `maximum_outdoor_air_fraction_or_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Outdoor Air Fraction or Temperature Schedule Name"]

    @maximum_outdoor_air_fraction_or_temperature_schedule_name.setter
    def maximum_outdoor_air_fraction_or_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Maximum Outdoor Air Fraction or Temperature Schedule Name`
        that this depends on the control type as to whether it is a fraction or temperature

        Args:
            value (str): value for IDD Field `Maximum Outdoor Air Fraction or Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_outdoor_air_fraction_or_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_outdoor_air_fraction_or_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `maximum_outdoor_air_fraction_or_temperature_schedule_name`')
        self._data["Maximum Outdoor Air Fraction or Temperature Schedule Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Outdoor Air Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Exhaust Air Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def mixed_air_node_name(self):
        """Get mixed_air_node_name

        Returns:
            str: the value of `mixed_air_node_name` or None if not set
        """
        return self._data["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Air Node Name`
        inlet to coils

        Args:
            value (str): value for IDD Field `Mixed Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `mixed_air_node_name`')
        self._data["Mixed Air Node Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`
        Allowable fan types are Fan:ConstantVolume, Fan:OnOff and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                      - Fan:VariableVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
            vals["fan:variablevolume"] = "Fan:VariableVolume"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def coil_option(self):
        """Get coil_option

        Returns:
            str: the value of `coil_option` or None if not set
        """
        return self._data["Coil Option"]

    @coil_option.setter
    def coil_option(self, value=None):
        """  Corresponds to IDD Field `Coil Option`

        Args:
            value (str): value for IDD Field `Coil Option`
                Accepted values are:
                      - None
                      - Heating
                      - Cooling
                      - HeatingAndCooling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `coil_option`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `coil_option`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `coil_option`')
            vals = {}
            vals["none"] = "None"
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["heatingandcooling"] = "HeatingAndCooling"
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
                                     'field `coil_option`'.format(value))
            value = vals[value_lower]
        self._data["Coil Option"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule that controls fan operation. Schedule
        name values of 0 denote cycling fan operation (fan cycles with
        cooling/heating coil). Schedule values greater than 0 denote
        constant fan operation (fan runs continually regardless of coil
        operation). The fan operating mode defaults to cycling fan operation
        if this input field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Heating Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_convergence_tolerance`')
        self._data["Heating Convergence Tolerance"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatExchangerAssisted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatExchangerAssisted"
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
                                     'field `cooling_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Cooling Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_name`')
        self._data["Cooling Coil Name"] = value

    @property
    def cooling_convergence_tolerance(self):
        """Get cooling_convergence_tolerance

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set
        """
        return self._data["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Cooling Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cooling_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_convergence_tolerance`')
        self._data["Cooling Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacUnitHeater(object):
    """ Corresponds to IDD object `ZoneHVAC:UnitHeater`
        Unit heater. Forced-convection heating-only unit with supply fan, heating coil
        (gas, electric, hot water, or steam) and fixed-position outdoor air mixer.
    
    """
    internal_name = "ZoneHVAC:UnitHeater"
    field_count = 16
    required_fields = ["Name", "Availability Schedule Name", "Supply Air Fan Object Type", "Supply Air Fan Name", "Maximum Supply Air Flow Rate", "Heating Coil Object Type", "Heating Coil Name", "Supply Air Fan Operation During No Heating"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:UnitHeater`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Maximum Supply Air Flow Rate"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Supply Air Fan Operation During No Heating"] = None
        self._data["Maximum Hot Water or Steam Flow Rate"] = None
        self._data["Minimum Hot Water or Steam Flow Rate"] = None
        self._data["Heating Convergence Tolerance"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_operation_during_no_heating = None
        else:
            self.supply_air_fan_operation_during_no_heating = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`
        Allowable fan types are Fan:ConstantVolume, Fan:OnOff and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                      - Fan:VariableVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
            vals["fan:variablevolume"] = "Fan:VariableVolume"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def maximum_supply_air_flow_rate(self):
        """Get maximum_supply_air_flow_rate

        Returns:
            float: the value of `maximum_supply_air_flow_rate` or None if not set
        """
        return self._data["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_supply_air_flow_rate`')
        self._data["Maximum Supply Air Flow Rate"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule that controls fan operation. Schedule
        name values of 0 denote cycling fan operation (fan cycles with the
        heating coil). Schedule values greater than 0 denote constant fan
        operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this
        input field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def supply_air_fan_operation_during_no_heating(self):
        """Get supply_air_fan_operation_during_no_heating

        Returns:
            str: the value of `supply_air_fan_operation_during_no_heating` or None if not set
        """
        return self._data["Supply Air Fan Operation During No Heating"]

    @supply_air_fan_operation_during_no_heating.setter
    def supply_air_fan_operation_during_no_heating(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operation During No Heating`
        This choice field allows the user to define how the unit heater will operate
        under no heating load or cooling conditions. If the No is selected, then
        the fan will not run unless there is a heating load. If the fan does not run,
        this effectively shuts the unit heater system off when there is no heating load.
        If the Yes is selected, the unit heater is available and has a ConstantVolume
        fan, or has an OnOff fan with Supply Air Fan Operating Mode Schedule value
        greater than zero, then the fan will always run regardless of the zone load.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operation During No Heating`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operation_during_no_heating`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operation_during_no_heating`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operation_during_no_heating`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `supply_air_fan_operation_during_no_heating`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Operation During No Heating"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """Get maximum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `maximum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water or Steam Flow Rate`
        Not used when heating coil is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_or_steam_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_hot_water_or_steam_flow_rate`')
        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water or Steam Flow Rate`
        Not used when heating coil is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_or_steam_flow_rate`')
        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Heating Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_convergence_tolerance`')
        self._data["Heating Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacEvaporativeCoolerUnit(object):
    """ Corresponds to IDD object `ZoneHVAC:EvaporativeCoolerUnit`
        Zone evaporative cooler. Forced-convection cooling-only unit with supply fan,
        100% outdoor air supply.  Optional relief exaust node
    
    """
    internal_name = "ZoneHVAC:EvaporativeCoolerUnit"
    field_count = 18
    required_fields = ["Name", "Availability Schedule Name", "Outdoor Air Inlet Node Name", "Cooler Outlet Node Name", "Supply Air Fan Object Type", "Supply Air Fan Name", "Design Supply Air Flow Rate", "Fan Placement", "Cooler Unit Control Method", "First Evaporative Cooler Object Type", "First Evaporative Cooler Object Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:EvaporativeCoolerUnit`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Cooler Outlet Node Name"] = None
        self._data["Zone Relief Air Node Name"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Design Supply Air Flow Rate"] = None
        self._data["Fan Placement"] = None
        self._data["Cooler Unit Control Method"] = None
        self._data["Throttling Range Temperature Difference"] = None
        self._data["Cooling Load Control Threshold Heat Transfer Rate"] = None
        self._data["First Evaporative Cooler Object Type"] = None
        self._data["First Evaporative Cooler Object Name"] = None
        self._data["Second Evaporative Cooler Object Type"] = None
        self._data["Second Evaporative Cooler Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
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
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooler_outlet_node_name = None
        else:
            self.cooler_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_relief_air_node_name = None
        else:
            self.zone_relief_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate = None
        else:
            self.design_supply_air_flow_rate = vals[i]
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
            self.cooler_unit_control_method = None
        else:
            self.cooler_unit_control_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.throttling_range_temperature_difference = None
        else:
            self.throttling_range_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_load_control_threshold_heat_transfer_rate = None
        else:
            self.cooling_load_control_threshold_heat_transfer_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.first_evaporative_cooler_object_type = None
        else:
            self.first_evaporative_cooler_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.first_evaporative_cooler_object_name = None
        else:
            self.first_evaporative_cooler_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.second_evaporative_cooler_object_type = None
        else:
            self.second_evaporative_cooler_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.second_evaporative_cooler_name = None
        else:
            self.second_evaporative_cooler_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        this is an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def cooler_outlet_node_name(self):
        """Get cooler_outlet_node_name

        Returns:
            str: the value of `cooler_outlet_node_name` or None if not set
        """
        return self._data["Cooler Outlet Node Name"]

    @cooler_outlet_node_name.setter
    def cooler_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cooler Outlet Node Name`
        this is a zone inlet node

        Args:
            value (str): value for IDD Field `Cooler Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooler_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooler_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooler_outlet_node_name`')
        self._data["Cooler Outlet Node Name"] = value

    @property
    def zone_relief_air_node_name(self):
        """Get zone_relief_air_node_name

        Returns:
            str: the value of `zone_relief_air_node_name` or None if not set
        """
        return self._data["Zone Relief Air Node Name"]

    @zone_relief_air_node_name.setter
    def zone_relief_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Relief Air Node Name`
        this is a zone exhaust node, optional if flow is being balanced elsewhere

        Args:
            value (str): value for IDD Field `Zone Relief Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_relief_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_relief_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_relief_air_node_name`')
        self._data["Zone Relief Air Node Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:ConstantVolume
                      - Fan:OnOff
                      - Fan:VariableVolume
                      - Fan:ComponentModel
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:variablevolume"] = "Fan:VariableVolume"
            vals["fan:componentmodel"] = "Fan:ComponentModel"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_name`')
        self._data["Supply Air Fan Name"] = value

    @property
    def design_supply_air_flow_rate(self):
        """Get design_supply_air_flow_rate

        Returns:
            float: the value of `design_supply_air_flow_rate` or None if not set
        """
        return self._data["Design Supply Air Flow Rate"]

    @design_supply_air_flow_rate.setter
    def design_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Supply Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_supply_air_flow_rate`')
        self._data["Design Supply Air Flow Rate"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value=None):
        """  Corresponds to IDD Field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def cooler_unit_control_method(self):
        """Get cooler_unit_control_method

        Returns:
            str: the value of `cooler_unit_control_method` or None if not set
        """
        return self._data["Cooler Unit Control Method"]

    @cooler_unit_control_method.setter
    def cooler_unit_control_method(self, value=None):
        """  Corresponds to IDD Field `Cooler Unit Control Method`

        Args:
            value (str): value for IDD Field `Cooler Unit Control Method`
                Accepted values are:
                      - ZoneTemperatureDeadbandOnOffCycling
                      - ZoneCoolingLoadOnOffCycling
                      - ZoneCoolingLoadVariableSpeedFan
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooler_unit_control_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooler_unit_control_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooler_unit_control_method`')
            vals = {}
            vals["zonetemperaturedeadbandonoffcycling"] = "ZoneTemperatureDeadbandOnOffCycling"
            vals["zonecoolingloadonoffcycling"] = "ZoneCoolingLoadOnOffCycling"
            vals["zonecoolingloadvariablespeedfan"] = "ZoneCoolingLoadVariableSpeedFan"
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
                                     'field `cooler_unit_control_method`'.format(value))
            value = vals[value_lower]
        self._data["Cooler Unit Control Method"] = value

    @property
    def throttling_range_temperature_difference(self):
        """Get throttling_range_temperature_difference

        Returns:
            float: the value of `throttling_range_temperature_difference` or None if not set
        """
        return self._data["Throttling Range Temperature Difference"]

    @throttling_range_temperature_difference.setter
    def throttling_range_temperature_difference(self, value=1.0):
        """  Corresponds to IDD Field `Throttling Range Temperature Difference`
        used for ZoneTemperatureDeadbandOnOffCycling hystersis range for thermostatic control

        Args:
            value (float): value for IDD Field `Throttling Range Temperature Difference`
                Units: deltaC
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `throttling_range_temperature_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `throttling_range_temperature_difference`')
        self._data["Throttling Range Temperature Difference"] = value

    @property
    def cooling_load_control_threshold_heat_transfer_rate(self):
        """Get cooling_load_control_threshold_heat_transfer_rate

        Returns:
            float: the value of `cooling_load_control_threshold_heat_transfer_rate` or None if not set
        """
        return self._data["Cooling Load Control Threshold Heat Transfer Rate"]

    @cooling_load_control_threshold_heat_transfer_rate.setter
    def cooling_load_control_threshold_heat_transfer_rate(self, value=100.0):
        """  Corresponds to IDD Field `Cooling Load Control Threshold Heat Transfer Rate`
        Sign convention is that positive values indicate a cooling load

        Args:
            value (float): value for IDD Field `Cooling Load Control Threshold Heat Transfer Rate`
                Units: W
                Default value: 100.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cooling_load_control_threshold_heat_transfer_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_load_control_threshold_heat_transfer_rate`')
        self._data["Cooling Load Control Threshold Heat Transfer Rate"] = value

    @property
    def first_evaporative_cooler_object_type(self):
        """Get first_evaporative_cooler_object_type

        Returns:
            str: the value of `first_evaporative_cooler_object_type` or None if not set
        """
        return self._data["First Evaporative Cooler Object Type"]

    @first_evaporative_cooler_object_type.setter
    def first_evaporative_cooler_object_type(self, value=None):
        """  Corresponds to IDD Field `First Evaporative Cooler Object Type`

        Args:
            value (str): value for IDD Field `First Evaporative Cooler Object Type`
                Accepted values are:
                      - EvaporativeCooler:Direct:CelDekPad
                      - EvaporativeCooler:Direct:ResearchSpecial
                      - EvaporativeCooler:Indirect:CelDekPad
                      - EvaporativeCooler:Indirect:WetCoil
                      - EvaporativeCooler:Indirect:ResearchSpecial
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `first_evaporative_cooler_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `first_evaporative_cooler_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `first_evaporative_cooler_object_type`')
            vals = {}
            vals["evaporativecooler:direct:celdekpad"] = "EvaporativeCooler:Direct:CelDekPad"
            vals["evaporativecooler:direct:researchspecial"] = "EvaporativeCooler:Direct:ResearchSpecial"
            vals["evaporativecooler:indirect:celdekpad"] = "EvaporativeCooler:Indirect:CelDekPad"
            vals["evaporativecooler:indirect:wetcoil"] = "EvaporativeCooler:Indirect:WetCoil"
            vals["evaporativecooler:indirect:researchspecial"] = "EvaporativeCooler:Indirect:ResearchSpecial"
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
                                     'field `first_evaporative_cooler_object_type`'.format(value))
            value = vals[value_lower]
        self._data["First Evaporative Cooler Object Type"] = value

    @property
    def first_evaporative_cooler_object_name(self):
        """Get first_evaporative_cooler_object_name

        Returns:
            str: the value of `first_evaporative_cooler_object_name` or None if not set
        """
        return self._data["First Evaporative Cooler Object Name"]

    @first_evaporative_cooler_object_name.setter
    def first_evaporative_cooler_object_name(self, value=None):
        """  Corresponds to IDD Field `First Evaporative Cooler Object Name`

        Args:
            value (str): value for IDD Field `First Evaporative Cooler Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `first_evaporative_cooler_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `first_evaporative_cooler_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `first_evaporative_cooler_object_name`')
        self._data["First Evaporative Cooler Object Name"] = value

    @property
    def second_evaporative_cooler_object_type(self):
        """Get second_evaporative_cooler_object_type

        Returns:
            str: the value of `second_evaporative_cooler_object_type` or None if not set
        """
        return self._data["Second Evaporative Cooler Object Type"]

    @second_evaporative_cooler_object_type.setter
    def second_evaporative_cooler_object_type(self, value=None):
        """  Corresponds to IDD Field `Second Evaporative Cooler Object Type`
        optional, used for direct/indirect configurations
        second cooler must be immediately downstream of first cooler, if present

        Args:
            value (str): value for IDD Field `Second Evaporative Cooler Object Type`
                Accepted values are:
                      - EvaporativeCooler:Direct:CelDekPad
                      - EvaporativeCooler:Direct:ResearchSpecial
                      - EvaporativeCooler:Indirect:CelDekPad
                      - EvaporativeCooler:Indirect:WetCoil
                      - EvaporativeCooler:Indirect:ResearchSpecial
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `second_evaporative_cooler_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `second_evaporative_cooler_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `second_evaporative_cooler_object_type`')
            vals = {}
            vals["evaporativecooler:direct:celdekpad"] = "EvaporativeCooler:Direct:CelDekPad"
            vals["evaporativecooler:direct:researchspecial"] = "EvaporativeCooler:Direct:ResearchSpecial"
            vals["evaporativecooler:indirect:celdekpad"] = "EvaporativeCooler:Indirect:CelDekPad"
            vals["evaporativecooler:indirect:wetcoil"] = "EvaporativeCooler:Indirect:WetCoil"
            vals["evaporativecooler:indirect:researchspecial"] = "EvaporativeCooler:Indirect:ResearchSpecial"
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
                                     'field `second_evaporative_cooler_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Second Evaporative Cooler Object Type"] = value

    @property
    def second_evaporative_cooler_name(self):
        """Get second_evaporative_cooler_name

        Returns:
            str: the value of `second_evaporative_cooler_name` or None if not set
        """
        return self._data["Second Evaporative Cooler Name"]

    @second_evaporative_cooler_name.setter
    def second_evaporative_cooler_name(self, value=None):
        """  Corresponds to IDD Field `Second Evaporative Cooler Name`
        optional, used for direct/indirect configurations

        Args:
            value (str): value for IDD Field `Second Evaporative Cooler Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `second_evaporative_cooler_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `second_evaporative_cooler_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `second_evaporative_cooler_name`')
        self._data["Second Evaporative Cooler Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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

class ZoneHvacOutdoorAirUnit(object):
    """ Corresponds to IDD object `ZoneHVAC:OutdoorAirUnit`
        The zone outdoor air unit models a single-zone dedicated outdoor air system (DOAS).
        Forced-convection 100% outdoor air unit with supply fan and optional equipment
        including exhaust fan, heating coil, cooling coil, and heat recovery.
    
    """
    internal_name = "ZoneHVAC:OutdoorAirUnit"
    field_count = 19
    required_fields = ["Name", "Zone Name", "Outdoor Air Flow Rate", "Outdoor Air Schedule Name", "Supply Fan Name", "Supply Fan Placement", "Unit Control Type", "Outdoor Air Node Name", "AirOutlet Node Name", "Supply FanOutlet Node Name", "Outdoor Air Unit List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:OutdoorAirUnit`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Outdoor Air Flow Rate"] = None
        self._data["Outdoor Air Schedule Name"] = None
        self._data["Supply Fan Name"] = None
        self._data["Supply Fan Placement"] = None
        self._data["Exhaust Fan Name"] = None
        self._data["Exhaust Air Flow Rate"] = None
        self._data["Exhaust Air Schedule Name"] = None
        self._data["Unit Control Type"] = None
        self._data["High Air Control Temperature Schedule Name"] = None
        self._data["Low Air Control Temperature Schedule Name"] = None
        self._data["Outdoor Air Node Name"] = None
        self._data["AirOutlet Node Name"] = None
        self._data["AirInlet Node Name"] = None
        self._data["Supply FanOutlet Node Name"] = None
        self._data["Outdoor Air Unit List Name"] = None
        self._data["Availability Manager List Name"] = None
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate = None
        else:
            self.outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_schedule_name = None
        else:
            self.outdoor_air_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_fan_name = None
        else:
            self.supply_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_fan_placement = None
        else:
            self.supply_fan_placement = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_fan_name = None
        else:
            self.exhaust_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_flow_rate = None
        else:
            self.exhaust_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_schedule_name = None
        else:
            self.exhaust_air_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.unit_control_type = None
        else:
            self.unit_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_air_control_temperature_schedule_name = None
        else:
            self.high_air_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_air_control_temperature_schedule_name = None
        else:
            self.low_air_control_temperature_schedule_name = vals[i]
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
            self.airoutlet_node_name = None
        else:
            self.airoutlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.airinlet_node_name = None
        else:
            self.airinlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_fanoutlet_node_name = None
        else:
            self.supply_fanoutlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_unit_list_name = None
        else:
            self.outdoor_air_unit_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        (name of zone system is serving)

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def outdoor_air_flow_rate(self):
        """Get outdoor_air_flow_rate

        Returns:
            float: the value of `outdoor_air_flow_rate` or None if not set
        """
        return self._data["Outdoor Air Flow Rate"]

    @outdoor_air_flow_rate.setter
    def outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `outdoor_air_flow_rate`')
        self._data["Outdoor Air Flow Rate"] = value

    @property
    def outdoor_air_schedule_name(self):
        """Get outdoor_air_schedule_name

        Returns:
            str: the value of `outdoor_air_schedule_name` or None if not set
        """
        return self._data["Outdoor Air Schedule Name"]

    @outdoor_air_schedule_name.setter
    def outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Schedule Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_schedule_name`')
        self._data["Outdoor Air Schedule Name"] = value

    @property
    def supply_fan_name(self):
        """Get supply_fan_name

        Returns:
            str: the value of `supply_fan_name` or None if not set
        """
        return self._data["Supply Fan Name"]

    @supply_fan_name.setter
    def supply_fan_name(self, value=None):
        """  Corresponds to IDD Field `Supply Fan Name`
        Allowable fan types are Fan:ConstantVolume and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Supply Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_fan_name`')
        self._data["Supply Fan Name"] = value

    @property
    def supply_fan_placement(self):
        """Get supply_fan_placement

        Returns:
            str: the value of `supply_fan_placement` or None if not set
        """
        return self._data["Supply Fan Placement"]

    @supply_fan_placement.setter
    def supply_fan_placement(self, value="DrawThrough"):
        """  Corresponds to IDD Field `Supply Fan Placement`

        Args:
            value (str): value for IDD Field `Supply Fan Placement`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_placement`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_fan_placement`')
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
                                     'field `supply_fan_placement`'.format(value))
            value = vals[value_lower]
        self._data["Supply Fan Placement"] = value

    @property
    def exhaust_fan_name(self):
        """Get exhaust_fan_name

        Returns:
            str: the value of `exhaust_fan_name` or None if not set
        """
        return self._data["Exhaust Fan Name"]

    @exhaust_fan_name.setter
    def exhaust_fan_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Fan Name`
        Allowable fan types are Fan:ConstantVolume and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Exhaust Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exhaust_fan_name`')
        self._data["Exhaust Fan Name"] = value

    @property
    def exhaust_air_flow_rate(self):
        """Get exhaust_air_flow_rate

        Returns:
            float: the value of `exhaust_air_flow_rate` or None if not set
        """
        return self._data["Exhaust Air Flow Rate"]

    @exhaust_air_flow_rate.setter
    def exhaust_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Exhaust Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Exhaust Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_flow_rate`'.format(value))
        self._data["Exhaust Air Flow Rate"] = value

    @property
    def exhaust_air_schedule_name(self):
        """Get exhaust_air_schedule_name

        Returns:
            str: the value of `exhaust_air_schedule_name` or None if not set
        """
        return self._data["Exhaust Air Schedule Name"]

    @exhaust_air_schedule_name.setter
    def exhaust_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Schedule Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exhaust_air_schedule_name`')
        self._data["Exhaust Air Schedule Name"] = value

    @property
    def unit_control_type(self):
        """Get unit_control_type

        Returns:
            str: the value of `unit_control_type` or None if not set
        """
        return self._data["Unit Control Type"]

    @unit_control_type.setter
    def unit_control_type(self, value="NeutralControl"):
        """  Corresponds to IDD Field `Unit Control Type`

        Args:
            value (str): value for IDD Field `Unit Control Type`
                Accepted values are:
                      - NeutralControl
                      - TemperatureControl
                Default value: NeutralControl
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `unit_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unit_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `unit_control_type`')
            vals = {}
            vals["neutralcontrol"] = "NeutralControl"
            vals["temperaturecontrol"] = "TemperatureControl"
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
                                     'field `unit_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Unit Control Type"] = value

    @property
    def high_air_control_temperature_schedule_name(self):
        """Get high_air_control_temperature_schedule_name

        Returns:
            str: the value of `high_air_control_temperature_schedule_name` or None if not set
        """
        return self._data["High Air Control Temperature Schedule Name"]

    @high_air_control_temperature_schedule_name.setter
    def high_air_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `High Air Control Temperature Schedule Name`
        Air and control temperatures for cooling. If outdoor air temperature
        is above the high air control temperature, then the zone inlet air temperature
        is set to the high air control temperature. If the outdoor air is between high and low
        air control temperature, then there is no cooling/heating requirements.

        Args:
            value (str): value for IDD Field `High Air Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `high_air_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `high_air_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `high_air_control_temperature_schedule_name`')
        self._data["High Air Control Temperature Schedule Name"] = value

    @property
    def low_air_control_temperature_schedule_name(self):
        """Get low_air_control_temperature_schedule_name

        Returns:
            str: the value of `low_air_control_temperature_schedule_name` or None if not set
        """
        return self._data["Low Air Control Temperature Schedule Name"]

    @low_air_control_temperature_schedule_name.setter
    def low_air_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Low Air Control Temperature Schedule Name`
        Air and control temperatures for Heating. If outdoor air temperature
        is below the low air control temperature, then the zone inlet air temperature
        is set to the low air control temperature. If the outdoor air is between high and low
        air control temperature, then there is no cooling/heating requirements.

        Args:
            value (str): value for IDD Field `Low Air Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `low_air_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `low_air_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `low_air_control_temperature_schedule_name`')
        self._data["Low Air Control Temperature Schedule Name"] = value

    @property
    def outdoor_air_node_name(self):
        """Get outdoor_air_node_name

        Returns:
            str: the value of `outdoor_air_node_name` or None if not set
        """
        return self._data["Outdoor Air Node Name"]

    @outdoor_air_node_name.setter
    def outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def airoutlet_node_name(self):
        """Get airoutlet_node_name

        Returns:
            str: the value of `airoutlet_node_name` or None if not set
        """
        return self._data["AirOutlet Node Name"]

    @airoutlet_node_name.setter
    def airoutlet_node_name(self, value=None):
        """  Corresponds to IDD Field `AirOutlet Node Name`

        Args:
            value (str): value for IDD Field `AirOutlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `airoutlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airoutlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `airoutlet_node_name`')
        self._data["AirOutlet Node Name"] = value

    @property
    def airinlet_node_name(self):
        """Get airinlet_node_name

        Returns:
            str: the value of `airinlet_node_name` or None if not set
        """
        return self._data["AirInlet Node Name"]

    @airinlet_node_name.setter
    def airinlet_node_name(self, value=None):
        """  Corresponds to IDD Field `AirInlet Node Name`
        air leaves zone

        Args:
            value (str): value for IDD Field `AirInlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `airinlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airinlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `airinlet_node_name`')
        self._data["AirInlet Node Name"] = value

    @property
    def supply_fanoutlet_node_name(self):
        """Get supply_fanoutlet_node_name

        Returns:
            str: the value of `supply_fanoutlet_node_name` or None if not set
        """
        return self._data["Supply FanOutlet Node Name"]

    @supply_fanoutlet_node_name.setter
    def supply_fanoutlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply FanOutlet Node Name`

        Args:
            value (str): value for IDD Field `Supply FanOutlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fanoutlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fanoutlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_fanoutlet_node_name`')
        self._data["Supply FanOutlet Node Name"] = value

    @property
    def outdoor_air_unit_list_name(self):
        """Get outdoor_air_unit_list_name

        Returns:
            str: the value of `outdoor_air_unit_list_name` or None if not set
        """
        return self._data["Outdoor Air Unit List Name"]

    @outdoor_air_unit_list_name.setter
    def outdoor_air_unit_list_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Unit List Name`
        Enter the name of an ZoneHVAC:OutdoorAirUnit:EquipmentList object.

        Args:
            value (str): value for IDD Field `Outdoor Air Unit List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_unit_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_unit_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_unit_list_name`')
        self._data["Outdoor Air Unit List Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

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

class ZoneHvacOutdoorAirUnitEquipmentList(object):
    """ Corresponds to IDD object `ZoneHVAC:OutdoorAirUnit:EquipmentList`
        Equipment list for components in a ZoneHVAC:OutdoorAirUnit. Components are simulated
        sequentially in the order given in the equipment list.
    
    """
    internal_name = "ZoneHVAC:OutdoorAirUnit:EquipmentList"
    field_count = 17
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:OutdoorAirUnit:EquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Component 1 Object Type"] = None
        self._data["Component 1 Name"] = None
        self._data["Component 2 Object Type"] = None
        self._data["Component 2 Name"] = None
        self._data["Component 3 Object Type"] = None
        self._data["Component 3 Name"] = None
        self._data["Component 4 Object Type"] = None
        self._data["Component 4 Name"] = None
        self._data["Component 5 Object Type"] = None
        self._data["Component 5 Name"] = None
        self._data["Component 6 Object Type"] = None
        self._data["Component 6 Name"] = None
        self._data["Component 7 Object Type"] = None
        self._data["Component 7 Name"] = None
        self._data["Component 8 Object Type"] = None
        self._data["Component 8 Name"] = None
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
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
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
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def component_1_object_type(self):
        """Get component_1_object_type

        Returns:
            str: the value of `component_1_object_type` or None if not set
        """
        return self._data["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 1 Object Type`

        Args:
            value (str): value for IDD Field `Component 1 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_1_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 1 Object Type"] = value

    @property
    def component_1_name(self):
        """Get component_1_name

        Returns:
            str: the value of `component_1_name` or None if not set
        """
        return self._data["Component 1 Name"]

    @component_1_name.setter
    def component_1_name(self, value=None):
        """  Corresponds to IDD Field `Component 1 Name`

        Args:
            value (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_name`')
        self._data["Component 1 Name"] = value

    @property
    def component_2_object_type(self):
        """Get component_2_object_type

        Returns:
            str: the value of `component_2_object_type` or None if not set
        """
        return self._data["Component 2 Object Type"]

    @component_2_object_type.setter
    def component_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 2 Object Type`

        Args:
            value (str): value for IDD Field `Component 2 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_2_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 2 Object Type"] = value

    @property
    def component_2_name(self):
        """Get component_2_name

        Returns:
            str: the value of `component_2_name` or None if not set
        """
        return self._data["Component 2 Name"]

    @component_2_name.setter
    def component_2_name(self, value=None):
        """  Corresponds to IDD Field `Component 2 Name`

        Args:
            value (str): value for IDD Field `Component 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_name`')
        self._data["Component 2 Name"] = value

    @property
    def component_3_object_type(self):
        """Get component_3_object_type

        Returns:
            str: the value of `component_3_object_type` or None if not set
        """
        return self._data["Component 3 Object Type"]

    @component_3_object_type.setter
    def component_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 3 Object Type`

        Args:
            value (str): value for IDD Field `Component 3 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_3_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 3 Object Type"] = value

    @property
    def component_3_name(self):
        """Get component_3_name

        Returns:
            str: the value of `component_3_name` or None if not set
        """
        return self._data["Component 3 Name"]

    @component_3_name.setter
    def component_3_name(self, value=None):
        """  Corresponds to IDD Field `Component 3 Name`

        Args:
            value (str): value for IDD Field `Component 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_name`')
        self._data["Component 3 Name"] = value

    @property
    def component_4_object_type(self):
        """Get component_4_object_type

        Returns:
            str: the value of `component_4_object_type` or None if not set
        """
        return self._data["Component 4 Object Type"]

    @component_4_object_type.setter
    def component_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 4 Object Type`

        Args:
            value (str): value for IDD Field `Component 4 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_4_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 4 Object Type"] = value

    @property
    def component_4_name(self):
        """Get component_4_name

        Returns:
            str: the value of `component_4_name` or None if not set
        """
        return self._data["Component 4 Name"]

    @component_4_name.setter
    def component_4_name(self, value=None):
        """  Corresponds to IDD Field `Component 4 Name`

        Args:
            value (str): value for IDD Field `Component 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_name`')
        self._data["Component 4 Name"] = value

    @property
    def component_5_object_type(self):
        """Get component_5_object_type

        Returns:
            str: the value of `component_5_object_type` or None if not set
        """
        return self._data["Component 5 Object Type"]

    @component_5_object_type.setter
    def component_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 5 Object Type`

        Args:
            value (str): value for IDD Field `Component 5 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_5_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 5 Object Type"] = value

    @property
    def component_5_name(self):
        """Get component_5_name

        Returns:
            str: the value of `component_5_name` or None if not set
        """
        return self._data["Component 5 Name"]

    @component_5_name.setter
    def component_5_name(self, value=None):
        """  Corresponds to IDD Field `Component 5 Name`

        Args:
            value (str): value for IDD Field `Component 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_name`')
        self._data["Component 5 Name"] = value

    @property
    def component_6_object_type(self):
        """Get component_6_object_type

        Returns:
            str: the value of `component_6_object_type` or None if not set
        """
        return self._data["Component 6 Object Type"]

    @component_6_object_type.setter
    def component_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 6 Object Type`

        Args:
            value (str): value for IDD Field `Component 6 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_6_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 6 Object Type"] = value

    @property
    def component_6_name(self):
        """Get component_6_name

        Returns:
            str: the value of `component_6_name` or None if not set
        """
        return self._data["Component 6 Name"]

    @component_6_name.setter
    def component_6_name(self, value=None):
        """  Corresponds to IDD Field `Component 6 Name`

        Args:
            value (str): value for IDD Field `Component 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_name`')
        self._data["Component 6 Name"] = value

    @property
    def component_7_object_type(self):
        """Get component_7_object_type

        Returns:
            str: the value of `component_7_object_type` or None if not set
        """
        return self._data["Component 7 Object Type"]

    @component_7_object_type.setter
    def component_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 7 Object Type`

        Args:
            value (str): value for IDD Field `Component 7 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_7_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 7 Object Type"] = value

    @property
    def component_7_name(self):
        """Get component_7_name

        Returns:
            str: the value of `component_7_name` or None if not set
        """
        return self._data["Component 7 Name"]

    @component_7_name.setter
    def component_7_name(self, value=None):
        """  Corresponds to IDD Field `Component 7 Name`

        Args:
            value (str): value for IDD Field `Component 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_name`')
        self._data["Component 7 Name"] = value

    @property
    def component_8_object_type(self):
        """Get component_8_object_type

        Returns:
            str: the value of `component_8_object_type` or None if not set
        """
        return self._data["Component 8 Object Type"]

    @component_8_object_type.setter
    def component_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 8 Object Type`

        Args:
            value (str): value for IDD Field `Component 8 Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                      - Coil:Heating:Water
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatexchangerAssisted
                      - CoilSystem:Cooling:DX
                      - CoilSystem:Heating:DX
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - Dehumidifier:Desiccant:NoFans
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatexchangerAssisted"
            vals["coilsystem:cooling:dx"] = "CoilSystem:Cooling:DX"
            vals["coilsystem:heating:dx"] = "CoilSystem:Heating:DX"
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["dehumidifier:desiccant:nofans"] = "Dehumidifier:Desiccant:NoFans"
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
                                     'field `component_8_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Component 8 Object Type"] = value

    @property
    def component_8_name(self):
        """Get component_8_name

        Returns:
            str: the value of `component_8_name` or None if not set
        """
        return self._data["Component 8 Name"]

    @component_8_name.setter
    def component_8_name(self, value=None):
        """  Corresponds to IDD Field `Component 8 Name`

        Args:
            value (str): value for IDD Field `Component 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_name`')
        self._data["Component 8 Name"] = value

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

class ZoneHvacTerminalUnitVariableRefrigerantFlow(object):
    """ Corresponds to IDD object `ZoneHVAC:TerminalUnit:VariableRefrigerantFlow`
        Zone terminal unit with variable refrigerant flow (VRF) DX cooling and heating coils
        (air-to-air heat pump). The VRF terminal units are served by an
        AirConditioner:VariableRefrigerantFlow system.
    
    """
    internal_name = "ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"
    field_count = 26
    required_fields = ["Zone Terminal Unit Name", "Terminal Unit Air Inlet Node Name", "Terminal Unit Air Outlet Node Name", "Supply Air Fan Operating Mode Schedule Name", "Supply Air Fan Object Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:TerminalUnit:VariableRefrigerantFlow`
        """
        self._data = OrderedDict()
        self._data["Zone Terminal Unit Name"] = None
        self._data["Terminal Unit Availability Schedule"] = None
        self._data["Terminal Unit Air Inlet Node Name"] = None
        self._data["Terminal Unit Air Outlet Node Name"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate When No Cooling is Needed"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate When No Heating is Needed"] = None
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = None
        self._data["Outdoor Air Flow Rate During Heating Operation"] = None
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Supply Air Fan Placement"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Object Name"] = None
        self._data["Outside Air Mixer Object Type"] = None
        self._data["Outside Air Mixer Object Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Object Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Object Name"] = None
        self._data["Zone Terminal Unit On Parasitic Electric Energy Use"] = None
        self._data["Zone Terminal Unit Off Parasitic Electric Energy Use"] = None
        self._data["Rated Heating Capacity Sizing Ratio"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name = None
        else:
            self.zone_terminal_unit_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_availability_schedule = None
        else:
            self.terminal_unit_availability_schedule = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_air_inlet_node_name = None
        else:
            self.terminal_unit_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_air_outlet_node_name = None
        else:
            self.terminal_unit_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_placement = None
        else:
            self.supply_air_fan_placement = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_fan_object_name = None
        else:
            self.supply_air_fan_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_air_mixer_object_type = None
        else:
            self.outside_air_mixer_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_air_mixer_object_name = None
        else:
            self.outside_air_mixer_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_name = None
        else:
            self.cooling_coil_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_name = None
        else:
            self.heating_coil_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_on_parasitic_electric_energy_use = None
        else:
            self.zone_terminal_unit_on_parasitic_electric_energy_use = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_off_parasitic_electric_energy_use = None
        else:
            self.zone_terminal_unit_off_parasitic_electric_energy_use = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_heating_capacity_sizing_ratio = None
        else:
            self.rated_heating_capacity_sizing_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_terminal_unit_name(self):
        """Get zone_terminal_unit_name

        Returns:
            str: the value of `zone_terminal_unit_name` or None if not set
        """
        return self._data["Zone Terminal Unit Name"]

    @zone_terminal_unit_name.setter
    def zone_terminal_unit_name(self, value=None):
        """  Corresponds to IDD Field `Zone Terminal Unit Name`

        Args:
            value (str): value for IDD Field `Zone Terminal Unit Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name`')
        self._data["Zone Terminal Unit Name"] = value

    @property
    def terminal_unit_availability_schedule(self):
        """Get terminal_unit_availability_schedule

        Returns:
            str: the value of `terminal_unit_availability_schedule` or None if not set
        """
        return self._data["Terminal Unit Availability Schedule"]

    @terminal_unit_availability_schedule.setter
    def terminal_unit_availability_schedule(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Availability Schedule`
        The unit is available the entire simulation if this field is left blank
        Schedule values of 0 denote the unit is off.

        Args:
            value (str): value for IDD Field `Terminal Unit Availability Schedule`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_availability_schedule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_availability_schedule`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_availability_schedule`')
        self._data["Terminal Unit Availability Schedule"] = value

    @property
    def terminal_unit_air_inlet_node_name(self):
        """Get terminal_unit_air_inlet_node_name

        Returns:
            str: the value of `terminal_unit_air_inlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Air Inlet Node Name"]

    @terminal_unit_air_inlet_node_name.setter
    def terminal_unit_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Air Inlet Node Name`
        the inlet node to the terminal unit

        Args:
            value (str): value for IDD Field `Terminal Unit Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_air_inlet_node_name`')
        self._data["Terminal Unit Air Inlet Node Name"] = value

    @property
    def terminal_unit_air_outlet_node_name(self):
        """Get terminal_unit_air_outlet_node_name

        Returns:
            str: the value of `terminal_unit_air_outlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Air Outlet Node Name"]

    @terminal_unit_air_outlet_node_name.setter
    def terminal_unit_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Air Outlet Node Name`
        the outlet node of the terminal unit

        Args:
            value (str): value for IDD Field `Terminal Unit Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_air_outlet_node_name`')
        self._data["Terminal Unit Air Outlet Node Name"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Cooling Operation`

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')
        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling is Needed"]

    @supply_air_flow_rate_when_no_cooling_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_is_needed(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate When No Cooling is Needed`

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate When No Cooling is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_when_no_cooling_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_is_needed`')
        self._data["Supply Air Flow Rate When No Cooling is Needed"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate During Heating Operation`

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')
        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Heating is Needed"]

    @supply_air_flow_rate_when_no_heating_is_needed.setter
    def supply_air_flow_rate_when_no_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Supply Air Flow Rate When No Heating is Needed`

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate When No Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `supply_air_flow_rate_when_no_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_heating_is_needed`')
        self._data["Supply Air Flow Rate When No Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_during_cooling_operation(self):
        """Get outdoor_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Cooling Operation"]

    @outdoor_air_flow_rate_during_cooling_operation.setter
    def outdoor_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Cooling Operation`

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Cooling Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Cooling Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`')
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = value

    @property
    def outdoor_air_flow_rate_during_heating_operation(self):
        """Get outdoor_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Heating Operation"]

    @outdoor_air_flow_rate_during_heating_operation.setter
    def outdoor_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate During Heating Operation`

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Heating Operation`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate During Heating Operation"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`')
        self._data["Outdoor Air Flow Rate During Heating Operation"] = value

    @property
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"]

    @outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`')
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')
        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def supply_air_fan_placement(self):
        """Get supply_air_fan_placement

        Returns:
            str: the value of `supply_air_fan_placement` or None if not set
        """
        return self._data["Supply Air Fan Placement"]

    @supply_air_fan_placement.setter
    def supply_air_fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `Supply Air Fan Placement`
        Select fan placement as either blow through or draw through.

        Args:
            value (str): value for IDD Field `Supply Air Fan Placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_placement`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_placement`')
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
                                     'field `supply_air_fan_placement`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Placement"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value="Fan:ConstantVolume"):
        """  Corresponds to IDD Field `Supply Air Fan Object Type`

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                Default value: Fan:ConstantVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
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
                                     'field `supply_air_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_object_name(self):
        """Get supply_air_fan_object_name

        Returns:
            str: the value of `supply_air_fan_object_name` or None if not set
        """
        return self._data["Supply Air Fan Object Name"]

    @supply_air_fan_object_name.setter
    def supply_air_fan_object_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Fan Object Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_fan_object_name`')
        self._data["Supply Air Fan Object Name"] = value

    @property
    def outside_air_mixer_object_type(self):
        """Get outside_air_mixer_object_type

        Returns:
            str: the value of `outside_air_mixer_object_type` or None if not set
        """
        return self._data["Outside Air Mixer Object Type"]

    @outside_air_mixer_object_type.setter
    def outside_air_mixer_object_type(self, value=None):
        """  Corresponds to IDD Field `Outside Air Mixer Object Type`
        If this field is blank, and outside air mixer is not used.

        Args:
            value (str): value for IDD Field `Outside Air Mixer Object Type`
                Accepted values are:
                      - OutdoorAir:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outside_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_air_mixer_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outside_air_mixer_object_type`')
            vals = {}
            vals["outdoorair:mixer"] = "OutdoorAir:Mixer"
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
                                     'field `outside_air_mixer_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Outside Air Mixer Object Type"] = value

    @property
    def outside_air_mixer_object_name(self):
        """Get outside_air_mixer_object_name

        Returns:
            str: the value of `outside_air_mixer_object_name` or None if not set
        """
        return self._data["Outside Air Mixer Object Name"]

    @outside_air_mixer_object_name.setter
    def outside_air_mixer_object_name(self, value=None):
        """  Corresponds to IDD Field `Outside Air Mixer Object Name`
        If this field is blank, and outside air mixer is not used.

        Args:
            value (str): value for IDD Field `Outside Air Mixer Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outside_air_mixer_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_air_mixer_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outside_air_mixer_object_name`')
        self._data["Outside Air Mixer Object Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`
        Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow
        This field may be left blank if heating-only mode is used

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:DX:VariableRefrigerantFlow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:dx:variablerefrigerantflow"] = "Coil:Cooling:DX:VariableRefrigerantFlow"
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
                                     'field `cooling_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_object_name(self):
        """Get cooling_coil_object_name

        Returns:
            str: the value of `cooling_coil_object_name` or None if not set
        """
        return self._data["Cooling Coil Object Name"]

    @cooling_coil_object_name.setter
    def cooling_coil_object_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Name`
        Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow
        This field may be left blank if heating-only mode is used

        Args:
            value (str): value for IDD Field `Cooling Coil Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_name`')
        self._data["Cooling Coil Object Name"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`
        Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow
        This field may be left blank if cooling-only mode is used

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:DX:VariableRefrigerantFlow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:dx:variablerefrigerantflow"] = "Coil:Heating:DX:VariableRefrigerantFlow"
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
                                     'field `heating_coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_object_name(self):
        """Get heating_coil_object_name

        Returns:
            str: the value of `heating_coil_object_name` or None if not set
        """
        return self._data["Heating Coil Object Name"]

    @heating_coil_object_name.setter
    def heating_coil_object_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Name`
        Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow
        This field may be left blank if cooling-only mode is used

        Args:
            value (str): value for IDD Field `Heating Coil Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_name`')
        self._data["Heating Coil Object Name"] = value

    @property
    def zone_terminal_unit_on_parasitic_electric_energy_use(self):
        """Get zone_terminal_unit_on_parasitic_electric_energy_use

        Returns:
            float: the value of `zone_terminal_unit_on_parasitic_electric_energy_use` or None if not set
        """
        return self._data["Zone Terminal Unit On Parasitic Electric Energy Use"]

    @zone_terminal_unit_on_parasitic_electric_energy_use.setter
    def zone_terminal_unit_on_parasitic_electric_energy_use(self, value=0.0):
        """  Corresponds to IDD Field `Zone Terminal Unit On Parasitic Electric Energy Use`

        Args:
            value (float): value for IDD Field `Zone Terminal Unit On Parasitic Electric Energy Use`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_terminal_unit_on_parasitic_electric_energy_use`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_terminal_unit_on_parasitic_electric_energy_use`')
        self._data["Zone Terminal Unit On Parasitic Electric Energy Use"] = value

    @property
    def zone_terminal_unit_off_parasitic_electric_energy_use(self):
        """Get zone_terminal_unit_off_parasitic_electric_energy_use

        Returns:
            float: the value of `zone_terminal_unit_off_parasitic_electric_energy_use` or None if not set
        """
        return self._data["Zone Terminal Unit Off Parasitic Electric Energy Use"]

    @zone_terminal_unit_off_parasitic_electric_energy_use.setter
    def zone_terminal_unit_off_parasitic_electric_energy_use(self, value=0.0):
        """  Corresponds to IDD Field `Zone Terminal Unit Off Parasitic Electric Energy Use`

        Args:
            value (float): value for IDD Field `Zone Terminal Unit Off Parasitic Electric Energy Use`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_terminal_unit_off_parasitic_electric_energy_use`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_terminal_unit_off_parasitic_electric_energy_use`')
        self._data["Zone Terminal Unit Off Parasitic Electric Energy Use"] = value

    @property
    def rated_heating_capacity_sizing_ratio(self):
        """Get rated_heating_capacity_sizing_ratio

        Returns:
            float: the value of `rated_heating_capacity_sizing_ratio` or None if not set
        """
        return self._data["Rated Heating Capacity Sizing Ratio"]

    @rated_heating_capacity_sizing_ratio.setter
    def rated_heating_capacity_sizing_ratio(self, value=1.0):
        """  Corresponds to IDD Field `Rated Heating Capacity Sizing Ratio`
        If this terminal unit's heating coil is autosized, the heating capacity is sized
        to be equal to the cooling capacity multiplied by this sizing ratio.
        This input applies to the terminal unit heating coil and overrides the sizing
        ratio entered in the AirConditioner:VariableRefrigerantFlow object.

        Args:
            value (float): value for IDD Field `Rated Heating Capacity Sizing Ratio`
                Units: W/W
                Default value: 1.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_heating_capacity_sizing_ratio`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `rated_heating_capacity_sizing_ratio`')
        self._data["Rated Heating Capacity Sizing Ratio"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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