from collections import OrderedDict

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RunPeriodControl:SpecialDays`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Start Date"] = None
        self._data["Duration"] = None
        self._data["Special Day Type"] = None

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
            self.start_date = None
        else:
            self.start_date = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.duration = None
        else:
            self.duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.special_day_type = None
        else:
            self.special_day_type = vals[i]
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
                Unit: days
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
            vals = set()
            vals.add("Holiday")
            vals.add("SummerDesignDay")
            vals.add("WinterDesignDay")
            vals.add("CustomDay1")
            vals.add("CustomDay2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `special_day_type`'.format(value))

        self._data["Special Day Type"] = value

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
        out.append(self._to_str(self.start_date))
        out.append(self._to_str(self.duration))
        out.append(self._to_str(self.special_day_type))
        return ",".join(out)

class RunPeriodControlDaylightSavingTime(object):
    """ Corresponds to IDD object `RunPeriodControl:DaylightSavingTime`
        This object sets up the daylight saving time period for any RunPeriod.
        Ignores any daylight saving time period on the weather file and uses this definition.
        These are not used with SizingPeriod:DesignDay objects.
        Use with SizingPeriod:WeatherFileDays object can be controlled in that object.
    """
    internal_name = "RunPeriodControl:DaylightSavingTime"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RunPeriodControl:DaylightSavingTime`
        """
        self._data = OrderedDict()
        self._data["Start Date"] = None
        self._data["End Date"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.start_date = None
        else:
            self.start_date = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.end_date = None
        else:
            self.end_date = vals[i]
        i += 1

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

        self._data["End Date"] = value

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
        out.append(self._to_str(self.start_date))
        out.append(self._to_str(self.end_date))
        return ",".join(out)