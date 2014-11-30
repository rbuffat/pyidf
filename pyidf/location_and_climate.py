from collections import OrderedDict

class SiteLocation(object):
    """ Corresponds to IDD object `Site:Location`
        Specifies the building's location. Only one location is allowed.
        Weather data file location, if it exists, will override this object.
    
    """
    internal_name = "Site:Location"
    field_count = 5
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:Location`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Latitude"] = None
        self._data["Longitude"] = None
        self._data["Time Zone"] = None
        self._data["Elevation"] = None
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
            self.latitude = None
        else:
            self.latitude = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.longitude = None
        else:
            self.longitude = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.time_zone = None
        else:
            self.time_zone = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.elevation = None
        else:
            self.elevation = vals[i]
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
                Units: deg
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
                Units: deg
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
                Units: hr
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
                Units: m
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

class SizingPeriodDesignDay(object):
    """ Corresponds to IDD object `SizingPeriod:DesignDay`
        The design day object creates the parameters for the program to create
        the 24 hour weather profile that can be used for sizing as well as
        running to test the other simulation parameters. Parameters in this
        include a date (month and day), a day type (which uses the appropriate
        schedules for either sizing or simple tests), min/max temperatures,
        wind speeds, and solar radiation values.
    
    """
    internal_name = "SizingPeriod:DesignDay"
    field_count = 26
    required_fields = ["Name", "Month", "Day of Month", "Day Type", "Wind Speed", "Wind Direction"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SizingPeriod:DesignDay`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Month"] = None
        self._data["Day of Month"] = None
        self._data["Day Type"] = None
        self._data["Maximum Dry-Bulb Temperature"] = None
        self._data["Daily Dry-Bulb Temperature Range"] = None
        self._data["Dry-Bulb Temperature Range Modifier Type"] = None
        self._data["Dry-Bulb Temperature Range Modifier Day Schedule Name"] = None
        self._data["Humidity Condition Type"] = None
        self._data["Wetbulb or DewPoint at Maximum Dry-Bulb"] = None
        self._data["Humidity Condition Day Schedule Name"] = None
        self._data["Humidity Ratio at Maximum Dry-Bulb"] = None
        self._data["Enthalpy at Maximum Dry-Bulb  !will require units transition."] = None
        self._data["Daily Wet-Bulb Temperature Range"] = None
        self._data["Barometric Pressure"] = None
        self._data["Wind Speed"] = None
        self._data["Wind Direction"] = None
        self._data["Rain Indicator"] = None
        self._data["Snow Indicator"] = None
        self._data["Daylight Saving Time Indicator"] = None
        self._data["Solar Model Indicator"] = None
        self._data["Beam Solar Day Schedule Name"] = None
        self._data["Diffuse Solar Day Schedule Name"] = None
        self._data["ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)"] = None
        self._data["ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)"] = None
        self._data["Sky Clearness"] = None
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
            self.month = None
        else:
            self.month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_of_month = None
        else:
            self.day_of_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_type = None
        else:
            self.day_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_drybulb_temperature = None
        else:
            self.maximum_drybulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.daily_drybulb_temperature_range = None
        else:
            self.daily_drybulb_temperature_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_modifier_type = None
        else:
            self.drybulb_temperature_range_modifier_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_modifier_day_schedule_name = None
        else:
            self.drybulb_temperature_range_modifier_day_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_condition_type = None
        else:
            self.humidity_condition_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_or_dewpoint_at_maximum_drybulb = None
        else:
            self.wetbulb_or_dewpoint_at_maximum_drybulb = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_condition_day_schedule_name = None
        else:
            self.humidity_condition_day_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_at_maximum_drybulb = None
        else:
            self.humidity_ratio_at_maximum_drybulb = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enthalpy_at_maximum_drybulb_will_require_units_transition_ = None
        else:
            self.enthalpy_at_maximum_drybulb_will_require_units_transition_ = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.daily_wetbulb_temperature_range = None
        else:
            self.daily_wetbulb_temperature_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.barometric_pressure = None
        else:
            self.barometric_pressure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_speed = None
        else:
            self.wind_speed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction = None
        else:
            self.wind_direction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rain_indicator = None
        else:
            self.rain_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.snow_indicator = None
        else:
            self.snow_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.daylight_saving_time_indicator = None
        else:
            self.daylight_saving_time_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.solar_model_indicator = None
        else:
            self.solar_model_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.beam_solar_day_schedule_name = None
        else:
            self.beam_solar_day_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diffuse_solar_day_schedule_name = None
        else:
            self.diffuse_solar_day_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = None
        else:
            self.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = None
        else:
            self.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sky_clearness = None
        else:
            self.sky_clearness = vals[i]
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
    def month(self):
        """Get month

        Returns:
            int: the value of `month` or None if not set
        """
        return self._data["Month"]

    @month.setter
    def month(self, value=None):
        """  Corresponds to IDD Field `month`

        Args:
            value (int): value for IDD Field `month`
                value >= 1
                value <= 12
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
                                 'for field `month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `month`')

        self._data["Month"] = value

    @property
    def day_of_month(self):
        """Get day_of_month

        Returns:
            int: the value of `day_of_month` or None if not set
        """
        return self._data["Day of Month"]

    @day_of_month.setter
    def day_of_month(self, value=None):
        """  Corresponds to IDD Field `day_of_month`
        must be valid for Month field

        Args:
            value (int): value for IDD Field `day_of_month`
                value >= 1
                value <= 31
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
                                 'for field `day_of_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `day_of_month`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `day_of_month`')

        self._data["Day of Month"] = value

    @property
    def day_type(self):
        """Get day_type

        Returns:
            str: the value of `day_type` or None if not set
        """
        return self._data["Day Type"]

    @day_type.setter
    def day_type(self, value=None):
        """  Corresponds to IDD Field `day_type`
        Day Type selects the schedules appropriate for this design day

        Args:
            value (str): value for IDD Field `day_type`
                Accepted values are:
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `day_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `day_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `day_type`')
            vals = {}
            vals["sunday"] = "Sunday"
            vals["monday"] = "Monday"
            vals["tuesday"] = "Tuesday"
            vals["wednesday"] = "Wednesday"
            vals["thursday"] = "Thursday"
            vals["friday"] = "Friday"
            vals["saturday"] = "Saturday"
            vals["holiday"] = "Holiday"
            vals["summerdesignday"] = "SummerDesignDay"
            vals["winterdesignday"] = "WinterDesignDay"
            vals["customday1"] = "CustomDay1"
            vals["customday2"] = "CustomDay2"
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
                                     'field `day_type`'.format(value))
            value = vals[value_lower]

        self._data["Day Type"] = value

    @property
    def maximum_drybulb_temperature(self):
        """Get maximum_drybulb_temperature

        Returns:
            float: the value of `maximum_drybulb_temperature` or None if not set
        """
        return self._data["Maximum Dry-Bulb Temperature"]

    @maximum_drybulb_temperature.setter
    def maximum_drybulb_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_drybulb_temperature`
        This field is required when field "Dry-Bulb Temperature Range Modifier Type"
        is not "TemperatureProfileSchedule".

        Args:
            value (float): value for IDD Field `maximum_drybulb_temperature`
                Units: C
                value >= -90.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_drybulb_temperature`'.format(value))
            if value < -90.0:
                raise ValueError('value need to be greater or equal -90.0 '
                                 'for field `maximum_drybulb_temperature`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `maximum_drybulb_temperature`')

        self._data["Maximum Dry-Bulb Temperature"] = value

    @property
    def daily_drybulb_temperature_range(self):
        """Get daily_drybulb_temperature_range

        Returns:
            float: the value of `daily_drybulb_temperature_range` or None if not set
        """
        return self._data["Daily Dry-Bulb Temperature Range"]

    @daily_drybulb_temperature_range.setter
    def daily_drybulb_temperature_range(self, value=0.0 ):
        """  Corresponds to IDD Field `daily_drybulb_temperature_range`
        Must still produce appropriate maximum dry bulb (within range)
        This field is not needed if Dry-Bulb Temperature Range Modifier Type
        is "delta".

        Args:
            value (float): value for IDD Field `daily_drybulb_temperature_range`
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
                                 'for field `daily_drybulb_temperature_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `daily_drybulb_temperature_range`')

        self._data["Daily Dry-Bulb Temperature Range"] = value

    @property
    def drybulb_temperature_range_modifier_type(self):
        """Get drybulb_temperature_range_modifier_type

        Returns:
            str: the value of `drybulb_temperature_range_modifier_type` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range Modifier Type"]

    @drybulb_temperature_range_modifier_type.setter
    def drybulb_temperature_range_modifier_type(self, value="DefaultMultipliers"):
        """  Corresponds to IDD Field `drybulb_temperature_range_modifier_type`
        Type of modifier to the dry-bulb temperature calculated for the timestep

        Args:
            value (str): value for IDD Field `drybulb_temperature_range_modifier_type`
                Accepted values are:
                      - MultiplierSchedule
                      - DifferenceSchedule
                      - TemperatureProfileSchedule
                      - DefaultMultipliers
                Default value: DefaultMultipliers
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drybulb_temperature_range_modifier_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drybulb_temperature_range_modifier_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `drybulb_temperature_range_modifier_type`')
            vals = {}
            vals["multiplierschedule"] = "MultiplierSchedule"
            vals["differenceschedule"] = "DifferenceSchedule"
            vals["temperatureprofileschedule"] = "TemperatureProfileSchedule"
            vals["defaultmultipliers"] = "DefaultMultipliers"
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
                                     'field `drybulb_temperature_range_modifier_type`'.format(value))
            value = vals[value_lower]

        self._data["Dry-Bulb Temperature Range Modifier Type"] = value

    @property
    def drybulb_temperature_range_modifier_day_schedule_name(self):
        """Get drybulb_temperature_range_modifier_day_schedule_name

        Returns:
            str: the value of `drybulb_temperature_range_modifier_day_schedule_name` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range Modifier Day Schedule Name"]

    @drybulb_temperature_range_modifier_day_schedule_name.setter
    def drybulb_temperature_range_modifier_day_schedule_name(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_modifier_day_schedule_name`
        Only used when previous field is "MultiplierSchedule", "DifferenceSchedule" or
        "TemperatureProfileSchedule".
        For type "MultiplierSchedule"  the hour/time interval values should specify
        the fraction (0-1) of the dry-bulb temperature range to be subtracted
        from the maximum dry-bulb temperature for each timestep in the day
        For type "DifferenceSchedule" the values should specify a number to be subtracted
        from the maximum dry-bulb temperature for each timestep in the day.
        Note that numbers in the difference schedule cannot be negative as that
        would result in a higher maximum than the maximum previously specified.
        For type "TemperatureProfileSchedule" the values should specify the actual drybulb
        temperature for each timestep in the day.

        Args:
            value (str): value for IDD Field `drybulb_temperature_range_modifier_day_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drybulb_temperature_range_modifier_day_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drybulb_temperature_range_modifier_day_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `drybulb_temperature_range_modifier_day_schedule_name`')

        self._data["Dry-Bulb Temperature Range Modifier Day Schedule Name"] = value

    @property
    def humidity_condition_type(self):
        """Get humidity_condition_type

        Returns:
            str: the value of `humidity_condition_type` or None if not set
        """
        return self._data["Humidity Condition Type"]

    @humidity_condition_type.setter
    def humidity_condition_type(self, value="WetBulb"):
        """  Corresponds to IDD Field `humidity_condition_type`
        values/schedules indicated here and in subsequent fields create the humidity
        values in the 24 hour design day conditions profile.

        Args:
            value (str): value for IDD Field `humidity_condition_type`
                Accepted values are:
                      - WetBulb
                      - DewPoint
                      - HumidityRatio
                      - Enthalpy
                      - RelativeHumiditySchedule
                      - WetBulbProfileMultiplierSchedule
                      - WetBulbProfileDifferenceSchedule
                      - WetBulbProfileDefaultMultipliers
                Default value: WetBulb
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `humidity_condition_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `humidity_condition_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `humidity_condition_type`')
            vals = {}
            vals["wetbulb"] = "WetBulb"
            vals["dewpoint"] = "DewPoint"
            vals["humidityratio"] = "HumidityRatio"
            vals["enthalpy"] = "Enthalpy"
            vals["relativehumidityschedule"] = "RelativeHumiditySchedule"
            vals["wetbulbprofilemultiplierschedule"] = "WetBulbProfileMultiplierSchedule"
            vals["wetbulbprofiledifferenceschedule"] = "WetBulbProfileDifferenceSchedule"
            vals["wetbulbprofiledefaultmultipliers"] = "WetBulbProfileDefaultMultipliers"
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
                                     'field `humidity_condition_type`'.format(value))
            value = vals[value_lower]

        self._data["Humidity Condition Type"] = value

    @property
    def wetbulb_or_dewpoint_at_maximum_drybulb(self):
        """Get wetbulb_or_dewpoint_at_maximum_drybulb

        Returns:
            float: the value of `wetbulb_or_dewpoint_at_maximum_drybulb` or None if not set
        """
        return self._data["Wetbulb or DewPoint at Maximum Dry-Bulb"]

    @wetbulb_or_dewpoint_at_maximum_drybulb.setter
    def wetbulb_or_dewpoint_at_maximum_drybulb(self, value=None):
        """  Corresponds to IDD Field `wetbulb_or_dewpoint_at_maximum_drybulb`
        Wetbulb or dewpoint temperature coincident with the maximum temperature.
        Required only if field Humidity Condition Type is "Wetbulb", "Dewpoint",
        "WetBulbProfileMultiplierSchedule", "WetBulbProfileDifferenceSchedule",
        or "WetBulbProfileDefaultMultipliers"

        Args:
            value (float): value for IDD Field `wetbulb_or_dewpoint_at_maximum_drybulb`
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
                                 'for field `wetbulb_or_dewpoint_at_maximum_drybulb`'.format(value))

        self._data["Wetbulb or DewPoint at Maximum Dry-Bulb"] = value

    @property
    def humidity_condition_day_schedule_name(self):
        """Get humidity_condition_day_schedule_name

        Returns:
            str: the value of `humidity_condition_day_schedule_name` or None if not set
        """
        return self._data["Humidity Condition Day Schedule Name"]

    @humidity_condition_day_schedule_name.setter
    def humidity_condition_day_schedule_name(self, value=None):
        """  Corresponds to IDD Field `humidity_condition_day_schedule_name`
        Only used when Humidity Condition Type is "RelativeHumiditySchedule",
        "WetBulbProfileMultiplierSchedule", or "WetBulbProfileDifferenceSchedule"
        For type "RelativeHumiditySchedule", the hour/time interval values should specify
        relative humidity (percent) from 0.0 to 100.0.
        For type "WetBulbProfileMultiplierSchedule" the hour/time interval values should specify
        the fraction (0-1) of the wet-bulb temperature range to be subtracted from the
        maximum wet-bulb temperature for each timestep in the day (units = Fraction)
        For type "WetBulbProfileDifferenceSchedule" the values should specify a number to be subtracted
        from the maximum wet-bulb temperature for each timestep in the day. (units = deltaC)

        Args:
            value (str): value for IDD Field `humidity_condition_day_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `humidity_condition_day_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `humidity_condition_day_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `humidity_condition_day_schedule_name`')

        self._data["Humidity Condition Day Schedule Name"] = value

    @property
    def humidity_ratio_at_maximum_drybulb(self):
        """Get humidity_ratio_at_maximum_drybulb

        Returns:
            float: the value of `humidity_ratio_at_maximum_drybulb` or None if not set
        """
        return self._data["Humidity Ratio at Maximum Dry-Bulb"]

    @humidity_ratio_at_maximum_drybulb.setter
    def humidity_ratio_at_maximum_drybulb(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_at_maximum_drybulb`
        Humidity ratio coincident with the maximum temperature (constant humidity ratio throughout day).
        Required only if field Humidity Condition Type is "HumidityRatio".

        Args:
            value (float): value for IDD Field `humidity_ratio_at_maximum_drybulb`
                Units: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `humidity_ratio_at_maximum_drybulb`'.format(value))

        self._data["Humidity Ratio at Maximum Dry-Bulb"] = value

    @property
    def enthalpy_at_maximum_drybulb_will_require_units_transition_(self):
        """Get enthalpy_at_maximum_drybulb_will_require_units_transition_

        Returns:
            float: the value of `enthalpy_at_maximum_drybulb_will_require_units_transition_` or None if not set
        """
        return self._data["Enthalpy at Maximum Dry-Bulb  !will require units transition."]

    @enthalpy_at_maximum_drybulb_will_require_units_transition_.setter
    def enthalpy_at_maximum_drybulb_will_require_units_transition_(self, value=None):
        """  Corresponds to IDD Field `enthalpy_at_maximum_drybulb_will_require_units_transition_`
        Enthalpy coincident with the maximum temperature.
        Required only if field Humidity Condition Type is "Enthalpy".

        Args:
            value (float): value for IDD Field `enthalpy_at_maximum_drybulb_will_require_units_transition_`
                Units: J/kg
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_at_maximum_drybulb_will_require_units_transition_`'.format(value))

        self._data["Enthalpy at Maximum Dry-Bulb  !will require units transition."] = value

    @property
    def daily_wetbulb_temperature_range(self):
        """Get daily_wetbulb_temperature_range

        Returns:
            float: the value of `daily_wetbulb_temperature_range` or None if not set
        """
        return self._data["Daily Wet-Bulb Temperature Range"]

    @daily_wetbulb_temperature_range.setter
    def daily_wetbulb_temperature_range(self, value=None):
        """  Corresponds to IDD Field `daily_wetbulb_temperature_range`
        Required only if Humidity Condition Type = "WetbulbProfileMultiplierSchedule" or
        "WetBulbProfileDefaultMultipliers"

        Args:
            value (float): value for IDD Field `daily_wetbulb_temperature_range`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `daily_wetbulb_temperature_range`'.format(value))

        self._data["Daily Wet-Bulb Temperature Range"] = value

    @property
    def barometric_pressure(self):
        """Get barometric_pressure

        Returns:
            float: the value of `barometric_pressure` or None if not set
        """
        return self._data["Barometric Pressure"]

    @barometric_pressure.setter
    def barometric_pressure(self, value=None):
        """  Corresponds to IDD Field `barometric_pressure`
        This field's value is also checked against the calculated "standard barometric pressure"
        for the location.  If out of range (>10%) or blank, then is replaced by standard value.

        Args:
            value (float): value for IDD Field `barometric_pressure`
                Units: Pa
                IP-Units: inHg
                value >= 31000.0
                value <= 120000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `barometric_pressure`'.format(value))
            if value < 31000.0:
                raise ValueError('value need to be greater or equal 31000.0 '
                                 'for field `barometric_pressure`')
            if value > 120000.0:
                raise ValueError('value need to be smaller 120000.0 '
                                 'for field `barometric_pressure`')

        self._data["Barometric Pressure"] = value

    @property
    def wind_speed(self):
        """Get wind_speed

        Returns:
            float: the value of `wind_speed` or None if not set
        """
        return self._data["Wind Speed"]

    @wind_speed.setter
    def wind_speed(self, value=None):
        """  Corresponds to IDD Field `wind_speed`

        Args:
            value (float): value for IDD Field `wind_speed`
                Units: m/s
                IP-Units: miles/hr
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
                                 'for field `wind_speed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_speed`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `wind_speed`')

        self._data["Wind Speed"] = value

    @property
    def wind_direction(self):
        """Get wind_direction

        Returns:
            float: the value of `wind_direction` or None if not set
        """
        return self._data["Wind Direction"]

    @wind_direction.setter
    def wind_direction(self, value=None):
        """  Corresponds to IDD Field `wind_direction`
        North=0.0 East=90.0
        0 and 360 are the same direction.

        Args:
            value (float): value for IDD Field `wind_direction`
                Units: deg
                value >= 0.0
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wind_direction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction`')

        self._data["Wind Direction"] = value

    @property
    def rain_indicator(self):
        """Get rain_indicator

        Returns:
            str: the value of `rain_indicator` or None if not set
        """
        return self._data["Rain Indicator"]

    @rain_indicator.setter
    def rain_indicator(self, value="No"):
        """  Corresponds to IDD Field `rain_indicator`
        Yes is raining (all day), No is not raining

        Args:
            value (str): value for IDD Field `rain_indicator`
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
                                 'for field `rain_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `rain_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `rain_indicator`')
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
                                     'field `rain_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Rain Indicator"] = value

    @property
    def snow_indicator(self):
        """Get snow_indicator

        Returns:
            str: the value of `snow_indicator` or None if not set
        """
        return self._data["Snow Indicator"]

    @snow_indicator.setter
    def snow_indicator(self, value="No"):
        """  Corresponds to IDD Field `snow_indicator`
        Yes is Snow on Ground, No is no Snow on Ground

        Args:
            value (str): value for IDD Field `snow_indicator`
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
                                 'for field `snow_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `snow_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `snow_indicator`')
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
                                     'field `snow_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Snow Indicator"] = value

    @property
    def daylight_saving_time_indicator(self):
        """Get daylight_saving_time_indicator

        Returns:
            str: the value of `daylight_saving_time_indicator` or None if not set
        """
        return self._data["Daylight Saving Time Indicator"]

    @daylight_saving_time_indicator.setter
    def daylight_saving_time_indicator(self, value="No"):
        """  Corresponds to IDD Field `daylight_saving_time_indicator`
        Yes -- use schedules modified for Daylight Saving Time Schedules.
        No - do not use schedules modified for Daylight Saving Time Schedules

        Args:
            value (str): value for IDD Field `daylight_saving_time_indicator`
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
                                 'for field `daylight_saving_time_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `daylight_saving_time_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `daylight_saving_time_indicator`')
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
                                     'field `daylight_saving_time_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Daylight Saving Time Indicator"] = value

    @property
    def solar_model_indicator(self):
        """Get solar_model_indicator

        Returns:
            str: the value of `solar_model_indicator` or None if not set
        """
        return self._data["Solar Model Indicator"]

    @solar_model_indicator.setter
    def solar_model_indicator(self, value="ASHRAEClearSky"):
        """  Corresponds to IDD Field `solar_model_indicator`

        Args:
            value (str): value for IDD Field `solar_model_indicator`
                Accepted values are:
                      - ASHRAEClearSky
                      - ZhangHuang
                      - Schedule
                      - ASHRAETau
                Default value: ASHRAEClearSky
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `solar_model_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_model_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `solar_model_indicator`')
            vals = {}
            vals["ashraeclearsky"] = "ASHRAEClearSky"
            vals["zhanghuang"] = "ZhangHuang"
            vals["schedule"] = "Schedule"
            vals["ashraetau"] = "ASHRAETau"
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
                                     'field `solar_model_indicator`'.format(value))
            value = vals[value_lower]

        self._data["Solar Model Indicator"] = value

    @property
    def beam_solar_day_schedule_name(self):
        """Get beam_solar_day_schedule_name

        Returns:
            str: the value of `beam_solar_day_schedule_name` or None if not set
        """
        return self._data["Beam Solar Day Schedule Name"]

    @beam_solar_day_schedule_name.setter
    def beam_solar_day_schedule_name(self, value=None):
        """  Corresponds to IDD Field `beam_solar_day_schedule_name`
        if Solar Model Indicator = Schedule, then beam schedule name (for day)

        Args:
            value (str): value for IDD Field `beam_solar_day_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `beam_solar_day_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `beam_solar_day_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `beam_solar_day_schedule_name`')

        self._data["Beam Solar Day Schedule Name"] = value

    @property
    def diffuse_solar_day_schedule_name(self):
        """Get diffuse_solar_day_schedule_name

        Returns:
            str: the value of `diffuse_solar_day_schedule_name` or None if not set
        """
        return self._data["Diffuse Solar Day Schedule Name"]

    @diffuse_solar_day_schedule_name.setter
    def diffuse_solar_day_schedule_name(self, value=None):
        """  Corresponds to IDD Field `diffuse_solar_day_schedule_name`
        if Solar Model Indicator = Schedule, then diffuse schedule name (for day)

        Args:
            value (str): value for IDD Field `diffuse_solar_day_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `diffuse_solar_day_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `diffuse_solar_day_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `diffuse_solar_day_schedule_name`')

        self._data["Diffuse Solar Day Schedule Name"] = value

    @property
    def ashrae_clear_sky_optical_depth_for_beam_irradiance_taub(self):
        """Get ashrae_clear_sky_optical_depth_for_beam_irradiance_taub

        Returns:
            float: the value of `ashrae_clear_sky_optical_depth_for_beam_irradiance_taub` or None if not set
        """
        return self._data["ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)"]

    @ashrae_clear_sky_optical_depth_for_beam_irradiance_taub.setter
    def ashrae_clear_sky_optical_depth_for_beam_irradiance_taub(self, value=0.0 ):
        """  Corresponds to IDD Field `ashrae_clear_sky_optical_depth_for_beam_irradiance_taub`
        Required if Solar Model Indicator = ASHRAETau

        Args:
            value (float): value for IDD Field `ashrae_clear_sky_optical_depth_for_beam_irradiance_taub`
                Units: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ashrae_clear_sky_optical_depth_for_beam_irradiance_taub`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ashrae_clear_sky_optical_depth_for_beam_irradiance_taub`')
            if value > 1.2:
                raise ValueError('value need to be smaller 1.2 '
                                 'for field `ashrae_clear_sky_optical_depth_for_beam_irradiance_taub`')

        self._data["ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)"] = value

    @property
    def ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud(self):
        """Get ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud

        Returns:
            float: the value of `ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud` or None if not set
        """
        return self._data["ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)"]

    @ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud.setter
    def ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud(self, value=0.0 ):
        """  Corresponds to IDD Field `ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud`
        Required if Solar Model Indicator = ASHRAETau

        Args:
            value (float): value for IDD Field `ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud`
                Units: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud`')
            if value > 3.0:
                raise ValueError('value need to be smaller 3.0 '
                                 'for field `ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud`')

        self._data["ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)"] = value

    @property
    def sky_clearness(self):
        """Get sky_clearness

        Returns:
            float: the value of `sky_clearness` or None if not set
        """
        return self._data["Sky Clearness"]

    @sky_clearness.setter
    def sky_clearness(self, value=0.0 ):
        """  Corresponds to IDD Field `sky_clearness`
        Used if Sky Model Indicator = ASHRAEClearSky or ZhangHuang
        0.0 is totally unclear, 1.0 is totally clear

        Args:
            value (float): value for IDD Field `sky_clearness`
                Default value: 0.0
                value >= 0.0
                value <= 1.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `sky_clearness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sky_clearness`')
            if value > 1.2:
                raise ValueError('value need to be smaller 1.2 '
                                 'for field `sky_clearness`')

        self._data["Sky Clearness"] = value

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

class SizingPeriodWeatherFileDays(object):
    """ Corresponds to IDD object `SizingPeriod:WeatherFileDays`
        Use a weather file period for design sizing calculations.
    
    """
    internal_name = "SizingPeriod:WeatherFileDays"
    field_count = 8
    required_fields = ["Name", "Begin Month", "Begin Day of Month", "End Month", "End Day of Month"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SizingPeriod:WeatherFileDays`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Begin Month"] = None
        self._data["Begin Day of Month"] = None
        self._data["End Month"] = None
        self._data["End Day of Month"] = None
        self._data["Day of Week for Start Day"] = None
        self._data["Use Weather File Daylight Saving Period"] = None
        self._data["Use Weather File Rain and Snow Indicators"] = None
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
            self.begin_month = None
        else:
            self.begin_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.begin_day_of_month = None
        else:
            self.begin_day_of_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_month = None
        else:
            self.end_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_day_of_month = None
        else:
            self.end_day_of_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_of_week_for_start_day = None
        else:
            self.day_of_week_for_start_day = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_rain_and_snow_indicators = None
        else:
            self.use_weather_file_rain_and_snow_indicators = vals[i]
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
        user supplied name for reporting

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
    def begin_month(self):
        """Get begin_month

        Returns:
            int: the value of `begin_month` or None if not set
        """
        return self._data["Begin Month"]

    @begin_month.setter
    def begin_month(self, value=None):
        """  Corresponds to IDD Field `begin_month`

        Args:
            value (int): value for IDD Field `begin_month`
                value >= 1
                value <= 12
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
                                 'for field `begin_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `begin_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `begin_month`')

        self._data["Begin Month"] = value

    @property
    def begin_day_of_month(self):
        """Get begin_day_of_month

        Returns:
            int: the value of `begin_day_of_month` or None if not set
        """
        return self._data["Begin Day of Month"]

    @begin_day_of_month.setter
    def begin_day_of_month(self, value=None):
        """  Corresponds to IDD Field `begin_day_of_month`

        Args:
            value (int): value for IDD Field `begin_day_of_month`
                value >= 1
                value <= 31
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
                                 'for field `begin_day_of_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `begin_day_of_month`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `begin_day_of_month`')

        self._data["Begin Day of Month"] = value

    @property
    def end_month(self):
        """Get end_month

        Returns:
            int: the value of `end_month` or None if not set
        """
        return self._data["End Month"]

    @end_month.setter
    def end_month(self, value=None):
        """  Corresponds to IDD Field `end_month`

        Args:
            value (int): value for IDD Field `end_month`
                value >= 1
                value <= 12
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
                                 'for field `end_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `end_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `end_month`')

        self._data["End Month"] = value

    @property
    def end_day_of_month(self):
        """Get end_day_of_month

        Returns:
            int: the value of `end_day_of_month` or None if not set
        """
        return self._data["End Day of Month"]

    @end_day_of_month.setter
    def end_day_of_month(self, value=None):
        """  Corresponds to IDD Field `end_day_of_month`

        Args:
            value (int): value for IDD Field `end_day_of_month`
                value >= 1
                value <= 31
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
                                 'for field `end_day_of_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `end_day_of_month`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `end_day_of_month`')

        self._data["End Day of Month"] = value

    @property
    def day_of_week_for_start_day(self):
        """Get day_of_week_for_start_day

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set
        """
        return self._data["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="Monday"):
        """  Corresponds to IDD Field `day_of_week_for_start_day`
        =[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay|
        |CustomDay1|CustomDay2];
        if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will apply
        to the whole period; other days (i.e., Monday) will signify a start day and
        normal sequence ofsubsequent days

        Args:
            value (str): value for IDD Field `day_of_week_for_start_day`
                Accepted values are:
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                Default value: Monday
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `day_of_week_for_start_day`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `day_of_week_for_start_day`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `day_of_week_for_start_day`')
            vals = {}
            vals["sunday"] = "Sunday"
            vals["monday"] = "Monday"
            vals["tuesday"] = "Tuesday"
            vals["wednesday"] = "Wednesday"
            vals["thursday"] = "Thursday"
            vals["friday"] = "Friday"
            vals["saturday"] = "Saturday"
            vals["summerdesignday"] = "SummerDesignDay"
            vals["winterdesignday"] = "WinterDesignDay"
            vals["customday1"] = "CustomDay1"
            vals["customday2"] = "CustomDay2"
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
                                     'field `day_of_week_for_start_day`'.format(value))
            value = vals[value_lower]

        self._data["Day of Week for Start Day"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """Get use_weather_file_daylight_saving_period

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set
        """
        return self._data["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_daylight_saving_period`
        If yes or blank, use daylight saving period as specified on Weatherfile.
        If no, do not use the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `use_weather_file_daylight_saving_period`
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
                                 'for field `use_weather_file_daylight_saving_period`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_daylight_saving_period`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_daylight_saving_period`')
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
                                     'field `use_weather_file_daylight_saving_period`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Daylight Saving Period"] = value

    @property
    def use_weather_file_rain_and_snow_indicators(self):
        """Get use_weather_file_rain_and_snow_indicators

        Returns:
            str: the value of `use_weather_file_rain_and_snow_indicators` or None if not set
        """
        return self._data["Use Weather File Rain and Snow Indicators"]

    @use_weather_file_rain_and_snow_indicators.setter
    def use_weather_file_rain_and_snow_indicators(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_rain_and_snow_indicators`

        Args:
            value (str): value for IDD Field `use_weather_file_rain_and_snow_indicators`
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
                                 'for field `use_weather_file_rain_and_snow_indicators`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_rain_and_snow_indicators`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_rain_and_snow_indicators`')
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
                                     'field `use_weather_file_rain_and_snow_indicators`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Rain and Snow Indicators"] = value

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

class SizingPeriodWeatherFileConditionType(object):
    """ Corresponds to IDD object `SizingPeriod:WeatherFileConditionType`
        Use a weather file period for design sizing calculations.
        EPW weather files are created with typical and extreme periods
        created heuristically from the weather file data.  For more
        details on these periods, see AuxiliaryPrograms document.
    
    """
    internal_name = "SizingPeriod:WeatherFileConditionType"
    field_count = 5
    required_fields = ["Name", "Period Selection"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SizingPeriod:WeatherFileConditionType`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Period Selection"] = None
        self._data["Day of Week for Start Day"] = None
        self._data["Use Weather File Daylight Saving Period"] = None
        self._data["Use Weather File Rain and Snow Indicators"] = None
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
            self.period_selection = None
        else:
            self.period_selection = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_of_week_for_start_day = None
        else:
            self.day_of_week_for_start_day = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_rain_and_snow_indicators = None
        else:
            self.use_weather_file_rain_and_snow_indicators = vals[i]
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
        user supplied name for reporting

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
    def period_selection(self):
        """Get period_selection

        Returns:
            str: the value of `period_selection` or None if not set
        """
        return self._data["Period Selection"]

    @period_selection.setter
    def period_selection(self, value=None):
        """  Corresponds to IDD Field `period_selection`
        Following is a list of all possible types of Extreme and Typical periods that
        might be identified in the Weather File. Not all possible types are available
        for all weather files.

        Args:
            value (str): value for IDD Field `period_selection`
                Accepted values are:
                      - SummerExtreme
                      - SummerTypical
                      - WinterExtreme
                      - WinterTypical
                      - AutumnTypical
                      - SpringTypical
                      - WetSeason
                      - DrySeason
                      - NoDrySeason
                      - NoWetSeason
                      - TropicalHot
                      - TropicalCold
                      - NoDrySeasonMax
                      - NoDrySeasonMin
                      - NoWetSeasonMax
                      - NoWetSeasonMin
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `period_selection`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `period_selection`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `period_selection`')
            vals = {}
            vals["summerextreme"] = "SummerExtreme"
            vals["summertypical"] = "SummerTypical"
            vals["winterextreme"] = "WinterExtreme"
            vals["wintertypical"] = "WinterTypical"
            vals["autumntypical"] = "AutumnTypical"
            vals["springtypical"] = "SpringTypical"
            vals["wetseason"] = "WetSeason"
            vals["dryseason"] = "DrySeason"
            vals["nodryseason"] = "NoDrySeason"
            vals["nowetseason"] = "NoWetSeason"
            vals["tropicalhot"] = "TropicalHot"
            vals["tropicalcold"] = "TropicalCold"
            vals["nodryseasonmax"] = "NoDrySeasonMax"
            vals["nodryseasonmin"] = "NoDrySeasonMin"
            vals["nowetseasonmax"] = "NoWetSeasonMax"
            vals["nowetseasonmin"] = "NoWetSeasonMin"
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
                                     'field `period_selection`'.format(value))
            value = vals[value_lower]

        self._data["Period Selection"] = value

    @property
    def day_of_week_for_start_day(self):
        """Get day_of_week_for_start_day

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set
        """
        return self._data["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="Monday"):
        """  Corresponds to IDD Field `day_of_week_for_start_day`
        =[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay|
        |CustomDay1|CustomDay2];
        if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will apply
        to the whole period; other days (i.e., Monday) will signify a start day and
        normal sequence ofsubsequent days

        Args:
            value (str): value for IDD Field `day_of_week_for_start_day`
                Accepted values are:
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                Default value: Monday
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `day_of_week_for_start_day`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `day_of_week_for_start_day`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `day_of_week_for_start_day`')
            vals = {}
            vals["sunday"] = "Sunday"
            vals["monday"] = "Monday"
            vals["tuesday"] = "Tuesday"
            vals["wednesday"] = "Wednesday"
            vals["thursday"] = "Thursday"
            vals["friday"] = "Friday"
            vals["saturday"] = "Saturday"
            vals["summerdesignday"] = "SummerDesignDay"
            vals["winterdesignday"] = "WinterDesignDay"
            vals["customday1"] = "CustomDay1"
            vals["customday2"] = "CustomDay2"
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
                                     'field `day_of_week_for_start_day`'.format(value))
            value = vals[value_lower]

        self._data["Day of Week for Start Day"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """Get use_weather_file_daylight_saving_period

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set
        """
        return self._data["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_daylight_saving_period`
        If yes or blank, use daylight saving period as specified on Weatherfile.
        If no, do not use the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `use_weather_file_daylight_saving_period`
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
                                 'for field `use_weather_file_daylight_saving_period`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_daylight_saving_period`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_daylight_saving_period`')
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
                                     'field `use_weather_file_daylight_saving_period`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Daylight Saving Period"] = value

    @property
    def use_weather_file_rain_and_snow_indicators(self):
        """Get use_weather_file_rain_and_snow_indicators

        Returns:
            str: the value of `use_weather_file_rain_and_snow_indicators` or None if not set
        """
        return self._data["Use Weather File Rain and Snow Indicators"]

    @use_weather_file_rain_and_snow_indicators.setter
    def use_weather_file_rain_and_snow_indicators(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_rain_and_snow_indicators`

        Args:
            value (str): value for IDD Field `use_weather_file_rain_and_snow_indicators`
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
                                 'for field `use_weather_file_rain_and_snow_indicators`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_rain_and_snow_indicators`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_rain_and_snow_indicators`')
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
                                     'field `use_weather_file_rain_and_snow_indicators`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Rain and Snow Indicators"] = value

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

class RunPeriod(object):
    """ Corresponds to IDD object `RunPeriod`
        Specified a range of dates and other parameters for a weather file simulation.
        Multiple run periods may be input, but they may not overlap.
    
    """
    internal_name = "RunPeriod"
    field_count = 14
    required_fields = ["Begin Month", "Begin Day of Month", "End Month", "End Day of Month"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RunPeriod`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Begin Month"] = None
        self._data["Begin Day of Month"] = None
        self._data["End Month"] = None
        self._data["End Day of Month"] = None
        self._data["Day of Week for Start Day"] = None
        self._data["Use Weather File Holidays and Special Days"] = None
        self._data["Use Weather File Daylight Saving Period"] = None
        self._data["Apply Weekend Holiday Rule"] = None
        self._data["Use Weather File Rain Indicators"] = None
        self._data["Use Weather File Snow Indicators"] = None
        self._data["Number of Times Runperiod to be Repeated"] = None
        self._data["Increment Day of Week on repeat"] = None
        self._data["Start Year"] = None
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
            self.begin_month = None
        else:
            self.begin_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.begin_day_of_month = None
        else:
            self.begin_day_of_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_month = None
        else:
            self.end_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_day_of_month = None
        else:
            self.end_day_of_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_of_week_for_start_day = None
        else:
            self.day_of_week_for_start_day = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_holidays_and_special_days = None
        else:
            self.use_weather_file_holidays_and_special_days = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.apply_weekend_holiday_rule = None
        else:
            self.apply_weekend_holiday_rule = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_rain_indicators = None
        else:
            self.use_weather_file_rain_indicators = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_snow_indicators = None
        else:
            self.use_weather_file_snow_indicators = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_times_runperiod_to_be_repeated = None
        else:
            self.number_of_times_runperiod_to_be_repeated = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.increment_day_of_week_on_repeat = None
        else:
            self.increment_day_of_week_on_repeat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.start_year = None
        else:
            self.start_year = vals[i]
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
        descriptive name (used in reporting mainly)
        if blank, weather file title is used.  if not blank, must be unique

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
    def begin_month(self):
        """Get begin_month

        Returns:
            int: the value of `begin_month` or None if not set
        """
        return self._data["Begin Month"]

    @begin_month.setter
    def begin_month(self, value=None):
        """  Corresponds to IDD Field `begin_month`

        Args:
            value (int): value for IDD Field `begin_month`
                value >= 1
                value <= 12
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
                                 'for field `begin_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `begin_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `begin_month`')

        self._data["Begin Month"] = value

    @property
    def begin_day_of_month(self):
        """Get begin_day_of_month

        Returns:
            int: the value of `begin_day_of_month` or None if not set
        """
        return self._data["Begin Day of Month"]

    @begin_day_of_month.setter
    def begin_day_of_month(self, value=None):
        """  Corresponds to IDD Field `begin_day_of_month`

        Args:
            value (int): value for IDD Field `begin_day_of_month`
                value >= 1
                value <= 31
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
                                 'for field `begin_day_of_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `begin_day_of_month`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `begin_day_of_month`')

        self._data["Begin Day of Month"] = value

    @property
    def end_month(self):
        """Get end_month

        Returns:
            int: the value of `end_month` or None if not set
        """
        return self._data["End Month"]

    @end_month.setter
    def end_month(self, value=None):
        """  Corresponds to IDD Field `end_month`

        Args:
            value (int): value for IDD Field `end_month`
                value >= 1
                value <= 12
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
                                 'for field `end_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `end_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `end_month`')

        self._data["End Month"] = value

    @property
    def end_day_of_month(self):
        """Get end_day_of_month

        Returns:
            int: the value of `end_day_of_month` or None if not set
        """
        return self._data["End Day of Month"]

    @end_day_of_month.setter
    def end_day_of_month(self, value=None):
        """  Corresponds to IDD Field `end_day_of_month`

        Args:
            value (int): value for IDD Field `end_day_of_month`
                value >= 1
                value <= 31
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
                                 'for field `end_day_of_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `end_day_of_month`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `end_day_of_month`')

        self._data["End Day of Month"] = value

    @property
    def day_of_week_for_start_day(self):
        """Get day_of_week_for_start_day

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set
        """
        return self._data["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="UseWeatherFile"):
        """  Corresponds to IDD Field `day_of_week_for_start_day`
        =<blank - use WeatherFile>|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday];

        Args:
            value (str): value for IDD Field `day_of_week_for_start_day`
                Accepted values are:
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - UseWeatherFile
                Default value: UseWeatherFile
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `day_of_week_for_start_day`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `day_of_week_for_start_day`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `day_of_week_for_start_day`')
            vals = {}
            vals["sunday"] = "Sunday"
            vals["monday"] = "Monday"
            vals["tuesday"] = "Tuesday"
            vals["wednesday"] = "Wednesday"
            vals["thursday"] = "Thursday"
            vals["friday"] = "Friday"
            vals["saturday"] = "Saturday"
            vals["useweatherfile"] = "UseWeatherFile"
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
                                     'field `day_of_week_for_start_day`'.format(value))
            value = vals[value_lower]

        self._data["Day of Week for Start Day"] = value

    @property
    def use_weather_file_holidays_and_special_days(self):
        """Get use_weather_file_holidays_and_special_days

        Returns:
            str: the value of `use_weather_file_holidays_and_special_days` or None if not set
        """
        return self._data["Use Weather File Holidays and Special Days"]

    @use_weather_file_holidays_and_special_days.setter
    def use_weather_file_holidays_and_special_days(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_holidays_and_special_days`
        If yes or blank, use holidays as specified on Weatherfile.
        If no, do not use the holidays specified on the Weatherfile.
        Note: You can still specify holidays/special days using the RunPeriodControl:SpecialDays object(s).

        Args:
            value (str): value for IDD Field `use_weather_file_holidays_and_special_days`
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
                                 'for field `use_weather_file_holidays_and_special_days`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_holidays_and_special_days`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_holidays_and_special_days`')
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
                                     'field `use_weather_file_holidays_and_special_days`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Holidays and Special Days"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """Get use_weather_file_daylight_saving_period

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set
        """
        return self._data["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_daylight_saving_period`
        If yes or blank, use daylight saving period as specified on Weatherfile.
        If no, do not use the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `use_weather_file_daylight_saving_period`
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
                                 'for field `use_weather_file_daylight_saving_period`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_daylight_saving_period`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_daylight_saving_period`')
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
                                     'field `use_weather_file_daylight_saving_period`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Daylight Saving Period"] = value

    @property
    def apply_weekend_holiday_rule(self):
        """Get apply_weekend_holiday_rule

        Returns:
            str: the value of `apply_weekend_holiday_rule` or None if not set
        """
        return self._data["Apply Weekend Holiday Rule"]

    @apply_weekend_holiday_rule.setter
    def apply_weekend_holiday_rule(self, value="No"):
        """  Corresponds to IDD Field `apply_weekend_holiday_rule`
        if yes and single day holiday falls on weekend, "holiday" occurs on following Monday

        Args:
            value (str): value for IDD Field `apply_weekend_holiday_rule`
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
                                 'for field `apply_weekend_holiday_rule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `apply_weekend_holiday_rule`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `apply_weekend_holiday_rule`')
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
                                     'field `apply_weekend_holiday_rule`'.format(value))
            value = vals[value_lower]

        self._data["Apply Weekend Holiday Rule"] = value

    @property
    def use_weather_file_rain_indicators(self):
        """Get use_weather_file_rain_indicators

        Returns:
            str: the value of `use_weather_file_rain_indicators` or None if not set
        """
        return self._data["Use Weather File Rain Indicators"]

    @use_weather_file_rain_indicators.setter
    def use_weather_file_rain_indicators(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_rain_indicators`

        Args:
            value (str): value for IDD Field `use_weather_file_rain_indicators`
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
                                 'for field `use_weather_file_rain_indicators`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_rain_indicators`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_rain_indicators`')
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
                                     'field `use_weather_file_rain_indicators`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Rain Indicators"] = value

    @property
    def use_weather_file_snow_indicators(self):
        """Get use_weather_file_snow_indicators

        Returns:
            str: the value of `use_weather_file_snow_indicators` or None if not set
        """
        return self._data["Use Weather File Snow Indicators"]

    @use_weather_file_snow_indicators.setter
    def use_weather_file_snow_indicators(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_snow_indicators`

        Args:
            value (str): value for IDD Field `use_weather_file_snow_indicators`
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
                                 'for field `use_weather_file_snow_indicators`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_snow_indicators`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_snow_indicators`')
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
                                     'field `use_weather_file_snow_indicators`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Snow Indicators"] = value

    @property
    def number_of_times_runperiod_to_be_repeated(self):
        """Get number_of_times_runperiod_to_be_repeated

        Returns:
            int: the value of `number_of_times_runperiod_to_be_repeated` or None if not set
        """
        return self._data["Number of Times Runperiod to be Repeated"]

    @number_of_times_runperiod_to_be_repeated.setter
    def number_of_times_runperiod_to_be_repeated(self, value=1 ):
        """  Corresponds to IDD Field `number_of_times_runperiod_to_be_repeated`

        Args:
            value (int): value for IDD Field `number_of_times_runperiod_to_be_repeated`
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
                                 'for field `number_of_times_runperiod_to_be_repeated`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_times_runperiod_to_be_repeated`')

        self._data["Number of Times Runperiod to be Repeated"] = value

    @property
    def increment_day_of_week_on_repeat(self):
        """Get increment_day_of_week_on_repeat

        Returns:
            str: the value of `increment_day_of_week_on_repeat` or None if not set
        """
        return self._data["Increment Day of Week on repeat"]

    @increment_day_of_week_on_repeat.setter
    def increment_day_of_week_on_repeat(self, value="Yes"):
        """  Corresponds to IDD Field `increment_day_of_week_on_repeat`

        Args:
            value (str): value for IDD Field `increment_day_of_week_on_repeat`
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
                                 'for field `increment_day_of_week_on_repeat`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `increment_day_of_week_on_repeat`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `increment_day_of_week_on_repeat`')
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
                                     'field `increment_day_of_week_on_repeat`'.format(value))
            value = vals[value_lower]

        self._data["Increment Day of Week on repeat"] = value

    @property
    def start_year(self):
        """Get start_year

        Returns:
            float: the value of `start_year` or None if not set
        """
        return self._data["Start Year"]

    @start_year.setter
    def start_year(self, value=None):
        """  Corresponds to IDD Field `start_year`
        this is the start year for the start date.  If the leap year is "Yes" in the weather file header
        (that is HOLIDAYS/SPECIAL DAYS header first field), then any year which is a leap year will assume
        there will be a Feb 29. A repeat of this runperiod will automatically increment the year.

        Args:
            value (float): value for IDD Field `start_year`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `start_year`'.format(value))

        self._data["Start Year"] = value

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

