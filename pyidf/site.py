from collections import OrderedDict

class SiteLocation(object):
    """ Corresponds to IDD object `Site:Location`
        Specifies the building's location. Only one location is allowed.
        Weather data file location, if it exists, will override this object.
    """
    internal_name = "Site:Location"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:Location`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Latitude"] = None
        self._data["Longitude"] = None
        self._data["Time Zone"] = None
        self._data["Elevation"] = None

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
            self.latitude = None
        else:
            self.latitude = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.longitude = None
        else:
            self.longitude = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_zone = None
        else:
            self.time_zone = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.elevation = None
        else:
            self.elevation = vals[i]
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
    def latitude(self):
        """Get latitude

        Returns:
            float: the value of `latitude` or None if not set
        """
        return self._data["Latitude"]

    @latitude.setter
    def latitude(self, value=0.0 ):
        """  Corresponds to IDD Field `latitude`
        + is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)

        Args:
            value (float): value for IDD Field `latitude`
                Unit: deg
                Default value: 0.0
                value >= -90.0
                value <= 90.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `latitude`'.format(value))
            if value < -90.0:
                raise ValueError('value need to be greater or equal -90.0 '
                                 'for field `latitude`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `latitude`')

        self._data["Latitude"] = value

    @property
    def longitude(self):
        """Get longitude

        Returns:
            float: the value of `longitude` or None if not set
        """
        return self._data["Longitude"]

    @longitude.setter
    def longitude(self, value=0.0 ):
        """  Corresponds to IDD Field `longitude`
        - is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)

        Args:
            value (float): value for IDD Field `longitude`
                Unit: deg
                Default value: 0.0
                value >= -180.0
                value <= 180.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `longitude`'.format(value))
            if value < -180.0:
                raise ValueError('value need to be greater or equal -180.0 '
                                 'for field `longitude`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `longitude`')

        self._data["Longitude"] = value

    @property
    def time_zone(self):
        """Get time_zone

        Returns:
            float: the value of `time_zone` or None if not set
        """
        return self._data["Time Zone"]

    @time_zone.setter
    def time_zone(self, value=0.0 ):
        """  Corresponds to IDD Field `time_zone`
        basic these limits on the WorldTimeZone Map (2003)
        Time relative to GMT. Decimal hours.

        Args:
            value (float): value for IDD Field `time_zone`
                Unit: hr
                Default value: 0.0
                value >= -12.0
                value <= 14.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `time_zone`'.format(value))
            if value < -12.0:
                raise ValueError('value need to be greater or equal -12.0 '
                                 'for field `time_zone`')
            if value > 14.0:
                raise ValueError('value need to be smaller 14.0 '
                                 'for field `time_zone`')

        self._data["Time Zone"] = value

    @property
    def elevation(self):
        """Get elevation

        Returns:
            float: the value of `elevation` or None if not set
        """
        return self._data["Elevation"]

    @elevation.setter
    def elevation(self, value=0.0 ):
        """  Corresponds to IDD Field `elevation`

        Args:
            value (float): value for IDD Field `elevation`
                Unit: m
                Default value: 0.0
                value >= -300.0
                value < 8900.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `elevation`'.format(value))
            if value < -300.0:
                raise ValueError('value need to be greater or equal -300.0 '
                                 'for field `elevation`')
            if value >= 8900.0:
                raise ValueError('value need to be smaller 8900.0 '
                                 'for field `elevation`')

        self._data["Elevation"] = value

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
        out.append(self._to_str(self.latitude))
        out.append(self._to_str(self.longitude))
        out.append(self._to_str(self.time_zone))
        out.append(self._to_str(self.elevation))
        return ",".join(out)

class SiteWeatherStation(object):
    """ Corresponds to IDD object `Site:WeatherStation`
        This object should only be used for non-standard weather data.  Standard weather data
        such as TMY2, IWEC, and ASHRAE design day data are all measured at the
        default conditions and do not require this object.
    """
    internal_name = "Site:WeatherStation"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:WeatherStation`
        """
        self._data = OrderedDict()
        self._data["Wind Sensor Height Above Ground"] = None
        self._data["Wind Speed Profile Exponent"] = None
        self._data["Wind Speed Profile Boundary Layer Thickness"] = None
        self._data["Air Temperature Sensor Height Above Ground"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.wind_sensor_height_above_ground = None
        else:
            self.wind_sensor_height_above_ground = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed_profile_exponent = None
        else:
            self.wind_speed_profile_exponent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed_profile_boundary_layer_thickness = None
        else:
            self.wind_speed_profile_boundary_layer_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_temperature_sensor_height_above_ground = None
        else:
            self.air_temperature_sensor_height_above_ground = vals[i]
        i += 1

    @property
    def wind_sensor_height_above_ground(self):
        """Get wind_sensor_height_above_ground

        Returns:
            float: the value of `wind_sensor_height_above_ground` or None if not set
        """
        return self._data["Wind Sensor Height Above Ground"]

    @wind_sensor_height_above_ground.setter
    def wind_sensor_height_above_ground(self, value=10.0 ):
        """  Corresponds to IDD Field `wind_sensor_height_above_ground`

        Args:
            value (float): value for IDD Field `wind_sensor_height_above_ground`
                Unit: m
                Default value: 10.0
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
                                 'for field `wind_sensor_height_above_ground`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `wind_sensor_height_above_ground`')

        self._data["Wind Sensor Height Above Ground"] = value

    @property
    def wind_speed_profile_exponent(self):
        """Get wind_speed_profile_exponent

        Returns:
            float: the value of `wind_speed_profile_exponent` or None if not set
        """
        return self._data["Wind Speed Profile Exponent"]

    @wind_speed_profile_exponent.setter
    def wind_speed_profile_exponent(self, value=0.14 ):
        """  Corresponds to IDD Field `wind_speed_profile_exponent`

        Args:
            value (float): value for IDD Field `wind_speed_profile_exponent`
                Default value: 0.14
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
                                 'for field `wind_speed_profile_exponent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_speed_profile_exponent`')

        self._data["Wind Speed Profile Exponent"] = value

    @property
    def wind_speed_profile_boundary_layer_thickness(self):
        """Get wind_speed_profile_boundary_layer_thickness

        Returns:
            float: the value of `wind_speed_profile_boundary_layer_thickness` or None if not set
        """
        return self._data["Wind Speed Profile Boundary Layer Thickness"]

    @wind_speed_profile_boundary_layer_thickness.setter
    def wind_speed_profile_boundary_layer_thickness(self, value=270.0 ):
        """  Corresponds to IDD Field `wind_speed_profile_boundary_layer_thickness`

        Args:
            value (float): value for IDD Field `wind_speed_profile_boundary_layer_thickness`
                Unit: m
                Default value: 270.0
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
                                 'for field `wind_speed_profile_boundary_layer_thickness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_speed_profile_boundary_layer_thickness`')

        self._data["Wind Speed Profile Boundary Layer Thickness"] = value

    @property
    def air_temperature_sensor_height_above_ground(self):
        """Get air_temperature_sensor_height_above_ground

        Returns:
            float: the value of `air_temperature_sensor_height_above_ground` or None if not set
        """
        return self._data["Air Temperature Sensor Height Above Ground"]

    @air_temperature_sensor_height_above_ground.setter
    def air_temperature_sensor_height_above_ground(self, value=1.5 ):
        """  Corresponds to IDD Field `air_temperature_sensor_height_above_ground`

        Args:
            value (float): value for IDD Field `air_temperature_sensor_height_above_ground`
                Unit: m
                Default value: 1.5
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
                                 'for field `air_temperature_sensor_height_above_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `air_temperature_sensor_height_above_ground`')

        self._data["Air Temperature Sensor Height Above Ground"] = value

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
        out.append(self._to_str(self.wind_sensor_height_above_ground))
        out.append(self._to_str(self.wind_speed_profile_exponent))
        out.append(self._to_str(self.wind_speed_profile_boundary_layer_thickness))
        out.append(self._to_str(self.air_temperature_sensor_height_above_ground))
        return ",".join(out)

class SiteHeightVariation(object):
    """ Corresponds to IDD object `Site:HeightVariation`
        This object is used if the user requires advanced control over height-dependent
        variations in wind speed and temperature.  When this object is not present, the default model
        for temperature dependence on height is used, and the wind speed is modeled according
        to the Terrain field of the BUILDING object.
    """
    internal_name = "Site:HeightVariation"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:HeightVariation`
        """
        self._data = OrderedDict()
        self._data["Wind Speed Profile Exponent"] = None
        self._data["Wind Speed Profile Boundary Layer Thickness"] = None
        self._data["Air Temperature Gradient Coefficient"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.wind_speed_profile_exponent = None
        else:
            self.wind_speed_profile_exponent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed_profile_boundary_layer_thickness = None
        else:
            self.wind_speed_profile_boundary_layer_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_temperature_gradient_coefficient = None
        else:
            self.air_temperature_gradient_coefficient = vals[i]
        i += 1

    @property
    def wind_speed_profile_exponent(self):
        """Get wind_speed_profile_exponent

        Returns:
            float: the value of `wind_speed_profile_exponent` or None if not set
        """
        return self._data["Wind Speed Profile Exponent"]

    @wind_speed_profile_exponent.setter
    def wind_speed_profile_exponent(self, value=0.22 ):
        """  Corresponds to IDD Field `wind_speed_profile_exponent`
        Set to zero for no wind speed dependence on height.

        Args:
            value (float): value for IDD Field `wind_speed_profile_exponent`
                Default value: 0.22
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
                                 'for field `wind_speed_profile_exponent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_speed_profile_exponent`')

        self._data["Wind Speed Profile Exponent"] = value

    @property
    def wind_speed_profile_boundary_layer_thickness(self):
        """Get wind_speed_profile_boundary_layer_thickness

        Returns:
            float: the value of `wind_speed_profile_boundary_layer_thickness` or None if not set
        """
        return self._data["Wind Speed Profile Boundary Layer Thickness"]

    @wind_speed_profile_boundary_layer_thickness.setter
    def wind_speed_profile_boundary_layer_thickness(self, value=370.0 ):
        """  Corresponds to IDD Field `wind_speed_profile_boundary_layer_thickness`

        Args:
            value (float): value for IDD Field `wind_speed_profile_boundary_layer_thickness`
                Unit: m
                Default value: 370.0
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
                                 'for field `wind_speed_profile_boundary_layer_thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `wind_speed_profile_boundary_layer_thickness`')

        self._data["Wind Speed Profile Boundary Layer Thickness"] = value

    @property
    def air_temperature_gradient_coefficient(self):
        """Get air_temperature_gradient_coefficient

        Returns:
            float: the value of `air_temperature_gradient_coefficient` or None if not set
        """
        return self._data["Air Temperature Gradient Coefficient"]

    @air_temperature_gradient_coefficient.setter
    def air_temperature_gradient_coefficient(self, value=0.0065 ):
        """  Corresponds to IDD Field `air_temperature_gradient_coefficient`
        Set to zero for no air temperature dependence on height.

        Args:
            value (float): value for IDD Field `air_temperature_gradient_coefficient`
                Unit: K/m
                Default value: 0.0065
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
                                 'for field `air_temperature_gradient_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `air_temperature_gradient_coefficient`')

        self._data["Air Temperature Gradient Coefficient"] = value

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
        out.append(self._to_str(self.wind_speed_profile_exponent))
        out.append(self._to_str(self.wind_speed_profile_boundary_layer_thickness))
        out.append(self._to_str(self.air_temperature_gradient_coefficient))
        return ",".join(out)

class SiteGroundTemperatureBuildingSurface(object):
    """ Corresponds to IDD object `Site:GroundTemperature:BuildingSurface`
        These temperatures are specifically for those surfaces that have the outside environment
        of "Ground".  Documentation about what values these should be is located in the
        Auxiliary programs document (Ground Heat Transfer) as well as the InputOutput Reference.
        CAUTION - Do not use the "undisturbed" ground temperatures from the weather data.
        These values are too extreme for the soil under a conditioned building.
        For best results, use the Slab or Basement program to calculate custom monthly
        average ground temperatures (see Auxiliary Programs).  For typical commercial
        buildings in the USA, a reasonable default value is 2C less than the average indoor space temperature.
    """
    internal_name = "Site:GroundTemperature:BuildingSurface"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:GroundTemperature:BuildingSurface`
        """
        self._data = OrderedDict()
        self._data["January Ground Temperature"] = None
        self._data["February Ground Temperature"] = None
        self._data["March Ground Temperature"] = None
        self._data["April Ground Temperature"] = None
        self._data["May Ground Temperature"] = None
        self._data["June Ground Temperature"] = None
        self._data["July Ground Temperature"] = None
        self._data["August Ground Temperature"] = None
        self._data["September Ground Temperature"] = None
        self._data["October Ground Temperature"] = None
        self._data["November Ground Temperature"] = None
        self._data["December Ground Temperature"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.january_ground_temperature = None
        else:
            self.january_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.february_ground_temperature = None
        else:
            self.february_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.march_ground_temperature = None
        else:
            self.march_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.april_ground_temperature = None
        else:
            self.april_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.may_ground_temperature = None
        else:
            self.may_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.june_ground_temperature = None
        else:
            self.june_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.july_ground_temperature = None
        else:
            self.july_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.august_ground_temperature = None
        else:
            self.august_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.september_ground_temperature = None
        else:
            self.september_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.october_ground_temperature = None
        else:
            self.october_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.november_ground_temperature = None
        else:
            self.november_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.december_ground_temperature = None
        else:
            self.december_ground_temperature = vals[i]
        i += 1

    @property
    def january_ground_temperature(self):
        """Get january_ground_temperature

        Returns:
            float: the value of `january_ground_temperature` or None if not set
        """
        return self._data["January Ground Temperature"]

    @january_ground_temperature.setter
    def january_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `january_ground_temperature`

        Args:
            value (float): value for IDD Field `january_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `january_ground_temperature`'.format(value))

        self._data["January Ground Temperature"] = value

    @property
    def february_ground_temperature(self):
        """Get february_ground_temperature

        Returns:
            float: the value of `february_ground_temperature` or None if not set
        """
        return self._data["February Ground Temperature"]

    @february_ground_temperature.setter
    def february_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `february_ground_temperature`

        Args:
            value (float): value for IDD Field `february_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `february_ground_temperature`'.format(value))

        self._data["February Ground Temperature"] = value

    @property
    def march_ground_temperature(self):
        """Get march_ground_temperature

        Returns:
            float: the value of `march_ground_temperature` or None if not set
        """
        return self._data["March Ground Temperature"]

    @march_ground_temperature.setter
    def march_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `march_ground_temperature`

        Args:
            value (float): value for IDD Field `march_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `march_ground_temperature`'.format(value))

        self._data["March Ground Temperature"] = value

    @property
    def april_ground_temperature(self):
        """Get april_ground_temperature

        Returns:
            float: the value of `april_ground_temperature` or None if not set
        """
        return self._data["April Ground Temperature"]

    @april_ground_temperature.setter
    def april_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `april_ground_temperature`

        Args:
            value (float): value for IDD Field `april_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `april_ground_temperature`'.format(value))

        self._data["April Ground Temperature"] = value

    @property
    def may_ground_temperature(self):
        """Get may_ground_temperature

        Returns:
            float: the value of `may_ground_temperature` or None if not set
        """
        return self._data["May Ground Temperature"]

    @may_ground_temperature.setter
    def may_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `may_ground_temperature`

        Args:
            value (float): value for IDD Field `may_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `may_ground_temperature`'.format(value))

        self._data["May Ground Temperature"] = value

    @property
    def june_ground_temperature(self):
        """Get june_ground_temperature

        Returns:
            float: the value of `june_ground_temperature` or None if not set
        """
        return self._data["June Ground Temperature"]

    @june_ground_temperature.setter
    def june_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `june_ground_temperature`

        Args:
            value (float): value for IDD Field `june_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `june_ground_temperature`'.format(value))

        self._data["June Ground Temperature"] = value

    @property
    def july_ground_temperature(self):
        """Get july_ground_temperature

        Returns:
            float: the value of `july_ground_temperature` or None if not set
        """
        return self._data["July Ground Temperature"]

    @july_ground_temperature.setter
    def july_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `july_ground_temperature`

        Args:
            value (float): value for IDD Field `july_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `july_ground_temperature`'.format(value))

        self._data["July Ground Temperature"] = value

    @property
    def august_ground_temperature(self):
        """Get august_ground_temperature

        Returns:
            float: the value of `august_ground_temperature` or None if not set
        """
        return self._data["August Ground Temperature"]

    @august_ground_temperature.setter
    def august_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `august_ground_temperature`

        Args:
            value (float): value for IDD Field `august_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `august_ground_temperature`'.format(value))

        self._data["August Ground Temperature"] = value

    @property
    def september_ground_temperature(self):
        """Get september_ground_temperature

        Returns:
            float: the value of `september_ground_temperature` or None if not set
        """
        return self._data["September Ground Temperature"]

    @september_ground_temperature.setter
    def september_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `september_ground_temperature`

        Args:
            value (float): value for IDD Field `september_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `september_ground_temperature`'.format(value))

        self._data["September Ground Temperature"] = value

    @property
    def october_ground_temperature(self):
        """Get october_ground_temperature

        Returns:
            float: the value of `october_ground_temperature` or None if not set
        """
        return self._data["October Ground Temperature"]

    @october_ground_temperature.setter
    def october_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `october_ground_temperature`

        Args:
            value (float): value for IDD Field `october_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `october_ground_temperature`'.format(value))

        self._data["October Ground Temperature"] = value

    @property
    def november_ground_temperature(self):
        """Get november_ground_temperature

        Returns:
            float: the value of `november_ground_temperature` or None if not set
        """
        return self._data["November Ground Temperature"]

    @november_ground_temperature.setter
    def november_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `november_ground_temperature`

        Args:
            value (float): value for IDD Field `november_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `november_ground_temperature`'.format(value))

        self._data["November Ground Temperature"] = value

    @property
    def december_ground_temperature(self):
        """Get december_ground_temperature

        Returns:
            float: the value of `december_ground_temperature` or None if not set
        """
        return self._data["December Ground Temperature"]

    @december_ground_temperature.setter
    def december_ground_temperature(self, value=18.0 ):
        """  Corresponds to IDD Field `december_ground_temperature`

        Args:
            value (float): value for IDD Field `december_ground_temperature`
                Unit: C
                Default value: 18.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `december_ground_temperature`'.format(value))

        self._data["December Ground Temperature"] = value

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
        out.append(self._to_str(self.january_ground_temperature))
        out.append(self._to_str(self.february_ground_temperature))
        out.append(self._to_str(self.march_ground_temperature))
        out.append(self._to_str(self.april_ground_temperature))
        out.append(self._to_str(self.may_ground_temperature))
        out.append(self._to_str(self.june_ground_temperature))
        out.append(self._to_str(self.july_ground_temperature))
        out.append(self._to_str(self.august_ground_temperature))
        out.append(self._to_str(self.september_ground_temperature))
        out.append(self._to_str(self.october_ground_temperature))
        out.append(self._to_str(self.november_ground_temperature))
        out.append(self._to_str(self.december_ground_temperature))
        return ",".join(out)

class SiteGroundTemperatureFcfactorMethod(object):
    """ Corresponds to IDD object `Site:GroundTemperature:FCfactorMethod`
        These temperatures are specifically for underground walls and ground floors
        defined with the C-factor and F-factor methods, and should be close to the
        monthly average outdoor air temperature delayed by 3 months for the location.
    """
    internal_name = "Site:GroundTemperature:FCfactorMethod"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:GroundTemperature:FCfactorMethod`
        """
        self._data = OrderedDict()
        self._data["January Ground Temperature"] = None
        self._data["February Ground Temperature"] = None
        self._data["March Ground Temperature"] = None
        self._data["April Ground Temperature"] = None
        self._data["May Ground Temperature"] = None
        self._data["June Ground Temperature"] = None
        self._data["July Ground Temperature"] = None
        self._data["August Ground Temperature"] = None
        self._data["September Ground Temperature"] = None
        self._data["October Ground Temperature"] = None
        self._data["November Ground Temperature"] = None
        self._data["December Ground Temperature"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.january_ground_temperature = None
        else:
            self.january_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.february_ground_temperature = None
        else:
            self.february_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.march_ground_temperature = None
        else:
            self.march_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.april_ground_temperature = None
        else:
            self.april_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.may_ground_temperature = None
        else:
            self.may_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.june_ground_temperature = None
        else:
            self.june_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.july_ground_temperature = None
        else:
            self.july_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.august_ground_temperature = None
        else:
            self.august_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.september_ground_temperature = None
        else:
            self.september_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.october_ground_temperature = None
        else:
            self.october_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.november_ground_temperature = None
        else:
            self.november_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.december_ground_temperature = None
        else:
            self.december_ground_temperature = vals[i]
        i += 1

    @property
    def january_ground_temperature(self):
        """Get january_ground_temperature

        Returns:
            float: the value of `january_ground_temperature` or None if not set
        """
        return self._data["January Ground Temperature"]

    @january_ground_temperature.setter
    def january_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `january_ground_temperature`

        Args:
            value (float): value for IDD Field `january_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `january_ground_temperature`'.format(value))

        self._data["January Ground Temperature"] = value

    @property
    def february_ground_temperature(self):
        """Get february_ground_temperature

        Returns:
            float: the value of `february_ground_temperature` or None if not set
        """
        return self._data["February Ground Temperature"]

    @february_ground_temperature.setter
    def february_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `february_ground_temperature`

        Args:
            value (float): value for IDD Field `february_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `february_ground_temperature`'.format(value))

        self._data["February Ground Temperature"] = value

    @property
    def march_ground_temperature(self):
        """Get march_ground_temperature

        Returns:
            float: the value of `march_ground_temperature` or None if not set
        """
        return self._data["March Ground Temperature"]

    @march_ground_temperature.setter
    def march_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `march_ground_temperature`

        Args:
            value (float): value for IDD Field `march_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `march_ground_temperature`'.format(value))

        self._data["March Ground Temperature"] = value

    @property
    def april_ground_temperature(self):
        """Get april_ground_temperature

        Returns:
            float: the value of `april_ground_temperature` or None if not set
        """
        return self._data["April Ground Temperature"]

    @april_ground_temperature.setter
    def april_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `april_ground_temperature`

        Args:
            value (float): value for IDD Field `april_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `april_ground_temperature`'.format(value))

        self._data["April Ground Temperature"] = value

    @property
    def may_ground_temperature(self):
        """Get may_ground_temperature

        Returns:
            float: the value of `may_ground_temperature` or None if not set
        """
        return self._data["May Ground Temperature"]

    @may_ground_temperature.setter
    def may_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `may_ground_temperature`

        Args:
            value (float): value for IDD Field `may_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `may_ground_temperature`'.format(value))

        self._data["May Ground Temperature"] = value

    @property
    def june_ground_temperature(self):
        """Get june_ground_temperature

        Returns:
            float: the value of `june_ground_temperature` or None if not set
        """
        return self._data["June Ground Temperature"]

    @june_ground_temperature.setter
    def june_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `june_ground_temperature`

        Args:
            value (float): value for IDD Field `june_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `june_ground_temperature`'.format(value))

        self._data["June Ground Temperature"] = value

    @property
    def july_ground_temperature(self):
        """Get july_ground_temperature

        Returns:
            float: the value of `july_ground_temperature` or None if not set
        """
        return self._data["July Ground Temperature"]

    @july_ground_temperature.setter
    def july_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `july_ground_temperature`

        Args:
            value (float): value for IDD Field `july_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `july_ground_temperature`'.format(value))

        self._data["July Ground Temperature"] = value

    @property
    def august_ground_temperature(self):
        """Get august_ground_temperature

        Returns:
            float: the value of `august_ground_temperature` or None if not set
        """
        return self._data["August Ground Temperature"]

    @august_ground_temperature.setter
    def august_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `august_ground_temperature`

        Args:
            value (float): value for IDD Field `august_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `august_ground_temperature`'.format(value))

        self._data["August Ground Temperature"] = value

    @property
    def september_ground_temperature(self):
        """Get september_ground_temperature

        Returns:
            float: the value of `september_ground_temperature` or None if not set
        """
        return self._data["September Ground Temperature"]

    @september_ground_temperature.setter
    def september_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `september_ground_temperature`

        Args:
            value (float): value for IDD Field `september_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `september_ground_temperature`'.format(value))

        self._data["September Ground Temperature"] = value

    @property
    def october_ground_temperature(self):
        """Get october_ground_temperature

        Returns:
            float: the value of `october_ground_temperature` or None if not set
        """
        return self._data["October Ground Temperature"]

    @october_ground_temperature.setter
    def october_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `october_ground_temperature`

        Args:
            value (float): value for IDD Field `october_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `october_ground_temperature`'.format(value))

        self._data["October Ground Temperature"] = value

    @property
    def november_ground_temperature(self):
        """Get november_ground_temperature

        Returns:
            float: the value of `november_ground_temperature` or None if not set
        """
        return self._data["November Ground Temperature"]

    @november_ground_temperature.setter
    def november_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `november_ground_temperature`

        Args:
            value (float): value for IDD Field `november_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `november_ground_temperature`'.format(value))

        self._data["November Ground Temperature"] = value

    @property
    def december_ground_temperature(self):
        """Get december_ground_temperature

        Returns:
            float: the value of `december_ground_temperature` or None if not set
        """
        return self._data["December Ground Temperature"]

    @december_ground_temperature.setter
    def december_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `december_ground_temperature`

        Args:
            value (float): value for IDD Field `december_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `december_ground_temperature`'.format(value))

        self._data["December Ground Temperature"] = value

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
        out.append(self._to_str(self.january_ground_temperature))
        out.append(self._to_str(self.february_ground_temperature))
        out.append(self._to_str(self.march_ground_temperature))
        out.append(self._to_str(self.april_ground_temperature))
        out.append(self._to_str(self.may_ground_temperature))
        out.append(self._to_str(self.june_ground_temperature))
        out.append(self._to_str(self.july_ground_temperature))
        out.append(self._to_str(self.august_ground_temperature))
        out.append(self._to_str(self.september_ground_temperature))
        out.append(self._to_str(self.october_ground_temperature))
        out.append(self._to_str(self.november_ground_temperature))
        out.append(self._to_str(self.december_ground_temperature))
        return ",".join(out)

class SiteGroundTemperatureShallow(object):
    """ Corresponds to IDD object `Site:GroundTemperature:Shallow`
        These temperatures are specifically for the Surface Ground Heat Exchanger and
        should probably be close to the average outdoor air temperature for the location.
        They are not used in other models.
    """
    internal_name = "Site:GroundTemperature:Shallow"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:GroundTemperature:Shallow`
        """
        self._data = OrderedDict()
        self._data["January Surface Ground Temperature"] = None
        self._data["February Surface Ground Temperature"] = None
        self._data["March Surface Ground Temperature"] = None
        self._data["April Surface Ground Temperature"] = None
        self._data["May Surface Ground Temperature"] = None
        self._data["June Surface Ground Temperature"] = None
        self._data["July Surface Ground Temperature"] = None
        self._data["August Surface Ground Temperature"] = None
        self._data["September Surface Ground Temperature"] = None
        self._data["October Surface Ground Temperature"] = None
        self._data["November Surface Ground Temperature"] = None
        self._data["December Surface Ground Temperature"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.january_surface_ground_temperature = None
        else:
            self.january_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.february_surface_ground_temperature = None
        else:
            self.february_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.march_surface_ground_temperature = None
        else:
            self.march_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.april_surface_ground_temperature = None
        else:
            self.april_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.may_surface_ground_temperature = None
        else:
            self.may_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.june_surface_ground_temperature = None
        else:
            self.june_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.july_surface_ground_temperature = None
        else:
            self.july_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.august_surface_ground_temperature = None
        else:
            self.august_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.september_surface_ground_temperature = None
        else:
            self.september_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.october_surface_ground_temperature = None
        else:
            self.october_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.november_surface_ground_temperature = None
        else:
            self.november_surface_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.december_surface_ground_temperature = None
        else:
            self.december_surface_ground_temperature = vals[i]
        i += 1

    @property
    def january_surface_ground_temperature(self):
        """Get january_surface_ground_temperature

        Returns:
            float: the value of `january_surface_ground_temperature` or None if not set
        """
        return self._data["January Surface Ground Temperature"]

    @january_surface_ground_temperature.setter
    def january_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `january_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `january_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `january_surface_ground_temperature`'.format(value))

        self._data["January Surface Ground Temperature"] = value

    @property
    def february_surface_ground_temperature(self):
        """Get february_surface_ground_temperature

        Returns:
            float: the value of `february_surface_ground_temperature` or None if not set
        """
        return self._data["February Surface Ground Temperature"]

    @february_surface_ground_temperature.setter
    def february_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `february_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `february_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `february_surface_ground_temperature`'.format(value))

        self._data["February Surface Ground Temperature"] = value

    @property
    def march_surface_ground_temperature(self):
        """Get march_surface_ground_temperature

        Returns:
            float: the value of `march_surface_ground_temperature` or None if not set
        """
        return self._data["March Surface Ground Temperature"]

    @march_surface_ground_temperature.setter
    def march_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `march_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `march_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `march_surface_ground_temperature`'.format(value))

        self._data["March Surface Ground Temperature"] = value

    @property
    def april_surface_ground_temperature(self):
        """Get april_surface_ground_temperature

        Returns:
            float: the value of `april_surface_ground_temperature` or None if not set
        """
        return self._data["April Surface Ground Temperature"]

    @april_surface_ground_temperature.setter
    def april_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `april_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `april_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `april_surface_ground_temperature`'.format(value))

        self._data["April Surface Ground Temperature"] = value

    @property
    def may_surface_ground_temperature(self):
        """Get may_surface_ground_temperature

        Returns:
            float: the value of `may_surface_ground_temperature` or None if not set
        """
        return self._data["May Surface Ground Temperature"]

    @may_surface_ground_temperature.setter
    def may_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `may_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `may_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `may_surface_ground_temperature`'.format(value))

        self._data["May Surface Ground Temperature"] = value

    @property
    def june_surface_ground_temperature(self):
        """Get june_surface_ground_temperature

        Returns:
            float: the value of `june_surface_ground_temperature` or None if not set
        """
        return self._data["June Surface Ground Temperature"]

    @june_surface_ground_temperature.setter
    def june_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `june_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `june_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `june_surface_ground_temperature`'.format(value))

        self._data["June Surface Ground Temperature"] = value

    @property
    def july_surface_ground_temperature(self):
        """Get july_surface_ground_temperature

        Returns:
            float: the value of `july_surface_ground_temperature` or None if not set
        """
        return self._data["July Surface Ground Temperature"]

    @july_surface_ground_temperature.setter
    def july_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `july_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `july_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `july_surface_ground_temperature`'.format(value))

        self._data["July Surface Ground Temperature"] = value

    @property
    def august_surface_ground_temperature(self):
        """Get august_surface_ground_temperature

        Returns:
            float: the value of `august_surface_ground_temperature` or None if not set
        """
        return self._data["August Surface Ground Temperature"]

    @august_surface_ground_temperature.setter
    def august_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `august_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `august_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `august_surface_ground_temperature`'.format(value))

        self._data["August Surface Ground Temperature"] = value

    @property
    def september_surface_ground_temperature(self):
        """Get september_surface_ground_temperature

        Returns:
            float: the value of `september_surface_ground_temperature` or None if not set
        """
        return self._data["September Surface Ground Temperature"]

    @september_surface_ground_temperature.setter
    def september_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `september_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `september_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `september_surface_ground_temperature`'.format(value))

        self._data["September Surface Ground Temperature"] = value

    @property
    def october_surface_ground_temperature(self):
        """Get october_surface_ground_temperature

        Returns:
            float: the value of `october_surface_ground_temperature` or None if not set
        """
        return self._data["October Surface Ground Temperature"]

    @october_surface_ground_temperature.setter
    def october_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `october_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `october_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `october_surface_ground_temperature`'.format(value))

        self._data["October Surface Ground Temperature"] = value

    @property
    def november_surface_ground_temperature(self):
        """Get november_surface_ground_temperature

        Returns:
            float: the value of `november_surface_ground_temperature` or None if not set
        """
        return self._data["November Surface Ground Temperature"]

    @november_surface_ground_temperature.setter
    def november_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `november_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `november_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `november_surface_ground_temperature`'.format(value))

        self._data["November Surface Ground Temperature"] = value

    @property
    def december_surface_ground_temperature(self):
        """Get december_surface_ground_temperature

        Returns:
            float: the value of `december_surface_ground_temperature` or None if not set
        """
        return self._data["December Surface Ground Temperature"]

    @december_surface_ground_temperature.setter
    def december_surface_ground_temperature(self, value=13.0 ):
        """  Corresponds to IDD Field `december_surface_ground_temperature`

        Args:
            value (float): value for IDD Field `december_surface_ground_temperature`
                Unit: C
                Default value: 13.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `december_surface_ground_temperature`'.format(value))

        self._data["December Surface Ground Temperature"] = value

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
        out.append(self._to_str(self.january_surface_ground_temperature))
        out.append(self._to_str(self.february_surface_ground_temperature))
        out.append(self._to_str(self.march_surface_ground_temperature))
        out.append(self._to_str(self.april_surface_ground_temperature))
        out.append(self._to_str(self.may_surface_ground_temperature))
        out.append(self._to_str(self.june_surface_ground_temperature))
        out.append(self._to_str(self.july_surface_ground_temperature))
        out.append(self._to_str(self.august_surface_ground_temperature))
        out.append(self._to_str(self.september_surface_ground_temperature))
        out.append(self._to_str(self.october_surface_ground_temperature))
        out.append(self._to_str(self.november_surface_ground_temperature))
        out.append(self._to_str(self.december_surface_ground_temperature))
        return ",".join(out)

class SiteGroundTemperatureDeep(object):
    """ Corresponds to IDD object `Site:GroundTemperature:Deep`
        These temperatures are specifically for the ground heat exchangers that would use
        "deep" (3-4 m depth) ground temperatures for their heat source.
        They are not used in other models.
    """
    internal_name = "Site:GroundTemperature:Deep"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:GroundTemperature:Deep`
        """
        self._data = OrderedDict()
        self._data["January Deep Ground Temperature"] = None
        self._data["February Deep Ground Temperature"] = None
        self._data["March Deep Ground Temperature"] = None
        self._data["April Deep Ground Temperature"] = None
        self._data["May Deep Ground Temperature"] = None
        self._data["June Deep Ground Temperature"] = None
        self._data["July Deep Ground Temperature"] = None
        self._data["August Deep Ground Temperature"] = None
        self._data["September Deep Ground Temperature"] = None
        self._data["October Deep Ground Temperature"] = None
        self._data["November Deep Ground Temperature"] = None
        self._data["December Deep Ground Temperature"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.january_deep_ground_temperature = None
        else:
            self.january_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.february_deep_ground_temperature = None
        else:
            self.february_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.march_deep_ground_temperature = None
        else:
            self.march_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.april_deep_ground_temperature = None
        else:
            self.april_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.may_deep_ground_temperature = None
        else:
            self.may_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.june_deep_ground_temperature = None
        else:
            self.june_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.july_deep_ground_temperature = None
        else:
            self.july_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.august_deep_ground_temperature = None
        else:
            self.august_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.september_deep_ground_temperature = None
        else:
            self.september_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.october_deep_ground_temperature = None
        else:
            self.october_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.november_deep_ground_temperature = None
        else:
            self.november_deep_ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.december_deep_ground_temperature = None
        else:
            self.december_deep_ground_temperature = vals[i]
        i += 1

    @property
    def january_deep_ground_temperature(self):
        """Get january_deep_ground_temperature

        Returns:
            float: the value of `january_deep_ground_temperature` or None if not set
        """
        return self._data["January Deep Ground Temperature"]

    @january_deep_ground_temperature.setter
    def january_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `january_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `january_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `january_deep_ground_temperature`'.format(value))

        self._data["January Deep Ground Temperature"] = value

    @property
    def february_deep_ground_temperature(self):
        """Get february_deep_ground_temperature

        Returns:
            float: the value of `february_deep_ground_temperature` or None if not set
        """
        return self._data["February Deep Ground Temperature"]

    @february_deep_ground_temperature.setter
    def february_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `february_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `february_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `february_deep_ground_temperature`'.format(value))

        self._data["February Deep Ground Temperature"] = value

    @property
    def march_deep_ground_temperature(self):
        """Get march_deep_ground_temperature

        Returns:
            float: the value of `march_deep_ground_temperature` or None if not set
        """
        return self._data["March Deep Ground Temperature"]

    @march_deep_ground_temperature.setter
    def march_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `march_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `march_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `march_deep_ground_temperature`'.format(value))

        self._data["March Deep Ground Temperature"] = value

    @property
    def april_deep_ground_temperature(self):
        """Get april_deep_ground_temperature

        Returns:
            float: the value of `april_deep_ground_temperature` or None if not set
        """
        return self._data["April Deep Ground Temperature"]

    @april_deep_ground_temperature.setter
    def april_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `april_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `april_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `april_deep_ground_temperature`'.format(value))

        self._data["April Deep Ground Temperature"] = value

    @property
    def may_deep_ground_temperature(self):
        """Get may_deep_ground_temperature

        Returns:
            float: the value of `may_deep_ground_temperature` or None if not set
        """
        return self._data["May Deep Ground Temperature"]

    @may_deep_ground_temperature.setter
    def may_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `may_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `may_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `may_deep_ground_temperature`'.format(value))

        self._data["May Deep Ground Temperature"] = value

    @property
    def june_deep_ground_temperature(self):
        """Get june_deep_ground_temperature

        Returns:
            float: the value of `june_deep_ground_temperature` or None if not set
        """
        return self._data["June Deep Ground Temperature"]

    @june_deep_ground_temperature.setter
    def june_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `june_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `june_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `june_deep_ground_temperature`'.format(value))

        self._data["June Deep Ground Temperature"] = value

    @property
    def july_deep_ground_temperature(self):
        """Get july_deep_ground_temperature

        Returns:
            float: the value of `july_deep_ground_temperature` or None if not set
        """
        return self._data["July Deep Ground Temperature"]

    @july_deep_ground_temperature.setter
    def july_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `july_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `july_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `july_deep_ground_temperature`'.format(value))

        self._data["July Deep Ground Temperature"] = value

    @property
    def august_deep_ground_temperature(self):
        """Get august_deep_ground_temperature

        Returns:
            float: the value of `august_deep_ground_temperature` or None if not set
        """
        return self._data["August Deep Ground Temperature"]

    @august_deep_ground_temperature.setter
    def august_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `august_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `august_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `august_deep_ground_temperature`'.format(value))

        self._data["August Deep Ground Temperature"] = value

    @property
    def september_deep_ground_temperature(self):
        """Get september_deep_ground_temperature

        Returns:
            float: the value of `september_deep_ground_temperature` or None if not set
        """
        return self._data["September Deep Ground Temperature"]

    @september_deep_ground_temperature.setter
    def september_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `september_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `september_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `september_deep_ground_temperature`'.format(value))

        self._data["September Deep Ground Temperature"] = value

    @property
    def october_deep_ground_temperature(self):
        """Get october_deep_ground_temperature

        Returns:
            float: the value of `october_deep_ground_temperature` or None if not set
        """
        return self._data["October Deep Ground Temperature"]

    @october_deep_ground_temperature.setter
    def october_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `october_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `october_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `october_deep_ground_temperature`'.format(value))

        self._data["October Deep Ground Temperature"] = value

    @property
    def november_deep_ground_temperature(self):
        """Get november_deep_ground_temperature

        Returns:
            float: the value of `november_deep_ground_temperature` or None if not set
        """
        return self._data["November Deep Ground Temperature"]

    @november_deep_ground_temperature.setter
    def november_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `november_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `november_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `november_deep_ground_temperature`'.format(value))

        self._data["November Deep Ground Temperature"] = value

    @property
    def december_deep_ground_temperature(self):
        """Get december_deep_ground_temperature

        Returns:
            float: the value of `december_deep_ground_temperature` or None if not set
        """
        return self._data["December Deep Ground Temperature"]

    @december_deep_ground_temperature.setter
    def december_deep_ground_temperature(self, value=16.0 ):
        """  Corresponds to IDD Field `december_deep_ground_temperature`

        Args:
            value (float): value for IDD Field `december_deep_ground_temperature`
                Unit: C
                Default value: 16.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `december_deep_ground_temperature`'.format(value))

        self._data["December Deep Ground Temperature"] = value

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
        out.append(self._to_str(self.january_deep_ground_temperature))
        out.append(self._to_str(self.february_deep_ground_temperature))
        out.append(self._to_str(self.march_deep_ground_temperature))
        out.append(self._to_str(self.april_deep_ground_temperature))
        out.append(self._to_str(self.may_deep_ground_temperature))
        out.append(self._to_str(self.june_deep_ground_temperature))
        out.append(self._to_str(self.july_deep_ground_temperature))
        out.append(self._to_str(self.august_deep_ground_temperature))
        out.append(self._to_str(self.september_deep_ground_temperature))
        out.append(self._to_str(self.october_deep_ground_temperature))
        out.append(self._to_str(self.november_deep_ground_temperature))
        out.append(self._to_str(self.december_deep_ground_temperature))
        return ",".join(out)

class SiteGroundDomain(object):
    """ Corresponds to IDD object `Site:GroundDomain`
        Ground coupled slab model for on-grade and
        in-grade cases with or without insulation.
    """
    internal_name = "Site:GroundDomain"
    field_count = 24

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:GroundDomain`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Ground Domain Depth"] = None
        self._data["Aspect Ratio"] = None
        self._data["Perimeter Offset"] = None
        self._data["Soil Thermal Conductivity"] = None
        self._data["Soil Density"] = None
        self._data["Soil Specific Heat"] = None
        self._data["Soil Moisture Content Volume Fraction"] = None
        self._data["Soil Moisture Content Volume Fraction at Saturation"] = None
        self._data["Kusuda-Achenbach Average Surface Temperature"] = None
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = None
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = None
        self._data["Evapotranspiration Ground Cover Parameter"] = None
        self._data["Slab Boundary Condition Model Name"] = None
        self._data["Slab Location"] = None
        self._data["Slab Material Name"] = None
        self._data["Horizontal Insulation"] = None
        self._data["Horizontal Insulation Material Name"] = None
        self._data["Horizontal Insulation Extents"] = None
        self._data["Perimeter Insulation Width"] = None
        self._data["Vertical Insulation"] = None
        self._data["Vertical Insulation Material Name"] = None
        self._data["Vertical Insulation Depth"] = None
        self._data["Simulation Timestep"] = None

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
            self.ground_domain_depth = None
        else:
            self.ground_domain_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.aspect_ratio = None
        else:
            self.aspect_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.perimeter_offset = None
        else:
            self.perimeter_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_thermal_conductivity = None
        else:
            self.soil_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_density = None
        else:
            self.soil_density = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_specific_heat = None
        else:
            self.soil_specific_heat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction = None
        else:
            self.soil_moisture_content_volume_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction_at_saturation = None
        else:
            self.soil_moisture_content_volume_fraction_at_saturation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_surface_temperature = None
        else:
            self.kusudaachenbach_average_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = None
        else:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = None
        else:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evapotranspiration_ground_cover_parameter = None
        else:
            self.evapotranspiration_ground_cover_parameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slab_boundary_condition_model_name = None
        else:
            self.slab_boundary_condition_model_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slab_location = None
        else:
            self.slab_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slab_material_name = None
        else:
            self.slab_material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.horizontal_insulation = None
        else:
            self.horizontal_insulation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.horizontal_insulation_material_name = None
        else:
            self.horizontal_insulation_material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.horizontal_insulation_extents = None
        else:
            self.horizontal_insulation_extents = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.perimeter_insulation_width = None
        else:
            self.perimeter_insulation_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertical_insulation = None
        else:
            self.vertical_insulation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertical_insulation_material_name = None
        else:
            self.vertical_insulation_material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertical_insulation_depth = None
        else:
            self.vertical_insulation_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simulation_timestep = None
        else:
            self.simulation_timestep = vals[i]
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
    def ground_domain_depth(self):
        """Get ground_domain_depth

        Returns:
            float: the value of `ground_domain_depth` or None if not set
        """
        return self._data["Ground Domain Depth"]

    @ground_domain_depth.setter
    def ground_domain_depth(self, value=None):
        """  Corresponds to IDD Field `ground_domain_depth`

        Args:
            value (float): value for IDD Field `ground_domain_depth`
                Unit: m
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
                                 'for field `ground_domain_depth`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_domain_depth`')

        self._data["Ground Domain Depth"] = value

    @property
    def aspect_ratio(self):
        """Get aspect_ratio

        Returns:
            float: the value of `aspect_ratio` or None if not set
        """
        return self._data["Aspect Ratio"]

    @aspect_ratio.setter
    def aspect_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `aspect_ratio`

        Args:
            value (float): value for IDD Field `aspect_ratio`
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
                                 'for field `aspect_ratio`'.format(value))

        self._data["Aspect Ratio"] = value

    @property
    def perimeter_offset(self):
        """Get perimeter_offset

        Returns:
            float: the value of `perimeter_offset` or None if not set
        """
        return self._data["Perimeter Offset"]

    @perimeter_offset.setter
    def perimeter_offset(self, value=None):
        """  Corresponds to IDD Field `perimeter_offset`

        Args:
            value (float): value for IDD Field `perimeter_offset`
                Unit: m
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
                                 'for field `perimeter_offset`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `perimeter_offset`')

        self._data["Perimeter Offset"] = value

    @property
    def soil_thermal_conductivity(self):
        """Get soil_thermal_conductivity

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set
        """
        return self._data["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `soil_thermal_conductivity`

        Args:
            value (float): value for IDD Field `soil_thermal_conductivity`
                Unit: W/m-K
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
                                 'for field `soil_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_thermal_conductivity`')

        self._data["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """Get soil_density

        Returns:
            float: the value of `soil_density` or None if not set
        """
        return self._data["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=None):
        """  Corresponds to IDD Field `soil_density`

        Args:
            value (float): value for IDD Field `soil_density`
                Unit: kg/m3
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
                                 'for field `soil_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_density`')

        self._data["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """Get soil_specific_heat

        Returns:
            float: the value of `soil_specific_heat` or None if not set
        """
        return self._data["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=None):
        """  Corresponds to IDD Field `soil_specific_heat`

        Args:
            value (float): value for IDD Field `soil_specific_heat`
                Unit: J/kg-K
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
                                 'for field `soil_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_specific_heat`')

        self._data["Soil Specific Heat"] = value

    @property
    def soil_moisture_content_volume_fraction(self):
        """Get soil_moisture_content_volume_fraction

        Returns:
            float: the value of `soil_moisture_content_volume_fraction` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction"]

    @soil_moisture_content_volume_fraction.setter
    def soil_moisture_content_volume_fraction(self, value=30.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_volume_fraction`

        Args:
            value (float): value for IDD Field `soil_moisture_content_volume_fraction`
                Unit: percent
                Default value: 30.0
                value >= 0.0
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
                                 'for field `soil_moisture_content_volume_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_volume_fraction`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_volume_fraction`')

        self._data["Soil Moisture Content Volume Fraction"] = value

    @property
    def soil_moisture_content_volume_fraction_at_saturation(self):
        """Get soil_moisture_content_volume_fraction_at_saturation

        Returns:
            float: the value of `soil_moisture_content_volume_fraction_at_saturation` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction at Saturation"]

    @soil_moisture_content_volume_fraction_at_saturation.setter
    def soil_moisture_content_volume_fraction_at_saturation(self, value=50.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_volume_fraction_at_saturation`

        Args:
            value (float): value for IDD Field `soil_moisture_content_volume_fraction_at_saturation`
                Unit: percent
                Default value: 50.0
                value >= 0.0
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
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`')

        self._data["Soil Moisture Content Volume Fraction at Saturation"] = value

    @property
    def kusudaachenbach_average_surface_temperature(self):
        """Get kusudaachenbach_average_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Surface Temperature"]

    @kusudaachenbach_average_surface_temperature.setter
    def kusudaachenbach_average_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_surface_temperature`
        Annual average surface temperature.

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_surface_temperature`
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
                                 'for field `kusudaachenbach_average_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Surface Temperature"] = value

    @property
    def kusudaachenbach_average_amplitude_of_surface_temperature(self):
        """Get kusudaachenbach_average_amplitude_of_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_amplitude_of_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"]

    @kusudaachenbach_average_amplitude_of_surface_temperature.setter
    def kusudaachenbach_average_amplitude_of_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`
        Annual average surface temperature variation from average.

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`
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
                                 'for field `kusudaachenbach_average_amplitude_of_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = value

    @property
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self):
        """Get kusudaachenbach_phase_shift_of_minimum_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_phase_shift_of_minimum_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"]

    @kusudaachenbach_phase_shift_of_minimum_surface_temperature.setter
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`
        The phase shift of minimum surface temperature, or the day
        of the year when the minimum surface temperature occurs.

        Args:
            value (float): value for IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`
                Unit: days
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """Get evapotranspiration_ground_cover_parameter

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set
        """
        return self._data["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4 ):
        """  Corresponds to IDD Field `evapotranspiration_ground_cover_parameter`
        This specifies the ground cover effects during evapotranspiration
        calculations.  The value roughly represents the following cases:
        = 0   : concrete or other solid, non-permeable ground surface material
        = 0.5 : short grass, much like a manicured lawn
        = 1   : standard reference state (12 cm grass)
        = 1.5 : wild growth

        Args:
            value (float): value for IDD Field `evapotranspiration_ground_cover_parameter`
                Default value: 0.4
                value >= 0.0
                value <= 1.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `evapotranspiration_ground_cover_parameter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evapotranspiration_ground_cover_parameter`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `evapotranspiration_ground_cover_parameter`')

        self._data["Evapotranspiration Ground Cover Parameter"] = value

    @property
    def slab_boundary_condition_model_name(self):
        """Get slab_boundary_condition_model_name

        Returns:
            str: the value of `slab_boundary_condition_model_name` or None if not set
        """
        return self._data["Slab Boundary Condition Model Name"]

    @slab_boundary_condition_model_name.setter
    def slab_boundary_condition_model_name(self, value=None):
        """  Corresponds to IDD Field `slab_boundary_condition_model_name`

        Args:
            value (str): value for IDD Field `slab_boundary_condition_model_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `slab_boundary_condition_model_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `slab_boundary_condition_model_name`')

        self._data["Slab Boundary Condition Model Name"] = value

    @property
    def slab_location(self):
        """Get slab_location

        Returns:
            str: the value of `slab_location` or None if not set
        """
        return self._data["Slab Location"]

    @slab_location.setter
    def slab_location(self, value=None):
        """  Corresponds to IDD Field `slab_location`
        This field specifies whether the slab is located "in-grade" or "on-grade"

        Args:
            value (str): value for IDD Field `slab_location`
                Accepted values are:
                      - InGrade
                      - OnGrade
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `slab_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `slab_location`')
            vals = set()
            vals.add("InGrade")
            vals.add("OnGrade")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `slab_location`'.format(value))

        self._data["Slab Location"] = value

    @property
    def slab_material_name(self):
        """Get slab_material_name

        Returns:
            str: the value of `slab_material_name` or None if not set
        """
        return self._data["Slab Material Name"]

    @slab_material_name.setter
    def slab_material_name(self, value=None):
        """  Corresponds to IDD Field `slab_material_name`
        Only applicable for the in-grade case

        Args:
            value (str): value for IDD Field `slab_material_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `slab_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `slab_material_name`')

        self._data["Slab Material Name"] = value

    @property
    def horizontal_insulation(self):
        """Get horizontal_insulation

        Returns:
            str: the value of `horizontal_insulation` or None if not set
        """
        return self._data["Horizontal Insulation"]

    @horizontal_insulation.setter
    def horizontal_insulation(self, value="No"):
        """  Corresponds to IDD Field `horizontal_insulation`
        This field specifies the presence of insulation beneath the slab.
        Only required for in-grade case.

        Args:
            value (str): value for IDD Field `horizontal_insulation`
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
                                 'for field `horizontal_insulation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `horizontal_insulation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `horizontal_insulation`'.format(value))

        self._data["Horizontal Insulation"] = value

    @property
    def horizontal_insulation_material_name(self):
        """Get horizontal_insulation_material_name

        Returns:
            str: the value of `horizontal_insulation_material_name` or None if not set
        """
        return self._data["Horizontal Insulation Material Name"]

    @horizontal_insulation_material_name.setter
    def horizontal_insulation_material_name(self, value=None):
        """  Corresponds to IDD Field `horizontal_insulation_material_name`
        This field specifies the horizontal insulation material.

        Args:
            value (str): value for IDD Field `horizontal_insulation_material_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `horizontal_insulation_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `horizontal_insulation_material_name`')

        self._data["Horizontal Insulation Material Name"] = value

    @property
    def horizontal_insulation_extents(self):
        """Get horizontal_insulation_extents

        Returns:
            str: the value of `horizontal_insulation_extents` or None if not set
        """
        return self._data["Horizontal Insulation Extents"]

    @horizontal_insulation_extents.setter
    def horizontal_insulation_extents(self, value="Full"):
        """  Corresponds to IDD Field `horizontal_insulation_extents`
        This field specifies whether the horizontal insulation fully insulates
        the surface or is perimeter only insulation

        Args:
            value (str): value for IDD Field `horizontal_insulation_extents`
                Accepted values are:
                      - Full
                      - Perimeter
                Default value: Full
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `horizontal_insulation_extents`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `horizontal_insulation_extents`')
            vals = set()
            vals.add("Full")
            vals.add("Perimeter")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `horizontal_insulation_extents`'.format(value))

        self._data["Horizontal Insulation Extents"] = value

    @property
    def perimeter_insulation_width(self):
        """Get perimeter_insulation_width

        Returns:
            float: the value of `perimeter_insulation_width` or None if not set
        """
        return self._data["Perimeter Insulation Width"]

    @perimeter_insulation_width.setter
    def perimeter_insulation_width(self, value=None):
        """  Corresponds to IDD Field `perimeter_insulation_width`
        This field specifies the width of the underfloor perimeter insulation

        Args:
            value (float): value for IDD Field `perimeter_insulation_width`
                Unit: m
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
                                 'for field `perimeter_insulation_width`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `perimeter_insulation_width`')

        self._data["Perimeter Insulation Width"] = value

    @property
    def vertical_insulation(self):
        """Get vertical_insulation

        Returns:
            str: the value of `vertical_insulation` or None if not set
        """
        return self._data["Vertical Insulation"]

    @vertical_insulation.setter
    def vertical_insulation(self, value="No"):
        """  Corresponds to IDD Field `vertical_insulation`
        This field specifies the presence of vertical insulation at the slab edge.

        Args:
            value (str): value for IDD Field `vertical_insulation`
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
                                 'for field `vertical_insulation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `vertical_insulation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `vertical_insulation`'.format(value))

        self._data["Vertical Insulation"] = value

    @property
    def vertical_insulation_material_name(self):
        """Get vertical_insulation_material_name

        Returns:
            str: the value of `vertical_insulation_material_name` or None if not set
        """
        return self._data["Vertical Insulation Material Name"]

    @vertical_insulation_material_name.setter
    def vertical_insulation_material_name(self, value=None):
        """  Corresponds to IDD Field `vertical_insulation_material_name`
        This field specifies the vertical insulation material.

        Args:
            value (str): value for IDD Field `vertical_insulation_material_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `vertical_insulation_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `vertical_insulation_material_name`')

        self._data["Vertical Insulation Material Name"] = value

    @property
    def vertical_insulation_depth(self):
        """Get vertical_insulation_depth

        Returns:
            float: the value of `vertical_insulation_depth` or None if not set
        """
        return self._data["Vertical Insulation Depth"]

    @vertical_insulation_depth.setter
    def vertical_insulation_depth(self, value=None):
        """  Corresponds to IDD Field `vertical_insulation_depth`
        Only used when including vertical insulation
        This field specifies the depth of the vertical insulation

        Args:
            value (float): value for IDD Field `vertical_insulation_depth`
                Unit: m
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
                                 'for field `vertical_insulation_depth`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `vertical_insulation_depth`')

        self._data["Vertical Insulation Depth"] = value

    @property
    def simulation_timestep(self):
        """Get simulation_timestep

        Returns:
            str: the value of `simulation_timestep` or None if not set
        """
        return self._data["Simulation Timestep"]

    @simulation_timestep.setter
    def simulation_timestep(self, value="Hourly"):
        """  Corresponds to IDD Field `simulation_timestep`
        This field specifies the domain simulation timestep.

        Args:
            value (str): value for IDD Field `simulation_timestep`
                Accepted values are:
                      - Hourly
                      - Timestep
                Default value: Hourly
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simulation_timestep`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simulation_timestep`')
            vals = set()
            vals.add("Hourly")
            vals.add("Timestep")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simulation_timestep`'.format(value))

        self._data["Simulation Timestep"] = value

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
        out.append(self._to_str(self.ground_domain_depth))
        out.append(self._to_str(self.aspect_ratio))
        out.append(self._to_str(self.perimeter_offset))
        out.append(self._to_str(self.soil_thermal_conductivity))
        out.append(self._to_str(self.soil_density))
        out.append(self._to_str(self.soil_specific_heat))
        out.append(self._to_str(self.soil_moisture_content_volume_fraction))
        out.append(self._to_str(self.soil_moisture_content_volume_fraction_at_saturation))
        out.append(self._to_str(self.kusudaachenbach_average_surface_temperature))
        out.append(self._to_str(self.kusudaachenbach_average_amplitude_of_surface_temperature))
        out.append(self._to_str(self.kusudaachenbach_phase_shift_of_minimum_surface_temperature))
        out.append(self._to_str(self.evapotranspiration_ground_cover_parameter))
        out.append(self._to_str(self.slab_boundary_condition_model_name))
        out.append(self._to_str(self.slab_location))
        out.append(self._to_str(self.slab_material_name))
        out.append(self._to_str(self.horizontal_insulation))
        out.append(self._to_str(self.horizontal_insulation_material_name))
        out.append(self._to_str(self.horizontal_insulation_extents))
        out.append(self._to_str(self.perimeter_insulation_width))
        out.append(self._to_str(self.vertical_insulation))
        out.append(self._to_str(self.vertical_insulation_material_name))
        out.append(self._to_str(self.vertical_insulation_depth))
        out.append(self._to_str(self.simulation_timestep))
        return ",".join(out)

