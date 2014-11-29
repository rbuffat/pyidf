from collections import OrderedDict

class ZoneVentilationDesignFlowRate(object):
    """ Corresponds to IDD object `ZoneVentilation:DesignFlowRate`
        Ventilation is specified as a design level which is modified by a schedule fraction, temperature difference and wind speed:
        Ventilation=Vdesign * Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "ZoneVentilation:DesignFlowRate"
    field_count = 26

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneVentilation:DesignFlowRate`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Flow Rate Calculation Method"] = None
        self._data["Design Flow Rate"] = None
        self._data["Flow Rate per Zone Floor Area"] = None
        self._data["Flow Rate per Person"] = None
        self._data["Air Changes per Hour"] = None
        self._data["Ventilation Type"] = None
        self._data["Fan Pressure Rise"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Constant Term Coefficient"] = None
        self._data["Temperature Term Coefficient"] = None
        self._data["Velocity Term Coefficient"] = None
        self._data["Velocity Squared Term Coefficient"] = None
        self._data["Minimum Indoor Temperature"] = None
        self._data["Minimum Indoor Temperature Schedule Name"] = None
        self._data["Maximum Indoor Temperature"] = None
        self._data["Maximum Indoor Temperature Schedule Name"] = None
        self._data["Delta Temperature"] = None
        self._data["Delta Temperature Schedule Name"] = None
        self._data["Minimum Outdoor Temperature"] = None
        self._data["Minimum Outdoor Temperature Schedule Name"] = None
        self._data["Maximum Outdoor Temperature"] = None
        self._data["Maximum Outdoor Temperature Schedule Name"] = None
        self._data["Maximum Wind Speed"] = None

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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_flow_rate_calculation_method = None
        else:
            self.design_flow_rate_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_rate_per_zone_floor_area = None
        else:
            self.flow_rate_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_rate_per_person = None
        else:
            self.flow_rate_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_changes_per_hour = None
        else:
            self.air_changes_per_hour = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_type = None
        else:
            self.ventilation_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_pressure_rise = None
        else:
            self.fan_pressure_rise = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_total_efficiency = None
        else:
            self.fan_total_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_term_coefficient = None
        else:
            self.constant_term_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_term_coefficient = None
        else:
            self.temperature_term_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.velocity_term_coefficient = None
        else:
            self.velocity_term_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.velocity_squared_term_coefficient = None
        else:
            self.velocity_squared_term_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_indoor_temperature = None
        else:
            self.minimum_indoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_indoor_temperature_schedule_name = None
        else:
            self.minimum_indoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_indoor_temperature = None
        else:
            self.maximum_indoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_indoor_temperature_schedule_name = None
        else:
            self.maximum_indoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_temperature = None
        else:
            self.delta_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_temperature_schedule_name = None
        else:
            self.delta_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature = None
        else:
            self.minimum_outdoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_schedule_name = None
        else:
            self.minimum_outdoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature = None
        else:
            self.maximum_outdoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_schedule_name = None
        else:
            self.maximum_outdoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_wind_speed = None
        else:
            self.maximum_wind_speed = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`

        Args:
            value (str): value for IDD Field `schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_flow_rate_calculation_method(self):
        """Get design_flow_rate_calculation_method

        Returns:
            str: the value of `design_flow_rate_calculation_method` or None if not set
        """
        return self._data["Design Flow Rate Calculation Method"]

    @design_flow_rate_calculation_method.setter
    def design_flow_rate_calculation_method(self, value="Flow/Zone"):
        """  Corresponds to IDD Field `design_flow_rate_calculation_method`
        The entered calculation method is used to create the maximum amount of ventilation
        for this set of attributes
        Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate
        Flow/Area => Flow Rate per Zone Floor Area - Value * Floor Area (zone) = Design Flow Rate
        Flow/Person => Flow Rate per Person - Value * #people = Design Flow Rate
        AirChanges/Hour => Air Changes per Hour - Value * Floor Volume (zone) adjusted for m3/s = Design Volume Flow Rate
        "Vdesign" in Equation is the result.

        Args:
            value (str): value for IDD Field `design_flow_rate_calculation_method`
                Accepted values are:
                      - Flow/Zone
                      - Flow/Area
                      - Flow/Person
                      - AirChanges/Hour
                Default value: Flow/Zone
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_flow_rate_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_flow_rate_calculation_method`')
            vals = set()
            vals.add("Flow/Zone")
            vals.add("Flow/Area")
            vals.add("Flow/Person")
            vals.add("AirChanges/Hour")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_flow_rate_calculation_method`'.format(value))

        self._data["Design Flow Rate Calculation Method"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_flow_rate`

        Args:
            value (float): value for IDD Field `design_flow_rate`
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
                                 'for field `design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_flow_rate`')

        self._data["Design Flow Rate"] = value

    @property
    def flow_rate_per_zone_floor_area(self):
        """Get flow_rate_per_zone_floor_area

        Returns:
            float: the value of `flow_rate_per_zone_floor_area` or None if not set
        """
        return self._data["Flow Rate per Zone Floor Area"]

    @flow_rate_per_zone_floor_area.setter
    def flow_rate_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `flow_rate_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `flow_rate_per_zone_floor_area`
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
                                 'for field `flow_rate_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `flow_rate_per_zone_floor_area`')

        self._data["Flow Rate per Zone Floor Area"] = value

    @property
    def flow_rate_per_person(self):
        """Get flow_rate_per_person

        Returns:
            float: the value of `flow_rate_per_person` or None if not set
        """
        return self._data["Flow Rate per Person"]

    @flow_rate_per_person.setter
    def flow_rate_per_person(self, value=None):
        """  Corresponds to IDD Field `flow_rate_per_person`

        Args:
            value (float): value for IDD Field `flow_rate_per_person`
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
                                 'for field `flow_rate_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `flow_rate_per_person`')

        self._data["Flow Rate per Person"] = value

    @property
    def air_changes_per_hour(self):
        """Get air_changes_per_hour

        Returns:
            float: the value of `air_changes_per_hour` or None if not set
        """
        return self._data["Air Changes per Hour"]

    @air_changes_per_hour.setter
    def air_changes_per_hour(self, value=None):
        """  Corresponds to IDD Field `air_changes_per_hour`

        Args:
            value (float): value for IDD Field `air_changes_per_hour`
                Unit: 1/hr
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
                                 'for field `air_changes_per_hour`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `air_changes_per_hour`')

        self._data["Air Changes per Hour"] = value

    @property
    def ventilation_type(self):
        """Get ventilation_type

        Returns:
            str: the value of `ventilation_type` or None if not set
        """
        return self._data["Ventilation Type"]

    @ventilation_type.setter
    def ventilation_type(self, value="Natural"):
        """  Corresponds to IDD Field `ventilation_type`

        Args:
            value (str): value for IDD Field `ventilation_type`
                Accepted values are:
                      - Natural
                      - Intake
                      - Exhaust
                      - Balanced
                Default value: Natural
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ventilation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_type`')
            vals = set()
            vals.add("Natural")
            vals.add("Intake")
            vals.add("Exhaust")
            vals.add("Balanced")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ventilation_type`'.format(value))

        self._data["Ventilation Type"] = value

    @property
    def fan_pressure_rise(self):
        """Get fan_pressure_rise

        Returns:
            float: the value of `fan_pressure_rise` or None if not set
        """
        return self._data["Fan Pressure Rise"]

    @fan_pressure_rise.setter
    def fan_pressure_rise(self, value=0.0 ):
        """  Corresponds to IDD Field `fan_pressure_rise`
        pressure rise across the fan

        Args:
            value (float): value for IDD Field `fan_pressure_rise`
                Unit: Pa
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
                                 'for field `fan_pressure_rise`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fan_pressure_rise`')

        self._data["Fan Pressure Rise"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency

        Returns:
            float: the value of `fan_total_efficiency` or None if not set
        """
        return self._data["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=1.0 ):
        """  Corresponds to IDD Field `fan_total_efficiency`

        Args:
            value (float): value for IDD Field `fan_total_efficiency`
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
                                 'for field `fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fan_total_efficiency`')

        self._data["Fan Total Efficiency"] = value

    @property
    def constant_term_coefficient(self):
        """Get constant_term_coefficient

        Returns:
            float: the value of `constant_term_coefficient` or None if not set
        """
        return self._data["Constant Term Coefficient"]

    @constant_term_coefficient.setter
    def constant_term_coefficient(self, value=1.0 ):
        """  Corresponds to IDD Field `constant_term_coefficient`
        "A" in Equation

        Args:
            value (float): value for IDD Field `constant_term_coefficient`
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
                                 'for field `constant_term_coefficient`'.format(value))

        self._data["Constant Term Coefficient"] = value

    @property
    def temperature_term_coefficient(self):
        """Get temperature_term_coefficient

        Returns:
            float: the value of `temperature_term_coefficient` or None if not set
        """
        return self._data["Temperature Term Coefficient"]

    @temperature_term_coefficient.setter
    def temperature_term_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_term_coefficient`
        "B" in Equation

        Args:
            value (float): value for IDD Field `temperature_term_coefficient`
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
                                 'for field `temperature_term_coefficient`'.format(value))

        self._data["Temperature Term Coefficient"] = value

    @property
    def velocity_term_coefficient(self):
        """Get velocity_term_coefficient

        Returns:
            float: the value of `velocity_term_coefficient` or None if not set
        """
        return self._data["Velocity Term Coefficient"]

    @velocity_term_coefficient.setter
    def velocity_term_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `velocity_term_coefficient`
        "C" in Equation

        Args:
            value (float): value for IDD Field `velocity_term_coefficient`
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
                                 'for field `velocity_term_coefficient`'.format(value))

        self._data["Velocity Term Coefficient"] = value

    @property
    def velocity_squared_term_coefficient(self):
        """Get velocity_squared_term_coefficient

        Returns:
            float: the value of `velocity_squared_term_coefficient` or None if not set
        """
        return self._data["Velocity Squared Term Coefficient"]

    @velocity_squared_term_coefficient.setter
    def velocity_squared_term_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `velocity_squared_term_coefficient`
        "D" in Equation

        Args:
            value (float): value for IDD Field `velocity_squared_term_coefficient`
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
                                 'for field `velocity_squared_term_coefficient`'.format(value))

        self._data["Velocity Squared Term Coefficient"] = value

    @property
    def minimum_indoor_temperature(self):
        """Get minimum_indoor_temperature

        Returns:
            float: the value of `minimum_indoor_temperature` or None if not set
        """
        return self._data["Minimum Indoor Temperature"]

    @minimum_indoor_temperature.setter
    def minimum_indoor_temperature(self, value=-100.0 ):
        """  Corresponds to IDD Field `minimum_indoor_temperature`
        this is the indoor temperature below which ventilation is shutoff

        Args:
            value (float): value for IDD Field `minimum_indoor_temperature`
                Unit: C
                Default value: -100.0
                value >= -100.0
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
                                 'for field `minimum_indoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_indoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_indoor_temperature`')

        self._data["Minimum Indoor Temperature"] = value

    @property
    def minimum_indoor_temperature_schedule_name(self):
        """Get minimum_indoor_temperature_schedule_name

        Returns:
            str: the value of `minimum_indoor_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Indoor Temperature Schedule Name"]

    @minimum_indoor_temperature_schedule_name.setter
    def minimum_indoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_indoor_temperature_schedule_name`
        This schedule contains the indoor temperature versus time below which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `minimum_indoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_indoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_indoor_temperature_schedule_name`')

        self._data["Minimum Indoor Temperature Schedule Name"] = value

    @property
    def maximum_indoor_temperature(self):
        """Get maximum_indoor_temperature

        Returns:
            float: the value of `maximum_indoor_temperature` or None if not set
        """
        return self._data["Maximum Indoor Temperature"]

    @maximum_indoor_temperature.setter
    def maximum_indoor_temperature(self, value=100.0 ):
        """  Corresponds to IDD Field `maximum_indoor_temperature`
        this is the indoor temperature above which ventilation is shutoff

        Args:
            value (float): value for IDD Field `maximum_indoor_temperature`
                Unit: C
                Default value: 100.0
                value >= -100.0
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
                                 'for field `maximum_indoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `maximum_indoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_indoor_temperature`')

        self._data["Maximum Indoor Temperature"] = value

    @property
    def maximum_indoor_temperature_schedule_name(self):
        """Get maximum_indoor_temperature_schedule_name

        Returns:
            str: the value of `maximum_indoor_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Indoor Temperature Schedule Name"]

    @maximum_indoor_temperature_schedule_name.setter
    def maximum_indoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_indoor_temperature_schedule_name`
        This schedule contains the indoor temperature versus time above which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `maximum_indoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_indoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_indoor_temperature_schedule_name`')

        self._data["Maximum Indoor Temperature Schedule Name"] = value

    @property
    def delta_temperature(self):
        """Get delta_temperature

        Returns:
            float: the value of `delta_temperature` or None if not set
        """
        return self._data["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=-100.0 ):
        """  Corresponds to IDD Field `delta_temperature`
        This is the temperature differential between indoor and outdoor below which ventilation is shutoff.
        If ((IndoorTemp - OutdoorTemp) < DeltaTemperature) then ventilation is not allowed.
        For example, if delta temperature is 2C, ventilation is assumed to be available if the outside air temperature
        is at least 2C cooler than the zone air temperature. The values for this field can include negative numbers.
        This allows ventilation to occur even if the outdoor temperature is above the indoor temperature.

        Args:
            value (float): value for IDD Field `delta_temperature`
                Unit: deltaC
                Default value: -100.0
                value >= -100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `delta_temperature`')

        self._data["Delta Temperature"] = value

    @property
    def delta_temperature_schedule_name(self):
        """Get delta_temperature_schedule_name

        Returns:
            str: the value of `delta_temperature_schedule_name` or None if not set
        """
        return self._data["Delta Temperature Schedule Name"]

    @delta_temperature_schedule_name.setter
    def delta_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `delta_temperature_schedule_name`
        This schedule contains the temperature differential between indoor and outdoor
        versus time below which ventilation is shutoff.

        Args:
            value (str): value for IDD Field `delta_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `delta_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `delta_temperature_schedule_name`')

        self._data["Delta Temperature Schedule Name"] = value

    @property
    def minimum_outdoor_temperature(self):
        """Get minimum_outdoor_temperature

        Returns:
            float: the value of `minimum_outdoor_temperature` or None if not set
        """
        return self._data["Minimum Outdoor Temperature"]

    @minimum_outdoor_temperature.setter
    def minimum_outdoor_temperature(self, value=-100.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_temperature`
        this is the outdoor temperature below which ventilation is shutoff

        Args:
            value (float): value for IDD Field `minimum_outdoor_temperature`
                Unit: C
                Default value: -100.0
                value >= -100.0
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
                                 'for field `minimum_outdoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_outdoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_outdoor_temperature`')

        self._data["Minimum Outdoor Temperature"] = value

    @property
    def minimum_outdoor_temperature_schedule_name(self):
        """Get minimum_outdoor_temperature_schedule_name

        Returns:
            str: the value of `minimum_outdoor_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Outdoor Temperature Schedule Name"]

    @minimum_outdoor_temperature_schedule_name.setter
    def minimum_outdoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_outdoor_temperature_schedule_name`
        This schedule contains the outdoor temperature versus time below which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `minimum_outdoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_outdoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_outdoor_temperature_schedule_name`')

        self._data["Minimum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_outdoor_temperature(self):
        """Get maximum_outdoor_temperature

        Returns:
            float: the value of `maximum_outdoor_temperature` or None if not set
        """
        return self._data["Maximum Outdoor Temperature"]

    @maximum_outdoor_temperature.setter
    def maximum_outdoor_temperature(self, value=100.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_temperature`
        this is the outdoor temperature above which ventilation is shutoff

        Args:
            value (float): value for IDD Field `maximum_outdoor_temperature`
                Unit: C
                Default value: 100.0
                value >= -100.0
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
                                 'for field `maximum_outdoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `maximum_outdoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_outdoor_temperature`')

        self._data["Maximum Outdoor Temperature"] = value

    @property
    def maximum_outdoor_temperature_schedule_name(self):
        """Get maximum_outdoor_temperature_schedule_name

        Returns:
            str: the value of `maximum_outdoor_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Outdoor Temperature Schedule Name"]

    @maximum_outdoor_temperature_schedule_name.setter
    def maximum_outdoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_outdoor_temperature_schedule_name`
        This schedule contains the outdoor temperature versus time above which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `maximum_outdoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_outdoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_outdoor_temperature_schedule_name`')

        self._data["Maximum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_wind_speed(self):
        """Get maximum_wind_speed

        Returns:
            float: the value of `maximum_wind_speed` or None if not set
        """
        return self._data["Maximum Wind Speed"]

    @maximum_wind_speed.setter
    def maximum_wind_speed(self, value=40.0 ):
        """  Corresponds to IDD Field `maximum_wind_speed`
        this is the outdoor wind speed above which ventilation is shutoff

        Args:
            value (float): value for IDD Field `maximum_wind_speed`
                Unit: m/s
                Default value: 40.0
                value >= 0.0
                value <= 40.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_wind_speed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_wind_speed`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `maximum_wind_speed`')

        self._data["Maximum Wind Speed"] = value

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
        out.append(self._to_str(self.zone_or_zonelist_name))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_flow_rate_calculation_method))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.flow_rate_per_zone_floor_area))
        out.append(self._to_str(self.flow_rate_per_person))
        out.append(self._to_str(self.air_changes_per_hour))
        out.append(self._to_str(self.ventilation_type))
        out.append(self._to_str(self.fan_pressure_rise))
        out.append(self._to_str(self.fan_total_efficiency))
        out.append(self._to_str(self.constant_term_coefficient))
        out.append(self._to_str(self.temperature_term_coefficient))
        out.append(self._to_str(self.velocity_term_coefficient))
        out.append(self._to_str(self.velocity_squared_term_coefficient))
        out.append(self._to_str(self.minimum_indoor_temperature))
        out.append(self._to_str(self.minimum_indoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_indoor_temperature))
        out.append(self._to_str(self.maximum_indoor_temperature_schedule_name))
        out.append(self._to_str(self.delta_temperature))
        out.append(self._to_str(self.delta_temperature_schedule_name))
        out.append(self._to_str(self.minimum_outdoor_temperature))
        out.append(self._to_str(self.minimum_outdoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_outdoor_temperature))
        out.append(self._to_str(self.maximum_outdoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_wind_speed))
        return ",".join(out)

class ZoneVentilationWindandStackOpenArea(object):
    """ Corresponds to IDD object `ZoneVentilation:WindandStackOpenArea`
        This object is specified as natural ventilation driven by wind and stack effect only:
        Ventilation Wind = Cw * Opening Area * Schedule * WindSpd
        Ventilation Stack = Cd * Opening Area * Schedule * SQRT(2*g*DH*(|(Tzone-Todb)|/Tzone))
        Total Ventilation = SQRT((Ventilation Wind)^2 + (Ventilation Stack)^2)
    """
    internal_name = "ZoneVentilation:WindandStackOpenArea"
    field_count = 19

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneVentilation:WindandStackOpenArea`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Opening Area"] = None
        self._data["Opening Area Fraction Schedule Name"] = None
        self._data["Opening Effectiveness"] = None
        self._data["Effective Angle"] = None
        self._data["Height Difference"] = None
        self._data["Discharge Coefficient for Opening"] = None
        self._data["Minimum Indoor Temperature"] = None
        self._data["Minimum Indoor Temperature Schedule Name"] = None
        self._data["Maximum Indoor Temperature"] = None
        self._data["Maximum Indoor Temperature Schedule Name"] = None
        self._data["Delta Temperature"] = None
        self._data["Delta Temperature Schedule Name"] = None
        self._data["Minimum Outdoor Temperature"] = None
        self._data["Minimum Outdoor Temperature Schedule Name"] = None
        self._data["Maximum Outdoor Temperature"] = None
        self._data["Maximum Outdoor Temperature Schedule Name"] = None
        self._data["Maximum Wind Speed"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_area = None
        else:
            self.opening_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_area_fraction_schedule_name = None
        else:
            self.opening_area_fraction_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_effectiveness = None
        else:
            self.opening_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_angle = None
        else:
            self.effective_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_difference = None
        else:
            self.height_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening = None
        else:
            self.discharge_coefficient_for_opening = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_indoor_temperature = None
        else:
            self.minimum_indoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_indoor_temperature_schedule_name = None
        else:
            self.minimum_indoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_indoor_temperature = None
        else:
            self.maximum_indoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_indoor_temperature_schedule_name = None
        else:
            self.maximum_indoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_temperature = None
        else:
            self.delta_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_temperature_schedule_name = None
        else:
            self.delta_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature = None
        else:
            self.minimum_outdoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_schedule_name = None
        else:
            self.minimum_outdoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature = None
        else:
            self.maximum_outdoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_schedule_name = None
        else:
            self.maximum_outdoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_wind_speed = None
        else:
            self.maximum_wind_speed = vals[i]
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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

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
    def opening_area(self):
        """Get opening_area

        Returns:
            float: the value of `opening_area` or None if not set
        """
        return self._data["Opening Area"]

    @opening_area.setter
    def opening_area(self, value=0.0 ):
        """  Corresponds to IDD Field `opening_area`
        This is the opening area used to calculate stack effect and wind driven ventilation.

        Args:
            value (float): value for IDD Field `opening_area`
                Unit: m2
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
                                 'for field `opening_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `opening_area`')

        self._data["Opening Area"] = value

    @property
    def opening_area_fraction_schedule_name(self):
        """Get opening_area_fraction_schedule_name

        Returns:
            str: the value of `opening_area_fraction_schedule_name` or None if not set
        """
        return self._data["Opening Area Fraction Schedule Name"]

    @opening_area_fraction_schedule_name.setter
    def opening_area_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `opening_area_fraction_schedule_name`
        This schedule contains the fraction values applied to the opening area given in the previous
        input field (0.0 - 1.0).

        Args:
            value (str): value for IDD Field `opening_area_fraction_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `opening_area_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `opening_area_fraction_schedule_name`')

        self._data["Opening Area Fraction Schedule Name"] = value

    @property
    def opening_effectiveness(self):
        """Get opening_effectiveness

        Returns:
            float: the value of `opening_effectiveness` or None if not set
        """
        return self._data["Opening Effectiveness"]

    @opening_effectiveness.setter
    def opening_effectiveness(self, value=None):
        """  Corresponds to IDD Field `opening_effectiveness`
        This field is used to calculate wind driven ventilation.
        "Cw" in the wind-driven equation and the maximum value is 1.0.
        When the input is Autocalculate, the program calculates Cw based on an angle between
        wind direction and effective angle
        Cw = 0.55 at angle = 0, and Cw = 0.3 at angle=180
        Linear interpolation is used to calculate Cw based on the above two values.

        Args:
            value (float): value for IDD Field `opening_effectiveness`
                Unit: dimensionless
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
                                 'for field `opening_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `opening_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `opening_effectiveness`')

        self._data["Opening Effectiveness"] = value

    @property
    def effective_angle(self):
        """Get effective_angle

        Returns:
            float: the value of `effective_angle` or None if not set
        """
        return self._data["Effective Angle"]

    @effective_angle.setter
    def effective_angle(self, value=0.0 ):
        """  Corresponds to IDD Field `effective_angle`
        This field is defined as normal angle of the opening area and is used when input
        field Opening Effectiveness = Autocalculate.

        Args:
            value (float): value for IDD Field `effective_angle`
                Unit: deg
                Default value: 0.0
                value >= 0.0
                value < 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `effective_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `effective_angle`')
            if value >= 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `effective_angle`')

        self._data["Effective Angle"] = value

    @property
    def height_difference(self):
        """Get height_difference

        Returns:
            float: the value of `height_difference` or None if not set
        """
        return self._data["Height Difference"]

    @height_difference.setter
    def height_difference(self, value=0.0 ):
        """  Corresponds to IDD Field `height_difference`
        This is the height difference between the midpoint of an opening and
        the neutral pressure level.
        "DH" in the stack equation.

        Args:
            value (float): value for IDD Field `height_difference`
                Unit: m
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
                                 'for field `height_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `height_difference`')

        self._data["Height Difference"] = value

    @property
    def discharge_coefficient_for_opening(self):
        """Get discharge_coefficient_for_opening

        Returns:
            float: the value of `discharge_coefficient_for_opening` or None if not set
        """
        return self._data["Discharge Coefficient for Opening"]

    @discharge_coefficient_for_opening.setter
    def discharge_coefficient_for_opening(self, value=None):
        """  Corresponds to IDD Field `discharge_coefficient_for_opening`
        This is the discharge coefficient used to calculate stack effect.
        "Cd" in the stack equation and the maximum value is 1.0.
        When the input is Autocalculate, the following equation is used to calculate the
        coefficient:
        Cd = 0.4 + 0.0045*|(Tzone-Todb)|

        Args:
            value (float): value for IDD Field `discharge_coefficient_for_opening`
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
                                 'for field `discharge_coefficient_for_opening`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `discharge_coefficient_for_opening`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `discharge_coefficient_for_opening`')

        self._data["Discharge Coefficient for Opening"] = value

    @property
    def minimum_indoor_temperature(self):
        """Get minimum_indoor_temperature

        Returns:
            float: the value of `minimum_indoor_temperature` or None if not set
        """
        return self._data["Minimum Indoor Temperature"]

    @minimum_indoor_temperature.setter
    def minimum_indoor_temperature(self, value=-100.0 ):
        """  Corresponds to IDD Field `minimum_indoor_temperature`
        This is the indoor temperature below which ventilation is shutoff.

        Args:
            value (float): value for IDD Field `minimum_indoor_temperature`
                Unit: C
                Default value: -100.0
                value >= -100.0
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
                                 'for field `minimum_indoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_indoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_indoor_temperature`')

        self._data["Minimum Indoor Temperature"] = value

    @property
    def minimum_indoor_temperature_schedule_name(self):
        """Get minimum_indoor_temperature_schedule_name

        Returns:
            str: the value of `minimum_indoor_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Indoor Temperature Schedule Name"]

    @minimum_indoor_temperature_schedule_name.setter
    def minimum_indoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_indoor_temperature_schedule_name`
        This schedule contains the indoor temperature versus time below which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `minimum_indoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_indoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_indoor_temperature_schedule_name`')

        self._data["Minimum Indoor Temperature Schedule Name"] = value

    @property
    def maximum_indoor_temperature(self):
        """Get maximum_indoor_temperature

        Returns:
            float: the value of `maximum_indoor_temperature` or None if not set
        """
        return self._data["Maximum Indoor Temperature"]

    @maximum_indoor_temperature.setter
    def maximum_indoor_temperature(self, value=100.0 ):
        """  Corresponds to IDD Field `maximum_indoor_temperature`
        This is the indoor temperature above which ventilation is shutoff.

        Args:
            value (float): value for IDD Field `maximum_indoor_temperature`
                Unit: C
                Default value: 100.0
                value >= -100.0
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
                                 'for field `maximum_indoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `maximum_indoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_indoor_temperature`')

        self._data["Maximum Indoor Temperature"] = value

    @property
    def maximum_indoor_temperature_schedule_name(self):
        """Get maximum_indoor_temperature_schedule_name

        Returns:
            str: the value of `maximum_indoor_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Indoor Temperature Schedule Name"]

    @maximum_indoor_temperature_schedule_name.setter
    def maximum_indoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_indoor_temperature_schedule_name`
        This schedule contains the indoor temperature versus time above which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `maximum_indoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_indoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_indoor_temperature_schedule_name`')

        self._data["Maximum Indoor Temperature Schedule Name"] = value

    @property
    def delta_temperature(self):
        """Get delta_temperature

        Returns:
            float: the value of `delta_temperature` or None if not set
        """
        return self._data["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=-100.0 ):
        """  Corresponds to IDD Field `delta_temperature`
        This is the temperature differential between indoor and outdoor below
        which ventilation is shutoff.

        Args:
            value (float): value for IDD Field `delta_temperature`
                Unit: deltaC
                Default value: -100.0
                value >= -100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `delta_temperature`')

        self._data["Delta Temperature"] = value

    @property
    def delta_temperature_schedule_name(self):
        """Get delta_temperature_schedule_name

        Returns:
            str: the value of `delta_temperature_schedule_name` or None if not set
        """
        return self._data["Delta Temperature Schedule Name"]

    @delta_temperature_schedule_name.setter
    def delta_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `delta_temperature_schedule_name`
        This schedule contains the temperature differential between indoor and outdoor
        versus time below which ventilation is shutoff.

        Args:
            value (str): value for IDD Field `delta_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `delta_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `delta_temperature_schedule_name`')

        self._data["Delta Temperature Schedule Name"] = value

    @property
    def minimum_outdoor_temperature(self):
        """Get minimum_outdoor_temperature

        Returns:
            float: the value of `minimum_outdoor_temperature` or None if not set
        """
        return self._data["Minimum Outdoor Temperature"]

    @minimum_outdoor_temperature.setter
    def minimum_outdoor_temperature(self, value=-100.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_temperature`
        This is the outdoor temperature below which ventilation is shutoff.

        Args:
            value (float): value for IDD Field `minimum_outdoor_temperature`
                Unit: C
                Default value: -100.0
                value >= -100.0
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
                                 'for field `minimum_outdoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_outdoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_outdoor_temperature`')

        self._data["Minimum Outdoor Temperature"] = value

    @property
    def minimum_outdoor_temperature_schedule_name(self):
        """Get minimum_outdoor_temperature_schedule_name

        Returns:
            str: the value of `minimum_outdoor_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Outdoor Temperature Schedule Name"]

    @minimum_outdoor_temperature_schedule_name.setter
    def minimum_outdoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_outdoor_temperature_schedule_name`
        This schedule contains the outdoor temperature versus time below which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `minimum_outdoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_outdoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_outdoor_temperature_schedule_name`')

        self._data["Minimum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_outdoor_temperature(self):
        """Get maximum_outdoor_temperature

        Returns:
            float: the value of `maximum_outdoor_temperature` or None if not set
        """
        return self._data["Maximum Outdoor Temperature"]

    @maximum_outdoor_temperature.setter
    def maximum_outdoor_temperature(self, value=100.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_temperature`
        This is the outdoor temperature above which ventilation is shutoff.

        Args:
            value (float): value for IDD Field `maximum_outdoor_temperature`
                Unit: C
                Default value: 100.0
                value >= -100.0
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
                                 'for field `maximum_outdoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `maximum_outdoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_outdoor_temperature`')

        self._data["Maximum Outdoor Temperature"] = value

    @property
    def maximum_outdoor_temperature_schedule_name(self):
        """Get maximum_outdoor_temperature_schedule_name

        Returns:
            str: the value of `maximum_outdoor_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Outdoor Temperature Schedule Name"]

    @maximum_outdoor_temperature_schedule_name.setter
    def maximum_outdoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_outdoor_temperature_schedule_name`
        This schedule contains the outdoor temperature versus time above which
        ventilation is shutoff.

        Args:
            value (str): value for IDD Field `maximum_outdoor_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_outdoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_outdoor_temperature_schedule_name`')

        self._data["Maximum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_wind_speed(self):
        """Get maximum_wind_speed

        Returns:
            float: the value of `maximum_wind_speed` or None if not set
        """
        return self._data["Maximum Wind Speed"]

    @maximum_wind_speed.setter
    def maximum_wind_speed(self, value=40.0 ):
        """  Corresponds to IDD Field `maximum_wind_speed`
        This is the outdoor wind speed above which ventilation is shutoff.

        Args:
            value (float): value for IDD Field `maximum_wind_speed`
                Unit: m/s
                Default value: 40.0
                value >= 0.0
                value <= 40.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_wind_speed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_wind_speed`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `maximum_wind_speed`')

        self._data["Maximum Wind Speed"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.opening_area))
        out.append(self._to_str(self.opening_area_fraction_schedule_name))
        out.append(self._to_str(self.opening_effectiveness))
        out.append(self._to_str(self.effective_angle))
        out.append(self._to_str(self.height_difference))
        out.append(self._to_str(self.discharge_coefficient_for_opening))
        out.append(self._to_str(self.minimum_indoor_temperature))
        out.append(self._to_str(self.minimum_indoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_indoor_temperature))
        out.append(self._to_str(self.maximum_indoor_temperature_schedule_name))
        out.append(self._to_str(self.delta_temperature))
        out.append(self._to_str(self.delta_temperature_schedule_name))
        out.append(self._to_str(self.minimum_outdoor_temperature))
        out.append(self._to_str(self.minimum_outdoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_outdoor_temperature))
        out.append(self._to_str(self.maximum_outdoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_wind_speed))
        return ",".join(out)