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
        """ Init data dictionary object for IDD  `ZoneInfiltration:DesignFlowRate`
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
        """ Init data dictionary object for IDD  `ZoneInfiltration:EffectiveLeakageArea`
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
        """ Init data dictionary object for IDD  `ZoneInfiltration:FlowCoefficient`
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
        """ Init data dictionary object for IDD  `ZoneVentilation:DesignFlowRate`
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
        """ Init data dictionary object for IDD  `ZoneVentilation:WindandStackOpenArea`
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

class ZoneAirBalanceOutdoorAir(object):
    """ Corresponds to IDD object `ZoneAirBalance:OutdoorAir`
        Provide a combined zone outdoor air flow by including interactions between
        mechanical ventilation, infiltration and duct leakage.
        This object will combine outdoor flows from all ZoneInfiltration and
        ZoneVentilation objects in the same zone. Balanced flows will be summed, while
        unbalanced flows will be added in quadrature.
    """
    internal_name = "ZoneAirBalance:OutdoorAir"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneAirBalance:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Air Balance Method"] = None
        self._data["Induced Outdoor Air Due to Unbalanced Duct Leakage"] = None
        self._data["Induced Outdoor Air Schedule Name"] = None

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
            self.air_balance_method = None
        else:
            self.air_balance_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.induced_outdoor_air_due_to_unbalanced_duct_leakage = None
        else:
            self.induced_outdoor_air_due_to_unbalanced_duct_leakage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.induced_outdoor_air_schedule_name = None
        else:
            self.induced_outdoor_air_schedule_name = vals[i]
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
    def air_balance_method(self):
        """Get air_balance_method

        Returns:
            str: the value of `air_balance_method` or None if not set
        """
        return self._data["Air Balance Method"]

    @air_balance_method.setter
    def air_balance_method(self, value="Quadrature"):
        """  Corresponds to IDD Field `air_balance_method`
        None: Only perform simple calculations without using a combined zone outdoor air.
        Quadrature: A combined outdoor air is used in the quadrature sum.

        Args:
            value (str): value for IDD Field `air_balance_method`
                Accepted values are:
                      - Quadrature
                      - None
                Default value: Quadrature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_balance_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_balance_method`')
            vals = set()
            vals.add("Quadrature")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `air_balance_method`'.format(value))

        self._data["Air Balance Method"] = value

    @property
    def induced_outdoor_air_due_to_unbalanced_duct_leakage(self):
        """Get induced_outdoor_air_due_to_unbalanced_duct_leakage

        Returns:
            float: the value of `induced_outdoor_air_due_to_unbalanced_duct_leakage` or None if not set
        """
        return self._data["Induced Outdoor Air Due to Unbalanced Duct Leakage"]

    @induced_outdoor_air_due_to_unbalanced_duct_leakage.setter
    def induced_outdoor_air_due_to_unbalanced_duct_leakage(self, value=0.0 ):
        """  Corresponds to IDD Field `induced_outdoor_air_due_to_unbalanced_duct_leakage`

        Args:
            value (float): value for IDD Field `induced_outdoor_air_due_to_unbalanced_duct_leakage`
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
                                 'for field `induced_outdoor_air_due_to_unbalanced_duct_leakage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `induced_outdoor_air_due_to_unbalanced_duct_leakage`')

        self._data["Induced Outdoor Air Due to Unbalanced Duct Leakage"] = value

    @property
    def induced_outdoor_air_schedule_name(self):
        """Get induced_outdoor_air_schedule_name

        Returns:
            str: the value of `induced_outdoor_air_schedule_name` or None if not set
        """
        return self._data["Induced Outdoor Air Schedule Name"]

    @induced_outdoor_air_schedule_name.setter
    def induced_outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `induced_outdoor_air_schedule_name`
        This schedule contains the fraction values applied to the Induced Outdoor Air given in the
        previous input field (0.0 - 1.0).

        Args:
            value (str): value for IDD Field `induced_outdoor_air_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `induced_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `induced_outdoor_air_schedule_name`')

        self._data["Induced Outdoor Air Schedule Name"] = value

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
        out.append(self._to_str(self.air_balance_method))
        out.append(self._to_str(self.induced_outdoor_air_due_to_unbalanced_duct_leakage))
        out.append(self._to_str(self.induced_outdoor_air_schedule_name))
        return ",".join(out)