class SiteGroundReflectance(object):
    """ Corresponds to IDD object `Site:GroundReflectance`
        Specifies the ground reflectance values used to calculate ground reflected solar.
        The ground reflectance can be further modified when snow is on the ground
        by Site:GroundReflectance:SnowModifier.
    """
    internal_name = "Site:GroundReflectance"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:GroundReflectance`
        """
        self._data = OrderedDict()
        self._data["January Ground Reflectance"] = None
        self._data["February Ground Reflectance"] = None
        self._data["March Ground Reflectance"] = None
        self._data["April Ground Reflectance"] = None
        self._data["May Ground Reflectance"] = None
        self._data["June Ground Reflectance"] = None
        self._data["July Ground Reflectance"] = None
        self._data["August Ground Reflectance"] = None
        self._data["September Ground Reflectance"] = None
        self._data["October Ground Reflectance"] = None
        self._data["November Ground Reflectance"] = None
        self._data["December Ground Reflectance"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.january_ground_reflectance = None
        else:
            self.january_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.february_ground_reflectance = None
        else:
            self.february_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.march_ground_reflectance = None
        else:
            self.march_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.april_ground_reflectance = None
        else:
            self.april_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.may_ground_reflectance = None
        else:
            self.may_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.june_ground_reflectance = None
        else:
            self.june_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.july_ground_reflectance = None
        else:
            self.july_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.august_ground_reflectance = None
        else:
            self.august_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.september_ground_reflectance = None
        else:
            self.september_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.october_ground_reflectance = None
        else:
            self.october_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.november_ground_reflectance = None
        else:
            self.november_ground_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.december_ground_reflectance = None
        else:
            self.december_ground_reflectance = vals[i]
        i += 1

    @property
    def january_ground_reflectance(self):
        """Get january_ground_reflectance

        Returns:
            float: the value of `january_ground_reflectance` or None if not set
        """
        return self._data["January Ground Reflectance"]

    @january_ground_reflectance.setter
    def january_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `january_ground_reflectance`

        Args:
            value (float): value for IDD Field `january_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `january_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `january_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `january_ground_reflectance`')

        self._data["January Ground Reflectance"] = value

    @property
    def february_ground_reflectance(self):
        """Get february_ground_reflectance

        Returns:
            float: the value of `february_ground_reflectance` or None if not set
        """
        return self._data["February Ground Reflectance"]

    @february_ground_reflectance.setter
    def february_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `february_ground_reflectance`

        Args:
            value (float): value for IDD Field `february_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `february_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `february_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `february_ground_reflectance`')

        self._data["February Ground Reflectance"] = value

    @property
    def march_ground_reflectance(self):
        """Get march_ground_reflectance

        Returns:
            float: the value of `march_ground_reflectance` or None if not set
        """
        return self._data["March Ground Reflectance"]

    @march_ground_reflectance.setter
    def march_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `march_ground_reflectance`

        Args:
            value (float): value for IDD Field `march_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `march_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `march_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `march_ground_reflectance`')

        self._data["March Ground Reflectance"] = value

    @property
    def april_ground_reflectance(self):
        """Get april_ground_reflectance

        Returns:
            float: the value of `april_ground_reflectance` or None if not set
        """
        return self._data["April Ground Reflectance"]

    @april_ground_reflectance.setter
    def april_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `april_ground_reflectance`

        Args:
            value (float): value for IDD Field `april_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `april_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `april_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `april_ground_reflectance`')

        self._data["April Ground Reflectance"] = value

    @property
    def may_ground_reflectance(self):
        """Get may_ground_reflectance

        Returns:
            float: the value of `may_ground_reflectance` or None if not set
        """
        return self._data["May Ground Reflectance"]

    @may_ground_reflectance.setter
    def may_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `may_ground_reflectance`

        Args:
            value (float): value for IDD Field `may_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `may_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `may_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `may_ground_reflectance`')

        self._data["May Ground Reflectance"] = value

    @property
    def june_ground_reflectance(self):
        """Get june_ground_reflectance

        Returns:
            float: the value of `june_ground_reflectance` or None if not set
        """
        return self._data["June Ground Reflectance"]

    @june_ground_reflectance.setter
    def june_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `june_ground_reflectance`

        Args:
            value (float): value for IDD Field `june_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `june_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `june_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `june_ground_reflectance`')

        self._data["June Ground Reflectance"] = value

    @property
    def july_ground_reflectance(self):
        """Get july_ground_reflectance

        Returns:
            float: the value of `july_ground_reflectance` or None if not set
        """
        return self._data["July Ground Reflectance"]

    @july_ground_reflectance.setter
    def july_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `july_ground_reflectance`

        Args:
            value (float): value for IDD Field `july_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `july_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `july_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `july_ground_reflectance`')

        self._data["July Ground Reflectance"] = value

    @property
    def august_ground_reflectance(self):
        """Get august_ground_reflectance

        Returns:
            float: the value of `august_ground_reflectance` or None if not set
        """
        return self._data["August Ground Reflectance"]

    @august_ground_reflectance.setter
    def august_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `august_ground_reflectance`

        Args:
            value (float): value for IDD Field `august_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `august_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `august_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `august_ground_reflectance`')

        self._data["August Ground Reflectance"] = value

    @property
    def september_ground_reflectance(self):
        """Get september_ground_reflectance

        Returns:
            float: the value of `september_ground_reflectance` or None if not set
        """
        return self._data["September Ground Reflectance"]

    @september_ground_reflectance.setter
    def september_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `september_ground_reflectance`

        Args:
            value (float): value for IDD Field `september_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `september_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `september_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `september_ground_reflectance`')

        self._data["September Ground Reflectance"] = value

    @property
    def october_ground_reflectance(self):
        """Get october_ground_reflectance

        Returns:
            float: the value of `october_ground_reflectance` or None if not set
        """
        return self._data["October Ground Reflectance"]

    @october_ground_reflectance.setter
    def october_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `october_ground_reflectance`

        Args:
            value (float): value for IDD Field `october_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `october_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `october_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `october_ground_reflectance`')

        self._data["October Ground Reflectance"] = value

    @property
    def november_ground_reflectance(self):
        """Get november_ground_reflectance

        Returns:
            float: the value of `november_ground_reflectance` or None if not set
        """
        return self._data["November Ground Reflectance"]

    @november_ground_reflectance.setter
    def november_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `november_ground_reflectance`

        Args:
            value (float): value for IDD Field `november_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `november_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `november_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `november_ground_reflectance`')

        self._data["November Ground Reflectance"] = value

    @property
    def december_ground_reflectance(self):
        """Get december_ground_reflectance

        Returns:
            float: the value of `december_ground_reflectance` or None if not set
        """
        return self._data["December Ground Reflectance"]

    @december_ground_reflectance.setter
    def december_ground_reflectance(self, value=0.2 ):
        """  Corresponds to IDD Field `december_ground_reflectance`

        Args:
            value (float): value for IDD Field `december_ground_reflectance`
                Unit: dimensionless
                Default value: 0.2
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
                                 'for field `december_ground_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `december_ground_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `december_ground_reflectance`')

        self._data["December Ground Reflectance"] = value

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
        out.append(self._to_str(self.january_ground_reflectance))
        out.append(self._to_str(self.february_ground_reflectance))
        out.append(self._to_str(self.march_ground_reflectance))
        out.append(self._to_str(self.april_ground_reflectance))
        out.append(self._to_str(self.may_ground_reflectance))
        out.append(self._to_str(self.june_ground_reflectance))
        out.append(self._to_str(self.july_ground_reflectance))
        out.append(self._to_str(self.august_ground_reflectance))
        out.append(self._to_str(self.september_ground_reflectance))
        out.append(self._to_str(self.october_ground_reflectance))
        out.append(self._to_str(self.november_ground_reflectance))
        out.append(self._to_str(self.december_ground_reflectance))
        return ",".join(out)

class SiteGroundReflectanceSnowModifier(object):
    """ Corresponds to IDD object `Site:GroundReflectance:SnowModifier`
        Specifies ground reflectance multipliers when snow resident on the ground.
        These multipliers are applied to the "normal" ground reflectances specified
        in Site:GroundReflectance.
    """
    internal_name = "Site:GroundReflectance:SnowModifier"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:GroundReflectance:SnowModifier`
        """
        self._data = OrderedDict()
        self._data["Ground Reflected Solar Modifier"] = None
        self._data["Daylighting Ground Reflected Solar Modifier"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.ground_reflected_solar_modifier = None
        else:
            self.ground_reflected_solar_modifier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daylighting_ground_reflected_solar_modifier = None
        else:
            self.daylighting_ground_reflected_solar_modifier = vals[i]
        i += 1

    @property
    def ground_reflected_solar_modifier(self):
        """Get ground_reflected_solar_modifier

        Returns:
            float: the value of `ground_reflected_solar_modifier` or None if not set
        """
        return self._data["Ground Reflected Solar Modifier"]

    @ground_reflected_solar_modifier.setter
    def ground_reflected_solar_modifier(self, value=1.0 ):
        """  Corresponds to IDD Field `ground_reflected_solar_modifier`
        Value for modifying the "normal" ground reflectance when Snow is on ground
        when calculating the "Ground Reflected Solar Radiation Value"
        a value of 1.0 here uses the "normal" ground reflectance
        Ground Reflected Solar = (BeamSolar*CosSunZenith + DiffuseSolar)*GroundReflectance
        This would be further modified by the Snow Ground Reflectance Modifier when Snow was on the ground
        When Snow on ground, effective GroundReflectance is normal GroundReflectance*"Ground Reflectance Snow Modifier"
        Ground Reflectance achieved in this manner will be restricted to [0.0,1.0]

        Args:
            value (float): value for IDD Field `ground_reflected_solar_modifier`
                Default value: 1.0
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
                                 'for field `ground_reflected_solar_modifier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ground_reflected_solar_modifier`')

        self._data["Ground Reflected Solar Modifier"] = value

    @property
    def daylighting_ground_reflected_solar_modifier(self):
        """Get daylighting_ground_reflected_solar_modifier

        Returns:
            float: the value of `daylighting_ground_reflected_solar_modifier` or None if not set
        """
        return self._data["Daylighting Ground Reflected Solar Modifier"]

    @daylighting_ground_reflected_solar_modifier.setter
    def daylighting_ground_reflected_solar_modifier(self, value=1.0 ):
        """  Corresponds to IDD Field `daylighting_ground_reflected_solar_modifier`
        Value for modifying the "normal" daylighting ground reflectance when Snow is on ground
        when calculating the "Ground Reflected Solar Radiation Value"
        a value of 1.0 here uses the "normal" ground reflectance
        Ground Reflected Solar = (BeamSolar*CosSunZenith + DiffuseSolar)*GroundReflectance
        This would be further modified by the Snow Ground Reflectance Modifier when Snow was on the ground
        When Snow on ground, effective GroundReflectance is normal GroundReflectance*"Daylighting Ground Reflectance Snow Modifier"
        Ground Reflectance achieved in this manner will be restricted to [0.0,1.0]

        Args:
            value (float): value for IDD Field `daylighting_ground_reflected_solar_modifier`
                Default value: 1.0
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
                                 'for field `daylighting_ground_reflected_solar_modifier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `daylighting_ground_reflected_solar_modifier`')

        self._data["Daylighting Ground Reflected Solar Modifier"] = value

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
        out.append(self._to_str(self.ground_reflected_solar_modifier))
        out.append(self._to_str(self.daylighting_ground_reflected_solar_modifier))
        return ",".join(out)