class RunPeriodCustomRange(object):
    """ Corresponds to IDD object `RunPeriod:CustomRange`
        run simulation for a custom created weather file
    
    """
    internal_name = "RunPeriod:CustomRange"
    field_count = 13
    required_fields = ["Begin Month", "Begin Day of Month", "Begin Year", "End Month", "End Day of Month", "End Year"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RunPeriod:CustomRange`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Begin Month"] = None
        self._data["Begin Day of Month"] = None
        self._data["Begin Year"] = None
        self._data["End Month"] = None
        self._data["End Day of Month"] = None
        self._data["End Year"] = None
        self._data["Day of Week for Start Day"] = None
        self._data["Use Weather File Holidays and Special Days"] = None
        self._data["Use Weather File Daylight Saving Period"] = None
        self._data["Apply Weekend Holiday Rule"] = None
        self._data["Use Weather File Rain Indicators"] = None
        self._data["Use Weather File Snow Indicators"] = None
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
            self.begin_month = None
        else:
            self.begin_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.begin_day_of_month = None
        else:
            self.begin_day_of_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.begin_year = None
        else:
            self.begin_year = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_month = None
        else:
            self.end_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_day_of_month = None
        else:
            self.end_day_of_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_year = None
        else:
            self.end_year = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_of_week_for_start_day = None
        else:
            self.day_of_week_for_start_day = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_holidays_and_special_days = None
        else:
            self.use_weather_file_holidays_and_special_days = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.apply_weekend_holiday_rule = None
        else:
            self.apply_weekend_holiday_rule = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_rain_indicators = None
        else:
            self.use_weather_file_rain_indicators = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.use_weather_file_snow_indicators = None
        else:
            self.use_weather_file_snow_indicators = vals[i]
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
        descriptive name (used in reporting mainly)
        if blank, weather file title is used.  if not blank, must be unique

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
    def begin_month(self):
        """Get begin_month

        Returns:
            int: the value of `begin_month` or None if not set
        """
        return self._data["Begin Month"]

    @begin_month.setter
    def begin_month(self, value=None):
        """  Corresponds to IDD Field `begin_month`

        Args:
            value (int): value for IDD Field `begin_month`
                value >= 1
                value <= 12
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
                                 'for field `begin_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `begin_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `begin_month`')

        self._data["Begin Month"] = value

    @property
    def begin_day_of_month(self):
        """Get begin_day_of_month

        Returns:
            int: the value of `begin_day_of_month` or None if not set
        """
        return self._data["Begin Day of Month"]

    @begin_day_of_month.setter
    def begin_day_of_month(self, value=None):
        """  Corresponds to IDD Field `begin_day_of_month`

        Args:
            value (int): value for IDD Field `begin_day_of_month`
                value >= 1
                value <= 31
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
                                 'for field `begin_day_of_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `begin_day_of_month`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `begin_day_of_month`')

        self._data["Begin Day of Month"] = value

    @property
    def begin_year(self):
        """Get begin_year

        Returns:
            float: the value of `begin_year` or None if not set
        """
        return self._data["Begin Year"]

    @begin_year.setter
    def begin_year(self, value=None):
        """  Corresponds to IDD Field `begin_year`
        must be start year of this date on weather file

        Args:
            value (float): value for IDD Field `begin_year`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `begin_year`'.format(value))

        self._data["Begin Year"] = value

    @property
    def end_month(self):
        """Get end_month

        Returns:
            int: the value of `end_month` or None if not set
        """
        return self._data["End Month"]

    @end_month.setter
    def end_month(self, value=None):
        """  Corresponds to IDD Field `end_month`

        Args:
            value (int): value for IDD Field `end_month`
                value >= 1
                value <= 12
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
                                 'for field `end_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `end_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `end_month`')

        self._data["End Month"] = value

    @property
    def end_day_of_month(self):
        """Get end_day_of_month

        Returns:
            int: the value of `end_day_of_month` or None if not set
        """
        return self._data["End Day of Month"]

    @end_day_of_month.setter
    def end_day_of_month(self, value=None):
        """  Corresponds to IDD Field `end_day_of_month`

        Args:
            value (int): value for IDD Field `end_day_of_month`
                value >= 1
                value <= 31
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
                                 'for field `end_day_of_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `end_day_of_month`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `end_day_of_month`')

        self._data["End Day of Month"] = value

    @property
    def end_year(self):
        """Get end_year

        Returns:
            float: the value of `end_year` or None if not set
        """
        return self._data["End Year"]

    @end_year.setter
    def end_year(self, value=None):
        """  Corresponds to IDD Field `end_year`
        must be end year of this date on weather file

        Args:
            value (float): value for IDD Field `end_year`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `end_year`'.format(value))

        self._data["End Year"] = value

    @property
    def day_of_week_for_start_day(self):
        """Get day_of_week_for_start_day

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set
        """
        return self._data["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="UseWeatherFile"):
        """  Corresponds to IDD Field `day_of_week_for_start_day`
        =<blank - use WeatherFile>|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday];

        Args:
            value (str): value for IDD Field `day_of_week_for_start_day`
                Accepted values are:
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - UseWeatherFile
                Default value: UseWeatherFile
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `day_of_week_for_start_day`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `day_of_week_for_start_day`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `day_of_week_for_start_day`')
            vals = {}
            vals["sunday"] = "Sunday"
            vals["monday"] = "Monday"
            vals["tuesday"] = "Tuesday"
            vals["wednesday"] = "Wednesday"
            vals["thursday"] = "Thursday"
            vals["friday"] = "Friday"
            vals["saturday"] = "Saturday"
            vals["useweatherfile"] = "UseWeatherFile"
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
                                     'field `day_of_week_for_start_day`'.format(value))
            value = vals[value_lower]

        self._data["Day of Week for Start Day"] = value

    @property
    def use_weather_file_holidays_and_special_days(self):
        """Get use_weather_file_holidays_and_special_days

        Returns:
            str: the value of `use_weather_file_holidays_and_special_days` or None if not set
        """
        return self._data["Use Weather File Holidays and Special Days"]

    @use_weather_file_holidays_and_special_days.setter
    def use_weather_file_holidays_and_special_days(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_holidays_and_special_days`
        If yes or blank, use holidays as specified on Weatherfile.
        If no, do not use the holidays specified on the Weatherfile.
        Note: You can still specify holidays/special days using the RunPeriodControl:SpecialDays object(s).

        Args:
            value (str): value for IDD Field `use_weather_file_holidays_and_special_days`
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
                                 'for field `use_weather_file_holidays_and_special_days`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_holidays_and_special_days`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_holidays_and_special_days`')
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
                                     'field `use_weather_file_holidays_and_special_days`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Holidays and Special Days"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """Get use_weather_file_daylight_saving_period

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set
        """
        return self._data["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_daylight_saving_period`
        If yes or blank, use daylight saving period as specified on Weatherfile.
        If no, do not use the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `use_weather_file_daylight_saving_period`
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
                                 'for field `use_weather_file_daylight_saving_period`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_daylight_saving_period`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_daylight_saving_period`')
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
                                     'field `use_weather_file_daylight_saving_period`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Daylight Saving Period"] = value

    @property
    def apply_weekend_holiday_rule(self):
        """Get apply_weekend_holiday_rule

        Returns:
            str: the value of `apply_weekend_holiday_rule` or None if not set
        """
        return self._data["Apply Weekend Holiday Rule"]

    @apply_weekend_holiday_rule.setter
    def apply_weekend_holiday_rule(self, value="No"):
        """  Corresponds to IDD Field `apply_weekend_holiday_rule`
        if yes and single day holiday falls on weekend, "holiday" occurs on following Monday

        Args:
            value (str): value for IDD Field `apply_weekend_holiday_rule`
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
                                 'for field `apply_weekend_holiday_rule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `apply_weekend_holiday_rule`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `apply_weekend_holiday_rule`')
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
                                     'field `apply_weekend_holiday_rule`'.format(value))
            value = vals[value_lower]

        self._data["Apply Weekend Holiday Rule"] = value

    @property
    def use_weather_file_rain_indicators(self):
        """Get use_weather_file_rain_indicators

        Returns:
            str: the value of `use_weather_file_rain_indicators` or None if not set
        """
        return self._data["Use Weather File Rain Indicators"]

    @use_weather_file_rain_indicators.setter
    def use_weather_file_rain_indicators(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_rain_indicators`

        Args:
            value (str): value for IDD Field `use_weather_file_rain_indicators`
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
                                 'for field `use_weather_file_rain_indicators`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_rain_indicators`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_rain_indicators`')
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
                                     'field `use_weather_file_rain_indicators`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Rain Indicators"] = value

    @property
    def use_weather_file_snow_indicators(self):
        """Get use_weather_file_snow_indicators

        Returns:
            str: the value of `use_weather_file_snow_indicators` or None if not set
        """
        return self._data["Use Weather File Snow Indicators"]

    @use_weather_file_snow_indicators.setter
    def use_weather_file_snow_indicators(self, value="Yes"):
        """  Corresponds to IDD Field `use_weather_file_snow_indicators`

        Args:
            value (str): value for IDD Field `use_weather_file_snow_indicators`
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
                                 'for field `use_weather_file_snow_indicators`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_weather_file_snow_indicators`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `use_weather_file_snow_indicators`')
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
                                     'field `use_weather_file_snow_indicators`'.format(value))
            value = vals[value_lower]

        self._data["Use Weather File Snow Indicators"] = value

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

