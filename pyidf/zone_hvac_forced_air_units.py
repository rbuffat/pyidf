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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_supply_air_node_name = None
        else:
            self.zone_supply_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_exhaust_air_node_name = None
        else:
            self.zone_exhaust_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_heating_supply_air_temperature = None
        else:
            self.maximum_heating_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_cooling_supply_air_temperature = None
        else:
            self.minimum_cooling_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_heating_supply_air_humidity_ratio = None
        else:
            self.maximum_heating_supply_air_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_cooling_supply_air_humidity_ratio = None
        else:
            self.minimum_cooling_supply_air_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_limit = None
        else:
            self.heating_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_heating_air_flow_rate = None
        else:
            self.maximum_heating_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_sensible_heating_capacity = None
        else:
            self.maximum_sensible_heating_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_limit = None
        else:
            self.cooling_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_cooling_air_flow_rate = None
        else:
            self.maximum_cooling_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_total_cooling_capacity = None
        else:
            self.maximum_total_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_availability_schedule_name = None
        else:
            self.heating_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_availability_schedule_name = None
        else:
            self.cooling_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_sensible_heat_ratio = None
        else:
            self.cooling_sensible_heat_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidification_control_type = None
        else:
            self.humidification_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_controlled_ventilation_type = None
        else:
            self.demand_controlled_ventilation_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_economizer_type = None
        else:
            self.outdoor_air_economizer_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_type = None
        else:
            self.heat_recovery_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_heat_recovery_effectiveness = None
        else:
            self.sensible_heat_recovery_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latent_heat_recovery_effectiveness = None
        else:
            self.latent_heat_recovery_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `zone_supply_air_node_name`
        Must match a zone air inlet node name.

        Args:
            value (str): value for IDD Field `zone_supply_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_supply_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `zone_exhaust_air_node_name`
        Should match a zone air exhaust node name.
        This field is optional, but is required if this
        this object is used with other forced air equipment.

        Args:
            value (str): value for IDD Field `zone_exhaust_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_exhaust_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def maximum_heating_supply_air_temperature(self, value=50.0 ):
        """  Corresponds to IDD Field `maximum_heating_supply_air_temperature`

        Args:
            value (float): value for IDD Field `maximum_heating_supply_air_temperature`
                Unit: C
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
            except:
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
    def minimum_cooling_supply_air_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `minimum_cooling_supply_air_temperature`

        Args:
            value (float): value for IDD Field `minimum_cooling_supply_air_temperature`
                Unit: C
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
            except:
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
    def maximum_heating_supply_air_humidity_ratio(self, value=0.0156 ):
        """  Corresponds to IDD Field `maximum_heating_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `maximum_heating_supply_air_humidity_ratio`
                Unit: kgWater/kgDryAir
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
            except:
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
    def minimum_cooling_supply_air_humidity_ratio(self, value=0.0077 ):
        """  Corresponds to IDD Field `minimum_cooling_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `minimum_cooling_supply_air_humidity_ratio`
                Unit: kgWater/kgDryAir
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
            except:
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
        """  Corresponds to IDD Field `heating_limit`

        Args:
            value (str): value for IDD Field `heating_limit`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_limit`')
            vals = set()
            vals.add("NoLimit")
            vals.add("LimitFlowRate")
            vals.add("LimitCapacity")
            vals.add("LimitFlowRateAndCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_limit`'.format(value))

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
        """  Corresponds to IDD Field `maximum_heating_air_flow_rate`
        This field is ignored if Heating Limit = NoLimit
        If this field is blank, there is no limit.

        Args:
            value (float): value for IDD Field `maximum_heating_air_flow_rate`
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
        """  Corresponds to IDD Field `maximum_sensible_heating_capacity`
        This field is ignored if Heating Limit = NoLimit
        If this field is blank, there is no limit.

        Args:
            value (float): value for IDD Field `maximum_sensible_heating_capacity`
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
        """  Corresponds to IDD Field `cooling_limit`

        Args:
            value (str): value for IDD Field `cooling_limit`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_limit`')
            vals = set()
            vals.add("NoLimit")
            vals.add("LimitFlowRate")
            vals.add("LimitCapacity")
            vals.add("LimitFlowRateAndCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_limit`'.format(value))

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
        """  Corresponds to IDD Field `maximum_cooling_air_flow_rate`
        This field is ignored if Cooling Limit = NoLimit
        This field is required if Outdoor Air Economizer Type is anything other than NoEconomizer.

        Args:
            value (float): value for IDD Field `maximum_cooling_air_flow_rate`
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
        """  Corresponds to IDD Field `maximum_total_cooling_capacity`
        This field is ignored if Cooling Limit = NoLimit

        Args:
            value (float): value for IDD Field `maximum_total_cooling_capacity`
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
        """  Corresponds to IDD Field `heating_availability_schedule_name`
        If blank, heating is always available.

        Args:
            value (str): value for IDD Field `heating_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `cooling_availability_schedule_name`
        If blank, cooling is always available.

        Args:
            value (str): value for IDD Field `cooling_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `dehumidification_control_type`
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
            value (str): value for IDD Field `dehumidification_control_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dehumidification_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dehumidification_control_type`')
            vals = set()
            vals.add("ConstantSensibleHeatRatio")
            vals.add("Humidistat")
            vals.add("None")
            vals.add("ConstantSupplyHumidityRatio")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `dehumidification_control_type`'.format(value))

        self._data["Dehumidification Control Type"] = value

    @property
    def cooling_sensible_heat_ratio(self):
        """Get cooling_sensible_heat_ratio

        Returns:
            float: the value of `cooling_sensible_heat_ratio` or None if not set
        """
        return self._data["Cooling Sensible Heat Ratio"]

    @cooling_sensible_heat_ratio.setter
    def cooling_sensible_heat_ratio(self, value=0.7 ):
        """  Corresponds to IDD Field `cooling_sensible_heat_ratio`
        This field is applicable only when Dehumidification Control Type is ConstantSensibleHeatRatio

        Args:
            value (float): value for IDD Field `cooling_sensible_heat_ratio`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `humidification_control_type`
        None means that there is no humidification.
        Humidistat means that there is a ZoneControl:Humidistat for this
        zone and the ideal loads system will attempt to satisfy the humidistat.
        ConstantSupplyHumidityRatio means that during heating the supply air
        will always be at the Maximum Heating Supply Humidity Ratio.

        Args:
            value (str): value for IDD Field `humidification_control_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `humidification_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `humidification_control_type`')
            vals = set()
            vals.add("None")
            vals.add("Humidistat")
            vals.add("ConstantSupplyHumidityRatio")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `humidification_control_type`'.format(value))

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
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the minimum
        outdoor air flow rate will be computed using these specifications. The outdoor air
        flow rate will also be affected by the next two fields.
        If this field is blank, there will be no outdoor air and the remaining fields will
        be ignored.

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `outdoor_air_inlet_node_name`
        This field is required if the system provides outdoor air
        Enter the name of an outdoor air node. This node name is also specified in
        an OutdoorAir:Node or OutdoorAir:NodeList object.

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
    def demand_controlled_ventilation_type(self):
        """Get demand_controlled_ventilation_type

        Returns:
            str: the value of `demand_controlled_ventilation_type` or None if not set
        """
        return self._data["Demand Controlled Ventilation Type"]

    @demand_controlled_ventilation_type.setter
    def demand_controlled_ventilation_type(self, value="None"):
        """  Corresponds to IDD Field `demand_controlled_ventilation_type`
        This field controls how the minimum outdoor air flow rate is calculated.
        None means that design occupancy will be uased to compute the minimum outdoor air flow rate
        OccupancySchedule means that current occupancy level will be used.
        CO2Setpoint means that the design occupancy will be used to compute the minimum outdoor air flow
        reate and the outdoor air flow rate may be increased if necessary to maintain the indoor air carbon
        dioxide setpoint defined in a ZoneControl:ContaminantController object.

        Args:
            value (str): value for IDD Field `demand_controlled_ventilation_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_controlled_ventilation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_controlled_ventilation_type`')
            vals = set()
            vals.add("None")
            vals.add("OccupancySchedule")
            vals.add("CO2Setpoint")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demand_controlled_ventilation_type`'.format(value))

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
        """  Corresponds to IDD Field `outdoor_air_economizer_type`
        DifferentialDryBulb and DifferentialEnthalpy will increase the outdoor air flow rate
        when there is a cooling load and the outdoor air temperature or enthalpy
        is below the zone exhaust air temperature or enthalpy.

        Args:
            value (str): value for IDD Field `outdoor_air_economizer_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_economizer_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_economizer_type`')
            vals = set()
            vals.add("NoEconomizer")
            vals.add("DifferentialDryBulb")
            vals.add("DifferentialEnthalpy")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_economizer_type`'.format(value))

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
        """  Corresponds to IDD Field `heat_recovery_type`

        Args:
            value (str): value for IDD Field `heat_recovery_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_recovery_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_type`')
            vals = set()
            vals.add("None")
            vals.add("Sensible")
            vals.add("Enthalpy")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_recovery_type`'.format(value))

        self._data["Heat Recovery Type"] = value

    @property
    def sensible_heat_recovery_effectiveness(self):
        """Get sensible_heat_recovery_effectiveness

        Returns:
            float: the value of `sensible_heat_recovery_effectiveness` or None if not set
        """
        return self._data["Sensible Heat Recovery Effectiveness"]

    @sensible_heat_recovery_effectiveness.setter
    def sensible_heat_recovery_effectiveness(self, value=0.7 ):
        """  Corresponds to IDD Field `sensible_heat_recovery_effectiveness`

        Args:
            value (float): value for IDD Field `sensible_heat_recovery_effectiveness`
                Unit: dimensionless
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
            except:
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
    def latent_heat_recovery_effectiveness(self, value=0.65 ):
        """  Corresponds to IDD Field `latent_heat_recovery_effectiveness`
        Applicable only if Heat Recovery Type is Enthalpy.

        Args:
            value (float): value for IDD Field `latent_heat_recovery_effectiveness`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_supply_air_node_name))
        out.append(self._to_str(self.zone_exhaust_air_node_name))
        out.append(self._to_str(self.maximum_heating_supply_air_temperature))
        out.append(self._to_str(self.minimum_cooling_supply_air_temperature))
        out.append(self._to_str(self.maximum_heating_supply_air_humidity_ratio))
        out.append(self._to_str(self.minimum_cooling_supply_air_humidity_ratio))
        out.append(self._to_str(self.heating_limit))
        out.append(self._to_str(self.maximum_heating_air_flow_rate))
        out.append(self._to_str(self.maximum_sensible_heating_capacity))
        out.append(self._to_str(self.cooling_limit))
        out.append(self._to_str(self.maximum_cooling_air_flow_rate))
        out.append(self._to_str(self.maximum_total_cooling_capacity))
        out.append(self._to_str(self.heating_availability_schedule_name))
        out.append(self._to_str(self.cooling_availability_schedule_name))
        out.append(self._to_str(self.dehumidification_control_type))
        out.append(self._to_str(self.cooling_sensible_heat_ratio))
        out.append(self._to_str(self.humidification_control_type))
        out.append(self._to_str(self.design_specification_outdoor_air_object_name))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.demand_controlled_ventilation_type))
        out.append(self._to_str(self.outdoor_air_economizer_type))
        out.append(self._to_str(self.heat_recovery_type))
        out.append(self._to_str(self.sensible_heat_recovery_effectiveness))
        out.append(self._to_str(self.latent_heat_recovery_effectiveness))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacFourPipeFanCoil(object):
    """ Corresponds to IDD object `ZoneHVAC:FourPipeFanCoil`
        Four pipe fan coil system. Forced-convection hydronic heating-cooling unit with
        supply fan, hot water heating coil, chilled water cooling coil, and fixed-position
        outdoor air mixer.
    """
    internal_name = "ZoneHVAC:FourPipeFanCoil"
    field_count = 26

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_control_method = None
        else:
            self.capacity_control_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_speed_supply_air_flow_ratio = None
        else:
            self.low_speed_supply_air_flow_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.medium_speed_supply_air_flow_ratio = None
        else:
            self.medium_speed_supply_air_flow_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_schedule_name = None
        else:
            self.outdoor_air_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_cold_water_flow_rate = None
        else:
            self.maximum_cold_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_cold_water_flow_rate = None
        else:
            self.minimum_cold_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_hot_water_flow_rate = None
        else:
            self.maximum_hot_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_hot_water_flow_rate = None
        else:
            self.minimum_hot_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `capacity_control_method`

        Args:
            value (str): value for IDD Field `capacity_control_method`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `capacity_control_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_control_method`')
            vals = set()
            vals.add("ConstantFanVariableFlow")
            vals.add("CyclingFan")
            vals.add("VariableFanVariableFlow")
            vals.add("VariableFanConstantFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `capacity_control_method`'.format(value))

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
        """  Corresponds to IDD Field `maximum_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_supply_air_flow_rate`
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
    def low_speed_supply_air_flow_ratio(self, value=0.33 ):
        """  Corresponds to IDD Field `low_speed_supply_air_flow_ratio`

        Args:
            value (float): value for IDD Field `low_speed_supply_air_flow_ratio`
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
            except:
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
    def medium_speed_supply_air_flow_ratio(self, value=0.66 ):
        """  Corresponds to IDD Field `medium_speed_supply_air_flow_ratio`
        Medium Speed Supply Air Flow Ratio should be greater
        than Low Speed Supply Air Flow Ratio

        Args:
            value (float): value for IDD Field `medium_speed_supply_air_flow_ratio`
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
            except:
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
        """  Corresponds to IDD Field `maximum_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_outdoor_air_flow_rate`
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
        """  Corresponds to IDD Field `outdoor_air_schedule_name`
        Value of schedule multiplies maximum outdoor air flow rate

        Args:
            value (str): value for IDD Field `outdoor_air_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `air_inlet_node_name`

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
        """  Corresponds to IDD Field `outdoor_air_mixer_object_type`
        currently only one type OutdoorAir:Mixer object is available.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = set()
            vals.add("OutdoorAir:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_mixer_object_type`'.format(value))

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
        """  Corresponds to IDD Field `outdoor_air_mixer_name`

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Fan type must be according to capacity control method (see I/O)
        For ConstantFanVariableFlow a Fan:OnOff or Fan:ConstantVolume is valid.
        For CyclingFan, a Fan:OnOff is valid.
        For VariableFanVariableFlow or VariableFanConstantFlow a Fan:VariableVolume is valid.
        The fans inlet node should be the same as the outdoor air mixers mixed air node.

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            vals.add("Fan:VariableVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatExchangerAssisted")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `cooling_coil_name`

        Args:
            value (str): value for IDD Field `cooling_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `maximum_cold_water_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_cold_water_flow_rate`
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
    def minimum_cold_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_cold_water_flow_rate`

        Args:
            value (float): value for IDD Field `minimum_cold_water_flow_rate`
                Unit: m3/s
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
    def cooling_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `cooling_convergence_tolerance`

        Args:
            value (float): value for IDD Field `cooling_convergence_tolerance`
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
            except:
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
        """  Corresponds to IDD Field `heating_coil_object_type`

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Water")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `heating_coil_name`

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `maximum_hot_water_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_hot_water_flow_rate`
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
    def minimum_hot_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_flow_rate`

        Args:
            value (float): value for IDD Field `minimum_hot_water_flow_rate`
                Unit: m3/s
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
    def heating_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `heating_convergence_tolerance`

        Args:
            value (float): value for IDD Field `heating_convergence_tolerance`
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
            except:
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.capacity_control_method))
        out.append(self._to_str(self.maximum_supply_air_flow_rate))
        out.append(self._to_str(self.low_speed_supply_air_flow_ratio))
        out.append(self._to_str(self.medium_speed_supply_air_flow_ratio))
        out.append(self._to_str(self.maximum_outdoor_air_flow_rate))
        out.append(self._to_str(self.outdoor_air_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.outdoor_air_mixer_object_type))
        out.append(self._to_str(self.outdoor_air_mixer_name))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.maximum_cold_water_flow_rate))
        out.append(self._to_str(self.minimum_cold_water_flow_rate))
        out.append(self._to_str(self.cooling_convergence_tolerance))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.maximum_hot_water_flow_rate))
        out.append(self._to_str(self.minimum_hot_water_flow_rate))
        out.append(self._to_str(self.heating_convergence_tolerance))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacWindowAirConditioner(object):
    """ Corresponds to IDD object `ZoneHVAC:WindowAirConditioner`
        Window air conditioner. Forced-convection cooling-only unit with supply fan, direct
        expansion (DX) cooling coil, and fixed-position outdoor air mixer.
    """
    internal_name = "ZoneHVAC:WindowAirConditioner"
    field_count = 17

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dx_cooling_coil_name = None
        else:
            self.dx_cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `maximum_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_supply_air_flow_rate`
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
        """  Corresponds to IDD Field `maximum_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_outdoor_air_flow_rate`
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
        """  Corresponds to IDD Field `air_inlet_node_name`

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
        """  Corresponds to IDD Field `outdoor_air_mixer_object_type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = set()
            vals.add("OutdoorAir:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_mixer_object_type`'.format(value))

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
        """  Corresponds to IDD Field `outdoor_air_mixer_name`

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Fan:ConstantVolume only works when continuous fan operation is used the entire
        simulation (all supply air fan operating mode schedule values are greater than 0).
        If any fan operating mode schedule values are 0 a Fan:OnOff object must be used.

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`
        Fan type Fan:ConstantVolume is used with continuous fan
        and fan type Fan:OnOff is used with cycling Fan.

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `dx_cooling_coil_name`

        Args:
            value (str): value for IDD Field `dx_cooling_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dx_cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote
        cycling fan operation (fan cycles with cooling coil). Schedule values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

    @property
    def cooling_convergence_tolerance(self):
        """Get cooling_convergence_tolerance

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set
        """
        return self._data["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `cooling_convergence_tolerance`

        Args:
            value (float): value for IDD Field `cooling_convergence_tolerance`
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
            except:
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.maximum_supply_air_flow_rate))
        out.append(self._to_str(self.maximum_outdoor_air_flow_rate))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.outdoor_air_mixer_object_type))
        out.append(self._to_str(self.outdoor_air_mixer_name))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.dx_cooling_coil_name))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.cooling_convergence_tolerance))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacPackagedTerminalAirConditioner(object):
    """ Corresponds to IDD object `ZoneHVAC:PackagedTerminalAirConditioner`
        Packaged terminal air conditioner (PTAC).  Forced-convection heating-cooling unit
        with supply fan, direct expansion (DX) cooling coil, heating coil (gas, electric, hot
        water, or steam) and fixed-position outdoor air mixer.
    """
    internal_name = "ZoneHVAC:PackagedTerminalAirConditioner"
    field_count = 22

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        Unique name for this packaged terminal air conditioner object.

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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Schedule values of 0 denote the unit is off.

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
        """  Corresponds to IDD Field `air_inlet_node_name`
        Air inlet node for the PTAC must be a zone air exhaust Node.

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
        Air outlet node for the PTAC must be a zone air inlet node.

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
        """  Corresponds to IDD Field `outdoor_air_mixer_object_type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = set()
            vals.add("OutdoorAir:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_mixer_object_type`'.format(value))

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
        """  Corresponds to IDD Field `outdoor_air_mixer_name`
        Needs to match the name of the PTAC outdoor air mixer object.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`
        Must be less than or equal to fan size.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`
        Must be less than or equal to fan size.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Must be less than or equal to fan size.
        Only used when supply air fan operating mode schedule values specify continuous fan
        (schedule values greater than 0 specify continuous fan operation).
        This air flow rate is used when no heating or cooling is required and the cooling or
        heating coil is off. If this field is left blank or zero, the supply air flow rate
        from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_cooling_operation`
        Must be less than or equal to supply air flow rate during cooling operation.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_heating_operation`
        Must be less than or equal to supply air flow rate during heating operation.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Only used when supply air fan operating mode schedule values specify continuous fan
        (schedule values greater than 0 specify continuous fan operation).
        This air flow rate is used when no heating or cooling is required and the cooling or
        heating coil is off. If this field is left blank or zero, the outdoor air flow rate
        from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
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
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Fan:ConstantVolume only works when continuous fan operation is used the entire
        simulation (all supply air fan operating mode schedule values are greater than 0).
        If any fan operating mode schedule values are 0 a Fan:OnOff object must be used.

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`
        Needs to match in the fan object.

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `heating_coil_object_type`
        Select the type of heating coil.

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `heating_coil_name`
        Needs to match in the heating coil object.

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `cooling_coil_object_type`
        Select the type of Cooling Coil.
        Only works with Coil:Cooling:DX:SingleSpeed or
        CoilSystem:Cooling:DX:HeatExchangerAssisted or
        Coil:Cooling:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("Coil:Cooling:DX:VariableSpeed")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `cooling_coil_name`
        Needs to match a DX cooling coil object.

        Args:
            value (str): value for IDD Field `cooling_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `fan_placement`
        Select fan placement as either blow through or draw through.

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
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.outdoor_air_mixer_object_type))
        out.append(self._to_str(self.outdoor_air_mixer_name))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacPackagedTerminalHeatPump(object):
    """ Corresponds to IDD object `ZoneHVAC:PackagedTerminalHeatPump`
        Packaged terminal heat pump (PTHP). Forced-convection heating-cooling unit with
        supply fan, direct expansion (DX) cooling coil, DX heating coil (air-to-air heat
        pump), supplemental heating coil (gas, electric, hot water, or steam), and
        fixed-position outdoor air mixer.
    """
    internal_name = "ZoneHVAC:PackagedTerminalHeatPump"
    field_count = 29

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_drybulb_temperature_for_compressor_operation = None
        else:
            self.minimum_outdoor_drybulb_temperature_for_compressor_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature_from_supplemental_heater = None
        else:
            self.maximum_supply_air_temperature_from_supplemental_heater = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        Unique name for this packaged terminal heat pump object.

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
        Schedule values of 0 denote the unit is off.

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
        """  Corresponds to IDD Field `air_inlet_node_name`
        Air inlet node for the PTHP must be a zone air exhaust node.

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
        Air outlet node for the PTHP must be a zone air inlet node.

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
        """  Corresponds to IDD Field `outdoor_air_mixer_object_type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = set()
            vals.add("OutdoorAir:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_mixer_object_type`'.format(value))

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
        """  Corresponds to IDD Field `outdoor_air_mixer_name`
        Needs to match name of outdoor air mixer object.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`
        Must be less than or equal to fan size.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`
        Must be less than or equal to fan size.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Must be less than or equal to fan size.
        Only used when heat pump fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the supply air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_cooling_operation`
        Must be less than or equal to supply air flow rate during cooling operation.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_heating_operation`
        Must be less than or equal to supply air flow rate during heating operation.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Only used when heat pump Fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the outdoor air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
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
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Fan:ConstantVolume only works with fan operating mode is continuous.

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`
        Needs to match a fan object.

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `heating_coil_object_type`
        Only works with Coil:Heating:DX:SingleSpeed or
        Coil:Heating:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:DX:SingleSpeed")
            vals.add("Coil:Heating:DX:VariableSpeed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `heating_coil_name`
        Needs to match in the DX Heating Coil object.

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def heating_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `heating_convergence_tolerance`
        Defines Heating convergence tolerence as a fraction of Heating load to be met.

        Args:
            value (float): value for IDD Field `heating_convergence_tolerance`
                Unit: dimensionless
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
            except:
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
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(self, value=-8.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_drybulb_temperature_for_compressor_operation`
        Needs to match the corresponding minimum outdoor temperature defined
        in the DX Heating Coil object.

        Args:
            value (float): value for IDD Field `minimum_outdoor_drybulb_temperature_for_compressor_operation`
                Unit: C
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
            except:
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
        """  Corresponds to IDD Field `cooling_coil_object_type`
        Only works with Coil:Cooling:DX:SingleSpeed or
        CoilSystem:Cooling:DX:HeatExchangerAssisted or
        Coil:Cooling:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("Coil:Cooling:DX:VariableSpeed")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `cooling_coil_name`
        Needs to match in the DX Cooling Coil object.

        Args:
            value (str): value for IDD Field `cooling_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def cooling_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `cooling_convergence_tolerance`
        Defines Cooling convergence tolerence as a fraction of the Cooling load to be met.

        Args:
            value (float): value for IDD Field `cooling_convergence_tolerance`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `supplemental_heating_coil_object_type`
        works with gas, electric, hot water and steam heating coil.

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supplemental_heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supplemental_heating_coil_name`
        Needs to match in the supplemental heating coil object.

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `maximum_supply_air_temperature_from_supplemental_heater`
        Supply air temperature from the supplemental heater will not exceed this value.

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature_from_supplemental_heater`
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
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
        Supplemental heater will not operate when outdoor temperature exceeds this value.

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
                Unit: C
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
            except:
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
        """  Corresponds to IDD Field `fan_placement`
        Select fan placement as either blow through or draw through.

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
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule that controls fan operation. Schedule values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.outdoor_air_mixer_object_type))
        out.append(self._to_str(self.outdoor_air_mixer_name))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.heating_convergence_tolerance))
        out.append(self._to_str(self.minimum_outdoor_drybulb_temperature_for_compressor_operation))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.cooling_convergence_tolerance))
        out.append(self._to_str(self.supplemental_heating_coil_object_type))
        out.append(self._to_str(self.supplemental_heating_coil_name))
        out.append(self._to_str(self.maximum_supply_air_temperature_from_supplemental_heater))
        out.append(self._to_str(self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacWaterToAirHeatPump(object):
    """ Corresponds to IDD object `ZoneHVAC:WaterToAirHeatPump`
        Water-to-air heat pump. Forced-convection heating-cooling unit with supply fan,
        water-to-air cooling and heating coils, supplemental heating coil (gas, electric, hot
        water, or steam), and fixed-position outdoor air mixer.
    """
    internal_name = "ZoneHVAC:WaterToAirHeatPump"
    field_count = 32

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_cycling_rate = None
        else:
            self.maximum_cycling_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_time_constant = None
        else:
            self.heat_pump_time_constant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_oncycle_power_use = None
        else:
            self.fraction_of_oncycle_power_use = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_fan_delay_time = None
        else:
            self.heat_pump_fan_delay_time = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature_from_supplemental_heater = None
        else:
            self.maximum_supply_air_temperature_from_supplemental_heater = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_drybulb_temperature_sensor_node_name = None
        else:
            self.outdoor_drybulb_temperature_sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_coil_water_flow_mode = None
        else:
            self.heat_pump_coil_water_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `air_inlet_node_name`

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
        """  Corresponds to IDD Field `outdoor_air_mixer_object_type`
        currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = set()
            vals.add("OutdoorAir:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_mixer_object_type`'.format(value))

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
        """  Corresponds to IDD Field `outdoor_air_mixer_name`
        This optional field specifies the name of the outdoor air mixer object.
        When used, this name needs to match name of outdoor air mixer object.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`
        Must be less than or equal to fan size.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`
        Must be less than or equal to fan size.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Must be less than or equal to fan size.
        Only used when heat pump fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the supply air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_cooling_operation`
        Must be less than or equal to supply air flow rate during cooling operation.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_heating_operation`
        Must be less than or equal to supply air flow rate during heating operation.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Only used when heat pump Fan operating mode is continuous. This air flow rate
        is used when no heating or cooling is required and the DX coil compressor is off.
        If this field is left blank or zero, the outdoor air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
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
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Only works with On/Off Fan

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`
        Needs to match Fan:OnOff object

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `heating_coil_object_type`

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:WaterToAirHeatPump:EquationFit")
            vals.add("Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `heating_coil_name`
        Needs to match in the water-to-air heatpump heating coil object

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:WaterToAirHeatPump:EquationFit")
            vals.add("Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `cooling_coil_name`
        Needs to match in the water-to-air heatpump cooling coil object

        Args:
            value (str): value for IDD Field `cooling_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def maximum_cycling_rate(self, value=2.5 ):
        """  Corresponds to IDD Field `maximum_cycling_rate`
        The maximum on-off cycling rate for the compressor
        Suggested value is 2.5 for a typical heat pump

        Args:
            value (float): value for IDD Field `maximum_cycling_rate`
                Unit: cycles/hr
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
    def heat_pump_time_constant(self):
        """Get heat_pump_time_constant

        Returns:
            float: the value of `heat_pump_time_constant` or None if not set
        """
        return self._data["Heat Pump Time Constant"]

    @heat_pump_time_constant.setter
    def heat_pump_time_constant(self, value=60.0 ):
        """  Corresponds to IDD Field `heat_pump_time_constant`
        Time constant for the cooling coil's capacity to reach steady state after startup
        Suggested value is 60 for a typical heat pump

        Args:
            value (float): value for IDD Field `heat_pump_time_constant`
                Unit: s
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
            except:
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
    def fraction_of_oncycle_power_use(self, value=0.01 ):
        """  Corresponds to IDD Field `fraction_of_oncycle_power_use`
        The fraction of on-cycle power use to adjust the part load fraction based on
        the off-cycle power consumption due to crankcase heaters, controls, fans, and etc.
        Suggested value is 0.01 for a typical heat pump

        Args:
            value (float): value for IDD Field `fraction_of_oncycle_power_use`
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
            except:
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
    def heat_pump_fan_delay_time(self, value=60.0 ):
        """  Corresponds to IDD Field `heat_pump_fan_delay_time`
        Programmed time delay for heat pump fan to shut off after compressor cycle off.
        Only required when fan operating mode is cycling
        Enter 0 when fan operating mode is continuous

        Args:
            value (float): value for IDD Field `heat_pump_fan_delay_time`
                Unit: s
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
            except:
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
        """  Corresponds to IDD Field `supplemental_heating_coil_object_type`
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supplemental_heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supplemental_heating_coil_name`
        Needs to match in the supplemental heating coil object

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `maximum_supply_air_temperature_from_supplemental_heater`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature_from_supplemental_heater`
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
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
                Unit: C
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
            except:
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
        """  Corresponds to IDD Field `outdoor_drybulb_temperature_sensor_node_name`

        Args:
            value (str): value for IDD Field `outdoor_drybulb_temperature_sensor_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule that controls fan operation. Schedule values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil). Schedule values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `heat_pump_coil_water_flow_mode`
        used only when the heat pump coils are of the type WaterToAirHeatPump:EquationFit
        Constant results in 100% water flow regardless of compressor PLR
        Cycling results in water flow that matches compressor PLR
        ConstantOnDemand results in 100% water flow whenever the coil is on, but is 0% whenever the coil has no load

        Args:
            value (str): value for IDD Field `heat_pump_coil_water_flow_mode`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_pump_coil_water_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_pump_coil_water_flow_mode`')
            vals = set()
            vals.add("Constant")
            vals.add("Cycling")
            vals.add("ConstantOnDemand")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_pump_coil_water_flow_mode`'.format(value))

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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.outdoor_air_mixer_object_type))
        out.append(self._to_str(self.outdoor_air_mixer_name))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.maximum_cycling_rate))
        out.append(self._to_str(self.heat_pump_time_constant))
        out.append(self._to_str(self.fraction_of_oncycle_power_use))
        out.append(self._to_str(self.heat_pump_fan_delay_time))
        out.append(self._to_str(self.supplemental_heating_coil_object_type))
        out.append(self._to_str(self.supplemental_heating_coil_name))
        out.append(self._to_str(self.maximum_supply_air_temperature_from_supplemental_heater))
        out.append(self._to_str(self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation))
        out.append(self._to_str(self.outdoor_drybulb_temperature_sensor_node_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.heat_pump_coil_water_flow_mode))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacDehumidifierDx(object):
    """ Corresponds to IDD object `ZoneHVAC:Dehumidifier:DX`
        This object calculates the performance of zone (room) air dehumidifiers.
        Meant to model conventional direct expansion (DX) cooling-based room air
        dehumidifiers (reject 100% of condenser heat to the zone air), but this
        object might be able to be used to model other room air dehumidifier types.
    """
    internal_name = "ZoneHVAC:Dehumidifier:DX"
    field_count = 14

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_water_removal = None
        else:
            self.rated_water_removal = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_energy_factor = None
        else:
            self.rated_energy_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_air_flow_rate = None
        else:
            self.rated_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_removal_curve_name = None
        else:
            self.water_removal_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.energy_factor_curve_name = None
        else:
            self.energy_factor_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.part_load_fraction_correlation_curve_name = None
        else:
            self.part_load_fraction_correlation_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_drybulb_temperature_for_dehumidifier_operation = None
        else:
            self.minimum_drybulb_temperature_for_dehumidifier_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_drybulb_temperature_for_dehumidifier_operation = None
        else:
            self.maximum_drybulb_temperature_for_dehumidifier_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.offcycle_parasitic_electric_load = None
        else:
            self.offcycle_parasitic_electric_load = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condensate_collection_water_storage_tank_name = None
        else:
            self.condensate_collection_water_storage_tank_name = vals[i]
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
        Unique name for this direct expansion (DX) zone dehumidifier object.

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
        Schedule values of 0 denote the unit is off.
        Schedule values >0.0 (usually 1.0) indicate that the dehumidifier is available to operate.

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
        """  Corresponds to IDD Field `air_inlet_node_name`
        Air inlet node for the dehumidifier must be a zone air exhaust node.

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
        Air outlet node for the dehumidifier must be a zone air inlet node.

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
        """  Corresponds to IDD Field `rated_water_removal`
        Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.

        Args:
            value (float): value for IDD Field `rated_water_removal`
                Unit: L/day
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
        """  Corresponds to IDD Field `rated_energy_factor`
        Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.

        Args:
            value (float): value for IDD Field `rated_energy_factor`
                Unit: L/kWh
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
        """  Corresponds to IDD Field `rated_air_flow_rate`

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
    def water_removal_curve_name(self):
        """Get water_removal_curve_name

        Returns:
            str: the value of `water_removal_curve_name` or None if not set
        """
        return self._data["Water Removal Curve Name"]

    @water_removal_curve_name.setter
    def water_removal_curve_name(self, value=None):
        """  Corresponds to IDD Field `water_removal_curve_name`
        Table:TwoIndependentVariable object can also be used
        Name of a curve that describes the water removal rate (normalized to rated conditions)
        as a function of the dry-bulb temperature and relative humidity of the air
        entering the dehumidifier.
        Curve output = (actual water removal/rated water removal) = a + b*T + c*T**2 + d*RH +
        e*RH**2 + f*T*RH
        T = inlet air dry-bulb temperature (C)
        RH = inlet air RH (%)

        Args:
            value (str): value for IDD Field `water_removal_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_removal_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `energy_factor_curve_name`
        Table:TwoIndependentVariable object can also be used
        Name of a curve that describes the energy factor (normalized to rated conditions)
        as a function of the dry-bulb temperature and relative humidity of the air
        entering the dehumidifier.
        Curve output = (actual energy factor/rated energy factor) = a + b*T + c*T**2 + d*RH +
        e*RH**2 + f*T*RH
        T = inlet air dry-bulb temperature (C)
        RH = inlet air RH (%)

        Args:
            value (str): value for IDD Field `energy_factor_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `energy_factor_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `part_load_fraction_correlation_curve_name`
        Table:OneIndependentVariable can also be used
        Name of a curve that describes the part load fraction (PLF) of the system as
        a function of the part load ratio. Used to calculate dehumidifier run time fraction
        and electric power.
        quadratic curve = a + b*PLR + c*PLR**2
        cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3
        PLR = part load ratio (dehumidification load/steady state water removal capacity)

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
    def minimum_drybulb_temperature_for_dehumidifier_operation(self):
        """Get minimum_drybulb_temperature_for_dehumidifier_operation

        Returns:
            float: the value of `minimum_drybulb_temperature_for_dehumidifier_operation` or None if not set
        """
        return self._data["Minimum Dry-Bulb Temperature for Dehumidifier Operation"]

    @minimum_drybulb_temperature_for_dehumidifier_operation.setter
    def minimum_drybulb_temperature_for_dehumidifier_operation(self, value=10.0 ):
        """  Corresponds to IDD Field `minimum_drybulb_temperature_for_dehumidifier_operation`
        Dehumidifier shut off if inlet air (zone) temperature is below this value.
        This value must be less than the Maximum Dry-Bulb Temperature for Dehumidifier Operation.

        Args:
            value (float): value for IDD Field `minimum_drybulb_temperature_for_dehumidifier_operation`
                Unit: C
                Default value: 10.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
    def maximum_drybulb_temperature_for_dehumidifier_operation(self, value=35.0 ):
        """  Corresponds to IDD Field `maximum_drybulb_temperature_for_dehumidifier_operation`
        Dehumidifier shut off if inlet air (zone) temperature is above this value.
        This value must be greater than the Minimum Dry-Bulb Temperature for Dehumidifier Operation.

        Args:
            value (float): value for IDD Field `maximum_drybulb_temperature_for_dehumidifier_operation`
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
    def offcycle_parasitic_electric_load(self, value=0.0 ):
        """  Corresponds to IDD Field `offcycle_parasitic_electric_load`
        Parasitic electric power consumed when the dehumidifier is available to operate, but
        does not operate (i.e., no high humidity load to be met).
        Off cycle parasitic power is 0 when the availability schedule is 0.
        This electric load is considered as a heat gain to the zone air.

        Args:
            value (float): value for IDD Field `offcycle_parasitic_electric_load`
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
        """  Corresponds to IDD Field `condensate_collection_water_storage_tank_name`
        Name of storage tank used to collect water removed by the dehumidifier.

        Args:
            value (str): value for IDD Field `condensate_collection_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condensate_collection_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condensate_collection_water_storage_tank_name`')

        self._data["Condensate Collection Water Storage Tank Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.rated_water_removal))
        out.append(self._to_str(self.rated_energy_factor))
        out.append(self._to_str(self.rated_air_flow_rate))
        out.append(self._to_str(self.water_removal_curve_name))
        out.append(self._to_str(self.energy_factor_curve_name))
        out.append(self._to_str(self.part_load_fraction_correlation_curve_name))
        out.append(self._to_str(self.minimum_drybulb_temperature_for_dehumidifier_operation))
        out.append(self._to_str(self.maximum_drybulb_temperature_for_dehumidifier_operation))
        out.append(self._to_str(self.offcycle_parasitic_electric_load))
        out.append(self._to_str(self.condensate_collection_water_storage_tank_name))
        return ",".join(out)

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchanger_name = None
        else:
            self.heat_exchanger_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate = None
        else:
            self.supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_flow_rate = None
        else:
            self.exhaust_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_fan_name = None
        else:
            self.exhaust_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controller_name = None
        else:
            self.controller_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_rate_per_unit_floor_area = None
        else:
            self.ventilation_rate_per_unit_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_rate_per_occupant = None
        else:
            self.ventilation_rate_per_occupant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
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
        """  Corresponds to IDD Field `heat_exchanger_name`
        Heat exchanger type must be HeatExchanger:AirToAir:SensibleAndLatent

        Args:
            value (str): value for IDD Field `heat_exchanger_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_flow_rate`
        This flow rate must match the supply fan's air flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate`
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
        """  Corresponds to IDD Field `exhaust_air_flow_rate`
        This flow rate must match the supply fan air flow rate.

        Args:
            value (float): value for IDD Field `exhaust_air_flow_rate`
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
        """  Corresponds to IDD Field `supply_air_fan_name`
        Fan type must be Fan:OnOff

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `exhaust_air_fan_name`
        Fan type must be Fan:OnOff

        Args:
            value (str): value for IDD Field `exhaust_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `controller_name`
        Enter the name of a ZoneHVAC:EnergyRecoveryVentilator:Controller object.

        Args:
            value (str): value for IDD Field `controller_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `ventilation_rate_per_unit_floor_area`
        0.000508 m3/s-m2 corresponds to 0.1 ft3/min-ft2
        Used only when supply and exhaust air flow rates are autosized.

        Args:
            value (float): value for IDD Field `ventilation_rate_per_unit_floor_area`
                Unit: m3/s-m2
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
        """  Corresponds to IDD Field `ventilation_rate_per_occupant`
        0.00236 m3/s-person corresponds to 5 ft3/min-person
        Used only when supply and exhaust air flow rates are autosized.

        Args:
            value (float): value for IDD Field `ventilation_rate_per_occupant`
                Unit: m3/s-person
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')

        self._data["Availability Manager List Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.heat_exchanger_name))
        out.append(self._to_str(self.supply_air_flow_rate))
        out.append(self._to_str(self.exhaust_air_flow_rate))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.exhaust_air_fan_name))
        out.append(self._to_str(self.controller_name))
        out.append(self._to_str(self.ventilation_rate_per_unit_floor_area))
        out.append(self._to_str(self.ventilation_rate_per_occupant))
        out.append(self._to_str(self.availability_manager_list_name))
        return ",".join(out)

class ZoneHvacEnergyRecoveryVentilatorController(object):
    """ Corresponds to IDD object `ZoneHVAC:EnergyRecoveryVentilator:Controller`
        This controller is used exclusively by the ZoneHVAC:EnergyRecoveryVentilator object
        to allow economizer (free cooling) operation when possible.
    """
    internal_name = "ZoneHVAC:EnergyRecoveryVentilator:Controller"
    field_count = 13

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
            self.temperature_high_limit = None
        else:
            self.temperature_high_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_low_limit = None
        else:
            self.temperature_low_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_high_limit = None
        else:
            self.enthalpy_high_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_limit = None
        else:
            self.dewpoint_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electronic_enthalpy_limit_curve_name = None
        else:
            self.electronic_enthalpy_limit_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_temperature_limit = None
        else:
            self.exhaust_air_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_enthalpy_limit = None
        else:
            self.exhaust_air_enthalpy_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_of_day_economizer_flow_control_schedule_name = None
        else:
            self.time_of_day_economizer_flow_control_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_humidity_control_flag = None
        else:
            self.high_humidity_control_flag = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidistat_control_zone_name = None
        else:
            self.humidistat_control_zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_humidity_outdoor_air_flow_ratio = None
        else:
            self.high_humidity_outdoor_air_flow_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = None
        else:
            self.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = vals[i]
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
    def temperature_high_limit(self):
        """Get temperature_high_limit

        Returns:
            float: the value of `temperature_high_limit` or None if not set
        """
        return self._data["Temperature High Limit"]

    @temperature_high_limit.setter
    def temperature_high_limit(self, value=None):
        """  Corresponds to IDD Field `temperature_high_limit`
        Enter the maximum outdoor dry-bulb temperature limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `temperature_high_limit`
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
        """  Corresponds to IDD Field `temperature_low_limit`
        Enter the minimum outdoor dry-bulb temperature limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `temperature_low_limit`
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
        """  Corresponds to IDD Field `enthalpy_high_limit`
        Enter the maximum outdoor enthalpy limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `enthalpy_high_limit`
                Unit: J/kg
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `dewpoint_temperature_limit`
        Enter the maximum outdoor dewpoint temperature limit for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (float): value for IDD Field `dewpoint_temperature_limit`
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
        """  Corresponds to IDD Field `electronic_enthalpy_limit_curve_name`
        Table:OneIndependentVariable object can also be used
        Enter the name of a quadratic or cubic curve which defines the maximum outdoor
        humidity ratio (function of outdoor dry-bulb temperature) for economizer operation.
        No input or blank input means this limit is not operative

        Args:
            value (str): value for IDD Field `electronic_enthalpy_limit_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `electronic_enthalpy_limit_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `exhaust_air_temperature_limit`

        Args:
            value (str): value for IDD Field `exhaust_air_temperature_limit`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_temperature_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_temperature_limit`')
            vals = set()
            vals.add("ExhaustAirTemperatureLimit")
            vals.add("NoExhaustAirTemperatureLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `exhaust_air_temperature_limit`'.format(value))

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
        """  Corresponds to IDD Field `exhaust_air_enthalpy_limit`

        Args:
            value (str): value for IDD Field `exhaust_air_enthalpy_limit`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_enthalpy_limit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_enthalpy_limit`')
            vals = set()
            vals.add("ExhaustAirEnthalpyLimit")
            vals.add("NoExhaustAirEnthalpyLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `exhaust_air_enthalpy_limit`'.format(value))

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
        """  Corresponds to IDD Field `time_of_day_economizer_flow_control_schedule_name`
        Schedule values greater than 0 indicate economizer operation is active. This
        schedule may be used with or without the High Humidity Control option.
        When used together, high humidity control has priority over economizer control.

        Args:
            value (str): value for IDD Field `time_of_day_economizer_flow_control_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_of_day_economizer_flow_control_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `high_humidity_control_flag`
        Select Yes to modify air flow rates based on a zone humidistat.
        Select No to disable this feature.

        Args:
            value (str): value for IDD Field `high_humidity_control_flag`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `high_humidity_control_flag`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `high_humidity_control_flag`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `high_humidity_control_flag`'.format(value))

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
        """  Corresponds to IDD Field `humidistat_control_zone_name`
        Enter the name of the zone where the humidistat is located.

        Args:
            value (str): value for IDD Field `humidistat_control_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `humidistat_control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def high_humidity_outdoor_air_flow_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `high_humidity_outdoor_air_flow_ratio`
        Enter the ratio of supply (outdoor) air to the maximum supply air flow rate when modified
        air flow rates are active based on high indoor humidity.

        Args:
            value (float): value for IDD Field `high_humidity_outdoor_air_flow_ratio`
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
        """  Corresponds to IDD Field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`
        If NO is selected, the air flow rate is modified any time indoor relative
        humidity is above humidistat setpoint. If YES is selected, outdoor air flow
        rate is modified any time indoor relative humidity is above the humidistat
        setpoint AND the outdoor humidity ratio is less than the indoor humidity ratio.

        Args:
            value (str): value for IDD Field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))

        self._data["Control High Indoor Humidity Based on Outdoor Humidity Ratio"] = value

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
        out.append(self._to_str(self.temperature_high_limit))
        out.append(self._to_str(self.temperature_low_limit))
        out.append(self._to_str(self.enthalpy_high_limit))
        out.append(self._to_str(self.dewpoint_temperature_limit))
        out.append(self._to_str(self.electronic_enthalpy_limit_curve_name))
        out.append(self._to_str(self.exhaust_air_temperature_limit))
        out.append(self._to_str(self.exhaust_air_enthalpy_limit))
        out.append(self._to_str(self.time_of_day_economizer_flow_control_schedule_name))
        out.append(self._to_str(self.high_humidity_control_flag))
        out.append(self._to_str(self.humidistat_control_zone_name))
        out.append(self._to_str(self.high_humidity_outdoor_air_flow_ratio))
        out.append(self._to_str(self.control_high_indoor_humidity_based_on_outdoor_humidity_ratio))
        return ",".join(out)

class ZoneHvacUnitVentilator(object):
    """ Corresponds to IDD object `ZoneHVAC:UnitVentilator`
        Unit ventilator. Forced-convection ventilation unit with supply fan (constant-volume
        or variable-volume), optional chilled water cooling coil, optional heating coil
        (gas, electric, hot water, or steam) and controllable outdoor air mixer.
    """
    internal_name = "ZoneHVAC:UnitVentilator"
    field_count = 25

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_control_type = None
        else:
            self.outdoor_air_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_flow_rate = None
        else:
            self.minimum_outdoor_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_schedule_name = None
        else:
            self.minimum_outdoor_air_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_fraction_or_temperature_schedule_name = None
        else:
            self.maximum_outdoor_air_fraction_or_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_node_name = None
        else:
            self.outdoor_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_node_name = None
        else:
            self.exhaust_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_air_node_name = None
        else:
            self.mixed_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coil_option = None
        else:
            self.coil_option = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
        """  Corresponds to IDD Field `maximum_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_supply_air_flow_rate`
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
        """  Corresponds to IDD Field `outdoor_air_control_type`

        Args:
            value (str): value for IDD Field `outdoor_air_control_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_control_type`')
            vals = set()
            vals.add("FixedAmount")
            vals.add("VariablePercent")
            vals.add("FixedTemperature")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_control_type`'.format(value))

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
        """  Corresponds to IDD Field `minimum_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `minimum_outdoor_air_flow_rate`
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
        """  Corresponds to IDD Field `minimum_outdoor_air_schedule_name`
        schedule values multiply the minimum outdoor air flow rate

        Args:
            value (str): value for IDD Field `minimum_outdoor_air_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `maximum_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_outdoor_air_flow_rate`
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
        """  Corresponds to IDD Field `maximum_outdoor_air_fraction_or_temperature_schedule_name`
        that this depends on the control type as to whether it is a fraction or temperature

        Args:
            value (str): value for IDD Field `maximum_outdoor_air_fraction_or_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_outdoor_air_fraction_or_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `air_inlet_node_name`

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
        """  Corresponds to IDD Field `mixed_air_node_name`
        inlet to coils

        Args:
            value (str): value for IDD Field `mixed_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Allowable fan types are Fan:ConstantVolume, Fan:OnOff and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            vals.add("Fan:VariableVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `coil_option`

        Args:
            value (str): value for IDD Field `coil_option`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `coil_option`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `coil_option`')
            vals = set()
            vals.add("None")
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("HeatingAndCooling")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `coil_option`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule that controls fan operation. Schedule
        name values of 0 denote cycling fan operation (fan cycles with
        cooling/heating coil). Schedule values greater than 0 denote
        constant fan operation (fan runs continually regardless of coil
        operation). The fan operating mode defaults to cycling fan operation
        if this input field is left blank.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `heating_coil_object_type`

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `heating_coil_name`

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def heating_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `heating_convergence_tolerance`

        Args:
            value (float): value for IDD Field `heating_convergence_tolerance`
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
            except:
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
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatExchangerAssisted")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `cooling_coil_name`

        Args:
            value (str): value for IDD Field `cooling_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def cooling_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `cooling_convergence_tolerance`

        Args:
            value (float): value for IDD Field `cooling_convergence_tolerance`
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
            except:
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.maximum_supply_air_flow_rate))
        out.append(self._to_str(self.outdoor_air_control_type))
        out.append(self._to_str(self.minimum_outdoor_air_flow_rate))
        out.append(self._to_str(self.minimum_outdoor_air_schedule_name))
        out.append(self._to_str(self.maximum_outdoor_air_flow_rate))
        out.append(self._to_str(self.maximum_outdoor_air_fraction_or_temperature_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.outdoor_air_node_name))
        out.append(self._to_str(self.exhaust_air_node_name))
        out.append(self._to_str(self.mixed_air_node_name))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.coil_option))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.heating_convergence_tolerance))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.cooling_convergence_tolerance))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacUnitHeater(object):
    """ Corresponds to IDD object `ZoneHVAC:UnitHeater`
        Unit heater. Forced-convection heating-only unit with supply fan, heating coil
        (gas, electric, hot water, or steam) and fixed-position outdoor air mixer.
    """
    internal_name = "ZoneHVAC:UnitHeater"
    field_count = 16

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_flow_rate = None
        else:
            self.maximum_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operation_during_no_heating = None
        else:
            self.supply_air_fan_operation_during_no_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`

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
        """  Corresponds to IDD Field `air_inlet_node_name`

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
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Allowable fan types are Fan:ConstantVolume, Fan:OnOff and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            vals.add("Fan:VariableVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `maximum_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_supply_air_flow_rate`
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
        """  Corresponds to IDD Field `heating_coil_object_type`

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `heating_coil_name`

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule that controls fan operation. Schedule
        name values of 0 denote cycling fan operation (fan cycles with the
        heating coil). Schedule values greater than 0 denote constant fan
        operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this
        input field is left blank.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_operation_during_no_heating`
        This choice field allows the user to define how the unit heater will operate
        under no heating load or cooling conditions. If the No is selected, then
        the fan will not run unless there is a heating load. If the fan does not run,
        this effectively shuts the unit heater system off when there is no heating load.
        If the Yes is selected, the unit heater is available and has a ConstantVolume
        fan, or has an OnOff fan with Supply Air Fan Operating Mode Schedule value
        greater than zero, then the fan will always run regardless of the zone load.

        Args:
            value (str): value for IDD Field `supply_air_fan_operation_during_no_heating`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operation_during_no_heating`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operation_during_no_heating`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_operation_during_no_heating`'.format(value))

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
        """  Corresponds to IDD Field `maximum_hot_water_or_steam_flow_rate`
        Not used when heating coil is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_or_steam_flow_rate`
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
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_or_steam_flow_rate`
        Not used when heating coil is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_or_steam_flow_rate`
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
    def heating_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `heating_convergence_tolerance`

        Args:
            value (float): value for IDD Field `heating_convergence_tolerance`
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
            except:
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.maximum_supply_air_flow_rate))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.supply_air_fan_operation_during_no_heating))
        out.append(self._to_str(self.maximum_hot_water_or_steam_flow_rate))
        out.append(self._to_str(self.minimum_hot_water_or_steam_flow_rate))
        out.append(self._to_str(self.heating_convergence_tolerance))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacEvaporativeCoolerUnit(object):
    """ Corresponds to IDD object `ZoneHVAC:EvaporativeCoolerUnit`
        Zone evaporative cooler. Forced-convection cooling-only unit with supply fan,
        100% outdoor air supply.  Optional relief exaust node
    """
    internal_name = "ZoneHVAC:EvaporativeCoolerUnit"
    field_count = 18

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooler_outlet_node_name = None
        else:
            self.cooler_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_relief_air_node_name = None
        else:
            self.zone_relief_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate = None
        else:
            self.design_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooler_unit_control_method = None
        else:
            self.cooler_unit_control_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.throttling_range_temperature_difference = None
        else:
            self.throttling_range_temperature_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_load_control_threshold_heat_transfer_rate = None
        else:
            self.cooling_load_control_threshold_heat_transfer_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.first_evaporative_cooler_object_type = None
        else:
            self.first_evaporative_cooler_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.first_evaporative_cooler_object_name = None
        else:
            self.first_evaporative_cooler_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.second_evaporative_cooler_object_type = None
        else:
            self.second_evaporative_cooler_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.second_evaporative_cooler_name = None
        else:
            self.second_evaporative_cooler_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`

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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `outdoor_air_inlet_node_name`
        this is an outdoor air node

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
    def cooler_outlet_node_name(self):
        """Get cooler_outlet_node_name

        Returns:
            str: the value of `cooler_outlet_node_name` or None if not set
        """
        return self._data["Cooler Outlet Node Name"]

    @cooler_outlet_node_name.setter
    def cooler_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `cooler_outlet_node_name`
        this is a zone inlet node

        Args:
            value (str): value for IDD Field `cooler_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooler_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `zone_relief_air_node_name`
        this is a zone exhaust node, optional if flow is being balanced elsewhere

        Args:
            value (str): value for IDD Field `zone_relief_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_relief_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_object_type`

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:ConstantVolume")
            vals.add("Fan:OnOff")
            vals.add("Fan:VariableVolume")
            vals.add("Fan:ComponentModel")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_name`

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate`
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
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

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
        """  Corresponds to IDD Field `cooler_unit_control_method`

        Args:
            value (str): value for IDD Field `cooler_unit_control_method`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooler_unit_control_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooler_unit_control_method`')
            vals = set()
            vals.add("ZoneTemperatureDeadbandOnOffCycling")
            vals.add("ZoneCoolingLoadOnOffCycling")
            vals.add("ZoneCoolingLoadVariableSpeedFan")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooler_unit_control_method`'.format(value))

        self._data["Cooler Unit Control Method"] = value

    @property
    def throttling_range_temperature_difference(self):
        """Get throttling_range_temperature_difference

        Returns:
            float: the value of `throttling_range_temperature_difference` or None if not set
        """
        return self._data["Throttling Range Temperature Difference"]

    @throttling_range_temperature_difference.setter
    def throttling_range_temperature_difference(self, value=1.0 ):
        """  Corresponds to IDD Field `throttling_range_temperature_difference`
        used for ZoneTemperatureDeadbandOnOffCycling hystersis range for thermostatic control

        Args:
            value (float): value for IDD Field `throttling_range_temperature_difference`
                Unit: deltaC
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
    def cooling_load_control_threshold_heat_transfer_rate(self, value=100.0 ):
        """  Corresponds to IDD Field `cooling_load_control_threshold_heat_transfer_rate`
        Sign convention is that positive values indicate a cooling load

        Args:
            value (float): value for IDD Field `cooling_load_control_threshold_heat_transfer_rate`
                Unit: W
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
            except:
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
        """  Corresponds to IDD Field `first_evaporative_cooler_object_type`

        Args:
            value (str): value for IDD Field `first_evaporative_cooler_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `first_evaporative_cooler_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `first_evaporative_cooler_object_type`')
            vals = set()
            vals.add("EvaporativeCooler:Direct:CelDekPad")
            vals.add("EvaporativeCooler:Direct:ResearchSpecial")
            vals.add("EvaporativeCooler:Indirect:CelDekPad")
            vals.add("EvaporativeCooler:Indirect:WetCoil")
            vals.add("EvaporativeCooler:Indirect:ResearchSpecial")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `first_evaporative_cooler_object_type`'.format(value))

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
        """  Corresponds to IDD Field `first_evaporative_cooler_object_name`

        Args:
            value (str): value for IDD Field `first_evaporative_cooler_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `first_evaporative_cooler_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `second_evaporative_cooler_object_type`
        optional, used for direct/indirect configurations
        second cooler must be immediately downstream of first cooler, if present

        Args:
            value (str): value for IDD Field `second_evaporative_cooler_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `second_evaporative_cooler_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `second_evaporative_cooler_object_type`')
            vals = set()
            vals.add("EvaporativeCooler:Direct:CelDekPad")
            vals.add("EvaporativeCooler:Direct:ResearchSpecial")
            vals.add("EvaporativeCooler:Indirect:CelDekPad")
            vals.add("EvaporativeCooler:Indirect:WetCoil")
            vals.add("EvaporativeCooler:Indirect:ResearchSpecial")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `second_evaporative_cooler_object_type`'.format(value))

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
        """  Corresponds to IDD Field `second_evaporative_cooler_name`
        optional, used for direct/indirect configurations

        Args:
            value (str): value for IDD Field `second_evaporative_cooler_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `second_evaporative_cooler_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.outdoor_air_inlet_node_name))
        out.append(self._to_str(self.cooler_outlet_node_name))
        out.append(self._to_str(self.zone_relief_air_node_name))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.design_supply_air_flow_rate))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.cooler_unit_control_method))
        out.append(self._to_str(self.throttling_range_temperature_difference))
        out.append(self._to_str(self.cooling_load_control_threshold_heat_transfer_rate))
        out.append(self._to_str(self.first_evaporative_cooler_object_type))
        out.append(self._to_str(self.first_evaporative_cooler_object_name))
        out.append(self._to_str(self.second_evaporative_cooler_object_type))
        out.append(self._to_str(self.second_evaporative_cooler_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)

class ZoneHvacOutdoorAirUnit(object):
    """ Corresponds to IDD object `ZoneHVAC:OutdoorAirUnit`
        The zone outdoor air unit models a single-zone dedicated outdoor air system (DOAS).
        Forced-convection 100% outdoor air unit with supply fan and optional equipment
        including exhaust fan, heating coil, cooling coil, and heat recovery.
    """
    internal_name = "ZoneHVAC:OutdoorAirUnit"
    field_count = 19

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate = None
        else:
            self.outdoor_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_schedule_name = None
        else:
            self.outdoor_air_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_name = None
        else:
            self.supply_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_placement = None
        else:
            self.supply_fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_fan_name = None
        else:
            self.exhaust_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_flow_rate = None
        else:
            self.exhaust_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_schedule_name = None
        else:
            self.exhaust_air_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.unit_control_type = None
        else:
            self.unit_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_air_control_temperature_schedule_name = None
        else:
            self.high_air_control_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_air_control_temperature_schedule_name = None
        else:
            self.low_air_control_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_node_name = None
        else:
            self.outdoor_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airoutlet_node_name = None
        else:
            self.airoutlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airinlet_node_name = None
        else:
            self.airinlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fanoutlet_node_name = None
        else:
            self.supply_fanoutlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_unit_list_name = None
        else:
            self.outdoor_air_unit_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
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
        """  Corresponds to IDD Field `zone_name`
        (name of zone system is serving)

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate`
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
        """  Corresponds to IDD Field `outdoor_air_schedule_name`

        Args:
            value (str): value for IDD Field `outdoor_air_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_fan_name`
        Allowable fan types are Fan:ConstantVolume and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `supply_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_fan_placement`

        Args:
            value (str): value for IDD Field `supply_fan_placement`
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
                                 'for field `supply_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_fan_placement`'.format(value))

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
        """  Corresponds to IDD Field `exhaust_fan_name`
        Allowable fan types are Fan:ConstantVolume and
        Fan:VariableVolume

        Args:
            value (str): value for IDD Field `exhaust_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `exhaust_air_flow_rate`

        Args:
            value (float): value for IDD Field `exhaust_air_flow_rate`
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
        """  Corresponds to IDD Field `exhaust_air_schedule_name`

        Args:
            value (str): value for IDD Field `exhaust_air_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `unit_control_type`

        Args:
            value (str): value for IDD Field `unit_control_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `unit_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unit_control_type`')
            vals = set()
            vals.add("NeutralControl")
            vals.add("TemperatureControl")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `unit_control_type`'.format(value))

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
        """  Corresponds to IDD Field `high_air_control_temperature_schedule_name`
        Air and control temperatures for cooling. If outdoor air temperature
        is above the high air control temperature, then the zone inlet air temperature
        is set to the high air control temperature. If the outdoor air is between high and low
        air control temperature, then there is no cooling/heating requirements.

        Args:
            value (str): value for IDD Field `high_air_control_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `high_air_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `low_air_control_temperature_schedule_name`
        Air and control temperatures for Heating. If outdoor air temperature
        is below the low air control temperature, then the zone inlet air temperature
        is set to the low air control temperature. If the outdoor air is between high and low
        air control temperature, then there is no cooling/heating requirements.

        Args:
            value (str): value for IDD Field `low_air_control_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `low_air_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `outdoor_air_node_name`

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
        """  Corresponds to IDD Field `airoutlet_node_name`

        Args:
            value (str): value for IDD Field `airoutlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airoutlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `airinlet_node_name`
        air leaves zone

        Args:
            value (str): value for IDD Field `airinlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airinlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_fanoutlet_node_name`

        Args:
            value (str): value for IDD Field `supply_fanoutlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fanoutlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `outdoor_air_unit_list_name`
        Enter the name of an ZoneHVAC:OutdoorAirUnit:EquipmentList object.

        Args:
            value (str): value for IDD Field `outdoor_air_unit_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_unit_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')

        self._data["Availability Manager List Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.outdoor_air_flow_rate))
        out.append(self._to_str(self.outdoor_air_schedule_name))
        out.append(self._to_str(self.supply_fan_name))
        out.append(self._to_str(self.supply_fan_placement))
        out.append(self._to_str(self.exhaust_fan_name))
        out.append(self._to_str(self.exhaust_air_flow_rate))
        out.append(self._to_str(self.exhaust_air_schedule_name))
        out.append(self._to_str(self.unit_control_type))
        out.append(self._to_str(self.high_air_control_temperature_schedule_name))
        out.append(self._to_str(self.low_air_control_temperature_schedule_name))
        out.append(self._to_str(self.outdoor_air_node_name))
        out.append(self._to_str(self.airoutlet_node_name))
        out.append(self._to_str(self.airinlet_node_name))
        out.append(self._to_str(self.supply_fanoutlet_node_name))
        out.append(self._to_str(self.outdoor_air_unit_list_name))
        out.append(self._to_str(self.availability_manager_list_name))
        return ",".join(out)

class ZoneHvacOutdoorAirUnitEquipmentList(object):
    """ Corresponds to IDD object `ZoneHVAC:OutdoorAirUnit:EquipmentList`
        Equipment list for components in a ZoneHVAC:OutdoorAirUnit. Components are simulated
        sequentially in the order given in the equipment list.
    """
    internal_name = "ZoneHVAC:OutdoorAirUnit:EquipmentList"
    field_count = 17

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
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
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
    def component_1_object_type(self):
        """Get component_1_object_type

        Returns:
            str: the value of `component_1_object_type` or None if not set
        """
        return self._data["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """  Corresponds to IDD Field `component_1_object_type`

        Args:
            value (str): value for IDD Field `component_1_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_1_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_1_name`

        Args:
            value (str): value for IDD Field `component_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_2_object_type`

        Args:
            value (str): value for IDD Field `component_2_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_2_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_2_name`

        Args:
            value (str): value for IDD Field `component_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_3_object_type`

        Args:
            value (str): value for IDD Field `component_3_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_3_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_3_name`

        Args:
            value (str): value for IDD Field `component_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_4_object_type`

        Args:
            value (str): value for IDD Field `component_4_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_4_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_4_name`

        Args:
            value (str): value for IDD Field `component_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_5_object_type`

        Args:
            value (str): value for IDD Field `component_5_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_5_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_5_name`

        Args:
            value (str): value for IDD Field `component_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_6_object_type`

        Args:
            value (str): value for IDD Field `component_6_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_6_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_6_name`

        Args:
            value (str): value for IDD Field `component_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_7_object_type`

        Args:
            value (str): value for IDD Field `component_7_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_7_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_7_name`

        Args:
            value (str): value for IDD Field `component_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_8_object_type`

        Args:
            value (str): value for IDD Field `component_8_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatexchangerAssisted")
            vals.add("CoilSystem:Cooling:DX")
            vals.add("CoilSystem:Heating:DX")
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("Dehumidifier:Desiccant:NoFans")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_8_object_type`'.format(value))

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
        """  Corresponds to IDD Field `component_8_name`

        Args:
            value (str): value for IDD Field `component_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')

        self._data["Component 8 Name"] = value

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
        out.append(self._to_str(self.component_1_object_type))
        out.append(self._to_str(self.component_1_name))
        out.append(self._to_str(self.component_2_object_type))
        out.append(self._to_str(self.component_2_name))
        out.append(self._to_str(self.component_3_object_type))
        out.append(self._to_str(self.component_3_name))
        out.append(self._to_str(self.component_4_object_type))
        out.append(self._to_str(self.component_4_name))
        out.append(self._to_str(self.component_5_object_type))
        out.append(self._to_str(self.component_5_name))
        out.append(self._to_str(self.component_6_object_type))
        out.append(self._to_str(self.component_6_name))
        out.append(self._to_str(self.component_7_object_type))
        out.append(self._to_str(self.component_7_name))
        out.append(self._to_str(self.component_8_object_type))
        out.append(self._to_str(self.component_8_name))
        return ",".join(out)

class ZoneHvacTerminalUnitVariableRefrigerantFlow(object):
    """ Corresponds to IDD object `ZoneHVAC:TerminalUnit:VariableRefrigerantFlow`
        Zone terminal unit with variable refrigerant flow (VRF) DX cooling and heating coils
        (air-to-air heat pump). The VRF terminal units are served by an
        AirConditioner:VariableRefrigerantFlow system.
    """
    internal_name = "ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"
    field_count = 26

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

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name = None
        else:
            self.zone_terminal_unit_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.terminal_unit_availability_schedule = None
        else:
            self.terminal_unit_availability_schedule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.terminal_unit_air_inlet_node_name = None
        else:
            self.terminal_unit_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.terminal_unit_air_outlet_node_name = None
        else:
            self.terminal_unit_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_placement = None
        else:
            self.supply_air_fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_name = None
        else:
            self.supply_air_fan_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_air_mixer_object_type = None
        else:
            self.outside_air_mixer_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_air_mixer_object_name = None
        else:
            self.outside_air_mixer_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_name = None
        else:
            self.cooling_coil_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_object_name = None
        else:
            self.heating_coil_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_on_parasitic_electric_energy_use = None
        else:
            self.zone_terminal_unit_on_parasitic_electric_energy_use = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_off_parasitic_electric_energy_use = None
        else:
            self.zone_terminal_unit_off_parasitic_electric_energy_use = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_heating_capacity_sizing_ratio = None
        else:
            self.rated_heating_capacity_sizing_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
        i += 1

    @property
    def zone_terminal_unit_name(self):
        """Get zone_terminal_unit_name

        Returns:
            str: the value of `zone_terminal_unit_name` or None if not set
        """
        return self._data["Zone Terminal Unit Name"]

    @zone_terminal_unit_name.setter
    def zone_terminal_unit_name(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `terminal_unit_availability_schedule`
        The unit is available the entire simulation if this field is left blank
        Schedule values of 0 denote the unit is off.

        Args:
            value (str): value for IDD Field `terminal_unit_availability_schedule`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_availability_schedule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `terminal_unit_air_inlet_node_name`
        the inlet node to the terminal unit

        Args:
            value (str): value for IDD Field `terminal_unit_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `terminal_unit_air_outlet_node_name`
        the outlet node of the terminal unit

        Args:
            value (str): value for IDD Field `terminal_unit_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_is_needed`

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_is_needed`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_heating_is_needed`

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_heating_is_needed`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_cooling_operation`

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_cooling_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_heating_operation`

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_heating_operation`
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
        """  Corresponds to IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
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
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_air_fan_placement`
        Select fan placement as either blow through or draw through.

        Args:
            value (str): value for IDD Field `supply_air_fan_placement`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_placement`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_object_type`

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

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
        """  Corresponds to IDD Field `supply_air_fan_object_name`

        Args:
            value (str): value for IDD Field `supply_air_fan_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `outside_air_mixer_object_type`
        If this field is blank, and outside air mixer is not used.

        Args:
            value (str): value for IDD Field `outside_air_mixer_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outside_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_air_mixer_object_type`')
            vals = set()
            vals.add("OutdoorAir:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outside_air_mixer_object_type`'.format(value))

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
        """  Corresponds to IDD Field `outside_air_mixer_object_name`
        If this field is blank, and outside air mixer is not used.

        Args:
            value (str): value for IDD Field `outside_air_mixer_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outside_air_mixer_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `cooling_coil_object_type`
        Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow
        This field may be left blank if heating-only mode is used

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:VariableRefrigerantFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `cooling_coil_object_name`
        Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow
        This field may be left blank if heating-only mode is used

        Args:
            value (str): value for IDD Field `cooling_coil_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `heating_coil_object_type`
        Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow
        This field may be left blank if cooling-only mode is used

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:DX:VariableRefrigerantFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `heating_coil_object_name`
        Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow
        This field may be left blank if cooling-only mode is used

        Args:
            value (str): value for IDD Field `heating_coil_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
    def zone_terminal_unit_on_parasitic_electric_energy_use(self, value=0.0 ):
        """  Corresponds to IDD Field `zone_terminal_unit_on_parasitic_electric_energy_use`

        Args:
            value (float): value for IDD Field `zone_terminal_unit_on_parasitic_electric_energy_use`
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
    def zone_terminal_unit_off_parasitic_electric_energy_use(self, value=0.0 ):
        """  Corresponds to IDD Field `zone_terminal_unit_off_parasitic_electric_energy_use`

        Args:
            value (float): value for IDD Field `zone_terminal_unit_off_parasitic_electric_energy_use`
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
    def rated_heating_capacity_sizing_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `rated_heating_capacity_sizing_ratio`
        If this terminal unit's heating coil is autosized, the heating capacity is sized
        to be equal to the cooling capacity multiplied by this sizing ratio.
        This input applies to the terminal unit heating coil and overrides the sizing
        ratio entered in the AirConditioner:VariableRefrigerantFlow object.

        Args:
            value (float): value for IDD Field `rated_heating_capacity_sizing_ratio`
                Unit: W/W
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
            except:
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
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `design_specification_zonehvac_sizing_object_name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `design_specification_zonehvac_sizing_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zonehvac_sizing_object_name`')

        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

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
        out.append(self._to_str(self.zone_terminal_unit_name))
        out.append(self._to_str(self.terminal_unit_availability_schedule))
        out.append(self._to_str(self.terminal_unit_air_inlet_node_name))
        out.append(self._to_str(self.terminal_unit_air_outlet_node_name))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_is_needed))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_heating_is_needed))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.supply_air_fan_placement))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_object_name))
        out.append(self._to_str(self.outside_air_mixer_object_type))
        out.append(self._to_str(self.outside_air_mixer_object_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_object_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_object_name))
        out.append(self._to_str(self.zone_terminal_unit_on_parasitic_electric_energy_use))
        out.append(self._to_str(self.zone_terminal_unit_off_parasitic_electric_energy_use))
        out.append(self._to_str(self.rated_heating_capacity_sizing_ratio))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_specification_zonehvac_sizing_object_name))
        return ",".join(out)