from collections import OrderedDict

class SizingParameters(object):
    """ Corresponds to IDD object `Sizing:Parameters`
        Specifies global heating and cooling sizing factors/ratios.
        These ratios are applied at the zone level to all of the zone heating and cooling loads
        and air flow rates. Then these new loads and air flow rates are used to calculate the
        system level flow rates and capacities and are used in all component sizing calculations.
        Specifies the width (in load timesteps) of a moving average window
        which is used to smooth the peak load across more than one timestep.
    """
    internal_name = "Sizing:Parameters"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Sizing:Parameters`
        """
        self._data = OrderedDict()
        self._data["Heating Sizing Factor"] = None
        self._data["Cooling Sizing Factor"] = None
        self._data["Timesteps in Averaging Window"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.heating_sizing_factor = None
        else:
            self.heating_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_sizing_factor = None
        else:
            self.cooling_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.timesteps_in_averaging_window = None
        else:
            self.timesteps_in_averaging_window = vals[i]
        i += 1

    @property
    def heating_sizing_factor(self):
        """Get heating_sizing_factor

        Returns:
            float: the value of `heating_sizing_factor` or None if not set
        """
        return self._data["Heating Sizing Factor"]

    @heating_sizing_factor.setter
    def heating_sizing_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `heating_sizing_factor`

        Args:
            value (float): value for IDD Field `heating_sizing_factor`
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
                                 'for field `heating_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_sizing_factor`')

        self._data["Heating Sizing Factor"] = value

    @property
    def cooling_sizing_factor(self):
        """Get cooling_sizing_factor

        Returns:
            float: the value of `cooling_sizing_factor` or None if not set
        """
        return self._data["Cooling Sizing Factor"]

    @cooling_sizing_factor.setter
    def cooling_sizing_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `cooling_sizing_factor`

        Args:
            value (float): value for IDD Field `cooling_sizing_factor`
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
                                 'for field `cooling_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_sizing_factor`')

        self._data["Cooling Sizing Factor"] = value

    @property
    def timesteps_in_averaging_window(self):
        """Get timesteps_in_averaging_window

        Returns:
            int: the value of `timesteps_in_averaging_window` or None if not set
        """
        return self._data["Timesteps in Averaging Window"]

    @timesteps_in_averaging_window.setter
    def timesteps_in_averaging_window(self, value=None):
        """  Corresponds to IDD Field `timesteps_in_averaging_window`
        blank => set the timesteps in averaging window to
        Number of Timesteps per Hour resulting in a 1 hour averaging window
        default is number of timesteps for 1 hour averaging window

        Args:
            value (int): value for IDD Field `timesteps_in_averaging_window`
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
                                 'for field `timesteps_in_averaging_window`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `timesteps_in_averaging_window`')

        self._data["Timesteps in Averaging Window"] = value

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
        out.append(self._to_str(self.heating_sizing_factor))
        out.append(self._to_str(self.cooling_sizing_factor))
        out.append(self._to_str(self.timesteps_in_averaging_window))
        return ",".join(out)

class SizingZone(object):
    """ Corresponds to IDD object `Sizing:Zone`
        Specifies the data needed to perform a zone design air flow calculation.
        The calculation is done for every sizing period included in the input. The maximum
        cooling and heating load and cooling, heating, and ventilation air flows are then saved
        for system level and zone component design calculations.
    """
    internal_name = "Sizing:Zone"
    field_count = 23

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Sizing:Zone`
        """
        self._data = OrderedDict()
        self._data["Zone or ZoneList Name"] = None
        self._data["Zone Cooling Design Supply Air Temperature Input Method"] = None
        self._data["Zone Cooling Design Supply Air Temperature"] = None
        self._data["Zone Cooling Design Supply Air Temperature Difference"] = None
        self._data["Zone Heating Design Supply Air Temperature Input Method"] = None
        self._data["Zone Heating Design Supply Air Temperature"] = None
        self._data["Zone Heating Design Supply Air Temperature Difference"] = None
        self._data["Zone Cooling Design Supply Air Humidity Ratio"] = None
        self._data["Zone Heating Design Supply Air Humidity Ratio"] = None
        self._data["Design Specification Outdoor Air Object Name"] = None
        self._data["Zone Heating Sizing Factor"] = None
        self._data["Zone Cooling Sizing Factor"] = None
        self._data["Cooling Design Air Flow Method"] = None
        self._data["Cooling Design Air Flow Rate"] = None
        self._data["Cooling Minimum Air Flow per Zone Floor Area"] = None
        self._data["Cooling Minimum Air Flow"] = None
        self._data["Cooling Minimum Air Flow Fraction"] = None
        self._data["Heating Design Air Flow Method"] = None
        self._data["Heating Design Air Flow Rate"] = None
        self._data["Heating Maximum Air Flow per Zone Floor Area"] = None
        self._data["Heating Maximum Air Flow"] = None
        self._data["Heating Maximum Air Flow Fraction"] = None
        self._data["Design Specification Zone Air Distribution Object Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_temperature_input_method = None
        else:
            self.zone_cooling_design_supply_air_temperature_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_temperature = None
        else:
            self.zone_cooling_design_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_temperature_difference = None
        else:
            self.zone_cooling_design_supply_air_temperature_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_temperature_input_method = None
        else:
            self.zone_heating_design_supply_air_temperature_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_temperature = None
        else:
            self.zone_heating_design_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_temperature_difference = None
        else:
            self.zone_heating_design_supply_air_temperature_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_humidity_ratio = None
        else:
            self.zone_cooling_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_humidity_ratio = None
        else:
            self.zone_heating_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_heating_sizing_factor = None
        else:
            self.zone_heating_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_cooling_sizing_factor = None
        else:
            self.zone_cooling_sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_method = None
        else:
            self.cooling_design_air_flow_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_rate = None
        else:
            self.cooling_design_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_minimum_air_flow_per_zone_floor_area = None
        else:
            self.cooling_minimum_air_flow_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_minimum_air_flow = None
        else:
            self.cooling_minimum_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_minimum_air_flow_fraction = None
        else:
            self.cooling_minimum_air_flow_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_air_flow_method = None
        else:
            self.heating_design_air_flow_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_air_flow_rate = None
        else:
            self.heating_design_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_maximum_air_flow_per_zone_floor_area = None
        else:
            self.heating_maximum_air_flow_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_maximum_air_flow = None
        else:
            self.heating_maximum_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_maximum_air_flow_fraction = None
        else:
            self.heating_maximum_air_flow_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name = None
        else:
            self.design_specification_zone_air_distribution_object_name = vals[i]
        i += 1

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `zone_or_zonelist_name`

        Args:
            value (str): value for IDD Field `zone_or_zonelist_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_or_zonelist_name`')

        self._data["Zone or ZoneList Name"] = value

    @property
    def zone_cooling_design_supply_air_temperature_input_method(self):
        """Get zone_cooling_design_supply_air_temperature_input_method

        Returns:
            str: the value of `zone_cooling_design_supply_air_temperature_input_method` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Temperature Input Method"]

    @zone_cooling_design_supply_air_temperature_input_method.setter
    def zone_cooling_design_supply_air_temperature_input_method(self, value="SupplyAirTemperature"):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_temperature_input_method`

        Args:
            value (str): value for IDD Field `zone_cooling_design_supply_air_temperature_input_method`
                Accepted values are:
                      - SupplyAirTemperature
                      - TemperatureDifference
                Default value: SupplyAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_cooling_design_supply_air_temperature_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_cooling_design_supply_air_temperature_input_method`')
            vals = set()
            vals.add("SupplyAirTemperature")
            vals.add("TemperatureDifference")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `zone_cooling_design_supply_air_temperature_input_method`'.format(value))

        self._data["Zone Cooling Design Supply Air Temperature Input Method"] = value

    @property
    def zone_cooling_design_supply_air_temperature(self):
        """Get zone_cooling_design_supply_air_temperature

        Returns:
            float: the value of `zone_cooling_design_supply_air_temperature` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Temperature"]

    @zone_cooling_design_supply_air_temperature.setter
    def zone_cooling_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_temperature`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `zone_cooling_design_supply_air_temperature`
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
                                 'for field `zone_cooling_design_supply_air_temperature`'.format(value))

        self._data["Zone Cooling Design Supply Air Temperature"] = value

    @property
    def zone_cooling_design_supply_air_temperature_difference(self):
        """Get zone_cooling_design_supply_air_temperature_difference

        Returns:
            float: the value of `zone_cooling_design_supply_air_temperature_difference` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Temperature Difference"]

    @zone_cooling_design_supply_air_temperature_difference.setter
    def zone_cooling_design_supply_air_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_temperature_difference`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be subtracted from the zone temperature
        at peak load to calculate the Zone Cooling Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `zone_cooling_design_supply_air_temperature_difference`
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
                                 'for field `zone_cooling_design_supply_air_temperature_difference`'.format(value))

        self._data["Zone Cooling Design Supply Air Temperature Difference"] = value

    @property
    def zone_heating_design_supply_air_temperature_input_method(self):
        """Get zone_heating_design_supply_air_temperature_input_method

        Returns:
            str: the value of `zone_heating_design_supply_air_temperature_input_method` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Temperature Input Method"]

    @zone_heating_design_supply_air_temperature_input_method.setter
    def zone_heating_design_supply_air_temperature_input_method(self, value="SupplyAirTemperature"):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_temperature_input_method`

        Args:
            value (str): value for IDD Field `zone_heating_design_supply_air_temperature_input_method`
                Accepted values are:
                      - SupplyAirTemperature
                      - TemperatureDifference
                Default value: SupplyAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_heating_design_supply_air_temperature_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_heating_design_supply_air_temperature_input_method`')
            vals = set()
            vals.add("SupplyAirTemperature")
            vals.add("TemperatureDifference")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `zone_heating_design_supply_air_temperature_input_method`'.format(value))

        self._data["Zone Heating Design Supply Air Temperature Input Method"] = value

    @property
    def zone_heating_design_supply_air_temperature(self):
        """Get zone_heating_design_supply_air_temperature

        Returns:
            float: the value of `zone_heating_design_supply_air_temperature` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Temperature"]

    @zone_heating_design_supply_air_temperature.setter
    def zone_heating_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_temperature`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `zone_heating_design_supply_air_temperature`
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
                                 'for field `zone_heating_design_supply_air_temperature`'.format(value))

        self._data["Zone Heating Design Supply Air Temperature"] = value

    @property
    def zone_heating_design_supply_air_temperature_difference(self):
        """Get zone_heating_design_supply_air_temperature_difference

        Returns:
            float: the value of `zone_heating_design_supply_air_temperature_difference` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Temperature Difference"]

    @zone_heating_design_supply_air_temperature_difference.setter
    def zone_heating_design_supply_air_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_temperature_difference`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be added to the zone temperature
        at peak load to calculate the Zone Heating Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `zone_heating_design_supply_air_temperature_difference`
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
                                 'for field `zone_heating_design_supply_air_temperature_difference`'.format(value))

        self._data["Zone Heating Design Supply Air Temperature Difference"] = value

    @property
    def zone_cooling_design_supply_air_humidity_ratio(self):
        """Get zone_cooling_design_supply_air_humidity_ratio

        Returns:
            float: the value of `zone_cooling_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Humidity Ratio"]

    @zone_cooling_design_supply_air_humidity_ratio.setter
    def zone_cooling_design_supply_air_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `zone_cooling_design_supply_air_humidity_ratio`
                Unit: kgWater/kgDryAir
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
                                 'for field `zone_cooling_design_supply_air_humidity_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_cooling_design_supply_air_humidity_ratio`')

        self._data["Zone Cooling Design Supply Air Humidity Ratio"] = value

    @property
    def zone_heating_design_supply_air_humidity_ratio(self):
        """Get zone_heating_design_supply_air_humidity_ratio

        Returns:
            float: the value of `zone_heating_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Humidity Ratio"]

    @zone_heating_design_supply_air_humidity_ratio.setter
    def zone_heating_design_supply_air_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `zone_heating_design_supply_air_humidity_ratio`
                Unit: kgWater/kgDryAir
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
                                 'for field `zone_heating_design_supply_air_humidity_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_heating_design_supply_air_humidity_ratio`')

        self._data["Zone Heating Design Supply Air Humidity Ratio"] = value

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
    def zone_heating_sizing_factor(self):
        """Get zone_heating_sizing_factor

        Returns:
            float: the value of `zone_heating_sizing_factor` or None if not set
        """
        return self._data["Zone Heating Sizing Factor"]

    @zone_heating_sizing_factor.setter
    def zone_heating_sizing_factor(self, value=None):
        """  Corresponds to IDD Field `zone_heating_sizing_factor`
        if blank or zero, global heating sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `zone_heating_sizing_factor`
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
                                 'for field `zone_heating_sizing_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_heating_sizing_factor`')

        self._data["Zone Heating Sizing Factor"] = value

    @property
    def zone_cooling_sizing_factor(self):
        """Get zone_cooling_sizing_factor

        Returns:
            float: the value of `zone_cooling_sizing_factor` or None if not set
        """
        return self._data["Zone Cooling Sizing Factor"]

    @zone_cooling_sizing_factor.setter
    def zone_cooling_sizing_factor(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_sizing_factor`
        if blank or zero, global cooling sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `zone_cooling_sizing_factor`
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
                                 'for field `zone_cooling_sizing_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_cooling_sizing_factor`')

        self._data["Zone Cooling Sizing Factor"] = value

    @property
    def cooling_design_air_flow_method(self):
        """Get cooling_design_air_flow_method

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set
        """
        return self._data["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `cooling_design_air_flow_method`

        Args:
            value (str): value for IDD Field `cooling_design_air_flow_method`
                Accepted values are:
                      - Flow/Zone
                      - DesignDay
                      - DesignDayWithLimit
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_air_flow_method`')
            vals = set()
            vals.add("Flow/Zone")
            vals.add("DesignDay")
            vals.add("DesignDayWithLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_design_air_flow_method`'.format(value))

        self._data["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_air_flow_rate(self):
        """Get cooling_design_air_flow_rate

        Returns:
            float: the value of `cooling_design_air_flow_rate` or None if not set
        """
        return self._data["Cooling Design Air Flow Rate"]

    @cooling_design_air_flow_rate.setter
    def cooling_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_design_air_flow_rate`
        This input is used if Cooling Design Air Flow Method is Flow/Zone
        This value will be multiplied by the global or zone sizing factor and
        by zone multipliers.

        Args:
            value (float): value for IDD Field `cooling_design_air_flow_rate`
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
                                 'for field `cooling_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_air_flow_rate`')

        self._data["Cooling Design Air Flow Rate"] = value

    @property
    def cooling_minimum_air_flow_per_zone_floor_area(self):
        """Get cooling_minimum_air_flow_per_zone_floor_area

        Returns:
            float: the value of `cooling_minimum_air_flow_per_zone_floor_area` or None if not set
        """
        return self._data["Cooling Minimum Air Flow per Zone Floor Area"]

    @cooling_minimum_air_flow_per_zone_floor_area.setter
    def cooling_minimum_air_flow_per_zone_floor_area(self, value=0.000762 ):
        """  Corresponds to IDD Field `cooling_minimum_air_flow_per_zone_floor_area`
        default is .15 cfm/ft2
        This input is used if Cooling Design Air Flow Method is DesignDayWithLimit

        Args:
            value (float): value for IDD Field `cooling_minimum_air_flow_per_zone_floor_area`
                Unit: m3/s-m2
                Default value: 0.000762
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
                                 'for field `cooling_minimum_air_flow_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_minimum_air_flow_per_zone_floor_area`')

        self._data["Cooling Minimum Air Flow per Zone Floor Area"] = value

    @property
    def cooling_minimum_air_flow(self):
        """Get cooling_minimum_air_flow

        Returns:
            float: the value of `cooling_minimum_air_flow` or None if not set
        """
        return self._data["Cooling Minimum Air Flow"]

    @cooling_minimum_air_flow.setter
    def cooling_minimum_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_minimum_air_flow`
        This input is used if Cooling Design Air Flow Method is DesignDayWithLimit

        Args:
            value (float): value for IDD Field `cooling_minimum_air_flow`
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
                                 'for field `cooling_minimum_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_minimum_air_flow`')

        self._data["Cooling Minimum Air Flow"] = value

    @property
    def cooling_minimum_air_flow_fraction(self):
        """Get cooling_minimum_air_flow_fraction

        Returns:
            float: the value of `cooling_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Cooling Minimum Air Flow Fraction"]

    @cooling_minimum_air_flow_fraction.setter
    def cooling_minimum_air_flow_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_minimum_air_flow_fraction`
        fraction of the Cooling design Air Flow Rate
        This input is currently used in sizing the Fan minimum Flow Rate.
        It does not currently affect other component autosizing.

        Args:
            value (float): value for IDD Field `cooling_minimum_air_flow_fraction`
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
                                 'for field `cooling_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_minimum_air_flow_fraction`')

        self._data["Cooling Minimum Air Flow Fraction"] = value

    @property
    def heating_design_air_flow_method(self):
        """Get heating_design_air_flow_method

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set
        """
        return self._data["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `heating_design_air_flow_method`

        Args:
            value (str): value for IDD Field `heating_design_air_flow_method`
                Accepted values are:
                      - Flow/Zone
                      - DesignDay
                      - DesignDayWithLimit
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_air_flow_method`')
            vals = set()
            vals.add("Flow/Zone")
            vals.add("DesignDay")
            vals.add("DesignDayWithLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_design_air_flow_method`'.format(value))

        self._data["Heating Design Air Flow Method"] = value

    @property
    def heating_design_air_flow_rate(self):
        """Get heating_design_air_flow_rate

        Returns:
            float: the value of `heating_design_air_flow_rate` or None if not set
        """
        return self._data["Heating Design Air Flow Rate"]

    @heating_design_air_flow_rate.setter
    def heating_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `heating_design_air_flow_rate`
        This input is used if Heating Design Air Flow Method is Flow/Zone.
        This value will be multiplied by the global or zone sizing factor and
        by zone multipliers.

        Args:
            value (float): value for IDD Field `heating_design_air_flow_rate`
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
                                 'for field `heating_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_air_flow_rate`')

        self._data["Heating Design Air Flow Rate"] = value

    @property
    def heating_maximum_air_flow_per_zone_floor_area(self):
        """Get heating_maximum_air_flow_per_zone_floor_area

        Returns:
            float: the value of `heating_maximum_air_flow_per_zone_floor_area` or None if not set
        """
        return self._data["Heating Maximum Air Flow per Zone Floor Area"]

    @heating_maximum_air_flow_per_zone_floor_area.setter
    def heating_maximum_air_flow_per_zone_floor_area(self, value=0.002032 ):
        """  Corresponds to IDD Field `heating_maximum_air_flow_per_zone_floor_area`
        default is .40 cfm/ft2
        This field is used to size the heating design flow rate when Heating Design Air Flow Method = Flow/Zone.
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `heating_maximum_air_flow_per_zone_floor_area`
                Unit: m3/s-m2
                Default value: 0.002032
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
                                 'for field `heating_maximum_air_flow_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_maximum_air_flow_per_zone_floor_area`')

        self._data["Heating Maximum Air Flow per Zone Floor Area"] = value

    @property
    def heating_maximum_air_flow(self):
        """Get heating_maximum_air_flow

        Returns:
            float: the value of `heating_maximum_air_flow` or None if not set
        """
        return self._data["Heating Maximum Air Flow"]

    @heating_maximum_air_flow.setter
    def heating_maximum_air_flow(self, value=0.1415762 ):
        """  Corresponds to IDD Field `heating_maximum_air_flow`
        default is 300 cfm
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `heating_maximum_air_flow`
                Unit: m3/s
                Default value: 0.1415762
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
                                 'for field `heating_maximum_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_maximum_air_flow`')

        self._data["Heating Maximum Air Flow"] = value

    @property
    def heating_maximum_air_flow_fraction(self):
        """Get heating_maximum_air_flow_fraction

        Returns:
            float: the value of `heating_maximum_air_flow_fraction` or None if not set
        """
        return self._data["Heating Maximum Air Flow Fraction"]

    @heating_maximum_air_flow_fraction.setter
    def heating_maximum_air_flow_fraction(self, value=0.3 ):
        """  Corresponds to IDD Field `heating_maximum_air_flow_fraction`
        fraction of the Heating Design Air Flow Rate
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `heating_maximum_air_flow_fraction`
                Default value: 0.3
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
                                 'for field `heating_maximum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_maximum_air_flow_fraction`')

        self._data["Heating Maximum Air Flow Fraction"] = value

    @property
    def design_specification_zone_air_distribution_object_name(self):
        """Get design_specification_zone_air_distribution_object_name

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name"]

    @design_specification_zone_air_distribution_object_name.setter
    def design_specification_zone_air_distribution_object_name(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zone_air_distribution_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name`')

        self._data["Design Specification Zone Air Distribution Object Name"] = value

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
        out.append(self._to_str(self.zone_or_zonelist_name))
        out.append(self._to_str(self.zone_cooling_design_supply_air_temperature_input_method))
        out.append(self._to_str(self.zone_cooling_design_supply_air_temperature))
        out.append(self._to_str(self.zone_cooling_design_supply_air_temperature_difference))
        out.append(self._to_str(self.zone_heating_design_supply_air_temperature_input_method))
        out.append(self._to_str(self.zone_heating_design_supply_air_temperature))
        out.append(self._to_str(self.zone_heating_design_supply_air_temperature_difference))
        out.append(self._to_str(self.zone_cooling_design_supply_air_humidity_ratio))
        out.append(self._to_str(self.zone_heating_design_supply_air_humidity_ratio))
        out.append(self._to_str(self.design_specification_outdoor_air_object_name))
        out.append(self._to_str(self.zone_heating_sizing_factor))
        out.append(self._to_str(self.zone_cooling_sizing_factor))
        out.append(self._to_str(self.cooling_design_air_flow_method))
        out.append(self._to_str(self.cooling_design_air_flow_rate))
        out.append(self._to_str(self.cooling_minimum_air_flow_per_zone_floor_area))
        out.append(self._to_str(self.cooling_minimum_air_flow))
        out.append(self._to_str(self.cooling_minimum_air_flow_fraction))
        out.append(self._to_str(self.heating_design_air_flow_method))
        out.append(self._to_str(self.heating_design_air_flow_rate))
        out.append(self._to_str(self.heating_maximum_air_flow_per_zone_floor_area))
        out.append(self._to_str(self.heating_maximum_air_flow))
        out.append(self._to_str(self.heating_maximum_air_flow_fraction))
        out.append(self._to_str(self.design_specification_zone_air_distribution_object_name))
        return ",".join(out)

class SizingSystem(object):
    """ Corresponds to IDD object `Sizing:System`
        Specifies the input needed to perform sizing calculations for a central forced air
        system design air flow, heating capacity, and cooling capacity.
    """
    internal_name = "Sizing:System"
    field_count = 36

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Sizing:System`
        """
        self._data = OrderedDict()
        self._data["AirLoop Name"] = None
        self._data["Type of Load to Size On"] = None
        self._data["Design Outdoor Air Flow Rate"] = None
        self._data["Minimum System Air Flow Ratio"] = None
        self._data["Preheat Design Temperature"] = None
        self._data["Preheat Design Humidity Ratio"] = None
        self._data["Precool Design Temperature"] = None
        self._data["Precool Design Humidity Ratio"] = None
        self._data["Central Cooling Design Supply Air Temperature"] = None
        self._data["Central Heating Design Supply Air Temperature"] = None
        self._data["Sizing Option"] = None
        self._data["100% Outdoor Air in Cooling"] = None
        self._data["100% Outdoor Air in Heating"] = None
        self._data["Central Cooling Design Supply Air Humidity Ratio"] = None
        self._data["Central Heating Design Supply Air Humidity Ratio"] = None
        self._data["Cooling Design Air Flow Method"] = None
        self._data["Cooling Design Air Flow Rate"] = None
        self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"] = None
        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = None
        self._data["Design Supply Air Flow Rate Per Unit Cooling Capacity"] = None
        self._data["Heating Design Air Flow Method"] = None
        self._data["Heating Design Air Flow Rate"] = None
        self._data["Supply Air Flow Rate Per Floor Area During Heating Operation"] = None
        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"] = None
        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = None
        self._data["Design Supply Air Flow Rate Per Unit Heating Capacity"] = None
        self._data["System Outdoor Air Method"] = None
        self._data["Zone Maximum Outdoor Air Fraction"] = None
        self._data["Cooling Design Capacity Method"] = None
        self._data["Cooling Design Capacity"] = None
        self._data["Cooling Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Cooling Design Capacity"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.airloop_name = None
        else:
            self.airloop_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.type_of_load_to_size_on = None
        else:
            self.type_of_load_to_size_on = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_outdoor_air_flow_rate = None
        else:
            self.design_outdoor_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_system_air_flow_ratio = None
        else:
            self.minimum_system_air_flow_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.preheat_design_temperature = None
        else:
            self.preheat_design_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.preheat_design_humidity_ratio = None
        else:
            self.preheat_design_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.precool_design_temperature = None
        else:
            self.precool_design_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.precool_design_humidity_ratio = None
        else:
            self.precool_design_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_cooling_design_supply_air_temperature = None
        else:
            self.central_cooling_design_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_heating_design_supply_air_temperature = None
        else:
            self.central_heating_design_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_option = None
        else:
            self.sizing_option = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.100_outdoor_air_in_cooling = None
        else:
            self.100_outdoor_air_in_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.100_outdoor_air_in_heating = None
        else:
            self.100_outdoor_air_in_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_cooling_design_supply_air_humidity_ratio = None
        else:
            self.central_cooling_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_heating_design_supply_air_humidity_ratio = None
        else:
            self.central_heating_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_method = None
        else:
            self.cooling_design_air_flow_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_rate = None
        else:
            self.cooling_design_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_per_floor_area_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_cooling_capacity = None
        else:
            self.design_supply_air_flow_rate_per_unit_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_air_flow_method = None
        else:
            self.heating_design_air_flow_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_air_flow_rate = None
        else:
            self.heating_design_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_during_heating_operation = None
        else:
            self.supply_air_flow_rate_per_floor_area_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_heating_capacity = None
        else:
            self.design_supply_air_flow_rate_per_unit_heating_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.system_outdoor_air_method = None
        else:
            self.system_outdoor_air_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_maximum_outdoor_air_fraction = None
        else:
            self.zone_maximum_outdoor_air_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_capacity_method = None
        else:
            self.cooling_design_capacity_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_capacity = None
        else:
            self.cooling_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_capacity_per_floor_area = None
        else:
            self.cooling_design_capacity_per_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_cooling_design_capacity = None
        else:
            self.fraction_of_autosized_cooling_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1

    @property
    def airloop_name(self):
        """Get airloop_name

        Returns:
            str: the value of `airloop_name` or None if not set
        """
        return self._data["AirLoop Name"]

    @airloop_name.setter
    def airloop_name(self, value=None):
        """  Corresponds to IDD Field `airloop_name`

        Args:
            value (str): value for IDD Field `airloop_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airloop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airloop_name`')

        self._data["AirLoop Name"] = value

    @property
    def type_of_load_to_size_on(self):
        """Get type_of_load_to_size_on

        Returns:
            str: the value of `type_of_load_to_size_on` or None if not set
        """
        return self._data["Type of Load to Size On"]

    @type_of_load_to_size_on.setter
    def type_of_load_to_size_on(self, value="Sensible"):
        """  Corresponds to IDD Field `type_of_load_to_size_on`
        Specifies the basis for sizing the system supply air flow rate
        Sensible and VentilationRequirement are the only available options
        Sensible uses the zone design air flow rates
        VentilationRequirement uses the system ventilation requirement

        Args:
            value (str): value for IDD Field `type_of_load_to_size_on`
                Accepted values are:
                      - Sensible
                      - VentilationRequirement
                Default value: Sensible
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `type_of_load_to_size_on`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_load_to_size_on`')
            vals = set()
            vals.add("Sensible")
            vals.add("VentilationRequirement")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `type_of_load_to_size_on`'.format(value))

        self._data["Type of Load to Size On"] = value

    @property
    def design_outdoor_air_flow_rate(self):
        """Get design_outdoor_air_flow_rate

        Returns:
            float: the value of `design_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Design Outdoor Air Flow Rate"]

    @design_outdoor_air_flow_rate.setter
    def design_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `design_outdoor_air_flow_rate`
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
                                 'for field `design_outdoor_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_outdoor_air_flow_rate`')

        self._data["Design Outdoor Air Flow Rate"] = value

    @property
    def minimum_system_air_flow_ratio(self):
        """Get minimum_system_air_flow_ratio

        Returns:
            float: the value of `minimum_system_air_flow_ratio` or None if not set
        """
        return self._data["Minimum System Air Flow Ratio"]

    @minimum_system_air_flow_ratio.setter
    def minimum_system_air_flow_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_system_air_flow_ratio`

        Args:
            value (float): value for IDD Field `minimum_system_air_flow_ratio`
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
                                 'for field `minimum_system_air_flow_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_system_air_flow_ratio`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_system_air_flow_ratio`')

        self._data["Minimum System Air Flow Ratio"] = value

    @property
    def preheat_design_temperature(self):
        """Get preheat_design_temperature

        Returns:
            float: the value of `preheat_design_temperature` or None if not set
        """
        return self._data["Preheat Design Temperature"]

    @preheat_design_temperature.setter
    def preheat_design_temperature(self, value=None):
        """  Corresponds to IDD Field `preheat_design_temperature`

        Args:
            value (float): value for IDD Field `preheat_design_temperature`
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
                                 'for field `preheat_design_temperature`'.format(value))

        self._data["Preheat Design Temperature"] = value

    @property
    def preheat_design_humidity_ratio(self):
        """Get preheat_design_humidity_ratio

        Returns:
            float: the value of `preheat_design_humidity_ratio` or None if not set
        """
        return self._data["Preheat Design Humidity Ratio"]

    @preheat_design_humidity_ratio.setter
    def preheat_design_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `preheat_design_humidity_ratio`

        Args:
            value (float): value for IDD Field `preheat_design_humidity_ratio`
                Unit: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `preheat_design_humidity_ratio`'.format(value))

        self._data["Preheat Design Humidity Ratio"] = value

    @property
    def precool_design_temperature(self):
        """Get precool_design_temperature

        Returns:
            float: the value of `precool_design_temperature` or None if not set
        """
        return self._data["Precool Design Temperature"]

    @precool_design_temperature.setter
    def precool_design_temperature(self, value=None):
        """  Corresponds to IDD Field `precool_design_temperature`

        Args:
            value (float): value for IDD Field `precool_design_temperature`
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
                                 'for field `precool_design_temperature`'.format(value))

        self._data["Precool Design Temperature"] = value

    @property
    def precool_design_humidity_ratio(self):
        """Get precool_design_humidity_ratio

        Returns:
            float: the value of `precool_design_humidity_ratio` or None if not set
        """
        return self._data["Precool Design Humidity Ratio"]

    @precool_design_humidity_ratio.setter
    def precool_design_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `precool_design_humidity_ratio`

        Args:
            value (float): value for IDD Field `precool_design_humidity_ratio`
                Unit: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `precool_design_humidity_ratio`'.format(value))

        self._data["Precool Design Humidity Ratio"] = value

    @property
    def central_cooling_design_supply_air_temperature(self):
        """Get central_cooling_design_supply_air_temperature

        Returns:
            float: the value of `central_cooling_design_supply_air_temperature` or None if not set
        """
        return self._data["Central Cooling Design Supply Air Temperature"]

    @central_cooling_design_supply_air_temperature.setter
    def central_cooling_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `central_cooling_design_supply_air_temperature`

        Args:
            value (float): value for IDD Field `central_cooling_design_supply_air_temperature`
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
                                 'for field `central_cooling_design_supply_air_temperature`'.format(value))

        self._data["Central Cooling Design Supply Air Temperature"] = value

    @property
    def central_heating_design_supply_air_temperature(self):
        """Get central_heating_design_supply_air_temperature

        Returns:
            float: the value of `central_heating_design_supply_air_temperature` or None if not set
        """
        return self._data["Central Heating Design Supply Air Temperature"]

    @central_heating_design_supply_air_temperature.setter
    def central_heating_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `central_heating_design_supply_air_temperature`

        Args:
            value (float): value for IDD Field `central_heating_design_supply_air_temperature`
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
                                 'for field `central_heating_design_supply_air_temperature`'.format(value))

        self._data["Central Heating Design Supply Air Temperature"] = value

    @property
    def sizing_option(self):
        """Get sizing_option

        Returns:
            str: the value of `sizing_option` or None if not set
        """
        return self._data["Sizing Option"]

    @sizing_option.setter
    def sizing_option(self, value="NonCoincident"):
        """  Corresponds to IDD Field `sizing_option`

        Args:
            value (str): value for IDD Field `sizing_option`
                Accepted values are:
                      - Coincident
                      - NonCoincident
                Default value: NonCoincident
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sizing_option`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sizing_option`')
            vals = set()
            vals.add("Coincident")
            vals.add("NonCoincident")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `sizing_option`'.format(value))

        self._data["Sizing Option"] = value

    @property
    def 100_outdoor_air_in_cooling(self):
        """Get 100_outdoor_air_in_cooling

        Returns:
            str: the value of `100_outdoor_air_in_cooling` or None if not set
        """
        return self._data["100% Outdoor Air in Cooling"]

    @100_outdoor_air_in_cooling.setter
    def 100_outdoor_air_in_cooling(self, value="No"):
        """  Corresponds to IDD Field `100_outdoor_air_in_cooling`

        Args:
            value (str): value for IDD Field `100_outdoor_air_in_cooling`
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
                                 'for field `100_outdoor_air_in_cooling`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `100_outdoor_air_in_cooling`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `100_outdoor_air_in_cooling`'.format(value))

        self._data["100% Outdoor Air in Cooling"] = value

    @property
    def 100_outdoor_air_in_heating(self):
        """Get 100_outdoor_air_in_heating

        Returns:
            str: the value of `100_outdoor_air_in_heating` or None if not set
        """
        return self._data["100% Outdoor Air in Heating"]

    @100_outdoor_air_in_heating.setter
    def 100_outdoor_air_in_heating(self, value="No"):
        """  Corresponds to IDD Field `100_outdoor_air_in_heating`

        Args:
            value (str): value for IDD Field `100_outdoor_air_in_heating`
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
                                 'for field `100_outdoor_air_in_heating`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `100_outdoor_air_in_heating`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `100_outdoor_air_in_heating`'.format(value))

        self._data["100% Outdoor Air in Heating"] = value

    @property
    def central_cooling_design_supply_air_humidity_ratio(self):
        """Get central_cooling_design_supply_air_humidity_ratio

        Returns:
            float: the value of `central_cooling_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Central Cooling Design Supply Air Humidity Ratio"]

    @central_cooling_design_supply_air_humidity_ratio.setter
    def central_cooling_design_supply_air_humidity_ratio(self, value=0.008 ):
        """  Corresponds to IDD Field `central_cooling_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `central_cooling_design_supply_air_humidity_ratio`
                Unit: kgWater/kgDryAir
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
                                 'for field `central_cooling_design_supply_air_humidity_ratio`'.format(value))

        self._data["Central Cooling Design Supply Air Humidity Ratio"] = value

    @property
    def central_heating_design_supply_air_humidity_ratio(self):
        """Get central_heating_design_supply_air_humidity_ratio

        Returns:
            float: the value of `central_heating_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Central Heating Design Supply Air Humidity Ratio"]

    @central_heating_design_supply_air_humidity_ratio.setter
    def central_heating_design_supply_air_humidity_ratio(self, value=0.008 ):
        """  Corresponds to IDD Field `central_heating_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `central_heating_design_supply_air_humidity_ratio`
                Unit: kgWater/kgDryAir
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
                                 'for field `central_heating_design_supply_air_humidity_ratio`'.format(value))

        self._data["Central Heating Design Supply Air Humidity Ratio"] = value

    @property
    def cooling_design_air_flow_method(self):
        """Get cooling_design_air_flow_method

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set
        """
        return self._data["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `cooling_design_air_flow_method`

        Args:
            value (str): value for IDD Field `cooling_design_air_flow_method`
                Accepted values are:
                      - Flow/System
                      - DesignDay
                      - FlowPerFloorArea
                      - FractionOfAutosizedCoolingAirflow
                      - FlowPerCoolingCapacity
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_air_flow_method`')
            vals = set()
            vals.add("Flow/System")
            vals.add("DesignDay")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedCoolingAirflow")
            vals.add("FlowPerCoolingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_design_air_flow_method`'.format(value))

        self._data["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_air_flow_rate(self):
        """Get cooling_design_air_flow_rate

        Returns:
            float: the value of `cooling_design_air_flow_rate` or None if not set
        """
        return self._data["Cooling Design Air Flow Rate"]

    @cooling_design_air_flow_rate.setter
    def cooling_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_design_air_flow_rate`
        This input is used if Cooling Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `cooling_design_air_flow_rate`
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
                                 'for field `cooling_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_air_flow_rate`')

        self._data["Cooling Design Air Flow Rate"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self):
        """Get supply_air_flow_rate_per_floor_area_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"]

    @supply_air_flow_rate_per_floor_area_during_cooling_operation.setter
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_during_cooling_operation`
        Enter the cooling supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method during cooling operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_during_cooling_operation`
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
                                 'for field `supply_air_flow_rate_per_floor_area_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_during_cooling_operation`')

        self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self):
        """Get fraction_of_autosized_design_cooling_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method during cooling operation is
        FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`')

        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_cooling_capacity(self):
        """Get design_supply_air_flow_rate_per_unit_cooling_capacity

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_cooling_capacity` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit Cooling Capacity"]

    @design_supply_air_flow_rate_per_unit_cooling_capacity.setter
    def design_supply_air_flow_rate_per_unit_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_cooling_capacity`
        Enter the supply air volume flow rate per unit cooling capacity.
        Required field when Supply air Flow Rate Method During Cooling Operation is
        FlowPerCoolingCapacity.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_cooling_capacity`
                Unit: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_cooling_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_cooling_capacity`')

        self._data["Design Supply Air Flow Rate Per Unit Cooling Capacity"] = value

    @property
    def heating_design_air_flow_method(self):
        """Get heating_design_air_flow_method

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set
        """
        return self._data["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `heating_design_air_flow_method`

        Args:
            value (str): value for IDD Field `heating_design_air_flow_method`
                Accepted values are:
                      - Flow/System
                      - DesignDay
                      - FlowPerFloorArea
                      - FractionOfAutosizedHeatingAirflow
                      - FractionOfAutosizedCoolingAirflow
                      - FlowPerCoolingCapacity
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_air_flow_method`')
            vals = set()
            vals.add("Flow/System")
            vals.add("DesignDay")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedHeatingAirflow")
            vals.add("FractionOfAutosizedCoolingAirflow")
            vals.add("FlowPerCoolingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_design_air_flow_method`'.format(value))

        self._data["Heating Design Air Flow Method"] = value

    @property
    def heating_design_air_flow_rate(self):
        """Get heating_design_air_flow_rate

        Returns:
            float: the value of `heating_design_air_flow_rate` or None if not set
        """
        return self._data["Heating Design Air Flow Rate"]

    @heating_design_air_flow_rate.setter
    def heating_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `heating_design_air_flow_rate`
        This input is used if Heating Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `heating_design_air_flow_rate`
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
                                 'for field `heating_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_air_flow_rate`')

        self._data["Heating Design Air Flow Rate"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self):
        """Get supply_air_flow_rate_per_floor_area_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area During Heating Operation"]

    @supply_air_flow_rate_per_floor_area_during_heating_operation.setter
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_during_heating_operation`
        Enter the heating supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method during heating operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_during_heating_operation`
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
                                 'for field `supply_air_flow_rate_per_floor_area_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_during_heating_operation`')

        self._data["Supply Air Flow Rate Per Floor Area During Heating Operation"] = value

    @property
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self):
        """Get fraction_of_autosized_design_heating_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_design_heating_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"]

    @fraction_of_autosized_design_heating_supply_air_flow_rate.setter
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method during heating operation is
        FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate`')

        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self):
        """Get fraction_of_autosized_design_cooling_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method during heating operation is
        FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`')

        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_heating_capacity(self):
        """Get design_supply_air_flow_rate_per_unit_heating_capacity

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_heating_capacity` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit Heating Capacity"]

    @design_supply_air_flow_rate_per_unit_heating_capacity.setter
    def design_supply_air_flow_rate_per_unit_heating_capacity(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_heating_capacity`
        Enter the heating supply air volume flow rate per unit heating capacity.
        Required field when Supply air Flow Rate Method during heating operation is
        FlowPerHeatingCapacity.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_heating_capacity`
                Unit: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_heating_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_heating_capacity`')

        self._data["Design Supply Air Flow Rate Per Unit Heating Capacity"] = value

    @property
    def system_outdoor_air_method(self):
        """Get system_outdoor_air_method

        Returns:
            str: the value of `system_outdoor_air_method` or None if not set
        """
        return self._data["System Outdoor Air Method"]

    @system_outdoor_air_method.setter
    def system_outdoor_air_method(self, value="ZoneSum"):
        """  Corresponds to IDD Field `system_outdoor_air_method`

        Args:
            value (str): value for IDD Field `system_outdoor_air_method`
                Accepted values are:
                      - ZoneSum
                      - VentilationRateProcedure
                Default value: ZoneSum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `system_outdoor_air_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `system_outdoor_air_method`')
            vals = set()
            vals.add("ZoneSum")
            vals.add("VentilationRateProcedure")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `system_outdoor_air_method`'.format(value))

        self._data["System Outdoor Air Method"] = value

    @property
    def zone_maximum_outdoor_air_fraction(self):
        """Get zone_maximum_outdoor_air_fraction

        Returns:
            float: the value of `zone_maximum_outdoor_air_fraction` or None if not set
        """
        return self._data["Zone Maximum Outdoor Air Fraction"]

    @zone_maximum_outdoor_air_fraction.setter
    def zone_maximum_outdoor_air_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `zone_maximum_outdoor_air_fraction`

        Args:
            value (float): value for IDD Field `zone_maximum_outdoor_air_fraction`
                Unit: dimensionless
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
                                 'for field `zone_maximum_outdoor_air_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `zone_maximum_outdoor_air_fraction`')

        self._data["Zone Maximum Outdoor Air Fraction"] = value

    @property
    def cooling_design_capacity_method(self):
        """Get cooling_design_capacity_method

        Returns:
            str: the value of `cooling_design_capacity_method` or None if not set
        """
        return self._data["Cooling Design Capacity Method"]

    @cooling_design_capacity_method.setter
    def cooling_design_capacity_method(self, value="CoolingDesignCapacity"):
        """  Corresponds to IDD Field `cooling_design_capacity_method`
        Enter the method used to determine the system cooling design capacity for scalable sizing.
        None is used when a cooling coils is not included in an airloop or this field may be blank.
        If this input field is left blank, then the design cooling capacity is set to zero.
        CoolingDesignCapacity => selected when the design cooling capacity value is specified or
        auto-sized. CapacityPerFloorArea => selected when the design cooling capacity is determined
        from user specified cooling capacity per floor area and total floor area of cooled zones
        served by an airloop. FractionOfAutosizedCoolingCapacity => is selected when the design
        cooling capacity is determined from a user specified fraction and the auto-sized design
        cooling capacity of the system.

        Args:
            value (str): value for IDD Field `cooling_design_capacity_method`
                Accepted values are:
                      - None
                      - CoolingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedCoolingCapacity
                Default value: CoolingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_capacity_method`')
            vals = set()
            vals.add("None")
            vals.add("CoolingDesignCapacity")
            vals.add("CapacityPerFloorArea")
            vals.add("FractionOfAutosizedCoolingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_design_capacity_method`'.format(value))

        self._data["Cooling Design Capacity Method"] = value

    @property
    def cooling_design_capacity(self):
        """Get cooling_design_capacity

        Returns:
            float: the value of `cooling_design_capacity` or None if not set
        """
        return self._data["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `cooling_design_capacity`
        Enter the design cooling capacity. Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float): value for IDD Field `cooling_design_capacity`
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
                                 'for field `cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_capacity`')

        self._data["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """Get cooling_design_capacity_per_floor_area

        Returns:
            float: the value of `cooling_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Cooling Design Capacity Per Floor Area"]

    @cooling_design_capacity_per_floor_area.setter
    def cooling_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `cooling_design_capacity_per_floor_area`
        Enter the cooling design capacity per total floor area of cooled zones served by an airloop.
        Required field when the cooling design capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `cooling_design_capacity_per_floor_area`
                Unit: W/m2
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
                                 'for field `cooling_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_capacity_per_floor_area`')

        self._data["Cooling Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_capacity(self):
        """Get fraction_of_autosized_cooling_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Cooling Design Capacity"]

    @fraction_of_autosized_cooling_design_capacity.setter
    def fraction_of_autosized_cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_cooling_design_capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_cooling_design_capacity`
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
                                 'for field `fraction_of_autosized_cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_cooling_design_capacity`')

        self._data["Fraction of Autosized Cooling Design Capacity"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `heating_design_capacity_method`
        Enter the method used to determine the heating design capacity for scalable sizing.
        None is used when a heating coil not included in an airloop or this field may be blank.
        If this input field is left blank, then the design heating capacity is set to zero.
        HeatingDesignCapacity => selected when the design heating capacity value is specified or
        auto-sized. CapacityPerFloorArea => selected when the design heating capacity is determined
        from user specified heating capacity per flow area and total floor area of heated zones
        served by an airloop. FractionOfAutosizedHeatingCapacity => is selected when the design
        heating capacity is determined from a user specified fraction and the auto-sized design
        heating capacity of the system.

        Args:
            value (str): value for IDD Field `heating_design_capacity_method`
                Accepted values are:
                      - None
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_capacity_method`')
            vals = set()
            vals.add("None")
            vals.add("HeatingDesignCapacity")
            vals.add("CapacityPerFloorArea")
            vals.add("FractionOfAutosizedHeatingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_design_capacity_method`'.format(value))

        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value=None):
        """  Corresponds to IDD Field `heating_design_capacity`
        Enter the design heating capacity. Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float): value for IDD Field `heating_design_capacity`
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
                                 'for field `heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_capacity`')

        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `heating_design_capacity_per_floor_area`
        Enter the heating design capacity per zone floor area. Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `heating_design_capacity_per_floor_area`
                Unit: W/m2
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
                                 'for field `heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_capacity_per_floor_area`')

        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_heating_design_capacity`
        Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_heating_design_capacity`
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
                                 'for field `fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_heating_design_capacity`')

        self._data["Fraction of Autosized Heating Design Capacity"] = value

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
        out.append(self._to_str(self.airloop_name))
        out.append(self._to_str(self.type_of_load_to_size_on))
        out.append(self._to_str(self.design_outdoor_air_flow_rate))
        out.append(self._to_str(self.minimum_system_air_flow_ratio))
        out.append(self._to_str(self.preheat_design_temperature))
        out.append(self._to_str(self.preheat_design_humidity_ratio))
        out.append(self._to_str(self.precool_design_temperature))
        out.append(self._to_str(self.precool_design_humidity_ratio))
        out.append(self._to_str(self.central_cooling_design_supply_air_temperature))
        out.append(self._to_str(self.central_heating_design_supply_air_temperature))
        out.append(self._to_str(self.sizing_option))
        out.append(self._to_str(self.100_outdoor_air_in_cooling))
        out.append(self._to_str(self.100_outdoor_air_in_heating))
        out.append(self._to_str(self.central_cooling_design_supply_air_humidity_ratio))
        out.append(self._to_str(self.central_heating_design_supply_air_humidity_ratio))
        out.append(self._to_str(self.cooling_design_air_flow_method))
        out.append(self._to_str(self.cooling_design_air_flow_rate))
        out.append(self._to_str(self.supply_air_flow_rate_per_floor_area_during_cooling_operation))
        out.append(self._to_str(self.fraction_of_autosized_design_cooling_supply_air_flow_rate))
        out.append(self._to_str(self.design_supply_air_flow_rate_per_unit_cooling_capacity))
        out.append(self._to_str(self.heating_design_air_flow_method))
        out.append(self._to_str(self.heating_design_air_flow_rate))
        out.append(self._to_str(self.supply_air_flow_rate_per_floor_area_during_heating_operation))
        out.append(self._to_str(self.fraction_of_autosized_design_heating_supply_air_flow_rate))
        out.append(self._to_str(self.fraction_of_autosized_design_cooling_supply_air_flow_rate))
        out.append(self._to_str(self.design_supply_air_flow_rate_per_unit_heating_capacity))
        out.append(self._to_str(self.system_outdoor_air_method))
        out.append(self._to_str(self.zone_maximum_outdoor_air_fraction))
        out.append(self._to_str(self.cooling_design_capacity_method))
        out.append(self._to_str(self.cooling_design_capacity))
        out.append(self._to_str(self.cooling_design_capacity_per_floor_area))
        out.append(self._to_str(self.fraction_of_autosized_cooling_design_capacity))
        out.append(self._to_str(self.heating_design_capacity_method))
        out.append(self._to_str(self.heating_design_capacity))
        out.append(self._to_str(self.heating_design_capacity_per_floor_area))
        out.append(self._to_str(self.fraction_of_autosized_heating_design_capacity))
        return ",".join(out)

class SizingPlant(object):
    """ Corresponds to IDD object `Sizing:Plant`
        Specifies the input needed to autosize plant loop flow rates and equipment capacities.
        This information is initially used by components that use water for heating or cooling
        such as hot or chilled water coils to calculate their maximum water flow rates. These
        flow rates are then summed for use in calculating the Plant Loop flow rates.
    """
    internal_name = "Sizing:Plant"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Sizing:Plant`
        """
        self._data = OrderedDict()
        self._data["Plant or Condenser Loop Name"] = None
        self._data["Loop Type"] = None
        self._data["Design Loop Exit Temperature"] = None
        self._data["Loop Design Temperature Difference"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.plant_or_condenser_loop_name = None
        else:
            self.plant_or_condenser_loop_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loop_type = None
        else:
            self.loop_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_loop_exit_temperature = None
        else:
            self.design_loop_exit_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loop_design_temperature_difference = None
        else:
            self.loop_design_temperature_difference = vals[i]
        i += 1

    @property
    def plant_or_condenser_loop_name(self):
        """Get plant_or_condenser_loop_name

        Returns:
            str: the value of `plant_or_condenser_loop_name` or None if not set
        """
        return self._data["Plant or Condenser Loop Name"]

    @plant_or_condenser_loop_name.setter
    def plant_or_condenser_loop_name(self, value=None):
        """  Corresponds to IDD Field `plant_or_condenser_loop_name`
        Enter the name of a PlantLoop or a CondenserLoop object

        Args:
            value (str): value for IDD Field `plant_or_condenser_loop_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_or_condenser_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_or_condenser_loop_name`')

        self._data["Plant or Condenser Loop Name"] = value

    @property
    def loop_type(self):
        """Get loop_type

        Returns:
            str: the value of `loop_type` or None if not set
        """
        return self._data["Loop Type"]

    @loop_type.setter
    def loop_type(self, value=None):
        """  Corresponds to IDD Field `loop_type`

        Args:
            value (str): value for IDD Field `loop_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Condenser
                      - Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Condenser")
            vals.add("Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `loop_type`'.format(value))

        self._data["Loop Type"] = value

    @property
    def design_loop_exit_temperature(self):
        """Get design_loop_exit_temperature

        Returns:
            float: the value of `design_loop_exit_temperature` or None if not set
        """
        return self._data["Design Loop Exit Temperature"]

    @design_loop_exit_temperature.setter
    def design_loop_exit_temperature(self, value=None):
        """  Corresponds to IDD Field `design_loop_exit_temperature`

        Args:
            value (float): value for IDD Field `design_loop_exit_temperature`
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
                                 'for field `design_loop_exit_temperature`'.format(value))

        self._data["Design Loop Exit Temperature"] = value

    @property
    def loop_design_temperature_difference(self):
        """Get loop_design_temperature_difference

        Returns:
            float: the value of `loop_design_temperature_difference` or None if not set
        """
        return self._data["Loop Design Temperature Difference"]

    @loop_design_temperature_difference.setter
    def loop_design_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `loop_design_temperature_difference`

        Args:
            value (float): value for IDD Field `loop_design_temperature_difference`
                Unit: deltaC
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
                                 'for field `loop_design_temperature_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loop_design_temperature_difference`')

        self._data["Loop Design Temperature Difference"] = value

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
        out.append(self._to_str(self.plant_or_condenser_loop_name))
        out.append(self._to_str(self.loop_type))
        out.append(self._to_str(self.design_loop_exit_temperature))
        out.append(self._to_str(self.loop_design_temperature_difference))
        return ",".join(out)