class RunPeriodControlSpecialDays(object):
    """ Corresponds to IDD object `RunPeriodControl:SpecialDays`
        This object sets up holidays/special days to be used during weather file
        run periods.  (These are not used with SizingPeriod:* objects.)
        Depending on the value in the run period, days on the weather file may also
        be used.  However, the weather file specification will take precedence over
        any specification shown here.  (No error message on duplicate days or overlapping
        days).
    
    """
    internal_name = "RunPeriodControl:SpecialDays"
    field_count = 4
    required_fields = ["Name", "Start Date", "Special Day Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RunPeriodControl:SpecialDays`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Start Date"] = None
        self._data["Duration"] = None
        self._data["Special Day Type"] = None
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
            self.start_date = None
        else:
            self.start_date = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.duration = None
        else:
            self.duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.special_day_type = None
        else:
            self.special_day_type = vals[i]
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
    def start_date(self):
        """Get start_date

        Returns:
            str: the value of `start_date` or None if not set
        """
        return self._data["Start Date"]

    @start_date.setter
    def start_date(self, value=None):
        """  Corresponds to IDD Field `start_date`
        Dates can be several formats:
        <number>/<number>  (month/day)
        <number> <Month>
        <Month> <number>
        <Nth> <Weekday> in <Month)
        Last <WeekDay> in <Month>
        <Month> can be January, February, March, April, May, June, July, August, September, October, November, December
        Months can be the first 3 letters of the month
        <Weekday> can be Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        <Nth> can be 1 or 1st, 2 or 2nd, etc. up to 5(?)

        Args:
            value (str): value for IDD Field `start_date`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `start_date`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `start_date`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `start_date`')

        self._data["Start Date"] = value

    @property
    def duration(self):
        """Get duration

        Returns:
            float: the value of `duration` or None if not set
        """
        return self._data["Duration"]

    @duration.setter
    def duration(self, value=1.0 ):
        """  Corresponds to IDD Field `duration`

        Args:
            value (float): value for IDD Field `duration`
                Units: days
                Default value: 1.0
                value >= 1.0
                value <= 366.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `duration`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `duration`')
            if value > 366.0:
                raise ValueError('value need to be smaller 366.0 '
                                 'for field `duration`')

        self._data["Duration"] = value

    @property
    def special_day_type(self):
        """Get special_day_type

        Returns:
            str: the value of `special_day_type` or None if not set
        """
        return self._data["Special Day Type"]

    @special_day_type.setter
    def special_day_type(self, value="Holiday"):
        """  Corresponds to IDD Field `special_day_type`
        Special Day Type selects the schedules appropriate for each day so labeled

        Args:
            value (str): value for IDD Field `special_day_type`
                Accepted values are:
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                Default value: Holiday
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `special_day_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `special_day_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `special_day_type`')
            vals = {}
            vals["holiday"] = "Holiday"
            vals["summerdesignday"] = "SummerDesignDay"
            vals["winterdesignday"] = "WinterDesignDay"
            vals["customday1"] = "CustomDay1"
            vals["customday2"] = "CustomDay2"
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
                                     'field `special_day_type`'.format(value))
            value = vals[value_lower]

        self._data["Special Day Type"] = value

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

class RunPeriodControlDaylightSavingTime(object):
    """ Corresponds to IDD object `RunPeriodControl:DaylightSavingTime`
        This object sets up the daylight saving time period for any RunPeriod.
        Ignores any daylight saving time period on the weather file and uses this definition.
        These are not used with SizingPeriod:DesignDay objects.
        Use with SizingPeriod:WeatherFileDays object can be controlled in that object.
    
    """
    internal_name = "RunPeriodControl:DaylightSavingTime"
    field_count = 2
    required_fields = ["Start Date", "End Date"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RunPeriodControl:DaylightSavingTime`
        """
        self._data = OrderedDict()
        self._data["Start Date"] = None
        self._data["End Date"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.start_date = None
        else:
            self.start_date = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.end_date = None
        else:
            self.end_date = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def start_date(self):
        """Get start_date

        Returns:
            str: the value of `start_date` or None if not set
        """
        return self._data["Start Date"]

    @start_date.setter
    def start_date(self, value=None):
        """  Corresponds to IDD Field `start_date`

        Args:
            value (str): value for IDD Field `start_date`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `start_date`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `start_date`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `start_date`')

        self._data["Start Date"] = value

    @property
    def end_date(self):
        """Get end_date

        Returns:
            str: the value of `end_date` or None if not set
        """
        return self._data["End Date"]

    @end_date.setter
    def end_date(self, value=None):
        """  Corresponds to IDD Field `end_date`
        Dates can be several formats:
        <number>/<number>  (month/day)
        <number> <Month>
        <Month> <number>
        <Nth> <Weekday> in <Month)
        Last <WeekDay> in <Month>
        <Month> can be January, February, March, April, May, June, July, August, September, October, November, December
        Months can be the first 3 letters of the month
        <Weekday> can be Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        <Nth> can be 1 or 1st, 2 or 2nd, etc. up to 5(?)

        Args:
            value (str): value for IDD Field `end_date`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `end_date`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `end_date`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `end_date`')

        self._data["End Date"] = value

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