class SiteWaterMainsTemperature(object):
    """ Corresponds to IDD object `Site:WaterMainsTemperature`
        Used to calculate water mains temperatures delivered by underground water main pipes.
        Water mains temperatures are a function of outdoor climate conditions
        and vary with time of year.
    """
    internal_name = "Site:WaterMainsTemperature"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:WaterMainsTemperature`
        """
        self._data = OrderedDict()
        self._data["Calculation Method"] = None
        self._data["Temperature Schedule Name"] = None
        self._data["Annual Average Outdoor Air Temperature"] = None
        self._data["Maximum Difference In Monthly Average Outdoor Air Temperatures"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.calculation_method = None
        else:
            self.calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_schedule_name = None
        else:
            self.temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.annual_average_outdoor_air_temperature = None
        else:
            self.annual_average_outdoor_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_difference_in_monthly_average_outdoor_air_temperatures = None
        else:
            self.maximum_difference_in_monthly_average_outdoor_air_temperatures = vals[i]
        i += 1

    @property
    def calculation_method(self):
        """Get calculation_method

        Returns:
            str: the value of `calculation_method` or None if not set
        """
        return self._data["Calculation Method"]

    @calculation_method.setter
    def calculation_method(self, value=None):
        """  Corresponds to IDD Field `calculation_method`

        Args:
            value (str): value for IDD Field `calculation_method`
                Accepted values are:
                      - Schedule
                      - Correlation
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `calculation_method`')
            vals = set()
            vals.add("Schedule")
            vals.add("Correlation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `calculation_method`'.format(value))

        self._data["Calculation Method"] = value

    @property
    def temperature_schedule_name(self):
        """Get temperature_schedule_name

        Returns:
            str: the value of `temperature_schedule_name` or None if not set
        """
        return self._data["Temperature Schedule Name"]

    @temperature_schedule_name.setter
    def temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `temperature_schedule_name`

        Args:
            value (str): value for IDD Field `temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `temperature_schedule_name`')

        self._data["Temperature Schedule Name"] = value

    @property
    def annual_average_outdoor_air_temperature(self):
        """Get annual_average_outdoor_air_temperature

        Returns:
            float: the value of `annual_average_outdoor_air_temperature` or None if not set
        """
        return self._data["Annual Average Outdoor Air Temperature"]

    @annual_average_outdoor_air_temperature.setter
    def annual_average_outdoor_air_temperature(self, value=None):
        """  Corresponds to IDD Field `annual_average_outdoor_air_temperature`

        Args:
            value (float): value for IDD Field `annual_average_outdoor_air_temperature`
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
                                 'for field `annual_average_outdoor_air_temperature`'.format(value))

        self._data["Annual Average Outdoor Air Temperature"] = value

    @property
    def maximum_difference_in_monthly_average_outdoor_air_temperatures(self):
        """Get maximum_difference_in_monthly_average_outdoor_air_temperatures

        Returns:
            float: the value of `maximum_difference_in_monthly_average_outdoor_air_temperatures` or None if not set
        """
        return self._data["Maximum Difference In Monthly Average Outdoor Air Temperatures"]

    @maximum_difference_in_monthly_average_outdoor_air_temperatures.setter
    def maximum_difference_in_monthly_average_outdoor_air_temperatures(self, value=None):
        """  Corresponds to IDD Field `maximum_difference_in_monthly_average_outdoor_air_temperatures`

        Args:
            value (float): value for IDD Field `maximum_difference_in_monthly_average_outdoor_air_temperatures`
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
                                 'for field `maximum_difference_in_monthly_average_outdoor_air_temperatures`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_difference_in_monthly_average_outdoor_air_temperatures`')

        self._data["Maximum Difference In Monthly Average Outdoor Air Temperatures"] = value

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
        out.append(self._to_str(self.calculation_method))
        out.append(self._to_str(self.temperature_schedule_name))
        out.append(self._to_str(self.annual_average_outdoor_air_temperature))
        out.append(self._to_str(self.maximum_difference_in_monthly_average_outdoor_air_temperatures))
        return ",".join(out)

