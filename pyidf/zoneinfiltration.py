from collections import OrderedDict

class ZoneInfiltrationDesignFlowRate(object):
    """ Corresponds to IDD object `ZoneInfiltration:DesignFlowRate`
        Infiltration is specified as a design level which is modified by a Schedule fraction, temperature difference and wind speed:
        Infiltration=Idesign * FSchedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "ZoneInfiltration:DesignFlowRate"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneInfiltration:DesignFlowRate`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Flow Rate Calculation Method"] = None
        self._data["Design Flow Rate"] = None
        self._data["Flow per Zone Floor Area"] = None
        self._data["Flow per Exterior Surface Area"] = None
        self._data["Air Changes per Hour"] = None
        self._data["Constant Term Coefficient"] = None
        self._data["Temperature Term Coefficient"] = None
        self._data["Velocity Term Coefficient"] = None
        self._data["Velocity Squared Term Coefficient"] = None

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
            self.flow_per_zone_floor_area = None
        else:
            self.flow_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_per_exterior_surface_area = None
        else:
            self.flow_per_exterior_surface_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_changes_per_hour = None
        else:
            self.air_changes_per_hour = vals[i]
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
        The entered calculation method is used to create the maximum amount of infiltration
        for this set of attributes
        Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate
        Flow/Area => Flow per Zone Floor Area - Value * Floor Area (zone) = Design Flow Rate
        Flow/ExteriorArea => Flow per Exterior Surface Area - Value * Exterior Surface Area (zone) = Design Flow Rate
        Flow/ExteriorWallArea => Flow per Exterior Surface Area - Value * Exterior Wall Surface Area (zone) = Design Flow Rate
        AirChanges/Hour => Air Changes per Hour - Value * Floor Volume (zone) adjusted for m3/s = Design Volume Flow Rate
        "Idesign" in Equation is the result.

        Args:
            value (str): value for IDD Field `design_flow_rate_calculation_method`
                Accepted values are:
                      - Flow/Zone
                      - Flow/Area
                      - Flow/ExteriorArea
                      - Flow/ExteriorWallArea
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
            vals.add("Flow/ExteriorArea")
            vals.add("Flow/ExteriorWallArea")
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
    def flow_per_zone_floor_area(self):
        """Get flow_per_zone_floor_area

        Returns:
            float: the value of `flow_per_zone_floor_area` or None if not set
        """
        return self._data["Flow per Zone Floor Area"]

    @flow_per_zone_floor_area.setter
    def flow_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `flow_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `flow_per_zone_floor_area`
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
                                 'for field `flow_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `flow_per_zone_floor_area`')

        self._data["Flow per Zone Floor Area"] = value

    @property
    def flow_per_exterior_surface_area(self):
        """Get flow_per_exterior_surface_area

        Returns:
            float: the value of `flow_per_exterior_surface_area` or None if not set
        """
        return self._data["Flow per Exterior Surface Area"]

    @flow_per_exterior_surface_area.setter
    def flow_per_exterior_surface_area(self, value=None):
        """  Corresponds to IDD Field `flow_per_exterior_surface_area`
        use key Flow/ExteriorArea for all exterior surface area
        use key Flow/ExteriorWallArea to include only exterior wall area

        Args:
            value (float): value for IDD Field `flow_per_exterior_surface_area`
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
                                 'for field `flow_per_exterior_surface_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `flow_per_exterior_surface_area`')

        self._data["Flow per Exterior Surface Area"] = value

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
        out.append(self._to_str(self.flow_per_zone_floor_area))
        out.append(self._to_str(self.flow_per_exterior_surface_area))
        out.append(self._to_str(self.air_changes_per_hour))
        out.append(self._to_str(self.constant_term_coefficient))
        out.append(self._to_str(self.temperature_term_coefficient))
        out.append(self._to_str(self.velocity_term_coefficient))
        out.append(self._to_str(self.velocity_squared_term_coefficient))
        return ",".join(out)