class WeatherPropertySkyTemperature(object):
    """ Corresponds to IDD object `WeatherProperty:SkyTemperature`
        This object is used to override internal sky temperature calculations.
    
    """
    internal_name = "WeatherProperty:SkyTemperature"
    field_count = 3
    required_fields = ["Calculation Type", "Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WeatherProperty:SkyTemperature`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Calculation Type"] = None
        self._data["Schedule Name"] = None
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
            self.calculation_type = None
        else:
            self.calculation_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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
        blank in this field will apply to all run periods (that is, all objects=
        SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or RunPeriod
        otherwise, this name must match one of the environment object names.

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
    def calculation_type(self):
        """Get calculation_type

        Returns:
            str: the value of `calculation_type` or None if not set
        """
        return self._data["Calculation Type"]

    @calculation_type.setter
    def calculation_type(self, value=None):
        """  Corresponds to IDD Field `calculation_type`

        Args:
            value (str): value for IDD Field `calculation_type`
                Accepted values are:
                      - ScheduleValue
                      - DifferenceScheduleDryBulbValue
                      - DifferenceScheduleDewPointValue
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `calculation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `calculation_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `calculation_type`')
            vals = {}
            vals["schedulevalue"] = "ScheduleValue"
            vals["differencescheduledrybulbvalue"] = "DifferenceScheduleDryBulbValue"
            vals["differencescheduledewpointvalue"] = "DifferenceScheduleDewPointValue"
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
                                     'field `calculation_type`'.format(value))
            value = vals[value_lower]

        self._data["Calculation Type"] = value

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
        if name matches a SizingPeriod:DesignDay, put in a day schedule of this name
        if name is for a SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or
        RunPeriod, put in a full year schedule that covers the appropriate days.

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

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

class SiteWeatherStation(object):
    """ Corresponds to IDD object `Site:WeatherStation`
        This object should only be used for non-standard weather data.  Standard weather data
        such as TMY2, IWEC, and ASHRAE design day data are all measured at the
        default conditions and do not require this object.
    
    """
    internal_name = "Site:WeatherStation"
    field_count = 4
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:WeatherStation`
        """
        self._data = OrderedDict()
        self._data["Wind Sensor Height Above Ground"] = None
        self._data["Wind Speed Profile Exponent"] = None
        self._data["Wind Speed Profile Boundary Layer Thickness"] = None
        self._data["Air Temperature Sensor Height Above Ground"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.wind_sensor_height_above_ground = None
        else:
            self.wind_sensor_height_above_ground = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_speed_profile_exponent = None
        else:
            self.wind_speed_profile_exponent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_speed_profile_boundary_layer_thickness = None
        else:
            self.wind_speed_profile_boundary_layer_thickness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_temperature_sensor_height_above_ground = None
        else:
            self.air_temperature_sensor_height_above_ground = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                Units: m
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
                Units: m
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
                Units: m
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

class SiteHeightVariation(object):
    """ Corresponds to IDD object `Site:HeightVariation`
        This object is used if the user requires advanced control over height-dependent
        variations in wind speed and temperature.  When this object is not present, the default model
        for temperature dependence on height is used, and the wind speed is modeled according
        to the Terrain field of the BUILDING object.
    
    """
    internal_name = "Site:HeightVariation"
    field_count = 3
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:HeightVariation`
        """
        self._data = OrderedDict()
        self._data["Wind Speed Profile Exponent"] = None
        self._data["Wind Speed Profile Boundary Layer Thickness"] = None
        self._data["Air Temperature Gradient Coefficient"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.wind_speed_profile_exponent = None
        else:
            self.wind_speed_profile_exponent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_speed_profile_boundary_layer_thickness = None
        else:
            self.wind_speed_profile_boundary_layer_thickness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_temperature_gradient_coefficient = None
        else:
            self.air_temperature_gradient_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                Units: m
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
                Units: K/m
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
    required_fields = ["January Ground Temperature", "February Ground Temperature", "March Ground Temperature", "April Ground Temperature", "May Ground Temperature", "June Ground Temperature", "July Ground Temperature", "August Ground Temperature", "September Ground Temperature", "October Ground Temperature", "November Ground Temperature", "December Ground Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:GroundTemperature:BuildingSurface`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.january_ground_temperature = None
        else:
            self.january_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.february_ground_temperature = None
        else:
            self.february_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.march_ground_temperature = None
        else:
            self.march_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.april_ground_temperature = None
        else:
            self.april_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.may_ground_temperature = None
        else:
            self.may_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.june_ground_temperature = None
        else:
            self.june_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.july_ground_temperature = None
        else:
            self.july_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.august_ground_temperature = None
        else:
            self.august_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.september_ground_temperature = None
        else:
            self.september_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.october_ground_temperature = None
        else:
            self.october_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.november_ground_temperature = None
        else:
            self.november_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.december_ground_temperature = None
        else:
            self.december_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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

class SiteGroundTemperatureFcfactorMethod(object):
    """ Corresponds to IDD object `Site:GroundTemperature:FCfactorMethod`
        These temperatures are specifically for underground walls and ground floors
        defined with the C-factor and F-factor methods, and should be close to the
        monthly average outdoor air temperature delayed by 3 months for the location.
    
    """
    internal_name = "Site:GroundTemperature:FCfactorMethod"
    field_count = 12
    required_fields = ["January Ground Temperature", "February Ground Temperature", "March Ground Temperature", "April Ground Temperature", "May Ground Temperature", "June Ground Temperature", "July Ground Temperature", "August Ground Temperature", "September Ground Temperature", "October Ground Temperature", "November Ground Temperature", "December Ground Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:GroundTemperature:FCfactorMethod`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.january_ground_temperature = None
        else:
            self.january_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.february_ground_temperature = None
        else:
            self.february_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.march_ground_temperature = None
        else:
            self.march_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.april_ground_temperature = None
        else:
            self.april_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.may_ground_temperature = None
        else:
            self.may_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.june_ground_temperature = None
        else:
            self.june_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.july_ground_temperature = None
        else:
            self.july_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.august_ground_temperature = None
        else:
            self.august_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.september_ground_temperature = None
        else:
            self.september_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.october_ground_temperature = None
        else:
            self.october_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.november_ground_temperature = None
        else:
            self.november_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.december_ground_temperature = None
        else:
            self.december_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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

class SiteGroundTemperatureShallow(object):
    """ Corresponds to IDD object `Site:GroundTemperature:Shallow`
        These temperatures are specifically for the Surface Ground Heat Exchanger and
        should probably be close to the average outdoor air temperature for the location.
        They are not used in other models.
    
    """
    internal_name = "Site:GroundTemperature:Shallow"
    field_count = 12
    required_fields = ["January Surface Ground Temperature", "February Surface Ground Temperature", "March Surface Ground Temperature", "April Surface Ground Temperature", "May Surface Ground Temperature", "June Surface Ground Temperature", "July Surface Ground Temperature", "August Surface Ground Temperature", "September Surface Ground Temperature", "October Surface Ground Temperature", "November Surface Ground Temperature", "December Surface Ground Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:GroundTemperature:Shallow`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.january_surface_ground_temperature = None
        else:
            self.january_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.february_surface_ground_temperature = None
        else:
            self.february_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.march_surface_ground_temperature = None
        else:
            self.march_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.april_surface_ground_temperature = None
        else:
            self.april_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.may_surface_ground_temperature = None
        else:
            self.may_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.june_surface_ground_temperature = None
        else:
            self.june_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.july_surface_ground_temperature = None
        else:
            self.july_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.august_surface_ground_temperature = None
        else:
            self.august_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.september_surface_ground_temperature = None
        else:
            self.september_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.october_surface_ground_temperature = None
        else:
            self.october_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.november_surface_ground_temperature = None
        else:
            self.november_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.december_surface_ground_temperature = None
        else:
            self.december_surface_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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

class SiteGroundTemperatureDeep(object):
    """ Corresponds to IDD object `Site:GroundTemperature:Deep`
        These temperatures are specifically for the ground heat exchangers that would use
        "deep" (3-4 m depth) ground temperatures for their heat source.
        They are not used in other models.
    
    """
    internal_name = "Site:GroundTemperature:Deep"
    field_count = 12
    required_fields = ["January Deep Ground Temperature", "February Deep Ground Temperature", "March Deep Ground Temperature", "April Deep Ground Temperature", "May Deep Ground Temperature", "June Deep Ground Temperature", "July Deep Ground Temperature", "August Deep Ground Temperature", "September Deep Ground Temperature", "October Deep Ground Temperature", "November Deep Ground Temperature", "December Deep Ground Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:GroundTemperature:Deep`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.january_deep_ground_temperature = None
        else:
            self.january_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.february_deep_ground_temperature = None
        else:
            self.february_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.march_deep_ground_temperature = None
        else:
            self.march_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.april_deep_ground_temperature = None
        else:
            self.april_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.may_deep_ground_temperature = None
        else:
            self.may_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.june_deep_ground_temperature = None
        else:
            self.june_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.july_deep_ground_temperature = None
        else:
            self.july_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.august_deep_ground_temperature = None
        else:
            self.august_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.september_deep_ground_temperature = None
        else:
            self.september_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.october_deep_ground_temperature = None
        else:
            self.october_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.november_deep_ground_temperature = None
        else:
            self.november_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.december_deep_ground_temperature = None
        else:
            self.december_deep_ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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
                Units: C
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

class SiteGroundDomain(object):
    """ Corresponds to IDD object `Site:GroundDomain`
        Ground coupled slab model for on-grade and
        in-grade cases with or without insulation.
    
    """
    internal_name = "Site:GroundDomain"
    field_count = 24
    required_fields = ["Name", "Ground Domain Depth", "Perimeter Offset", "Soil Thermal Conductivity", "Soil Density", "Soil Specific Heat", "Kusuda-Achenbach Average Surface Temperature", "Kusuda-Achenbach Average Amplitude of Surface Temperature", "Kusuda-Achenbach Phase Shift of Minimum Surface Temperature", "Slab Boundary Condition Model Name", "Slab Location", "Vertical Insulation", "Simulation Timestep"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:GroundDomain`
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
            self.ground_domain_depth = None
        else:
            self.ground_domain_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.aspect_ratio = None
        else:
            self.aspect_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perimeter_offset = None
        else:
            self.perimeter_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_thermal_conductivity = None
        else:
            self.soil_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_density = None
        else:
            self.soil_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_specific_heat = None
        else:
            self.soil_specific_heat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction = None
        else:
            self.soil_moisture_content_volume_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction_at_saturation = None
        else:
            self.soil_moisture_content_volume_fraction_at_saturation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_surface_temperature = None
        else:
            self.kusudaachenbach_average_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = None
        else:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = None
        else:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evapotranspiration_ground_cover_parameter = None
        else:
            self.evapotranspiration_ground_cover_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slab_boundary_condition_model_name = None
        else:
            self.slab_boundary_condition_model_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slab_location = None
        else:
            self.slab_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slab_material_name = None
        else:
            self.slab_material_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.horizontal_insulation = None
        else:
            self.horizontal_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.horizontal_insulation_material_name = None
        else:
            self.horizontal_insulation_material_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.horizontal_insulation_extents = None
        else:
            self.horizontal_insulation_extents = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perimeter_insulation_width = None
        else:
            self.perimeter_insulation_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertical_insulation = None
        else:
            self.vertical_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertical_insulation_material_name = None
        else:
            self.vertical_insulation_material_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertical_insulation_depth = None
        else:
            self.vertical_insulation_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simulation_timestep = None
        else:
            self.simulation_timestep = vals[i]
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
                Units: W/m-K
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
                Units: kg/m3
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
                Units: J/kg-K
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
                Units: percent
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
                Units: percent
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
                Units: deltaC
                if `value` is None it will not be checked against the
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
                Units: days
                if `value` is None it will not be checked against the
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `slab_location`')
            vals = {}
            vals["ingrade"] = "InGrade"
            vals["ongrade"] = "OnGrade"
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
                                     'field `slab_location`'.format(value))
            value = vals[value_lower]

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `horizontal_insulation`')
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
                                     'field `horizontal_insulation`'.format(value))
            value = vals[value_lower]

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `horizontal_insulation_extents`')
            vals = {}
            vals["full"] = "Full"
            vals["perimeter"] = "Perimeter"
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
                                     'field `horizontal_insulation_extents`'.format(value))
            value = vals[value_lower]

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `vertical_insulation`')
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
                                     'field `vertical_insulation`'.format(value))
            value = vals[value_lower]

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `simulation_timestep`')
            vals = {}
            vals["hourly"] = "Hourly"
            vals["timestep"] = "Timestep"
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
                                     'field `simulation_timestep`'.format(value))
            value = vals[value_lower]

        self._data["Simulation Timestep"] = value

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

class SiteGroundReflectance(object):
    """ Corresponds to IDD object `Site:GroundReflectance`
        Specifies the ground reflectance values used to calculate ground reflected solar.
        The ground reflectance can be further modified when snow is on the ground
        by Site:GroundReflectance:SnowModifier.
    
    """
    internal_name = "Site:GroundReflectance"
    field_count = 12
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:GroundReflectance`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.january_ground_reflectance = None
        else:
            self.january_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.february_ground_reflectance = None
        else:
            self.february_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.march_ground_reflectance = None
        else:
            self.march_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.april_ground_reflectance = None
        else:
            self.april_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.may_ground_reflectance = None
        else:
            self.may_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.june_ground_reflectance = None
        else:
            self.june_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.july_ground_reflectance = None
        else:
            self.july_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.august_ground_reflectance = None
        else:
            self.august_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.september_ground_reflectance = None
        else:
            self.september_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.october_ground_reflectance = None
        else:
            self.october_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.november_ground_reflectance = None
        else:
            self.november_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.december_ground_reflectance = None
        else:
            self.december_ground_reflectance = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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
                Units: dimensionless
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

class SiteGroundReflectanceSnowModifier(object):
    """ Corresponds to IDD object `Site:GroundReflectance:SnowModifier`
        Specifies ground reflectance multipliers when snow resident on the ground.
        These multipliers are applied to the "normal" ground reflectances specified
        in Site:GroundReflectance.
    
    """
    internal_name = "Site:GroundReflectance:SnowModifier"
    field_count = 2
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:GroundReflectance:SnowModifier`
        """
        self._data = OrderedDict()
        self._data["Ground Reflected Solar Modifier"] = None
        self._data["Daylighting Ground Reflected Solar Modifier"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.ground_reflected_solar_modifier = None
        else:
            self.ground_reflected_solar_modifier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.daylighting_ground_reflected_solar_modifier = None
        else:
            self.daylighting_ground_reflected_solar_modifier = vals[i]
        i += 1
        if i >= len(vals):
            return

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

class SiteWaterMainsTemperature(object):
    """ Corresponds to IDD object `Site:WaterMainsTemperature`
        Used to calculate water mains temperatures delivered by underground water main pipes.
        Water mains temperatures are a function of outdoor climate conditions
        and vary with time of year.
    
    """
    internal_name = "Site:WaterMainsTemperature"
    field_count = 4
    required_fields = ["Calculation Method"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:WaterMainsTemperature`
        """
        self._data = OrderedDict()
        self._data["Calculation Method"] = None
        self._data["Temperature Schedule Name"] = None
        self._data["Annual Average Outdoor Air Temperature"] = None
        self._data["Maximum Difference In Monthly Average Outdoor Air Temperatures"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.calculation_method = None
        else:
            self.calculation_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_schedule_name = None
        else:
            self.temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.annual_average_outdoor_air_temperature = None
        else:
            self.annual_average_outdoor_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_difference_in_monthly_average_outdoor_air_temperatures = None
        else:
            self.maximum_difference_in_monthly_average_outdoor_air_temperatures = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `calculation_method`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["correlation"] = "Correlation"
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
                                     'field `calculation_method`'.format(value))
            value = vals[value_lower]

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
                Units: deltaC
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

class SitePrecipitation(object):
    """ Corresponds to IDD object `Site:Precipitation`
        Used to describe the amount of water precipitation at the building site.
        Precipitation includes both rain and the equivalent water content of snow.
    
    """
    internal_name = "Site:Precipitation"
    field_count = 4
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:Precipitation`
        """
        self._data = OrderedDict()
        self._data["Precipitation Model Type"] = None
        self._data["Design Level for Total Annual Precipitation"] = None
        self._data["Precipitation Rates Schedule Name"] = None
        self._data["Average Total Annual Precipitation"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.precipitation_model_type = None
        else:
            self.precipitation_model_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_level_for_total_annual_precipitation = None
        else:
            self.design_level_for_total_annual_precipitation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.precipitation_rates_schedule_name = None
        else:
            self.precipitation_rates_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.average_total_annual_precipitation = None
        else:
            self.average_total_annual_precipitation = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `precipitation_model_type`')
            vals = {}
            vals["scheduleanddesignlevel"] = "ScheduleAndDesignLevel"
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
                                     'field `precipitation_model_type`'.format(value))
            value = vals[value_lower]

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
                Units: m/yr
                if `value` is None it will not be checked against the
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
                Units: m/yr
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

class RoofIrrigation(object):
    """ Corresponds to IDD object `RoofIrrigation`
        Used to describe the amount of irrigation on the ecoroof surface over the course
        of the simulation runperiod.
    
    """
    internal_name = "RoofIrrigation"
    field_count = 3
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `RoofIrrigation`
        """
        self._data = OrderedDict()
        self._data["Irrigation Model Type"] = None
        self._data["Irrigation Rate Schedule Name"] = None
        self._data["Irrigation Maximum Saturation Threshold"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.irrigation_model_type = None
        else:
            self.irrigation_model_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.irrigation_rate_schedule_name = None
        else:
            self.irrigation_rate_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.irrigation_maximum_saturation_threshold = None
        else:
            self.irrigation_maximum_saturation_threshold = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def irrigation_model_type(self):
        """Get irrigation_model_type

        Returns:
            str: the value of `irrigation_model_type` or None if not set
        """
        return self._data["Irrigation Model Type"]

    @irrigation_model_type.setter
    def irrigation_model_type(self, value=None):
        """  Corresponds to IDD Field `irrigation_model_type`
        SmartSchedule will not allow irrigation when soil is already moist.
        Current threshold set at 30% of saturation.

        Args:
            value (str): value for IDD Field `irrigation_model_type`
                Accepted values are:
                      - Schedule
                      - SmartSchedule
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `irrigation_model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `irrigation_model_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `irrigation_model_type`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["smartschedule"] = "SmartSchedule"
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
                                     'field `irrigation_model_type`'.format(value))
            value = vals[value_lower]

        self._data["Irrigation Model Type"] = value

    @property
    def irrigation_rate_schedule_name(self):
        """Get irrigation_rate_schedule_name

        Returns:
            str: the value of `irrigation_rate_schedule_name` or None if not set
        """
        return self._data["Irrigation Rate Schedule Name"]

    @irrigation_rate_schedule_name.setter
    def irrigation_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `irrigation_rate_schedule_name`
        Schedule values in meters of water per hour
        values should be non-negative

        Args:
            value (str): value for IDD Field `irrigation_rate_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `irrigation_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `irrigation_rate_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `irrigation_rate_schedule_name`')

        self._data["Irrigation Rate Schedule Name"] = value

    @property
    def irrigation_maximum_saturation_threshold(self):
        """Get irrigation_maximum_saturation_threshold

        Returns:
            float: the value of `irrigation_maximum_saturation_threshold` or None if not set
        """
        return self._data["Irrigation Maximum Saturation Threshold"]

    @irrigation_maximum_saturation_threshold.setter
    def irrigation_maximum_saturation_threshold(self, value=40.0 ):
        """  Corresponds to IDD Field `irrigation_maximum_saturation_threshold`
        Used with SmartSchedule to set the saturation level at which no
        irrigation is allowed.

        Args:
            value (float): value for IDD Field `irrigation_maximum_saturation_threshold`
                Units: percent
                Default value: 40.0
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
                                 'for field `irrigation_maximum_saturation_threshold`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `irrigation_maximum_saturation_threshold`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `irrigation_maximum_saturation_threshold`')

        self._data["Irrigation Maximum Saturation Threshold"] = value

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

class SiteSolarAndVisibleSpectrum(object):
    """ Corresponds to IDD object `Site:SolarAndVisibleSpectrum`
        If this object is omitted, the default solar and visible spectrum data will be used.
    
    """
    internal_name = "Site:SolarAndVisibleSpectrum"
    field_count = 4
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:SolarAndVisibleSpectrum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Spectrum Data Method"] = None
        self._data["Solar Spectrum Data Object Name"] = None
        self._data["Visible Spectrum Data Object Name"] = None
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
            self.spectrum_data_method = None
        else:
            self.spectrum_data_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.solar_spectrum_data_object_name = None
        else:
            self.solar_spectrum_data_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.visible_spectrum_data_object_name = None
        else:
            self.visible_spectrum_data_object_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `spectrum_data_method`')
            vals = {}
            vals["default"] = "Default"
            vals["userdefined"] = "UserDefined"
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
                                     'field `spectrum_data_method`'.format(value))
            value = vals[value_lower]

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `visible_spectrum_data_object_name`')

        self._data["Visible Spectrum Data Object Name"] = value

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

class SiteSpectrumData(object):
    """ Corresponds to IDD object `Site:SpectrumData`
        Spectrum Data Type is followed by up to 107 sets of normal-incidence measured values of
        [wavelength, spectrum] for wavelengths covering the solar (0.25 to 2.5 microns) or visible
        spectrum (0.38 to 0.78 microns)
    
    """
    internal_name = "Site:SpectrumData"
    field_count = 216
    required_fields = ["Name", "Spectrum Data Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Site:SpectrumData`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Spectrum Data Type"] = None
        self._data["Wavelength 1"] = None
        self._data["Spectrum 1"] = None
        self._data["Wavelength 2"] = None
        self._data["Spectrum 2"] = None
        self._data["Wavelength 3"] = None
        self._data["Spectrum 3"] = None
        self._data["Wavelength 4"] = None
        self._data["Spectrum 4"] = None
        self._data["Wavelength 5"] = None
        self._data["Spectrum 5"] = None
        self._data["Wavelength 6"] = None
        self._data["Spectrum 6"] = None
        self._data["Wavelength 7"] = None
        self._data["Spectrum 7"] = None
        self._data["Wavelength 8"] = None
        self._data["Spectrum 8"] = None
        self._data["Wavelength 9"] = None
        self._data["Spectrum 9"] = None
        self._data["Wavelength 10"] = None
        self._data["Spectrum 10"] = None
        self._data["Wavelength 11"] = None
        self._data["Spectrum 11"] = None
        self._data["Wavelength 12"] = None
        self._data["Spectrum 12"] = None
        self._data["Wavelength 13"] = None
        self._data["Spectrum 13"] = None
        self._data["Wavelength 14"] = None
        self._data["Spectrum 14"] = None
        self._data["Wavelength 15"] = None
        self._data["Spectrum 15"] = None
        self._data["Wavelength 16"] = None
        self._data["Spectrum 16"] = None
        self._data["Wavelength 17"] = None
        self._data["Spectrum 17"] = None
        self._data["Wavelength 18"] = None
        self._data["Spectrum 18"] = None
        self._data["Wavelength 19"] = None
        self._data["Spectrum 19"] = None
        self._data["Wavelength 20"] = None
        self._data["Spectrum 20"] = None
        self._data["Wavelength 21"] = None
        self._data["Spectrum 21"] = None
        self._data["Wavelength 22"] = None
        self._data["Spectrum 22"] = None
        self._data["Wavelength 23"] = None
        self._data["Spectrum 23"] = None
        self._data["Wavelength 24"] = None
        self._data["Spectrum 24"] = None
        self._data["Wavelength 25"] = None
        self._data["Spectrum 25"] = None
        self._data["Wavelength 26"] = None
        self._data["Spectrum 26"] = None
        self._data["Wavelength 27"] = None
        self._data["Spectrum 27"] = None
        self._data["Wavelength 28"] = None
        self._data["Spectrum 28"] = None
        self._data["Wavelength 29"] = None
        self._data["Spectrum 29"] = None
        self._data["Wavelength 30"] = None
        self._data["Spectrum 30"] = None
        self._data["Wavelength 31"] = None
        self._data["Spectrum 31"] = None
        self._data["Wavelength 32"] = None
        self._data["Spectrum 32"] = None
        self._data["Wavelength 33"] = None
        self._data["Spectrum 33"] = None
        self._data["Wavelength 34"] = None
        self._data["Spectrum 34"] = None
        self._data["Wavelength 35"] = None
        self._data["Spectrum 35"] = None
        self._data["Wavelength 36"] = None
        self._data["Spectrum 36"] = None
        self._data["Wavelength 37"] = None
        self._data["Spectrum 37"] = None
        self._data["Wavelength 38"] = None
        self._data["Spectrum 38"] = None
        self._data["Wavelength 39"] = None
        self._data["Spectrum 39"] = None
        self._data["Wavelength 40"] = None
        self._data["Spectrum 40"] = None
        self._data["Wavelength 41"] = None
        self._data["Spectrum 41"] = None
        self._data["Wavelength 42"] = None
        self._data["Spectrum 42"] = None
        self._data["Wavelength 43"] = None
        self._data["Spectrum 43"] = None
        self._data["Wavelength 44"] = None
        self._data["Spectrum 44"] = None
        self._data["Wavelength 45"] = None
        self._data["Spectrum 45"] = None
        self._data["Wavelength 46"] = None
        self._data["Spectrum 46"] = None
        self._data["Wavelength 47"] = None
        self._data["Spectrum 47"] = None
        self._data["Wavelength 48"] = None
        self._data["Spectrum 48"] = None
        self._data["Wavelength 49"] = None
        self._data["Spectrum 49"] = None
        self._data["Wavelength 50"] = None
        self._data["Spectrum 50"] = None
        self._data["Wavelength 51"] = None
        self._data["Spectrum 51"] = None
        self._data["Wavelength 52"] = None
        self._data["Spectrum 52"] = None
        self._data["Wavelength 53"] = None
        self._data["Spectrum 53"] = None
        self._data["Wavelength 54"] = None
        self._data["Spectrum 54"] = None
        self._data["Wavelength 55"] = None
        self._data["Spectrum 55"] = None
        self._data["Wavelength 56"] = None
        self._data["Spectrum 56"] = None
        self._data["Wavelength 57"] = None
        self._data["Spectrum 57"] = None
        self._data["Wavelength 58"] = None
        self._data["Spectrum 58"] = None
        self._data["Wavelength 59"] = None
        self._data["Spectrum 59"] = None
        self._data["Wavelength 60"] = None
        self._data["Spectrum 60"] = None
        self._data["Wavelength 61"] = None
        self._data["Spectrum 61"] = None
        self._data["Wavelength 62"] = None
        self._data["Spectrum 62"] = None
        self._data["Wavelength 63"] = None
        self._data["Spectrum 63"] = None
        self._data["Wavelength 64"] = None
        self._data["Spectrum 64"] = None
        self._data["Wavelength 65"] = None
        self._data["Spectrum 65"] = None
        self._data["Wavelength 66"] = None
        self._data["Spectrum 66"] = None
        self._data["Wavelength 67"] = None
        self._data["Spectrum 67"] = None
        self._data["Wavelength 68"] = None
        self._data["Spectrum 68"] = None
        self._data["Wavelength 69"] = None
        self._data["Spectrum 69"] = None
        self._data["Wavelength 70"] = None
        self._data["Spectrum 70"] = None
        self._data["Wavelength 71"] = None
        self._data["Spectrum 71"] = None
        self._data["Wavelength 72"] = None
        self._data["Spectrum 72"] = None
        self._data["Wavelength 73"] = None
        self._data["Spectrum 73"] = None
        self._data["Wavelength 74"] = None
        self._data["Spectrum 74"] = None
        self._data["Wavelength 75"] = None
        self._data["Spectrum 75"] = None
        self._data["Wavelength 76"] = None
        self._data["Spectrum 76"] = None
        self._data["Wavelength 77"] = None
        self._data["Spectrum 77"] = None
        self._data["Wavelength 78"] = None
        self._data["Spectrum 78"] = None
        self._data["Wavelength 79"] = None
        self._data["Spectrum 79"] = None
        self._data["Wavelength 80"] = None
        self._data["Spectrum 80"] = None
        self._data["Wavelength 81"] = None
        self._data["Spectrum 81"] = None
        self._data["Wavelength 82"] = None
        self._data["Spectrum 82"] = None
        self._data["Wavelength 83"] = None
        self._data["Spectrum 83"] = None
        self._data["Wavelength 84"] = None
        self._data["Spectrum 84"] = None
        self._data["Wavelength 85"] = None
        self._data["Spectrum 85"] = None
        self._data["Wavelength 86"] = None
        self._data["Spectrum 86"] = None
        self._data["Wavelength 87"] = None
        self._data["Spectrum 87"] = None
        self._data["Wavelength 88"] = None
        self._data["Spectrum 88"] = None
        self._data["Wavelength 89"] = None
        self._data["Spectrum 89"] = None
        self._data["Wavelength 90"] = None
        self._data["Spectrum 90"] = None
        self._data["Wavelength 91"] = None
        self._data["Spectrum 91"] = None
        self._data["Wavelength 92"] = None
        self._data["Spectrum 92"] = None
        self._data["Wavelength 93"] = None
        self._data["Spectrum 93"] = None
        self._data["Wavelength 94"] = None
        self._data["Spectrum 94"] = None
        self._data["Wavelength 95"] = None
        self._data["Spectrum 95"] = None
        self._data["Wavelength 96"] = None
        self._data["Spectrum 96"] = None
        self._data["Wavelength 97"] = None
        self._data["Spectrum 97"] = None
        self._data["Wavelength 98"] = None
        self._data["Spectrum 98"] = None
        self._data["Wavelength 99"] = None
        self._data["Spectrum 99"] = None
        self._data["Wavelength 100"] = None
        self._data["Spectrum 100"] = None
        self._data["Wavelength 101"] = None
        self._data["Spectrum 101"] = None
        self._data["Wavelength 102"] = None
        self._data["Spectrum 102"] = None
        self._data["Wavelength 103"] = None
        self._data["Spectrum 103"] = None
        self._data["Wavelength 104"] = None
        self._data["Spectrum 104"] = None
        self._data["Wavelength 105"] = None
        self._data["Spectrum 105"] = None
        self._data["Wavelength 106"] = None
        self._data["Spectrum 106"] = None
        self._data["Wavelength 107"] = None
        self._data["Spectrum 107"] = None
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
            self.spectrum_data_type = None
        else:
            self.spectrum_data_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_1 = None
        else:
            self.wavelength_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_1 = None
        else:
            self.spectrum_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_2 = None
        else:
            self.wavelength_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_2 = None
        else:
            self.spectrum_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_3 = None
        else:
            self.wavelength_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_3 = None
        else:
            self.spectrum_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_4 = None
        else:
            self.wavelength_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_4 = None
        else:
            self.spectrum_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_5 = None
        else:
            self.wavelength_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_5 = None
        else:
            self.spectrum_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_6 = None
        else:
            self.wavelength_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_6 = None
        else:
            self.spectrum_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_7 = None
        else:
            self.wavelength_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_7 = None
        else:
            self.spectrum_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_8 = None
        else:
            self.wavelength_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_8 = None
        else:
            self.spectrum_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_9 = None
        else:
            self.wavelength_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_9 = None
        else:
            self.spectrum_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_10 = None
        else:
            self.wavelength_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_10 = None
        else:
            self.spectrum_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_11 = None
        else:
            self.wavelength_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_11 = None
        else:
            self.spectrum_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_12 = None
        else:
            self.wavelength_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_12 = None
        else:
            self.spectrum_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_13 = None
        else:
            self.wavelength_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_13 = None
        else:
            self.spectrum_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_14 = None
        else:
            self.wavelength_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_14 = None
        else:
            self.spectrum_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_15 = None
        else:
            self.wavelength_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_15 = None
        else:
            self.spectrum_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_16 = None
        else:
            self.wavelength_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_16 = None
        else:
            self.spectrum_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_17 = None
        else:
            self.wavelength_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_17 = None
        else:
            self.spectrum_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_18 = None
        else:
            self.wavelength_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_18 = None
        else:
            self.spectrum_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_19 = None
        else:
            self.wavelength_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_19 = None
        else:
            self.spectrum_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_20 = None
        else:
            self.wavelength_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_20 = None
        else:
            self.spectrum_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_21 = None
        else:
            self.wavelength_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_21 = None
        else:
            self.spectrum_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_22 = None
        else:
            self.wavelength_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_22 = None
        else:
            self.spectrum_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_23 = None
        else:
            self.wavelength_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_23 = None
        else:
            self.spectrum_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_24 = None
        else:
            self.wavelength_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_24 = None
        else:
            self.spectrum_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_25 = None
        else:
            self.wavelength_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_25 = None
        else:
            self.spectrum_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_26 = None
        else:
            self.wavelength_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_26 = None
        else:
            self.spectrum_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_27 = None
        else:
            self.wavelength_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_27 = None
        else:
            self.spectrum_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_28 = None
        else:
            self.wavelength_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_28 = None
        else:
            self.spectrum_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_29 = None
        else:
            self.wavelength_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_29 = None
        else:
            self.spectrum_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_30 = None
        else:
            self.wavelength_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_30 = None
        else:
            self.spectrum_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_31 = None
        else:
            self.wavelength_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_31 = None
        else:
            self.spectrum_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_32 = None
        else:
            self.wavelength_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_32 = None
        else:
            self.spectrum_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_33 = None
        else:
            self.wavelength_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_33 = None
        else:
            self.spectrum_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_34 = None
        else:
            self.wavelength_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_34 = None
        else:
            self.spectrum_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_35 = None
        else:
            self.wavelength_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_35 = None
        else:
            self.spectrum_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_36 = None
        else:
            self.wavelength_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_36 = None
        else:
            self.spectrum_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_37 = None
        else:
            self.wavelength_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_37 = None
        else:
            self.spectrum_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_38 = None
        else:
            self.wavelength_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_38 = None
        else:
            self.spectrum_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_39 = None
        else:
            self.wavelength_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_39 = None
        else:
            self.spectrum_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_40 = None
        else:
            self.wavelength_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_40 = None
        else:
            self.spectrum_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_41 = None
        else:
            self.wavelength_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_41 = None
        else:
            self.spectrum_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_42 = None
        else:
            self.wavelength_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_42 = None
        else:
            self.spectrum_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_43 = None
        else:
            self.wavelength_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_43 = None
        else:
            self.spectrum_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_44 = None
        else:
            self.wavelength_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_44 = None
        else:
            self.spectrum_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_45 = None
        else:
            self.wavelength_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_45 = None
        else:
            self.spectrum_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_46 = None
        else:
            self.wavelength_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_46 = None
        else:
            self.spectrum_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_47 = None
        else:
            self.wavelength_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_47 = None
        else:
            self.spectrum_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_48 = None
        else:
            self.wavelength_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_48 = None
        else:
            self.spectrum_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_49 = None
        else:
            self.wavelength_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_49 = None
        else:
            self.spectrum_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_50 = None
        else:
            self.wavelength_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_50 = None
        else:
            self.spectrum_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_51 = None
        else:
            self.wavelength_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_51 = None
        else:
            self.spectrum_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_52 = None
        else:
            self.wavelength_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_52 = None
        else:
            self.spectrum_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_53 = None
        else:
            self.wavelength_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_53 = None
        else:
            self.spectrum_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_54 = None
        else:
            self.wavelength_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_54 = None
        else:
            self.spectrum_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_55 = None
        else:
            self.wavelength_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_55 = None
        else:
            self.spectrum_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_56 = None
        else:
            self.wavelength_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_56 = None
        else:
            self.spectrum_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_57 = None
        else:
            self.wavelength_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_57 = None
        else:
            self.spectrum_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_58 = None
        else:
            self.wavelength_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_58 = None
        else:
            self.spectrum_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_59 = None
        else:
            self.wavelength_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_59 = None
        else:
            self.spectrum_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_60 = None
        else:
            self.wavelength_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_60 = None
        else:
            self.spectrum_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_61 = None
        else:
            self.wavelength_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_61 = None
        else:
            self.spectrum_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_62 = None
        else:
            self.wavelength_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_62 = None
        else:
            self.spectrum_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_63 = None
        else:
            self.wavelength_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_63 = None
        else:
            self.spectrum_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_64 = None
        else:
            self.wavelength_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_64 = None
        else:
            self.spectrum_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_65 = None
        else:
            self.wavelength_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_65 = None
        else:
            self.spectrum_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_66 = None
        else:
            self.wavelength_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_66 = None
        else:
            self.spectrum_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_67 = None
        else:
            self.wavelength_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_67 = None
        else:
            self.spectrum_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_68 = None
        else:
            self.wavelength_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_68 = None
        else:
            self.spectrum_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_69 = None
        else:
            self.wavelength_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_69 = None
        else:
            self.spectrum_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_70 = None
        else:
            self.wavelength_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_70 = None
        else:
            self.spectrum_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_71 = None
        else:
            self.wavelength_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_71 = None
        else:
            self.spectrum_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_72 = None
        else:
            self.wavelength_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_72 = None
        else:
            self.spectrum_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_73 = None
        else:
            self.wavelength_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_73 = None
        else:
            self.spectrum_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_74 = None
        else:
            self.wavelength_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_74 = None
        else:
            self.spectrum_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_75 = None
        else:
            self.wavelength_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_75 = None
        else:
            self.spectrum_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_76 = None
        else:
            self.wavelength_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_76 = None
        else:
            self.spectrum_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_77 = None
        else:
            self.wavelength_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_77 = None
        else:
            self.spectrum_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_78 = None
        else:
            self.wavelength_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_78 = None
        else:
            self.spectrum_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_79 = None
        else:
            self.wavelength_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_79 = None
        else:
            self.spectrum_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_80 = None
        else:
            self.wavelength_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_80 = None
        else:
            self.spectrum_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_81 = None
        else:
            self.wavelength_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_81 = None
        else:
            self.spectrum_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_82 = None
        else:
            self.wavelength_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_82 = None
        else:
            self.spectrum_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_83 = None
        else:
            self.wavelength_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_83 = None
        else:
            self.spectrum_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_84 = None
        else:
            self.wavelength_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_84 = None
        else:
            self.spectrum_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_85 = None
        else:
            self.wavelength_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_85 = None
        else:
            self.spectrum_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_86 = None
        else:
            self.wavelength_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_86 = None
        else:
            self.spectrum_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_87 = None
        else:
            self.wavelength_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_87 = None
        else:
            self.spectrum_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_88 = None
        else:
            self.wavelength_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_88 = None
        else:
            self.spectrum_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_89 = None
        else:
            self.wavelength_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_89 = None
        else:
            self.spectrum_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_90 = None
        else:
            self.wavelength_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_90 = None
        else:
            self.spectrum_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_91 = None
        else:
            self.wavelength_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_91 = None
        else:
            self.spectrum_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_92 = None
        else:
            self.wavelength_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_92 = None
        else:
            self.spectrum_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_93 = None
        else:
            self.wavelength_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_93 = None
        else:
            self.spectrum_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_94 = None
        else:
            self.wavelength_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_94 = None
        else:
            self.spectrum_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_95 = None
        else:
            self.wavelength_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_95 = None
        else:
            self.spectrum_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_96 = None
        else:
            self.wavelength_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_96 = None
        else:
            self.spectrum_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_97 = None
        else:
            self.wavelength_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_97 = None
        else:
            self.spectrum_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_98 = None
        else:
            self.wavelength_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_98 = None
        else:
            self.spectrum_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_99 = None
        else:
            self.wavelength_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_99 = None
        else:
            self.spectrum_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_100 = None
        else:
            self.wavelength_100 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_100 = None
        else:
            self.spectrum_100 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_101 = None
        else:
            self.wavelength_101 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_101 = None
        else:
            self.spectrum_101 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_102 = None
        else:
            self.wavelength_102 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_102 = None
        else:
            self.spectrum_102 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_103 = None
        else:
            self.wavelength_103 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_103 = None
        else:
            self.spectrum_103 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_104 = None
        else:
            self.wavelength_104 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_104 = None
        else:
            self.spectrum_104 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_105 = None
        else:
            self.wavelength_105 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_105 = None
        else:
            self.spectrum_105 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_106 = None
        else:
            self.wavelength_106 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_106 = None
        else:
            self.spectrum_106 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wavelength_107 = None
        else:
            self.wavelength_107 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.spectrum_107 = None
        else:
            self.spectrum_107 = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `spectrum_data_type`')
            vals = {}
            vals["solar"] = "Solar"
            vals["visible"] = "Visible"
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
                                     'field `spectrum_data_type`'.format(value))
            value = vals[value_lower]

        self._data["Spectrum Data Type"] = value

    @property
    def wavelength_1(self):
        """Get wavelength_1

        Returns:
            float: the value of `wavelength_1` or None if not set
        """
        return self._data["Wavelength 1"]

    @wavelength_1.setter
    def wavelength_1(self, value=None):
        """  Corresponds to IDD Field `wavelength_1`

        Args:
            value (float): value for IDD Field `wavelength_1`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_1`'.format(value))

        self._data["Wavelength 1"] = value

    @property
    def spectrum_1(self):
        """Get spectrum_1

        Returns:
            float: the value of `spectrum_1` or None if not set
        """
        return self._data["Spectrum 1"]

    @spectrum_1.setter
    def spectrum_1(self, value=None):
        """  Corresponds to IDD Field `spectrum_1`

        Args:
            value (float): value for IDD Field `spectrum_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_1`'.format(value))

        self._data["Spectrum 1"] = value

    @property
    def wavelength_2(self):
        """Get wavelength_2

        Returns:
            float: the value of `wavelength_2` or None if not set
        """
        return self._data["Wavelength 2"]

    @wavelength_2.setter
    def wavelength_2(self, value=None):
        """  Corresponds to IDD Field `wavelength_2`

        Args:
            value (float): value for IDD Field `wavelength_2`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_2`'.format(value))

        self._data["Wavelength 2"] = value

    @property
    def spectrum_2(self):
        """Get spectrum_2

        Returns:
            float: the value of `spectrum_2` or None if not set
        """
        return self._data["Spectrum 2"]

    @spectrum_2.setter
    def spectrum_2(self, value=None):
        """  Corresponds to IDD Field `spectrum_2`

        Args:
            value (float): value for IDD Field `spectrum_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_2`'.format(value))

        self._data["Spectrum 2"] = value

    @property
    def wavelength_3(self):
        """Get wavelength_3

        Returns:
            float: the value of `wavelength_3` or None if not set
        """
        return self._data["Wavelength 3"]

    @wavelength_3.setter
    def wavelength_3(self, value=None):
        """  Corresponds to IDD Field `wavelength_3`

        Args:
            value (float): value for IDD Field `wavelength_3`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_3`'.format(value))

        self._data["Wavelength 3"] = value

    @property
    def spectrum_3(self):
        """Get spectrum_3

        Returns:
            float: the value of `spectrum_3` or None if not set
        """
        return self._data["Spectrum 3"]

    @spectrum_3.setter
    def spectrum_3(self, value=None):
        """  Corresponds to IDD Field `spectrum_3`

        Args:
            value (float): value for IDD Field `spectrum_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_3`'.format(value))

        self._data["Spectrum 3"] = value

    @property
    def wavelength_4(self):
        """Get wavelength_4

        Returns:
            float: the value of `wavelength_4` or None if not set
        """
        return self._data["Wavelength 4"]

    @wavelength_4.setter
    def wavelength_4(self, value=None):
        """  Corresponds to IDD Field `wavelength_4`

        Args:
            value (float): value for IDD Field `wavelength_4`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_4`'.format(value))

        self._data["Wavelength 4"] = value

    @property
    def spectrum_4(self):
        """Get spectrum_4

        Returns:
            float: the value of `spectrum_4` or None if not set
        """
        return self._data["Spectrum 4"]

    @spectrum_4.setter
    def spectrum_4(self, value=None):
        """  Corresponds to IDD Field `spectrum_4`

        Args:
            value (float): value for IDD Field `spectrum_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_4`'.format(value))

        self._data["Spectrum 4"] = value

    @property
    def wavelength_5(self):
        """Get wavelength_5

        Returns:
            float: the value of `wavelength_5` or None if not set
        """
        return self._data["Wavelength 5"]

    @wavelength_5.setter
    def wavelength_5(self, value=None):
        """  Corresponds to IDD Field `wavelength_5`

        Args:
            value (float): value for IDD Field `wavelength_5`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_5`'.format(value))

        self._data["Wavelength 5"] = value

    @property
    def spectrum_5(self):
        """Get spectrum_5

        Returns:
            float: the value of `spectrum_5` or None if not set
        """
        return self._data["Spectrum 5"]

    @spectrum_5.setter
    def spectrum_5(self, value=None):
        """  Corresponds to IDD Field `spectrum_5`

        Args:
            value (float): value for IDD Field `spectrum_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_5`'.format(value))

        self._data["Spectrum 5"] = value

    @property
    def wavelength_6(self):
        """Get wavelength_6

        Returns:
            float: the value of `wavelength_6` or None if not set
        """
        return self._data["Wavelength 6"]

    @wavelength_6.setter
    def wavelength_6(self, value=None):
        """  Corresponds to IDD Field `wavelength_6`

        Args:
            value (float): value for IDD Field `wavelength_6`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_6`'.format(value))

        self._data["Wavelength 6"] = value

    @property
    def spectrum_6(self):
        """Get spectrum_6

        Returns:
            float: the value of `spectrum_6` or None if not set
        """
        return self._data["Spectrum 6"]

    @spectrum_6.setter
    def spectrum_6(self, value=None):
        """  Corresponds to IDD Field `spectrum_6`

        Args:
            value (float): value for IDD Field `spectrum_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_6`'.format(value))

        self._data["Spectrum 6"] = value

    @property
    def wavelength_7(self):
        """Get wavelength_7

        Returns:
            float: the value of `wavelength_7` or None if not set
        """
        return self._data["Wavelength 7"]

    @wavelength_7.setter
    def wavelength_7(self, value=None):
        """  Corresponds to IDD Field `wavelength_7`

        Args:
            value (float): value for IDD Field `wavelength_7`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_7`'.format(value))

        self._data["Wavelength 7"] = value

    @property
    def spectrum_7(self):
        """Get spectrum_7

        Returns:
            float: the value of `spectrum_7` or None if not set
        """
        return self._data["Spectrum 7"]

    @spectrum_7.setter
    def spectrum_7(self, value=None):
        """  Corresponds to IDD Field `spectrum_7`

        Args:
            value (float): value for IDD Field `spectrum_7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_7`'.format(value))

        self._data["Spectrum 7"] = value

    @property
    def wavelength_8(self):
        """Get wavelength_8

        Returns:
            float: the value of `wavelength_8` or None if not set
        """
        return self._data["Wavelength 8"]

    @wavelength_8.setter
    def wavelength_8(self, value=None):
        """  Corresponds to IDD Field `wavelength_8`

        Args:
            value (float): value for IDD Field `wavelength_8`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_8`'.format(value))

        self._data["Wavelength 8"] = value

    @property
    def spectrum_8(self):
        """Get spectrum_8

        Returns:
            float: the value of `spectrum_8` or None if not set
        """
        return self._data["Spectrum 8"]

    @spectrum_8.setter
    def spectrum_8(self, value=None):
        """  Corresponds to IDD Field `spectrum_8`

        Args:
            value (float): value for IDD Field `spectrum_8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_8`'.format(value))

        self._data["Spectrum 8"] = value

    @property
    def wavelength_9(self):
        """Get wavelength_9

        Returns:
            float: the value of `wavelength_9` or None if not set
        """
        return self._data["Wavelength 9"]

    @wavelength_9.setter
    def wavelength_9(self, value=None):
        """  Corresponds to IDD Field `wavelength_9`

        Args:
            value (float): value for IDD Field `wavelength_9`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_9`'.format(value))

        self._data["Wavelength 9"] = value

    @property
    def spectrum_9(self):
        """Get spectrum_9

        Returns:
            float: the value of `spectrum_9` or None if not set
        """
        return self._data["Spectrum 9"]

    @spectrum_9.setter
    def spectrum_9(self, value=None):
        """  Corresponds to IDD Field `spectrum_9`

        Args:
            value (float): value for IDD Field `spectrum_9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_9`'.format(value))

        self._data["Spectrum 9"] = value

    @property
    def wavelength_10(self):
        """Get wavelength_10

        Returns:
            float: the value of `wavelength_10` or None if not set
        """
        return self._data["Wavelength 10"]

    @wavelength_10.setter
    def wavelength_10(self, value=None):
        """  Corresponds to IDD Field `wavelength_10`

        Args:
            value (float): value for IDD Field `wavelength_10`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_10`'.format(value))

        self._data["Wavelength 10"] = value

    @property
    def spectrum_10(self):
        """Get spectrum_10

        Returns:
            float: the value of `spectrum_10` or None if not set
        """
        return self._data["Spectrum 10"]

    @spectrum_10.setter
    def spectrum_10(self, value=None):
        """  Corresponds to IDD Field `spectrum_10`

        Args:
            value (float): value for IDD Field `spectrum_10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_10`'.format(value))

        self._data["Spectrum 10"] = value

    @property
    def wavelength_11(self):
        """Get wavelength_11

        Returns:
            float: the value of `wavelength_11` or None if not set
        """
        return self._data["Wavelength 11"]

    @wavelength_11.setter
    def wavelength_11(self, value=None):
        """  Corresponds to IDD Field `wavelength_11`

        Args:
            value (float): value for IDD Field `wavelength_11`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_11`'.format(value))

        self._data["Wavelength 11"] = value

    @property
    def spectrum_11(self):
        """Get spectrum_11

        Returns:
            float: the value of `spectrum_11` or None if not set
        """
        return self._data["Spectrum 11"]

    @spectrum_11.setter
    def spectrum_11(self, value=None):
        """  Corresponds to IDD Field `spectrum_11`

        Args:
            value (float): value for IDD Field `spectrum_11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_11`'.format(value))

        self._data["Spectrum 11"] = value

    @property
    def wavelength_12(self):
        """Get wavelength_12

        Returns:
            float: the value of `wavelength_12` or None if not set
        """
        return self._data["Wavelength 12"]

    @wavelength_12.setter
    def wavelength_12(self, value=None):
        """  Corresponds to IDD Field `wavelength_12`

        Args:
            value (float): value for IDD Field `wavelength_12`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_12`'.format(value))

        self._data["Wavelength 12"] = value

    @property
    def spectrum_12(self):
        """Get spectrum_12

        Returns:
            float: the value of `spectrum_12` or None if not set
        """
        return self._data["Spectrum 12"]

    @spectrum_12.setter
    def spectrum_12(self, value=None):
        """  Corresponds to IDD Field `spectrum_12`

        Args:
            value (float): value for IDD Field `spectrum_12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_12`'.format(value))

        self._data["Spectrum 12"] = value

    @property
    def wavelength_13(self):
        """Get wavelength_13

        Returns:
            float: the value of `wavelength_13` or None if not set
        """
        return self._data["Wavelength 13"]

    @wavelength_13.setter
    def wavelength_13(self, value=None):
        """  Corresponds to IDD Field `wavelength_13`

        Args:
            value (float): value for IDD Field `wavelength_13`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_13`'.format(value))

        self._data["Wavelength 13"] = value

    @property
    def spectrum_13(self):
        """Get spectrum_13

        Returns:
            float: the value of `spectrum_13` or None if not set
        """
        return self._data["Spectrum 13"]

    @spectrum_13.setter
    def spectrum_13(self, value=None):
        """  Corresponds to IDD Field `spectrum_13`

        Args:
            value (float): value for IDD Field `spectrum_13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_13`'.format(value))

        self._data["Spectrum 13"] = value

    @property
    def wavelength_14(self):
        """Get wavelength_14

        Returns:
            float: the value of `wavelength_14` or None if not set
        """
        return self._data["Wavelength 14"]

    @wavelength_14.setter
    def wavelength_14(self, value=None):
        """  Corresponds to IDD Field `wavelength_14`

        Args:
            value (float): value for IDD Field `wavelength_14`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_14`'.format(value))

        self._data["Wavelength 14"] = value

    @property
    def spectrum_14(self):
        """Get spectrum_14

        Returns:
            float: the value of `spectrum_14` or None if not set
        """
        return self._data["Spectrum 14"]

    @spectrum_14.setter
    def spectrum_14(self, value=None):
        """  Corresponds to IDD Field `spectrum_14`

        Args:
            value (float): value for IDD Field `spectrum_14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_14`'.format(value))

        self._data["Spectrum 14"] = value

    @property
    def wavelength_15(self):
        """Get wavelength_15

        Returns:
            float: the value of `wavelength_15` or None if not set
        """
        return self._data["Wavelength 15"]

    @wavelength_15.setter
    def wavelength_15(self, value=None):
        """  Corresponds to IDD Field `wavelength_15`

        Args:
            value (float): value for IDD Field `wavelength_15`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_15`'.format(value))

        self._data["Wavelength 15"] = value

    @property
    def spectrum_15(self):
        """Get spectrum_15

        Returns:
            float: the value of `spectrum_15` or None if not set
        """
        return self._data["Spectrum 15"]

    @spectrum_15.setter
    def spectrum_15(self, value=None):
        """  Corresponds to IDD Field `spectrum_15`

        Args:
            value (float): value for IDD Field `spectrum_15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_15`'.format(value))

        self._data["Spectrum 15"] = value

    @property
    def wavelength_16(self):
        """Get wavelength_16

        Returns:
            float: the value of `wavelength_16` or None if not set
        """
        return self._data["Wavelength 16"]

    @wavelength_16.setter
    def wavelength_16(self, value=None):
        """  Corresponds to IDD Field `wavelength_16`

        Args:
            value (float): value for IDD Field `wavelength_16`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_16`'.format(value))

        self._data["Wavelength 16"] = value

    @property
    def spectrum_16(self):
        """Get spectrum_16

        Returns:
            float: the value of `spectrum_16` or None if not set
        """
        return self._data["Spectrum 16"]

    @spectrum_16.setter
    def spectrum_16(self, value=None):
        """  Corresponds to IDD Field `spectrum_16`

        Args:
            value (float): value for IDD Field `spectrum_16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_16`'.format(value))

        self._data["Spectrum 16"] = value

    @property
    def wavelength_17(self):
        """Get wavelength_17

        Returns:
            float: the value of `wavelength_17` or None if not set
        """
        return self._data["Wavelength 17"]

    @wavelength_17.setter
    def wavelength_17(self, value=None):
        """  Corresponds to IDD Field `wavelength_17`

        Args:
            value (float): value for IDD Field `wavelength_17`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_17`'.format(value))

        self._data["Wavelength 17"] = value

    @property
    def spectrum_17(self):
        """Get spectrum_17

        Returns:
            float: the value of `spectrum_17` or None if not set
        """
        return self._data["Spectrum 17"]

    @spectrum_17.setter
    def spectrum_17(self, value=None):
        """  Corresponds to IDD Field `spectrum_17`

        Args:
            value (float): value for IDD Field `spectrum_17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_17`'.format(value))

        self._data["Spectrum 17"] = value

    @property
    def wavelength_18(self):
        """Get wavelength_18

        Returns:
            float: the value of `wavelength_18` or None if not set
        """
        return self._data["Wavelength 18"]

    @wavelength_18.setter
    def wavelength_18(self, value=None):
        """  Corresponds to IDD Field `wavelength_18`

        Args:
            value (float): value for IDD Field `wavelength_18`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_18`'.format(value))

        self._data["Wavelength 18"] = value

    @property
    def spectrum_18(self):
        """Get spectrum_18

        Returns:
            float: the value of `spectrum_18` or None if not set
        """
        return self._data["Spectrum 18"]

    @spectrum_18.setter
    def spectrum_18(self, value=None):
        """  Corresponds to IDD Field `spectrum_18`

        Args:
            value (float): value for IDD Field `spectrum_18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_18`'.format(value))

        self._data["Spectrum 18"] = value

    @property
    def wavelength_19(self):
        """Get wavelength_19

        Returns:
            float: the value of `wavelength_19` or None if not set
        """
        return self._data["Wavelength 19"]

    @wavelength_19.setter
    def wavelength_19(self, value=None):
        """  Corresponds to IDD Field `wavelength_19`

        Args:
            value (float): value for IDD Field `wavelength_19`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_19`'.format(value))

        self._data["Wavelength 19"] = value

    @property
    def spectrum_19(self):
        """Get spectrum_19

        Returns:
            float: the value of `spectrum_19` or None if not set
        """
        return self._data["Spectrum 19"]

    @spectrum_19.setter
    def spectrum_19(self, value=None):
        """  Corresponds to IDD Field `spectrum_19`

        Args:
            value (float): value for IDD Field `spectrum_19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_19`'.format(value))

        self._data["Spectrum 19"] = value

    @property
    def wavelength_20(self):
        """Get wavelength_20

        Returns:
            float: the value of `wavelength_20` or None if not set
        """
        return self._data["Wavelength 20"]

    @wavelength_20.setter
    def wavelength_20(self, value=None):
        """  Corresponds to IDD Field `wavelength_20`

        Args:
            value (float): value for IDD Field `wavelength_20`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_20`'.format(value))

        self._data["Wavelength 20"] = value

    @property
    def spectrum_20(self):
        """Get spectrum_20

        Returns:
            float: the value of `spectrum_20` or None if not set
        """
        return self._data["Spectrum 20"]

    @spectrum_20.setter
    def spectrum_20(self, value=None):
        """  Corresponds to IDD Field `spectrum_20`

        Args:
            value (float): value for IDD Field `spectrum_20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_20`'.format(value))

        self._data["Spectrum 20"] = value

    @property
    def wavelength_21(self):
        """Get wavelength_21

        Returns:
            float: the value of `wavelength_21` or None if not set
        """
        return self._data["Wavelength 21"]

    @wavelength_21.setter
    def wavelength_21(self, value=None):
        """  Corresponds to IDD Field `wavelength_21`

        Args:
            value (float): value for IDD Field `wavelength_21`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_21`'.format(value))

        self._data["Wavelength 21"] = value

    @property
    def spectrum_21(self):
        """Get spectrum_21

        Returns:
            float: the value of `spectrum_21` or None if not set
        """
        return self._data["Spectrum 21"]

    @spectrum_21.setter
    def spectrum_21(self, value=None):
        """  Corresponds to IDD Field `spectrum_21`

        Args:
            value (float): value for IDD Field `spectrum_21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_21`'.format(value))

        self._data["Spectrum 21"] = value

    @property
    def wavelength_22(self):
        """Get wavelength_22

        Returns:
            float: the value of `wavelength_22` or None if not set
        """
        return self._data["Wavelength 22"]

    @wavelength_22.setter
    def wavelength_22(self, value=None):
        """  Corresponds to IDD Field `wavelength_22`

        Args:
            value (float): value for IDD Field `wavelength_22`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_22`'.format(value))

        self._data["Wavelength 22"] = value

    @property
    def spectrum_22(self):
        """Get spectrum_22

        Returns:
            float: the value of `spectrum_22` or None if not set
        """
        return self._data["Spectrum 22"]

    @spectrum_22.setter
    def spectrum_22(self, value=None):
        """  Corresponds to IDD Field `spectrum_22`

        Args:
            value (float): value for IDD Field `spectrum_22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_22`'.format(value))

        self._data["Spectrum 22"] = value

    @property
    def wavelength_23(self):
        """Get wavelength_23

        Returns:
            float: the value of `wavelength_23` or None if not set
        """
        return self._data["Wavelength 23"]

    @wavelength_23.setter
    def wavelength_23(self, value=None):
        """  Corresponds to IDD Field `wavelength_23`

        Args:
            value (float): value for IDD Field `wavelength_23`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_23`'.format(value))

        self._data["Wavelength 23"] = value

    @property
    def spectrum_23(self):
        """Get spectrum_23

        Returns:
            float: the value of `spectrum_23` or None if not set
        """
        return self._data["Spectrum 23"]

    @spectrum_23.setter
    def spectrum_23(self, value=None):
        """  Corresponds to IDD Field `spectrum_23`

        Args:
            value (float): value for IDD Field `spectrum_23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_23`'.format(value))

        self._data["Spectrum 23"] = value

    @property
    def wavelength_24(self):
        """Get wavelength_24

        Returns:
            float: the value of `wavelength_24` or None if not set
        """
        return self._data["Wavelength 24"]

    @wavelength_24.setter
    def wavelength_24(self, value=None):
        """  Corresponds to IDD Field `wavelength_24`

        Args:
            value (float): value for IDD Field `wavelength_24`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_24`'.format(value))

        self._data["Wavelength 24"] = value

    @property
    def spectrum_24(self):
        """Get spectrum_24

        Returns:
            float: the value of `spectrum_24` or None if not set
        """
        return self._data["Spectrum 24"]

    @spectrum_24.setter
    def spectrum_24(self, value=None):
        """  Corresponds to IDD Field `spectrum_24`

        Args:
            value (float): value for IDD Field `spectrum_24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_24`'.format(value))

        self._data["Spectrum 24"] = value

    @property
    def wavelength_25(self):
        """Get wavelength_25

        Returns:
            float: the value of `wavelength_25` or None if not set
        """
        return self._data["Wavelength 25"]

    @wavelength_25.setter
    def wavelength_25(self, value=None):
        """  Corresponds to IDD Field `wavelength_25`

        Args:
            value (float): value for IDD Field `wavelength_25`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_25`'.format(value))

        self._data["Wavelength 25"] = value

    @property
    def spectrum_25(self):
        """Get spectrum_25

        Returns:
            float: the value of `spectrum_25` or None if not set
        """
        return self._data["Spectrum 25"]

    @spectrum_25.setter
    def spectrum_25(self, value=None):
        """  Corresponds to IDD Field `spectrum_25`

        Args:
            value (float): value for IDD Field `spectrum_25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_25`'.format(value))

        self._data["Spectrum 25"] = value

    @property
    def wavelength_26(self):
        """Get wavelength_26

        Returns:
            float: the value of `wavelength_26` or None if not set
        """
        return self._data["Wavelength 26"]

    @wavelength_26.setter
    def wavelength_26(self, value=None):
        """  Corresponds to IDD Field `wavelength_26`

        Args:
            value (float): value for IDD Field `wavelength_26`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_26`'.format(value))

        self._data["Wavelength 26"] = value

    @property
    def spectrum_26(self):
        """Get spectrum_26

        Returns:
            float: the value of `spectrum_26` or None if not set
        """
        return self._data["Spectrum 26"]

    @spectrum_26.setter
    def spectrum_26(self, value=None):
        """  Corresponds to IDD Field `spectrum_26`

        Args:
            value (float): value for IDD Field `spectrum_26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_26`'.format(value))

        self._data["Spectrum 26"] = value

    @property
    def wavelength_27(self):
        """Get wavelength_27

        Returns:
            float: the value of `wavelength_27` or None if not set
        """
        return self._data["Wavelength 27"]

    @wavelength_27.setter
    def wavelength_27(self, value=None):
        """  Corresponds to IDD Field `wavelength_27`

        Args:
            value (float): value for IDD Field `wavelength_27`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_27`'.format(value))

        self._data["Wavelength 27"] = value

    @property
    def spectrum_27(self):
        """Get spectrum_27

        Returns:
            float: the value of `spectrum_27` or None if not set
        """
        return self._data["Spectrum 27"]

    @spectrum_27.setter
    def spectrum_27(self, value=None):
        """  Corresponds to IDD Field `spectrum_27`

        Args:
            value (float): value for IDD Field `spectrum_27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_27`'.format(value))

        self._data["Spectrum 27"] = value

    @property
    def wavelength_28(self):
        """Get wavelength_28

        Returns:
            float: the value of `wavelength_28` or None if not set
        """
        return self._data["Wavelength 28"]

    @wavelength_28.setter
    def wavelength_28(self, value=None):
        """  Corresponds to IDD Field `wavelength_28`

        Args:
            value (float): value for IDD Field `wavelength_28`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_28`'.format(value))

        self._data["Wavelength 28"] = value

    @property
    def spectrum_28(self):
        """Get spectrum_28

        Returns:
            float: the value of `spectrum_28` or None if not set
        """
        return self._data["Spectrum 28"]

    @spectrum_28.setter
    def spectrum_28(self, value=None):
        """  Corresponds to IDD Field `spectrum_28`

        Args:
            value (float): value for IDD Field `spectrum_28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_28`'.format(value))

        self._data["Spectrum 28"] = value

    @property
    def wavelength_29(self):
        """Get wavelength_29

        Returns:
            float: the value of `wavelength_29` or None if not set
        """
        return self._data["Wavelength 29"]

    @wavelength_29.setter
    def wavelength_29(self, value=None):
        """  Corresponds to IDD Field `wavelength_29`

        Args:
            value (float): value for IDD Field `wavelength_29`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_29`'.format(value))

        self._data["Wavelength 29"] = value

    @property
    def spectrum_29(self):
        """Get spectrum_29

        Returns:
            float: the value of `spectrum_29` or None if not set
        """
        return self._data["Spectrum 29"]

    @spectrum_29.setter
    def spectrum_29(self, value=None):
        """  Corresponds to IDD Field `spectrum_29`

        Args:
            value (float): value for IDD Field `spectrum_29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_29`'.format(value))

        self._data["Spectrum 29"] = value

    @property
    def wavelength_30(self):
        """Get wavelength_30

        Returns:
            float: the value of `wavelength_30` or None if not set
        """
        return self._data["Wavelength 30"]

    @wavelength_30.setter
    def wavelength_30(self, value=None):
        """  Corresponds to IDD Field `wavelength_30`

        Args:
            value (float): value for IDD Field `wavelength_30`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_30`'.format(value))

        self._data["Wavelength 30"] = value

    @property
    def spectrum_30(self):
        """Get spectrum_30

        Returns:
            float: the value of `spectrum_30` or None if not set
        """
        return self._data["Spectrum 30"]

    @spectrum_30.setter
    def spectrum_30(self, value=None):
        """  Corresponds to IDD Field `spectrum_30`

        Args:
            value (float): value for IDD Field `spectrum_30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_30`'.format(value))

        self._data["Spectrum 30"] = value

    @property
    def wavelength_31(self):
        """Get wavelength_31

        Returns:
            float: the value of `wavelength_31` or None if not set
        """
        return self._data["Wavelength 31"]

    @wavelength_31.setter
    def wavelength_31(self, value=None):
        """  Corresponds to IDD Field `wavelength_31`

        Args:
            value (float): value for IDD Field `wavelength_31`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_31`'.format(value))

        self._data["Wavelength 31"] = value

    @property
    def spectrum_31(self):
        """Get spectrum_31

        Returns:
            float: the value of `spectrum_31` or None if not set
        """
        return self._data["Spectrum 31"]

    @spectrum_31.setter
    def spectrum_31(self, value=None):
        """  Corresponds to IDD Field `spectrum_31`

        Args:
            value (float): value for IDD Field `spectrum_31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_31`'.format(value))

        self._data["Spectrum 31"] = value

    @property
    def wavelength_32(self):
        """Get wavelength_32

        Returns:
            float: the value of `wavelength_32` or None if not set
        """
        return self._data["Wavelength 32"]

    @wavelength_32.setter
    def wavelength_32(self, value=None):
        """  Corresponds to IDD Field `wavelength_32`

        Args:
            value (float): value for IDD Field `wavelength_32`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_32`'.format(value))

        self._data["Wavelength 32"] = value

    @property
    def spectrum_32(self):
        """Get spectrum_32

        Returns:
            float: the value of `spectrum_32` or None if not set
        """
        return self._data["Spectrum 32"]

    @spectrum_32.setter
    def spectrum_32(self, value=None):
        """  Corresponds to IDD Field `spectrum_32`

        Args:
            value (float): value for IDD Field `spectrum_32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_32`'.format(value))

        self._data["Spectrum 32"] = value

    @property
    def wavelength_33(self):
        """Get wavelength_33

        Returns:
            float: the value of `wavelength_33` or None if not set
        """
        return self._data["Wavelength 33"]

    @wavelength_33.setter
    def wavelength_33(self, value=None):
        """  Corresponds to IDD Field `wavelength_33`

        Args:
            value (float): value for IDD Field `wavelength_33`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_33`'.format(value))

        self._data["Wavelength 33"] = value

    @property
    def spectrum_33(self):
        """Get spectrum_33

        Returns:
            float: the value of `spectrum_33` or None if not set
        """
        return self._data["Spectrum 33"]

    @spectrum_33.setter
    def spectrum_33(self, value=None):
        """  Corresponds to IDD Field `spectrum_33`

        Args:
            value (float): value for IDD Field `spectrum_33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_33`'.format(value))

        self._data["Spectrum 33"] = value

    @property
    def wavelength_34(self):
        """Get wavelength_34

        Returns:
            float: the value of `wavelength_34` or None if not set
        """
        return self._data["Wavelength 34"]

    @wavelength_34.setter
    def wavelength_34(self, value=None):
        """  Corresponds to IDD Field `wavelength_34`

        Args:
            value (float): value for IDD Field `wavelength_34`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_34`'.format(value))

        self._data["Wavelength 34"] = value

    @property
    def spectrum_34(self):
        """Get spectrum_34

        Returns:
            float: the value of `spectrum_34` or None if not set
        """
        return self._data["Spectrum 34"]

    @spectrum_34.setter
    def spectrum_34(self, value=None):
        """  Corresponds to IDD Field `spectrum_34`

        Args:
            value (float): value for IDD Field `spectrum_34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_34`'.format(value))

        self._data["Spectrum 34"] = value

    @property
    def wavelength_35(self):
        """Get wavelength_35

        Returns:
            float: the value of `wavelength_35` or None if not set
        """
        return self._data["Wavelength 35"]

    @wavelength_35.setter
    def wavelength_35(self, value=None):
        """  Corresponds to IDD Field `wavelength_35`

        Args:
            value (float): value for IDD Field `wavelength_35`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_35`'.format(value))

        self._data["Wavelength 35"] = value

    @property
    def spectrum_35(self):
        """Get spectrum_35

        Returns:
            float: the value of `spectrum_35` or None if not set
        """
        return self._data["Spectrum 35"]

    @spectrum_35.setter
    def spectrum_35(self, value=None):
        """  Corresponds to IDD Field `spectrum_35`

        Args:
            value (float): value for IDD Field `spectrum_35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_35`'.format(value))

        self._data["Spectrum 35"] = value

    @property
    def wavelength_36(self):
        """Get wavelength_36

        Returns:
            float: the value of `wavelength_36` or None if not set
        """
        return self._data["Wavelength 36"]

    @wavelength_36.setter
    def wavelength_36(self, value=None):
        """  Corresponds to IDD Field `wavelength_36`

        Args:
            value (float): value for IDD Field `wavelength_36`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_36`'.format(value))

        self._data["Wavelength 36"] = value

    @property
    def spectrum_36(self):
        """Get spectrum_36

        Returns:
            float: the value of `spectrum_36` or None if not set
        """
        return self._data["Spectrum 36"]

    @spectrum_36.setter
    def spectrum_36(self, value=None):
        """  Corresponds to IDD Field `spectrum_36`

        Args:
            value (float): value for IDD Field `spectrum_36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_36`'.format(value))

        self._data["Spectrum 36"] = value

    @property
    def wavelength_37(self):
        """Get wavelength_37

        Returns:
            float: the value of `wavelength_37` or None if not set
        """
        return self._data["Wavelength 37"]

    @wavelength_37.setter
    def wavelength_37(self, value=None):
        """  Corresponds to IDD Field `wavelength_37`

        Args:
            value (float): value for IDD Field `wavelength_37`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_37`'.format(value))

        self._data["Wavelength 37"] = value

    @property
    def spectrum_37(self):
        """Get spectrum_37

        Returns:
            float: the value of `spectrum_37` or None if not set
        """
        return self._data["Spectrum 37"]

    @spectrum_37.setter
    def spectrum_37(self, value=None):
        """  Corresponds to IDD Field `spectrum_37`

        Args:
            value (float): value for IDD Field `spectrum_37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_37`'.format(value))

        self._data["Spectrum 37"] = value

    @property
    def wavelength_38(self):
        """Get wavelength_38

        Returns:
            float: the value of `wavelength_38` or None if not set
        """
        return self._data["Wavelength 38"]

    @wavelength_38.setter
    def wavelength_38(self, value=None):
        """  Corresponds to IDD Field `wavelength_38`

        Args:
            value (float): value for IDD Field `wavelength_38`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_38`'.format(value))

        self._data["Wavelength 38"] = value

    @property
    def spectrum_38(self):
        """Get spectrum_38

        Returns:
            float: the value of `spectrum_38` or None if not set
        """
        return self._data["Spectrum 38"]

    @spectrum_38.setter
    def spectrum_38(self, value=None):
        """  Corresponds to IDD Field `spectrum_38`

        Args:
            value (float): value for IDD Field `spectrum_38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_38`'.format(value))

        self._data["Spectrum 38"] = value

    @property
    def wavelength_39(self):
        """Get wavelength_39

        Returns:
            float: the value of `wavelength_39` or None if not set
        """
        return self._data["Wavelength 39"]

    @wavelength_39.setter
    def wavelength_39(self, value=None):
        """  Corresponds to IDD Field `wavelength_39`

        Args:
            value (float): value for IDD Field `wavelength_39`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_39`'.format(value))

        self._data["Wavelength 39"] = value

    @property
    def spectrum_39(self):
        """Get spectrum_39

        Returns:
            float: the value of `spectrum_39` or None if not set
        """
        return self._data["Spectrum 39"]

    @spectrum_39.setter
    def spectrum_39(self, value=None):
        """  Corresponds to IDD Field `spectrum_39`

        Args:
            value (float): value for IDD Field `spectrum_39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_39`'.format(value))

        self._data["Spectrum 39"] = value

    @property
    def wavelength_40(self):
        """Get wavelength_40

        Returns:
            float: the value of `wavelength_40` or None if not set
        """
        return self._data["Wavelength 40"]

    @wavelength_40.setter
    def wavelength_40(self, value=None):
        """  Corresponds to IDD Field `wavelength_40`

        Args:
            value (float): value for IDD Field `wavelength_40`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_40`'.format(value))

        self._data["Wavelength 40"] = value

    @property
    def spectrum_40(self):
        """Get spectrum_40

        Returns:
            float: the value of `spectrum_40` or None if not set
        """
        return self._data["Spectrum 40"]

    @spectrum_40.setter
    def spectrum_40(self, value=None):
        """  Corresponds to IDD Field `spectrum_40`

        Args:
            value (float): value for IDD Field `spectrum_40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_40`'.format(value))

        self._data["Spectrum 40"] = value

    @property
    def wavelength_41(self):
        """Get wavelength_41

        Returns:
            float: the value of `wavelength_41` or None if not set
        """
        return self._data["Wavelength 41"]

    @wavelength_41.setter
    def wavelength_41(self, value=None):
        """  Corresponds to IDD Field `wavelength_41`

        Args:
            value (float): value for IDD Field `wavelength_41`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_41`'.format(value))

        self._data["Wavelength 41"] = value

    @property
    def spectrum_41(self):
        """Get spectrum_41

        Returns:
            float: the value of `spectrum_41` or None if not set
        """
        return self._data["Spectrum 41"]

    @spectrum_41.setter
    def spectrum_41(self, value=None):
        """  Corresponds to IDD Field `spectrum_41`

        Args:
            value (float): value for IDD Field `spectrum_41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_41`'.format(value))

        self._data["Spectrum 41"] = value

    @property
    def wavelength_42(self):
        """Get wavelength_42

        Returns:
            float: the value of `wavelength_42` or None if not set
        """
        return self._data["Wavelength 42"]

    @wavelength_42.setter
    def wavelength_42(self, value=None):
        """  Corresponds to IDD Field `wavelength_42`

        Args:
            value (float): value for IDD Field `wavelength_42`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_42`'.format(value))

        self._data["Wavelength 42"] = value

    @property
    def spectrum_42(self):
        """Get spectrum_42

        Returns:
            float: the value of `spectrum_42` or None if not set
        """
        return self._data["Spectrum 42"]

    @spectrum_42.setter
    def spectrum_42(self, value=None):
        """  Corresponds to IDD Field `spectrum_42`

        Args:
            value (float): value for IDD Field `spectrum_42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_42`'.format(value))

        self._data["Spectrum 42"] = value

    @property
    def wavelength_43(self):
        """Get wavelength_43

        Returns:
            float: the value of `wavelength_43` or None if not set
        """
        return self._data["Wavelength 43"]

    @wavelength_43.setter
    def wavelength_43(self, value=None):
        """  Corresponds to IDD Field `wavelength_43`

        Args:
            value (float): value for IDD Field `wavelength_43`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_43`'.format(value))

        self._data["Wavelength 43"] = value

    @property
    def spectrum_43(self):
        """Get spectrum_43

        Returns:
            float: the value of `spectrum_43` or None if not set
        """
        return self._data["Spectrum 43"]

    @spectrum_43.setter
    def spectrum_43(self, value=None):
        """  Corresponds to IDD Field `spectrum_43`

        Args:
            value (float): value for IDD Field `spectrum_43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_43`'.format(value))

        self._data["Spectrum 43"] = value

    @property
    def wavelength_44(self):
        """Get wavelength_44

        Returns:
            float: the value of `wavelength_44` or None if not set
        """
        return self._data["Wavelength 44"]

    @wavelength_44.setter
    def wavelength_44(self, value=None):
        """  Corresponds to IDD Field `wavelength_44`

        Args:
            value (float): value for IDD Field `wavelength_44`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_44`'.format(value))

        self._data["Wavelength 44"] = value

    @property
    def spectrum_44(self):
        """Get spectrum_44

        Returns:
            float: the value of `spectrum_44` or None if not set
        """
        return self._data["Spectrum 44"]

    @spectrum_44.setter
    def spectrum_44(self, value=None):
        """  Corresponds to IDD Field `spectrum_44`

        Args:
            value (float): value for IDD Field `spectrum_44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_44`'.format(value))

        self._data["Spectrum 44"] = value

    @property
    def wavelength_45(self):
        """Get wavelength_45

        Returns:
            float: the value of `wavelength_45` or None if not set
        """
        return self._data["Wavelength 45"]

    @wavelength_45.setter
    def wavelength_45(self, value=None):
        """  Corresponds to IDD Field `wavelength_45`

        Args:
            value (float): value for IDD Field `wavelength_45`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_45`'.format(value))

        self._data["Wavelength 45"] = value

    @property
    def spectrum_45(self):
        """Get spectrum_45

        Returns:
            float: the value of `spectrum_45` or None if not set
        """
        return self._data["Spectrum 45"]

    @spectrum_45.setter
    def spectrum_45(self, value=None):
        """  Corresponds to IDD Field `spectrum_45`

        Args:
            value (float): value for IDD Field `spectrum_45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_45`'.format(value))

        self._data["Spectrum 45"] = value

    @property
    def wavelength_46(self):
        """Get wavelength_46

        Returns:
            float: the value of `wavelength_46` or None if not set
        """
        return self._data["Wavelength 46"]

    @wavelength_46.setter
    def wavelength_46(self, value=None):
        """  Corresponds to IDD Field `wavelength_46`

        Args:
            value (float): value for IDD Field `wavelength_46`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_46`'.format(value))

        self._data["Wavelength 46"] = value

    @property
    def spectrum_46(self):
        """Get spectrum_46

        Returns:
            float: the value of `spectrum_46` or None if not set
        """
        return self._data["Spectrum 46"]

    @spectrum_46.setter
    def spectrum_46(self, value=None):
        """  Corresponds to IDD Field `spectrum_46`

        Args:
            value (float): value for IDD Field `spectrum_46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_46`'.format(value))

        self._data["Spectrum 46"] = value

    @property
    def wavelength_47(self):
        """Get wavelength_47

        Returns:
            float: the value of `wavelength_47` or None if not set
        """
        return self._data["Wavelength 47"]

    @wavelength_47.setter
    def wavelength_47(self, value=None):
        """  Corresponds to IDD Field `wavelength_47`

        Args:
            value (float): value for IDD Field `wavelength_47`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_47`'.format(value))

        self._data["Wavelength 47"] = value

    @property
    def spectrum_47(self):
        """Get spectrum_47

        Returns:
            float: the value of `spectrum_47` or None if not set
        """
        return self._data["Spectrum 47"]

    @spectrum_47.setter
    def spectrum_47(self, value=None):
        """  Corresponds to IDD Field `spectrum_47`

        Args:
            value (float): value for IDD Field `spectrum_47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_47`'.format(value))

        self._data["Spectrum 47"] = value

    @property
    def wavelength_48(self):
        """Get wavelength_48

        Returns:
            float: the value of `wavelength_48` or None if not set
        """
        return self._data["Wavelength 48"]

    @wavelength_48.setter
    def wavelength_48(self, value=None):
        """  Corresponds to IDD Field `wavelength_48`

        Args:
            value (float): value for IDD Field `wavelength_48`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_48`'.format(value))

        self._data["Wavelength 48"] = value

    @property
    def spectrum_48(self):
        """Get spectrum_48

        Returns:
            float: the value of `spectrum_48` or None if not set
        """
        return self._data["Spectrum 48"]

    @spectrum_48.setter
    def spectrum_48(self, value=None):
        """  Corresponds to IDD Field `spectrum_48`

        Args:
            value (float): value for IDD Field `spectrum_48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_48`'.format(value))

        self._data["Spectrum 48"] = value

    @property
    def wavelength_49(self):
        """Get wavelength_49

        Returns:
            float: the value of `wavelength_49` or None if not set
        """
        return self._data["Wavelength 49"]

    @wavelength_49.setter
    def wavelength_49(self, value=None):
        """  Corresponds to IDD Field `wavelength_49`

        Args:
            value (float): value for IDD Field `wavelength_49`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_49`'.format(value))

        self._data["Wavelength 49"] = value

    @property
    def spectrum_49(self):
        """Get spectrum_49

        Returns:
            float: the value of `spectrum_49` or None if not set
        """
        return self._data["Spectrum 49"]

    @spectrum_49.setter
    def spectrum_49(self, value=None):
        """  Corresponds to IDD Field `spectrum_49`

        Args:
            value (float): value for IDD Field `spectrum_49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_49`'.format(value))

        self._data["Spectrum 49"] = value

    @property
    def wavelength_50(self):
        """Get wavelength_50

        Returns:
            float: the value of `wavelength_50` or None if not set
        """
        return self._data["Wavelength 50"]

    @wavelength_50.setter
    def wavelength_50(self, value=None):
        """  Corresponds to IDD Field `wavelength_50`

        Args:
            value (float): value for IDD Field `wavelength_50`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_50`'.format(value))

        self._data["Wavelength 50"] = value

    @property
    def spectrum_50(self):
        """Get spectrum_50

        Returns:
            float: the value of `spectrum_50` or None if not set
        """
        return self._data["Spectrum 50"]

    @spectrum_50.setter
    def spectrum_50(self, value=None):
        """  Corresponds to IDD Field `spectrum_50`

        Args:
            value (float): value for IDD Field `spectrum_50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_50`'.format(value))

        self._data["Spectrum 50"] = value

    @property
    def wavelength_51(self):
        """Get wavelength_51

        Returns:
            float: the value of `wavelength_51` or None if not set
        """
        return self._data["Wavelength 51"]

    @wavelength_51.setter
    def wavelength_51(self, value=None):
        """  Corresponds to IDD Field `wavelength_51`

        Args:
            value (float): value for IDD Field `wavelength_51`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_51`'.format(value))

        self._data["Wavelength 51"] = value

    @property
    def spectrum_51(self):
        """Get spectrum_51

        Returns:
            float: the value of `spectrum_51` or None if not set
        """
        return self._data["Spectrum 51"]

    @spectrum_51.setter
    def spectrum_51(self, value=None):
        """  Corresponds to IDD Field `spectrum_51`

        Args:
            value (float): value for IDD Field `spectrum_51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_51`'.format(value))

        self._data["Spectrum 51"] = value

    @property
    def wavelength_52(self):
        """Get wavelength_52

        Returns:
            float: the value of `wavelength_52` or None if not set
        """
        return self._data["Wavelength 52"]

    @wavelength_52.setter
    def wavelength_52(self, value=None):
        """  Corresponds to IDD Field `wavelength_52`

        Args:
            value (float): value for IDD Field `wavelength_52`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_52`'.format(value))

        self._data["Wavelength 52"] = value

    @property
    def spectrum_52(self):
        """Get spectrum_52

        Returns:
            float: the value of `spectrum_52` or None if not set
        """
        return self._data["Spectrum 52"]

    @spectrum_52.setter
    def spectrum_52(self, value=None):
        """  Corresponds to IDD Field `spectrum_52`

        Args:
            value (float): value for IDD Field `spectrum_52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_52`'.format(value))

        self._data["Spectrum 52"] = value

    @property
    def wavelength_53(self):
        """Get wavelength_53

        Returns:
            float: the value of `wavelength_53` or None if not set
        """
        return self._data["Wavelength 53"]

    @wavelength_53.setter
    def wavelength_53(self, value=None):
        """  Corresponds to IDD Field `wavelength_53`

        Args:
            value (float): value for IDD Field `wavelength_53`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_53`'.format(value))

        self._data["Wavelength 53"] = value

    @property
    def spectrum_53(self):
        """Get spectrum_53

        Returns:
            float: the value of `spectrum_53` or None if not set
        """
        return self._data["Spectrum 53"]

    @spectrum_53.setter
    def spectrum_53(self, value=None):
        """  Corresponds to IDD Field `spectrum_53`

        Args:
            value (float): value for IDD Field `spectrum_53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_53`'.format(value))

        self._data["Spectrum 53"] = value

    @property
    def wavelength_54(self):
        """Get wavelength_54

        Returns:
            float: the value of `wavelength_54` or None if not set
        """
        return self._data["Wavelength 54"]

    @wavelength_54.setter
    def wavelength_54(self, value=None):
        """  Corresponds to IDD Field `wavelength_54`

        Args:
            value (float): value for IDD Field `wavelength_54`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_54`'.format(value))

        self._data["Wavelength 54"] = value

    @property
    def spectrum_54(self):
        """Get spectrum_54

        Returns:
            float: the value of `spectrum_54` or None if not set
        """
        return self._data["Spectrum 54"]

    @spectrum_54.setter
    def spectrum_54(self, value=None):
        """  Corresponds to IDD Field `spectrum_54`

        Args:
            value (float): value for IDD Field `spectrum_54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_54`'.format(value))

        self._data["Spectrum 54"] = value

    @property
    def wavelength_55(self):
        """Get wavelength_55

        Returns:
            float: the value of `wavelength_55` or None if not set
        """
        return self._data["Wavelength 55"]

    @wavelength_55.setter
    def wavelength_55(self, value=None):
        """  Corresponds to IDD Field `wavelength_55`

        Args:
            value (float): value for IDD Field `wavelength_55`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_55`'.format(value))

        self._data["Wavelength 55"] = value

    @property
    def spectrum_55(self):
        """Get spectrum_55

        Returns:
            float: the value of `spectrum_55` or None if not set
        """
        return self._data["Spectrum 55"]

    @spectrum_55.setter
    def spectrum_55(self, value=None):
        """  Corresponds to IDD Field `spectrum_55`

        Args:
            value (float): value for IDD Field `spectrum_55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_55`'.format(value))

        self._data["Spectrum 55"] = value

    @property
    def wavelength_56(self):
        """Get wavelength_56

        Returns:
            float: the value of `wavelength_56` or None if not set
        """
        return self._data["Wavelength 56"]

    @wavelength_56.setter
    def wavelength_56(self, value=None):
        """  Corresponds to IDD Field `wavelength_56`

        Args:
            value (float): value for IDD Field `wavelength_56`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_56`'.format(value))

        self._data["Wavelength 56"] = value

    @property
    def spectrum_56(self):
        """Get spectrum_56

        Returns:
            float: the value of `spectrum_56` or None if not set
        """
        return self._data["Spectrum 56"]

    @spectrum_56.setter
    def spectrum_56(self, value=None):
        """  Corresponds to IDD Field `spectrum_56`

        Args:
            value (float): value for IDD Field `spectrum_56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_56`'.format(value))

        self._data["Spectrum 56"] = value

    @property
    def wavelength_57(self):
        """Get wavelength_57

        Returns:
            float: the value of `wavelength_57` or None if not set
        """
        return self._data["Wavelength 57"]

    @wavelength_57.setter
    def wavelength_57(self, value=None):
        """  Corresponds to IDD Field `wavelength_57`

        Args:
            value (float): value for IDD Field `wavelength_57`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_57`'.format(value))

        self._data["Wavelength 57"] = value

    @property
    def spectrum_57(self):
        """Get spectrum_57

        Returns:
            float: the value of `spectrum_57` or None if not set
        """
        return self._data["Spectrum 57"]

    @spectrum_57.setter
    def spectrum_57(self, value=None):
        """  Corresponds to IDD Field `spectrum_57`

        Args:
            value (float): value for IDD Field `spectrum_57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_57`'.format(value))

        self._data["Spectrum 57"] = value

    @property
    def wavelength_58(self):
        """Get wavelength_58

        Returns:
            float: the value of `wavelength_58` or None if not set
        """
        return self._data["Wavelength 58"]

    @wavelength_58.setter
    def wavelength_58(self, value=None):
        """  Corresponds to IDD Field `wavelength_58`

        Args:
            value (float): value for IDD Field `wavelength_58`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_58`'.format(value))

        self._data["Wavelength 58"] = value

    @property
    def spectrum_58(self):
        """Get spectrum_58

        Returns:
            float: the value of `spectrum_58` or None if not set
        """
        return self._data["Spectrum 58"]

    @spectrum_58.setter
    def spectrum_58(self, value=None):
        """  Corresponds to IDD Field `spectrum_58`

        Args:
            value (float): value for IDD Field `spectrum_58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_58`'.format(value))

        self._data["Spectrum 58"] = value

    @property
    def wavelength_59(self):
        """Get wavelength_59

        Returns:
            float: the value of `wavelength_59` or None if not set
        """
        return self._data["Wavelength 59"]

    @wavelength_59.setter
    def wavelength_59(self, value=None):
        """  Corresponds to IDD Field `wavelength_59`

        Args:
            value (float): value for IDD Field `wavelength_59`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_59`'.format(value))

        self._data["Wavelength 59"] = value

    @property
    def spectrum_59(self):
        """Get spectrum_59

        Returns:
            float: the value of `spectrum_59` or None if not set
        """
        return self._data["Spectrum 59"]

    @spectrum_59.setter
    def spectrum_59(self, value=None):
        """  Corresponds to IDD Field `spectrum_59`

        Args:
            value (float): value for IDD Field `spectrum_59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_59`'.format(value))

        self._data["Spectrum 59"] = value

    @property
    def wavelength_60(self):
        """Get wavelength_60

        Returns:
            float: the value of `wavelength_60` or None if not set
        """
        return self._data["Wavelength 60"]

    @wavelength_60.setter
    def wavelength_60(self, value=None):
        """  Corresponds to IDD Field `wavelength_60`

        Args:
            value (float): value for IDD Field `wavelength_60`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_60`'.format(value))

        self._data["Wavelength 60"] = value

    @property
    def spectrum_60(self):
        """Get spectrum_60

        Returns:
            float: the value of `spectrum_60` or None if not set
        """
        return self._data["Spectrum 60"]

    @spectrum_60.setter
    def spectrum_60(self, value=None):
        """  Corresponds to IDD Field `spectrum_60`

        Args:
            value (float): value for IDD Field `spectrum_60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_60`'.format(value))

        self._data["Spectrum 60"] = value

    @property
    def wavelength_61(self):
        """Get wavelength_61

        Returns:
            float: the value of `wavelength_61` or None if not set
        """
        return self._data["Wavelength 61"]

    @wavelength_61.setter
    def wavelength_61(self, value=None):
        """  Corresponds to IDD Field `wavelength_61`

        Args:
            value (float): value for IDD Field `wavelength_61`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_61`'.format(value))

        self._data["Wavelength 61"] = value

    @property
    def spectrum_61(self):
        """Get spectrum_61

        Returns:
            float: the value of `spectrum_61` or None if not set
        """
        return self._data["Spectrum 61"]

    @spectrum_61.setter
    def spectrum_61(self, value=None):
        """  Corresponds to IDD Field `spectrum_61`

        Args:
            value (float): value for IDD Field `spectrum_61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_61`'.format(value))

        self._data["Spectrum 61"] = value

    @property
    def wavelength_62(self):
        """Get wavelength_62

        Returns:
            float: the value of `wavelength_62` or None if not set
        """
        return self._data["Wavelength 62"]

    @wavelength_62.setter
    def wavelength_62(self, value=None):
        """  Corresponds to IDD Field `wavelength_62`

        Args:
            value (float): value for IDD Field `wavelength_62`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_62`'.format(value))

        self._data["Wavelength 62"] = value

    @property
    def spectrum_62(self):
        """Get spectrum_62

        Returns:
            float: the value of `spectrum_62` or None if not set
        """
        return self._data["Spectrum 62"]

    @spectrum_62.setter
    def spectrum_62(self, value=None):
        """  Corresponds to IDD Field `spectrum_62`

        Args:
            value (float): value for IDD Field `spectrum_62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_62`'.format(value))

        self._data["Spectrum 62"] = value

    @property
    def wavelength_63(self):
        """Get wavelength_63

        Returns:
            float: the value of `wavelength_63` or None if not set
        """
        return self._data["Wavelength 63"]

    @wavelength_63.setter
    def wavelength_63(self, value=None):
        """  Corresponds to IDD Field `wavelength_63`

        Args:
            value (float): value for IDD Field `wavelength_63`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_63`'.format(value))

        self._data["Wavelength 63"] = value

    @property
    def spectrum_63(self):
        """Get spectrum_63

        Returns:
            float: the value of `spectrum_63` or None if not set
        """
        return self._data["Spectrum 63"]

    @spectrum_63.setter
    def spectrum_63(self, value=None):
        """  Corresponds to IDD Field `spectrum_63`

        Args:
            value (float): value for IDD Field `spectrum_63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_63`'.format(value))

        self._data["Spectrum 63"] = value

    @property
    def wavelength_64(self):
        """Get wavelength_64

        Returns:
            float: the value of `wavelength_64` or None if not set
        """
        return self._data["Wavelength 64"]

    @wavelength_64.setter
    def wavelength_64(self, value=None):
        """  Corresponds to IDD Field `wavelength_64`

        Args:
            value (float): value for IDD Field `wavelength_64`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_64`'.format(value))

        self._data["Wavelength 64"] = value

    @property
    def spectrum_64(self):
        """Get spectrum_64

        Returns:
            float: the value of `spectrum_64` or None if not set
        """
        return self._data["Spectrum 64"]

    @spectrum_64.setter
    def spectrum_64(self, value=None):
        """  Corresponds to IDD Field `spectrum_64`

        Args:
            value (float): value for IDD Field `spectrum_64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_64`'.format(value))

        self._data["Spectrum 64"] = value

    @property
    def wavelength_65(self):
        """Get wavelength_65

        Returns:
            float: the value of `wavelength_65` or None if not set
        """
        return self._data["Wavelength 65"]

    @wavelength_65.setter
    def wavelength_65(self, value=None):
        """  Corresponds to IDD Field `wavelength_65`

        Args:
            value (float): value for IDD Field `wavelength_65`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_65`'.format(value))

        self._data["Wavelength 65"] = value

    @property
    def spectrum_65(self):
        """Get spectrum_65

        Returns:
            float: the value of `spectrum_65` or None if not set
        """
        return self._data["Spectrum 65"]

    @spectrum_65.setter
    def spectrum_65(self, value=None):
        """  Corresponds to IDD Field `spectrum_65`

        Args:
            value (float): value for IDD Field `spectrum_65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_65`'.format(value))

        self._data["Spectrum 65"] = value

    @property
    def wavelength_66(self):
        """Get wavelength_66

        Returns:
            float: the value of `wavelength_66` or None if not set
        """
        return self._data["Wavelength 66"]

    @wavelength_66.setter
    def wavelength_66(self, value=None):
        """  Corresponds to IDD Field `wavelength_66`

        Args:
            value (float): value for IDD Field `wavelength_66`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_66`'.format(value))

        self._data["Wavelength 66"] = value

    @property
    def spectrum_66(self):
        """Get spectrum_66

        Returns:
            float: the value of `spectrum_66` or None if not set
        """
        return self._data["Spectrum 66"]

    @spectrum_66.setter
    def spectrum_66(self, value=None):
        """  Corresponds to IDD Field `spectrum_66`

        Args:
            value (float): value for IDD Field `spectrum_66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_66`'.format(value))

        self._data["Spectrum 66"] = value

    @property
    def wavelength_67(self):
        """Get wavelength_67

        Returns:
            float: the value of `wavelength_67` or None if not set
        """
        return self._data["Wavelength 67"]

    @wavelength_67.setter
    def wavelength_67(self, value=None):
        """  Corresponds to IDD Field `wavelength_67`

        Args:
            value (float): value for IDD Field `wavelength_67`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_67`'.format(value))

        self._data["Wavelength 67"] = value

    @property
    def spectrum_67(self):
        """Get spectrum_67

        Returns:
            float: the value of `spectrum_67` or None if not set
        """
        return self._data["Spectrum 67"]

    @spectrum_67.setter
    def spectrum_67(self, value=None):
        """  Corresponds to IDD Field `spectrum_67`

        Args:
            value (float): value for IDD Field `spectrum_67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_67`'.format(value))

        self._data["Spectrum 67"] = value

    @property
    def wavelength_68(self):
        """Get wavelength_68

        Returns:
            float: the value of `wavelength_68` or None if not set
        """
        return self._data["Wavelength 68"]

    @wavelength_68.setter
    def wavelength_68(self, value=None):
        """  Corresponds to IDD Field `wavelength_68`

        Args:
            value (float): value for IDD Field `wavelength_68`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_68`'.format(value))

        self._data["Wavelength 68"] = value

    @property
    def spectrum_68(self):
        """Get spectrum_68

        Returns:
            float: the value of `spectrum_68` or None if not set
        """
        return self._data["Spectrum 68"]

    @spectrum_68.setter
    def spectrum_68(self, value=None):
        """  Corresponds to IDD Field `spectrum_68`

        Args:
            value (float): value for IDD Field `spectrum_68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_68`'.format(value))

        self._data["Spectrum 68"] = value

    @property
    def wavelength_69(self):
        """Get wavelength_69

        Returns:
            float: the value of `wavelength_69` or None if not set
        """
        return self._data["Wavelength 69"]

    @wavelength_69.setter
    def wavelength_69(self, value=None):
        """  Corresponds to IDD Field `wavelength_69`

        Args:
            value (float): value for IDD Field `wavelength_69`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_69`'.format(value))

        self._data["Wavelength 69"] = value

    @property
    def spectrum_69(self):
        """Get spectrum_69

        Returns:
            float: the value of `spectrum_69` or None if not set
        """
        return self._data["Spectrum 69"]

    @spectrum_69.setter
    def spectrum_69(self, value=None):
        """  Corresponds to IDD Field `spectrum_69`

        Args:
            value (float): value for IDD Field `spectrum_69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_69`'.format(value))

        self._data["Spectrum 69"] = value

    @property
    def wavelength_70(self):
        """Get wavelength_70

        Returns:
            float: the value of `wavelength_70` or None if not set
        """
        return self._data["Wavelength 70"]

    @wavelength_70.setter
    def wavelength_70(self, value=None):
        """  Corresponds to IDD Field `wavelength_70`

        Args:
            value (float): value for IDD Field `wavelength_70`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_70`'.format(value))

        self._data["Wavelength 70"] = value

    @property
    def spectrum_70(self):
        """Get spectrum_70

        Returns:
            float: the value of `spectrum_70` or None if not set
        """
        return self._data["Spectrum 70"]

    @spectrum_70.setter
    def spectrum_70(self, value=None):
        """  Corresponds to IDD Field `spectrum_70`

        Args:
            value (float): value for IDD Field `spectrum_70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_70`'.format(value))

        self._data["Spectrum 70"] = value

    @property
    def wavelength_71(self):
        """Get wavelength_71

        Returns:
            float: the value of `wavelength_71` or None if not set
        """
        return self._data["Wavelength 71"]

    @wavelength_71.setter
    def wavelength_71(self, value=None):
        """  Corresponds to IDD Field `wavelength_71`

        Args:
            value (float): value for IDD Field `wavelength_71`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_71`'.format(value))

        self._data["Wavelength 71"] = value

    @property
    def spectrum_71(self):
        """Get spectrum_71

        Returns:
            float: the value of `spectrum_71` or None if not set
        """
        return self._data["Spectrum 71"]

    @spectrum_71.setter
    def spectrum_71(self, value=None):
        """  Corresponds to IDD Field `spectrum_71`

        Args:
            value (float): value for IDD Field `spectrum_71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_71`'.format(value))

        self._data["Spectrum 71"] = value

    @property
    def wavelength_72(self):
        """Get wavelength_72

        Returns:
            float: the value of `wavelength_72` or None if not set
        """
        return self._data["Wavelength 72"]

    @wavelength_72.setter
    def wavelength_72(self, value=None):
        """  Corresponds to IDD Field `wavelength_72`

        Args:
            value (float): value for IDD Field `wavelength_72`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_72`'.format(value))

        self._data["Wavelength 72"] = value

    @property
    def spectrum_72(self):
        """Get spectrum_72

        Returns:
            float: the value of `spectrum_72` or None if not set
        """
        return self._data["Spectrum 72"]

    @spectrum_72.setter
    def spectrum_72(self, value=None):
        """  Corresponds to IDD Field `spectrum_72`

        Args:
            value (float): value for IDD Field `spectrum_72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_72`'.format(value))

        self._data["Spectrum 72"] = value

    @property
    def wavelength_73(self):
        """Get wavelength_73

        Returns:
            float: the value of `wavelength_73` or None if not set
        """
        return self._data["Wavelength 73"]

    @wavelength_73.setter
    def wavelength_73(self, value=None):
        """  Corresponds to IDD Field `wavelength_73`

        Args:
            value (float): value for IDD Field `wavelength_73`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_73`'.format(value))

        self._data["Wavelength 73"] = value

    @property
    def spectrum_73(self):
        """Get spectrum_73

        Returns:
            float: the value of `spectrum_73` or None if not set
        """
        return self._data["Spectrum 73"]

    @spectrum_73.setter
    def spectrum_73(self, value=None):
        """  Corresponds to IDD Field `spectrum_73`

        Args:
            value (float): value for IDD Field `spectrum_73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_73`'.format(value))

        self._data["Spectrum 73"] = value

    @property
    def wavelength_74(self):
        """Get wavelength_74

        Returns:
            float: the value of `wavelength_74` or None if not set
        """
        return self._data["Wavelength 74"]

    @wavelength_74.setter
    def wavelength_74(self, value=None):
        """  Corresponds to IDD Field `wavelength_74`

        Args:
            value (float): value for IDD Field `wavelength_74`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_74`'.format(value))

        self._data["Wavelength 74"] = value

    @property
    def spectrum_74(self):
        """Get spectrum_74

        Returns:
            float: the value of `spectrum_74` or None if not set
        """
        return self._data["Spectrum 74"]

    @spectrum_74.setter
    def spectrum_74(self, value=None):
        """  Corresponds to IDD Field `spectrum_74`

        Args:
            value (float): value for IDD Field `spectrum_74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_74`'.format(value))

        self._data["Spectrum 74"] = value

    @property
    def wavelength_75(self):
        """Get wavelength_75

        Returns:
            float: the value of `wavelength_75` or None if not set
        """
        return self._data["Wavelength 75"]

    @wavelength_75.setter
    def wavelength_75(self, value=None):
        """  Corresponds to IDD Field `wavelength_75`

        Args:
            value (float): value for IDD Field `wavelength_75`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_75`'.format(value))

        self._data["Wavelength 75"] = value

    @property
    def spectrum_75(self):
        """Get spectrum_75

        Returns:
            float: the value of `spectrum_75` or None if not set
        """
        return self._data["Spectrum 75"]

    @spectrum_75.setter
    def spectrum_75(self, value=None):
        """  Corresponds to IDD Field `spectrum_75`

        Args:
            value (float): value for IDD Field `spectrum_75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_75`'.format(value))

        self._data["Spectrum 75"] = value

    @property
    def wavelength_76(self):
        """Get wavelength_76

        Returns:
            float: the value of `wavelength_76` or None if not set
        """
        return self._data["Wavelength 76"]

    @wavelength_76.setter
    def wavelength_76(self, value=None):
        """  Corresponds to IDD Field `wavelength_76`

        Args:
            value (float): value for IDD Field `wavelength_76`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_76`'.format(value))

        self._data["Wavelength 76"] = value

    @property
    def spectrum_76(self):
        """Get spectrum_76

        Returns:
            float: the value of `spectrum_76` or None if not set
        """
        return self._data["Spectrum 76"]

    @spectrum_76.setter
    def spectrum_76(self, value=None):
        """  Corresponds to IDD Field `spectrum_76`

        Args:
            value (float): value for IDD Field `spectrum_76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_76`'.format(value))

        self._data["Spectrum 76"] = value

    @property
    def wavelength_77(self):
        """Get wavelength_77

        Returns:
            float: the value of `wavelength_77` or None if not set
        """
        return self._data["Wavelength 77"]

    @wavelength_77.setter
    def wavelength_77(self, value=None):
        """  Corresponds to IDD Field `wavelength_77`

        Args:
            value (float): value for IDD Field `wavelength_77`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_77`'.format(value))

        self._data["Wavelength 77"] = value

    @property
    def spectrum_77(self):
        """Get spectrum_77

        Returns:
            float: the value of `spectrum_77` or None if not set
        """
        return self._data["Spectrum 77"]

    @spectrum_77.setter
    def spectrum_77(self, value=None):
        """  Corresponds to IDD Field `spectrum_77`

        Args:
            value (float): value for IDD Field `spectrum_77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_77`'.format(value))

        self._data["Spectrum 77"] = value

    @property
    def wavelength_78(self):
        """Get wavelength_78

        Returns:
            float: the value of `wavelength_78` or None if not set
        """
        return self._data["Wavelength 78"]

    @wavelength_78.setter
    def wavelength_78(self, value=None):
        """  Corresponds to IDD Field `wavelength_78`

        Args:
            value (float): value for IDD Field `wavelength_78`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_78`'.format(value))

        self._data["Wavelength 78"] = value

    @property
    def spectrum_78(self):
        """Get spectrum_78

        Returns:
            float: the value of `spectrum_78` or None if not set
        """
        return self._data["Spectrum 78"]

    @spectrum_78.setter
    def spectrum_78(self, value=None):
        """  Corresponds to IDD Field `spectrum_78`

        Args:
            value (float): value for IDD Field `spectrum_78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_78`'.format(value))

        self._data["Spectrum 78"] = value

    @property
    def wavelength_79(self):
        """Get wavelength_79

        Returns:
            float: the value of `wavelength_79` or None if not set
        """
        return self._data["Wavelength 79"]

    @wavelength_79.setter
    def wavelength_79(self, value=None):
        """  Corresponds to IDD Field `wavelength_79`

        Args:
            value (float): value for IDD Field `wavelength_79`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_79`'.format(value))

        self._data["Wavelength 79"] = value

    @property
    def spectrum_79(self):
        """Get spectrum_79

        Returns:
            float: the value of `spectrum_79` or None if not set
        """
        return self._data["Spectrum 79"]

    @spectrum_79.setter
    def spectrum_79(self, value=None):
        """  Corresponds to IDD Field `spectrum_79`

        Args:
            value (float): value for IDD Field `spectrum_79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_79`'.format(value))

        self._data["Spectrum 79"] = value

    @property
    def wavelength_80(self):
        """Get wavelength_80

        Returns:
            float: the value of `wavelength_80` or None if not set
        """
        return self._data["Wavelength 80"]

    @wavelength_80.setter
    def wavelength_80(self, value=None):
        """  Corresponds to IDD Field `wavelength_80`

        Args:
            value (float): value for IDD Field `wavelength_80`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_80`'.format(value))

        self._data["Wavelength 80"] = value

    @property
    def spectrum_80(self):
        """Get spectrum_80

        Returns:
            float: the value of `spectrum_80` or None if not set
        """
        return self._data["Spectrum 80"]

    @spectrum_80.setter
    def spectrum_80(self, value=None):
        """  Corresponds to IDD Field `spectrum_80`

        Args:
            value (float): value for IDD Field `spectrum_80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_80`'.format(value))

        self._data["Spectrum 80"] = value

    @property
    def wavelength_81(self):
        """Get wavelength_81

        Returns:
            float: the value of `wavelength_81` or None if not set
        """
        return self._data["Wavelength 81"]

    @wavelength_81.setter
    def wavelength_81(self, value=None):
        """  Corresponds to IDD Field `wavelength_81`

        Args:
            value (float): value for IDD Field `wavelength_81`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_81`'.format(value))

        self._data["Wavelength 81"] = value

    @property
    def spectrum_81(self):
        """Get spectrum_81

        Returns:
            float: the value of `spectrum_81` or None if not set
        """
        return self._data["Spectrum 81"]

    @spectrum_81.setter
    def spectrum_81(self, value=None):
        """  Corresponds to IDD Field `spectrum_81`

        Args:
            value (float): value for IDD Field `spectrum_81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_81`'.format(value))

        self._data["Spectrum 81"] = value

    @property
    def wavelength_82(self):
        """Get wavelength_82

        Returns:
            float: the value of `wavelength_82` or None if not set
        """
        return self._data["Wavelength 82"]

    @wavelength_82.setter
    def wavelength_82(self, value=None):
        """  Corresponds to IDD Field `wavelength_82`

        Args:
            value (float): value for IDD Field `wavelength_82`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_82`'.format(value))

        self._data["Wavelength 82"] = value

    @property
    def spectrum_82(self):
        """Get spectrum_82

        Returns:
            float: the value of `spectrum_82` or None if not set
        """
        return self._data["Spectrum 82"]

    @spectrum_82.setter
    def spectrum_82(self, value=None):
        """  Corresponds to IDD Field `spectrum_82`

        Args:
            value (float): value for IDD Field `spectrum_82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_82`'.format(value))

        self._data["Spectrum 82"] = value

    @property
    def wavelength_83(self):
        """Get wavelength_83

        Returns:
            float: the value of `wavelength_83` or None if not set
        """
        return self._data["Wavelength 83"]

    @wavelength_83.setter
    def wavelength_83(self, value=None):
        """  Corresponds to IDD Field `wavelength_83`

        Args:
            value (float): value for IDD Field `wavelength_83`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_83`'.format(value))

        self._data["Wavelength 83"] = value

    @property
    def spectrum_83(self):
        """Get spectrum_83

        Returns:
            float: the value of `spectrum_83` or None if not set
        """
        return self._data["Spectrum 83"]

    @spectrum_83.setter
    def spectrum_83(self, value=None):
        """  Corresponds to IDD Field `spectrum_83`

        Args:
            value (float): value for IDD Field `spectrum_83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_83`'.format(value))

        self._data["Spectrum 83"] = value

    @property
    def wavelength_84(self):
        """Get wavelength_84

        Returns:
            float: the value of `wavelength_84` or None if not set
        """
        return self._data["Wavelength 84"]

    @wavelength_84.setter
    def wavelength_84(self, value=None):
        """  Corresponds to IDD Field `wavelength_84`

        Args:
            value (float): value for IDD Field `wavelength_84`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_84`'.format(value))

        self._data["Wavelength 84"] = value

    @property
    def spectrum_84(self):
        """Get spectrum_84

        Returns:
            float: the value of `spectrum_84` or None if not set
        """
        return self._data["Spectrum 84"]

    @spectrum_84.setter
    def spectrum_84(self, value=None):
        """  Corresponds to IDD Field `spectrum_84`

        Args:
            value (float): value for IDD Field `spectrum_84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_84`'.format(value))

        self._data["Spectrum 84"] = value

    @property
    def wavelength_85(self):
        """Get wavelength_85

        Returns:
            float: the value of `wavelength_85` or None if not set
        """
        return self._data["Wavelength 85"]

    @wavelength_85.setter
    def wavelength_85(self, value=None):
        """  Corresponds to IDD Field `wavelength_85`

        Args:
            value (float): value for IDD Field `wavelength_85`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_85`'.format(value))

        self._data["Wavelength 85"] = value

    @property
    def spectrum_85(self):
        """Get spectrum_85

        Returns:
            float: the value of `spectrum_85` or None if not set
        """
        return self._data["Spectrum 85"]

    @spectrum_85.setter
    def spectrum_85(self, value=None):
        """  Corresponds to IDD Field `spectrum_85`

        Args:
            value (float): value for IDD Field `spectrum_85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_85`'.format(value))

        self._data["Spectrum 85"] = value

    @property
    def wavelength_86(self):
        """Get wavelength_86

        Returns:
            float: the value of `wavelength_86` or None if not set
        """
        return self._data["Wavelength 86"]

    @wavelength_86.setter
    def wavelength_86(self, value=None):
        """  Corresponds to IDD Field `wavelength_86`

        Args:
            value (float): value for IDD Field `wavelength_86`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_86`'.format(value))

        self._data["Wavelength 86"] = value

    @property
    def spectrum_86(self):
        """Get spectrum_86

        Returns:
            float: the value of `spectrum_86` or None if not set
        """
        return self._data["Spectrum 86"]

    @spectrum_86.setter
    def spectrum_86(self, value=None):
        """  Corresponds to IDD Field `spectrum_86`

        Args:
            value (float): value for IDD Field `spectrum_86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_86`'.format(value))

        self._data["Spectrum 86"] = value

    @property
    def wavelength_87(self):
        """Get wavelength_87

        Returns:
            float: the value of `wavelength_87` or None if not set
        """
        return self._data["Wavelength 87"]

    @wavelength_87.setter
    def wavelength_87(self, value=None):
        """  Corresponds to IDD Field `wavelength_87`

        Args:
            value (float): value for IDD Field `wavelength_87`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_87`'.format(value))

        self._data["Wavelength 87"] = value

    @property
    def spectrum_87(self):
        """Get spectrum_87

        Returns:
            float: the value of `spectrum_87` or None if not set
        """
        return self._data["Spectrum 87"]

    @spectrum_87.setter
    def spectrum_87(self, value=None):
        """  Corresponds to IDD Field `spectrum_87`

        Args:
            value (float): value for IDD Field `spectrum_87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_87`'.format(value))

        self._data["Spectrum 87"] = value

    @property
    def wavelength_88(self):
        """Get wavelength_88

        Returns:
            float: the value of `wavelength_88` or None if not set
        """
        return self._data["Wavelength 88"]

    @wavelength_88.setter
    def wavelength_88(self, value=None):
        """  Corresponds to IDD Field `wavelength_88`

        Args:
            value (float): value for IDD Field `wavelength_88`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_88`'.format(value))

        self._data["Wavelength 88"] = value

    @property
    def spectrum_88(self):
        """Get spectrum_88

        Returns:
            float: the value of `spectrum_88` or None if not set
        """
        return self._data["Spectrum 88"]

    @spectrum_88.setter
    def spectrum_88(self, value=None):
        """  Corresponds to IDD Field `spectrum_88`

        Args:
            value (float): value for IDD Field `spectrum_88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_88`'.format(value))

        self._data["Spectrum 88"] = value

    @property
    def wavelength_89(self):
        """Get wavelength_89

        Returns:
            float: the value of `wavelength_89` or None if not set
        """
        return self._data["Wavelength 89"]

    @wavelength_89.setter
    def wavelength_89(self, value=None):
        """  Corresponds to IDD Field `wavelength_89`

        Args:
            value (float): value for IDD Field `wavelength_89`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_89`'.format(value))

        self._data["Wavelength 89"] = value

    @property
    def spectrum_89(self):
        """Get spectrum_89

        Returns:
            float: the value of `spectrum_89` or None if not set
        """
        return self._data["Spectrum 89"]

    @spectrum_89.setter
    def spectrum_89(self, value=None):
        """  Corresponds to IDD Field `spectrum_89`

        Args:
            value (float): value for IDD Field `spectrum_89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_89`'.format(value))

        self._data["Spectrum 89"] = value

    @property
    def wavelength_90(self):
        """Get wavelength_90

        Returns:
            float: the value of `wavelength_90` or None if not set
        """
        return self._data["Wavelength 90"]

    @wavelength_90.setter
    def wavelength_90(self, value=None):
        """  Corresponds to IDD Field `wavelength_90`

        Args:
            value (float): value for IDD Field `wavelength_90`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_90`'.format(value))

        self._data["Wavelength 90"] = value

    @property
    def spectrum_90(self):
        """Get spectrum_90

        Returns:
            float: the value of `spectrum_90` or None if not set
        """
        return self._data["Spectrum 90"]

    @spectrum_90.setter
    def spectrum_90(self, value=None):
        """  Corresponds to IDD Field `spectrum_90`

        Args:
            value (float): value for IDD Field `spectrum_90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_90`'.format(value))

        self._data["Spectrum 90"] = value

    @property
    def wavelength_91(self):
        """Get wavelength_91

        Returns:
            float: the value of `wavelength_91` or None if not set
        """
        return self._data["Wavelength 91"]

    @wavelength_91.setter
    def wavelength_91(self, value=None):
        """  Corresponds to IDD Field `wavelength_91`

        Args:
            value (float): value for IDD Field `wavelength_91`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_91`'.format(value))

        self._data["Wavelength 91"] = value

    @property
    def spectrum_91(self):
        """Get spectrum_91

        Returns:
            float: the value of `spectrum_91` or None if not set
        """
        return self._data["Spectrum 91"]

    @spectrum_91.setter
    def spectrum_91(self, value=None):
        """  Corresponds to IDD Field `spectrum_91`

        Args:
            value (float): value for IDD Field `spectrum_91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_91`'.format(value))

        self._data["Spectrum 91"] = value

    @property
    def wavelength_92(self):
        """Get wavelength_92

        Returns:
            float: the value of `wavelength_92` or None if not set
        """
        return self._data["Wavelength 92"]

    @wavelength_92.setter
    def wavelength_92(self, value=None):
        """  Corresponds to IDD Field `wavelength_92`

        Args:
            value (float): value for IDD Field `wavelength_92`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_92`'.format(value))

        self._data["Wavelength 92"] = value

    @property
    def spectrum_92(self):
        """Get spectrum_92

        Returns:
            float: the value of `spectrum_92` or None if not set
        """
        return self._data["Spectrum 92"]

    @spectrum_92.setter
    def spectrum_92(self, value=None):
        """  Corresponds to IDD Field `spectrum_92`

        Args:
            value (float): value for IDD Field `spectrum_92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_92`'.format(value))

        self._data["Spectrum 92"] = value

    @property
    def wavelength_93(self):
        """Get wavelength_93

        Returns:
            float: the value of `wavelength_93` or None if not set
        """
        return self._data["Wavelength 93"]

    @wavelength_93.setter
    def wavelength_93(self, value=None):
        """  Corresponds to IDD Field `wavelength_93`

        Args:
            value (float): value for IDD Field `wavelength_93`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_93`'.format(value))

        self._data["Wavelength 93"] = value

    @property
    def spectrum_93(self):
        """Get spectrum_93

        Returns:
            float: the value of `spectrum_93` or None if not set
        """
        return self._data["Spectrum 93"]

    @spectrum_93.setter
    def spectrum_93(self, value=None):
        """  Corresponds to IDD Field `spectrum_93`

        Args:
            value (float): value for IDD Field `spectrum_93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_93`'.format(value))

        self._data["Spectrum 93"] = value

    @property
    def wavelength_94(self):
        """Get wavelength_94

        Returns:
            float: the value of `wavelength_94` or None if not set
        """
        return self._data["Wavelength 94"]

    @wavelength_94.setter
    def wavelength_94(self, value=None):
        """  Corresponds to IDD Field `wavelength_94`

        Args:
            value (float): value for IDD Field `wavelength_94`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_94`'.format(value))

        self._data["Wavelength 94"] = value

    @property
    def spectrum_94(self):
        """Get spectrum_94

        Returns:
            float: the value of `spectrum_94` or None if not set
        """
        return self._data["Spectrum 94"]

    @spectrum_94.setter
    def spectrum_94(self, value=None):
        """  Corresponds to IDD Field `spectrum_94`

        Args:
            value (float): value for IDD Field `spectrum_94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_94`'.format(value))

        self._data["Spectrum 94"] = value

    @property
    def wavelength_95(self):
        """Get wavelength_95

        Returns:
            float: the value of `wavelength_95` or None if not set
        """
        return self._data["Wavelength 95"]

    @wavelength_95.setter
    def wavelength_95(self, value=None):
        """  Corresponds to IDD Field `wavelength_95`

        Args:
            value (float): value for IDD Field `wavelength_95`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_95`'.format(value))

        self._data["Wavelength 95"] = value

    @property
    def spectrum_95(self):
        """Get spectrum_95

        Returns:
            float: the value of `spectrum_95` or None if not set
        """
        return self._data["Spectrum 95"]

    @spectrum_95.setter
    def spectrum_95(self, value=None):
        """  Corresponds to IDD Field `spectrum_95`

        Args:
            value (float): value for IDD Field `spectrum_95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_95`'.format(value))

        self._data["Spectrum 95"] = value

    @property
    def wavelength_96(self):
        """Get wavelength_96

        Returns:
            float: the value of `wavelength_96` or None if not set
        """
        return self._data["Wavelength 96"]

    @wavelength_96.setter
    def wavelength_96(self, value=None):
        """  Corresponds to IDD Field `wavelength_96`

        Args:
            value (float): value for IDD Field `wavelength_96`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_96`'.format(value))

        self._data["Wavelength 96"] = value

    @property
    def spectrum_96(self):
        """Get spectrum_96

        Returns:
            float: the value of `spectrum_96` or None if not set
        """
        return self._data["Spectrum 96"]

    @spectrum_96.setter
    def spectrum_96(self, value=None):
        """  Corresponds to IDD Field `spectrum_96`

        Args:
            value (float): value for IDD Field `spectrum_96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_96`'.format(value))

        self._data["Spectrum 96"] = value

    @property
    def wavelength_97(self):
        """Get wavelength_97

        Returns:
            float: the value of `wavelength_97` or None if not set
        """
        return self._data["Wavelength 97"]

    @wavelength_97.setter
    def wavelength_97(self, value=None):
        """  Corresponds to IDD Field `wavelength_97`

        Args:
            value (float): value for IDD Field `wavelength_97`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_97`'.format(value))

        self._data["Wavelength 97"] = value

    @property
    def spectrum_97(self):
        """Get spectrum_97

        Returns:
            float: the value of `spectrum_97` or None if not set
        """
        return self._data["Spectrum 97"]

    @spectrum_97.setter
    def spectrum_97(self, value=None):
        """  Corresponds to IDD Field `spectrum_97`

        Args:
            value (float): value for IDD Field `spectrum_97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_97`'.format(value))

        self._data["Spectrum 97"] = value

    @property
    def wavelength_98(self):
        """Get wavelength_98

        Returns:
            float: the value of `wavelength_98` or None if not set
        """
        return self._data["Wavelength 98"]

    @wavelength_98.setter
    def wavelength_98(self, value=None):
        """  Corresponds to IDD Field `wavelength_98`

        Args:
            value (float): value for IDD Field `wavelength_98`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_98`'.format(value))

        self._data["Wavelength 98"] = value

    @property
    def spectrum_98(self):
        """Get spectrum_98

        Returns:
            float: the value of `spectrum_98` or None if not set
        """
        return self._data["Spectrum 98"]

    @spectrum_98.setter
    def spectrum_98(self, value=None):
        """  Corresponds to IDD Field `spectrum_98`

        Args:
            value (float): value for IDD Field `spectrum_98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_98`'.format(value))

        self._data["Spectrum 98"] = value

    @property
    def wavelength_99(self):
        """Get wavelength_99

        Returns:
            float: the value of `wavelength_99` or None if not set
        """
        return self._data["Wavelength 99"]

    @wavelength_99.setter
    def wavelength_99(self, value=None):
        """  Corresponds to IDD Field `wavelength_99`

        Args:
            value (float): value for IDD Field `wavelength_99`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_99`'.format(value))

        self._data["Wavelength 99"] = value

    @property
    def spectrum_99(self):
        """Get spectrum_99

        Returns:
            float: the value of `spectrum_99` or None if not set
        """
        return self._data["Spectrum 99"]

    @spectrum_99.setter
    def spectrum_99(self, value=None):
        """  Corresponds to IDD Field `spectrum_99`

        Args:
            value (float): value for IDD Field `spectrum_99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_99`'.format(value))

        self._data["Spectrum 99"] = value

    @property
    def wavelength_100(self):
        """Get wavelength_100

        Returns:
            float: the value of `wavelength_100` or None if not set
        """
        return self._data["Wavelength 100"]

    @wavelength_100.setter
    def wavelength_100(self, value=None):
        """  Corresponds to IDD Field `wavelength_100`

        Args:
            value (float): value for IDD Field `wavelength_100`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_100`'.format(value))

        self._data["Wavelength 100"] = value

    @property
    def spectrum_100(self):
        """Get spectrum_100

        Returns:
            float: the value of `spectrum_100` or None if not set
        """
        return self._data["Spectrum 100"]

    @spectrum_100.setter
    def spectrum_100(self, value=None):
        """  Corresponds to IDD Field `spectrum_100`

        Args:
            value (float): value for IDD Field `spectrum_100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_100`'.format(value))

        self._data["Spectrum 100"] = value

    @property
    def wavelength_101(self):
        """Get wavelength_101

        Returns:
            float: the value of `wavelength_101` or None if not set
        """
        return self._data["Wavelength 101"]

    @wavelength_101.setter
    def wavelength_101(self, value=None):
        """  Corresponds to IDD Field `wavelength_101`

        Args:
            value (float): value for IDD Field `wavelength_101`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_101`'.format(value))

        self._data["Wavelength 101"] = value

    @property
    def spectrum_101(self):
        """Get spectrum_101

        Returns:
            float: the value of `spectrum_101` or None if not set
        """
        return self._data["Spectrum 101"]

    @spectrum_101.setter
    def spectrum_101(self, value=None):
        """  Corresponds to IDD Field `spectrum_101`

        Args:
            value (float): value for IDD Field `spectrum_101`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_101`'.format(value))

        self._data["Spectrum 101"] = value

    @property
    def wavelength_102(self):
        """Get wavelength_102

        Returns:
            float: the value of `wavelength_102` or None if not set
        """
        return self._data["Wavelength 102"]

    @wavelength_102.setter
    def wavelength_102(self, value=None):
        """  Corresponds to IDD Field `wavelength_102`

        Args:
            value (float): value for IDD Field `wavelength_102`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_102`'.format(value))

        self._data["Wavelength 102"] = value

    @property
    def spectrum_102(self):
        """Get spectrum_102

        Returns:
            float: the value of `spectrum_102` or None if not set
        """
        return self._data["Spectrum 102"]

    @spectrum_102.setter
    def spectrum_102(self, value=None):
        """  Corresponds to IDD Field `spectrum_102`

        Args:
            value (float): value for IDD Field `spectrum_102`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_102`'.format(value))

        self._data["Spectrum 102"] = value

    @property
    def wavelength_103(self):
        """Get wavelength_103

        Returns:
            float: the value of `wavelength_103` or None if not set
        """
        return self._data["Wavelength 103"]

    @wavelength_103.setter
    def wavelength_103(self, value=None):
        """  Corresponds to IDD Field `wavelength_103`

        Args:
            value (float): value for IDD Field `wavelength_103`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_103`'.format(value))

        self._data["Wavelength 103"] = value

    @property
    def spectrum_103(self):
        """Get spectrum_103

        Returns:
            float: the value of `spectrum_103` or None if not set
        """
        return self._data["Spectrum 103"]

    @spectrum_103.setter
    def spectrum_103(self, value=None):
        """  Corresponds to IDD Field `spectrum_103`

        Args:
            value (float): value for IDD Field `spectrum_103`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_103`'.format(value))

        self._data["Spectrum 103"] = value

    @property
    def wavelength_104(self):
        """Get wavelength_104

        Returns:
            float: the value of `wavelength_104` or None if not set
        """
        return self._data["Wavelength 104"]

    @wavelength_104.setter
    def wavelength_104(self, value=None):
        """  Corresponds to IDD Field `wavelength_104`

        Args:
            value (float): value for IDD Field `wavelength_104`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_104`'.format(value))

        self._data["Wavelength 104"] = value

    @property
    def spectrum_104(self):
        """Get spectrum_104

        Returns:
            float: the value of `spectrum_104` or None if not set
        """
        return self._data["Spectrum 104"]

    @spectrum_104.setter
    def spectrum_104(self, value=None):
        """  Corresponds to IDD Field `spectrum_104`

        Args:
            value (float): value for IDD Field `spectrum_104`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_104`'.format(value))

        self._data["Spectrum 104"] = value

    @property
    def wavelength_105(self):
        """Get wavelength_105

        Returns:
            float: the value of `wavelength_105` or None if not set
        """
        return self._data["Wavelength 105"]

    @wavelength_105.setter
    def wavelength_105(self, value=None):
        """  Corresponds to IDD Field `wavelength_105`

        Args:
            value (float): value for IDD Field `wavelength_105`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_105`'.format(value))

        self._data["Wavelength 105"] = value

    @property
    def spectrum_105(self):
        """Get spectrum_105

        Returns:
            float: the value of `spectrum_105` or None if not set
        """
        return self._data["Spectrum 105"]

    @spectrum_105.setter
    def spectrum_105(self, value=None):
        """  Corresponds to IDD Field `spectrum_105`

        Args:
            value (float): value for IDD Field `spectrum_105`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_105`'.format(value))

        self._data["Spectrum 105"] = value

    @property
    def wavelength_106(self):
        """Get wavelength_106

        Returns:
            float: the value of `wavelength_106` or None if not set
        """
        return self._data["Wavelength 106"]

    @wavelength_106.setter
    def wavelength_106(self, value=None):
        """  Corresponds to IDD Field `wavelength_106`

        Args:
            value (float): value for IDD Field `wavelength_106`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_106`'.format(value))

        self._data["Wavelength 106"] = value

    @property
    def spectrum_106(self):
        """Get spectrum_106

        Returns:
            float: the value of `spectrum_106` or None if not set
        """
        return self._data["Spectrum 106"]

    @spectrum_106.setter
    def spectrum_106(self, value=None):
        """  Corresponds to IDD Field `spectrum_106`

        Args:
            value (float): value for IDD Field `spectrum_106`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_106`'.format(value))

        self._data["Spectrum 106"] = value

    @property
    def wavelength_107(self):
        """Get wavelength_107

        Returns:
            float: the value of `wavelength_107` or None if not set
        """
        return self._data["Wavelength 107"]

    @wavelength_107.setter
    def wavelength_107(self, value=None):
        """  Corresponds to IDD Field `wavelength_107`

        Args:
            value (float): value for IDD Field `wavelength_107`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_107`'.format(value))

        self._data["Wavelength 107"] = value

    @property
    def spectrum_107(self):
        """Get spectrum_107

        Returns:
            float: the value of `spectrum_107` or None if not set
        """
        return self._data["Spectrum 107"]

    @spectrum_107.setter
    def spectrum_107(self, value=None):
        """  Corresponds to IDD Field `spectrum_107`

        Args:
            value (float): value for IDD Field `spectrum_107`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `spectrum_107`'.format(value))

        self._data["Spectrum 107"] = value

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