class ZoneMixing(object):
    """ Corresponds to IDD object `ZoneMixing`
        ZoneMixing is a simple air exchange from one zone to another. Note that this statement
        only affects the energy balance of the "receiving" zone and will not produce
        any effect on the "source" zone. Mixing statements can be complementary and include
        multiple zones, but the balancing of flows between zones is left to the user's
        discretion.
    """
    internal_name = "ZoneMixing"
    field_count = 17

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneMixing`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Flow Rate Calculation Method"] = None
        self._data["Design Flow Rate"] = None
        self._data["Flow Rate per Zone Floor Area"] = None
        self._data["Flow Rate per Person"] = None
        self._data["Air Changes per Hour"] = None
        self._data["Source Zone Name"] = None
        self._data["Delta Temperature"] = None
        self._data["Delta Temperature Schedule Name"] = None
        self._data["Minimum Zone Temperature Schedule Name"] = None
        self._data["Maximum Zone Temperature Schedule Name"] = None
        self._data["Minimum Source Zone Temperature Schedule Name"] = None
        self._data["Maximum Source Zone Temperature Schedule Name"] = None
        self._data["Minimum Outdoor Temperature Schedule Name"] = None
        self._data["Maximum Outdoor Temperature Schedule Name"] = None

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
            self.source_zone_name = None
        else:
            self.source_zone_name = vals[i]
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
            self.minimum_zone_temperature_schedule_name = None
        else:
            self.minimum_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_zone_temperature_schedule_name = None
        else:
            self.maximum_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_source_zone_temperature_schedule_name = None
        else:
            self.minimum_source_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_source_zone_temperature_schedule_name = None
        else:
            self.maximum_source_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_schedule_name = None
        else:
            self.minimum_outdoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_schedule_name = None
        else:
            self.maximum_outdoor_temperature_schedule_name = vals[i]
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
    def source_zone_name(self):
        """Get source_zone_name

        Returns:
            str: the value of `source_zone_name` or None if not set
        """
        return self._data["Source Zone Name"]

    @source_zone_name.setter
    def source_zone_name(self, value=None):
        """  Corresponds to IDD Field `source_zone_name`

        Args:
            value (str): value for IDD Field `source_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_zone_name`')

        self._data["Source Zone Name"] = value

    @property
    def delta_temperature(self):
        """Get delta_temperature

        Returns:
            float: the value of `delta_temperature` or None if not set
        """
        return self._data["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `delta_temperature`
        This field contains the constant temperature differential between source and
        receiving zones below which mixing is shutoff.

        Args:
            value (float): value for IDD Field `delta_temperature`
                Unit: deltaC
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
                                 'for field `delta_temperature`'.format(value))

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
        This schedule contains the temperature differential between source and receiving
        zones versus time below which mixing is shutoff.

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
    def minimum_zone_temperature_schedule_name(self):
        """Get minimum_zone_temperature_schedule_name

        Returns:
            str: the value of `minimum_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Zone Temperature Schedule Name"]

    @minimum_zone_temperature_schedule_name.setter
    def minimum_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_zone_temperature_schedule_name`
        This schedule contains the zone dry-bulb temperature versus time below which
        mixing is shutoff.

        Args:
            value (str): value for IDD Field `minimum_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_zone_temperature_schedule_name`')

        self._data["Minimum Zone Temperature Schedule Name"] = value

    @property
    def maximum_zone_temperature_schedule_name(self):
        """Get maximum_zone_temperature_schedule_name

        Returns:
            str: the value of `maximum_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Zone Temperature Schedule Name"]

    @maximum_zone_temperature_schedule_name.setter
    def maximum_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_zone_temperature_schedule_name`
        This schedule contains the zone dry-bulb temperature versus time above which
        mixing is shutoff.

        Args:
            value (str): value for IDD Field `maximum_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_zone_temperature_schedule_name`')

        self._data["Maximum Zone Temperature Schedule Name"] = value

    @property
    def minimum_source_zone_temperature_schedule_name(self):
        """Get minimum_source_zone_temperature_schedule_name

        Returns:
            str: the value of `minimum_source_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Source Zone Temperature Schedule Name"]

    @minimum_source_zone_temperature_schedule_name.setter
    def minimum_source_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_source_zone_temperature_schedule_name`
        This schedule contains the source zone dry-bulb temperature versus time below
        which mixing is shutoff.

        Args:
            value (str): value for IDD Field `minimum_source_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_source_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_source_zone_temperature_schedule_name`')

        self._data["Minimum Source Zone Temperature Schedule Name"] = value

    @property
    def maximum_source_zone_temperature_schedule_name(self):
        """Get maximum_source_zone_temperature_schedule_name

        Returns:
            str: the value of `maximum_source_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Source Zone Temperature Schedule Name"]

    @maximum_source_zone_temperature_schedule_name.setter
    def maximum_source_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_source_zone_temperature_schedule_name`
        This schedule contains the source zone dry-bulb temperature versus time above
        which mixing is shutoff.

        Args:
            value (str): value for IDD Field `maximum_source_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_source_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_source_zone_temperature_schedule_name`')

        self._data["Maximum Source Zone Temperature Schedule Name"] = value

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
        mixing is shutoff.

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
        mixing is shutoff.

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
        out.append(self._to_str(self.design_flow_rate_calculation_method))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.flow_rate_per_zone_floor_area))
        out.append(self._to_str(self.flow_rate_per_person))
        out.append(self._to_str(self.air_changes_per_hour))
        out.append(self._to_str(self.source_zone_name))
        out.append(self._to_str(self.delta_temperature))
        out.append(self._to_str(self.delta_temperature_schedule_name))
        out.append(self._to_str(self.minimum_zone_temperature_schedule_name))
        out.append(self._to_str(self.maximum_zone_temperature_schedule_name))
        out.append(self._to_str(self.minimum_source_zone_temperature_schedule_name))
        out.append(self._to_str(self.maximum_source_zone_temperature_schedule_name))
        out.append(self._to_str(self.minimum_outdoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_outdoor_temperature_schedule_name))
        return ",".join(out)

class ZoneCrossMixing(object):
    """ Corresponds to IDD object `ZoneCrossMixing`
        ZoneCrossMixing exchanges an equal amount of air between two zones. Note that this
        statement affects the energy balance of both zones.
    """
    internal_name = "ZoneCrossMixing"
    field_count = 17

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneCrossMixing`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Flow Rate Calculation Method"] = None
        self._data["Design Flow Rate"] = None
        self._data["Flow Rate per Zone Floor Area"] = None
        self._data["Flow Rate per Person"] = None
        self._data["Air Changes per Hour"] = None
        self._data["Source Zone Name"] = None
        self._data["Delta Temperature"] = None
        self._data["Delta Temperature Schedule Name"] = None
        self._data["Minimum Zone Temperature Schedule Name"] = None
        self._data["Maximum Zone Temperature Schedule Name"] = None
        self._data["Minimum Source Zone Temperature Schedule Name"] = None
        self._data["Maximum Source Zone Temperature Schedule Name"] = None
        self._data["Minimum Outdoor Temperature Schedule Name"] = None
        self._data["Maximum Outdoor Temperature Schedule Name"] = None

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
            self.source_zone_name = None
        else:
            self.source_zone_name = vals[i]
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
            self.minimum_zone_temperature_schedule_name = None
        else:
            self.minimum_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_zone_temperature_schedule_name = None
        else:
            self.maximum_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_source_zone_temperature_schedule_name = None
        else:
            self.minimum_source_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_source_zone_temperature_schedule_name = None
        else:
            self.maximum_source_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_schedule_name = None
        else:
            self.minimum_outdoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_schedule_name = None
        else:
            self.maximum_outdoor_temperature_schedule_name = vals[i]
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
                      - Flow/Person
                      - Flow/Area
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
            vals.add("Flow/Person")
            vals.add("Flow/Area")
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
    def source_zone_name(self):
        """Get source_zone_name

        Returns:
            str: the value of `source_zone_name` or None if not set
        """
        return self._data["Source Zone Name"]

    @source_zone_name.setter
    def source_zone_name(self, value=None):
        """  Corresponds to IDD Field `source_zone_name`

        Args:
            value (str): value for IDD Field `source_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_zone_name`')

        self._data["Source Zone Name"] = value

    @property
    def delta_temperature(self):
        """Get delta_temperature

        Returns:
            float: the value of `delta_temperature` or None if not set
        """
        return self._data["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `delta_temperature`
        This field contains the constant temperature differential between source and
        receiving zones below which cross mixing is shutoff. This value must be greater
        than or equal to zero.

        Args:
            value (float): value for IDD Field `delta_temperature`
                Unit: deltaC
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
                                 'for field `delta_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
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
        This schedule contains the temperature differential between source and receiving
        zones versus time below which cross mixing is shutoff.

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
    def minimum_zone_temperature_schedule_name(self):
        """Get minimum_zone_temperature_schedule_name

        Returns:
            str: the value of `minimum_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Zone Temperature Schedule Name"]

    @minimum_zone_temperature_schedule_name.setter
    def minimum_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_zone_temperature_schedule_name`
        This schedule contains the indoor temperature versus time below which
        cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `minimum_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_zone_temperature_schedule_name`')

        self._data["Minimum Zone Temperature Schedule Name"] = value

    @property
    def maximum_zone_temperature_schedule_name(self):
        """Get maximum_zone_temperature_schedule_name

        Returns:
            str: the value of `maximum_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Zone Temperature Schedule Name"]

    @maximum_zone_temperature_schedule_name.setter
    def maximum_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_zone_temperature_schedule_name`
        This schedule contains the indoor temperature versus time above which
        cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `maximum_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_zone_temperature_schedule_name`')

        self._data["Maximum Zone Temperature Schedule Name"] = value

    @property
    def minimum_source_zone_temperature_schedule_name(self):
        """Get minimum_source_zone_temperature_schedule_name

        Returns:
            str: the value of `minimum_source_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Source Zone Temperature Schedule Name"]

    @minimum_source_zone_temperature_schedule_name.setter
    def minimum_source_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_source_zone_temperature_schedule_name`
        This schedule contains the source zone dry-bulb temperature versus time below
        which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `minimum_source_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_source_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_source_zone_temperature_schedule_name`')

        self._data["Minimum Source Zone Temperature Schedule Name"] = value

    @property
    def maximum_source_zone_temperature_schedule_name(self):
        """Get maximum_source_zone_temperature_schedule_name

        Returns:
            str: the value of `maximum_source_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Source Zone Temperature Schedule Name"]

    @maximum_source_zone_temperature_schedule_name.setter
    def maximum_source_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_source_zone_temperature_schedule_name`
        This schedule contains the source zone dry-bulb temperature versus time above
        which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `maximum_source_zone_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_source_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_source_zone_temperature_schedule_name`')

        self._data["Maximum Source Zone Temperature Schedule Name"] = value

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
        cross mixing is shutoff.

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
        cross mixing is shutoff.

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
        out.append(self._to_str(self.design_flow_rate_calculation_method))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.flow_rate_per_zone_floor_area))
        out.append(self._to_str(self.flow_rate_per_person))
        out.append(self._to_str(self.air_changes_per_hour))
        out.append(self._to_str(self.source_zone_name))
        out.append(self._to_str(self.delta_temperature))
        out.append(self._to_str(self.delta_temperature_schedule_name))
        out.append(self._to_str(self.minimum_zone_temperature_schedule_name))
        out.append(self._to_str(self.maximum_zone_temperature_schedule_name))
        out.append(self._to_str(self.minimum_source_zone_temperature_schedule_name))
        out.append(self._to_str(self.maximum_source_zone_temperature_schedule_name))
        out.append(self._to_str(self.minimum_outdoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_outdoor_temperature_schedule_name))
        return ",".join(out)

class ZoneRefrigerationDoorMixing(object):
    """ Corresponds to IDD object `ZoneRefrigerationDoorMixing`
        Refrigeration Door Mixing is used for an opening between two zones that are at the
        same elevation but have different air temperatures.  In this case, the mixing air flow
        between the two zones is determined by the density difference between the two zones.
        This would typically be used between two zones in a refrigerated warehouse that are
        controlled at different temperatures.  It could also be used to model a door to a walk-in
        refrigerated space if that space were modeled as a zone instead of using the object Refrigeration:WalkIn.
    """
    internal_name = "ZoneRefrigerationDoorMixing"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneRefrigerationDoorMixing`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone 1 Name"] = None
        self._data["Zone 2 Name"] = None
        self._data["Schedule Name"] = None
        self._data["Door Height"] = None
        self._data["Door Area"] = None
        self._data["Door Protection Type"] = None

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
            self.zone_1_name = None
        else:
            self.zone_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_2_name = None
        else:
            self.zone_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.door_height = None
        else:
            self.door_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.door_area = None
        else:
            self.door_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.door_protection_type = None
        else:
            self.door_protection_type = vals[i]
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
    def zone_1_name(self):
        """Get zone_1_name

        Returns:
            str: the value of `zone_1_name` or None if not set
        """
        return self._data["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """  Corresponds to IDD Field `zone_1_name`

        Args:
            value (str): value for IDD Field `zone_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_1_name`')

        self._data["Zone 1 Name"] = value

    @property
    def zone_2_name(self):
        """Get zone_2_name

        Returns:
            str: the value of `zone_2_name` or None if not set
        """
        return self._data["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """  Corresponds to IDD Field `zone_2_name`

        Args:
            value (str): value for IDD Field `zone_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_2_name`')

        self._data["Zone 2 Name"] = value

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
        This schedule defines the fraction of the time the refrigeration door is open
        For example, if the warehouse is closed at night and there are no door openings
        between two zones, the value for that time period would be 0.
        If doors were propped open, the value  over that time period would be 1.0
        If the doors were open about 20% of the time, the value over that period would be 0.2
        Schedule values must lie between 0 and 1.0

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
    def door_height(self):
        """Get door_height

        Returns:
            float: the value of `door_height` or None if not set
        """
        return self._data["Door Height"]

    @door_height.setter
    def door_height(self, value=3.0 ):
        """  Corresponds to IDD Field `door_height`

        Args:
            value (float): value for IDD Field `door_height`
                Unit: m
                Default value: 3.0
                value >= 0.0
                value <= 50.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `door_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `door_height`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `door_height`')

        self._data["Door Height"] = value

    @property
    def door_area(self):
        """Get door_area

        Returns:
            float: the value of `door_area` or None if not set
        """
        return self._data["Door Area"]

    @door_area.setter
    def door_area(self, value=9.0 ):
        """  Corresponds to IDD Field `door_area`

        Args:
            value (float): value for IDD Field `door_area`
                Unit: m2
                Default value: 9.0
                value >= 0.0
                value <= 400.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `door_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `door_area`')
            if value > 400.0:
                raise ValueError('value need to be smaller 400.0 '
                                 'for field `door_area`')

        self._data["Door Area"] = value

    @property
    def door_protection_type(self):
        """Get door_protection_type

        Returns:
            str: the value of `door_protection_type` or None if not set
        """
        return self._data["Door Protection Type"]

    @door_protection_type.setter
    def door_protection_type(self, value="None"):
        """  Corresponds to IDD Field `door_protection_type`
        Door protection can reduce the air flow through a refrigeration door
        The default value is "None"
        Choices: "None", "AirCurtain", and "StripCurtain"
        A strip curtain reduces the air flow more than an air curtain

        Args:
            value (str): value for IDD Field `door_protection_type`
                Accepted values are:
                      - None
                      - AirCurtain
                      - StripCurtain
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
                                 'for field `door_protection_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `door_protection_type`')
            vals = set()
            vals.add("None")
            vals.add("AirCurtain")
            vals.add("StripCurtain")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `door_protection_type`'.format(value))

        self._data["Door Protection Type"] = value

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
        out.append(self._to_str(self.zone_1_name))
        out.append(self._to_str(self.zone_2_name))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.door_height))
        out.append(self._to_str(self.door_area))
        out.append(self._to_str(self.door_protection_type))
        return ",".join(out)