class ZoneInfiltrationEffectiveLeakageArea(object):
    """ Corresponds to IDD object `ZoneInfiltration:EffectiveLeakageArea`
        Infiltration is specified as effective leakage area at 4 Pa, schedule fraction, stack and wind coefficients, and
        is a function of temperature difference and wind speed:
        Infiltration=FSchedule * (AL /1000) SQRT(Cs*|(Tzone-Todb)| +  Cw*WindSpd**2 )
    """
    internal_name = "ZoneInfiltration:EffectiveLeakageArea"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneInfiltration:EffectiveLeakageArea`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Effective Air Leakage Area"] = None
        self._data["Stack Coefficient"] = None
        self._data["Wind Coefficient"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_air_leakage_area = None
        else:
            self.effective_air_leakage_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.stack_coefficient = None
        else:
            self.stack_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_coefficient = None
        else:
            self.wind_coefficient = vals[i]
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
    def effective_air_leakage_area(self):
        """Get effective_air_leakage_area

        Returns:
            float: the value of `effective_air_leakage_area` or None if not set
        """
        return self._data["Effective Air Leakage Area"]

    @effective_air_leakage_area.setter
    def effective_air_leakage_area(self, value=None):
        """  Corresponds to IDD Field `effective_air_leakage_area`
        "AL" in Equation
        units are cm2 (square centimeters)

        Args:
            value (float): value for IDD Field `effective_air_leakage_area`
                Unit: cm2
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
                                 'for field `effective_air_leakage_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_air_leakage_area`')

        self._data["Effective Air Leakage Area"] = value

    @property
    def stack_coefficient(self):
        """Get stack_coefficient

        Returns:
            float: the value of `stack_coefficient` or None if not set
        """
        return self._data["Stack Coefficient"]

    @stack_coefficient.setter
    def stack_coefficient(self, value=None):
        """  Corresponds to IDD Field `stack_coefficient`
        "Cs" in Equation

        Args:
            value (float): value for IDD Field `stack_coefficient`
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
                                 'for field `stack_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `stack_coefficient`')

        self._data["Stack Coefficient"] = value

    @property
    def wind_coefficient(self):
        """Get wind_coefficient

        Returns:
            float: the value of `wind_coefficient` or None if not set
        """
        return self._data["Wind Coefficient"]

    @wind_coefficient.setter
    def wind_coefficient(self, value=None):
        """  Corresponds to IDD Field `wind_coefficient`
        "Cw" in Equation

        Args:
            value (float): value for IDD Field `wind_coefficient`
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
                                 'for field `wind_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `wind_coefficient`')

        self._data["Wind Coefficient"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.effective_air_leakage_area))
        out.append(self._to_str(self.stack_coefficient))
        out.append(self._to_str(self.wind_coefficient))
        return ",".join(out)

class ZoneInfiltrationFlowCoefficient(object):
    """ Corresponds to IDD object `ZoneInfiltration:FlowCoefficient`
        Infiltration is specified as flow coefficient, schedule fraction, stack and wind coefficients, and
        is a function of temperature difference and wind speed:
        Infiltration=FSchedule * SQRT( (c * Cs*|(Tzone-Todb)|**n)**2 + (c* Cw*(s * WindSpd)**2n)**2 )
    """
    internal_name = "ZoneInfiltration:FlowCoefficient"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneInfiltration:FlowCoefficient`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Flow Coefficient"] = None
        self._data["Stack Coefficient"] = None
        self._data["Pressure Exponent"] = None
        self._data["Wind Coefficient"] = None
        self._data["Shelter Factor"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_coefficient = None
        else:
            self.flow_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.stack_coefficient = None
        else:
            self.stack_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pressure_exponent = None
        else:
            self.pressure_exponent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_coefficient = None
        else:
            self.wind_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shelter_factor = None
        else:
            self.shelter_factor = vals[i]
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
    def flow_coefficient(self):
        """Get flow_coefficient

        Returns:
            float: the value of `flow_coefficient` or None if not set
        """
        return self._data["Flow Coefficient"]

    @flow_coefficient.setter
    def flow_coefficient(self, value=None):
        """  Corresponds to IDD Field `flow_coefficient`
        "c" in Equation

        Args:
            value (float): value for IDD Field `flow_coefficient`
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
                                 'for field `flow_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `flow_coefficient`')

        self._data["Flow Coefficient"] = value

    @property
    def stack_coefficient(self):
        """Get stack_coefficient

        Returns:
            float: the value of `stack_coefficient` or None if not set
        """
        return self._data["Stack Coefficient"]

    @stack_coefficient.setter
    def stack_coefficient(self, value=None):
        """  Corresponds to IDD Field `stack_coefficient`
        "Cs" in Equation

        Args:
            value (float): value for IDD Field `stack_coefficient`
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
                                 'for field `stack_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `stack_coefficient`')

        self._data["Stack Coefficient"] = value

    @property
    def pressure_exponent(self):
        """Get pressure_exponent

        Returns:
            float: the value of `pressure_exponent` or None if not set
        """
        return self._data["Pressure Exponent"]

    @pressure_exponent.setter
    def pressure_exponent(self, value=0.67 ):
        """  Corresponds to IDD Field `pressure_exponent`
        "n" in Equation

        Args:
            value (float): value for IDD Field `pressure_exponent`
                Default value: 0.67
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
                                 'for field `pressure_exponent`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pressure_exponent`')

        self._data["Pressure Exponent"] = value

    @property
    def wind_coefficient(self):
        """Get wind_coefficient

        Returns:
            float: the value of `wind_coefficient` or None if not set
        """
        return self._data["Wind Coefficient"]

    @wind_coefficient.setter
    def wind_coefficient(self, value=None):
        """  Corresponds to IDD Field `wind_coefficient`
        "Cw" in Equation

        Args:
            value (float): value for IDD Field `wind_coefficient`
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
                                 'for field `wind_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `wind_coefficient`')

        self._data["Wind Coefficient"] = value

    @property
    def shelter_factor(self):
        """Get shelter_factor

        Returns:
            float: the value of `shelter_factor` or None if not set
        """
        return self._data["Shelter Factor"]

    @shelter_factor.setter
    def shelter_factor(self, value=None):
        """  Corresponds to IDD Field `shelter_factor`
        "s" in Equation

        Args:
            value (float): value for IDD Field `shelter_factor`
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
                                 'for field `shelter_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `shelter_factor`')

        self._data["Shelter Factor"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.flow_coefficient))
        out.append(self._to_str(self.stack_coefficient))
        out.append(self._to_str(self.pressure_exponent))
        out.append(self._to_str(self.wind_coefficient))
        out.append(self._to_str(self.shelter_factor))
        return ",".join(out)