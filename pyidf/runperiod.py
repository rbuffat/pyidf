from collections import OrderedDict

class RunPeriod(object):
    """ Corresponds to IDD object `RunPeriod`
        Specified a range of dates and other parameters for a weather file simulation.
        Multiple run periods may be input, but they may not overlap.
    """
    internal_name = "RunPeriod"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RunPeriod`
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
            self.use_weather_file_holidays_and_special_days = None
        else:
            self.use_weather_file_holidays_and_special_days = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.apply_weekend_holiday_rule = None
        else:
            self.apply_weekend_holiday_rule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_rain_indicators = None
        else:
            self.use_weather_file_rain_indicators = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_snow_indicators = None
        else:
            self.use_weather_file_snow_indicators = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_times_runperiod_to_be_repeated = None
        else:
            self.number_of_times_runperiod_to_be_repeated = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.increment_day_of_week_on_repeat = None
        else:
            self.increment_day_of_week_on_repeat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.start_year = None
        else:
            self.start_year = vals[i]
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
            vals = set()
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("UseWeatherFile")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `day_of_week_for_start_day`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_holidays_and_special_days`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_daylight_saving_period`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `apply_weekend_holiday_rule`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_rain_indicators`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_snow_indicators`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `increment_day_of_week_on_repeat`'.format(value))

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
        out.append(self._to_str(self.use_weather_file_holidays_and_special_days))
        out.append(self._to_str(self.use_weather_file_daylight_saving_period))
        out.append(self._to_str(self.apply_weekend_holiday_rule))
        out.append(self._to_str(self.use_weather_file_rain_indicators))
        out.append(self._to_str(self.use_weather_file_snow_indicators))
        out.append(self._to_str(self.number_of_times_runperiod_to_be_repeated))
        out.append(self._to_str(self.increment_day_of_week_on_repeat))
        out.append(self._to_str(self.start_year))
        return ",".join(out)

class RunPeriodCustomRange(object):
    """ Corresponds to IDD object `RunPeriod:CustomRange`
        run simulation for a custom created weather file
    """
    internal_name = "RunPeriod:CustomRange"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RunPeriod:CustomRange`
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
            self.begin_year = None
        else:
            self.begin_year = vals[i]
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
            self.end_year = None
        else:
            self.end_year = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day_of_week_for_start_day = None
        else:
            self.day_of_week_for_start_day = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_holidays_and_special_days = None
        else:
            self.use_weather_file_holidays_and_special_days = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_daylight_saving_period = None
        else:
            self.use_weather_file_daylight_saving_period = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.apply_weekend_holiday_rule = None
        else:
            self.apply_weekend_holiday_rule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_rain_indicators = None
        else:
            self.use_weather_file_rain_indicators = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_weather_file_snow_indicators = None
        else:
            self.use_weather_file_snow_indicators = vals[i]
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
            vals = set()
            vals.add("Sunday")
            vals.add("Monday")
            vals.add("Tuesday")
            vals.add("Wednesday")
            vals.add("Thursday")
            vals.add("Friday")
            vals.add("Saturday")
            vals.add("UseWeatherFile")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `day_of_week_for_start_day`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_holidays_and_special_days`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_daylight_saving_period`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `apply_weekend_holiday_rule`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_rain_indicators`'.format(value))

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
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_weather_file_snow_indicators`'.format(value))

        self._data["Use Weather File Snow Indicators"] = value

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
        out.append(self._to_str(self.begin_year))
        out.append(self._to_str(self.end_month))
        out.append(self._to_str(self.end_day_of_month))
        out.append(self._to_str(self.end_year))
        out.append(self._to_str(self.day_of_week_for_start_day))
        out.append(self._to_str(self.use_weather_file_holidays_and_special_days))
        out.append(self._to_str(self.use_weather_file_daylight_saving_period))
        out.append(self._to_str(self.apply_weekend_holiday_rule))
        out.append(self._to_str(self.use_weather_file_rain_indicators))
        out.append(self._to_str(self.use_weather_file_snow_indicators))
        return ",".join(out)