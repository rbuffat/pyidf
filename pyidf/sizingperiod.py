from collections import OrderedDict

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SizingPeriod:DesignDay`
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
            self.month = None
        else:
            self.month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day_of_month = None
        else:
            self.day_of_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day_type = None
        else:
            self.day_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_drybulb_temperature = None
        else:
            self.maximum_drybulb_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daily_drybulb_temperature_range = None
        else:
            self.daily_drybulb_temperature_range = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_modifier_type = None
        else:
            self.drybulb_temperature_range_modifier_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_modifier_day_schedule_name = None
        else:
            self.drybulb_temperature_range_modifier_day_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_condition_type = None
        else:
            self.humidity_condition_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_or_dewpoint_at_maximum_drybulb = None
        else:
            self.wetbulb_or_dewpoint_at_maximum_drybulb = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_condition_day_schedule_name = None
        else:
            self.humidity_condition_day_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_at_maximum_drybulb = None
        else:
            self.humidity_ratio_at_maximum_drybulb = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_at_maximum_drybulb_will_require_units_transition_ = None
        else:
            self.enthalpy_at_maximum_drybulb_will_require_units_transition_ = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daily_wetbulb_temperature_range = None
        else:
            self.daily_wetbulb_temperature_range = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.barometric_pressure = None
        else:
            self.barometric_pressure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed = None
        else:
            self.wind_speed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction = None
        else:
            self.wind_direction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rain_indicator = None
        else:
            self.rain_indicator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.snow_indicator = None
        else:
            self.snow_indicator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daylight_saving_time_indicator = None
        else:
            self.daylight_saving_time_indicator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_model_indicator = None
        else:
            self.solar_model_indicator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.beam_solar_day_schedule_name = None
        else:
            self.beam_solar_day_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_solar_day_schedule_name = None
        else:
            self.diffuse_solar_day_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = None
        else:
            self.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = None
        else:
            self.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sky_clearness = None
        else:
            self.sky_clearness = vals[i]
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
            vals = set()
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("Holiday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `day_type`'.format(value))

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
                Unit: C
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
            vals = set()
            vals.add("MultiplierSchedule")
            vals.add("DifferenceSchedule")
            vals.add("TemperatureProfileSchedule")
            vals.add("DefaultMultipliers")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drybulb_temperature_range_modifier_type`'.format(value))

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
            vals = set()
            vals.add("WetBulb")
            vals.add("DewPoint")
            vals.add("HumidityRatio")
            vals.add("Enthalpy")
            vals.add("RelativeHumiditySchedule")
            vals.add("WetBulbProfileMultiplierSchedule")
            vals.add("WetBulbProfileDifferenceSchedule")
            vals.add("WetBulbProfileDefaultMultipliers")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `humidity_condition_type`'.format(value))

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
                Unit: Pa
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
                Unit: m/s
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
                Unit: deg
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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `rain_indicator`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `snow_indicator`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `daylight_saving_time_indicator`'.format(value))

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
            vals = set()
            vals.add("ASHRAEClearSky")
            vals.add("ZhangHuang")
            vals.add("Schedule")
            vals.add("ASHRAETau")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `solar_model_indicator`'.format(value))

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
                Unit: dimensionless
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
                Unit: dimensionless
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
        out.append(self._to_str(self.month))
        out.append(self._to_str(self.day_of_month))
        out.append(self._to_str(self.day_type))
        out.append(self._to_str(self.maximum_drybulb_temperature))
        out.append(self._to_str(self.daily_drybulb_temperature_range))
        out.append(self._to_str(self.drybulb_temperature_range_modifier_type))
        out.append(self._to_str(self.drybulb_temperature_range_modifier_day_schedule_name))
        out.append(self._to_str(self.humidity_condition_type))
        out.append(self._to_str(self.wetbulb_or_dewpoint_at_maximum_drybulb))
        out.append(self._to_str(self.humidity_condition_day_schedule_name))
        out.append(self._to_str(self.humidity_ratio_at_maximum_drybulb))
        out.append(self._to_str(self.enthalpy_at_maximum_drybulb_will_require_units_transition_))
        out.append(self._to_str(self.daily_wetbulb_temperature_range))
        out.append(self._to_str(self.barometric_pressure))
        out.append(self._to_str(self.wind_speed))
        out.append(self._to_str(self.wind_direction))
        out.append(self._to_str(self.rain_indicator))
        out.append(self._to_str(self.snow_indicator))
        out.append(self._to_str(self.daylight_saving_time_indicator))
        out.append(self._to_str(self.solar_model_indicator))
        out.append(self._to_str(self.beam_solar_day_schedule_name))
        out.append(self._to_str(self.diffuse_solar_day_schedule_name))
        out.append(self._to_str(self.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub))
        out.append(self._to_str(self.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud))
        out.append(self._to_str(self.sky_clearness))
        return ",".join(out)

