from collections import OrderedDict

class ZoneEarthtube(object):
    """ Corresponds to IDD object `ZoneEarthtube`
        Earth Tube is specified as a design level which is modified by a Schedule fraction, temperature difference and wind speed:
        Earthtube=Edesign * Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)
    """
    internal_name = "ZoneEarthtube"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneEarthtube`
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