class SitePrecipitation(object):
    """ Corresponds to IDD object `Site:Precipitation`
        Used to describe the amount of water precipitation at the building site.
        Precipitation includes both rain and the equivalent water content of snow.
    """
    internal_name = "Site:Precipitation"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:Precipitation`
        """
        self._data = OrderedDict()
        self._data["Precipitation Model Type"] = None
        self._data["Design Level for Total Annual Precipitation"] = None
        self._data["Precipitation Rates Schedule Name"] = None
        self._data["Average Total Annual Precipitation"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.precipitation_model_type = None
        else:
            self.precipitation_model_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_for_total_annual_precipitation = None
        else:
            self.design_level_for_total_annual_precipitation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.precipitation_rates_schedule_name = None
        else:
            self.precipitation_rates_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.average_total_annual_precipitation = None
        else:
            self.average_total_annual_precipitation = vals[i]
        i += 1

    @property
    def precipitation_model_type(self):
        """Get precipitation_model_type

        Returns:
            str: the value of `precipitation_model_type` or None if not set
        """
        return self._data["Precipitation Model Type"]

    @precipitation_model_type.setter
    def precipitation_model_type(self, value=None):
        """  Corresponds to IDD Field `precipitation_model_type`

        Args:
            value (str): value for IDD Field `precipitation_model_type`
                Accepted values are:
                      - ScheduleAndDesignLevel
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `precipitation_model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `precipitation_model_type`')
            vals = set()
            vals.add("ScheduleAndDesignLevel")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `precipitation_model_type`'.format(value))

        self._data["Precipitation Model Type"] = value

    @property
    def design_level_for_total_annual_precipitation(self):
        """Get design_level_for_total_annual_precipitation

        Returns:
            float: the value of `design_level_for_total_annual_precipitation` or None if not set
        """
        return self._data["Design Level for Total Annual Precipitation"]

    @design_level_for_total_annual_precipitation.setter
    def design_level_for_total_annual_precipitation(self, value=None):
        """  Corresponds to IDD Field `design_level_for_total_annual_precipitation`
        meters of water per year used for design level

        Args:
            value (float): value for IDD Field `design_level_for_total_annual_precipitation`
                Unit: m/yr
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_level_for_total_annual_precipitation`'.format(value))

        self._data["Design Level for Total Annual Precipitation"] = value

    @property
    def precipitation_rates_schedule_name(self):
        """Get precipitation_rates_schedule_name

        Returns:
            str: the value of `precipitation_rates_schedule_name` or None if not set
        """
        return self._data["Precipitation Rates Schedule Name"]

    @precipitation_rates_schedule_name.setter
    def precipitation_rates_schedule_name(self, value=None):
        """  Corresponds to IDD Field `precipitation_rates_schedule_name`
        Schedule values in meters of water per hour
        values should be non-negative

        Args:
            value (str): value for IDD Field `precipitation_rates_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `precipitation_rates_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `precipitation_rates_schedule_name`')

        self._data["Precipitation Rates Schedule Name"] = value

    @property
    def average_total_annual_precipitation(self):
        """Get average_total_annual_precipitation

        Returns:
            float: the value of `average_total_annual_precipitation` or None if not set
        """
        return self._data["Average Total Annual Precipitation"]

    @average_total_annual_precipitation.setter
    def average_total_annual_precipitation(self, value=None):
        """  Corresponds to IDD Field `average_total_annual_precipitation`
        meters of water per year from average weather statistics

        Args:
            value (float): value for IDD Field `average_total_annual_precipitation`
                Unit: m/yr
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
                                 'for field `average_total_annual_precipitation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `average_total_annual_precipitation`')

        self._data["Average Total Annual Precipitation"] = value

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
        out.append(self._to_str(self.precipitation_model_type))
        out.append(self._to_str(self.design_level_for_total_annual_precipitation))
        out.append(self._to_str(self.precipitation_rates_schedule_name))
        out.append(self._to_str(self.average_total_annual_precipitation))
        return ",".join(out)

class SiteSolarAndVisibleSpectrum(object):
    """ Corresponds to IDD object `Site:SolarAndVisibleSpectrum`
        If this object is omitted, the default solar and visible spectrum data will be used.
    """
    internal_name = "Site:SolarAndVisibleSpectrum"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:SolarAndVisibleSpectrum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Spectrum Data Method"] = None
        self._data["Solar Spectrum Data Object Name"] = None
        self._data["Visible Spectrum Data Object Name"] = None

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
            self.spectrum_data_method = None
        else:
            self.spectrum_data_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_spectrum_data_object_name = None
        else:
            self.solar_spectrum_data_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_spectrum_data_object_name = None
        else:
            self.visible_spectrum_data_object_name = vals[i]
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
    def spectrum_data_method(self):
        """Get spectrum_data_method

        Returns:
            str: the value of `spectrum_data_method` or None if not set
        """
        return self._data["Spectrum Data Method"]

    @spectrum_data_method.setter
    def spectrum_data_method(self, value="Default"):
        """  Corresponds to IDD Field `spectrum_data_method`
        The method specifies which of the solar and visible spectrum data to use in the calculations.
        Choices: Default - existing hard-wired spectrum data in EnergyPlus.
        UserDefined - user specified spectrum data referenced by the next two fields

        Args:
            value (str): value for IDD Field `spectrum_data_method`
                Accepted values are:
                      - Default
                      - UserDefined
                Default value: Default
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `spectrum_data_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `spectrum_data_method`')
            vals = set()
            vals.add("Default")
            vals.add("UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `spectrum_data_method`'.format(value))

        self._data["Spectrum Data Method"] = value

    @property
    def solar_spectrum_data_object_name(self):
        """Get solar_spectrum_data_object_name

        Returns:
            str: the value of `solar_spectrum_data_object_name` or None if not set
        """
        return self._data["Solar Spectrum Data Object Name"]

    @solar_spectrum_data_object_name.setter
    def solar_spectrum_data_object_name(self, value=None):
        """  Corresponds to IDD Field `solar_spectrum_data_object_name`

        Args:
            value (str): value for IDD Field `solar_spectrum_data_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `solar_spectrum_data_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_spectrum_data_object_name`')

        self._data["Solar Spectrum Data Object Name"] = value

    @property
    def visible_spectrum_data_object_name(self):
        """Get visible_spectrum_data_object_name

        Returns:
            str: the value of `visible_spectrum_data_object_name` or None if not set
        """
        return self._data["Visible Spectrum Data Object Name"]

    @visible_spectrum_data_object_name.setter
    def visible_spectrum_data_object_name(self, value=None):
        """  Corresponds to IDD Field `visible_spectrum_data_object_name`

        Args:
            value (str): value for IDD Field `visible_spectrum_data_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `visible_spectrum_data_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `visible_spectrum_data_object_name`')

        self._data["Visible Spectrum Data Object Name"] = value

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
        out.append(self._to_str(self.spectrum_data_method))
        out.append(self._to_str(self.solar_spectrum_data_object_name))
        out.append(self._to_str(self.visible_spectrum_data_object_name))
        return ",".join(out)

class SiteSpectrumData(object):
    """ Corresponds to IDD object `Site:SpectrumData`
        Spectrum Data Type is followed by up to 107 sets of normal-incidence measured values of
        [wavelength, spectrum] for wavelengths covering the solar (0.25 to 2.5 microns) or visible
        spectrum (0.38 to 0.78 microns)
    """
    internal_name = "Site:SpectrumData"
    field_count = 112

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Site:SpectrumData`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Spectrum Data Type"] = None
        self._data["Wavelength"] = None
        self._data["Spectrum"] = None
        self._data["Wavelength"] = None
        self._data["Spectrum"] = None
        self._data["Wavelength"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None
        self._data["Spectrum"] = None

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
            self.spectrum_data_type = None
        else:
            self.spectrum_data_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wavelength = None
        else:
            self.wavelength = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wavelength = None
        else:
            self.wavelength = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wavelength = None
        else:
            self.wavelength = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.spectrum = None
        else:
            self.spectrum = vals[i]
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
    def spectrum_data_type(self):
        """Get spectrum_data_type

        Returns:
            str: the value of `spectrum_data_type` or None if not set
        """
        return self._data["Spectrum Data Type"]

    @spectrum_data_type.setter
    def spectrum_data_type(self, value=None):
        """  Corresponds to IDD Field `spectrum_data_type`

        Args:
            value (str): value for IDD Field `spectrum_data_type`
                Accepted values are:
                      - Solar
                      - Visible
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `spectrum_data_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `spectrum_data_type`')
            vals = set()
            vals.add("Solar")
            vals.add("Visible")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `spectrum_data_type`'.format(value))

        self._data["Spectrum Data Type"] = value

    @property
    def wavelength(self):
        """Get wavelength

        Returns:
            float: the value of `wavelength` or None if not set
        """
        return self._data["Wavelength"]

    @wavelength.setter
    def wavelength(self, value=None):
        """  Corresponds to IDD Field `wavelength`

        Args:
            value (float): value for IDD Field `wavelength`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength`'.format(value))

        self._data["Wavelength"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def wavelength(self):
        """Get wavelength

        Returns:
            float: the value of `wavelength` or None if not set
        """
        return self._data["Wavelength"]

    @wavelength.setter
    def wavelength(self, value=None):
        """  Corresponds to IDD Field `wavelength`

        Args:
            value (float): value for IDD Field `wavelength`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength`'.format(value))

        self._data["Wavelength"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def wavelength(self):
        """Get wavelength

        Returns:
            float: the value of `wavelength` or None if not set
        """
        return self._data["Wavelength"]

    @wavelength.setter
    def wavelength(self, value=None):
        """  Corresponds to IDD Field `wavelength`

        Args:
            value (float): value for IDD Field `wavelength`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength`'.format(value))

        self._data["Wavelength"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

    @property
    def spectrum(self):
        """Get spectrum

        Returns:
            float: the value of `spectrum` or None if not set
        """
        return self._data["Spectrum"]

    @spectrum.setter
    def spectrum(self, value=None):
        """  Corresponds to IDD Field `spectrum`

        Args:
            value (float): value for IDD Field `spectrum`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum`'.format(value))

        self._data["Spectrum"] = value

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
        out.append(self._to_str(self.spectrum_data_type))
        out.append(self._to_str(self.wavelength))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.wavelength))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.wavelength))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        out.append(self._to_str(self.spectrum))
        return ",".join(out)