class SizingPeriodWeatherFileDays(object):
    """ Corresponds to IDD object `SizingPeriod:WeatherFileDays`
        Use a weather file period for design sizing calculations.
    """
    internal_name = "SizingPeriod:WeatherFileDays"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SizingPeriod:WeatherFileDays`
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
            self.begin_month = None
        else:
            self.begin_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.begin_day_of_month = None
        else:
            self.begin_day_of_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.end_month = None
        else:
            self.end_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.end_day_of_month = None
        else:
            self.end_day_of_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day_of_week_for_start_day = None
        else:
            self.day_of_week_for_start_day = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_rain_and_snow_indicators = None
        else:
            self.use_weather_file_rain_and_snow_indicators = vals[i]
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
            vals = set()
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `day_of_week_for_start_day`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_daylight_saving_period`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_rain_and_snow_indicators`'.format(value))

        self._data["Use Weather File Rain and Snow Indicators"] = value

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
        out.append(self._to_str(self.begin_month))
        out.append(self._to_str(self.begin_day_of_month))
        out.append(self._to_str(self.end_month))
        out.append(self._to_str(self.end_day_of_month))
        out.append(self._to_str(self.day_of_week_for_start_day))
        out.append(self._to_str(self.use_weather_file_daylight_saving_period))
        out.append(self._to_str(self.use_weather_file_rain_and_snow_indicators))
        return ",".join(out)

class SizingPeriodWeatherFileConditionType(object):
    """ Corresponds to IDD object `SizingPeriod:WeatherFileConditionType`
        Use a weather file period for design sizing calculations.
        EPW weather files are created with typical and extreme periods
        created heuristically from the weather file data.  For more
        details on these periods, see AuxiliaryPrograms document.
    """
    internal_name = "SizingPeriod:WeatherFileConditionType"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SizingPeriod:WeatherFileConditionType`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Period Selection"] = None
        self._data["Day of Week for Start Day"] = None
        self._data["Use Weather File Daylight Saving Period"] = None
        self._data["Use Weather File Rain and Snow Indicators"] = None

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
            self.period_selection = None
        else:
            self.period_selection = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day_of_week_for_start_day = None
        else:
            self.day_of_week_for_start_day = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_rain_and_snow_indicators = None
        else:
            self.use_weather_file_rain_and_snow_indicators = vals[i]
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
            vals = set()
            vals.add("SummerExtreme")
            vals.add("SummerTypical")
            vals.add("WinterExtreme")
            vals.add("WinterTypical")
            vals.add("AutumnTypical")
            vals.add("SpringTypical")
            vals.add("WetSeason")
            vals.add("DrySeason")
            vals.add("NoDrySeason")
            vals.add("NoWetSeason")
            vals.add("TropicalHot")
            vals.add("TropicalCold")
            vals.add("NoDrySeasonMax")
            vals.add("NoDrySeasonMin")
            vals.add("NoWetSeasonMax")
            vals.add("NoWetSeasonMin")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `period_selection`'.format(value))

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
            vals = set()
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `day_of_week_for_start_day`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_daylight_saving_period`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_rain_and_snow_indicators`'.format(value))

        self._data["Use Weather File Rain and Snow Indicators"] = value

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
        out.append(self._to_str(self.period_selection))
        out.append(self._to_str(self.day_of_week_for_start_day))
        out.append(self._to_str(self.use_weather_file_daylight_saving_period))
        out.append(self._to_str(self.use_weather_file_rain_and_snow_indicators))
        return ",".join(out)