class ZoneEarthtube(object):
    """ Corresponds to IDD object `ZoneEarthtube`
        Earth Tube is specified as a design level which is modified by a Schedule fraction, temperature difference and wind speed:
        Earthtube=Edesign * Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)
    """
    internal_name = "ZoneEarthtube"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneEarthtube`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Flow Rate"] = None
        self._data["Minimum Zone Temperature when Cooling"] = None
        self._data["Maximum Zone Temperature when Heating"] = None
        self._data["Delta Temperature"] = None
        self._data["Earthtube Type"] = None
        self._data["Fan Pressure Rise"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Pipe Radius"] = None
        self._data["Pipe Thickness"] = None
        self._data["Pipe Length"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Depth Under Ground Surface"] = None
        self._data["Soil Condition"] = None
        self._data["Average Soil Surface Temperature"] = None
        self._data["Amplitude of Soil Surface Temperature"] = None
        self._data["Phase Constant of Soil Surface Temperature"] = None
        self._data["Constant Term Flow Coefficient"] = None
        self._data["Temperature Term Flow Coefficient"] = None
        self._data["Velocity Term Flow Coefficient"] = None
        self._data["Velocity Squared Term Flow Coefficient"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
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
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_zone_temperature_when_cooling = None
        else:
            self.minimum_zone_temperature_when_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_zone_temperature_when_heating = None
        else:
            self.maximum_zone_temperature_when_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_temperature = None
        else:
            self.delta_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.earthtube_type = None
        else:
            self.earthtube_type = vals[i]
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
            self.pipe_radius = None
        else:
            self.pipe_radius = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_thickness = None
        else:
            self.pipe_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_length = None
        else:
            self.pipe_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_depth_under_ground_surface = None
        else:
            self.pipe_depth_under_ground_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_condition = None
        else:
            self.soil_condition = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.average_soil_surface_temperature = None
        else:
            self.average_soil_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.amplitude_of_soil_surface_temperature = None
        else:
            self.amplitude_of_soil_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.phase_constant_of_soil_surface_temperature = None
        else:
            self.phase_constant_of_soil_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_term_flow_coefficient = None
        else:
            self.constant_term_flow_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_term_flow_coefficient = None
        else:
            self.temperature_term_flow_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.velocity_term_flow_coefficient = None
        else:
            self.velocity_term_flow_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.velocity_squared_term_flow_coefficient = None
        else:
            self.velocity_squared_term_flow_coefficient = vals[i]
        i += 1

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
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_flow_rate`
        "Edesign" in Equation

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
    def minimum_zone_temperature_when_cooling(self):
        """Get minimum_zone_temperature_when_cooling

        Returns:
            float: the value of `minimum_zone_temperature_when_cooling` or None if not set
        """
        return self._data["Minimum Zone Temperature when Cooling"]

    @minimum_zone_temperature_when_cooling.setter
    def minimum_zone_temperature_when_cooling(self, value=None):
        """  Corresponds to IDD Field `minimum_zone_temperature_when_cooling`
        this is the indoor temperature below which the earth tube is shut off

        Args:
            value (float): value for IDD Field `minimum_zone_temperature_when_cooling`
                Unit: C
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
                                 'for field `minimum_zone_temperature_when_cooling`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_zone_temperature_when_cooling`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_zone_temperature_when_cooling`')

        self._data["Minimum Zone Temperature when Cooling"] = value

    @property
    def maximum_zone_temperature_when_heating(self):
        """Get maximum_zone_temperature_when_heating

        Returns:
            float: the value of `maximum_zone_temperature_when_heating` or None if not set
        """
        return self._data["Maximum Zone Temperature when Heating"]

    @maximum_zone_temperature_when_heating.setter
    def maximum_zone_temperature_when_heating(self, value=None):
        """  Corresponds to IDD Field `maximum_zone_temperature_when_heating`
        this is the indoor temperature above which the earth tube is shut off

        Args:
            value (float): value for IDD Field `maximum_zone_temperature_when_heating`
                Unit: C
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
                                 'for field `maximum_zone_temperature_when_heating`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `maximum_zone_temperature_when_heating`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_zone_temperature_when_heating`')

        self._data["Maximum Zone Temperature when Heating"] = value

    @property
    def delta_temperature(self):
        """Get delta_temperature

        Returns:
            float: the value of `delta_temperature` or None if not set
        """
        return self._data["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=None):
        """  Corresponds to IDD Field `delta_temperature`
        This is the temperature difference between indoor and outdoor below which the earth tube is shut off

        Args:
            value (float): value for IDD Field `delta_temperature`
                Unit: deltaC
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
                                 'for field `delta_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `delta_temperature`')

        self._data["Delta Temperature"] = value

    @property
    def earthtube_type(self):
        """Get earthtube_type

        Returns:
            str: the value of `earthtube_type` or None if not set
        """
        return self._data["Earthtube Type"]

    @earthtube_type.setter
    def earthtube_type(self, value="Natural"):
        """  Corresponds to IDD Field `earthtube_type`

        Args:
            value (str): value for IDD Field `earthtube_type`
                Accepted values are:
                      - Natural
                      - Intake
                      - Exhaust
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
                                 'for field `earthtube_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `earthtube_type`')
            vals = set()
            vals.add("Natural")
            vals.add("Intake")
            vals.add("Exhaust")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `earthtube_type`'.format(value))

        self._data["Earthtube Type"] = value

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
    def pipe_radius(self):
        """Get pipe_radius

        Returns:
            float: the value of `pipe_radius` or None if not set
        """
        return self._data["Pipe Radius"]

    @pipe_radius.setter
    def pipe_radius(self, value=1.0 ):
        """  Corresponds to IDD Field `pipe_radius`

        Args:
            value (float): value for IDD Field `pipe_radius`
                Unit: m
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
                                 'for field `pipe_radius`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_radius`')

        self._data["Pipe Radius"] = value

    @property
    def pipe_thickness(self):
        """Get pipe_thickness

        Returns:
            float: the value of `pipe_thickness` or None if not set
        """
        return self._data["Pipe Thickness"]

    @pipe_thickness.setter
    def pipe_thickness(self, value=0.2 ):
        """  Corresponds to IDD Field `pipe_thickness`

        Args:
            value (float): value for IDD Field `pipe_thickness`
                Unit: m
                Default value: 0.2
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
                                 'for field `pipe_thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thickness`')

        self._data["Pipe Thickness"] = value

    @property
    def pipe_length(self):
        """Get pipe_length

        Returns:
            float: the value of `pipe_length` or None if not set
        """
        return self._data["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=15.0 ):
        """  Corresponds to IDD Field `pipe_length`

        Args:
            value (float): value for IDD Field `pipe_length`
                Unit: m
                Default value: 15.0
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
                                 'for field `pipe_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_length`')

        self._data["Pipe Length"] = value

    @property
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=200.0 ):
        """  Corresponds to IDD Field `pipe_thermal_conductivity`

        Args:
            value (float): value for IDD Field `pipe_thermal_conductivity`
                Unit: W/m-K
                Default value: 200.0
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
                                 'for field `pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thermal_conductivity`')

        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_depth_under_ground_surface(self):
        """Get pipe_depth_under_ground_surface

        Returns:
            float: the value of `pipe_depth_under_ground_surface` or None if not set
        """
        return self._data["Pipe Depth Under Ground Surface"]

    @pipe_depth_under_ground_surface.setter
    def pipe_depth_under_ground_surface(self, value=3.0 ):
        """  Corresponds to IDD Field `pipe_depth_under_ground_surface`

        Args:
            value (float): value for IDD Field `pipe_depth_under_ground_surface`
                Unit: m
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
                                 'for field `pipe_depth_under_ground_surface`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_depth_under_ground_surface`')

        self._data["Pipe Depth Under Ground Surface"] = value

    @property
    def soil_condition(self):
        """Get soil_condition

        Returns:
            str: the value of `soil_condition` or None if not set
        """
        return self._data["Soil Condition"]

    @soil_condition.setter
    def soil_condition(self, value="HeavyAndDamp"):
        """  Corresponds to IDD Field `soil_condition`

        Args:
            value (str): value for IDD Field `soil_condition`
                Accepted values are:
                      - HeavyAndSaturated
                      - HeavyAndDamp
                      - HeavyAndDry
                      - LightAndDry
                Default value: HeavyAndDamp
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `soil_condition`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `soil_condition`')
            vals = set()
            vals.add("HeavyAndSaturated")
            vals.add("HeavyAndDamp")
            vals.add("HeavyAndDry")
            vals.add("LightAndDry")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `soil_condition`'.format(value))

        self._data["Soil Condition"] = value

    @property
    def average_soil_surface_temperature(self):
        """Get average_soil_surface_temperature

        Returns:
            float: the value of `average_soil_surface_temperature` or None if not set
        """
        return self._data["Average Soil Surface Temperature"]

    @average_soil_surface_temperature.setter
    def average_soil_surface_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `average_soil_surface_temperature`

        Args:
            value (float): value for IDD Field `average_soil_surface_temperature`
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
                                 'for field `average_soil_surface_temperature`'.format(value))

        self._data["Average Soil Surface Temperature"] = value

    @property
    def amplitude_of_soil_surface_temperature(self):
        """Get amplitude_of_soil_surface_temperature

        Returns:
            float: the value of `amplitude_of_soil_surface_temperature` or None if not set
        """
        return self._data["Amplitude of Soil Surface Temperature"]

    @amplitude_of_soil_surface_temperature.setter
    def amplitude_of_soil_surface_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `amplitude_of_soil_surface_temperature`

        Args:
            value (float): value for IDD Field `amplitude_of_soil_surface_temperature`
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
                                 'for field `amplitude_of_soil_surface_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `amplitude_of_soil_surface_temperature`')

        self._data["Amplitude of Soil Surface Temperature"] = value

    @property
    def phase_constant_of_soil_surface_temperature(self):
        """Get phase_constant_of_soil_surface_temperature

        Returns:
            float: the value of `phase_constant_of_soil_surface_temperature` or None if not set
        """
        return self._data["Phase Constant of Soil Surface Temperature"]

    @phase_constant_of_soil_surface_temperature.setter
    def phase_constant_of_soil_surface_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `phase_constant_of_soil_surface_temperature`

        Args:
            value (float): value for IDD Field `phase_constant_of_soil_surface_temperature`
                Unit: days
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
                                 'for field `phase_constant_of_soil_surface_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `phase_constant_of_soil_surface_temperature`')

        self._data["Phase Constant of Soil Surface Temperature"] = value

    @property
    def constant_term_flow_coefficient(self):
        """Get constant_term_flow_coefficient

        Returns:
            float: the value of `constant_term_flow_coefficient` or None if not set
        """
        return self._data["Constant Term Flow Coefficient"]

    @constant_term_flow_coefficient.setter
    def constant_term_flow_coefficient(self, value=1.0 ):
        """  Corresponds to IDD Field `constant_term_flow_coefficient`
        "A" in Equation

        Args:
            value (float): value for IDD Field `constant_term_flow_coefficient`
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
                                 'for field `constant_term_flow_coefficient`'.format(value))

        self._data["Constant Term Flow Coefficient"] = value

    @property
    def temperature_term_flow_coefficient(self):
        """Get temperature_term_flow_coefficient

        Returns:
            float: the value of `temperature_term_flow_coefficient` or None if not set
        """
        return self._data["Temperature Term Flow Coefficient"]

    @temperature_term_flow_coefficient.setter
    def temperature_term_flow_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_term_flow_coefficient`
        "B" in Equation

        Args:
            value (float): value for IDD Field `temperature_term_flow_coefficient`
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
                                 'for field `temperature_term_flow_coefficient`'.format(value))

        self._data["Temperature Term Flow Coefficient"] = value

    @property
    def velocity_term_flow_coefficient(self):
        """Get velocity_term_flow_coefficient

        Returns:
            float: the value of `velocity_term_flow_coefficient` or None if not set
        """
        return self._data["Velocity Term Flow Coefficient"]

    @velocity_term_flow_coefficient.setter
    def velocity_term_flow_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `velocity_term_flow_coefficient`
        "C" in Equation

        Args:
            value (float): value for IDD Field `velocity_term_flow_coefficient`
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
                                 'for field `velocity_term_flow_coefficient`'.format(value))

        self._data["Velocity Term Flow Coefficient"] = value

    @property
    def velocity_squared_term_flow_coefficient(self):
        """Get velocity_squared_term_flow_coefficient

        Returns:
            float: the value of `velocity_squared_term_flow_coefficient` or None if not set
        """
        return self._data["Velocity Squared Term Flow Coefficient"]

    @velocity_squared_term_flow_coefficient.setter
    def velocity_squared_term_flow_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `velocity_squared_term_flow_coefficient`
        "D" in Equation

        Args:
            value (float): value for IDD Field `velocity_squared_term_flow_coefficient`
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
                                 'for field `velocity_squared_term_flow_coefficient`'.format(value))

        self._data["Velocity Squared Term Flow Coefficient"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.minimum_zone_temperature_when_cooling))
        out.append(self._to_str(self.maximum_zone_temperature_when_heating))
        out.append(self._to_str(self.delta_temperature))
        out.append(self._to_str(self.earthtube_type))
        out.append(self._to_str(self.fan_pressure_rise))
        out.append(self._to_str(self.fan_total_efficiency))
        out.append(self._to_str(self.pipe_radius))
        out.append(self._to_str(self.pipe_thickness))
        out.append(self._to_str(self.pipe_length))
        out.append(self._to_str(self.pipe_thermal_conductivity))
        out.append(self._to_str(self.pipe_depth_under_ground_surface))
        out.append(self._to_str(self.soil_condition))
        out.append(self._to_str(self.average_soil_surface_temperature))
        out.append(self._to_str(self.amplitude_of_soil_surface_temperature))
        out.append(self._to_str(self.phase_constant_of_soil_surface_temperature))
        out.append(self._to_str(self.constant_term_flow_coefficient))
        out.append(self._to_str(self.temperature_term_flow_coefficient))
        out.append(self._to_str(self.velocity_term_flow_coefficient))
        out.append(self._to_str(self.velocity_squared_term_flow_coefficient))
        return ",".join(out)

class ZoneCoolTowerShower(object):
    """ Corresponds to IDD object `ZoneCoolTower:Shower`
        A cooltower (sometimes referred to as a wind tower or a shower cooling tower)
        models passive downdraught evaporative cooling (PDEC) that is designed to capture the
        wind at the top of a tower and cool the outdoor air using water evaporation before
        delivering it to a space.
    """
    internal_name = "ZoneCoolTower:Shower"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneCoolTower:Shower`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Water Supply Storage Tank Name"] = None
        self._data["Flow Control Type"] = None
        self._data["Pump Flow Rate Schedule Name"] = None
        self._data["Maximum Water Flow Rate"] = None
        self._data["Effective Tower Height"] = None
        self._data["Airflow Outlet Area"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Minimum Indoor Temperature"] = None
        self._data["Fraction of Water Loss"] = None
        self._data["Fraction of Flow Schedule"] = None
        self._data["Rated Power Consumption"] = None

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
            self.water_supply_storage_tank_name = None
        else:
            self.water_supply_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_control_type = None
        else:
            self.flow_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate = None
        else:
            self.maximum_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_tower_height = None
        else:
            self.effective_tower_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_outlet_area = None
        else:
            self.airflow_outlet_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_indoor_temperature = None
        else:
            self.minimum_indoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_water_loss = None
        else:
            self.fraction_of_water_loss = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_flow_schedule = None
        else:
            self.fraction_of_flow_schedule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
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
    def water_supply_storage_tank_name(self):
        """Get water_supply_storage_tank_name

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set
        """
        return self._data["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `water_supply_storage_tank_name`
        In case of stand alone tank or underground water, leave this input blank

        Args:
            value (str): value for IDD Field `water_supply_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_supply_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_supply_storage_tank_name`')

        self._data["Water Supply Storage Tank Name"] = value

    @property
    def flow_control_type(self):
        """Get flow_control_type

        Returns:
            str: the value of `flow_control_type` or None if not set
        """
        return self._data["Flow Control Type"]

    @flow_control_type.setter
    def flow_control_type(self, value="WindDrivenFlow"):
        """  Corresponds to IDD Field `flow_control_type`
        Water flow schedule should be selected when the water flow rate is known.
        Wind-driven flow should be selected when the water flow rate is unknown.

        Args:
            value (str): value for IDD Field `flow_control_type`
                Accepted values are:
                      - WaterFlowSchedule
                      - WindDrivenFlow
                Default value: WindDrivenFlow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `flow_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_control_type`')
            vals = set()
            vals.add("WaterFlowSchedule")
            vals.add("WindDrivenFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `flow_control_type`'.format(value))

        self._data["Flow Control Type"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """Get pump_flow_rate_schedule_name

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set
        """
        return self._data["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pump_flow_rate_schedule_name`

        Args:
            value (str): value for IDD Field `pump_flow_rate_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_flow_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_flow_rate_schedule_name`')

        self._data["Pump Flow Rate Schedule Name"] = value

    @property
    def maximum_water_flow_rate(self):
        """Get maximum_water_flow_rate

        Returns:
            float: the value of `maximum_water_flow_rate` or None if not set
        """
        return self._data["Maximum Water Flow Rate"]

    @maximum_water_flow_rate.setter
    def maximum_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_water_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_water_flow_rate`
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
                                 'for field `maximum_water_flow_rate`'.format(value))

        self._data["Maximum Water Flow Rate"] = value

    @property
    def effective_tower_height(self):
        """Get effective_tower_height

        Returns:
            float: the value of `effective_tower_height` or None if not set
        """
        return self._data["Effective Tower Height"]

    @effective_tower_height.setter
    def effective_tower_height(self, value=None):
        """  Corresponds to IDD Field `effective_tower_height`
        This field is from either the spray or the wet pad to the top of the outlet.

        Args:
            value (float): value for IDD Field `effective_tower_height`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `effective_tower_height`'.format(value))

        self._data["Effective Tower Height"] = value

    @property
    def airflow_outlet_area(self):
        """Get airflow_outlet_area

        Returns:
            float: the value of `airflow_outlet_area` or None if not set
        """
        return self._data["Airflow Outlet Area"]

    @airflow_outlet_area.setter
    def airflow_outlet_area(self, value=None):
        """  Corresponds to IDD Field `airflow_outlet_area`
        User have to specify effective area when outlet area is relatively bigger than the cross sectional area
        of cooltower. If the number of outlet is more than one, assume the air passes through only one.

        Args:
            value (float): value for IDD Field `airflow_outlet_area`
                Unit: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `airflow_outlet_area`'.format(value))

        self._data["Airflow Outlet Area"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

        self._data["Maximum Air Flow Rate"] = value

    @property
    def minimum_indoor_temperature(self):
        """Get minimum_indoor_temperature

        Returns:
            float: the value of `minimum_indoor_temperature` or None if not set
        """
        return self._data["Minimum Indoor Temperature"]

    @minimum_indoor_temperature.setter
    def minimum_indoor_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_indoor_temperature`
        This field is to specify the indoor temperature below which cooltower is shutoff.

        Args:
            value (float): value for IDD Field `minimum_indoor_temperature`
                Unit: C
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
    def fraction_of_water_loss(self):
        """Get fraction_of_water_loss

        Returns:
            float: the value of `fraction_of_water_loss` or None if not set
        """
        return self._data["Fraction of Water Loss"]

    @fraction_of_water_loss.setter
    def fraction_of_water_loss(self, value=None):
        """  Corresponds to IDD Field `fraction_of_water_loss`

        Args:
            value (float): value for IDD Field `fraction_of_water_loss`
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
                                 'for field `fraction_of_water_loss`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_water_loss`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_water_loss`')

        self._data["Fraction of Water Loss"] = value

    @property
    def fraction_of_flow_schedule(self):
        """Get fraction_of_flow_schedule

        Returns:
            float: the value of `fraction_of_flow_schedule` or None if not set
        """
        return self._data["Fraction of Flow Schedule"]

    @fraction_of_flow_schedule.setter
    def fraction_of_flow_schedule(self, value=None):
        """  Corresponds to IDD Field `fraction_of_flow_schedule`

        Args:
            value (float): value for IDD Field `fraction_of_flow_schedule`
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
                                 'for field `fraction_of_flow_schedule`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_flow_schedule`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_flow_schedule`')

        self._data["Fraction of Flow Schedule"] = value

    @property
    def rated_power_consumption(self):
        """Get rated_power_consumption

        Returns:
            float: the value of `rated_power_consumption` or None if not set
        """
        return self._data["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_power_consumption`

        Args:
            value (float): value for IDD Field `rated_power_consumption`
                Unit: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_power_consumption`'.format(value))

        self._data["Rated Power Consumption"] = value

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
        out.append(self._to_str(self.water_supply_storage_tank_name))
        out.append(self._to_str(self.flow_control_type))
        out.append(self._to_str(self.pump_flow_rate_schedule_name))
        out.append(self._to_str(self.maximum_water_flow_rate))
        out.append(self._to_str(self.effective_tower_height))
        out.append(self._to_str(self.airflow_outlet_area))
        out.append(self._to_str(self.maximum_air_flow_rate))
        out.append(self._to_str(self.minimum_indoor_temperature))
        out.append(self._to_str(self.fraction_of_water_loss))
        out.append(self._to_str(self.fraction_of_flow_schedule))
        out.append(self._to_str(self.rated_power_consumption))
        return ",".join(out)

class ZoneThermalChimney(object):
    """ Corresponds to IDD object `ZoneThermalChimney`
        A thermal chimney is a vertical shaft utilizing solar radiation to enhance natural
        ventilation. It consists of an absorber wall, air gap and glass cover with high solar
        transmissivity.
    """
    internal_name = "ZoneThermalChimney"
    field_count = 86

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneThermalChimney`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Width of the Absorber Wall"] = None
        self._data["Cross Sectional Area of Air Channel Outlet"] = None
        self._data["Discharge Coefficient"] = None
        self._data["Zone 1 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 1"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 1"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 1"] = None
        self._data["Zone 2 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 2"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 2"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 2"] = None
        self._data["Zone 3 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 3"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 3"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 3"] = None
        self._data["Zone 4 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 4"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 4"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 4"] = None
        self._data["Zone 5 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 5"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 5"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 5"] = None
        self._data["Zone 6 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 6"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 6"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 6"] = None
        self._data["Zone 7 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 7"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 7"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 7"] = None
        self._data["Zone 8 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 8"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 8"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 8"] = None
        self._data["Zone 9 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 9"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 9"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 9"] = None
        self._data["Zone 10 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 10"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 10"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 10"] = None
        self._data["Zone 11 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 11"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 11"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 11"] = None
        self._data["Zone 12 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 12"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 12"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 12"] = None
        self._data["Zone 13 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 13"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 13"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 13"] = None
        self._data["Zone 14 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 14"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 14"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 14"] = None
        self._data["Zone 15 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 15"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 15"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 15"] = None
        self._data["Zone 16 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 16"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 16"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 16"] = None
        self._data["Zone 17 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 17"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 17"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 17"] = None
        self._data["Zone 18 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 18"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 18"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 18"] = None
        self._data["Zone 19 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 19"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 19"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 19"] = None
        self._data["Zone 20 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 20"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 20"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 20"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_of_the_absorber_wall = None
        else:
            self.width_of_the_absorber_wall = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_area_of_air_channel_outlet = None
        else:
            self.cross_sectional_area_of_air_channel_outlet = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_1_name = None
        else:
            self.zone_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_1 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_1 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_1 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_2_name = None
        else:
            self.zone_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_2 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_2 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_2 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_3_name = None
        else:
            self.zone_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_3 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_3 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_3 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_4_name = None
        else:
            self.zone_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_4 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_4 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_4 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_5_name = None
        else:
            self.zone_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_5 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_5 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_5 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_6_name = None
        else:
            self.zone_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_6 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_6 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_6 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_7_name = None
        else:
            self.zone_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_7 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_7 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_7 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_8_name = None
        else:
            self.zone_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_8 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_8 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_8 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_9_name = None
        else:
            self.zone_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_9 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_9 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_9 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_10_name = None
        else:
            self.zone_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_10 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_10 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_10 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_11_name = None
        else:
            self.zone_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_11 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_11 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_11 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_12_name = None
        else:
            self.zone_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_12 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_12 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_12 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_13_name = None
        else:
            self.zone_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_13 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_13 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_13 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_14_name = None
        else:
            self.zone_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_14 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_14 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_14 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_15_name = None
        else:
            self.zone_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_15 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_15 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_15 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_16_name = None
        else:
            self.zone_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_16 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_16 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_16 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_17_name = None
        else:
            self.zone_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_17 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_17 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_17 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_18_name = None
        else:
            self.zone_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_18 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_18 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_18 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_19_name = None
        else:
            self.zone_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_19 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_19 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_19 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_20_name = None
        else:
            self.zone_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_20 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_20 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_20 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_20 = vals[i]
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
        Name of zone that is the thermal chimney

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
    def width_of_the_absorber_wall(self):
        """Get width_of_the_absorber_wall

        Returns:
            float: the value of `width_of_the_absorber_wall` or None if not set
        """
        return self._data["Width of the Absorber Wall"]

    @width_of_the_absorber_wall.setter
    def width_of_the_absorber_wall(self, value=None):
        """  Corresponds to IDD Field `width_of_the_absorber_wall`

        Args:
            value (float): value for IDD Field `width_of_the_absorber_wall`
                Unit: m
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
                                 'for field `width_of_the_absorber_wall`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `width_of_the_absorber_wall`')

        self._data["Width of the Absorber Wall"] = value

    @property
    def cross_sectional_area_of_air_channel_outlet(self):
        """Get cross_sectional_area_of_air_channel_outlet

        Returns:
            float: the value of `cross_sectional_area_of_air_channel_outlet` or None if not set
        """
        return self._data["Cross Sectional Area of Air Channel Outlet"]

    @cross_sectional_area_of_air_channel_outlet.setter
    def cross_sectional_area_of_air_channel_outlet(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_area_of_air_channel_outlet`

        Args:
            value (float): value for IDD Field `cross_sectional_area_of_air_channel_outlet`
                Unit: m2
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
                                 'for field `cross_sectional_area_of_air_channel_outlet`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_area_of_air_channel_outlet`')

        self._data["Cross Sectional Area of Air Channel Outlet"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient

        Returns:
            float: the value of `discharge_coefficient` or None if not set
        """
        return self._data["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=0.8 ):
        """  Corresponds to IDD Field `discharge_coefficient`

        Args:
            value (float): value for IDD Field `discharge_coefficient`
                Default value: 0.8
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
                                 'for field `discharge_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `discharge_coefficient`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `discharge_coefficient`')

        self._data["Discharge Coefficient"] = value

    @property
    def zone_1_name(self):
        """Get zone_1_name

        Returns:
            str: the value of `zone_1_name` or None if not set
        """
        return self._data["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """  Corresponds to IDD Field `zone_1_name`

        Args:
            value (str): value for IDD Field `zone_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_1_name`')

        self._data["Zone 1 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_1(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_1

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_1` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 1"]

    @distance_from_top_of_thermal_chimney_to_inlet_1.setter
    def distance_from_top_of_thermal_chimney_to_inlet_1(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_1`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_1`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_1`')

        self._data["Distance from Top of Thermal Chimney to Inlet 1"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_1(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_1

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_1` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 1"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_1.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_1(self, value=1.0 ):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_1`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_1`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_1`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 1"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_1(self):
        """Get cross_sectional_areas_of_air_channel_inlet_1

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_1` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 1"]

    @cross_sectional_areas_of_air_channel_inlet_1.setter
    def cross_sectional_areas_of_air_channel_inlet_1(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_1`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_1`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_1`')

        self._data["Cross Sectional Areas of Air Channel Inlet 1"] = value

    @property
    def zone_2_name(self):
        """Get zone_2_name

        Returns:
            str: the value of `zone_2_name` or None if not set
        """
        return self._data["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """  Corresponds to IDD Field `zone_2_name`

        Args:
            value (str): value for IDD Field `zone_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_2_name`')

        self._data["Zone 2 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_2(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_2

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_2` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 2"]

    @distance_from_top_of_thermal_chimney_to_inlet_2.setter
    def distance_from_top_of_thermal_chimney_to_inlet_2(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_2`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_2`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_2`')

        self._data["Distance from Top of Thermal Chimney to Inlet 2"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_2(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_2

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_2` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 2"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_2.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_2(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_2`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_2`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_2`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 2"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_2(self):
        """Get cross_sectional_areas_of_air_channel_inlet_2

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_2` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 2"]

    @cross_sectional_areas_of_air_channel_inlet_2.setter
    def cross_sectional_areas_of_air_channel_inlet_2(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_2`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_2`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_2`')

        self._data["Cross Sectional Areas of Air Channel Inlet 2"] = value

    @property
    def zone_3_name(self):
        """Get zone_3_name

        Returns:
            str: the value of `zone_3_name` or None if not set
        """
        return self._data["Zone 3 Name"]

    @zone_3_name.setter
    def zone_3_name(self, value=None):
        """  Corresponds to IDD Field `zone_3_name`

        Args:
            value (str): value for IDD Field `zone_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_3_name`')

        self._data["Zone 3 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_3(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_3

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_3` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 3"]

    @distance_from_top_of_thermal_chimney_to_inlet_3.setter
    def distance_from_top_of_thermal_chimney_to_inlet_3(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_3`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_3`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_3`')

        self._data["Distance from Top of Thermal Chimney to Inlet 3"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_3(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_3

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_3` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 3"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_3.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_3(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_3`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_3`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_3`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 3"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_3(self):
        """Get cross_sectional_areas_of_air_channel_inlet_3

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_3` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 3"]

    @cross_sectional_areas_of_air_channel_inlet_3.setter
    def cross_sectional_areas_of_air_channel_inlet_3(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_3`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_3`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_3`')

        self._data["Cross Sectional Areas of Air Channel Inlet 3"] = value

    @property
    def zone_4_name(self):
        """Get zone_4_name

        Returns:
            str: the value of `zone_4_name` or None if not set
        """
        return self._data["Zone 4 Name"]

    @zone_4_name.setter
    def zone_4_name(self, value=None):
        """  Corresponds to IDD Field `zone_4_name`

        Args:
            value (str): value for IDD Field `zone_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_4_name`')

        self._data["Zone 4 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_4(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_4

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_4` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 4"]

    @distance_from_top_of_thermal_chimney_to_inlet_4.setter
    def distance_from_top_of_thermal_chimney_to_inlet_4(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_4`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_4`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_4`')

        self._data["Distance from Top of Thermal Chimney to Inlet 4"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_4(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_4

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_4` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 4"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_4.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_4(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_4`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_4`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_4`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 4"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_4(self):
        """Get cross_sectional_areas_of_air_channel_inlet_4

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_4` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 4"]

    @cross_sectional_areas_of_air_channel_inlet_4.setter
    def cross_sectional_areas_of_air_channel_inlet_4(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_4`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_4`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_4`')

        self._data["Cross Sectional Areas of Air Channel Inlet 4"] = value

    @property
    def zone_5_name(self):
        """Get zone_5_name

        Returns:
            str: the value of `zone_5_name` or None if not set
        """
        return self._data["Zone 5 Name"]

    @zone_5_name.setter
    def zone_5_name(self, value=None):
        """  Corresponds to IDD Field `zone_5_name`

        Args:
            value (str): value for IDD Field `zone_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_5_name`')

        self._data["Zone 5 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_5(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_5

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_5` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 5"]

    @distance_from_top_of_thermal_chimney_to_inlet_5.setter
    def distance_from_top_of_thermal_chimney_to_inlet_5(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_5`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_5`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_5`')

        self._data["Distance from Top of Thermal Chimney to Inlet 5"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_5(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_5

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_5` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 5"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_5.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_5(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_5`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_5`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_5`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_5`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 5"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_5(self):
        """Get cross_sectional_areas_of_air_channel_inlet_5

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_5` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 5"]

    @cross_sectional_areas_of_air_channel_inlet_5.setter
    def cross_sectional_areas_of_air_channel_inlet_5(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_5`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_5`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_5`')

        self._data["Cross Sectional Areas of Air Channel Inlet 5"] = value

    @property
    def zone_6_name(self):
        """Get zone_6_name

        Returns:
            str: the value of `zone_6_name` or None if not set
        """
        return self._data["Zone 6 Name"]

    @zone_6_name.setter
    def zone_6_name(self, value=None):
        """  Corresponds to IDD Field `zone_6_name`

        Args:
            value (str): value for IDD Field `zone_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_6_name`')

        self._data["Zone 6 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_6(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_6

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_6` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 6"]

    @distance_from_top_of_thermal_chimney_to_inlet_6.setter
    def distance_from_top_of_thermal_chimney_to_inlet_6(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_6`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_6`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_6`')

        self._data["Distance from Top of Thermal Chimney to Inlet 6"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_6(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_6

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_6` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 6"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_6.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_6(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_6`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_6`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_6`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_6`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 6"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_6(self):
        """Get cross_sectional_areas_of_air_channel_inlet_6

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_6` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 6"]

    @cross_sectional_areas_of_air_channel_inlet_6.setter
    def cross_sectional_areas_of_air_channel_inlet_6(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_6`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_6`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_6`')

        self._data["Cross Sectional Areas of Air Channel Inlet 6"] = value

    @property
    def zone_7_name(self):
        """Get zone_7_name

        Returns:
            str: the value of `zone_7_name` or None if not set
        """
        return self._data["Zone 7 Name"]

    @zone_7_name.setter
    def zone_7_name(self, value=None):
        """  Corresponds to IDD Field `zone_7_name`

        Args:
            value (str): value for IDD Field `zone_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_7_name`')

        self._data["Zone 7 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_7(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_7

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_7` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 7"]

    @distance_from_top_of_thermal_chimney_to_inlet_7.setter
    def distance_from_top_of_thermal_chimney_to_inlet_7(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_7`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_7`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_7`')

        self._data["Distance from Top of Thermal Chimney to Inlet 7"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_7(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_7

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_7` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 7"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_7.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_7(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_7`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_7`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_7`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_7`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 7"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_7(self):
        """Get cross_sectional_areas_of_air_channel_inlet_7

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_7` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 7"]

    @cross_sectional_areas_of_air_channel_inlet_7.setter
    def cross_sectional_areas_of_air_channel_inlet_7(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_7`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_7`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_7`')

        self._data["Cross Sectional Areas of Air Channel Inlet 7"] = value

    @property
    def zone_8_name(self):
        """Get zone_8_name

        Returns:
            str: the value of `zone_8_name` or None if not set
        """
        return self._data["Zone 8 Name"]

    @zone_8_name.setter
    def zone_8_name(self, value=None):
        """  Corresponds to IDD Field `zone_8_name`

        Args:
            value (str): value for IDD Field `zone_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_8_name`')

        self._data["Zone 8 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_8(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_8

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_8` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 8"]

    @distance_from_top_of_thermal_chimney_to_inlet_8.setter
    def distance_from_top_of_thermal_chimney_to_inlet_8(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_8`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_8`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_8`')

        self._data["Distance from Top of Thermal Chimney to Inlet 8"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_8(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_8

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_8` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 8"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_8.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_8(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_8`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_8`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_8`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_8`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 8"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_8(self):
        """Get cross_sectional_areas_of_air_channel_inlet_8

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_8` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 8"]

    @cross_sectional_areas_of_air_channel_inlet_8.setter
    def cross_sectional_areas_of_air_channel_inlet_8(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_8`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_8`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_8`')

        self._data["Cross Sectional Areas of Air Channel Inlet 8"] = value

    @property
    def zone_9_name(self):
        """Get zone_9_name

        Returns:
            str: the value of `zone_9_name` or None if not set
        """
        return self._data["Zone 9 Name"]

    @zone_9_name.setter
    def zone_9_name(self, value=None):
        """  Corresponds to IDD Field `zone_9_name`

        Args:
            value (str): value for IDD Field `zone_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_9_name`')

        self._data["Zone 9 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_9(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_9

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_9` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 9"]

    @distance_from_top_of_thermal_chimney_to_inlet_9.setter
    def distance_from_top_of_thermal_chimney_to_inlet_9(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_9`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_9`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_9`')

        self._data["Distance from Top of Thermal Chimney to Inlet 9"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_9(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_9

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_9` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 9"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_9.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_9(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_9`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_9`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_9`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_9`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 9"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_9(self):
        """Get cross_sectional_areas_of_air_channel_inlet_9

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_9` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 9"]

    @cross_sectional_areas_of_air_channel_inlet_9.setter
    def cross_sectional_areas_of_air_channel_inlet_9(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_9`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_9`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_9`')

        self._data["Cross Sectional Areas of Air Channel Inlet 9"] = value

    @property
    def zone_10_name(self):
        """Get zone_10_name

        Returns:
            str: the value of `zone_10_name` or None if not set
        """
        return self._data["Zone 10 Name"]

    @zone_10_name.setter
    def zone_10_name(self, value=None):
        """  Corresponds to IDD Field `zone_10_name`

        Args:
            value (str): value for IDD Field `zone_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_10_name`')

        self._data["Zone 10 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_10(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_10

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_10` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 10"]

    @distance_from_top_of_thermal_chimney_to_inlet_10.setter
    def distance_from_top_of_thermal_chimney_to_inlet_10(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_10`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_10`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_10`')

        self._data["Distance from Top of Thermal Chimney to Inlet 10"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_10(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_10

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_10` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 10"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_10.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_10(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_10`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_10`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_10`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_10`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 10"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_10(self):
        """Get cross_sectional_areas_of_air_channel_inlet_10

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_10` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 10"]

    @cross_sectional_areas_of_air_channel_inlet_10.setter
    def cross_sectional_areas_of_air_channel_inlet_10(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_10`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_10`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_10`')

        self._data["Cross Sectional Areas of Air Channel Inlet 10"] = value

    @property
    def zone_11_name(self):
        """Get zone_11_name

        Returns:
            str: the value of `zone_11_name` or None if not set
        """
        return self._data["Zone 11 Name"]

    @zone_11_name.setter
    def zone_11_name(self, value=None):
        """  Corresponds to IDD Field `zone_11_name`

        Args:
            value (str): value for IDD Field `zone_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_11_name`')

        self._data["Zone 11 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_11(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_11

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_11` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 11"]

    @distance_from_top_of_thermal_chimney_to_inlet_11.setter
    def distance_from_top_of_thermal_chimney_to_inlet_11(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_11`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_11`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_11`')

        self._data["Distance from Top of Thermal Chimney to Inlet 11"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_11(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_11

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_11` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 11"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_11.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_11(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_11`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_11`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_11`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_11`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 11"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_11(self):
        """Get cross_sectional_areas_of_air_channel_inlet_11

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_11` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 11"]

    @cross_sectional_areas_of_air_channel_inlet_11.setter
    def cross_sectional_areas_of_air_channel_inlet_11(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_11`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_11`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_11`')

        self._data["Cross Sectional Areas of Air Channel Inlet 11"] = value

    @property
    def zone_12_name(self):
        """Get zone_12_name

        Returns:
            str: the value of `zone_12_name` or None if not set
        """
        return self._data["Zone 12 Name"]

    @zone_12_name.setter
    def zone_12_name(self, value=None):
        """  Corresponds to IDD Field `zone_12_name`

        Args:
            value (str): value for IDD Field `zone_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_12_name`')

        self._data["Zone 12 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_12(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_12

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_12` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 12"]

    @distance_from_top_of_thermal_chimney_to_inlet_12.setter
    def distance_from_top_of_thermal_chimney_to_inlet_12(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_12`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_12`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_12`')

        self._data["Distance from Top of Thermal Chimney to Inlet 12"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_12(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_12

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_12` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 12"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_12.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_12(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_12`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_12`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_12`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_12`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 12"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_12(self):
        """Get cross_sectional_areas_of_air_channel_inlet_12

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_12` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 12"]

    @cross_sectional_areas_of_air_channel_inlet_12.setter
    def cross_sectional_areas_of_air_channel_inlet_12(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_12`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_12`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_12`')

        self._data["Cross Sectional Areas of Air Channel Inlet 12"] = value

    @property
    def zone_13_name(self):
        """Get zone_13_name

        Returns:
            str: the value of `zone_13_name` or None if not set
        """
        return self._data["Zone 13 Name"]

    @zone_13_name.setter
    def zone_13_name(self, value=None):
        """  Corresponds to IDD Field `zone_13_name`

        Args:
            value (str): value for IDD Field `zone_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_13_name`')

        self._data["Zone 13 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_13(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_13

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_13` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 13"]

    @distance_from_top_of_thermal_chimney_to_inlet_13.setter
    def distance_from_top_of_thermal_chimney_to_inlet_13(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_13`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_13`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_13`')

        self._data["Distance from Top of Thermal Chimney to Inlet 13"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_13(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_13

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_13` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 13"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_13.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_13(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_13`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_13`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_13`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_13`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 13"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_13(self):
        """Get cross_sectional_areas_of_air_channel_inlet_13

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_13` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 13"]

    @cross_sectional_areas_of_air_channel_inlet_13.setter
    def cross_sectional_areas_of_air_channel_inlet_13(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_13`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_13`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_13`')

        self._data["Cross Sectional Areas of Air Channel Inlet 13"] = value

    @property
    def zone_14_name(self):
        """Get zone_14_name

        Returns:
            str: the value of `zone_14_name` or None if not set
        """
        return self._data["Zone 14 Name"]

    @zone_14_name.setter
    def zone_14_name(self, value=None):
        """  Corresponds to IDD Field `zone_14_name`

        Args:
            value (str): value for IDD Field `zone_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_14_name`')

        self._data["Zone 14 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_14(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_14

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_14` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 14"]

    @distance_from_top_of_thermal_chimney_to_inlet_14.setter
    def distance_from_top_of_thermal_chimney_to_inlet_14(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_14`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_14`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_14`')

        self._data["Distance from Top of Thermal Chimney to Inlet 14"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_14(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_14

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_14` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 14"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_14.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_14(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_14`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_14`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_14`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_14`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 14"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_14(self):
        """Get cross_sectional_areas_of_air_channel_inlet_14

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_14` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 14"]

    @cross_sectional_areas_of_air_channel_inlet_14.setter
    def cross_sectional_areas_of_air_channel_inlet_14(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_14`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_14`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_14`')

        self._data["Cross Sectional Areas of Air Channel Inlet 14"] = value

    @property
    def zone_15_name(self):
        """Get zone_15_name

        Returns:
            str: the value of `zone_15_name` or None if not set
        """
        return self._data["Zone 15 Name"]

    @zone_15_name.setter
    def zone_15_name(self, value=None):
        """  Corresponds to IDD Field `zone_15_name`

        Args:
            value (str): value for IDD Field `zone_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_15_name`')

        self._data["Zone 15 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_15(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_15

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_15` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 15"]

    @distance_from_top_of_thermal_chimney_to_inlet_15.setter
    def distance_from_top_of_thermal_chimney_to_inlet_15(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_15`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_15`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_15`')

        self._data["Distance from Top of Thermal Chimney to Inlet 15"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_15(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_15

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_15` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 15"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_15.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_15(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_15`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_15`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_15`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_15`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 15"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_15(self):
        """Get cross_sectional_areas_of_air_channel_inlet_15

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_15` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 15"]

    @cross_sectional_areas_of_air_channel_inlet_15.setter
    def cross_sectional_areas_of_air_channel_inlet_15(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_15`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_15`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_15`')

        self._data["Cross Sectional Areas of Air Channel Inlet 15"] = value

    @property
    def zone_16_name(self):
        """Get zone_16_name

        Returns:
            str: the value of `zone_16_name` or None if not set
        """
        return self._data["Zone 16 Name"]

    @zone_16_name.setter
    def zone_16_name(self, value=None):
        """  Corresponds to IDD Field `zone_16_name`

        Args:
            value (str): value for IDD Field `zone_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_16_name`')

        self._data["Zone 16 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_16(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_16

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_16` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 16"]

    @distance_from_top_of_thermal_chimney_to_inlet_16.setter
    def distance_from_top_of_thermal_chimney_to_inlet_16(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_16`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_16`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_16`')

        self._data["Distance from Top of Thermal Chimney to Inlet 16"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_16(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_16

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_16` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 16"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_16.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_16(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_16`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_16`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_16`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_16`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 16"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_16(self):
        """Get cross_sectional_areas_of_air_channel_inlet_16

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_16` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 16"]

    @cross_sectional_areas_of_air_channel_inlet_16.setter
    def cross_sectional_areas_of_air_channel_inlet_16(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_16`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_16`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_16`')

        self._data["Cross Sectional Areas of Air Channel Inlet 16"] = value

    @property
    def zone_17_name(self):
        """Get zone_17_name

        Returns:
            str: the value of `zone_17_name` or None if not set
        """
        return self._data["Zone 17 Name"]

    @zone_17_name.setter
    def zone_17_name(self, value=None):
        """  Corresponds to IDD Field `zone_17_name`

        Args:
            value (str): value for IDD Field `zone_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_17_name`')

        self._data["Zone 17 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_17(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_17

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_17` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 17"]

    @distance_from_top_of_thermal_chimney_to_inlet_17.setter
    def distance_from_top_of_thermal_chimney_to_inlet_17(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_17`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_17`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_17`')

        self._data["Distance from Top of Thermal Chimney to Inlet 17"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_17(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_17

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_17` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 17"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_17.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_17(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_17`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_17`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_17`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_17`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 17"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_17(self):
        """Get cross_sectional_areas_of_air_channel_inlet_17

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_17` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 17"]

    @cross_sectional_areas_of_air_channel_inlet_17.setter
    def cross_sectional_areas_of_air_channel_inlet_17(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_17`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_17`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_17`')

        self._data["Cross Sectional Areas of Air Channel Inlet 17"] = value

    @property
    def zone_18_name(self):
        """Get zone_18_name

        Returns:
            str: the value of `zone_18_name` or None if not set
        """
        return self._data["Zone 18 Name"]

    @zone_18_name.setter
    def zone_18_name(self, value=None):
        """  Corresponds to IDD Field `zone_18_name`

        Args:
            value (str): value for IDD Field `zone_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_18_name`')

        self._data["Zone 18 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_18(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_18

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_18` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 18"]

    @distance_from_top_of_thermal_chimney_to_inlet_18.setter
    def distance_from_top_of_thermal_chimney_to_inlet_18(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_18`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_18`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_18`')

        self._data["Distance from Top of Thermal Chimney to Inlet 18"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_18(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_18

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_18` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 18"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_18.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_18(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_18`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_18`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_18`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_18`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 18"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_18(self):
        """Get cross_sectional_areas_of_air_channel_inlet_18

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_18` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 18"]

    @cross_sectional_areas_of_air_channel_inlet_18.setter
    def cross_sectional_areas_of_air_channel_inlet_18(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_18`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_18`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_18`')

        self._data["Cross Sectional Areas of Air Channel Inlet 18"] = value

    @property
    def zone_19_name(self):
        """Get zone_19_name

        Returns:
            str: the value of `zone_19_name` or None if not set
        """
        return self._data["Zone 19 Name"]

    @zone_19_name.setter
    def zone_19_name(self, value=None):
        """  Corresponds to IDD Field `zone_19_name`

        Args:
            value (str): value for IDD Field `zone_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_19_name`')

        self._data["Zone 19 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_19(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_19

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_19` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 19"]

    @distance_from_top_of_thermal_chimney_to_inlet_19.setter
    def distance_from_top_of_thermal_chimney_to_inlet_19(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_19`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_19`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_19`')

        self._data["Distance from Top of Thermal Chimney to Inlet 19"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_19(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_19

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_19` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 19"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_19.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_19(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_19`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_19`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_19`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_19`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 19"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_19(self):
        """Get cross_sectional_areas_of_air_channel_inlet_19

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_19` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 19"]

    @cross_sectional_areas_of_air_channel_inlet_19.setter
    def cross_sectional_areas_of_air_channel_inlet_19(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_19`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_19`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_19`')

        self._data["Cross Sectional Areas of Air Channel Inlet 19"] = value

    @property
    def zone_20_name(self):
        """Get zone_20_name

        Returns:
            str: the value of `zone_20_name` or None if not set
        """
        return self._data["Zone 20 Name"]

    @zone_20_name.setter
    def zone_20_name(self, value=None):
        """  Corresponds to IDD Field `zone_20_name`

        Args:
            value (str): value for IDD Field `zone_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_20_name`')

        self._data["Zone 20 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_20(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_20

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_20` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 20"]

    @distance_from_top_of_thermal_chimney_to_inlet_20.setter
    def distance_from_top_of_thermal_chimney_to_inlet_20(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_20`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_20`
                Unit: m
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_20`')

        self._data["Distance from Top of Thermal Chimney to Inlet 20"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_20(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_20

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_20` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 20"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_20.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_20(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_20`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_20`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_20`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_20`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 20"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_20(self):
        """Get cross_sectional_areas_of_air_channel_inlet_20

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_20` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 20"]

    @cross_sectional_areas_of_air_channel_inlet_20.setter
    def cross_sectional_areas_of_air_channel_inlet_20(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_20`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_20`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_20`')

        self._data["Cross Sectional Areas of Air Channel Inlet 20"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.width_of_the_absorber_wall))
        out.append(self._to_str(self.cross_sectional_area_of_air_channel_outlet))
        out.append(self._to_str(self.discharge_coefficient))
        out.append(self._to_str(self.zone_1_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_1))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_1))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_1))
        out.append(self._to_str(self.zone_2_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_2))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_2))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_2))
        out.append(self._to_str(self.zone_3_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_3))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_3))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_3))
        out.append(self._to_str(self.zone_4_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_4))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_4))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_4))
        out.append(self._to_str(self.zone_5_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_5))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_5))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_5))
        out.append(self._to_str(self.zone_6_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_6))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_6))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_6))
        out.append(self._to_str(self.zone_7_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_7))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_7))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_7))
        out.append(self._to_str(self.zone_8_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_8))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_8))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_8))
        out.append(self._to_str(self.zone_9_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_9))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_9))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_9))
        out.append(self._to_str(self.zone_10_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_10))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_10))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_10))
        out.append(self._to_str(self.zone_11_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_11))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_11))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_11))
        out.append(self._to_str(self.zone_12_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_12))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_12))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_12))
        out.append(self._to_str(self.zone_13_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_13))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_13))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_13))
        out.append(self._to_str(self.zone_14_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_14))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_14))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_14))
        out.append(self._to_str(self.zone_15_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_15))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_15))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_15))
        out.append(self._to_str(self.zone_16_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_16))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_16))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_16))
        out.append(self._to_str(self.zone_17_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_17))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_17))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_17))
        out.append(self._to_str(self.zone_18_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_18))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_18))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_18))
        out.append(self._to_str(self.zone_19_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_19))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_19))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_19))
        out.append(self._to_str(self.zone_20_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_20))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_20))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_20))
        return ",".join(out)